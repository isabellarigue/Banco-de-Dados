from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
from datetime import datetime
import sys
import os
import mysql.connector

options_set = ["Adicionar Simulação", "Adicionar Teste", "Ver Simulações", "Ver Testes"]

def reiniciar():
    ''' Reinicia o programa. '''
    python = sys.executable
    os.execl(python, python, * sys.argv) 

def adicionar_simulacao():
    ''' Adiciona uma nova simulação. '''
    novaJanela = Tk()
    novaJanela.configure(background = "light gray")
    novaJanela.title("Adicionar nova simulação")
    novaJanela.geometry("930x800")
    novaJanela.tk.call('wm', 'iconphoto', novaJanela._w, tkinter.PhotoImage(file='icon.png'))
    novaJanela.mainloop()

def adicionar_teste():
    ''' Adiciona um novo teste. '''
    # Código para adicionar teste

def ver_simulacao():
    ''' Mostra as simulações. '''
    novaJanela = Tk()
    novaJanela.configure(background = "light gray")
    novaJanela.title("Ver simulação")
    novaJanela.geometry("930x800")
    novaJanela.tk.call('wm', 'iconphoto', novaJanela._w, tkinter.PhotoImage(file='icon.png'))
    novaJanela.mainloop()

def ver_teste():
    ''' Mostra os testes. '''
    # Código para mostrar testes

if __name__ == "__main__" :
    ''' Configurando a interface da janela: '''
    gui = Tk()
    gui.configure(background = "light gray")
    gui.title("Banco de Dados")
    gui.geometry("930x800")
    #gui.tk.call('wm', 'iconphoto', gui._w, tkinter.PhotoImage(file='icon.png'))

    con = mysql.connector.connect(host = 'localhost', database = 'Aero', user = 'root', password = '14041981')

    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão ", db_info)
        cursor = con.cursor()
        cursor.execute("select database();")
        linha = cursor.fetchone()
        print("Conectado ao banco de dados ", linha)

    # Tem que finalizar a conexão em algum momento

    # cb_tamanhos = ttk.Combobox(gui, values=options_set)
    # cb_tamanhos.set("Selecione uma opção")
    # cb_tamanhos.place(x = 0, y = 10)

    Reiniciar = Button(gui, text = "Reiniciar", fg = "Black", bg = "gray", command = reiniciar, height = 2, width = 10)
    Reiniciar.place(x = 717, y = 750)

    # Pizza1 = Label(gui, text = "Numero da Pizza (inteira):", bg = "yellow")
    # Pizza1Field = Entry(gui)
    # Pizza1.grid(row = 0, column = 2)
    # Pizza1Field.grid(row = 1, column = 2, ipadx = 50)   

    AdcSimu = Button(gui, text = "Adicionar Simulação", fg = "Black", bg = "gray", command = adicionar_simulacao, height = 2, width = 20)
    AdcSimu.place(x = 250, y = 250)

    AdcTeste = Button(gui, text = "Adicionar Teste", fg = "Black", bg = "gray", command = adicionar_teste, height = 2, width = 20)
    AdcTeste.place(x = 500, y = 250)

    VerSimu = Button(gui, text = "Ver Simulação", fg = "Black", bg = "gray", command = ver_simulacao, height = 2, width = 20)
    VerSimu.place(x = 250, y = 500)

    VerTeste = Button(gui, text = "Ver Teste", fg = "Black", bg = "gray", command = ver_teste, height = 2, width = 20)
    VerTeste.place(x = 500, y = 500)



    gui.mainloop()
