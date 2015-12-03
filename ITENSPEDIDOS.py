
from tkinter import *

janela = Tk()
janela.geometry("350x300")
janela.title("PEDIDOS")

labelTitulo = Label(text = "ITENS PEDIDOS")


# Criação dos paineis

frameTela = Frame(janela)
frameBotoes = Frame(frameTela)
frameNumeroPedido= Frame(frameTela)
frameCodProduto = Frame(frameTela)
frameDescricaoProduto = Frame(frameTela)
frameQuantProduto = Frame (frameTela)
frameValorProduto = Frame (frameTela)

separator1 = Frame(frameTela,height=2, bd=1, relief=SUNKEN)
separator2 = Frame(frameTela,height=2, bd=1, relief=SUNKEN)



# Elementos do painel Nome
labelNumeroPedido = Label(frameNumeroPedido,text =   "Número Pedido     :")
entryNumeroPedido = Entry(frameNumeroPedido)

labelCodProduto = Label(frameCodProduto,text =   "Código Produto   :")
entryCodProduto = Entry(frameCodProduto)

labelDescricaoProduto = Label(frameDescricaoProduto,text =   "Descrição do Produto    :")
entryDescricaoProduto = Entry(frameDescricaoProduto)

labelQuantProduto = Label(frameQuantProduto,text =   "Quantidade do Produto  :")
entryQuantProduto = Entry(frameQuantProduto)

labelValorProduto = Label(frameValorProduto,text = "Valor  :R$")
entryValorProduto = Entry(frameValorProduto)

# E aqui onde eu criei os botões

btNovo = Button(frameBotoes, text = "Novo")
btGravar = Button(frameBotoes, text = "Gravar")
btExcluir = Button(frameBotoes, text = "Excluir")
btAlterar = Button(frameBotoes, text = "Alterar")

# Organização dos elementos no tela

labelTitulo.pack(pady = 5)

labelNumeroPedido.pack(side = LEFT,padx = 10)
entryNumeroPedido.pack(side = LEFT)
labelCodProduto.pack(side = LEFT,padx = 10)
entryCodProduto.pack(side = LEFT)
labelDescricaoProduto.pack(side = LEFT,padx = 10)
entryDescricaoProduto.pack(side = LEFT)
labelQuantProduto.pack(side = LEFT,padx = 10)
entryQuantProduto.pack(side = LEFT)
labelValorProduto.pack(side = LEFT, padx = 10)
entryValorProduto.pack(side = LEFT)



btNovo.pack(side = LEFT, padx = 10)
btGravar.pack(side = LEFT, padx = 10)
btExcluir.pack(side = LEFT, padx = 10)
btAlterar.pack(side = LEFT, padx = 10)

separator1.pack(fill=X, padx=5, pady=5)
frameNumeroPedido.pack(side = TOP, pady = 10)
frameCodProduto.pack(side = TOP, pady = 10)
frameDescricaoProduto.pack(side = TOP, pady = 10)
frameQuantProduto.pack(side = TOP, pady =10)
frameValorProduto.pack(side = TOP, pady = 10)


separator2.pack(fill=X, padx=5, pady=5)
frameBotoes.pack(side = BOTTOM,pady = 10)

frameTela.pack(side = LEFT)







janela.mainloop()
