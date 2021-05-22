#!/usr/bin/env python
# coding: utf-8

# In[81]:


#!pip install "watson-developer-cloud"
get_ipython().system('pip install "ibm-watson"')
#!pip install --upgrade watson-developer-cloud
get_ipython().system('pip install wordcloud')
#!pip install --wordcloud

get_ipython().run_line_magic('pip', 'install --user conversation_analytics_toolkit')

import json
import nltk
import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import ibm_watson
import conversation_analytics_toolkit
from conversation_analytics_toolkit import wa_assistant_skills
from conversation_analytics_toolkit import transformation
from conversation_analytics_toolkit import filtering2 as filtering
from conversation_analytics_toolkit import analysis 
from conversation_analytics_toolkit import visualization 
from conversation_analytics_toolkit import selection as vis_selection
from conversation_analytics_toolkit import wa_adaptor 
from conversation_analytics_toolkit import transcript 
from conversation_analytics_toolkit import flows 
from conversation_analytics_toolkit import keyword_analysis 
from conversation_analytics_toolkit import sentiment_analysis 

pd.options.display.max_colwidth = 150


# In[82]:


# Dados do Workspace a ser acessado. Estas informações foram extraídas do Watson Assistant
WAS_WORKSPACE = "ba8da1b8-596f-4627-b935-79b286b55a7d"
WAS_API_KEY = "zpH0eNRelMOvZsAQFiCrzrxGQC6lIJu-A1nofrdMxgPm"
WAS_URL = "https://api.us-south.assistant.watson.cloud.ibm.com"


# In[83]:


# Estabelecendo a autenticação com as informações do ambiente criado com o Watson Assistant
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(WAS_API_KEY)
assistant = AssistantV1(
    version='2020-04-01',
    authenticator=authenticator
)

assistant.set_service_url(WAS_URL)
original_workspace_id = WAS_WORKSPACE




# In[84]:


# Verifica se é possível estabelecer uma conexão com o workspace

def verifica_workspace(check_workspace_id):
    wksp_notready = True
    
    while(wksp_notready == True):
        print('Testando workspace...' + check_workspace_id)
        workspace = assistant.get_workspace(workspace_id=check_workspace_id).get_result()

        print('Workspace Status: {0}'.format(workspace['status']))
        if workspace['status'] == 'Available':
            wksp_notready = False
            print('Pronto para uso!')
        else:
            print('Em treinamento...aguarde 20 segundos e tente novamente')
            time.sleep(20)

# Imprime os resultados do teste
def printred(str_temp,isbold):
    if isbold:
        print(colored(str_temp, 'red', attrs=['bold']))
    else:
        print(colored(str_temp, 'red'))


# In[85]:


original_workspace = assistant.get_workspace(workspace_id=original_workspace_id, export=True)

verifica_workspace(original_workspace_id)


# In[86]:


# Buscando os registros
workspace=assistant.get_workspace(
    workspace_id=WAS_WORKSPACE,
    export=True
).get_result()

limit_number_of_records=5000
# Filtrando os Logs de Maio/2021 a Junho/2021
query_filter = "response_timestamp>=2021-05-10,response_timestamp<2021-06-30"

# Lendo e Salvando o log para um dataframe do Pandas
df_logs = wa_adaptor.read_logs(assistant, WAS_WORKSPACE, limit_number_of_records, query_filter)


# Passo 1 - Preparando a Skill

# In[87]:


#WAS_WORKSPACE: Contém o ID da Skill do ChatBot
skill_id = WAS_WORKSPACE
assistant_skills = wa_assistant_skills.WA_Assistant_Skills()
assistant_skills.add_skill(skill_id, workspace)


# Passo 2 - Extração e Transformação

# In[88]:



df_logs_canonical = transformation.to_canonical_WA_v2(df_logs, assistant_skills, skill_id_field=None, include_nodes_visited_str_types=True, include_context=True)


# Visualizando o log a ser analisado

# In[89]:


df_logs_to_analyze = df_logs_canonical.copy(deep=False)
with pd.option_context('display.max_rows', 5, 'display.max_columns', None): 
    display(df_logs_to_analyze.head(33))


# Indicadores e métricas de conversas com o chatbot 
# 
# Iniciando com uma visualização do fluxo para medir e descobrir como as conversas progridem em cada retorno da conversa.

# In[90]:


title = "Todas as Conversas"
turn_based_path_flows = analysis.aggregate_flows(df_logs_to_analyze, mode="turn-based", on_column="turn_label", max_depth=400, trim_reroutes=False)
# increase the width of the Jupyter output cell   
display(HTML("<style>.container { width:95% !important; }</style>"))
config = {
    'commonRootPathName': title, # label for the first root node 
    'height': 700, # control the visualization height.  Default 600
    'nodeWidth': 250, 
    'maxChildrenInNode':10, # control the number of immediate children to show (and collapse rest into *others* node).  Default 5
    'linkWidth' : 360,  # control the width between pathflow layers.  Default 360     'sortByAttribute': 'flowRatio'  # control the sorting of the chart. (Options: flowRatio, dropped_offRatio, flows, dropped_off, rerouted)
    'sortByAttribute': 'flowRatio',
    'title': title,
    'mode': "turn-based"
}
jsondata = json.loads(turn_based_path_flows.to_json(orient='records'))
visualization.draw_flowchart(config, jsondata, python_selection_var="selection")


# In[91]:


ano_mes = pd.DatetimeIndex(df_logs_to_analyze['response_timestamp']).to_period('D')
grafico_interacoes = df_logs_to_analyze.groupby(ano_mes).count()[['conversation_id']]
grafico_pessoas = df_logs_to_analyze.groupby(ano_mes).agg({"conversation_id": pd.Series.nunique})


grafico_pessoas.plot.line(legend=False)
plt.title("Quantidade de Acessos ao Francobot")
plt.xlabel("Dia")
plt.ylabel("Quantidade de Acessos")


grafico_interacoes.plot.line(legend=False)
plt.title("Quantidade de Interações com o Francobot")
plt.xlabel("Dia")
plt.ylabel("Quantidade de Interações")


# Nuvem de palavras com os textos procurados no FrancoBot

# In[92]:


nltk.download('stopwords')
text = df_logs_to_analyze.loc[df_logs_to_analyze['request_text'] != '']['request_text']

stopwords = nltk.corpus.stopwords.words('portuguese')
newStopWords = ['Sair', 'Encerramento','Oi', 'Fim', 'Começar']
stopwords.extend(newStopWords)
wordcloud = WordCloud(stopwords=stopwords).generate(' '.join(text))


# Mostra a Nuvem gerada
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

