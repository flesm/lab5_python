#!/usr/bin/env python
# coding: utf-8

# ## Лабараторная работа № 5 Варыянт 18

# ### Візуалізацыя дадзеных у Matplotlib

# 1. **Работа з графікам і апрацоўка масіваў**

# $$y=\sin\left(\frac{x}{3}\right)+1.2a;\text{ пры } x = 3.567 \text{ и } -5\leq a\leq 12;\text{ }\Delta a = 2.5$$

# In[55]:


import numpy as np
import matplotlib.pyplot as plt

x = 3.567
a_list = np.arange(-5, 12, 2.5)
y_list = []
for i in range(len(a_list)):
    y = np.sin(x/3) + 1.2 * a_list[i]
    y_list.append(round(y, 3))
    
print(f"Спіс аргументаў функцыі: {a_list}")
print(f"Спіс значэнняў функцыі: {y_list}", end='\n\n')

print(f"Найбольшае значэнне фунцыі: {max(y_list)}")
print(f"Найменшае значэнне фунцыі: {min(y_list)}")
mean_y = round(np.mean(y_list), 3)
print(f"Сярэдняе значэнне фунцыі: {mean_y}")
print(f"Колькасць элементаў спіса значэнняў функцыі: {len(y_list)}")
print(f"Адасартыраваны спіс па ўбыванні: {sorted(y_list, reverse=True)}")


print("\n\nГрафік функцыі f(x)")
plt.scatter(a_list, y_list) # кропкі
plt.plot(a_list, y_list) # лінія
plt.xlabel("X", fontsize=15, color='blue') # подпіс асі X
plt.ylabel("Y", fontsize=15, color='red', rotation=0) # подпіс асі Y
plt.xticks(a_list) # дзяленні асі адпавядаюць элементам спісу
plt.yticks(y_list)
plt.xlim(-6, 11) # межы графіка
plt.ylim(-6, 14)
plt.show()

plt.axhline(mean_y, color='green')
plt.xlabel("X", fontsize=15, color='blue')
plt.ylabel("Y", fontsize=15, color='red', rotation=0) 
plt.xlim(-6, 11) 
plt.ylim(-6, 14)
plt.show()


# 2. **Пабудаваць графік функцый**

# $$z1=x^(0.25) + y^(0.25)$$

# $$z2=x^2 - y^2$$

# $$z3=2x + 3y$$

# $$z4=x^2 + y^2$$

# $$z5=2 + 2x + 2y - x^2 - y^2$$

# In[54]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x = np.arange(0, 18, 2.5)
y = np.arange(0, 11, 1.5)
z1, z2, z3, z4, z5 = [], [], [], [], []

for i in range(len(x)):
    z1_val = x[i]**(0.25) + y[i]**(0.25)
    z2_val = x[i]**2 - y[i]**2
    z3_val = 2 * x[i] + 3 * y[i]
    z4_val = x[i]**2 + y[i]**2
    z5_val = 2 + 2*x[i] + 2*y[i] - x[i]**2 - y[i]**2
    
    z1.append(z1_val)
    z2.append(z2_val)
    z3.append(z3_val)
    z4.append(z4_val)
    z5.append(z5_val)
    
print("\n\nГрафік функцыі z1")
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
# plt.xlabel("X", fontsize=15, color='blue')
# plt.ylabel("Y", fontsize=15, color='red') 
# ax.set_zlabel("Z", fontsize=15, color='green') 
ax.scatter(x, y, z1, c='orange')
plt.plot(x, y, z1, c='orange')
plt.show()

print("\n\nГрафік функцыі z2")
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z2, c='y')
plt.plot(x, y, z2, c='y')
plt.show()

print("\n\nГрафік функцыі z3")
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z3, c='b')
plt.plot(x, y, z3, c='b')
plt.show()

print("\n\nГрафік функцыі z4")
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z4, c='m')
plt.plot(x, y, z4, c='m')
plt.show()

print("\n\nГрафік функцыі z5")
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z5, c='c')
plt.plot(x, y, z5, c='c')
plt.show()


# In[ ]:




