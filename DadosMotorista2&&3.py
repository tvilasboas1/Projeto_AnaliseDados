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
    plt.figure(figsize=(10, 6))
    
    # Filtrar os dados para cada mês e plotar
    for mes in df['Mês'].unique():
        df_mes = df[df['Mês'] == mes]
        plt.plot(df_mes['DIA'], df_mes['LIQUIDO'], marker='o', label=mes)

    plt.title('Ganhos por Dia')
    plt.xlabel('Dia')
    plt.ylabel('Liquido')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Carregar os dados dos arquivos
arquivos = ['PlanilhaGanhosAppFev22.csv', 'PlanilhaGanhosAppMar22.csv']
dados = carregar_dados(arquivos)

# Exibir os primeiros dados para verificação
print(dados.head())

# Plotar os gráficos
plotar_graficos(dados)
