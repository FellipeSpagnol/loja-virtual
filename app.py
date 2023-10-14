from loja import Loja


class App:
    
    def __init__(self) -> None:
        self.loja = Loja()
    
    def excecutar(self) -> None:
        self.menu()
        
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