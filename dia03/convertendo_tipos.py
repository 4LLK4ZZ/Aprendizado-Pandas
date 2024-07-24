# %%
import pandas as pd

df = pd.read_csv('../data/customers.csv', sep=";")
df
# %%
df.dtypes
# %%
df['Points'].astype(str)
# %%
df["Points Double"] = df['Points'] * 2
# %%
df

df[["Points", "Points Double"]].astype(float)
# %%
