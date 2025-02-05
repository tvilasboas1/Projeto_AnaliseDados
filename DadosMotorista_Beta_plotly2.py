import pandas as pd
import plotly.express as px

# Lista de arquivos (adicione mais meses conforme necessário)
arquivos = [
    "GanhosAppFev22_Beta.csv",
    "GanhosAppMar22_Beta.csv",
    "GanhosAppAbr22_Beta.csv",
    "GanhosAppMai22_Beta.csv",
    "GanhosAppJun22_Beta.csv"
]

# Função para corrigir a conversão de números
def corrigir_valor(valor):
    if isinstance(valor, str):
        # Remover o separador de milhar (apenas se houver mais de uma vírgula ou ponto)
        if valor.count('.') > 1:  # Se houver mais de um ponto, é separador de milhar
            valor = valor.replace('.', '')
        # Substituir a vírgula decimal por ponto
        valor = valor.replace(',', '.')
    return valor

# Lista para armazenar os DataFrames de cada mês
dados_mensais = []

# Carregar e processar cada arquivo
for arquivo in arquivos:
    # Extrair o nome do mês do nome do arquivo
    mes = arquivo.split("GanhosApp")[1].split("_Beta.csv")[0]
    
    # Carregar os dados
    dados = pd.read_csv(arquivo, sep=',', decimal=',', thousands='.')
    
    # Renomear a coluna de dia
    dados = dados.rename(columns={dados.columns[0]: 'DIA'})
    dados['DIA'] = pd.to_numeric(dados['DIA'], errors='coerce').astype('Int64')
    
    # Adicionar o nome do mês
    dados['Mês'] = mes
    
    # Padronizar o nome da coluna de gastos
    if 'Gastos' in dados.columns:
        dados = dados.rename(columns={'Gastos': 'GASTOS'})
    
    # Aplicar a correção nas colunas numéricas
    for col in ['UBER', '99POP', 'OUTROS', 'TOTAL', 'GASTOS', 'LIQUIDO']:
        if col in dados.columns:
            dados[col] = dados[col].apply(corrigir_valor)
            dados[col] = pd.to_numeric(dados[col], errors='coerce')
        else:
            # Se a coluna não existir, criar com valores 0
            dados[col] = 0
    
    # Adicionar ao DataFrame de dados mensais
    dados_mensais.append(dados)

# Combinar todos os DataFrames em um único DataFrame
dados_completos = pd.concat(dados_mensais, ignore_index=True)

# Preencher valores NaN na coluna GASTOS com 0
dados_completos['GASTOS'] = dados_completos['GASTOS'].fillna(0)

# Exibir os primeiros registros do DataFrame combinado
print("Dados combinados:")
print(dados_completos.head())

# Verificar se há dados de gastos para cada mês
print("\nVerificação de dados de gastos por mês:")
print(dados_completos.groupby('Mês')['GASTOS'].apply(lambda x: x.isnull().all()))

# Gráfico 1: Ganhos líquidos por dia (todos os meses)
fig1 = px.line(
    dados_completos, x="DIA", y="LIQUIDO", color="Mês", 
    title="Ganhos Líquidos por Dia (Vários Meses)",
    labels={"LIQUIDO": "Ganho Líquido (R$)", "DIA": "Dia"},
    markers=True
)
# Ajustar o eixo X para mostrar de 1 a 31
fig1.update_xaxes(range=[1, 31], dtick=1)
fig1.show()

# Gráfico 2: Gastos por dia (todos os meses)
fig2 = px.bar(
    dados_completos, x="DIA", y="GASTOS", color="Mês", 
    title="Gastos por Dia (Vários Meses)",
    labels={"GASTOS": "Gastos (R$)", "DIA": "Dia"}
)
# Ajustar o eixo Y para inverter a direção das barras
fig2.update_yaxes(autorange="reversed")  # Inverte a escala do eixo Y
# Ajustar o eixo X para mostrar de 1 a 31
fig2.update_xaxes(range=[1, 31], dtick=1)
fig2.show()

# Gráfico 3: Comparação de ganhos por aplicativo (todos os meses)
fig3 = px.bar(
    dados_completos, x="DIA", y=["UBER", "99POP", "OUTROS"], 
    color="Mês", title="Comparação de Ganhos por Aplicativo (Vários Meses)",
    labels={"value": "Ganho Bruto (R$)", "variable": "Aplicativo", "DIA": "Dia"},
    barmode="stack"
)
# Ajustar o eixo X para mostrar de 1 a 31
fig3.update_xaxes(range=[1, 31], dtick=1)
fig3.show()