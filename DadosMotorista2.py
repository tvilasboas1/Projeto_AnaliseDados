import pandas as pd
import matplotlib.pyplot as plt

# Função para carregar e transformar os dados
def carregar_dados(arquivos):
    dataframes = []

    for arquivo in arquivos:
        # Carregar o arquivo CSV
        df = pd.read_csv(arquivo, sep=',', decimal=',', quotechar='"')

        # Verificar as colunas do DataFrame
        print(f"Colunas do arquivo {arquivo}: {df.columns.tolist()}")

        # A primeira coluna parece ser o mês, vamos tratá-la corretamente
        nome_mes = arquivo.split('.')[0].replace('PlanilhaGanhosApp', '')
        
        # Renomear as colunas para que 'DIA' seja a primeira coluna
        df.columns = ['DIA'] + list(df.columns[1:])
        
        # Remover a coluna 'LIQUIDO' original para evitar conflito
        if 'LIQUIDO' in df.columns:
            df = df.drop(columns=['LIQUIDO'])

        # Realizar o melt para transformar as colunas de mês em linhas
        df = df.melt(id_vars=['DIA'], var_name="Mês", value_name="LIQUIDO")
        
        # Adicionar o nome do mês
        df['Mês'] = nome_mes
        
        # Converter os valores da coluna 'LIQUIDO' para numérico
        df['LIQUIDO'] = pd.to_numeric(df['LIQUIDO'].str.replace(',', '.'), errors='coerce')
        
        dataframes.append(df)

    # Concatenar todos os DataFrames
    return pd.concat(dataframes, ignore_index=True)

# Função para plotar os gráficos
def plotar_graficos(df):
    # Verificar as colunas do DataFrame antes de plotar
    print(f"Colunas antes de plotar gráficos: {df.columns.tolist()}")
    
    # Gráfico de Linhas (como antes)
    plt.figure(figsize=(10, 6))
    for mes in df['Mês'].unique():
        df_mes = df[df['Mês'] == mes]
        plt.plot(df_mes['DIA'], df_mes['LIQUIDO'], marker='o', label=mes)
    plt.title('Ganhos por Dia - Gráfico de Linhas')
    plt.xlabel('Dia')
    plt.ylabel('Liquido')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Gráfico de Barras
    plt.figure(figsize=(10, 6))
    for mes in df['Mês'].unique():
        df_mes = df[df['Mês'] == mes]
        plt.bar(df_mes['DIA'], df_mes['LIQUIDO'], label=mes, alpha=0.6)
    plt.title('Ganhos por Dia - Gráfico de Barras')
    plt.xlabel('Dia')
    plt.ylabel('Liquido')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Gráfico de Boxplot (Distribuição dos ganhos)
    if 'LIQUIDO' in df.columns:
        plt.figure(figsize=(10, 6))
        df_box = df.groupby(['Mês', 'DIA'])['LIQUIDO'].describe()
        df_box = df_box.reset_index()
        print(f"Colunas de df_box antes do boxplot: {df_box.columns.tolist()}")
        
        # Corrigir a parte do boxplot
        plt.boxplot([df_box[df_box['Mês'] == mes]['mean'] for mes in df_box['Mês'].unique()], 
                    labels=df_box['Mês'].unique())
        plt.title('Distribuição dos Ganhos por Dia - Boxplot')
        plt.xlabel('Mês')
        plt.ylabel('Liquido')
        plt.tight_layout()
        plt.show()
    else:
        print("A coluna 'LIQUIDO' não foi encontrada, portanto o boxplot não pode ser gerado.")

# Carregar os dados dos arquivos
arquivos = ['PlanilhaGanhosAppFev22.csv', 'PlanilhaGanhosAppMar22.csv']
dados = carregar_dados(arquivos)

# Exibir os primeiros dados para verificação
print(dados.head())

# Plotar os gráficos
plotar_graficos(dados)
