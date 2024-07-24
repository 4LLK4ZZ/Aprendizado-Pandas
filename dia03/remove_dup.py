#%%

import pandas as pd

# %%
data = {
    "Nome": ["Alcides", "Aparecida", "Gustavo", "Altiérys", "Ana Paula", "Alcides", "Aparecida", "Gustavo"],
    "Idade": [24, 62, 25, 19, 46, 24, 62, 25],
    "modificado_em": [1, 2, 3, 1, 2, 1, 2, 3],
}

# %%
df = pd.DataFrame(data)
# Para poder apagar as duplicadas é ideal que ordene
# os valores pela data, para ter a garantia 
# de que está pegando os valores atuais.
df = (df.sort_values(by="modificado_em")
      .drop_duplicates(subset=['Nome', 'Idade'], keep='last'))
df
# %%
