#!/usr/bin/env python
# coding: utf-8

# ## Лабараторная работа № 5 Варыянт 18

# ### Вылічэнні з дапамогай NumPy

# 1. **Вылічыць выраз** 

# $$y=\tan(a+b)^2 - \sqrt[3]{a+1.5} + a*b^5 - \frac{b}{\ln a^2}$$

# In[1]:


import numpy as np

a = 1.21
b = 0.371

y = np.tan(a+b)**2 - np.cbrt(a+1.5) + a*b**5 - b/np.log(a**2)

y


# 2. **Знайсці ацэнкі ўраўнення рэгрэсіі**

# $$\mathbf{A} = (\mathbf{X}^\mathrm{T}\mathbf{X})^{-1}(\mathbf{X}^\mathrm{T}\mathbf{Y})$$

# In[1]:


import numpy as np
import random as r
from IPython.display import display

matrixX = []
matrixY = []

for i in range(12):
    row = [1]
    row.append(r.randint(18, 30))
    row.append(r.randint(60, 82))
    matrixX.append(row)
    
    matrixY.append([round(r.uniform(13.5, 18.6), 1)])

print("Матрыца X:")
display(matrixX)
print("Матрыца Y:")
display(matrixY)

X = np.array(matrixX)
Y = np.array(matrixY)

A = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)
print(f"Вектар ацэнак A:\n{np.matrix(A)}", end='\n\n')

Y_CH = X.dot(A)
print(f"Вектар-праверка Y_CH:\n{np.matrix(Y_CH)}")

