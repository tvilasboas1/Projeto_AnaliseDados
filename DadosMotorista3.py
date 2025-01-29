import pandas as pd
import matplotlib.pyplot as plt

# Função para carregar e transformar os dados
def carregar_dados(arquivo):
    try:
        # Carregar o arquivo CSV
        df = pd.read_csv(arquivo, sep=',', decimal=',', thousands='.')

        # Exibir o cabeçalho para verificação
        print("Cabeçalho do arquivo:", df.columns.tolist())

        # Remover a linha de total (última linha)
        df = df.iloc[:-1]

        # Renomear a primeira coluna para 'DIA'
        df = df.rename(columns={df.columns[0]: 'DIA'})

        # Adicionar o nome do mês
        df['Mês'] = 'Fev22'

        # Converter os valores para numérico
        for col in ['UBER', '99POP', 'OUTROS', 'TOTAL', 'GASTOS', 'Liquido']:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace('.', '').str.replace(',', '.'), errors='coerce')

        return df
    except Exception as e:
        print(f"Erro ao processar o arquivo {arquivo}: {e}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

# Função para plotar os gráficos
def plotar_graficos(df):
    if df.empty:
        print("Nenhum dado disponível para plotar gráficos.")
        return

    # Verificar as colunas do DataFrame antes de plotar
    print(f"Colunas antes de plotar gráficos: {df.columns.tolist()}")

    # Gráfico de Linhas (Ganhos Líquidos por Dia)
    plt.figure(figsize=(12, 6))
    plt.plot(df['DIA'], df['Liquido'], marker='o', label='Fev22', color='blue')
    plt.title('Ganhos Líquidos por Dia - Gráfico de Linhas')
    plt.xlabel('Dia')
    plt.ylabel('Ganho Líquido (R$)')
    plt.legend()
    plt.xticks(df['DIA'], rotation=45)  # Definir os ticks do eixo X como os dias
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Gráfico de Barras (Comparação de Ganhos por Aplicativo)
    plt.figure(figsize=(12, 6))
    df[['UBER', '99POP', 'OUTROS']].sum().plot(kind='bar', color=['green', 'orange', 'red'])
    plt.title('Comparação de Ganhos por Aplicativo')
    plt.xlabel('Aplicativo')
    plt.ylabel('Ganho Bruto (R$)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    # Gráfico de Boxplot (Distribuição dos Ganhos Líquidos por Dia)
    plt.figure(figsize=(12, 6))
    df.boxplot(column='Liquido', by='DIA', grid=False)
    plt.title('Distribuição dos Ganhos Líquidos por Dia')
    plt.suptitle('')  # Remover título automático
    plt.xlabel('Dia')
    plt.ylabel('Ganho Líquido (R$)')
    plt.xticks(rotation=45)  # Rotacionar os rótulos do eixo X para melhor visualização
    plt.tight_layout()
    plt.show()

# Carregar os dados do arquivo
arquivo = 'GanhosAppFev22_Beta.csv'  # Substitua pelo caminho correto do arquivo
dados = carregar_dados(arquivo)

# Exibir os primeiros dados para verificação
print(dados.head())

# Plotar os gráficos
plotar_graficos(dados)