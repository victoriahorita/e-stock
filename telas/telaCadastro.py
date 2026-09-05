from graphics import *

#Tela de mensagem de confirmação do cadastro
def telaConfirma(win, telaCad, campos):
    #Pontos de referência
    center_x = win.getWidth() // 2
    center_y = win.getHeight() // 2

    #Mensagem principal
    confirmacao = Text(Point(center_x, center_y - 20), "Cadastro realizado com sucesso!\nDeseja continuar cadastrando?")
    confirmacao.setSize(15)
    confirmacao.draw(win)
    
    #Botões e escrita de dentro dos botões
    btnSim = Rectangle(Point(center_x - 80, center_y + 20), Point(center_x - 8, center_y + 50))
    btnSim.setFill("white")
    btnSim.setOutline("black")
    btnSim.draw(win)

    icnSim = Text(Point(center_x - 45, center_y + 35), "Continuar")
    icnSim.draw(win)

    btnSair = Rectangle(Point(center_x + 7, center_y + 20), Point(center_x + 75, center_y + 50))
    btnSair.setFill("white")
    btnSair.setOutline("black")
    btnSair.draw(win)

    icnSair = Text(Point(center_x + 40, center_y + 35), "Cancelar")
    icnSair.draw(win)

    #Tratamento de exceção
    while not win.isClosed():
        try:
            click = win.getMouse()
        except GraphicsError:
            break  

        #Verifica onde foi o click e realiza ação esperada
        if center_x - 80 <= click.x <= center_x -8 and center_y + 20 <= click.y <= center_y + 50:
            win.close()
            for campo in campos:
                campo.setText("")
            break

        elif center_x + 7 <= click.x <= center_x + 75 and center_y + 20 <= click.y <= center_y + 50:
            if not telaCad.isClosed():
                telaCad.close()
            if not win.isClosed():
                win.close()
            #Retorna a tela inicial
            from telas.telaInicial import telaInicial
            telaInicial()
            break

#Tela de mensagem caso seja encontrado um produto com mesmo nome
def mensagem(win, telaCad, campos, verificacao):
    center_x = win.getWidth() // 2
    center_y = win.getHeight() // 2
    mensagem = "erro"

    #Muda a mensagem de acordo com a situação
    if verificacao == "cadastraNovo":
        mensagem = "Este produto já existe no estoque.\nDeseja cadastrar um novo produto?"
        print(f"{verificacao}")
    elif verificacao == "adicionaQuantidade":
        mensagem = "Este produto foi encontrado no estoque\ne a quantidade foi atualizada!"
    
    #Mensagem principal
    confirmacao = Text(Point(center_x, center_y - 20), mensagem)
    confirmacao.draw(win)
    confirmacao.setSize(15)
    
    #Botões e escrita de dentro deles
    btnSim = Rectangle(Point(center_x - 80, center_y + 20), Point(center_x - 8, center_y + 50))
    btnSim.setFill("white")
    btnSim.setOutline("black")
    btnSim.draw(win)

    icnSim = Text(Point(center_x - 45, center_y + 35), "Continuar")
    icnSim.draw(win)

    btnSair = Rectangle(Point(center_x + 7, center_y + 20), Point(center_x + 75, center_y + 50))
    btnSair.setFill("white")
    btnSair.setOutline("black")
    btnSair.draw(win)

    icnSair = Text(Point(center_x + 40, center_y + 35), "Cancelar")
    icnSair.draw(win)


    #Tratamento de exceção
    while not win.isClosed():
        try:
            click = win.getMouse()
        except GraphicsError:
            break  

        #Realiza ação esperada de acordo com o lugar do click
        if center_x - 80 <= click.x <= center_x -8 and center_y + 20 <= click.y <= center_y + 50:
            win.close()
            for campo in campos:
                campo.setText("")
            if verificacao == "cadastraNovo":
                return False
            
            return True

        elif center_x + 7 <= click.x <= center_x + 50 and center_y + 20 <= click.y <= center_y + 50:
            if not telaCad.isClosed():
                telaCad.close()
            if not win.isClosed():
                win.close()
            #Retorna a tela inicial
            from telas.telaInicial import telaInicial
            telaInicial()

#Função para cadastrar novo item
def cadastra(codigo, produto, qtde, precoUnit, precoTotal):
    #Tratamento de exceção
    try:
        qtde = int(qtde)
        codigo = int(codigo)
    except ValueError:
        return False
    
    #Muda o ponto pra vírgula, caso o usuário tenha inserido valor com ponto
    unitarioCerto = ''
    totalCerto = ''
    precoUnit = f"R${precoUnit}"
    precoTotal = f"R${precoTotal}"

    for letra in precoUnit:
        if letra == ".":
            unitarioCerto += ","
        else:
            unitarioCerto += letra

    for letra in precoTotal:
        if letra == ".":
            totalCerto += ","
        else:
            totalCerto += letra
    
    #Monta uma linha e adiciona linha no arquivo
    linha = f"\n{codigo};{produto};{qtde};{unitarioCerto};{totalCerto}"
    arq = open("estoque.csv", "a", encoding='utf-8')
    if arq.write(linha):
        arq.close()
        return True
    
    arq.close()
    return False

#Função que verifica se o produto já existe no estoque
def existe(produto, precoUnit):
    #Deixa minúsculo para comparar 
    produto = produto.lower()
    arq = open("estoque.csv", "r", encoding="utf-8")
    arquivo = arq.readlines()
    lista = []
    precoCerto = ''

    #Criando uma lista a partir do arquivo
    for linha in arquivo:
        linha = linha.split(";")
        lista.append(linha)

    #Mudando ponto para vírgula
    for letra in precoUnit:
        if letra == ".":
            precoCerto += ","
        else:
            precoCerto += letra

    precoUnit = f"R${precoCerto}"

    #Verifica se o produto existe no estoque e se o preço é o mesmo que foi informado
    for linha2 in lista[1:]:
        nome = str(linha2[1]).lower()
        preco = linha2[3]
        if nome == produto and preco == precoUnit:
            return f"adicionaQuantidade"
        elif nome == produto and preco != precoUnit:
            return f"cadastraNovo"
        
    arq.close()
    return False

#Função para incrementar o código a partir do código do último item do estoque
def novoCodigo():
    arq = open("estoque.csv", "r", encoding="utf-8")
    arquivo = arq.readlines()
    lista = []
    for linha in arquivo:
        linha = linha.split(";")
        lista.append(linha)
    arq.close()
    #Pega o código do último item do estoque
    codigo = (lista[len(lista)-1][0])
    #Retorna adicionando 1
    return int(codigo) + 1

#Função que atualiza uma linha do estoque
def atualizaLinha(produto, quantidade):
    try:
        quantidade = int(quantidade)
    except ValueError:
        return False
    produto = produto.lower()
    arq = open("estoque.csv", "r", encoding="utf-8")
    arquivo = arq.readlines()
    arq.close()

    lista = []
    #Para cada linha, remove espaços sem sentido e separa os itens a partir do ";"
    for linha in arquivo:
        lista.append(linha.strip().split(";"))

    cont = 0
    while cont < len(lista):
        linha = lista[cont]
        #Pega o nome do produto e deixa minúsculo para comparar
        nome = linha[1].lower()
        if nome == produto:
            unitario = ''
            #Remove o "R$" do preço e troca vírgula por ponto para fazer o cálculo
            for letra in linha[3]:
                if letra != "R" and letra != "$" and letra != ",":
                    unitario += letra
                elif letra == ",":
                    unitario += "."

            linha[2] = str(int(linha[2]) + int(quantidade))  #Atualiza a quantidade
            total = float(linha[2]) * float(unitario) #Calcula o total
            total = round(total, 2) #Deixa duas casas decimais
            totalVirgula = ''
            for letra in str(total): #Retorna a vírgula no lugar do ponto
                if letra == ".":
                    totalVirgula += ","
                else:
                    totalVirgula += letra

            linha[4] = f"R${totalVirgula}" #Atualiza o preço total
            lista[cont] = linha  #Salva a linha atualizada na lista
            break
        cont += 1

    # Reescrevendo o arquivo com as mudanças
    arq = open("estoque.csv", "w", encoding="utf-8")
    for linha in lista:
        arq.write(";".join(linha) + "\n")
    arq.close()
    return True


#Tela de cadastro
def telaCadastro(win):
    #Deleta o conteúdo da tela anterior
    win.delete('all') 

    #Calcula o meio da tela vertical e horizontal
    center_x = win.getWidth() // 2
    center_y = win.getHeight() // 2

    #Botão Home
    buttonTelaPrincipal = Rectangle(Point(20, 20), Point(60, 60))
    buttonTelaPrincipal.setFill("white")
    buttonTelaPrincipal.draw(win)
    textTelaPrincipal = Text(Point(40, 40), '🏠')
    textTelaPrincipal.setSize(20)
    textTelaPrincipal.draw(win)

    #Título Da Tela
    titulo = Text(Point(center_x, 70), "Cadastro de Produtos E-Stock")
    titulo.setSize(20)
    titulo.setStyle("bold")
    titulo.draw(win)

    #Campos para o cadastro e labels com a descrição de cada um
    lblDescricao = Text(Point(center_x - 346, 240), "Descrição do Produto")
    lblDescricao.setSize(12)
    lblDescricao.draw(win)
    cmpDescricao = Entry(Point(center_x - 233, 270), 25)
    cmpDescricao.setSize(20)
    cmpDescricao.draw(win)

    lblQtde = Text(Point(center_x + 76, 240), "Quantidade")
    lblQtde.setSize(12)
    lblQtde.draw(win)
    cmpQtde = Entry(Point(center_x + 225, 270), 25)
    cmpQtde.setSize(20)
    cmpQtde.draw(win)

    lblUnitario = Text(Point(center_x - 372, 400), "Preço Unitário")
    lblUnitario.setSize(12)
    lblUnitario.draw(win)
    cmpUnitario = Entry(Point(center_x - 233, 430), 25)
    cmpUnitario.setSize(20)
    cmpUnitario.draw(win)

    lblTotal = Text(Point(center_x + 76, 400), "Preço Total")
    lblTotal.setSize(12)
    lblTotal.draw(win)
    cmpTotal = Entry(Point(center_x + 225, 430), 25)
    cmpTotal.setSize(20)
    cmpTotal.draw(win)

    #Botão de Cadastro
    btnCadastrar = Rectangle(Point(center_x - 95, center_y + 240), Point(center_x + 95, center_y + 290))
    btnCadastrar.setFill("white")
    btnCadastrar.setOutline("black")
    btnCadastrar.draw(win)
    #Escrita de dentro do botão
    icnSalvar = Text(Point(center_x, center_y + 267), "💾 Cadastrar")
    icnSalvar.setSize(18)
    icnSalvar.draw(win)

    #Lista de campos pra limpá-los em outras funções
    campos = [cmpDescricao, cmpQtde, cmpTotal, cmpUnitario]

    erro = None

    #Enquanto a janela estiver aberta:
    while not win.isClosed():
        try:
            click = win.getMouse()
        except GraphicsError:
            break 

        #Apaga o erro caso já estaja na tela
        if erro:
            erro.undraw()

        #Verifica onde foi o click
        if center_x - 95 <= click.x <= center_x + 95 and center_y + 240 <= click.y <= center_y + 290:  
            produto = cmpDescricao.getText() #Pega os valores de cada campo
            quantidade = cmpQtde.getText()
            valorUnit = cmpUnitario.getText()
            valorTotal = cmpTotal.getText()
            if (produto != "" and quantidade != "" and valorTotal != "" and valorUnit != ""):
                try:
                    # Verificar se os campos de quantidade e valores são números válidos
                    quantidade = int(quantidade)  # Deve ser um número inteiro
                
                    # Normalizar os valores com vírgula ou ponto
                    valorUnit = float(valorUnit.replace(",", "."))
                    valorTotal = float(valorTotal.replace(",", "."))

                    # Arredondar para 2 casas decimais e formatar como string com vírgula
                    valorUnit = f"{round(valorUnit, 2):.2f}".replace(".", ",")
                    valorTotal = f"{round(valorTotal, 2):.2f}".replace(".", ",")


                    verificacao = existe(produto, str(valorUnit)) #Verifica se já existe um produto com mesmo nome
                    #Realiza as funções esperadas de acordo com o retorno da função "existe()"
                    if verificacao == "adicionaQuantidade":
                        atualizaLinha(produto, quantidade)
                        mensagemWin = GraphWin("E-Stock", 400, 150)
                        mensagem(mensagemWin, win, campos, verificacao)

                    elif verificacao == "cadastraNovo":
                        mensagemWin = GraphWin("E-Stock", 400, 150)
                        mensagem(mensagemWin, win, campos, verificacao)
                        

                    else:
                        #Cadastra novo produto caso não haja nenhum igual

                        codigo = novoCodigo()
                        if cadastra(codigo, produto, quantidade, str(valorUnit), str(valorTotal)):
                                Confirmawin = GraphWin("E-Stock", 400, 150) #Mostra confirmação
                                telaConfirma(Confirmawin, win, campos)
                        else: #Caso os campos estejam com valores errados
                            erro = Text(Point(center_x, center_y + 160), "Erro ao cadastrar!")
                            erro.setTextColor("red")
                            erro.setStyle("bold")
                            erro.draw(win)

                except ValueError:
                    # Se quantidade ou valores não forem números válidos, exibir erro
                    erro = Text(Point(center_x, center_y + 160), "Preencha os campos de valores com números válidos!")
                    erro.setTextColor("red")
                    erro.setStyle("bold")
                    erro.draw(win)
            else:
                erro = Text(Point(center_x, center_y + 160), "Preencha todos os campos!")
                erro.setTextColor("red")
                erro.setStyle("bold")

                erro.draw(win)

        elif center_x - 620 <= click.x <= center_x - 570 and 20 <= click.y <= 60:
            if not win.isClosed():
                win.close()
            #Chama tela inicial
            from telas.telaInicial import telaInicial
            telaInicial()
            break