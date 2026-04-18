import streamlit as st
from usuario import Usuario
from professor import Professor
from aluno import Aluno

if 'autenticado' not in st.session_state:
    st.session_state.autenticado=False
if 'perfil' not in st.session_state:
    st.session_state.perfil=None
if 'mensagem' not in st.session_state:
    st.session_state.mensagem=None

def tela_login():
    st.title('Login')
    perfil=st.selectbox('Escolha o perfil:', ['usuario','aluno','professor'])
    login=st.text_input('Login')
    senha=st.text_input('Senha',type='password')
    
    if perfil=='usuario':
        obj=Usuario()
    elif perfil=='aluno':
        obj=Aluno()
    else:
        obj=Professor()

    if st.button('Confirmar'):
        ok,msg,perfil_autenticado=obj.RealizarLogin(login,senha)
        if ok: 
            st.session_state.autenticado=True
            st.session_state.perfil=perfil_autenticado
            st.session_state.mensagem=msg
        else:
            st.error(msg)

def tela_principal():
    st.title('Tela principal')
    st.success(st.session_state.mensagem) 

    if st.session_state.perfil=="usuario":
        st.write("Conteudo para o Usuario")
    elif st.session_state.perfil=="professor":
        st.write("Conteudo para o Professor")
    elif st.session_state.perfil=="aluno":
        st.write("Conteudo para o Aluno")

    if st.button('Sair'):
        st.session_state.autenticado=False
        st.session_state.perfil=None
        st.session_state.mensagem=""


def main():
    if not st.session_state.autenticado:
        tela_login()
    else:
        tela_principal()

if __name__== "__main__":
    main()