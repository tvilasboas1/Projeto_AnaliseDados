import pandas as pd

# Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo
df = pd.read_csv('PlanilhaGanhosApp.csv', sep=';', decimal=',')

# Visualizar as primeiras linhas do DataFrame
print(df.head())
# Remover linhas completamente vazias (se houver)
df = df.dropna(how='all')
print(df.columns)
df.columns = df.columns.str.strip()
print(df.columns)

# Garantir que os valores numéricos estejam no formato correto
# Substituir vírgulas por pontos nos números e converter para float
for col in ['UBER', '99POP', 'OUTROS', 'TOTAL', 'GASTOS', 'LIQUIDO']:
    df[col] = df[col].astype(str).str.replace(',', '.').astype(float)

# Visualizar o DataFrame ajustado
print(df.head())
# Calcular a coluna 'Liquido' como TOTAL - GASTOS
df['LIQUIDO'] = df['TOTAL'] - df['GASTOS']

# Visualizar o resultado
print(df[['TOTAL', 'GASTOS', 'LIQUIDO']].head())
