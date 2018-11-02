
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


pd.options.display.max_rows = 1000
pd.options.display.max_rows


# In[4]:


profissoes = pd.read_csv("ocupacao_cargo.csv", delimiter =';', encoding='latin-1')


# In[5]:


profissoes.head() # ver as 5ºs linhas


# In[6]:


profissoes.drop(['Porcentagem (%)', 'Unnamed: 5', 'Abrangência'], axis=1, inplace=True) #apagando o que não quero


# In[7]:


profissoes["Cargo"].unique() #me mostre o que tem


# In[8]:


DeputadoDistrital = profissoes.loc[profissoes['Cargo']=='Deputado Distrital'] #selecionando apenas cargo de Deputado Distrital


# In[9]:


DeputadoDistrital.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[10]:


DeputadoEstadual = profissoes.loc[profissoes['Cargo']=='Deputado Estadual'] #selecionando apenas cargo de Deputado Estadual


# In[11]:


DeputadoEstadual.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[12]:


DeputadoFederal = profissoes.loc[profissoes['Cargo']=='Deputado Federal'] #selecionando apenas cargo de Deputado Federal


# In[13]:


DeputadoFederal.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[14]:


Governador = profissoes.loc[profissoes['Cargo']=='Governador'] #selecionando apenas cargo de Governador


# In[15]:


Governador.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[16]:


Senador = profissoes.loc[profissoes['Cargo']=='Senador'] #selecionando apenas cargo de Senador


# In[17]:


Senador.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[18]:


SenadorSuplente = profissoes.loc[profissoes['Cargo']=='Senador 1º Suplente'] #selecionando apenas cargo de Senador 1º Suplente


# In[19]:


SenadorSuplente.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[20]:


SenadorSuplente2 = profissoes.loc[profissoes['Cargo']=='Senador 2º Suplente'] #selecionando apenas cargo de Senador 2º Suplente


# In[21]:


SenadorSuplente2.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[22]:


Vicegovernador = profissoes.loc[profissoes['Cargo']=='Vice-governador']


# In[23]:


Vicegovernador.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[24]:


Presidente = profissoes.loc[profissoes['Cargo']=='Presidente'] #selecionando apenas cargo de Presidente


# In[25]:


Presidente.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[26]:


Vicepresidente = profissoes.loc[profissoes['Cargo']=='Vice-presidente'] #selecionando apenas cargo de Vice-presidente


# In[27]:


Vicepresidente.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <

