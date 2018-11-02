
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


pd.options.display.max_rows = 1000
pd.options.display.max_rows


# In[3]:


cor = pd.read_csv("cor_raca_ocupacao.csv", delimiter =';', encoding='latin-1')


# In[4]:


cor.head() # ver as 5ºs linhas


# In[6]:


cor.drop(['Porcentagem (%)', 'Unnamed: 5', 'Abrangência'], axis=1, inplace=True) #apagando o que não quero


# In[7]:


cor["Cor/Raça"].unique() #me mostre o que tem


# In[13]:


Amarela = cor.loc[cor['Cor/Raça']=='Amarela'] #selecionando apenas cor/raça Amarela


# In[17]:


Amarela.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[15]:


Branca = cor.loc[cor['Cor/Raça']=='Branca'] #selecionando apenas cor/raça Branca


# In[16]:


Branca.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[19]:


Indígena = cor.loc[cor['Cor/Raça']=='Indígena'] #selecionando apenas cor/raça Indígena


# In[20]:


Indígena.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[21]:


Parda = cor.loc[cor['Cor/Raça']=='Parda'] #selecionando apenas cor/raça Parda


# In[22]:


Parda.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[23]:


Preta = cor.loc[cor['Cor/Raça']=='Preta'] #selecionando apenas cor/raça Parda


# In[24]:


Preta.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <

