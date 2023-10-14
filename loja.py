from produto import Produto
from compra import Compra
from pessoa import Pessoa
from item import Item
from typing import Optional

 
class Loja:
    
    def __init__(self) -> None:
        self.produtos: list[Produto] = []
        self.compras: list[Compra] = []
        self.compra_atual: Optional[Compra] = None
        self.usuarios: list[Pessoa] = []
    
    def iniciar_compra(self, usuario: Pessoa) -> bool:
        if self.compra_atual is None:
            self.usuarios.append(usuario)
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
    
    def numero_de_produtos(self) -> int:
        return len(self.produtos)
    
    def numero_de_vendas(self) -> int:
        return len(self.compras)
    
    def numero_de_usuarios(self) -> int:
        return len(self.usuarios)
    
    def valor_total_vendido(self) -> float:
        sum = 0
        
        for compra in self.compras:
            sum += compra.custo()
        
        return sum
    
    def valor_medio_das_compras(self) -> float:
        return self.valor_total_vendido() / self.numero_de_vendas()
    
    def usuario_com_mais_compras(self) -> Optional[Pessoa]:
        if self.numero_de_usuarios() > 0:
            usuario_final = None
            contador_final = 0
            
            for usuario in self.usuarios:
                contador = 0
                for compra in self.compras:
                    if compra.usuario == usuario:
                        contador += 1
                
                if contador > contador_final:
                    usuario_final = usuario
                    contador_final = contador
            
            return usuario_final 
        else:
            print('Não há usuarios cadastrados...\n')
            return None
        
    def produtos_mais_caros(self, numero_produtos: int) -> Optional[list[Produto]]:
        if self.numero_de_produtos() > 0:
            dict_produtos = {produto: produto.valor() for produto in self.produtos}
            dict_ordenado = dict(sorted(dict_produtos.items(), key=lambda item: item[1], reverse=True)[:numero_produtos])
            
            return [produto for produto in dict_ordenado]
        else:
            print('Não há produtos cadastrados...\n')
            return None
    
    def produtos_mais_vendidos(self, numero_produtos: int) -> None:
        if self.numero_de_produtos() > 0:
            dict_produtos: dict[Produto, int] = {}
            
            for produto in self.produtos:
                contador = 0
                for compra in self.compras:
                    for item in compra.itens:
                        if produto == item.produto:
                            contador += item.quantidade
                
                dict_produtos[produto] = contador
            
            dict_ordenado = dict(sorted(dict_produtos.items(), key=lambda item: item[1], reverse=True)[:numero_produtos])
            
            print(f'{numero_produtos} PRODUTOS MAIS VENDIDOS')
            for produto in dict_ordenado:
                print(f'> {produto.nome}')
                print(f'Número de Vendas: {dict_ordenado[produto]}')
                print(f'Valor Obtido: {dict_ordenado[produto] * produto.valor()}\n')
        else:
            print('Não há produtos cadastrados...\n')
        
    def compras_por_usuario(self) -> None:
        if self.numero_de_usuarios() > 0:
            print('COMPRAS POR USUÁRIO\n')
            for usuario in self.usuarios:
                valor_total = 0
                
                for compra in self.compras:
                    if compra.usuario == usuario:
                        valor_total += compra.custo()
                
                print(f'> {usuario.nome}')
                print(f'CPF: {usuario.cpf}')
                print(f'Valor Total Gasto: R${valor_total}\n')
        else:
            print('Não há usuários cadastrados...\n')