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

# Criar colunas com larguras relativas
col1, col2 = st.columns(2)

with col1:
   st.text("A cat bslkalsklkaldsdjfjfhj")
   

with col2:
    tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
    data = np.random.randn(10, 1)
    tab1.subheader("A tab with a chart")
    tab1.line_chart(data)

    tab2.subheader("A tab with the data")
    tab2.write(data)



row1 = st.columns(3)
for col in row1:
    tile = col.container(height=120)
    tile.text("data")



