class Funcionario:
    def __init__(self, nome:str, cpf:str,cargo:str,salario:float):
        self.__nome:str = nome
        self.__cpf:str = cpf
        self.__cargo:str = cargo
        self.__salario = float(salario)

    @property
    def get_nome(self)-> str:
        return self.__nome
    @get_nome.setter
    def set_nome(self, nome:str):
        self.__nome = nome

    @property   
    def get_cpf(self)-> str:
        return self.__cpf
    @get_cpf.setter
    def set_cpf(self, cpf:str):
        self.__cpf = cpf
    
    @property
    def get_cargo(self)-> str:
        return self.__cargo
    @get_cargo.setter
    def set_cargo(self, cargo:str):
        self.__cargo = cargo

    @property
    def get_salario(self)-> float:
        return self.__salario
    @get_salario.setter
    def set_salario(self, salario:float):
        self.__salario = float(salario)
    
    def salvar(self):
        return f"Funcionário {self.__nome} salvo com sucesso!"

