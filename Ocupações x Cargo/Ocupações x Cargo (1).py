
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


pd.options.display.max_rows = 1000
pd.options.display.max_rows


# In[ ]:


profissoes = pd.read_csv("ocupacao_cargo.csv", delimiter =';', encoding='latin-1')


# In[ ]:


profissoes.head() # ver as 5ºs linhas


# In[ ]:


profissoes.drop(['Porcentagem (%)', 'Unnamed: 5', 'Abrangência'], axis=1, inplace=True) #apagando o que não quero


# In[ ]:


profissoes["Cargo"].unique() #me mostre o que tem


# In[ ]:


DeputadoDistrital = profissoes.loc[profissoes['Cargo']=='Deputado Distrital'] #selecionando apenas cargo de Deputado Distrital


# In[ ]:


DeputadoDistrital.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[ ]:


DeputadoEstadual = profissoes.loc[profissoes['Cargo']=='Deputado Estadual'] #selecionando apenas cargo de Deputado Estadual


# In[ ]:


DeputadoEstadual.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[ ]:


DeputadoFederal = profissoes.loc[profissoes['Cargo']=='Deputado Federal'] #selecionando apenas cargo de Deputado Federal


# In[ ]:


DeputadoFederal.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[ ]:


Governador = profissoes.loc[profissoes['Cargo']=='Governador'] #selecionando apenas cargo de Governador


# In[ ]:


Governador.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[ ]:


Senador = profissoes.loc[profissoes['Cargo']=='Senador'] #selecionando apenas cargo de Senador


# In[ ]:


Senador.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[ ]:


SenadorSuplente = profissoes.loc[profissoes['Cargo']=='Senador 1º Suplente'] #selecionando apenas cargo de Senador 1º Suplente


# In[ ]:


SenadorSuplente.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[ ]:


SenadorSuplente2 = profissoes.loc[profissoes['Cargo']=='Senador 2º Suplente'] #selecionando apenas cargo de Senador 2º Suplente


# In[ ]:


SenadorSuplente2.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[ ]:


Vicegovernador = profissoes.loc[profissoes['Cargo']=='Vice-governador']


# In[ ]:


Vicegovernador.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[ ]:


Presidente = profissoes.loc[profissoes['Cargo']=='Presidente'] #selecionando apenas cargo de Presidente


# In[ ]:


Presidente.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <


# In[ ]:


Vicepresidente = profissoes.loc[profissoes['Cargo']=='Vice-presidente'] #selecionando apenas cargo de Vice-presidente


# In[ ]:


Vicepresidente.sort_values(by = "Quantitativo", ascending = False) #ver em ordem de > para <

