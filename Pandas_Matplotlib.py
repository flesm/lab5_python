#!/usr/bin/env python
# coding: utf-8

# ## Лабараторная работа № 5 Варыянт 18

# ### Работа з Pandas і візуалізацыя дадзеных у Matplotlib

# In[44]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pp = pd.read_csv('price_prepared.csv', delimiter=';', nrows=1000)
df = pd.read_csv('price_prepared.csv', delimiter=';', nrows=1000)

df.fillna(False, inplace=True)
display(df)

print("Усе дадзеныя запоўнены.") if pp.any().empty else print("Некаторыяя дадзеныя пустыя.")

fig, ax = plt.subplots()
ax.set_yscale('log')
ax.boxplot(pp['Square'], vert=False)
ax.set_title('Скрыня з вусамі (лагарыфмічная шкала)')

fig, ax = plt.subplots()
ax.hist(pp['Square'], bins=50)
ax.set_title('Гістаграма')
plt.show()

display(pp)
pp.fillna(0, inplace=True)
display(pp)

pp.to_csv('processed_data.csv', index=False)


# In[ ]:




