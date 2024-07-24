# %%
import pandas as pd
# %%
df_custom = pd.read_csv("../data/customers.csv", sep=";")
df_custom
# %%
df_custom.shape
# %%
df_custom.info(memory_usage="deep")
# %%
df_custom['Points'].describe()
# %%
df_custom['Points'].astype(int)
# %%
df_custom['Points'].describe()
# %%
condicao = df_custom["Points"] > 1000
df_custom[condicao]
# %%
df_custom[condicao].max()
# %%
condicao = df_custom["Points"] == df_custom["Points"].max()
df_custom[condicao]
# %%
condicao = df_custom["Points"] == df_custom["Points"].max()
df_maior = df_custom[condicao]
df_maior["Name"].iloc[0]
# %%
condicao = (df_custom["Points"] >= 1000) & (df_custom["Points"] <= 2000)
df_1000_2000 = df_custom[condicao].copy()
# Deve ser criado uma cópia, pois alterar os valores que estão sendo referenciados irá gerar conflitos.
df_1000_2000["Points"] = df_1000_2000["Points"] + 1000
df_1000_2000
# %%
a = [1,2,3,4] # 'a' é uma referência do vetor
b = a.copy() # 'b' copiou os valores de 'a', ou seja, não será mais uma referência de 'a'.

print(a)
print(b)

b.append(5)

print(a)
print(b)
# %%
df_custom[["UUID", "Name"]]
# %%
colunas = df_custom.columns.tolist()
colunas.sort()
colunas
# %%
df_custom = df_custom.rename(columns={"Name": "Nome", "Points": "Pontos"})
# %%
df_custom.rename(columns={"UUID": "ID"}, inplace=True)
df_custom

# %%
