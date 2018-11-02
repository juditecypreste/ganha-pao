
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np


# In[31]:


pd.options.display.max_rows = 1000
pd.options.display.max_rows


# In[32]:


genero = pd.read_csv("ocupacao_genero.csv", delimiter =';', encoding='latin-1')


# In[33]:


genero.head() # ver as 5ºs linhas


# In[34]:


genero.drop(['Porcentagem (%)', 'Unnamed: 5', 'Abrangência'], axis=1, inplace=True) #apagando o que não quero


# In[35]:


genero["Gênero"].unique() #me mostre o que tem


# In[36]:


feminino = genero.loc[cor['Gênero']=='Feminino'] #selecionando apenas o gênero feminino


# In[37]:


feminino.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[38]:


masculino = genero.loc[cor['Gênero']=='Masculino'] #selecionando apenas o gênero masculino


# In[39]:


masculino.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <

