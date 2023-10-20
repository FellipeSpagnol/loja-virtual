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
                if self.loja.numero_de_produtos() > 0:
                    for i in range(len(self.loja.produtos)):
                        print(f'\n{i + 1}> {self.loja.produtos[i].nome}')
                        print(f'> Valor: R${self.loja.produtos[i].valor():.2f}')
                else:
                    print('\nNão Há Produtos Registrados...')

            elif opcao == '3':
                print('\n< DETALHES DE PRODUTO >')
                nome = input('\nInforme o Nome do Produto: ')

                produto = self.loja.buscar_produto(nome)
                if produto is not None:
                    print(f'\n> {produto.nome}')
                    print(f'Categoria: {produto.categoria}')
                    print(f'Valor Bruto: R${produto.valor_bruto():.2f}')
                    print(f'Valor Desconto: R${produto.valor_desconto():.2f}')
                    print(f'Estoque Disponível: {produto.estoque()}')
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
                for usuario_registrado in self.loja.usuarios:
                    if usuario == usuario_registrado:
                        usuario = usuario_registrado
                        break
                
                if self.loja.iniciar_compra(usuario):
                    print('\nCompra Iniciada!')
                else:
                    print('\nJá há uma compra aberta no momento...')
                    print(
                        'Por favor, conclua ou cancele a compra atual antes de tentar novamente')


            elif opcao == '8':
                if self.loja.cancelar_compra():
                    print('\nCompra Cancelada!')
                else:
                    print('\nNão há nenhuma compra aberta no momento...')

            elif opcao == '9':
                if self.loja.concluir_compra():
                    print('\nCompra Concluida!')
                else:
                    print('\nNão há nenhuma compra aberta no momento...')
   
            elif opcao == '10':
                if self.loja.compra_atual is not None:
                    print('\n< ADIÇÃO DE ITEM >')
                    nome = input('\nInforme código do produto: ')

                    produto = self.loja.buscar_produto(nome)
                    if produto is not None:
                        if produto not in self.loja.compra_atual.itens:
                            quantidade = int(input('\nInforme o Número de Unidades: '))
                            if quantidade <= produto.estoque():
                                if self.loja.compra_atual.adicionar_item(produto, quantidade):
                                    print('\nItem Adicionado!')
                                else:
                                    print('\nQuantidade Inválida...')
                            else:
                                print("\nQuantidade Indisponível em Estoque...")
                        else:
                            print('\nEsse Produto Já Está no Carrinho...')    
                    else:
                        print("\nProduto Não Encontrado...")            
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
                    quantidade = int(input('\nInforme a Nova Quantidade: '))

                    teste = self.loja.compra_atual.atualizar_quantidade(
                        index, quantidade)

                    if teste[1]:
                        if teste[2]:
                            print('Quantidade Atualizada!')
                        else:
                            print('Índice Inválido...')
                    else:
                        print('Quantidade Inválida...')
                else:
                    print('\nNão há nenhuma compra aberta no momento...')

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
                print('\n< NÚMERO DE USUÁRIOS >')
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
                            f'{i+1} - {lista_produtos[i].nome} (R${lista_produtos[i].valor():.2f})')
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
            
            elif opcao == '69':
                self.loja.adicionar_produto('a', 1, 'p')
                self.loja.buscar_produto('a').registrar_aquisicao(10)
                
                self.loja.adicionar_produto('b', 2, 'p')
                self.loja.buscar_produto('b').registrar_aquisicao(10)
                
                self.loja.adicionar_produto('c', 3, 'p')
                self.loja.buscar_produto('c').registrar_aquisicao(10)  

                self.loja.adicionar_produto('d', 4, 'p')
                self.loja.buscar_produto('d').registrar_aquisicao(10)

                self.loja.adicionar_produto('e', 5, 'p')
                self.loja.buscar_produto('e').registrar_aquisicao(10)

                self.loja.adicionar_produto('f', 6, 'p')
                self.loja.buscar_produto('f').registrar_aquisicao(10)
                
                self.loja.iniciar_compra(Pessoa('Fellipe', 'fellipe@', '123456789-0'))
                self.loja.compra_atual.adicionar_item(self.loja.buscar_produto('a'), 5)
                self.loja.compra_atual.adicionar_item(self.loja.buscar_produto('b'), 4)
                self.loja.compra_atual.adicionar_item(self.loja.buscar_produto('c'), 3)
                self.loja.compra_atual.adicionar_item(self.loja.buscar_produto('d'), 2)
                self.loja.compra_atual.adicionar_item(self.loja.buscar_produto('e'), 1)
                
                self.loja.concluir_compra()
                
            else:
                print(f'\nOpção Inválida...')


    def menu(self) -> None:
        print('\n< MENU PRINCIPAL >')

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
        print('22) Relatório - Gastos por Pessoa')
        print('23) Encerrar Aplicativo\n')
