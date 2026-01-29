from main import store
import streamlit as st
import pandas as pd
import plotly.express as px

# extrair dados
lista_fat = ('Faturamento por Filial', 'Faturamento por Linha', 'Faturamento por Genero', 'Faturamento por Tipo de Cliente', 'Faturamento por Periodo')
lista_rank = ('Ranking por Filial', 'Ranking por Linha de Produto', 'Ranking por Genero')

# tratar aquilo que vem da interface
st.set_page_config(layout='wide', page_title='Dashboard Supermercado')

# construir a interface
st.write('## Dashbord de vendas')

st.write("### Grafico de Faturamento")
fat_choice = st.selectbox('Escolha um tipo de Grafico para exibir seu Faturamento', lista_fat)

if fat_choice == lista_fat[0]:
    st.plotly_chart(store.vendas_por_filial())
elif fat_choice == lista_fat[1]:
    st.plotly_chart(store.vendas_por_linha())
elif fat_choice == lista_fat[2]:
    st.plotly_chart(store.vendas_por_genero())
elif fat_choice == lista_fat[3]:
    st.plotly_chart(store.vendas_por_tipo_cliente())
elif fat_choice == lista_fat[4]:
    st.plotly_chart(store.vendas_por_periodo())

st.divider()

st.write('### Grafico de Avaliações')
rank_choice = st.selectbox("Escolha um tipo de grafico para exibir seu Ranking", lista_rank)

if rank_choice == lista_rank[0]:
    st.plotly_chart(store.ranking_por_filial())
elif rank_choice == lista_rank[1]:
    st.plotly_chart(store.ranking_por_categoria())
elif rank_choice == lista_rank[2]:
    st.plotly_chart(store.ranking_por_genero())
