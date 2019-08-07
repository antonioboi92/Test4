#!/usr/bin/env python
# coding: utf-8

# In[124]:


import pandas as pd
a=[]
b=[]
sum=0
words=pd.read_csv("foglio1.csv",names=["WORD"])
print(words)
results=words.sort_values(["WORD"],axis=0)
print("\n")
print(results)
df=pd.DataFrame(results)
df.to_csv('modifiedfoglio1.csv')
for i in range(0,len(words)):
    a.append(list[i])
print(a)
for i in range(0,len(a)):
    k=a[i].replace(' ','')
    b.append(k)
print(b)

for i in range(0,len(b)):
    sum+=len(b[i])
print("sum of every letters =",sum)
print("number of the words =",len(b))
print("aaverage word lenght =",sum/len(b))    


# In[ ]:





# In[ ]:




