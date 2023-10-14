class Produto:

    def __init__(self, nome: str, valor: float, categoria: str) -> None:
        self.nome = nome
        self._valor = valor
        self._estoque = 0
        self._desconto = 0
        self.categoria = categoria

    def valor(self) -> float:
        return self._valor*(1 - self._desconto)

    def registrar_aquisicao(self, quantidade: int) -> None:
        self._estoque += quantidade

    def registrar_venda(self, quantidade: int) -> bool:
        if (self._estoque - quantidade) >= 0:
            self._estoque -= quantidade
            return True
        else:
            return False

    def estoque(self) -> int:
        return self._estoque

    def atualizar_desconto(self, desconto_novo: float) -> bool:
        if (0 <= desconto_novo <= 1):
            self._desconto = desconto_novo
            return True
        else:
            return False

    def atualizar_valor(self, valor_novo: float) -> bool:
        if (valor_novo > 0):
            self._valor = valor_novo
            return True
        else:
            return False
        
    def __eq__(self, outro: "Produto") -> bool:
        return self.nome == outro.nome
