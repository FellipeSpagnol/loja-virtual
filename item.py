from produto import Produto


class Item:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.produto = produto
        self.nome = produto.nome
        self.quantidade = quantidade
        self.valor_final = 0.0

    def custo(self) -> float:
        return self.produto.valor() * self.quantidade
