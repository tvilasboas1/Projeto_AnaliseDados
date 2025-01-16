import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('PlanilhaGanhosApp.csv', sep=',', decimal=',', quotechar='"')

# Converter a coluna 'LIQUIDO' para o tipo numérico

df['UBER'] = pd.to_numeric(df['UBER'].str.replace(',', '.'), errors='coerce')
df['99POP'] = pd.to_numeric(df['99POP'].str.replace(',', '.'), errors='coerce')
df['OUTROS'] = pd.to_numeric(df['OUTROS'].str.replace(',','.'), errors='coerce')      
df['TOTAL'] = pd.to_numeric(df['TOTAL'].str.replace(',', '.'), errors='coerce')
df['GASTOS'] = pd.to_numeric(df['GASTOS'].str.replace(',','.'), errors='coerce')
df['LIQUIDO'] = pd.to_numeric(df['LIQUIDO'].str.replace(',', '.'), errors='coerce')
# Exibir as primeiras linhas do arquivo
print(df.head())

# Análise básica: Descrição estatística
print(df.describe())

# Calcular o total de valores líquidos
total_uber = df['UBER'].sum()
print(f'Total do valor Uber: {total_uber:.2f}')

total_99pop = df['99POP'].sum()
print(f'Total do Valor 99Pop: {total_99pop:.2f}')

total_outros = df['OUTROS'].sum()
print(f'Total do Valor de Outros: {total_outros:.2f}')

total_geral = df['TOTAL'].sum()
print(f'Valor Total: {total_geral:.2f}')

total_gastos = df['GASTOS'].sum()
print(f'Valor Gastos: {total_gastos:.2f}')

total_liquido = df['LIQUIDO'].sum()
print(f'Total do valor líquido: {total_liquido:.2f}')

# Exibir os dados com alinhamento ajustado
print(df.to_string(index=False, float_format='{:,.2f}'.format))


