import streamlit as st
import numpy as np

def main():
    # Configurar a largura da página
    st.set_page_config(layout="wide")

# Adicionar título ao contêiner
st.title("Visão Geral")

option = st.selectbox(
    'Selecione o ativo',
    ('BTC', 'ETH', 'DOT'))

st.write('Você selecionou:', option)

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



row1 = st.columns(3)
for col in row1:
    tile = col.container(height=120)
    tile.text("data")



