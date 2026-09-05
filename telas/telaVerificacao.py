from graphics import *

#Retorna a tela de verificação
def telaVerificacao(win):
    #Deleta o conteúdo da tela anterior
    win.delete('all') 

    #Calcula os meios (horizontal e vertical) da página
    center_x = win.getWidth()//2
    center_y = win.getHeight()//2

    #Botão Home
    buttonTelaPrincipal = Rectangle(Point(20, 20), Point(60, 60))
    buttonTelaPrincipal.setFill("white")
    buttonTelaPrincipal.draw(win)
    textTelaPrincipal = Text(Point(40, 40), '🏠')
    textTelaPrincipal.setSize(20)
    textTelaPrincipal.draw(win)

    #Título principal
    titulo = Text(Point(center_x, 70), "Consultar Quantidade E-Stock")
    titulo.setSize(20)
    titulo.setStyle("bold")
    titulo.draw(win)

    #Campo para pesquisa e label com a descrição
    lblNome = Text(Point(center_x - 80,center_y - 55), "Informe o nome do produto que deseja verificar:")
    lblNome.setSize(15)
    lblNome.draw(win)
    cmpNome = Entry(Point(center_x - 28, center_y - 18), 35)
    cmpNome.setSize(20)
    cmpNome.draw(win)

    #Desenhando a lupa de pesquisa (botão)
    circulo1 = Circle(Point(center_x + 270, center_y - 30), 25)
    circulo2 = Circle(Point(center_x + 270, center_y - 30), 21)

    linha1 = Line(Point(center_x + 290, center_y - 16), Point(center_x + 312, center_y))
    linha2 = Line(Point(center_x + 287, center_y - 11), Point(center_x + 307, center_y + 4))
    linha3 = Line(Point(center_x + 310, center_y), Point(center_x + 304, center_y + 4))

    circulo1.draw(win)
    circulo2.draw(win)
    linha1.draw(win)
    linha2.draw(win)
    linha3.draw(win)

    #Define um click mínimo e máximo para x e y
    clickMinX = center_x + 240
    clickMaxX = center_x + 320
    clickMinY = center_y - 20
    clickMaxY = center_y + 5

    #Pega o centro e o raio do círculo maior
    centro = circulo1.getCenter()
    raio = circulo1.getRadius()
    #Cria variáveis pra uso posterior
    resposta = None
    texto = ''
    
    while True:
        try:
            click = win.getMouse()
        except GraphicsError:
            break

        #Verifica se o click foi feito na lupa e pega o nome informado no campo
        distancia = ((click.x - centro.x) ** 2 + (click.y - centro.y) ** 2) ** 0.5

        if (distancia <= raio) or (clickMinX <= click.x <= clickMaxX and clickMinY <= click.y <= clickMaxY):
            produto = cmpNome.getText()

            if resposta: 
                resposta.undraw() #Apaga resposta se já tiver escrita pra não sobrepor

            if produto != "":
                quantidade = int(busca(produto)) #Chama a função de busca caso o campo não esteja vazio

                #Muda o texto de acordo com a quantidade do produto no estoque
                if quantidade == 1:
                    texto = f"Foi encontrado apenas {quantidade} item\ndo produto {produto}!"

                elif quantidade > 1:
                    texto = f"Foram encontrados {quantidade} itens\ndo produto {produto}!"

                else:
                    texto = "Nenhum item foi encontrado!"

            else:
                texto = "Preencha o campo corretamente!"
                
                
            resposta = Text(Point(center_x, center_y + 250), texto)
            resposta.setSize(20)
            resposta.setStyle("bold")
            resposta.draw(win)
        
        elif center_x - 620 <= click.x <= center_x - 570 and 20 <= click.y <= 60:
            if not win.isClosed():
                win.close()
            #Volta pra tela inicial
            from telas.telaInicial import telaInicial
            telaInicial()
            break

#Função para buscar produto no estoque
def busca(produto):
    produto = produto.lower() #Deixa minúsculo pra comparar
    arq = open("estoque.csv", "r", encoding="latin-1")
    arquivo = arq.readlines()
    lista = []
    for linha in arquivo:
        linha = linha.split(";")
        lista.append(linha)

    for linha in lista[1:]:
        nome = str(linha[1]).lower()
        if nome == produto: #retorna quantidade caso encontre o produto procurado
            return linha[2]
    arq.close()
    return 0 #Retorna 0 caso não encontre