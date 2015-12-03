from tkinter import *

janela = Tk()
janela.geometry("330x250")
janela.title("Formulário Cadastro Vendedores")

labelTitulo = Label(text = "CADASTRO VENDEDORES")


# Criação dos paineis

frameTela = Frame(janela)
frameBotoes = Frame(frameTela)
frameNome = Frame(frameTela)
frameCodigo = Frame(frameTela)
frameCPF = Frame (frameTela)

separator1 = Frame(frameTela,height=2, bd=1, relief=SUNKEN)
separator2 = Frame(frameTela,height=2, bd=1, relief=SUNKEN)



# Elementos do painel Nome
labelNome = Label(frameNome,text =   "Nome     :")
entryNome = Entry(frameNome)

labelCodigo = Label(frameCodigo,text =   "Código :")
entryCodigo = Entry(frameCodigo)

labelCPF = Label(frameCPF ,text = "CPF    :")
entryCPF  = Entry(frameCPF)

# E aqui onde eu criei os botões

btNovo = Button(frameBotoes, text = "Novo")
btGravar = Button(frameBotoes, text = "Gravar")
btExcluir = Button(frameBotoes, text = "Excluir")
btAlterar = Button(frameBotoes, text = "Alterar")

# Organização dos elementos no tela

labelTitulo.pack(pady = 5)

labelNome.pack(side = LEFT,padx = 10)
entryNome.pack(side = LEFT)

labelCodigo.pack(side = LEFT,padx = 10)
entryCodigo.pack(side = LEFT)

labelCPF.pack(side = LEFT,padx = 10)
entryCPF.pack(side = LEFT)

btNovo.pack(side = LEFT, padx = 10)
btGravar.pack(side = LEFT, padx = 10)
btExcluir.pack(side = LEFT, padx = 10)
btAlterar.pack(side = LEFT, padx = 10)

separator1.pack(fill=X, padx=5, pady=5)
frameNome.pack(side = TOP, pady = 10)
frameCodigo.pack(side = TOP, pady = 10)
frameCPF.pack(side = TOP,pady = 10)

separator2.pack(fill=X, padx=5, pady=5)
frameBotoes.pack(side = BOTTOM,pady = 10)

frameTela.pack(side = LEFT)







janela.mainloop()
