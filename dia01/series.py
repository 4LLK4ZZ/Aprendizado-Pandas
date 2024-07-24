# %%

import pandas as pd

# %%

idades = [30,20,40,10]
idades

# %%
media = sum(idades) / len(idades)
# %%
media
# %%
total = 0
for i in idades:
    total += (media - i)**2

variancia = total / (len(idades) - 1)

variancia
# %%

#Convertendo a lista 'idades' para serie e atribuindo em uma variável nova
series_idades = pd.Series(idades)
series_idades
# %%
# Média
series_idades.mean()
# %%
# Variância
series_idades.var()
# %%
# Mediana
series_idades.median()
# %%
# Quartil
series_idades.quantile(0.75)
# %%
# Desvio Padrão
series_idades.std()
# %%
# Sumarização
series_idades.describe()
# %%
#Dimensão da série
series_idades.shape
# %%
# Navegando na lista
idades[0]
# %%
# Navegando na série
series_idades[3]
# %%
# Alterando o index da série
series_idades.index = ['a', 'b', 'c', 'd']
# %%
# Navegando nos índices novos
series_idades['b']
# %%
#Diferentemente do index o 'iloc' busca pela POSIÇÃO
series_idades.iloc[0]
# %%
# LOC busca pelo ÍNDICE, ILOC busca pelo POSIÇÃO
series_idades.loc['a']
# %%
# Nomeando a série, similiar a um nome de coluna do excel
series_idades.name = 'idades'
series_idades
# %%
