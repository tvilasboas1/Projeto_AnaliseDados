import pandas as pd
import plotly.express as px

# Lista de arquivos (adicione mais meses conforme necessário)
arquivos = [
    "GanhosAppFev22_Beta.csv",
    "GanhosAppMar22_Beta.csv",
    "GanhosAppAbr22_Beta.csv",
    "GanhosAppMai22_Beta.csv",
    "GanhosAppJun22_Beta.csv",
    "GanhosAppMar23_Beta.csv",
    "GanhosAppAbr23_Beta.csv",
    "GanhosAppMai23_Beta.csv",
    "GanhosAppJun23_Beta.csv",
    "GanhosAppJul23_Beta.csv",
    "GanhosAppAgo23_Beta.csv",
    "GanhosAppSet23_Beta.csv",
    "GanhosAppOut23_Beta.csv",
    "GanhosAppNov23_Beta.csv",  # Adicionei a vírgula faltante aqui
    "GanhosAppDez23_Beta.csv",
    "GanhosAppJan24_Beta.csv",
    "GanhosAppFev24_Beta.csv",
    "GanhosAppMar24_Beta.csv",
    "GanhosAppAbr24_Beta.csv",
    "GanhosAppMai24_Beta.csv",
    "GanhosAppJun24_Beta.csv",
    "GanhosAppJul24_Beta.csv",
    "GanhosAppAgo24_Beta.csv",
    "GanhosAppSet24_Beta.csv",
    "GanhosAppOut24_Beta.csv",
    "GanhosAppNov24_Beta.csv",
    "GanhosAppDez24_Beta.csv"
    # Adicione os outros meses aqui
]

# Função para corrigir a conversão de números
def corrigir_valor(valor):
    """
    Corrige a formatação dos números, removendo separadores de milhar e convertendo vírgulas decimais para pontos.
    """
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
    try:
        # Extrair o nome do mês do nome do arquivo
        mes = arquivo.split("GanhosApp")[1].split("_Beta.csv")[0]
        
        # Carregar os dados
        dados = pd.read_csv(arquivo, sep=',', decimal=',', thousands='.')
        
        # Renomear a coluna de dia
        dados = dados.rename(columns={dados.columns[0]: 'DIA'})
        dados['DIA'] = pd.to_numeric(dados['DIA'], errors='coerce').astype('Int64')
        
        # Adicionar o nome do mês e o ano
        dados['Mês'] = mes
        dados['Ano'] = '20' + mes[-2:]  # Extrai o ano (últimos 2 caracteres)
        
        # Aplicar a correção nas colunas numéricas
        for col in ['UBER', '99POP', 'OUTROS', 'INDRIVER', 'IFOOD', 'TOTAL', 'GASTOS', 'LIQUIDO']:
            if col in dados.columns:
                dados[col] = dados[col].apply(corrigir_valor)
                dados[col] = pd.to_numeric(dados[col], errors='coerce')
            else:
                # Se a coluna não existir, criar com valores 0
                dados[col] = 0
        
        # Adicionar ao DataFrame de dados mensais
        dados_mensais.append(dados)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {arquivo}. Verifique o nome do arquivo e tente novamente.")
    except Exception as e:
        print(f"Erro ao processar o arquivo {arquivo}: {e}")

# Combinar todos os DataFrames em um único DataFrame
dados_completos = pd.concat(dados_mensais, ignore_index=True)

# Preencher valores NaN nas colunas com 0
for col in ['UBER', '99POP', 'OUTROS', 'INDRIVER', 'IFOOD', 'TOTAL', 'GASTOS', 'LIQUIDO']:
    dados_completos[col] = dados_completos[col].fillna(0)

# Exibir os primeiros registros do DataFrame combinado
print("Dados combinados:")
print(dados_completos.head())

# Verificar se há dados de gastos e líquidos para cada mês
print("\nVerificação de dados de gastos por mês:")
print(dados_completos.groupby('Mês')['GASTOS'].apply(lambda x: x.isnull().all()))

print("\nVerificação de dados de líquidos por mês:")
print(dados_completos.groupby('Mês')['LIQUIDO'].apply(lambda x: x.isnull().all()))

# Gráfico 1: Ganhos líquidos por dia (com filtro de ano)
fig1 = px.line(
    dados_completos, x="DIA", y="LIQUIDO", color="Mês", 
    title="Ganhos Líquidos por Dia (Filtro por Ano)",
    labels={"LIQUIDO": "Ganho Líquido (R$)", "DIA": "Dia"},
    markers=True,
    facet_col="Ano",  # Cria um gráfico separado para cada ano
    facet_col_wrap=2  # Organiza os gráficos em 2 colunas
)
# Ajustar o eixo X para mostrar de 1 a 31
fig1.update_xaxes(range=[1, 31], dtick=1)
fig1.show()

# Gráfico 2: Gastos por dia (com filtro de ano)
fig2 = px.bar(
    dados_completos, x="DIA", y="GASTOS", color="Mês", 
    title="Gastos por Dia (Filtro por Ano)",
    labels={"GASTOS": "Gastos (R$)", "DIA": "Dia"},
    facet_col="Ano",  # Cria um gráfico separado para cada ano
    facet_col_wrap=2  # Organiza os gráficos em 2 colunas
)
# Ajustar o eixo Y para inverter a direção das barras
fig2.update_yaxes(autorange="reversed")  # Inverte a escala do eixo Y
# Ajustar o eixo X para mostrar de 1 a 31
fig2.update_xaxes(range=[1, 31], dtick=1)
fig2.show()

# Gráfico 3: Comparação de ganhos por aplicativo (com filtro de ano)
fig3 = px.bar(
    dados_completos, x="DIA", y=["UBER", "99POP", "OUTROS", "INDRIVER", "IFOOD"], 
    color="Mês", title="Comparação de Ganhos por Aplicativo (Filtro por Ano)",
    labels={"value": "Ganho Bruto (R$)", "variable": "Aplicativo", "DIA": "Dia"},
    barmode="stack",
    facet_col="Ano",  # Cria um gráfico separado para cada ano
    facet_col_wrap=2  # Organiza os gráficos em 2 colunas
)
# Ajustar o eixo X para mostrar de 1 a 31
fig3.update_xaxes(range=[1, 31], dtick=1)
fig3.show()