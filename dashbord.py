from main import store
import streamlit as st
import pandas as pd
import plotly.express as px
import locale

# extrair dados

# tratar aquilo que vem da interface
st.set_page_config(layout='wide', page_title='Dashboard Supermercado')

# construir a interface
st.write(store.vendas_por_filial)