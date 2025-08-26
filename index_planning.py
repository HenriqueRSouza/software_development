import pandas as pd

# Carregar a planilha
df = pd.read_excel("meu.xlsx")  # ou pd.read_csv("sua_tabela.csv")

# Cria a coluna "Modelo" unindo informações relevantes
df["Modelo"] = df["MODEL DESCRIPTION"] + " " + df["DERIVATIVE DESCRIPTION"].str.extract(r'(\w+)$')[0]  # Ex: "EC40 Plus"

# Traduz os meses para abreviações
mes_dict = {
    "Janeiro": "Jan", "Fevereiro": "Fev", "Março": "Mar", "Abril": "Abr",
    "Maio": "Mai", "Junho": "Jun", "Julho": "Jul", "Agosto": "Ago",
    "Setembro": "Set", "Outubro": "Out", "Novembro": "Nov", "Dezembro": "Dez"
}
df["Mes"] = df["MES"].map(mes_dict)

# Cria a coluna "Valor" como contagem
df["Valor"] = 1

# Agrupa
df_resumo = df.groupby(["Modelo", "Mes"], as_index=False)["Valor"].sum()

df_resumo.to_excel('results_planning.xlsx', index=False)

# Exibe
print(df_resumo)
