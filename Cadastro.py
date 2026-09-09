import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome, data_nasc, tipo ):
    if nome and data_nasc <= date.today() and tipo:
        with open ("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{data_nasc}, {tipo}\n")
        st.session_state["sucesso"] = True
        # Resetando campos do formulário
        st.session_state["nome_cliente"] = ""
        st.session_state["dt_nascimento"] = date.today()
        st.session_state["tipo"] = None
        
    else:
        st.session_state["sucesso"] = False


st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="📔"
)

st.title("Cadastro de Clientes")
st.divider()

nome = st.text_input("Digite o nome do Cliente", 
                     key="nome_cliente")

dt_nascimento = st.date_input("Digite a data de Nascimento",
                                format="DD/MM/YYYY",key="dt_nascimento")

tipo = st.selectbox("Tipo do Cliente",
                    ["PJ","PF"],
                    index=None,
                    key="tipo")

btn_cadastrar = st.button("Cadastrar",
                          on_click=gravar_dados,
                          args=[nome, dt_nascimento, tipo])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso",
                   icon="👌")
    else:
        st.error("Problema no cadastro",
                 icon="❌")