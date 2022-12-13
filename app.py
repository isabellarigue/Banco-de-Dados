from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
from datetime import datetime
import sys
import os
import mysql.connector

options_set = ["Adicionar Simulação", "Adicionar Teste", "Ver Simulações", "Ver Testes"]
dados_simu = []
dados_ver_simu = []

def reiniciar():
    ''' Reinicia o programa. '''
    python = sys.executable
    os.execl(python, python, * sys.argv) 

def adicionar_simulacao_sql():
    cursor = con.cursor()
    cursor.execute("INSERT INTO simulacoes (link, dia, cl, cd, config, velocidade, angulo) VALUES (%s, %s, %s, %s, %s, %s, %s)", (dados_simu[0].get(), dados_simu[1].get(), dados_simu[2].get(), dados_simu[3].get(), dados_simu[4].get(), dados_simu[5].get(), "0"))
    con.commit()
    messagebox.showinfo("Info", "Simulação adicionada com sucesso! Pode fechar esta aba.")
    #colocar para fechar automaticamente depois
    return 

def adicionar_simulacao():
    ''' Adiciona uma nova simulação. '''
    janela2 = Toplevel()
    janela2.configure(background = "light gray")
    janela2.title("Adicionar nova simulação")
    janela2.geometry("930x800")
    #janela2.tk.call('wm', 'iconphoto', janela2._w, tkinter.PhotoImage(file='icon.png'))
    janela2.focus_force()
    janela2.transient(gui)
    #janela2.janela2.grab_set()

    Instrucao = Label(janela2, text = "Digite todas as informações referentes a simulação e pressione o botão confirmar. Caso não tenha algum parâmetro, apenas deixe em branco.", bg = "grey")
    Instrucao.place(relx=0.1, rely=0.08)

    link = Label(janela2, text = "Link do arquivo no drive", bg = "pink")
    linkField = Entry(janela2)
    link.place(relx=0.1, rely=0.2)
    linkField.place(relx=0.1, rely=0.23, relwidth=0.8)
    dados_simu.append(linkField)

    data = Label(janela2, text = "Data (formato ano/mês/dia) ", bg = "pink")
    dataField = Entry(janela2)
    data.place(relx=0.1, rely=0.3)
    dataField.place(relx=0.1, rely=0.33, relwidth=0.8)
    dados_simu.append(dataField)

    cl = Label(janela2, text = "Coeficiente de Lift (utilizar ponto como separador de decimais) ", bg = "pink")
    clField = Entry(janela2)
    cl.place(relx=0.1, rely=0.4)
    clField.place(relx=0.1, rely=0.43, relwidth=0.8)
    dados_simu.append(clField)

    cd = Label(janela2, text = "Coeficiente de Drag (utilizar ponto como separador de decimais) ", bg = "pink")
    cdField = Entry(janela2)
    cd.place(relx=0.1, rely=0.5)
    cdField.place(relx=0.1, rely=0.53, relwidth=0.8)
    dados_simu.append(cdField)

    config = Label(janela2, text = "Configuração da simulação, digite 1 para o carro completo, 2 para asa traseira, 3 para asa dianteira, 4 para radiador", bg = "pink")
    configField = Entry(janela2)
    config.place(relx=0.1, rely=0.6)
    configField.place(relx=0.1, rely=0.63, relwidth=0.8)
    dados_simu.append(configField)

    vel = Label(janela2, text = "Velocidade em km/h", bg = "pink")
    velField = Entry(janela2)
    velField.insert(0, "60")
    vel.place(relx=0.1, rely=0.7)
    velField.place(relx=0.1, rely=0.73, relwidth=0.8)
    dados_simu.append(velField)

    AdcSimusql = Button(janela2, text = "Confirmar", fg = "Black", bg = "gray", command = adicionar_simulacao_sql, height = 2, width = 20)
    AdcSimusql.place(relx=0.38, rely=0.83)

    # return ?


def adicionar_teste():
    ''' Adiciona um novo teste. '''
    # Código para adicionar teste
    # analogo do adicionar_simulacao, porém com os dados do teste (que no caso ainda n tenho certeza quais vao ser)

def mostrar_simulacao():
    escolhida = dados_ver_simu[0].get() #cb_simus.get
    for i in range(len(dados_ver_simu[1])):
        if(dados_ver_simu[1][i] == escolhida):
            linhas = dados_ver_simu[3][i]

            link = Label(dados_ver_simu[2], text = "Link do arquivo no drive", bg = "pink")
            #linkField = Label(dados_ver_simu[2], text = linhas[0], bg = "grey")
            linkField = Entry(dados_ver_simu[2]) #deixar assim para dar pra dar ctrl+c kkkk
            linkField.insert(0, linhas[0])
            link.place(relx=0.1, rely=0.3)
            linkField.place(relx=0.1, rely=0.33, relwidth=0.8)
            dados_simu.append(linkField)

            data = Label(dados_ver_simu[2], text = "Data (formato ano/mês/dia) ", bg = "pink")
            dataField = Label(dados_ver_simu[2], text = linhas[1], bg = "grey")
            data.place(relx=0.1, rely=0.4)
            dataField.place(relx=0.1, rely=0.43, relwidth=0.8)
            dados_simu.append(dataField)

            cl = Label(dados_ver_simu[2], text = "Coeficiente de Lift", bg = "pink")
            clField = Label(dados_ver_simu[2], text = linhas[2], bg = "grey")
            cl.place(relx=0.1, rely=0.5)
            clField.place(relx=0.1, rely=0.53, relwidth=0.8)
            dados_simu.append(clField)

            cd = Label(dados_ver_simu[2], text = "Coeficiente de Drag ", bg = "pink")
            cdField = Label(dados_ver_simu[2], text = linhas[3], bg = "grey")
            cd.place(relx=0.1, rely=0.6)
            cdField.place(relx=0.1, rely=0.63, relwidth=0.8)
            dados_simu.append(cdField)

            config = Label(dados_ver_simu[2], text = "Configuração da simulação", bg = "pink")
            configField = Label(dados_ver_simu[2], text = linhas[4], bg = "grey")
            config.place(relx=0.1, rely=0.7)
            configField.place(relx=0.1, rely=0.73, relwidth=0.8)
            dados_simu.append(configField)

            vel = Label(dados_ver_simu[2], text = "Velocidade em km/h", bg = "pink")
            velField = Label(dados_ver_simu[2], text = linhas[5], bg = "grey")
            vel.place(relx=0.1, rely=0.8)
            velField.place(relx=0.1, rely=0.83, relwidth=0.8)


def ver_simulacao():
    ''' Mostra as simulações. '''
    novaJanela = Toplevel()
    novaJanela.configure(background = "light gray")
    novaJanela.title("Ver simulação")
    novaJanela.geometry("930x800")
    #novaJanela.focus_force()
    #novaJanela.transient(gui)
    #novaJanela.tk.call('wm', 'iconphoto', novaJanela._w, tkinter.PhotoImage(file='icon.png'))

    cursor = con.cursor()
    cursor.execute("SELECT * FROM simulacoes")
    linhas = cursor.fetchall()
    links = [] #posteriormente talvez fosse melhor trabalhar com nomes/apelidos para as simulacoes e nao com os links para a pessoa escolher qual simu ela quer ver
    for linha in linhas:
        links.append(linha[0])

    cb_simus = ttk.Combobox(novaJanela, values=links)
    cb_simus.set("Selecione uma simulação")
    cb_simus.place(relx=0.1, rely=0.1, relwidth=0.8)
    dados_ver_simu.append(cb_simus)
    dados_ver_simu.append(links)
    dados_ver_simu.append(novaJanela)
    dados_ver_simu.append(linhas)

    mostrarButtom = Button(novaJanela, text = "Mostrar", fg = "Black", bg = "gray", command = mostrar_simulacao, height = 2, width = 20)
    mostrarButtom.place(relx=0.1, rely=0.2)
    


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

    con = mysql.connector.connect(host = 'localhost', database = 'Aero', user = 'root', password = '')

    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão ", db_info)
        cursor = con.cursor()
        cursor.execute("select database();")
        linha = cursor.fetchone()
        print("Conectado ao banco de dados ", linha)

    # Tem que finalizar a conexão em algum momento

    Reiniciar = Button(gui, text = "Reiniciar", fg = "Black", bg = "gray", command = reiniciar, height = 2, width = 10)
    Reiniciar.place(x = 717, y = 750)

    AdcSimu = Button(gui, text = "Adicionar Simulação", fg = "Black", bg = "gray", command = adicionar_simulacao, height = 2, width = 20)
    AdcSimu.place(x = 250, y = 250)

    AdcTeste = Button(gui, text = "Adicionar Teste", fg = "Black", bg = "gray", command = adicionar_teste, height = 2, width = 20)
    AdcTeste.place(x = 500, y = 250)

    VerSimu = Button(gui, text = "Ver Simulação", fg = "Black", bg = "gray", command = ver_simulacao, height = 2, width = 20)
    VerSimu.place(x = 250, y = 500)

    VerTeste = Button(gui, text = "Ver Teste", fg = "Black", bg = "gray", command = ver_teste, height = 2, width = 20)
    VerTeste.place(x = 500, y = 500)



    gui.mainloop()
