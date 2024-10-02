import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

junho = pd.read_csv('Junho.csv')
junho.drop(columns=['Orçamento do conjunto de anúncios','Tipo de orçamento do conjunto de anúncios','Configuração de atribuição','Indicador de resultados','Término','Início dos relatórios','Término dos relatórios','Nome da campanha','Veiculação da campanha'], inplace=True)
junho.head()

julho = pd.read_csv('Julho.csv')
julho.drop(columns=['Orçamento do conjunto de anúncios','Tipo de orçamento do conjunto de anúncios','Configuração de atribuição','Indicador de resultados','Término','Início dos relatórios','Término dos relatórios','Nome da campanha','Veiculação da campanha'], inplace=True)
julho.head()  

agosto = pd.read_csv('Agosto.csv')
agosto.drop(columns=['Orçamento do conjunto de anúncios','Tipo de orçamento do conjunto de anúncios','Configuração de atribuição','Indicador de resultados','Término','Início dos relatórios','Término dos relatórios','Nome da campanha','Veiculação da campanha'], inplace=True)
agosto.head()  

setembro = pd.read_csv('Setembro.csv')
setembro.drop(columns=['Orçamento do conjunto de anúncios','Tipo de orçamento do conjunto de anúncios','Configuração de atribuição','Indicador de resultados','Término','Início dos relatórios','Término dos relatórios','Nome da campanha','Veiculação da campanha'], inplace=True)
setembro.head() 

junho['Mês'] = 'Junho'
julho['Mês'] = 'Julho'
agosto['Mês'] = 'Agosto'
setembro['Mês'] = 'Setembro'

df_concat = pd.concat([junho, julho, agosto, setembro], ignore_index=True)

columns_to_round = ['Custo por resultados', 'Frequência', 'CPC (todos) (BRL)', 'CTR (todos)', 'CPM (custo por 1.000 impressões) (BRL)']
for column in columns_to_round:
  df_concat[column] = df_concat[column].round(2)

df_concat.head()

comparativo_por_mes = comparativo_por_mes.reindex(['Junho', 'Julho', 'Agosto', 'Setembro'])

st.title('Comparativo de Desempenho por Mês - Pelle Rio Preto')

# Criar o gráfico de barras
st.subheader('Gráfico de Comparativo por Mês')
fig, ax = plt.subplots(figsize=(15, 8))
comparativo_por_mes.plot(kind='bar', ax=ax)
plt.title('Comparativo por Mês - Pelle Rio Preto')
plt.xlabel('Mês')
plt.ylabel('Soma de Valores')
plt.xticks(rotation=0)
st.pyplot(fig)
