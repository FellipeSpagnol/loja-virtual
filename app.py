from loja import Loja
from pessoa import Pessoa
from produto import Produto


class App:

    def __init__(self) -> None:
        self.loja = Loja()
        self.loja.carregar()

    def excecutar(self) -> None:
        while (True):
            self.menu()

            opcao = input('> Informe a Opção Desejada: ')

            if opcao == '1':
                print('\n< CADASTRO DE PRODUTO >')
                nome = input('Nome: ')
                valor = float(input('Valor: '))
                categoria = input('Categoria: ')

                if self.loja.adicionar_produto(nome, valor, categoria):
                    print('Produto Registrado!')

            elif opcao == '2':
                print('\n< PRODUTOS REGISTRADOS >')

                for i in range(len(self.loja.produtos)):
                    print(f'\n{i + 1}> {self.loja.produtos[i].nome}')
                    print(f'> Valor: R${self.loja.produtos[i].valor()}')

            elif opcao == '3':
                print('\n< DETALHES DE PRODUTO >')
                nome = input('\nInforme o Nome do Produto: ')

                produto = self.loja.buscar_produto(nome)
                if produto is not None:
                    print(f'\n> {produto.nome}')
                    print(f'Categoria: {produto.categoria}')
                    print(f'Valor Bruto: R${produto.valor_bruto()}')
                    print(f'Valor Desconto: R${produto.valor_desconto()}')
                    print(f'Estoque Disponível: R${produto.estoque}')
                else:
                    print(f'O produto com "{nome}" não foi encontrado...')

            elif opcao == '4':
                print('\n< ATUALIZAÇÃO DE DESCONTO >')
                nome = input('\nInforme o Nome do Produto: ')

                produto = self.loja.buscar_produto(nome)
                if produto is not None:
                    desconto = float(
                        input('\nInforme o Novo Desconto Percentual: '))
                    if produto.atualizar_desconto(desconto):
                        print('Desconto Atualizado!')
                    else:
                        print('Valor Inválido...')
                else:
                    print(f'O produto com "{nome}" não foi encontrado...')

            elif opcao == '5':
                print('\n< REGISTRO DE AQUISIÇÃO >')
                nome = input('\nInforme o Nome do Produto: ')

                produto = self.loja.buscar_produto(nome)
                if produto is not None:
                    quantidade = int(input('\nInforme o Número de Unidades: '))
                    if produto.registrar_aquisicao(quantidade):
                        print('Aquisição Registrada!')
                    else:
                        print('Quantidade Inválida...')
                else:
                    print(f'O produto com "{nome}" não foi encontrado...')

            elif opcao == '6':
                print('\n< REMOÇÃO DE PRODUTO >')
                nome = input('\nInforme código do produto: ')

                produto = self.loja.buscar_produto(nome)
                if produto is not None:
                    self.loja.produtos.remove(produto)
                    print('Produto Removido!')
                else:
                    print(f'O produto com "{nome}" não foi encontrado...')

            elif opcao == '7':
                print('\n< INICIALIZAÇÃO DE COMPRA >')

                nome = input('\nInforme o Nome do Usuário: ')
                email = input('\nInforme o e-mail do Usuário: ')
                cpf = input('\nInforme o CPF do Usuário: ')

                usuario = Pessoa(nome, email, cpf)
                if usuario not in self.loja.usuarios:
                    if self.loja.iniciar_compra(usuario):
                        print('Compra Iniciada!')
                    else:
                        print('Já há uma compra aberta no momento...')
                        print(
                            'Por favor, conclua ou cancele a compra atual antes de tentar novamente')
                else:
                    print('Já há um usuário com pelo menos um dos dados...')

            elif opcao == '8':
                if self.loja.cancelar_compra():
                    print('\nCompra Cancelada!')
                else:
                    print('Não há nenhuma compra aberta no momento...')

            elif opcao == '9':
                if self.loja.concluir_compra():
                    print('\nCompra Concluida!')
                else:
                    print('Não há nenhuma compra aberta no momento...')

            elif opcao == '10':
                if self.loja.compra_atual is not None:
                    print('\n< ADIÇÃO DE ITEM >')
                    nome = input('\nInforme código do produto: ')

                    produto = self.loja.buscar_produto(nome)
                    if produto not in self.loja.produtos:
                        if produto is not None:
                            quantidade = int(
                                input('\nInforme o Número de Unidades: '))
                            if self.loja.compra_atual.adicionar_item(produto, quantidade):
                                print('Item Adicionado!')
                            else:
                                print('Quantidade Inválida...')
                    else:
                        print('Esse Produto Já Está no Carrinho...')
                else:
                    print('\nNão há nenhuma compra aberta no momento...')

            elif opcao == '11':
                if self.loja.compra_atual is not None:
                    self.loja.compra_atual.exibir_compra()
                else:
                    print('\nNão há nenhuma compra aberta no momento...')

            elif opcao == '12':
                if self.loja.compra_atual is not None:
                    print('\n< REMOÇÃO DE ITEM >')
                    index = int(input('\nInforme o Índice do Item: '))
                    if self.loja.compra_atual.remover_produto(index):
                        print('Item Removido!')
                    else:
                        print('Índice Inválido...')
                else:
                    print('\nNão há nenhuma compra aberta no momento...')

            elif opcao == '13':
                if self.loja.compra_atual is not None:
                    print('\n< ATUALIZAÇÃO DE ITEM >')
                    index = int(input('\nInforme o Índice do Item: '))
                    quantidade = int(input('\nInforme o Índice do Item: '))

                    teste = self.loja.compra_atual.atualizar_quantidade(
                        index, quantidade)

                    if teste[1]:
                        if teste[2]:
                            print('Quantidade Atualizada!')
                        else:
                            print('Índice Inválido...')
                    else:
                        print('Quantidade Inválida...')

            elif opcao == '14':
                print('\n< NÚMERO DE PRODUTOS >')
                print(f'> Total: {self.loja.numero_de_produtos()}')

            elif opcao == '15':
                print('\n< NÚMERO DE VENDAS >')
                print(f'> Total: {self.loja.numero_de_vendas()}')

            elif opcao == '16':
                print('\n< VALOR TOTAL VENDIDO >')
                print(f'> Total: R${self.loja.valor_total_vendido():.2f}')

            elif opcao == '17':
                print('\n< VALOR MÉDIO DAS COMPRAS >')
                print(f'> Total: R${self.loja.valor_medio_das_compras():.2f}')

            elif opcao == '18':
                print('\n< NÚMERO DE PRODUTOS >')
                print(f'> Total: {self.loja.numero_de_usuarios()}')

            elif opcao == '19':
                print('\n< USUÁRIO COM MAIS COMPRAS >')
                usuario = self.loja.usuario_com_mais_compras()
                if usuario is not None:
                    print(f'> Nome Do Usuário: {usuario.nome}')
                else:
                    print('Não Há Usuários Cadastrados...')

            elif opcao == '20':
                numero_produtos = 5
                lista_produtos = self.loja.produtos_mais_caros(numero_produtos)

                if lista_produtos is not None:
                    print(f'\n< {numero_produtos} PRODUTOS MAIS CAROS >')
                    for i in range(len(lista_produtos)):
                        print(
                            f'{i+1} - {lista_produtos[i].nome} (R${lista_produtos[i].valor:.2f})')
                else:
                    print('Não há produtos cadastrados...\n')

            elif opcao == '21':
                numero_produtos = 5
                self.loja.produtos_mais_vendidos(numero_produtos)

            elif opcao == '22':
                self.loja.compras_por_usuario()

            elif opcao == '23':
                self.loja.salvar()
                print(f'\nEncerrando...')
                break
            else:
                print(f'\nOpção Inválida...')

    def menu(self) -> None:
        print('< MENU PRINCIPAL >')

        print('1 ) Cadastrar Produto')
        print('2 ) Visualizar Produtos')
        print('3 ) Detalhar Produto')
        print('4 ) Atualizar Desconto')
        print('5 ) Registrar Aquisição')
        print('6 ) Remover Produto')
        print('7 ) Iniciar Compra')
        print('8 ) Cancelar Compra Atual')
        print('9 ) Finalizar Compra Atual')
        print('10) Adicionar Item na Compra')
        print('11) Visualizar Compra Atual')
        print('12) Remover Item da Compra')
        print('13) Atualizar Item da Compra')
        print('14) Relatório - Número de Produtos')
        print('15) Relatório - Número de Vendas')
        print('16) Relatório - Valor Total Vendido')
        print('17) Relatório - Valor Médio Vendido')
        print('18) Relatório - Número de Usuários')
        print('19) Relatório - Usuário com mais Compras')
        print('20) Relatório - 5 Produtos mais Caros')
        print('21) Relatório - 5 Produtos mais Vendidos')
        print('22) Relatório - Gastos por Pessoa\n')
        print('23) Encerrar Aplicativo')
