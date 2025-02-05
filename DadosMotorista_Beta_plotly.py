import pandas as pd
import plotly.express as px

# Carregar dados
dados = pd.read_csv('GanhosAppFev22_Beta.csv', sep=',', decimal=',', thousands='.')

# Renomear a coluna de dia
dados = dados.rename(columns={dados.columns[0]: 'DIA'})
dados['DIA'] = pd.to_numeric(dados['DIA'], errors='coerce').astype('Int64')

# Adicionar o nome do mês
dados['Mês'] = 'Fev22'  # Ajustar conforme necessário

# Converter colunas numéricas corretamente (Corrigido)
for col in ['UBER', '99POP', 'OUTROS', 'TOTAL', 'GASTOS', 'Liquido']:
    if col in dados.columns:
        dados[col] = pd.to_numeric(
            dados[col].astype(str)
            .str.replace('.', '', regex=False)  # Remover separador de milhar
            .str.replace(',', '.', regex=False),  # Converter vírgula decimal para ponto
            errors='coerce'
        )

# Exibir valores corrigidos do dia 11 de fevereiro
print("Valores do dia 11 de Fevereiro após correção:")
print(dados[dados['DIA'] == 11][['DIA', 'UBER', '99POP', 'OUTROS', 'TOTAL', 'GASTOS', 'Liquido']])

# Gráfico 1: Ganhos líquidos por dia
fig1 = px.line(
    dados, x="DIA", y="Liquido", title="Ganhos Líquidos por Dia",
    labels={"Liquido": "Ganho Líquido (R$)", "DIA": "Dia"},
    markers=True
)
fig1.show()

# Gráfico 2: Gastos por dia
fig2 = px.bar(
    dados, x="DIA", y="GASTOS", title="Gastos por Dia",
    labels={"GASTOS": "Gastos (R$)", "DIA": "Dia"},
    color="Mês"
)
fig2.show()

# Gráfico 3: Comparação de ganhos por aplicativo (Corrigido)
fig3 = px.bar(
    dados, x="DIA", y=["UBER", "99POP", "OUTROS"], 
    title="Comparação de Ganhos por Aplicativo",
    labels={"value": "Ganho Bruto (R$)", "variable": "Aplicativo", "DIA": "Dia"},
    barmode="stack"
)
fig3.show()
