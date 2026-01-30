from main import store
import streamlit as st
import pandas as pd
import plotly.express as px
import locale

# extrair dados
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
        border=True
        )

    b.metric(
        "💰 Faturamento Total:", 
        moeda_local(store.total_vendido), 
        border=True
        )

    c.metric(
        "🎫 Ticket Medio:", 
        locale.currency(store.ticket_medio, grouping=True), 
        border=True)

    st.plotly_chart(store.comparativo_faturamento())