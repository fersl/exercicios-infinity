from tkinter import *

janela = Tk()
janela.title("Hello Window")
janela.geometry("400x200")

# masculino = Checkbutton(janela, text="Masculino",)
# masculino.grid(row=0, column=0)
# feminino = Checkbutton(janela, text="Feminino",)
# feminino.grid(row=0, column=1)

Label(janela, text="Login").grid(row=0)
login = Entry(janela).grid(row=0, column=1)

Label(janela, text="Senha").grid(row=1)
senha = Entry(janela, show='*').grid(row=1, column=1)

salvar_senha = Checkbutton(janela, text="Salvar senha?").grid(row=2)

entrar = Button(janela, text="Entrar").grid(row=3, column=0)
sair = Button(janela, text="Sair", command=janela.destroy).grid(row=3, column=1)


#########
janela.mainloop()
