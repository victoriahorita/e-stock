from graphics import *
from telas.telaRelatorio import gerarColunas

# Descobre qual a linha do item a ser removido e atualiza a quantidade
def removerItem(produtoComprado, quantidadeComprada, codigoProduto):
    dados = {}
    with open('estoque.csv', 'r') as arquivo:
        linhas = arquivo.readlines()  

    for i, linha in enumerate(linhas[1::], start=1):  # Ignora o cabeçalho e inicia a contagem pelo index 1

        colunas = linha.strip().split(';')
        codigoStock = colunas[0]
        produtoStock = colunas[1]
        quantidadeStock = int(colunas[2])

        # Replace susbtitui o caractere escolhido pelo o indicado
        preçoUnitarioStock = float(colunas[3].replace('R$', '').replace(',', '.'))  
        preçoTotalStock = float(colunas[4].replace('R$', '').replace(',', '.')) 

        # Verifica se o produto e código do input informado correspende ao mesmo valor no estoque
        if produtoComprado.upper() == produtoStock.upper() and codigoProduto == codigoStock:

            # Atualiza a quantidade do produto 
            valorAtualizado = quantidadeStock - int(quantidadeComprada)   

            # Atualiza o valor total do produto
            novoPreçoTotal = valorAtualizado * preçoUnitarioStock

            colunas[2] = str(valorAtualizado)  
            colunas[4] = f"R${novoPreçoTotal:.2f}".replace('.', ',')
            
            # Refaz a linha, concatenando as palavras de cada coluna com os valores de quantidade e valor total atualizados
            linhaAtualizada = ';'.join(colunas) + '\n'
           
            # Retorna os dados para atualizar o estoque
            dados = {
                'linha': i,  
                'conteudo': linhaAtualizada,
                'código': codigoStock,
                'quantidade': valorAtualizado,

            }
            return dados
    
# Atualiza o estoque com base nos dados informados
def atualizarStock(produtoComprado, quantidadeComprada, codigoProduto):
    itemComprado = removerItem(produtoComprado, quantidadeComprada, codigoProduto)
    with open('estoque.csv', 'r') as arquivo:
        linhas = arquivo.readlines()  

    index = itemComprado['linha']  # Índice da linha a ser modificada
    conteudo = itemComprado['conteudo'] # Linha com os valores atualizados

    if itemComprado['quantidade'] <= 0:
        linhas.pop(index)  # Remove a linha se a quantidade for zero ou menor
    else:
        linhas[index] = conteudo  # Atualiza a linha com a nova quantidade

    with open('estoque.csv', 'w') as arquivo:
        arquivo.writelines(linhas)  # Atualiza o csv


# Exibe mensagem de sucesso ao fazer a compra
def telaCompraMsg(win):
    
    win.delete('all') # Deleta o conteúdo da tela onde foi chamada antes de exibir a tela de mensagem

    # Pontos de referência
    center_x = win.getWidth() // 2
    center_y = win.getHeight() // 2
    
    # Texto principal
    textTela = Text(Point(center_x, 70), 'Efetuar Compra E-Stock')
    textTela.setSize(20)
    textTela.draw(win)

    # Mensagem de conclusão
    textMensagem = Text(Point(center_x, center_y), 'Compra concluída com sucesso!\nGostaria de realizar outra compra?')
    textMensagem.setSize(20)
    textMensagem.draw(win)
    
    # Botões
    # Botão de continuar
    butttonContinuar = Rectangle(Point(center_x - 125, center_y + 70), Point(center_x - 35, center_y + 100))
    butttonContinuar.setFill("white")
    butttonContinuar.setOutline("black")
    butttonContinuar.draw(win)
    textContinuar = Text(Point(center_x - 80, center_y + 85), 'Continuar')
    textContinuar.setSize(15)
    textContinuar.draw(win)

    # Botão de início
    buttonInicio = Rectangle(Point(center_x - 15, center_y + 70), Point(center_x + 125, center_y + 100))
    buttonInicio.setFill("white")
    buttonInicio.setOutline("black")
    buttonInicio.draw(win)
    textInicio = Text(Point(center_x + 55, center_y + 85), 'Voltar ao Início')
    textInicio.setSize(15)
    textInicio.draw(win)
    
    # Loop para controle de navegação
    while True:
        try:
            click = win.getMouse()
        except GraphicsError:
            break   
        x = click.getX()
        y = click.getY()

        # Verifica o click no botão de continuar
        if center_x - 90 <= x <= center_x + 10 and center_y + 70 <= y <= center_y + 100:
            telaCompraProdutos(win)
        
        # Verifica o click no botão de início
        elif center_x + 30 <= x <= center_x + 180 and center_y + 70 <= y <= center_y + 100:
            win.close()
            from telas.telaInicial import telaInicial
            telaInicial()
    win.close()

# Exibe uma janela menor com os erros ao efetuar a compra
def janelaErro(erros):
    win = GraphWin("Erro", 400, 150)

    # Pontos de referência
    center_x = win.getWidth() // 2
    center_y = win.getHeight() // 2

    # Distância entre as mensagens de erro
    dist = 20

    # Exibindo as mensagens de erro
    for i, erro in enumerate(erros):
        textErro = Text(Point(center_x, center_y - (i * dist)), erro)
        textErro.draw(win)
    
    # Loop para controle do click
    while True:
        try:     # Bloco para evitar o erro de fechar todas as telas ao clicar no x
            click = win.getMouse()  
            win.close()  
            break  
        except GraphicsError:   # Captura o erro de fechar as telas clicando no x
            break  

# Trata os erros ao efetuar a compra
def tratamentoErros(inputCodigo, inputProduto, inputQuantidade):

    # Dados
    colunas = gerarColunas()
    codigos = colunas[0]
    produtos = colunas[1]
    quantidadeProdutos = colunas[2]
    produtosAtualizados = []
    erros = []

    # Lista de produtos em maiúsculas para verificação
    for produto in produtos:
        produtosAtualizados.append(produto.upper())

    # Erro de código não encontrado
    if inputCodigo not in codigos:
        erros.append("Código não encontrado.")
        return erros  
    
    # Erro de produto não encontrado
    if inputProduto.upper() not in produtosAtualizados:
        erros.append("Produto não encontrado.")
        return erros  

    # Verificar se a quantidade é um número válido
    try:
        inputQuantidade = int(inputQuantidade)  # Tenta converter para inteiro
        if inputQuantidade < 0:
            erros.append("Quantidade inválida!\nInforme um valor positivo.")
            return erros
    except:
        erros.append("Quantidade inválida!\nInforme um número válido.")
        return erros

    # Erro de quantidade maior que o estoque ou erro no código/produto
    for index, (codigo, produto, quantidade) in enumerate(zip(codigos, produtosAtualizados, quantidadeProdutos)):
        if inputCodigo == codigo and inputProduto.upper() == produto:
            if inputQuantidade > int(quantidade):
                erros.append(
                    f"Quantidade maior do que o estoque!\nInforme um valor menor.\nEstoque disponível: {quantidade} unidades."
                )
            break
    else:
        # Se nenhum código e produto corresponder
        erros.append("Produto não encontrado para o código especificado.")

    return erros

def telaCompraProdutos(win):

    win.delete('all')  # Deleta o conteúdo da tela anterior

    # Pontos de referência
    center_x = win.getWidth() // 2
    center_y = win.getHeight() // 2
    
    # Texto principal
    textTela = Text(Point(center_x, 70), 'Efetuar Compra E-Stock')
    textTela.setSize(20)
    textTela.draw(win)

    # Inputs e textos
    # Código
    textCodigo = Text(Point(center_x, center_y-50), 'Código')
    textCodigo.setSize(15)
    textCodigo.draw(win)
    inputCódigo = Entry(Point(center_x, center_y), 30)
    inputCódigo.setSize(20)
    inputCódigo.draw(win)

    # Produto
    textProduto = Text(Point(center_x, center_y+40), 'Produto')
    textProduto.setSize(15)
    textProduto.draw(win)
    inputProduto = Entry(Point(center_x, center_y+80), 30)
    inputProduto.setSize(20)
    inputProduto.draw(win)

    # Quantidade
    textQuantidade = Text(Point(center_x, center_y+120), 'Quantidade')
    textQuantidade.setSize(15)
    textQuantidade.draw(win)
    inputQuantidade = Entry(Point(center_x, center_y+160), 30)
    inputQuantidade.setSize(20)
    inputQuantidade.draw(win)

    # Botões
    # Finalizar Compra
    buttonFinalizar = Rectangle(Point(center_x - 95, center_y + 240), Point(center_x + 95, center_y + 290))
    buttonFinalizar.setFill("white")
    buttonFinalizar.setOutline("black")
    buttonFinalizar.draw(win)
    textFinalizar = Text(Point(center_x, center_y + 267), "🛒 Finalizar")
    textFinalizar.setSize(18)
    textFinalizar.draw(win)

    # Tela Inicial
    buttonTelaPrincipal = Rectangle(Point(20, 20), Point(60, 60))
    buttonTelaPrincipal.setFill("white")
    buttonTelaPrincipal.draw(win)
    textTelaPrincipal = Text(Point(40, 40), '🏠')
    textTelaPrincipal.setSize(20)
    textTelaPrincipal.draw(win)

    # Loop para controle de navegação
    while True: 
        click = win.getMouse()  
        x = click.getX()
        y = click.getY()

        # Verifica se o click foi no botão de voltar para a tela principal
        if 20 <= x <= 60 and 20 <= y <= 60:
            win.close()
            from telas.telaInicial import telaInicial
            telaInicial()
        
        # Verificar se o click foi em finalizar
        elif center_x - 95 <= x <= center_x + 95 and center_y + 240 <= y <= center_y + 290: 
            codigo = inputCódigo.getText() 
            produto = inputProduto.getText() 
            quantidade = inputQuantidade.getText()
            
            erros = tratamentoErros(codigo, produto, quantidade)
            if len(erros) > 0:
                janelaErro(erros)  
            else:
                atualizarStock(produto, quantidade, codigo)
                telaCompraMsg(win)