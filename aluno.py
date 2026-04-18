from usuario import Usuario

class Aluno(Usuario):
    def __init__(self, nome:str="", email:str="",matricula:str=""):
        super().__init__(nome, email)
        self._matricula=matricula

    @property #getter
    def matricula (self):
        return self._matricula
    
    @matricula.setter #setter
    def matricula (self,matricula):
        self._matricula=matricula

    def RealizarLogin(self,usuario,senha):
        if usuario=="aluno" and senha=="789":
            return True, f"Seja bem vindo aluno {self._nome}","aluno"
        return False, "Login/Senha inválidos pelo perfil Aluno", None