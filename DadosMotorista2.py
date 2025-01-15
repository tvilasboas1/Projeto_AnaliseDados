import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('PlanilhaGanhosApp.csv', sep=',', decimal=',', quotechar='"')

# Converter a coluna 'LIQUIDO' para o tipo numérico
df['LIQUIDO'] = pd.to_numeric(df['LIQUIDO'].str.replace(',', '.'), errors='coerce')

# Exibir as primeiras linhas do arquivo
print(df.head())

# Análise básica: Descrição estatística
print(df.describe())

# Calcular o total de valores líquidos
total_liquido = df['LIQUIDO'].sum()
print(f'Total do valor líquido: {total_liquido}')
