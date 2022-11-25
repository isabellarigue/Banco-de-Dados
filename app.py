from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
from datetime import datetime
import sys
import os

options_set = ["Adicionar Simulação", "Adicionar Teste", "Ver Simulações", "Ver Testes"]

def reiniciar():
    ''' Reinicia o programa. '''
    python = sys.executable
    os.execl(python, python, * sys.argv)



if __name__ == "__main__" :
    ''' Configurando a interface da janela: '''
    gui = Tk()
    gui.configure(background = "light gray")
    gui.title("Banco de Dados")
    gui.geometry("930x800")
    #gui.tk.call('wm', 'iconphoto', gui._w, tkinter.PhotoImage(file='icon.png'))

    cb_tamanhos = ttk.Combobox(gui, values=options_set)
    cb_tamanhos.set("Selecione uma opção")
    cb_tamanhos.place(x = 0, y = 10)

    Reiniciar = Button(gui, text = "Reiniciar", fg = "Black", bg = "gray", command = reiniciar, height = 2, width = 10)
    Reiniciar.place(x = 717, y = 750)

    gui.mainloop()
