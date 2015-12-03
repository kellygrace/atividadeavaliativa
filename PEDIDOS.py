
from tkinter import *

janela = Tk()
janela.geometry("350x300")
janela.title("Pedidos")

labelTitulo = Label(text = "CADASTRO DE PEDIDOS")


# Criação dos paineis

frameTela = Frame(janela)
frameBotoes = Frame(frameTela)
frameNumeroPedido= Frame(frameTela)
frameDataPedido = Frame(frameTela)
frameCodPedido = Frame (frameTela)
frameCodVendedor = Frame (frameTela)

separator1 = Frame(frameTela,height=2, bd=1, relief=SUNKEN)
separator2 = Frame(frameTela,height=2, bd=1, relief=SUNKEN)



# Elementos do painel Nome
labelNumeroPedido = Label(frameNumeroPedido,text =   "Número Pedido     :")
entryNumeroPedido = Entry(frameNumeroPedido)

labelDataPedido = Label(frameDataPedido,text =   "Data Pedido    :")
entryDataPedido = Entry(frameDataPedido)

labelCodPedido = Label(frameCodPedido,text =   "Código do Pedido    :")
entryCodPedido = Entry(frameCodPedido)

labelCodVendedor = Label(frameCodVendedor,text =   "Código do Vendedor   :")
entryCodVendedor = Entry(frameCodVendedor)

# E aqui onde eu criei os botões

btNovo = Button(frameBotoes, text = "Novo")
btGravar = Button(frameBotoes, text = "Gravar")
btExcluir = Button(frameBotoes, text = "Excluir")
btAlterar = Button(frameBotoes, text = "Alterar")

# Organização dos elementos no tela

labelTitulo.pack(pady = 5)

labelNumeroPedido.pack(side = LEFT,padx = 10)
entryNumeroPedido.pack(side = LEFT)
labelDataPedido.pack(side = LEFT,padx = 10)
entryDataPedido.pack(side = LEFT)
labelCodPedido.pack(side = LEFT,padx = 10)
entryCodPedido.pack(side = LEFT)
labelCodVendedor.pack(side = LEFT,padx = 10)
entryCodVendedor.pack(side = LEFT)



btNovo.pack(side = LEFT, padx = 10)
btGravar.pack(side = LEFT, padx = 10)
btExcluir.pack(side = LEFT, padx = 10)
btAlterar.pack(side = LEFT, padx = 10)

separator1.pack(fill=X, padx=5, pady=5)
frameNumeroPedido.pack(side = TOP, pady = 10)
frameDataPedido.pack(side = TOP, pady = 10)
frameCodPedido.pack(side = TOP, pady = 10)
frameCodVendedor.pack(side = TOP, pady =10)


separator2.pack(fill=X, padx=5, pady=5)
frameBotoes.pack(side = BOTTOM,pady = 10)

frameTela.pack(side = LEFT)







janela.mainloop()
