# %%
import pandas as pd
# %%
data = {
    "nome": ["alcides", "aparecida", "gustavo", "tiago"],
    "sobrenome": ["nogueira", "lopes", "jhorrany", "souza"],
    "idade": [23, 60, 25, 42] 
}
# %%
# Buscando a idade do primeiro nome
data["idade"][0]
# %%
# Transformando a série para um dataframe
df = pd.DataFrame(data)
df
# %%
# Garantir que será buscado pela posição 0 e não pelo índice
df["idade"].iloc[0]
# %%
# Identificando o tipo de dado.
type(df["idade"])
# %%
# Buscando os valores da primeira linha
df.iloc[0]

# %%
# Identificando o tipo do valor da primeira linha
type(df.iloc[0])
# %%
#Identificar nome das colunas
df.columns
# %%
#identificar os indices
df.index
# %%
# Características do dataFrame
df.info()
# %%
# memória real sendo usada para armazenar esses valores.
df.info(memory_usage='deep')
# %%
# Identificar o tipo de cada coluna no df
df.dtypes
# %%
df['peso'] = [71, 68, 79, 75]
sumario = df.describe()
sumario['peso']['mean']
# %%
# Mostrar uma parte dos dados do cabeçalho
df.head(2)
# %%
# Mostrar uma parte dos dados do rodapé
df.tail(2)
# %%
