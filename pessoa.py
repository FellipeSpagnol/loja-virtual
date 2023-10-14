class Pessoa:

    def __init__(self, nome: str, email: str, cpf: str) -> None:
        self.nome = nome
        self.email = email
        self.cpf = cpf

    def __eq__(self, outro: "Pessoa") -> bool:
        return (self.nome == outro.nome) or (self.email == outro.email) or (self.cpf == outro.cpf)
