import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('PlanilhaGanhosApp.csv', sep=',', decimal=',', quotechar='"')

# Converter as colunas relevantes para numérico
for col in ['UBER', '99POP', 'OUTROS', 'TOTAL', 'GASTOS', 'LIQUIDO']:
    df[col] = pd.to_numeric(df[col].str.replace(',', '.'), errors='coerce')

# Exibir as primeiras linhas do arquivo
print(df.head())

# Análise básica: Descrição estatística
print(df.describe())

# Calcular e exibir os totais
print(f"Total do valor Uber: {df['UBER'].sum():.2f}")
print(f"Total do valor 99Pop: {df['99POP'].sum():.2f}")
print(f"Total do valor Outros: {df['OUTROS'].sum():.2f}")
print(f"Valor Total: {df['TOTAL'].sum():.2f}")
print(f"Valor Gastos: {df['GASTOS'].sum():.2f}")
print(f"Total do valor líquido: {df['LIQUIDO'].sum():.2f}")

from tabulate import tabulate

# Exibir os dados da tabela de forma bonita
print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))

# Exibir apenas os totais de forma organizada
totals = [
    ['Uber', df['UBER'].sum()],
    ['99Pop', df['99POP'].sum()],
    ['Outros', df['OUTROS'].sum()],
    ['Total', df['TOTAL'].sum()],
    ['Gastos', df['GASTOS'].sum()],
    ['Líquido', df['LIQUIDO'].sum()]
]

print("\nTotais:")
print(tabulate(totals, headers=['Categoria', 'Total (R$)'], tablefmt='fancy_grid'))
