from usuario import Usuario

class Professor(Usuario):
    def __init__(self, nome:str="", email:str="",disciplina:str=""):
        super().__init__(nome, email)
        self._disciplina=disciplina

    @property #getter
    def disciplina (self):
        return self._disciplina
    
    @disciplina.setter #setter
    def disciplina (self,disciplina):
        self._disciplina=disciplina


    def RealizarLogin(self,usuario,senha):
        if usuario=="professor" and senha=="456":
            return True, f"Seja bem vindo professor {self._nome}","professor"
        return False, "Login/Senha inválidos pelo perfil Professor", None