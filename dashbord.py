from main import store
import streamlit as st
import pandas as pd
import plotly.express as px
import locale

# extrair dados
lista_fat = ('Faturamento por Filial', 'Faturamento por Linha', 'Faturamento por Genero', 'Faturamento por Tipo de Cliente')
lista_rank = ('Ranking por Filial', 'Ranking por Linha de Produto', 'Ranking por Genero')
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

nome = 'Gabriel'

# tratar aquilo que vem da interface
st.set_page_config(layout='wide', page_title='Dashboard Supermercado')

# construir a interface
st.write(f'## Olá, {nome} 👋')
st.write(f"Veja as estatisticas do seu negocio e veja ele crescendo!")

col1, col2 = st.columns([2, 1])

ctn_metodos_pagamento = col2.container(border=True, horizontal_alignment='center')
ctn_metodos_pagamento.markdown("<h4 style='text-align: center;'> Metodos de Pagamento</h4>", unsafe_allow_html=True)
ctn_metodos_pagamento.plotly_chart(store.metodos_pagamento_mais_usados(), use_container_width=False)

with col1:
    a, b, c = st.columns(3)
    a.metric("📦 Produtos Vendidos:",  locale.currency(store.quantidade_total, grouping=True), border=True)
    b.metric("💰 Faturamento Total:",  locale.currency(store.total_vendido, grouping=True), border=True)
    c.metric("🎫 Ticket Medio:", locale.currency(store.ticket_medio, grouping=True), border=True)

col1.plotly_chart(store.vendas_por_periodo())

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

st.divider()

st.write('### Grafico de Avaliações')
rank_choice = st.selectbox("Escolha um tipo de grafico para exibir seu Ranking", lista_rank)

if rank_choice == lista_rank[0]:
    st.plotly_chart(store.ranking_por_filial())
elif rank_choice == lista_rank[1]:
    st.plotly_chart(store.ranking_por_categoria())
elif rank_choice == lista_rank[2]:
    st.plotly_chart(store.ranking_por_genero())
