# %%
import pandas as pd
import numpy as np

data = {
    "nome": ["Alcides", "Ana", "José", "Luana", "Karol"],
    "idade": [24, 46, 52, 32, np.nan],
    "renda": [np.nan, 2600, 2300, 3200, np.nan]

}

df = pd.DataFrame(data)
df
# %%
df['idade'].isna().sum()
# %%
df.isna().sum()
# %%
df.isna().mean()
# %%
# Para análise de dados pode ser feito dessa maneira,
# Para o machine Learning não é correto fazer assim.
df.fillna({
    "idade": df['idade'].mean(),
    "renda": df['renda'].mean(),
    })
# %%
#Subset indicando quais as colunas devem estar NaN
#No how é possível colocar o 'any' que indicaria
#apenas uma das colunas sendo NaN
df.dropna(subset=["idade", "renda"], how='all')
# %%
#Dessa forma colocando o 'axis' ele deixa de identificar por linha
# e passa a dropar por colunas.
# 'thresh' é usado para identificar quantos valores não-nulos
# é necessário para não dropar.
df.dropna(axis=1, thresh=4)
# %%