from produto import Produto
from compra import Compra
from pessoa import Pessoa
from typing import Optional
import pickle


class Loja:

    def __init__(self) -> None:
        self.produtos: list[Produto] = []
        self.compras: list[Compra] = []
        self.compra_atual: Optional[Compra] = None
        self.usuarios: list[Pessoa] = []

    def salvar(self):
        dados = {
            'produtos': self.produtos,
            'compras': self.compras,
            'usuarios': self.usuarios
        }

        with open('backup_loja.pkl', 'wb') as arquivo:
            pickle.dump(dados, arquivo)

    def carregar(self):
        try:
            with open('backup_loja.pkl', 'rb') as arquivo:
                dados = pickle.load(arquivo)

                self.produtos = dados['produtos']
                self.compras = dados['compras']
                self.usuarios = dados['usuarios']

        except FileNotFoundError:
            self.salvar()

    def iniciar_compra(self, usuario: Pessoa) -> bool:
        if self.compra_atual is None:
            if usuario not in self.usuarios:
                self.usuarios.append(usuario)
            self.compra_atual = Compra(usuario)
            return True
        else:
            return False

    def buscar_produto(self, nome_produto: str) -> Optional[Produto]:
        for produto in self.produtos:
            if produto.nome.title() == nome_produto.title():
                return produto
        return None

    def adicionar_produto(self, nome: str, valor: float, categoria: str) -> bool:
        if valor > 0:
            produto = Produto(nome, valor, categoria)
            if produto not in self.produtos:
                self.produtos.append(produto)
            else:
                print('\nProduto Já Registrado...')
                return False
            return True
        else:
            print('Valor Inválido...')
            return False

    def cancelar_compra(self) -> bool:
        if self.compra_atual is not None:
            self.compra_atual = None
            return True
        else:
            return False

    def concluir_compra(self) -> bool:
        if self.compra_atual is not None:
            for item in self.compra_atual.itens:
                for produto in self.produtos:
                    if item.produto == produto:
                        if not produto.registrar_venda(item.quantidade):
                            print(
                                f'\nEstoque do Produto {produto.nome} Insuficiente...')
                        else:
                            item.valor_final = produto.valor() * item.quantidade

            self.compras.append(self.compra_atual)
            self.compra_atual = None
            return True
        else:
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
            for item in compra.itens:
                sum += item.valor_final

        return sum

    def valor_medio_das_compras(self) -> float:
        if self.numero_de_vendas() > 0:
            return self.valor_total_vendido() / self.numero_de_vendas()
        else:
            return 0

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
            return None

    def compras_por_usuario(self) -> None:
        if self.numero_de_usuarios() > 0:
            print('\n< COMPRAS POR USUÁRIO >')
            for usuario in self.usuarios:
                valor_total = 0

                for compra in self.compras:
                    for item in compra.itens:
                        if compra.usuario == usuario:
                            valor_total += item.valor_final

                print(f'\n> {usuario.nome}')
                print(f'CPF: {usuario.cpf}')
                print(f'Valor Total Gasto: R${valor_total:.2f}')
        else:
            print('\nNão há usuários cadastrados...')

    def produtos_mais_caros(self, numero_produtos: int) -> Optional[list]:
        if self.numero_de_produtos() > 0:
            dict_produtos = {produto: produto.valor()
                             for produto in self.produtos}

            num_disponivel = numero_produtos if (
                self.numero_de_produtos() >= numero_produtos) else self.numero_de_produtos()

            dict_ordenado = dict(sorted(dict_produtos.items(
            ), key=lambda item: item[1], reverse=True)[:num_disponivel])

            list = [produto for produto in dict_ordenado]

            return list
        else:
            return None

    def produtos_mais_vendidos(self, numero_produtos: int) -> None:
        if self.numero_de_produtos() > 0:
            dict_produtos: dict[Produto, list] = {}

            for produto in self.produtos:
                contador = 0
                valor_final = 0
                for compra in self.compras:
                    for item in compra.itens:
                        if produto == item.produto:
                            contador += item.quantidade
                            valor_final += item.valor_final
                print(valor_final)
                dict_produtos[produto] = [contador, valor_final]

            num_disponivel = numero_produtos if (
                self.numero_de_produtos() >= numero_produtos) else self.numero_de_produtos()

            dict_ordenado = dict(sorted(dict_produtos.items(
            ), key=lambda item: item[1], reverse=True)[:num_disponivel])

            print(f'\n< {num_disponivel} PRODUTOS MAIS VENDIDOS >')
            for produto in dict_ordenado:
                print(f'> {produto.nome}')
                print(f'Número de Vendas: {dict_ordenado[produto][0]}')
                print(
                    f'Valor Obtido: R${dict_ordenado[produto][1]:.2f}\n')
        else:
            print('Não há produtos cadastrados...\n')
