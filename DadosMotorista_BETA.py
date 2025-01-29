import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob

# Configuração do estilo dos gráficos
sns.set_theme(style="whitegrid")

# Função para carregar e transformar os dados de múltiplos arquivos
def carregar_dados():
    arquivos = glob.glob('GanhosApp*.csv')
    df_total = pd.DataFrame()

    for arquivo in arquivos:
        try:
            df = pd.read_csv(arquivo, sep=',', decimal=',', thousands='.')
            
            # Renomear a primeira coluna para 'DIA' e garantir que seja numérica
            df = df.rename(columns={df.columns[0]: 'DIA'})
            df['DIA'] = pd.to_numeric(df['DIA'], errors='coerce')
            df = df.dropna(subset=['DIA']).astype({'DIA': 'int'})

            # Identificar o mês a partir do nome do arquivo
            mes = arquivo.replace('GanhosApp', '').replace('.csv', '').strip()
            df['Mês'] = mes

            # Converter os valores corretamente
            for col in ['UBER', '99POP', 'OUTROS', 'TOTAL', 'GASTOS', 'Liquido']:
                if col in df.columns:
                    df[col] = pd.to_numeric(
                        df[col].astype(str).str.replace('.', '').str.replace(',', '.'),
                        errors='coerce'
                    )

            df_total = pd.concat([df_total, df], ignore_index=True)
        except Exception as e:
            print(f"Erro ao processar o arquivo {arquivo}: {e}")

    return df_total

# Função para plotar os gráficos
def plotar_graficos(df):
    if df.empty:
        print("Nenhum dado disponível para plotar gráficos.")
        return

    # Gráfico de Linhas - Ganhos Líquidos por Dia (MANTIDO)
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='DIA', y='Liquido', hue='Mês', marker='o', palette='tab10', linewidth=2.5)

    plt.title('Ganhos Líquidos por Dia', fontsize=14, fontweight='bold')
    plt.xlabel('Dia', fontsize=12)
    plt.ylabel('Ganho Líquido (R$)', fontsize=12)
    plt.xticks(df['DIA'].unique(), rotation=45)
    plt.legend(title="Mês", fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.show()

    # Gráfico de Barras - Comparação de Ganhos por Aplicativo (VOLTOU AO ESTILO ANTIGO)
    plt.figure(figsize=(10, 6))
    
    # Definição das cores personalizadas
    cores = ['green', 'orange', 'red']
    
    # Criar o gráfico de barras com os ganhos totais por aplicativo
    df[['UBER', '99POP', 'OUTROS']].sum().plot(kind='bar', color=cores, edgecolor='black')

    plt.title('Comparação de Ganhos por Aplicativo', fontsize=14, fontweight='bold')
    plt.xlabel('Aplicativo', fontsize=12)
    plt.ylabel('Ganho Bruto (R$)', fontsize=12)
    plt.xticks(rotation=0)
    
    # Adicionando valores em cima das barras
    total_ganhos = df[['UBER', '99POP', 'OUTROS']].sum()
    for i, valor in enumerate(total_ganhos):
        plt.text(i, valor + (valor * 0.02), f'R$ {valor:,.2f}', ha='center', fontsize=10, fontweight='bold')

    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

# Carregar os dados de todos os arquivos
dados = carregar_dados()

# Exibir os primeiros dados para verificação
print(dados.head())

# Plotar os gráficos
plotar_graficos(dados)
