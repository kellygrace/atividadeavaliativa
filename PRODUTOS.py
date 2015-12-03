from tkinter import *

formProdutos = Tk()
formProdutos.geometry("350x250")
formProdutos.title("Formulário Produtos")

def Novo():
    pass

# create a toplevel menu
menubar = Menu(formProdutos)
formProdutos.config(menu=menubar)
menubar.add_command(label="Novo", command=Novo)
menubar.add_command(label="Sair", command=formProdutos.quit)


frameCampos = Frame(formProdutos)

labelTitulo = Label(text = "PRODUTOS")

# Elementos do painel Nome
labelPrdCodigo = Label(frameCampos,text =     "Código:")
entryPrdCodigo = Entry(frameCampos,width=10)

labelPrdDescricao = Label(frameCampos,text =  "Descrição:")
entryPrdDescricao = Entry(frameCampos,width=20)

labelPrdValor = Label(frameCampos,text =      "Valor:")
entryPrdValor = Entry(frameCampos,width=5)

labelPrdQuantidade = Label(frameCampos,text = "Quantidade:")
entryPrdQuantidade = Entry(frameCampos,width=10)


# E aqui onde eu criei os botões

btNovo = Button(text = "Novo")
btGravar = Button(text = "Gravar")
btExcluir = Button(text = "Excluir")
btAlterar = Button(text = "Alterar")

# Organização dos elementos no tela


labelPrdCodigo.grid(row = 0, column = 0, sticky=E)
entryPrdCodigo.grid(row = 0, column = 1, columnspan=3, sticky=E)


labelPrdQuantidade.grid(row = 1, column = 0, sticky=E)
entryPrdQuantidade.grid(row = 1, column = 1, sticky=W)

labelPrdValor.grid(row = 1, column = 2, sticky=E)
entryPrdValor.grid(row = 1, column = 3, sticky=W)


labelPrdDescricao.grid(row = 2, column = 0, sticky=E)
entryPrdDescricao.grid(row = 2, column = 1, columnspan = 3, sticky=W)

labelTitulo.pack()
frameCampos.pack()




formProdutos.mainloop()
