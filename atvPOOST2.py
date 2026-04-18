import streamlit as st
import datetime
from classesSt2 import Produto, Fornecedor

st.set_page_config(
    page_title="Gestão de Produtos",
    page_icon="documento.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("Navegação")
opcao = st.sidebar.radio("Escolha uma opção", ["Menu Inicial","Cadastro de Fornecedores", "Cadastro de Produtos"])

if opcao == "Menu Inicial":
    st.header("Bem vindo a Aplicação!")
    st.write("Selecione uma opção no menu lateral")

elif opcao == "Cadastro de Fornecedores":
    st.header("Formulário de Cadastro de Fornecedores")

    with st.form(key="formulario_fornecedores"):
        nome_fornecedor = st.text_input("Nome do Fornecedor")
        cnpj = st.text_input("CNPJ")
        telefone = st.text_input("Telefone")
        email = st.text_input("Email")
        cidade = st.text_input("Cidade")
        submit_fornecedor = st.form_submit_button("Cadastrar Fornecedor")

    if submit_fornecedor:
        valid = True
        if not nome_fornecedor.strip():
            st.error("O nome do fornecedor é obrigatório")
            valid = False
        if not cnpj.strip():
            st.error("O CNPJ é obrigatório")
            valid = False
        if not telefone.strip():
            st.error("O telefone é obrigatório")
            valid = False
        if not email.strip():
            st.error("O email é obrigatório")
            valid = False
        if not cidade.strip():
            st.error("O nome da cidade é obrigatório")
            valid = False

        if valid:

            try:
                fornecedor = Fornecedor(nome_fornecedor, cnpj, telefone, email, cidade)
                st.success("Cadastro de Fornecedor enviado com sucesso!")
                st.write(f"**Nome do Fornecedor:** {fornecedor.get_nome()}")
                st.write(f"**CNPJ:** {fornecedor.get_cnpj()}")
                st.write(f"**Telefone:** {fornecedor.get_telefone()}")   
                st.write(f"**Email:** {fornecedor.get_email()}")    
            except Exception as e:
                st.error(f"Erro ao criar fornecedor: {e}")

elif opcao == "Cadastro de Produtos":
    st.header("Formulário de Cadastro de Produtos")

    with st.form(key="formulario_produtos"):
        nome_produto = st.text_input("Nome do Produto")
        categoria = st.selectbox("Categoria", ["Eletrônicos", "Roupas", "Alimentos", "Móveis"])
        preco = st.number_input("Preço", min_value=0.0, format="%.2f")
        estoque = st.slider("Quantidade em Estoque", min_value=0, step=1, max_value=2500)
        dataValidade = st.date_input("Data de Validade",
                                     min_value=datetime.date.today(),
                                     value=datetime.date.today(),
                                     max_value=datetime.date(2050, 12, 31))
        submit_produto = st.form_submit_button("Cadastrar Produto")

    if submit_produto:
        valid = True
        if not nome_produto.strip():
            st.error("O nome do produto é obrigatório")
            valid = False
        if not categoria.strip():
            st.error("A categoria é obrigatória")
            valid = False
        if preco <= 0:
            st.error("O preço deve ser maior que zero")
            valid = False
        if estoque <= 0:
            st.error("A quantidade em estoque deve ser maior que zero")
            valid = False
        if not isinstance(dataValidade, datetime.date):
            st.error("A data de validade é obrigatória")
            valid = False

        if valid:

            try:
                produto = Produto(nome_produto, categoria, preco, estoque, dataValidade)


                dataFormatada = produto.get_data_validade().strftime("%d/%m/%Y")
                st.success("Cadastro de produto enviado com sucesso!")
                st.write(f"**Nome do Produto:** {produto.get_nome()}")
                st.write(f"**Categoria:** {produto.get_categoria()}")
                st.write(f"**Preço:** R$ {produto.get_preco():.2f}")
                st.write(f"**Quantidade em Estoque:** {produto.get_quantidade_em_estoque()}")
                st.write(f"**Data de Validade:** {dataFormatada}")
            except Exception as e:
                st.error(f"Erro ao criar produto: {e}")
