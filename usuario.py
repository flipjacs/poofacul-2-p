class Usuario:
    def __init__(self,nome:str="",email:str=""):
        self._nome=nome
        self._email=email

    @property #getter
    def nome (self):
        return self._nome
    @nome.setter #setter
    def nome (self,nome):
        if not nome.strip() and nome!="":
            return print ("Preencher nome")
        self.nome=nome

    @property #getter
    def email(self):
        return self._email
    @email.setter #setter
    def email(self,email):
        if not email.strip() and email!="":
            return print("Preencher email")
        self._email=email

    def RealizarLogin(self,usuario,senha):
        if usuario=="usuario" and senha=="123":
            return True, f'Seja bem vindo {self._nome}','usuario'
        return False, "Login/senha inválido pelo perfil usuário",None