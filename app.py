import streamlit as st
import numpy as np
import pandas as pd 

st.set_page_config(layout="wide")

# Criar as colunas
col1, col2 = st.columns([1, 3])

# Adicionar título ao contêiner
with col1:
    st.sidebar.title("Wallet app v1")
    option = st.selectbox('Selecione o ativo', ('BTC', 'ETH', 'DOT'))
   

# Adicionar informações do ativo selecionado à esquerda
with col1:
    st.subheader(f"{option} Information")
    if option == 'BTC':
        # BTC - Total Value Locked
        st.text("Total Value Locked: $36.769b")
        # BTC - Stablecoins Mcap
        st.text("Stablecoins Mcap: $69.264b")
        # BTC - Fees (24h)
        st.text("Fees (24h): $5.18m")
        # BTC - Revenue (24h)
        st.text("Revenue (24h): $4.27m")
        # BTC - Volume (24h)
        st.text("Volume (24h): $677.55m")
        # BTC - Inflows (24h)
        st.text("Inflows (24h): $55.48m")
        # BTC - Treasury
        st.text("Treasury: $735.78m")

# Adicionar gráfico à direita
with col2:
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.line_chart(chart_data)

# Adicionar informações abaixo das colunas
st.subheader("Informações adicionais")
st.text("Essas informações podem incluir detalhes gerais sobre a plataforma ou qualquer outro conteúdo relevante sobre o ativo.")