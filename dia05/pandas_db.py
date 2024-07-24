#%%
import pandas as pd
import sqlalchemy
# %%

engine = sqlalchemy.create_engine("sqlite:///../data/database.db")
# %%

df_transactions_cart = pd.read_sql_table("transactions_cart", engine)
df_transactions_cart
# %%
query = """
SELECT *
FROM customers AS t1 
LEFT JOIN transactions AS t2
ON t1.UUID = t2.IdCustomer
LIMIT 10
"""
df_join = pd.read_sql_query(query, engine)
df_join
# %%
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

df_01.to_sql("tb_sla", engine, index= False)
# %%
df_02.to_sql("tb_sla", engine, index= False, if_exists="append")

# %%
