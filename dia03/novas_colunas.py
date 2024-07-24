# %%

import pandas as pd
import numpy as np

df = pd.read_csv("../data/customers.csv", sep=";")
# %%

df["Points_Double"] = df['Points'] * 2
df
# %%

df['Points_ratio'] = df['Points_Double'] / df['Points']
df
# %%
df['Constante'] = 1
df
# %%
df['Points_LOG'] = np.log(df['Points'])
df
# %%
df['Name'].str.upper()
# %%
df
# %%

def get_first(nome:str):
    nome = nome.upper()
    return nome.split("_")[0]

# %%

df['Name_First'] = df["Name"].apply( get_first )
df
# %%

get_f = lambda nome: nome.split("_")[0]
get_f("Alcides")
# %%
df["Name"].apply( lambda x: x.upper().split("_")[0] )

# %%

def intervalo_pontos(pontos):
    if pontos < 2500:
        return "baixo"
    elif pontos < 3500:
        return "médio"
    else:
        return "alto"
    
df["Faixa_Pontos"] = df["Points"].apply(intervalo_pontos)
df
# %%
df["UUID"].apply(lambda x: x[-3:])
# %%

data = {
    "nome": ["Alcides", "João", "Maria", "Luiza"],
    "row['recencia']": [15, 20, 10, 52],
    "row['valor']": [3500, 2600, 3100, 4300],
    "row['frequencia']": [6, 4, 7, 5],
}

df_crm = pd.DataFrame(data)
# %%
df_crm
# %%

def rfv(row):

    nota = 0

    if row['recencia'] <= 10:
        nota += 10
    elif 10 < row['recencia'] <= 30:
        nota += 5
    elif row['recencia'] > 30:
        nota += 0

    if row['valor'] > 1000:
        nota += 10
    elif 100 <= row['valor'] < 1000:
        nota += 5
    elif row['valor'] < 100:
        nota += 0

    if row['frequencia'] > 10:
        nota += 10
    elif 5 <= row['frequencia'] < 10:
        nota += 5
    elif row['frequencia'] < 5:
        nota += 0

    return nota


# %%
df_crm.apply(rfv, axis=1)
# %%
df_crm.iloc[0]
# %%
