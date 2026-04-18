# classes.py
import datetime

class Produto:
    def __init__(self, nome: str, categoria: str, preco: float, quantidade_em_estoque: int, data_validade: datetime.date):
        # atributos privados (name mangling)
        self.__nome = nome
        self.__categoria = categoria
        self.__preco = float(preco)
        self.__quantidade_em_estoque = int(quantidade_em_estoque)
        if not isinstance(data_validade, datetime.date):
            raise TypeError("data_validade deve ser um datetime.date")
        self.__data_validade = data_validade

    # GETTERS
    def get_nome(self) -> str:
        return self.__nome

    def get_categoria(self) -> str:
        return self.__categoria

    def get_preco(self) -> float:
        return self.__preco

    def get_quantidade_em_estoque(self) -> int:
        return self.__quantidade_em_estoque

    # Atenção: este método existe e é o correto a chamar no Streamlit
    def get_data_validade(self) -> datetime.date:
        return self.__data_validade

    # SETTERS (com validações simples)
    def set_nome(self, novo_nome: str):
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("Nome inválido")
        self.__nome = novo_nome.strip()

    def set_categoria(self, nova_categoria: str):
        if not isinstance(nova_categoria, str) or not nova_categoria.strip():
            raise ValueError("Categoria inválida")
        self.__categoria = nova_categoria.strip()

    def set_preco(self, novo_preco: float):
        novo_preco = float(novo_preco)
        if novo_preco <= 0:
            raise ValueError("Preço deve ser maior que zero")
        self.__preco = novo_preco

    def set_quantidade_em_estoque(self, nova_quantidade: int):
        nova_quantidade = int(nova_quantidade)
        if nova_quantidade < 0:
            raise ValueError("Quantidade em estoque não pode ser negativa")
        self.__quantidade_em_estoque = nova_quantidade

    def set_data_validade(self, nova_data: datetime.date):
        if not isinstance(nova_data, datetime.date):
            raise TypeError("data_validade deve ser um datetime.date")
        self.__data_validade = nova_data


class Fornecedor:
    def __init__(self, nome: str, cnpj: str, telefone: str, email: str, cidade: str):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__telefone = telefone
        self.__email = email
        self.__cidade = cidade

    # GETTERS
    def get_nome(self) -> str:
        return self.__nome

    def get_cnpj(self) -> str:
        return self.__cnpj

    def get_telefone(self) -> str:
        return self.__telefone

    def get_email(self) -> str:
        return self.__email

    def get_cidade(self) -> str:
        return self.__cidade

    # SETTERS
    def set_nome(self, novo_nome: str):
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("Nome inválido")
        self.__nome = novo_nome.strip()

    def set_cnpj(self, novo_cnpj: str):
        if not isinstance(novo_cnpj, str) or not novo_cnpj.strip():
            raise ValueError("CNPJ inválido")
        self.__cnpj = novo_cnpj.strip()

    def set_telefone(self, novo_telefone: str):
        if not isinstance(novo_telefone, str) or not novo_telefone.strip():
            raise ValueError("Telefone inválido")
        self.__telefone = novo_telefone.strip()

    def set_email(self, novo_email: str):
        if not isinstance(novo_email, str) or not novo_email.strip():
            raise ValueError("Email inválido")
        if "@" not in novo_email or "." not in novo_email:
            raise ValueError("Email com formato inválido")
        self.__email = novo_email.strip()

    def set_cidade(self, nova_cidade: str):
        if not isinstance(nova_cidade, str) or not nova_cidade.strip():
            raise ValueError("Cidade inválida")
        self.__cidade = nova_cidade.strip()
