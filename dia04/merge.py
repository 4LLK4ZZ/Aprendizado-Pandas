# %%
import pandas as pd

data_users = {
    "id": [1, 2, 3, 4],
    "nome": ["Alcides", "Ana", "Carlos", "Karol"],
    "idade": [24, 26, 27, 30]
}

df_user = pd.DataFrame(data_users)
df_user
# %%
data_transacoes = {
    "id_user": [1, 2, 3, 1, 1, 3, 5],
    "vl": [432, 532, 652, 20, 10, 100, 120],
    "qtProdutos": [10, 5, 7, 3, 9, 15, 8]
}
df_transacao = pd.DataFrame(data_transacoes)
df_transacao
# %%
df_transacao.merge(df_user,
                how="left",
                left_on="id_user", 
                right_on="id"
                )
# %%
df_transacao.merge(df_user,
                how="inner",
                left_on="id_user", 
                right_on="id"
                )
# %%
