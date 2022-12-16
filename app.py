from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
from datetime import datetime
import sys
import os
import mysql.connector

dados_simu = []
dados_ver_simu = []
descricoes = ["Link do arquivo no drive", "Data (formato ano/mês/dia) ", "Coeficiente de Lift (utilizar ponto como separador de decimais) ", "Coeficiente de Drag (utilizar ponto como separador de decimais) ", "Configuração da simulação, digite 1 para o carro completo, 2 para asa traseira, 3 para asa dianteira, 4 para radiador", "Velocidade em km/h"]
nova_coluna = []
colunas_simu = []
infos_gerais = []
info_excluir = []
i_value = []
janelas_editar = []
escolhida_simu = []

def reiniciar():
    ''' Reinicia o programa. '''
    python = sys.executable
    os.execl(python, python, * sys.argv) 

def adicionar_simulacao_sql():
    cursor = con.cursor()
    colunas_escrito = "("
    for i in range(len(colunas_simu)):
        colunas_escrito += colunas_simu[i]
        if i != len(colunas_simu)-1:
            colunas_escrito += ", "
    colunas_escrito += ")"

    values_escrito = "("
    for i in range(len(colunas_simu)):
        values_escrito += "%s"
        if i != len(colunas_simu)-1:
            values_escrito += ", "
    values_escrito += ")"

    infos_escrito = []
    for i in range(len(colunas_simu)):
        infos_escrito.append(dados_simu[i].get())

    cursor.execute("INSERT INTO simulacoes "+colunas_escrito+" VALUES "+values_escrito+"", infos_escrito)
    con.commit()
    messagebox.showinfo("Info", "Simulação adicionada com sucesso! Pode fechar esta aba.")
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

    rel_x = 0.1
    rel_y = 0.2
    for i in range(len(descricoes)):
        desc = Label(janela2, text = descricoes[i], bg = "pink")
        descField = Entry(janela2)
        desc.place(relx=rel_x, rely=rel_y)
        descField.place(relx=rel_x, rely=rel_y+0.03, relwidth=0.8)
        dados_simu.append(descField)
        rel_y += 0.1

    AdcSimusql = Button(janela2, text = "Confirmar", fg = "Black", bg = "gray", command = adicionar_simulacao_sql, height = 2, width = 20)
    AdcSimusql.place(relx=0.38, rely=0.83)

    # return ?


def adicionar_teste():
    ''' Adiciona um novo teste. '''
    # Código para adicionar teste
    # analogo do adicionar_simulacao, porém com os dados do teste (que no caso ainda n tenho certeza quais vao ser)

def pegar_escrito():
    novo_parametro = (nova_coluna[0].get())
    cursor = con.cursor()
    query = "ALTER TABLE simulacoes ADD "+novo_parametro+" VARCHAR(100)"
    cursor.execute(query)

    messagebox.showinfo("Info", "Parâmetro adicionado com sucesso! Pode fechar esta aba.")
    nova_coluna[1].destroy()

def pegar_escrito1():
    novo_parametro = (nova_coluna[0].get())
    cursor = con.cursor()
    query = "ALTER TABLE simulacoes ADD "+novo_parametro+" INT"
    cursor.execute(query)

    messagebox.showinfo("Info", "Parâmetro adicionado com sucesso! Pode fechar esta aba.")
    nova_coluna[1].destroy()

def adicionar_coluna():
    novaJanela3 = Toplevel()
    novaJanela3.configure(background = "light gray")
    novaJanela3.title("Adicionar parâmetro")
    novaJanela3.geometry("450x200")

    parametro = Label(novaJanela3, text = "Digite o nome do novo parametro", bg = "pink")
    parametroField = Entry(novaJanela3) #deixar assim para dar pra dar ctrl+c kkkk
    parametro.place(relx=0.1, rely=0.1, relwidth=1, relheight=0.5)
    parametroField.place(relx=0.1, rely=0.43, relwidth=0.8)
    nova_coluna.append(parametroField)
    nova_coluna.append(novaJanela3)

    addCHARButtom = Button(novaJanela3, text = "Adicionar char", fg = "Black", bg = "gray", command = pegar_escrito, height = 2, width = 20)
    addCHARButtom.place(relx=0.06, rely=0.6)

    addINTButtom = Button(novaJanela3, text = "Adicionar int", fg = "Black", bg = "gray", command = pegar_escrito1, height = 2, width = 20)
    addINTButtom.place(relx=0.4, rely=0.6)


def excluir_simu():
    okcancel = messagebox.askokcancel("Atenção!!!", "Tem certeza que deseja excluir a simulação? Essa ação é irreversível.")
    if(okcancel == True):
        comando = "DELETE FROM simulacoes WHERE link = "+"'"+str(info_excluir[0])+"'"  
        cursor.execute(comando)
        con.commit()
        messagebox.showinfo("Info", "Simulação excluída com sucesso!")
    return

def altera_mysql():
    elementoAlterado = colunas_simu[i_value[0]]
    novo_valor = i_value[2].get()
    comando = "UPDATE simulacoes SET "+elementoAlterado+" = "+"'"+novo_valor+"'"+" WHERE link = "+"'"+str(i_value[1])+"'"
    print(comando)
    cursor.execute(comando)
    con.commit()
    messagebox.showinfo("Info", "Valor alterado com sucesso!")
    janelas_editar[1].destroy()


def alterar_valor():
    i_value.append(escolhida_simu[0][0])
    janelaAlterar = Toplevel() 
    janelaAlterar.configure(background = "light gray")
    janelaAlterar.title("Alterar valor")
    janelaAlterar.geometry("750x200")
    janelas_editar.append(janelaAlterar)

    labelAlterar = Label(janelaAlterar, text = "Digite o novo valor na formatação adequada.", bg = "pink")
    alterarField = Entry(janelaAlterar) 
    labelAlterar.place(relx=0.2, rely=0.1, relwidth=0.7, relheight=0.5)
    alterarField.place(relx=0.27, rely=0.43, relwidth=0.6)
    i_value.append(alterarField)

    addButtom = Button(janelaAlterar, text = "Adicionar", fg = "Black", bg = "gray", command = altera_mysql, height = 2, width = 20)
    addButtom.place(relx=0.29, rely=0.6)

    return

def escolhido1():
    i_value.append(0)
    janelas_editar[0].destroy()
    alterar_valor()

def escolhido2():
    i_value.append(1)
    janelas_editar[0].destroy()
    alterar_valor()

def escolhido3():
    i_value.append(2)
    janelas_editar[0].destroy()
    alterar_valor()

def escolhido4():
    i_value.append(3)
    janelas_editar[0].destroy()
    alterar_valor()

def escolhido5():
    i_value.append(4)
    janelas_editar[0].destroy()
    alterar_valor()

def escolhido6():
    i_value.append(5)
    janelas_editar[0].destroy()
    alterar_valor()

def escolhido7():
    i_value.append(6)
    janelas_editar[0].destroy()
    alterar_valor()

def escolhido8():
    i_value.append(7)
    janelas_editar[0].destroy()
    alterar_valor()

def escolhido9():
    i_value.append(8)
    janelas_editar[0].destroy()
    alterar_valor()

# SEM IDEIAS DO Q FAZER AQUI, PQ PRECISA SABER O NUMERO DO PARAMETRO, MAS NAO SEI COMO FAZER ISSO, PQ NA TEORIA NAO SABEMOS, dito isso ta uma gambiarra ai embaixo, mas q so funciona ate 9 parametros
def escolheParametro():
    janelaAlterar1 = Toplevel() 
    janelaAlterar1.configure(background = "light gray")
    janelaAlterar1.title("Escolha o parâmetro")
    janelaAlterar1.geometry("650x500")
    janelas_editar.append(janelaAlterar1)
    rel_x = 0.01
    rel_y = 0.1
    i = 0
    max = len(descricoes)
    if i < max:
        pButtom = Button(janelaAlterar1, text = descricoes[i], fg = "Black", bg = "light blue", command = escolhido1)
        pButtom.place(relx=rel_x, rely=rel_y)
        rel_y += 0.1 
        i += 1
    if i < max:
        pButtom = Button(janelaAlterar1, text = descricoes[i], fg = "Black", bg = "light blue", command = escolhido2)
        pButtom.place(relx=rel_x, rely=rel_y)
        rel_y += 0.1 
        i += 1
    if i < max:
        pButtom = Button(janelaAlterar1, text = descricoes[i], fg = "Black", bg = "light blue", command = escolhido3)
        pButtom.place(relx=rel_x, rely=rel_y)
        rel_y += 0.1 
        i += 1
    if i < max:
        pButtom = Button(janelaAlterar1, text = descricoes[i], fg = "Black", bg = "light blue", command = escolhido4)
        pButtom.place(relx=rel_x, rely=rel_y)
        rel_y += 0.1 
        i += 1
    if i < max:
        pButtom = Button(janelaAlterar1, text = descricoes[i], fg = "Black", bg = "light blue", command = escolhido5)
        pButtom.place(relx=rel_x, rely=rel_y)
        rel_y += 0.1 
        i += 1
    if i < max:
        pButtom = Button(janelaAlterar1, text = descricoes[i], fg = "Black", bg = "light blue", command = escolhido6)
        pButtom.place(relx=rel_x, rely=rel_y)
        rel_y += 0.1 
        i += 1
    if i < max:
        pButtom = Button(janelaAlterar1, text = descricoes[i], fg = "Black", bg = "light blue", command = escolhido7)
        pButtom.place(relx=rel_x, rely=rel_y)
        rel_y += 0.1 
        i += 1
    if i < max:
        pButtom = Button(janelaAlterar1, text = descricoes[i], fg = "Black", bg = "light blue", command = escolhido8)
        pButtom.place(relx=rel_x, rely=rel_y)
        rel_y += 0.1 
        i += 1
    if i < max:
        pButtom = Button(janelaAlterar1, text = descricoes[i], fg = "Black", bg = "light blue", command = escolhido9)
        pButtom.place(relx=rel_x, rely=rel_y)
        rel_y += 0.1 
        i += 1

def mostrar_simulacao():
    escolhida = dados_ver_simu[0].get() #cb_simus.get
    for i in range(len(dados_ver_simu[1])):
        if(dados_ver_simu[1][i] == escolhida):
            linhas = dados_ver_simu[3][i]
            escolhida_simu.append(linhas)

            link = Label(dados_ver_simu[2], text = "Link do arquivo no drive", bg = "pink")
            #linkField = Label(dados_ver_simu[2], text = linhas[0], bg = "grey")
            linkField = Entry(dados_ver_simu[2]) #deixar assim para dar pra dar ctrl+c kkkk
            linkField.insert(0, linhas[0])
            info_excluir.append(linhas[0])
            link.place(relx=0.1, rely=0.3)
            linkField.place(relx=0.1, rely=0.33, relwidth=0.8)

            rel_x = 0.1
            rel_y = 0.4
            for i in range(1,len(descricoes)):
                desc = Label(dados_ver_simu[2], text = descricoes[i], bg = "pink")
                descField = Label(dados_ver_simu[2], text = linhas[i], bg = "grey")
                desc.place(relx=rel_x, rely=rel_y)
                descField.place(relx=rel_x, rely=rel_y+0.03, relwidth=0.8)
                #dados_simu.append(descField)
                rel_y += 0.1

            novaColunaButtom = Button(dados_ver_simu[2], text = "Adicionar novo parâmetro", fg = "Black", bg = "gray", command = adicionar_coluna, height = 2, width = 20)
            novaColunaButtom.place(relx=0.3, rely=0.2)

            excluirButtom = Button(dados_ver_simu[2], text = "Excluir simulação", fg = "Black", bg = "gray", command = excluir_simu, height = 2, width = 20)
            excluirButtom.place(relx=0.5, rely=0.2)

            editarButtom = Button(dados_ver_simu[2], text = "Editar algum valor", fg = "Black", bg = "gray", command = escolheParametro, height = 2, width = 20)
            editarButtom.place(relx=0.7, rely=0.2)


def ver_simulacao():
    ''' Mostra as simulações. '''
    novaJanela = Toplevel()
    novaJanela.configure(background = "light gray")
    novaJanela.title("Ver simulação")
    novaJanela.geometry("930x900")
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



def verificar():
    infos_gerais[0] = 1
    return

def conecta():
    gui2 = Toplevel() 
    gui2.configure(background = "light gray")
    gui2.title("Senha")
    gui2.geometry("300x200")

    senha = Label(gui2, text = "Digite sua senha", bg = "pink")
    senhaField = Entry(gui2) 
    senha.place(relx=0.09, rely=0.1, relwidth=0.7, relheight=0.5)
    senhaField.place(relx=0.17, rely=0.43, relwidth=0.6)

    addButtom = Button(gui2, text = "Adicionar", fg = "Black", bg = "gray", command = verificar, height = 2, width = 20)
    addButtom.place(relx=0.19, rely=0.6)

    infos_gerais.append(0)
    while(infos_gerais[0] != 1):
        gui2.update()
    con = mysql.connector.connect(host = 'localhost', database = 'Aero', user = 'root', password = senhaField.get())
    infos_gerais.append(con)
    messagebox.showinfo("Info", "Conectado com sucesso! Pode fechar esta aba.")
    gui2.destroy()
    return 

if __name__ == "__main__" :
    ''' Configurando a interface da janela: '''
    gui = Tk()
    gui.configure(background = "light gray")
    gui.title("Banco de Dados")
    gui.geometry("1x1")
    #gui.tk.call('wm', 'iconphoto', gui._w, tkinter.PhotoImage(file='icon.png'))

    conecta()

    #con = mysql.connector.connect(host = 'localhost', database = 'Aero', user = 'root', password = '')
    con = infos_gerais[1]
    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão ", db_info)
        cursor = con.cursor()
        cursor.execute("select database();")
        linha = cursor.fetchone()
        print("Conectado ao banco de dados ", linha)

    # Tem que finalizar a conexão em algum momento

    gui.geometry("930x800")
    
    cursor.execute("SHOW COLUMNS FROM simulacoes")
    colunas = cursor.fetchall()
    for i in range(len(colunas)):
        colunas_simu.append(colunas[i][0])

    k = len(descricoes)
    if len(colunas) != len(descricoes):
        for i in range(len(colunas) - k):
            descricoes.append(colunas[k+i][0])

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
