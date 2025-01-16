import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('PlanilhaGanhosApp.csv', sep=',', decimal=',', quotechar='"')

# Converter as colunas relevantes para numérico
for col in ['UBER', '99POP', 'OUTROS', 'TOTAL', 'GASTOS', 'LIQUIDO']:
    df[col] = pd.to_numeric(df[col].str.replace(',', '.'), errors='coerce')

# Gerar a coluna 'Fev22' (dias do mês)
ano = 2022
mes = 2
# Substituir valores inválidos ('-') por NaN, depois ignorá-los
df['Fev22'] = pd.to_numeric(df['Fev22'], errors='coerce')

# Gerar as datas para os dias válidos e associar aos dias da semana
df['Data'] = pd.to_datetime(df['Fev22'], format='%d', errors='coerce')
df['DiaSemana'] = df['Data'].dt.day_name()  # Obtém o nome do dia da semana

# Garantir que os dias da semana estão no formato correto para o gráfico
df['DiaSemana'] = pd.Categorical(df['DiaSemana'], categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], ordered=True)

# Gráfico de barras para valores líquidos por dia da semana
plt.figure(figsize=(10,6))
plt.bar(df['DiaSemana'], df['LIQUIDO'], color='skyblue')
plt.title('Valores Líquidos por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Líquido (R$)')
plt.xticks(rotation=45)
plt.tight_layout()

# Exibir o gráfico
plt.show()

# Gráfico de barras agrupadas para comparar os ganhos das plataformas
fig, ax = plt.subplots(figsize=(10,6))
df.set_index('DiaSemana')[['UBER', '99POP', 'OUTROS']].plot(kind='bar', stacked=True, ax=ax)
plt.title('Comparação dos Ganhos por Plataforma por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Ganhos (R$)')
plt.xticks(rotation=45)
plt.tight_layout()

# Exibir o gráfico
plt.show()
