from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys
import os
import mysql.connector

# Lists used to store global information that is used by different functions
columns_simu = []
descriptions = ["Nome", "Link do arquivo no drive", "Data (formato ano/mês/dia) ", "Coeficiente de Lift (utilizar ponto como separador de decimais) ", "Coeficiente de Drag (utilizar ponto como separador de decimais) ", "Configuração: digite 1 para o carro completo, 2 para asa traseira, 3 para asa dianteira, 4 para radiador", "Velocidade em km/h"]

def add_test():
    return

def look_test():
    return

def change_mysql(i, window, lines, field):
    ''' Changes the value of the chosen parameter on the database '''
    element_changed = columns_simu[i]
    new_value = field.get()
    comando = "UPDATE simulacoes SET "+element_changed+" = "+"'"+new_value+"'"+" WHERE link = "+"'"+str(lines[1])+"'"
    cursor.execute(comando)
    con.commit()
    messagebox.showinfo("Info", "Valor alterado com sucesso!")
    window.destroy()

def change_parameter(window, lines, answer):
    ''' Creates the visual interface for the user to enter the new value '''
    i = int(answer.get()) # number of the chosen parameter
    window.destroy()
    gui_change_parameter = Toplevel() 
    gui_change_parameter.configure(background = "light gray")
    gui_change_parameter.title("Alterar valor")
    gui_change_parameter.geometry("750x200")

    change_label = Label(gui_change_parameter, text = "Digite o novo valor na formatação adequada.", bg = "pink")
    change_field = Entry(gui_change_parameter) 
    change_label.place(relx=0.2, rely=0.1, relwidth=0.7, relheight=0.5)
    change_field.place(relx=0.27, rely=0.43, relwidth=0.6)

    addButtom = Button(gui_change_parameter, text = "Adicionar", fg = "Black", bg = "gray", command = lambda: change_mysql(i, gui_change_parameter, lines, change_field), height = 2, width = 20)
    addButtom.place(relx=0.29, rely=0.6)


def choose_parameter(lines):
    ''' Creates an Entry for the user to enter which parameter he wants to change. So, all available parameters are shown on the screen. '''
    gui_choose_parameter = Toplevel() 
    gui_choose_parameter.configure(background = "light gray")
    gui_choose_parameter.title("Escolha o parâmetro")
    gui_choose_parameter.geometry("750x500")

    which_number = Label(gui_choose_parameter, text = "Digite o n° do parâmetro que deseja editar", bg = "light blue")
    answer = Entry(gui_choose_parameter) 
    which_number.place(relx=0.01, rely=0.03)
    answer.place(relx=0.01, rely=0.075, relwidth=0.3)
    pButtom = Button(gui_choose_parameter, text = "Selecionar", fg = "Black", bg = "light green", command = lambda: change_parameter(gui_choose_parameter, lines, answer))
    pButtom.place(relx=0.45, rely=0.075)

    # Showing all available parameters and their respective numbers
    rel_y = 0.2
    for i in range(len(descriptions)):
        desc = Label(gui_choose_parameter, text = descriptions[i], bg = "light blue")
        number = Label(gui_choose_parameter, text = i, bg = "light blue")
        desc.place(relx=0.01, rely=rel_y)
        number.place(relx=0.8, rely=rel_y, relwidth=0.08)
        rel_y += 0.1

def delete_simu(link):
    ''' Deletes a simulation from the database according to its link '''
    okcancel = messagebox.askokcancel("Atenção!!!", "Tem certeza que deseja excluir a simulação? Essa ação é irreversível.")
    if(okcancel == True):
        command = "DELETE FROM simulacoes WHERE link = "+"'"+str(link)+"'"  
        cursor.execute(command)
        con.commit()
        messagebox.showinfo("Info", "Simulação excluída com sucesso!")
    return

def add_char(parameter_field, window):
    ''' Add a new column to the database for str values '''
    new_parameter = parameter_field.get()
    cursor = con.cursor()
    query = "ALTER TABLE simulacoes ADD "+new_parameter+" VARCHAR(100)"
    cursor.execute(query)

    messagebox.showinfo("Info", "Parâmetro adicionado com sucesso! Pode fechar esta aba.")
    window.destroy()

def add_int(parameter_field, window):
    ''' Add a new column to the database for int values '''
    new_parameter = parameter_field.get()
    cursor = con.cursor()
    query = "ALTER TABLE simulacoes ADD "+new_parameter+" INT"
    cursor.execute(query)

    messagebox.showinfo("Info", "Parâmetro adicionado com sucesso! Pode fechar esta aba.")
    window.destroy()

def add_column():
    ''' Creates the visual interface for the user to enter the name and type of the new column. '''
    gui_add_column = Toplevel()
    gui_add_column.configure(background = "light gray")
    gui_add_column.title("Adicionar parâmetro")
    gui_add_column.geometry("450x200")

    parameter = Label(gui_add_column, text = "Digite o nome do novo parâmetro", bg = "pink")
    parameter_field = Entry(gui_add_column) 
    parameter.place(relx=0.1, rely=0.1, relwidth=1, relheight=0.5)
    parameter_field.place(relx=0.1, rely=0.43, relwidth=0.8)

    add_char_buttom = Button(gui_add_column, text = "Adicionar char", fg = "Black", bg = "gray", command = lambda: add_char(parameter_field, gui_add_column), height = 2, width = 20)
    add_char_buttom.place(relx=0.06, rely=0.6)

    add_int_buttom = Button(gui_add_column, text = "Adicionar int", fg = "Black", bg = "gray", command = lambda: add_int(parameter_field, gui_add_column), height = 2, width = 20)
    add_int_buttom.place(relx=0.4, rely=0.6)


def show_simulation(data_look_simu):
    ''' Shows the simulation information on the screen '''
    chosen = data_look_simu[0].get() #cb_simus.get

    # Searching on the database the simulation with the name chosen by the user
    for i in range(len(data_look_simu[1])):
        if(data_look_simu[1][i] == chosen):
            lines = data_look_simu[3][i]

            # Displaying the simulation information on the screen
            gui_look_simu = data_look_simu[2]

            name = Label(gui_look_simu, text = descriptions[0], bg = "pink")
            nameField = Label(gui_look_simu, text = lines[0], bg = "grey")
            name.place(relx=0.1, rely=0.2)
            nameField.place(relx=0.1, rely=0.23, relwidth=0.8)

            link = Label(gui_look_simu, text = "Link do arquivo no drive", bg = "pink")
            linkField = Entry(gui_look_simu) 
            linkField.insert(0, lines[1])
            delete_info = lines[1] # Storing the link of the simulation if wanted to delete it later
            link.place(relx=0.1, rely=0.3)
            linkField.place(relx=0.1, rely=0.33, relwidth=0.8)

            rel_x = 0.1
            rel_y = 0.4
            for i in range(2,len(descriptions)):
                desc = Label(gui_look_simu, text = descriptions[i], bg = "pink")
                descField = Label(gui_look_simu, text = lines[i], bg = "grey")
                desc.place(relx=rel_x, rely=rel_y)
                descField.place(relx=rel_x, rely=rel_y+0.03, relwidth=0.8)
                rel_y += 0.1

            new_column_buttom = Button(gui_look_simu, text = "Adicionar novo parâmetro", fg = "Black", bg = "gray", command = add_column, height = 2, width = 20)
            new_column_buttom.place(relx=0.3, rely=0.1)

            delete_buttom = Button(gui_look_simu, text = "Excluir simulação", fg = "Black", bg = "gray", command = lambda: delete_simu(delete_info), height = 2, width = 20)
            delete_buttom.place(relx=0.5, rely=0.1)

            edit_buttom = Button(gui_look_simu, text = "Editar algum valor", fg = "Black", bg = "gray", command = lambda: choose_parameter(lines), height = 2, width = 20)
            edit_buttom.place(relx=0.7, rely=0.1)

def look_simulation():
    ''' Create the visual interface for the user select which simulation he wants to see '''
    gui_look_simu = Toplevel()
    gui_look_simu.configure(background = "light gray")
    gui_look_simu.title("Ver simulação")
    gui_look_simu.geometry("930x900")

    # Creating a list with all simulation names in order to display in the Combobox format for the user to select
    cursor = con.cursor()
    cursor.execute("SELECT * FROM simulacoes")
    lines = cursor.fetchall()
    names = [] 
    for line in lines:
        names.append(line[0])

    cb_simus = ttk.Combobox(gui_look_simu, values=names)
    cb_simus.set("Selecione uma simulação")
    cb_simus.place(relx=0.1, rely=0.03, relwidth=0.8)

    # Saving this data to be able to use in another function
    data_look_simu = []
    data_look_simu.append(cb_simus)
    data_look_simu.append(names)
    data_look_simu.append(gui_look_simu)
    data_look_simu.append(lines)

    show_buttom = Button(gui_look_simu, text = "Mostrar", fg = "Black", bg = "gray", command = lambda: show_simulation(data_look_simu), height = 2, width = 20)
    show_buttom.place(relx=0.1, rely=0.1)


def add_simulation_sql(data_simu):
    ''' Take the information that the user has entered and add it to the database '''
    cursor = con.cursor()

    # Putting in the proper formatting of the mySQL command
    written_columns = "("
    for i in range(len(columns_simu)):
        written_columns += columns_simu[i]
        if i != len(columns_simu)-1:
            written_columns += ", "
    written_columns += ")"

    written_values = "("
    for i in range(len(columns_simu)):
        written_values += "%s"
        if i != len(columns_simu)-1:
            written_values += ", "
    written_values += ")"

    written_infos = []
    for i in range(len(columns_simu)):
        written_infos.append(data_simu[i].get())

    cursor.execute("INSERT INTO simulacoes "+written_columns+" VALUES "+written_values+"", written_infos)
    con.commit()
    messagebox.showinfo("Info", "Simulação adicionada com sucesso! Pode fechar esta aba.")
    return 

def add_simulation():
    ''' Create the visual interface to add a new simulation. '''
    gui_add_simu = Toplevel()
    gui_add_simu.configure(background = "light gray")
    gui_add_simu.title("Adicionar nova simulação")
    gui_add_simu.geometry("930x800")
    gui_add_simu.focus_force()
    gui_add_simu.transient(gui)

    instructions = Label(gui_add_simu, text = "Digite todas as informações referentes a simulação e pressione o botão confirmar. Caso não tenha algum parâmetro, apenas deixe em branco.", bg = "grey")
    instructions.place(relx=0.1, rely=0.06)

    # Creating the labels for the data and storing them on a list
    rel_x = 0.1
    rel_y = 0.11
    data_simu = []
    for i in range(len(descriptions)):
        desc = Label(gui_add_simu, text = descriptions[i], bg = "pink")
        descField = Entry(gui_add_simu)
        desc.place(relx=rel_x, rely=rel_y)
        descField.place(relx=rel_x, rely=rel_y+0.03, relwidth=0.8)
        data_simu.append(descField)
        rel_y += 0.1

    add_simu_sql = Button(gui_add_simu, text = "Confirmar", fg = "Black", bg = "gray", command=lambda: add_simulation_sql(data_simu), height = 2, width = 20)
    add_simu_sql.place(relx=0.38, rely=0.83)


def restart():
    ''' Restart the program. '''
    python = sys.executable
    os.execl(python, python, * sys.argv) 

def verify(activated):
    activated[0] = 1
    return

def connect():
    ''' Make the connection to the database, asking the user for his password. '''
    gui_conect = Toplevel() 
    gui_conect.configure(background = "light gray")
    gui_conect.title("Senha")
    gui_conect.geometry("300x200")

    password = Label(gui_conect, text = "Digite sua senha", bg = "pink")
    password_field = Entry(gui_conect) 
    password.place(relx=0.09, rely=0.1, relwidth=0.7, relheight=0.5)
    password_field.place(relx=0.17, rely=0.43, relwidth=0.6)

    add_buttom = Button(gui_conect, text = "Adicionar", fg = "Black", bg = "gray", command = lambda: verify(activated), height = 2, width = 20)
    add_buttom.place(relx=0.19, rely=0.6)

    activated = [0]
    while(activated[0] != 1):
        gui_conect.update()
    con = mysql.connector.connect(host = 'localhost', database = 'Aero', user = 'root', password = password_field.get())
    messagebox.showinfo("Info", "Conectado com sucesso! Pode fechar esta aba.")
    gui_conect.destroy()

    return con

if __name__ == "__main__" :
    ''' Configure the window interface '''
    gui = Tk()
    gui.configure(background = "light gray")
    gui.title("Banco de Dados")
    gui.geometry("1x1")

    con = connect()

    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão ", db_info)
        cursor = con.cursor()
        cursor.execute("select database();")
        linha = cursor.fetchone()
        print("Conectado ao banco de dados ", linha)

    gui.geometry("930x800")
    
    # Getting the columns from 'simulacoes'
    cursor.execute("SHOW COLUMNS FROM simulacoes")
    columns = cursor.fetchall()
    for i in range(len(columns)):
        columns_simu.append(columns[i][0])

    # Adding the columns that are not in the descriptions list
    k = len(descriptions)
    if len(columns) != len(descriptions):
        for i in range(len(columns) - k):
            descriptions.append(columns[k+i][0])

    restart_button = Button(gui, text = "Reiniciar", fg = "Black", bg = "gray", command = restart, height = 2, width = 10)
    restart_button.place(x = 717, y = 750)

    add_simu = Button(gui, text = "Adicionar Simulação", fg = "Black", bg = "gray", command = add_simulation, height = 2, width = 20)
    add_simu.place(x = 250, y = 250)

    add_test_button = Button(gui, text = "Adicionar Teste", fg = "Black", bg = "gray", command = add_test, height = 2, width = 20)
    add_test_button.place(x = 500, y = 250)

    look_simu = Button(gui, text = "Ver Simulação", fg = "Black", bg = "gray", command = look_simulation, height = 2, width = 20)
    look_simu.place(x = 250, y = 500)

    look_test_button = Button(gui, text = "Ver Teste", fg = "Black", bg = "gray", command = look_test, height = 2, width = 20)
    look_test_button.place(x = 500, y = 500)

    gui.mainloop()