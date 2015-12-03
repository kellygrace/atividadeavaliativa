from tkinter import *

janela = Tk()
janela.geometry("330x250")
janela.title("Formulário Cadastro Clientes")

labelTitulo = Label(text = "CADASTRO CLIENTES")


# Criação dos paineis

frameTela = Frame(janela)
frameBotoes = Frame(frameTela)
frameNome = Frame(frameTela)
frameFone = Frame(frameTela)
frameEmail = Frame (frameTela)

separator1 = Frame(frameTela,height=2, bd=1, relief=SUNKEN)
separator2 = Frame(frameTela,height=2, bd=1, relief=SUNKEN)



# Elementos do painel Nome
labelNome = Label(frameNome,text =   "Nome     :")
entryNome = Entry(frameNome)

labelFone = Label(frameFone,text =   "Telefone :")
entryFone = Entry(frameFone)

labelEmail = Label(frameEmail,text = "Email    :")
entryEmail = Entry(frameEmail)

# E aqui onde eu criei os botões

btNovo = Button(frameBotoes, text = "Novo")
btGravar = Button(frameBotoes, text = "Gravar")
btExcluir = Button(frameBotoes, text = "Excluir")
btAlterar = Button(frameBotoes, text = "Alterar")

# Organização dos elementos no tela

labelTitulo.pack(pady = 5)

labelNome.pack(side = LEFT,padx = 10)
entryNome.pack(side = LEFT)

labelFone.pack(side = LEFT,padx = 10)
entryFone.pack(side = LEFT)

labelEmail.pack(side = LEFT,padx = 10)
entryEmail.pack(side = LEFT)

btNovo.pack(side = LEFT, padx = 10)
btGravar.pack(side = LEFT, padx = 10)
btExcluir.pack(side = LEFT, padx = 10)
btAlterar.pack(side = LEFT, padx = 10)

separator1.pack(fill=X, padx=5, pady=5)
frameNome.pack(side = TOP, pady = 10)
frameFone.pack(side = TOP, pady = 10)
frameEmail.pack(side = TOP,pady = 10)

separator2.pack(fill=X, padx=5, pady=5)
frameBotoes.pack(side = BOTTOM,pady = 10)

frameTela.pack(side = LEFT)







janela.mainloop()
