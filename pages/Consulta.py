import streamlit as st
import pandas as pd

dados = pd.read_csv("clientes.csv")

st.title("Clientes cadastrado")
st.divider()
st.dataframe(dados)