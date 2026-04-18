import streamlit as st 
from classe import Funcionario

st.set_page_config(
    page_title="Cadastro de Funcionários",
    layout="wide"
)

st.title("Cadastro de Funcionários")
st.header("Preencha o formulário abaixo para cadastrar um novo funcionário.")
with st.form("employee_form"):
    nome = st.text_input("Nome Completo")
    cpf = st.text_input("CPF")
    cargo = st.text_input("Cargo")
    salario = st.number_input("salario", min_value=0.0, format="%.2f")
    botao = st.form_submit_button("Cadastrar Funcionário")

    if botao:
        validacao = True
        if cpf == "" or len(cpf) != 11 or not cpf.isdigit():
            st.error("CPF inválido. Deve conter 11 dígitos numéricos.")
            validacao = False
        elif salario <= 0:
            st.error("O salário deve ser um valor positivo.")
            validacao = False
        else:
            funcionario = Funcionario(nome, cpf, cargo, salario)
            st.write(funcionario.salvar())
            st.success(f"Funcionário {funcionario.get_nome} cadastrado com sucesso!")
            st.write(f"**Nome:** {funcionario.get_nome}")
            st.write(f"**CPF:** {funcionario.get_cpf}")
            st.write(f"**Cargo:** {funcionario.get_cargo}")
            st.write(f"**Salário:** R$ {funcionario.get_salario:.2f}")