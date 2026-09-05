from graphics import *
from telas.telaRelatorio import telaRelatório
from telas.telaCompra import telaCompraProdutos
from telas.telaCadastro import telaCadastro
from telas.telaVerificacao import telaVerificacao

def telaInicial():
    
    # Tamanho da tela
    win = GraphWin("E-Stock", 1280, 720)

    # Quando é chamada de outras telas, deleta o conteúdo antes de exibir o conteúdo da tela inicial
    win.delete('all')

    # Retângulos Principais
    r1 = Rectangle(Point(72, 36), Point(383.2, 684)).draw(win)
    r2 = Rectangle(Point(1207.1, 36), Point(416.2, 684)).draw(win)

    # Texto E-Stock
    texto = Text(Point(228, 342), "E-Stock")
    texto.setSize(36)
    texto.draw(win)

    # Botões
    buttonCadastro = Rectangle(Point(576.0, 175.0) , Point(756.0, 305.0)).draw(win)
    buttonRelatorio = Rectangle(Point(876.0, 175.0), Point(1056.0, 305.0)).draw(win)
    buttonPesquisa = Rectangle(Point(576.0, 417.0), Point(756.0, 547.0)).draw(win)
    buttonCompra = Rectangle(Point(876.0, 417.0), Point(1056.0, 547.0)).draw(win)

    # Textos para os botões
    textCadastro = Text(Point(666.0, 240.0), "Cadastrar Produto")
    textCadastro.setSize(15)
    textCadastro.draw(win)

    textRelatorio = Text(Point(966.0, 240.0), "Gerar Relatório")
    textRelatorio.setSize(15)
    textRelatorio.draw(win)

    textPesquisa = Text(Point(666.0, 482.0), "Pesquisar Produto")
    textPesquisa.setSize(15)
    textPesquisa.draw(win)

    textCompra = Text(Point(966.0, 482.0), "Lançar Compra")
    textCompra.setSize(15)
    textCompra.draw(win)

    # Loop para controle de navegação entre as páginas, verifica o click
    while True:
        try:
            click = win.getMouse()
        except GraphicsError:
            break 
        x = click.getX()
        y = click.getY()

        # Click gerar relatório
        if 876 <= x <= 1056 and 175 <= y <= 305:
            telaRelatório(win)

        # Click tela compra
        elif 876 <= x <= 1056 and 417 <= y <= 547:
            telaCompraProdutos(win)

        # Click tela cadastro
        elif 576 <= x <= 756 and 175.0 <= y <= 305:
            telaCadastro(win)

        # Click tela pesquisa 
        elif 576 <= x <= 756 and 417 <= y <= 547: 
            telaVerificacao(win)
    win.close()