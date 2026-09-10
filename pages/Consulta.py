import streamlit as st
import pandas as pd
import altair as alt

# Carregar os dados
dados = pd.read_csv("clientes.csv")

# Ordenar em ordem alfabética pela coluna "nome"
dados = dados.sort_values(by="nome")

st.title("Clientes Cadastrados")
#st.divider()

# Campo de pesquisa
nome_pesquisa = st.text_input("Pesquisar cliente pelo nome:", icon="🔍")

if nome_pesquisa:
    # Filtrar os dados pelo nome digitado que começam com uma letra ou vogal
    resultado = dados[dados["nome"].str.lower().str.startswith(nome_pesquisa.lower(), na=False)]
    st.subheader("Resultado da pesquisa")
    st.dataframe(resultado, hide_index=True)
    contagem_tipo = resultado["tipo"].value_counts()
    st.bar_chart(
        contagem_tipo,
        color="Green",
        width=300,
        horizontal=True,
        height="content")
else:
    st.dataframe(dados, 
                 hide_index=True)
    contagem_tipo = dados["tipo"].value_counts()
    st.bar_chart(
        contagem_tipo,
        color="Green",
        width=300,
        horizontal=True,
        height="content")


