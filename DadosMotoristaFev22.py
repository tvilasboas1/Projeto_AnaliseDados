import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo CSV
df = pd.read_csv('PlanilhaGanhosAppFev22.csv', sep=',', decimal=',', quotechar='"')

# Converter as colunas relevantes para numérico
for col in ['UBER', '99POP', 'OUTROS', 'TOTAL', 'GASTOS', 'LIQUIDO']:
    df[col] = pd.to_numeric(df[col].str.replace(',', '.'), errors='coerce')

# Converta a coluna 'Fev22' para numérico, caso necessário
df['Fev22'] = pd.to_numeric(df['Fev22'], errors='coerce')

# Exibir as primeiras linhas do arquivo
print(df.head())

# Remover linhas com valores NaN na coluna 'Fev22' para o gráfico
df = df.dropna(subset=['Fev22'])

# Estilo de gráfico
sns.set(style="darkgrid")

# Gráfico de linha mostrando a tendência do valor líquido
plt.figure(figsize=(12, 6))
plt.plot(df['Fev22'], df['LIQUIDO'], marker='o', color='b', linestyle='-', linewidth=2, markersize=6)

# Adicionar título e rótulos
plt.title('Tendência do Valor Líquido por Dia de Fevereiro', fontsize=16)
plt.xlabel('Dia (Fev22)', fontsize=12)
plt.ylabel('Líquido (R$)', fontsize=12)

# Exibir o gráfico
plt.tight_layout()
plt.show()

# Carregar o arquivo CSV
df = pd.read_csv('PlanilhaGanhosApp.csv', sep=',', decimal=',', quotechar='"')

# Converter as colunas relevantes para numérico
for col in ['UBER', '99POP', 'OUTROS', 'TOTAL', 'GASTOS', 'LIQUIDO']:
    df[col] = pd.to_numeric(df[col].str.replace(',', '.'), errors='coerce')

# Converta a coluna 'Fev22' para numérico, caso necessário
df['Fev22'] = pd.to_numeric(df['Fev22'], errors='coerce')

# Exibir as primeiras linhas do arquivo
print(df.head())

# Remover linhas com valores NaN na coluna 'Fev22' para o gráfico
df = df.dropna(subset=['Fev22'])

# Estilo de gráfico
sns.set(style="whitegrid")

# Gráfico de barras empilhadas
plt.figure(figsize=(12, 6))
plt.bar(df['Fev22'], df['UBER'], label='UBER', color='skyblue')
plt.bar(df['Fev22'], df['99POP'], bottom=df['UBER'], label='99POP', color='orange')
plt.bar(df['Fev22'], df['OUTROS'], bottom=df['UBER'] + df['99POP'], label='OUTROS', color='green')

# Adicionar título e rótulos
plt.title('Distribuição dos Ganhos por Plataforma - Fevereiro', fontsize=16)
plt.xlabel('Dia (Fev22)', fontsize=12)
plt.ylabel('Valor (R$)', fontsize=12)

# Adicionar legenda
plt.legend()

# Exibir o gráfico
plt.tight_layout()
plt.show()


# Carregar o arquivo CSV
df = pd.read_csv('PlanilhaGanhosApp.csv', sep=',', decimal=',', quotechar='"')

# Converter as colunas relevantes para numérico
for col in ['UBER', '99POP', 'OUTROS', 'TOTAL', 'GASTOS', 'LIQUIDO']:
    df[col] = pd.to_numeric(df[col].str.replace(',', '.'), errors='coerce')

# Calcular o total de cada categoria
total_uber = df['UBER'].sum()
total_99pop = df['99POP'].sum()
total_outros = df['OUTROS'].sum()

# Gráfico de pizza mostrando a proporção de cada plataforma
labels = ['Uber', '99Pop', 'Outros']
sizes = [total_uber, total_99pop, total_outros]
colors = ['skyblue', 'orange', 'green']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90, explode=(0.1, 0, 0))

# Adicionar título
plt.title('Distribuição dos Ganhos por Plataforma', fontsize=16)

# Exibir o gráfico
plt.show()

# Carregar o arquivo CSV
df = pd.read_csv('PlanilhaGanhosApp.csv', sep=',', decimal=',', quotechar='"')

# Converter as colunas relevantes para numérico
for col in ['UBER', '99POP', 'OUTROS', 'TOTAL', 'GASTOS', 'LIQUIDO']:
    df[col] = pd.to_numeric(df[col].str.replace(',', '.'), errors='coerce')

# Filtro para mostrar apenas dias com valor líquido positivo
df_positive = df[df['LIQUIDO'] > 0]

# Estilo de gráfico
sns.set(style="whitegrid")

# Gráfico de barras para valores líquidos positivos
plt.figure(figsize=(12, 6))
plt.bar(df_positive['Fev22'], df_positive['LIQUIDO'], color='limegreen')

# Adicionar título e rótulos
plt.title('Valores Líquidos Positivos por Dia (Fevereiro)', fontsize=16)
plt.xlabel('Dia (Fev22)', fontsize=12)
plt.ylabel('Líquido (R$)', fontsize=12)

# Exibir o gráfico
plt.tight_layout()
plt.show()
