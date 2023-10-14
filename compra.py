from pessoa import Pessoa
from produto import Produto
from item import Item


class Compra:

    def __init__(self, usuario: Pessoa) -> None:
        self.usuario = usuario
        self.itens: list[Item] = []

    def custo(self) -> float:
        custo = 0

        for item in self.itens:
            custo += item.custo()

        return custo

    def adicionar_item(self, produto: Produto, quantidade: int) -> bool:
        if quantidade > 0:
            item = Item(produto, quantidade)
            self.itens.append(item)
            return True
        else:
            return False

    def exibir_compra(self) -> None:
        print('LISTA DE ITENS')
        for i in range(len(self.itens)):
            print(f'{i+1} > {self.itens[i].produto.nome} ')
            print(f'Valor Unitário: R${self.itens[i].produto.valor():.2f}')
            print(f'Quantidade: {self.itens[i].quantidade}')
            print(f'Valor Total: R${self.itens[i].custo():.2f}\n')

        print(f'VALOR TOTAL DA COMPRA: R${self.custo():.2f}')

    def remover_produto(self, index: int) -> bool:
        if index in range(1, (len(self.itens)+1)):
            self.itens.pop(index-1)
            return True
        else:
            return False

    def atualizar_quantidade(self, index: int, quantidade_nova: int) -> bool:
        if quantidade_nova > 0:
            self.itens[index].quantidade = quantidade_nova
            return True
        else:
            return False
