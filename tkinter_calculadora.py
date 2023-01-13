from tkinter import *

janelaPrincipal = Tk()
janelaPrincipal.title('calculadora')

def inserir(valor):
    visor.insert(END, valor)

def limpar():
    visor.delete(0, END)

def calcular():
    texto_visor = visor.get()
    resultado = eval(texto_visor)
    visor.delete(0,END)
    visor.insert(0, str(resultado))

#Visor para entrada de dados
visor = Entry(janelaPrincipal, font='Arial 20 bold', bg='#FFFFFF', fg='#000000', width=19)
visor.pack()

#Criar painel para inserir os botões
panel = Frame(janelaPrincipal)

#criar os botões
botao_1 = Button(panel, bg="#D5D6D6", bd=1, text='1', font='Arial 16 bold', fg='#000000', width=5, height=3, command=lambda: inserir('1'))
botao_2 = Button(panel, bg="#D5D6D6", bd=1, text='2', font='Arial 16 bold', fg='#000000', width=5, height=3, command=lambda: inserir('2'))
botao_3 = Button(panel, bg="#D5D6D6", bd=1, text='3', font='Arial 16 bold', fg='#000000', width=5, height=3, command=lambda: inserir('3'))
botao_4 = Button(panel, bg="#D5D6D6", bd=1, text='4', font='Arial 16 bold', fg='#000000', width=5, height=3, command=lambda: inserir('4'))
botao_5 = Button(panel, bg="#D5D6D6", bd=1, text='5', font='Arial 16 bold', fg='#000000', width=5, height=3, command=lambda: inserir('5'))
botao_6 = Button(panel, bg="#D5D6D6", bd=1, text='6', font='Arial 16 bold', fg='#000000', width=5, height=3, command=lambda: inserir('6'))
botao_7 = Button(panel, bg="#D5D6D6", bd=1, text='7', font='Arial 16 bold', fg='#000000', width=5, height=3, command=lambda: inserir('7'))
botao_8 = Button(panel, bg="#D5D6D6", bd=1, text='8', font='Arial 16 bold', fg='#000000', width=5, height=3, command=lambda: inserir('8'))
botao_9 = Button(panel, bg="#D5D6D6", bd=1, text='9', font='Arial 16 bold', fg='#000000', width=5, height=3, command=lambda: inserir('9'))
botao_0 = Button(panel, bg="#D5D6D6", bd=1, text='0', font='Arial 16 bold', fg='#000000', width=5, height=3, command=lambda: inserir('0'))
botao_soma = Button(panel, bg="#D5D6D6", bd=1, text='+', font='Arial 16 bold', fg='#000000', width=5, height=3, command=lambda: inserir('+'))
botao_subtracao = Button(panel, bg="#D5D6D6", bd=1, text='-', font='Arial 16 bold', fg='#000000', width=5, height=3, command=lambda: inserir('-'))
botao_multiplicacao = Button(panel, bg="#D5D6D6", bd=1, text='*', font='Arial 16 bold', fg='#000000', width=5, height=3, command=lambda: inserir('*'))
botao_divisao = Button(panel, bg="#D5D6D6", bd=1, text='/', font='Arial 16 bold', fg='#000000', width=5, height=3, command=lambda: inserir('/'))
botao_igual = Button(panel, bg="#D5D6D6", bd=1, text='=', font='Arial 16 bold', fg='#000000', width=5, height=3, command=calcular)
botao_clear = Button(panel, bg="#D5D6D6", bd=1, text='C', font='Arial 16 bold', fg='#000000', width=5, height=3, command=limpar)

#ativar o panel (exibir na tela)
panel.pack()

#Primeira Linha
botao_7.grid(row=0, column=0)
botao_8.grid(row=0, column=1)
botao_9.grid(row=0, column=2)
botao_divisao.grid(row=0, column=3)
#Segunda Linha
botao_4.grid(row=1, column=0)
botao_5.grid(row=1, column=1)
botao_6.grid(row=1, column=2)
botao_multiplicacao.grid(row=1, column=3)
#Terceira Linha
botao_1.grid(row=2, column=0)
botao_2.grid(row=2, column=1)
botao_3.grid(row=2, column=2)
botao_soma.grid(row=2, column=3)
#Quarta Linha
botao_0.grid(row=3, column=0)
botao_clear.grid(row=3, column=1)
botao_igual.grid(row=3, column=2)
botao_subtracao.grid(row=3, column=3)

mainloop()
