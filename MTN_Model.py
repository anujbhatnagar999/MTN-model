#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy.optimize import linprog


# In[10]:


c = [-1,-1,-1,-1,-1,-1,-1,-1]
A = [[124, 56, 61, 68, 117, 75, 98, 125], [126, 62, 63, 72, 115, 89, 98, 122], [129, 78, 68, 69, 95, 83, 92, 111], [112, 65, 67, 63, 102, 78, 97, 111],
    [118, 72, 128, 74, 108, 85, 100, 119], [148, 137, 122, 131, 156, 144, 157, 150],[124, 94, 79, 88, 72, 101, 114, 137], [94, 74, 73, 74, 98, 86, 95, 97,]]
b = [1,1,1,1,1,1,1,1]
x1_bounds = (0, None)
x2_bounds = (0, None)
x3_bounds = (0, None)
x4_bounds = (0, None)
x5_bounds = (0, None)
x6_bounds = (0, None)
x7_bounds = (0, None)
x8_bounds = (0, None)


# In[12]:


ans = linprog(c, A_ub=A, b_ub=b, bounds=[x1_bounds, x2_bounds, x3_bounds, x4_bounds, x5_bounds, x6_bounds, x7_bounds, x8_bounds], method='simplex')
print("GTWCN_Group2")
for i in range(1, len(ans['x'])+1):
	print("x"+str(i), "=", str(ans['x'][i-1]))

print("Zmax =", 1/-ans['fun'])


# In[ ]:




