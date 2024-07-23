import pandas as pd


df_vendas = pd.read_csv("./data/silver/dados_vendas_cursos_online.csv")


df_vendas = df_vendas.rename(columns={
    "Nome do Curso": "nome_curso",
    "Quantidade de Vendas": "qt_de_vendas",
    "Preço Unitário": "preco_unitario",
    "Data": "data"})


df_vendas["data"] = pd.to_datetime(df_vendas["data"], format='%Y-%m-%d')

print(f"Tipo do dado após conversão: {df_vendas['data'].dtypes}")
print(f"Amostrar para visualização {df_vendas['data'][1]}")


df_vendas["valor_vendas"] = df_vendas.qt_de_vendas*df_vendas.qt_de_vendas


df_vendas.to_csv("./data/gold/tratados_dados_vendas_cursos_online.csv",
                 index=False)
