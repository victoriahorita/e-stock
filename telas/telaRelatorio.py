from graphics import *

# Gera as colunas de cada item no estoque
def gerarColunas():
    with open('estoque.csv', 'r', encoding='utf-8') as arquivo:
        linha = arquivo.readline()

        coluna0 = []   # Coluna do código
        coluna1 = []   # Coluna do produto
        coluna2 = []   # Coluna da quantidade
        coluna3 = []   # Coluna do preço unitário
        coluna4 = []   # Coluna do preço total

        while linha:   # Separa a linha em palavras e adiciona cada palavra em sua coluna, de acordo com o index
            palavras = linha.strip().split(';')  
            coluna0.append(palavras[0])
            coluna1.append(palavras[1])
            coluna2.append(palavras[2])
            coluna3.append(palavras[3])
            coluna4.append(palavras[4])
                
            linha = arquivo.readline()
        colunas = [coluna0, coluna1, coluna2, coluna3, coluna4]
    return colunas

# Descobre o maior elemento de cada coluna para calcular a quantidade de espaços para o alinhamento da linha
def espaçosAlinhamento(coluna, tamanho_palavra):
    maior = cont = 0

    for palavra in coluna:
        cont += 1
        if cont == 1:
            maior = len(palavra)
        else:
            if len(palavra)  > maior:
                maior = len(palavra) 
            
    qtdEspaços = maior + 8 - tamanho_palavra
    return qtdEspaços


# Alinha as linhas do relatório
def dadosRelatório():
    colunas = gerarColunas()
    linhas = []

    with open('estoque.csv', 'r', encoding='utf-8') as arquivo:
        linha = arquivo.readline()
       
        while linha:
            palavras = linha.strip().split(';')
            linhaAlinhada = ''

            for index, palavra in enumerate(palavras):
                qtdEspaços = espaçosAlinhamento(colunas[index], len(palavra))
                linhaAlinhada += palavra + qtdEspaços * ' '
                
            linhas.append(linhaAlinhada)
            linha = arquivo.readline() 
    return linhas

# Gera o relátório por páginas
def gerarRelatorio(win, pagina, totalPaginas, relatorio):
    center_x = win.getWidth() // 2
    y_position = 225  
    textosExibidos = []  

    relatorio = relatorio[1::]   # Removendo o cabeçalho
    começo = (pagina - 1) * 15
    fim = min(pagina * 15, len(relatorio))  # Verifica o menor número para o fim 

    # Atualiza o título da página
    textoTitulo = Text(Point(300, 160), f'Página {pagina} de {totalPaginas}, Itens {começo+1}-{fim}')
    textoTitulo.setFace('courier')
    textoTitulo.setSize(12)
    textoTitulo.draw(win)
    textosExibidos.append(textoTitulo)

    # Atualiza a página de itens
    for linha in relatorio[começo:fim]:
        textLinha = Text(Point(690, y_position), linha)
        textLinha.setFace('courier')
        textLinha.setSize(12)
        textLinha.draw(win)
        y_position += 25  

        textosExibidos.append(textLinha) 
    return textosExibidos

def telaRelatório(win):
    win.delete('all')  # Deleta todo o conteúdo da tela em que foi chamado para depois exibir o conteúdo da tela do relatório
    
    # Pontos de referência
    center_x = win.getWidth() // 2
    center_y = win.getWidth() // 2

    # Texto principal
    textTela = Text(Point(center_x, 70), 'Relatório E-Stock')
    textTela.setSize(20)
    textTela.draw(win)

    # Linhas da Tabela 
    linha = Line(Point(170, 180), Point(1110, 180)).draw(win)
    linha = Line(Point(170, 595), Point(1110, 595)).draw(win)

    # Botões
    # Próximo página 
    buttonPróximo = Rectangle(Point(1080, 150), Point(1110, 170))
    buttonPróximo.setOutline("black")
    buttonPróximo.draw(win)
    setaPróximo = Text(Point(1095, 160), '>').draw(win)

    # Página Anterior
    buttonAnterior = Rectangle(Point(1040, 150), Point(1070, 170))
    buttonAnterior.setOutline("black")
    buttonAnterior.draw(win)
    setaAnterior = Text(Point(1055, 160), '<').draw(win)

    # Voltar para tela principal
    buttonTelaPrincipal = Rectangle(Point(20, 20), Point(60, 60))
    buttonTelaPrincipal.draw(win)
    textTelaPrincipal = Text(Point(40, 40), '🏠')
    textTelaPrincipal.setSize(20)
    textTelaPrincipal.draw(win)

    # Dados do relatório com as linhas alinhadas
    relatorio = dadosRelatório()

    # Texto Cabeçalho
    textCabeçalho = Text(Point(center_x+50, 200), relatorio[0]) 
    textCabeçalho.setFace('courier')
    textCabeçalho.setStyle('bold')
    textCabeçalho.setSize(12)
    textCabeçalho.draw(win)

    # Número da página inicial e cálculo da quantidade total de páginas
    pagina = 1
    totalPaginas = (len(relatorio) - 1) // 15
    if (len(relatorio) - 1) % 15 > 0:
        totalPaginas += 1
   
    # Exibição da primeira página do relatório
    textosExibidos = gerarRelatorio(win, pagina, totalPaginas, relatorio)

    # Loop para controle de navegação
    while True:
        try:
            click = win.getMouse()
        except GraphicsError:
            break 
        x = click.getX()
        y = click.getY()

        # Verifica se o click foi no botão Próximo
        if 1080 <= x <= 1110 and 150 <= y <= 170 and pagina < totalPaginas:
            # Atualiza o número da página
            pagina += 1
            
            # Remove os textos da página atual
            for item in textosExibidos:   
                item.undraw()  

            # Gera os textos para a próxima página e atualiza a lista
            textosExibidos = gerarRelatorio(win, pagina, totalPaginas, relatorio)

        # Verifica se o click foi no botão Anterior
        elif 1040 <= x <= 1070 and 150 <= y <= 170 and pagina > 1:
            # Atualiza o número da página
            pagina -= 1

            # Remove os textos da página atual
            for item in textosExibidos:
                item.undraw() 

            # Gera os textos para a página anterior e atualiza a lista
            textosExibidos = gerarRelatorio(win, pagina, totalPaginas, relatorio)
        
        # Verifica se o click foi no botão de voltar para a tela principal
        elif 20 <= x <= 60 and 20 <= y <= 60:
            win.close()
            from telas.telaInicial import telaInicial
            telaInicial()
    win.close()