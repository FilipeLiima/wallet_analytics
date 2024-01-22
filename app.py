import streamlit as st
import numpy as np

st.set_page_config(layout="wide")

# Criar as colunas
row1 = st.columns(1)
row2 = st.columns(3)

# Adicionar título ao contêiner
with row1[0].container():
    st.title("Wallet app v1")

option = st.selectbox(
    'Selecione o ativo',
    ('BTC', 'ETH', 'DOT'))

st.write('Você selecionou:', option)

# Título da barra lateral
st.sidebar.title("Informações do Ethereum (ETH)")

# Ethereum - Total Value Locked
st.sidebar.markdown("### Total Value Locked: $36.769b")

# Ethereum - Stablecoins Mcap
st.sidebar.markdown("### Stablecoins Mcap: $69.264b")

# Ethereum - Fees (24h)
st.sidebar.markdown("### Fees (24h): $5.18m")

# Ethereum - Revenue (24h)
st.sidebar.markdown("### Revenue (24h): $4.27m")

# Ethereum - Volume (24h)
st.sidebar.markdown("### Volume (24h): $677.55m")

# Ethereum - Inflows (24h)
st.sidebar.markdown("### Inflows (24h): $55.48m")

# Ethereum - Treasury
st.sidebar.markdown("### Treasury: $735.78m")

# Criar coluna
col1 = st.columns(1)[0]

# Adicionar abas à coluna
with col1:
    tabs = st.tabs(["📈 Chart", "🗃 Data"])

    # Conteúdo da primeira aba (gráfico)
    with tabs[0]:
        data_chart = np.random.randn(10, 1)
        st.subheader("A aba com um gráfico")
        st.line_chart(data_chart)

    # Conteúdo da segunda aba (dados)
    with tabs[1]:
        data_table = np.random.randn(10, 1)
        st.subheader("A aba com os dados")
        st.write(data_table)






