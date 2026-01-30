from main import store
import streamlit as st
import pandas as pd
import plotly.express as px
import locale

# extrair dados
lista_fat = ('Faturamento por Filial', 'Faturamento por Linha', 'Faturamento por Genero', 'Faturamento por Tipo de Cliente')

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
nome = "Gabriel"

def moeda_local(valor):
    return locale.currency(valor, grouping=True)

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

    a.metric(
        "📦 Produtos Vendidos:", 
        store.quantidade_total, 
        border=True, 
        chart_data=list(store.quantidade_por_periodo()['quantidade']), 
        chart_type='Area', 
        delta=list(store.quantidade_por_periodo()['quantidade'])[-1]
        )

    b.metric(
        "💰 Faturamento Total:", 
        moeda_local(store.total_vendido), 
        border=True, 
        chart_data=list(store.vendas_por_periodo(grafico=False)['total']), 
        chart_type='Area', 
        delta=moeda_local(list(store.vendas_por_periodo(grafico=False)['total'])[-1])
        )

    c.metric(
        "🎫 Ticket Medio:", 
        locale.currency(store.ticket_medio, grouping=True), 
        border=True, 
        chart_data=list(store.ticket_medio_por_periodo()['total']), 
        chart_type='Area',
        delta=moeda_local(list(store.ticket_medio_por_periodo()['total'])[-1])
        )

    st.plotly_chart(store.comparativo_faturamento())

ctn_faturamento = st.container(border=True)

ctn_faturamento.write("### 📊 Grafico de Faturamento")
ctn_faturamento.write("Acompanhe o faturamento do seu negocio atravez de diferentes aspectos! Selecione um abaixo:")

fat_choice = ctn_faturamento.pills(
    "Tipo de Grafico",
    lista_fat,
    selection_mode='single',
    label_visibility='collapsed',
    default='Faturamento por Filial'
)

if fat_choice == lista_fat[0]:
    ctn_faturamento.plotly_chart(store.vendas_por_filial())

elif fat_choice == lista_fat[1]:
    ctn_faturamento.plotly_chart(store.vendas_por_linha())

elif fat_choice == lista_fat[2]:
    ctn_faturamento.plotly_chart(store.vendas_por_genero())

elif fat_choice == lista_fat[3]:
    ctn_faturamento.plotly_chart(store.vendas_por_tipo_cliente())