import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo CSV
df = pd.read_csv('PlanilhaGanhosApp.csv', sep=',', decimal=',', quotechar='"')

# Converter as colunas relevantes para numérico
for col in ['UBER', '99POP', 'OUTROS', 'TOTAL', 'GASTOS', 'LIQUIDO']:
    df[col] = pd.to_numeric(df[col].str.replace(',', '.'), errors='coerce')

# Converta a coluna 'Fev22' para numérico, caso necessário
df['Fev22'] = pd.to_numeric(df['Fev22'], errors='coerce')

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

# Remover linhas com valores NaN na coluna 'Fev22' para o gráfico
df = df.dropna(subset=['Fev22'])

# Configuração do estilo do gráfico
sns.set(style="whitegrid")

# Gráfico de barras para valores líquidos por 'Fev22'
plt.figure(figsize=(10, 6))  # Ajusta o tamanho do gráfico
plt.bar(df['Fev22'], df['LIQUIDO'], color='skyblue', edgecolor='black')

# Adicionando uma linha de média
mean_value = df['LIQUIDO'].mean()
plt.axhline(mean_value, color='red', linestyle='--', label=f'Média: R$ {mean_value:.2f}')

# Título e rótulos
plt.title('Valores Líquidos por Dia de Fevereiro', fontsize=16)
plt.xlabel('Dia (Fev22)', fontsize=12)
plt.ylabel('Líquido (R$)', fontsize=12)

# Adicionar anotações nas barras
for i, value in enumerate(df['LIQUIDO']):
    plt.text(df['Fev22'].iloc[i], value + 5, f'R$ {value:.2f}', ha='center', va='bottom')

# Exibir legenda
plt.legend()

# Mostrar gráfico
plt.tight_layout()
plt.show()
