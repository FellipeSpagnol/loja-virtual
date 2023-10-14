from produto import Produto
from compra import Compra
from pessoa import Pessoa
from typing import Optional

 
class Loja:
    
    def __init__(self) -> None:
        self.produtos: list[Produto] = []
        self.compras: list[Compra] = []
        self.compra_atual: Optional[Compra] = None
    
    def iniciar_compra(self, usuario: Pessoa) -> bool:
        if self.compra_atual is None:
            self.compra_atual = Compra(usuario)
            return True
        else:
            print('Já há uma compra aberta no momento...')
            print('Por favor, conclua ou cancele a compra atual antes de tentar novamente')
            return False
    
    def buscar_produto(self, nome_produto: str) -> Optional[Produto]:
        for produto in self.produtos:
            if produto.nome == nome_produto:
                return produto
        return None

    def adicionar_produto(self, nome: str, valor: float, categoria: str) -> bool:
        if valor > 0:
            produto = Produto(nome, valor, categoria)
            self.produtos.append(produto)
            return True
        else:
            return False
    
    def cancelar_compra(self) -> None:
        self.compra_atual = None
    
    def concluir_compra(self) -> bool:
        if self.compra_atual is not None:
            for item in self.compra_atual.itens:
                for produto in self.produtos:
                    if item.produto == produto:
                        produto.registrar_venda(item.quantidade)
            return True
        else:
            print('Não há nenhuma compra aberta no momento...')
            return False
    