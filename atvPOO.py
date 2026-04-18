import streamlit as st
import datetime

st.set_page_config(
    page_title="Cadastro de Candidatos",
    page_icon="documento.png",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Olá Visitante!")
st.header("Selecione uma opção no menu lateral")

st.sidebar.title("Menu Lateral")
areaInterresse = st.sidebar.selectbox("Área de Interesse", ["Tecnologia", "Financeiro", "Marketing", "Recursos Humanos"])
cargoInteresse = st.sidebar.selectbox("Cargo de Interesse", ["Qualquer nível","Estágio", "Júnior", "Pleno", "Sênior"])
remoto = st.sidebar.slider("Disponibilidade para trabalho remoto", 0, 100)


with st.form("formulario_cadastro"):
    st.subheader("Formulário de Cadastro de Candidatos")
    nome = st.text_input("Nome Completo")
    email = st.text_input("E-mail")
    idade = st.number_input("Idade",min_value=18, max_value=65)
    dataNasc = st.date_input("Data de nascimento:", min_value=datetime.date(1960, 1, 1), max_value=datetime.date(2025, 12, 31))
    horarioFavorito = st.text_input("Horário Favorito para Entrevista")
    experiencia = st.text_area("Descreva sua experiência profissional")
    curriculo = st.file_uploader("Anexe seu currículo em PDF", type=["pdf"])
    submit_button = st.form_submit_button("Enviar Cadastro")

    if submit_button:
        st.success("Cadastro enviado com sucesso!")
        st.write(f"**Nome:** {nome}")
        st.write(f"**E-mail:** {email}")
        st.write(f"**Idade:** {idade}")
        st.write(f"**Data de Nascimento:** {dataNasc}")
        st.write(f"**Melhor horário:** {horarioFavorito}")
        st.write(f"**Experiência:** {experiencia}")
        st.write(f"**Área de Interesse:** {areaInterresse}")
        st.write(f"**Cargo de Interesse:** {cargoInteresse}")
        st.write(f"**Disponibilidade para trabalho remoto:** {remoto}%")
        st.write(f"**Currículo:** {curriculo.name if curriculo else 'Nenhum arquivo enviado'}")
