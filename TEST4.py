#!/usr/bin/env python
# coding: utf-8

# In[87]:


import pandas as pd


# In[88]:


words=pd.read_csv("foglio1.csv",names=["WORD"])


# In[89]:


print(words)


# In[90]:


results=words.sort_values(["WORD"],axis=0)


# In[91]:


print(results)


# In[92]:


df=pd.DataFrame(results)


# In[93]:


print(df)


# In[94]:


df.count()


# In[95]:


df.to_csv('modifiedfoglio1.csv')


# In[ ]:





# In[96]:


a=[]

for i in range(0,len(list)):
    a.append(list[i])
    

 


# In[97]:


print(a)


# In[98]:


b=[]

for i in range(0,len(a)):
    k=a[i].replace(' ','')
    b.append(k)
    
    


# In[99]:


print(b)


# In[100]:


print(len(b[2]))


# In[101]:


sum=0
for i in range(0,len(b)):
    sum+=len(b[i])

print(sum)
print(len(b))
print(sum/len(b))
    


# In[ ]:




