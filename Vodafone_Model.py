#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy.optimize import linprog


# In[20]:


c = [-1,-1,-1,-1,-1,-1,-1,-1]
A = [[76, 74,71,88,82,52,76,106], [144,138,122,135,128,63,106,126], [139,137,132,133,72,78,121,127], [132,128,132,137,126,69,112,126],
    [83,85,105,98,92,44,128,102], [125,111,117,122,115,56,99,114],[102,102,108,103,100,50,86,105], [75,78,89,89,81,43,63,103]]
b = [1,1,1,1,1,1,1,1]
x1_bounds = (0, None)
x2_bounds = (0, None)
x3_bounds = (0, None)
x4_bounds = (0, None)
x5_bounds = (0, None)
x6_bounds = (0, None)
x7_bounds = (0, None)
x8_bounds = (0, None)


# In[21]:


ans = linprog(c, A_ub=A, b_ub=b, bounds=[x1_bounds, x2_bounds, x3_bounds, x4_bounds, x5_bounds, x6_bounds, x7_bounds, x8_bounds], method='simplex')
print("GTWCN_Group2")
for i in range(1, len(ans['x'])+1):
	print("x"+str(i), "=", str(ans['x'][i-1]))

print("Zmax =", 1/-ans['fun'])


# In[ ]:




