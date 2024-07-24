#%%
import pandas as pd

data_01 = {
    "id": [1, 2, 3, 4],
    "nome": ["Alcides", "Ana", "Carlos", "Karol"],
    "idade": [24, 26, 27, 30]
}

df_01 = pd.DataFrame(data_01)
df_01

#%%

data_02 = {
    "id": [5, 6, 7, 8],
    "nome": ["Jhow", "Zinho", "Pietra", "Hi"],
    "idade": [25, 19, 7, 12]
}

df_02 = pd.DataFrame(data_02)
df_02
# %%
pd.concat([df_01, df_02]).reset_index(drop=True)
# %%
data_03 = {
    "sobrenome": ["Nogueira", "Carla", "Silva", "Souza"],
    "renda": [3100, 2900, 2700, 6000]
}

df_03 = pd.DataFrame(data_03).sort_values(["renda", "sobrenome"], ascending=[False, True])
df_03
# %%
pd.concat([df_01, df_03], axis=1 )
# %%
