import pandas as pd

# Exemplo da tabela original (você pode substituir por leitura de CSV ou Excel)
dados = pd.read_excel("default.xlsx", sheet_name="FORECAST2025")

# Criando o DataFrame
df = pd.DataFrame(dados)

# Transformando de wide para long
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
df_long = df.melt(id_vars=["Modelo"], value_vars=meses,
                  var_name="Mes", value_name="Valor")

# Removendo linhas com valor nulo (caso algum mês esteja em branco)
df_long = df_long.dropna(subset=["Valor"])

df_long.to_excel('results_forecast.xlsx', index=False)

# Exibindo resultado
print(df_long)
