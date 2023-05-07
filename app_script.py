from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys
import os
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Lists used to store global information that is used by different functions
columns_simu = []
columns_test = []
descriptions = ["Nome", "Link do arquivo no drive", "Data (formato ano/mês/dia) ", "Responsável","Coeficiente de Lift (utilizar ponto como separador de decimais) ", "Coeficiente de Drag (utilizar ponto como separador de decimais) ", "Configuração: digite 1 p/ carro completo, 2 p/ asa traseira, 3 p/ asa dianteira, 4 p/ radiador, 5 p/ difusor, 6 p/ outros", "Velocidade em km/h", "Área em m2"]
descriptions_tests = ["Nome", "Data (formato ano/mês/dia) ", "Configuração: digite 1 para o carro completo, 2 para asa traseira, 3 para asa dianteira, 4 para radiador, 5 para outros","Velocidade em km/h", "Front left", "Front right", "Rear left", "Rear right", "Carga", "Seção área túnel (m2)", "Peso do carro (kg)", "Área frontal do modelo (m2)"]
view_tests = ["Nome", "Data (formato ano/mês/dia) ", "Configuração: 1- carro completo, 2- asa traseira, 3- asa dianteira, 4- radiador, 5- outros","Velocidade em km/h", "Seção área túnel", "Peso do carro", "Área frontal do modelo", "Cl", "Cd", "Downforce", "Drag"]
password_list = ["planet"]

def change_mysql(i, window, lines, field, table):
    ''' Changes the value of the chosen parameter on the database '''
    if table == "simulacoes":
        element_changed = columns_simu[i]
    else:
        element_changed = columns_test[i]
    new_value = field.get()
    comando = "UPDATE "+table+" SET "+element_changed+" = "+"'"+new_value+"'"+" WHERE nome = "+"'"+str(lines[0])+"'"
    try:
        con = connect()
        con.cursor().execute(comando)
        con.commit()
        messagebox.showinfo("Info", "Valor alterado com sucesso!")
        disconnect(con)
    except:
        messagebox.showinfo("Info", "Erro ao alterar valor. Verifique se o valor está no formato correto.")
    window.destroy()

def change_parameter(window, lines, answer, table):
    ''' Creates the visual interface for the user to enter the new value '''
    i = int(answer.get()) # number of the chosen parameter
    window.destroy()
    gui_change_parameter = Toplevel() 
    gui_change_parameter.configure(background = "#202020")
    gui_change_parameter.title("Alterar valor")
    gui_change_parameter.geometry("500x200")

    change_label = Label(gui_change_parameter, text = "Digite o novo valor na formatação adequada.", bg = "#F59E1B")
    change_field = Entry(gui_change_parameter) 
    change_label.place(relx=0.16, rely=0.1, relwidth=0.7, relheight=0.5)
    change_field.place(relx=0.22, rely=0.43, relwidth=0.6)

    addButtom = Button(gui_change_parameter, text = "Adicionar", fg = "Black", bg = "#F59E1B", command = lambda: change_mysql(i, gui_change_parameter, lines, change_field, table), height = 2, width = 20)
    addButtom.place(relx=0.35, rely=0.6)

def choose_parameter(lines, descriptions, table):
    ''' Creates an Entry for the user to enter which parameter he wants to change. So, all available parameters are shown on the screen. '''
    gui_choose_parameter = Toplevel() 
    gui_choose_parameter.configure(background = "#202020")
    gui_choose_parameter.title("Escolha o parâmetro")
    gui_choose_parameter.geometry("750x500")

    which_number = Label(gui_choose_parameter, text = "Digite o n° do parâmetro que deseja editar", bg = "#F59E1B")
    answer = Entry(gui_choose_parameter) 
    which_number.place(relx=0.01, rely=0.03)
    answer.place(relx=0.01, rely=0.075, relwidth=0.3)
    pButtom = Button(gui_choose_parameter, text = "Selecionar", fg = "Black", bg = "#F59E1B", command = lambda: change_parameter(gui_choose_parameter, lines, answer, table))
    pButtom.place(relx=0.45, rely=0.075)

    # Showing all available parameters and their respective numbers
    rel_y = 0.2
    for i in range(len(descriptions)):
        desc = Label(gui_choose_parameter, text = descriptions[i], bg = "#E0E0E0")
        number = Label(gui_choose_parameter, text = i, bg = "#E0E0E0")
        desc.place(relx=0.01, rely=rel_y)
        number.place(relx=0.8, rely=rel_y, relwidth=0.08)
        rel_y += 0.05

def delete_simu(link, gui):
    ''' Deletes a simulation from the database according to its link '''
    okcancel = messagebox.askokcancel("Atenção!!!", "Tem certeza que deseja excluir a simulação? Essa ação é irreversível.")
    if(okcancel == True):
        command = "DELETE FROM simulacoes WHERE link = "+"'"+str(link)+"'"  
        con = connect()
        con.cursor().execute(command)
        con.commit()
        messagebox.showinfo("Info", "Simulação excluída com sucesso!")
        disconnect(con)
        gui.destroy()
    return

def delete_test(nome, gui):
    ''' Deletes a test from the database according to its link '''
    okcancel = messagebox.askokcancel("Atenção!!!", "Tem certeza que deseja excluir o teste? Essa ação é irreversível.")
    if(okcancel == True):
        command = "DELETE FROM testes WHERE nome = "+"'"+str(nome)+"'"  
        con = connect()
        con.cursor().execute(command)
        con.commit()
        messagebox.showinfo("Info", "Teste excluída com sucesso!")
        disconnect(con)
        gui.destroy()
    return

def add_char(parameter_field, window, table):
    ''' Add a new column to the database for str values '''
    new_parameter = parameter_field.get()
    con = connect()
    cursor = con.cursor()
    query = "ALTER TABLE "+table+" ADD "+new_parameter+" VARCHAR(100)"
    
    try:
        cursor.execute(query)
        messagebox.showinfo("Info", "Parâmetro adicionado com sucesso! Pode fechar esta aba.")
        window.destroy()
        disconnect(con)
    except:
        messagebox.showinfo("Info", "Algo deu errado. Lembre-se de não utilizar espaço ou acento nome.")
        disconnect(con)

def add_int(parameter_field, window, table):
    ''' Add a new column to the database for int values '''
    new_parameter = parameter_field.get()
    con = connect()
    cursor = con.cursor()
    query = "ALTER TABLE "+table+" ADD "+new_parameter+" INT"
    
    try:
        cursor.execute(query)
        messagebox.showinfo("Info", "Parâmetro adicionado com sucesso! Pode fechar esta aba.")
        window.destroy()
        disconnect(con)
    except:
        messagebox.showinfo("Info", "Algo deu errado. Lembre-se de não utilizar espaço ou acento no nome.")
        disconnect(con)
    
def add_column(table):
    ''' Creates the visual interface for the user to enter the name and type of the new column. '''
    gui_add_column = Toplevel()
    gui_add_column.configure(background = "#202020")
    gui_add_column.title("Adicionar parâmetro")
    gui_add_column.geometry("400x200")

    parameter = Label(gui_add_column, text = "Digite o nome do novo parâmetro", bg = "#F59E1B", font=("Arial", 12))
    parameter_field = Entry(gui_add_column, bg = "#E0E0E0") 
    parameter.place(relx=0.12, rely=0.1, relwidth=0.7, relheight=0.5)
    parameter_field.place(relx=0.21, rely=0.43, relwidth=0.47)

    add_char_buttom = Button(gui_add_column, text = "Adicionar char", fg = "Black", bg = "#F59E1B", command = lambda: add_char(parameter_field, gui_add_column, table), height = 2, width = 20)
    add_char_buttom.place(relx=0.12, rely=0.6)

    add_int_buttom = Button(gui_add_column, text = "Adicionar int", fg = "Black", bg = "#F59E1B", command = lambda: add_int(parameter_field, gui_add_column, table), height = 2, width = 20)
    add_int_buttom.place(relx=0.45, rely=0.6)

def canvas(alto, ancho, gui):
    ''' Creates a canvas for the user to scroll the screen '''
    # Create A Main Frame
    main_frame = Frame(gui,width=ancho,height=alto)
    main_frame.place(x=0,y=0)

    # Create A Canvas
    my_canvas = Canvas(main_frame, width=ancho, height=alto)
    my_canvas.place(x=0,y=0)

    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.place(x=810,y=0,height=alto)

    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.configure(background = "#202020")
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    def _on_mouse_wheel(event):
        my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")
    my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas,width=ancho,height=alto)
    second_frame.place(x=0,y=0)
    second_frame.configure(background = "#202020")

    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    return second_frame

def show_simulation(data_look_simu):
    ''' Shows the simulation information on the screen '''
    chosen = data_look_simu[0].get() #cb_simus.get

    # Searching on the database the simulation with the name chosen by the user
    for i in range(len(data_look_simu[1])):
        if(data_look_simu[1][i] == chosen):
            lines = data_look_simu[3][i]

            # Displaying the simulation information on the screen
            gui_look_simu = data_look_simu[2]

            second_frame = canvas(800, 830, gui_look_simu)

            name = Label(second_frame, text = descriptions[0], bg = "#F59E1B")
            nameField = Label(second_frame, text = lines[0], bg = "#E0E0E0")
            name.place(relx=0.1, y=230)
            nameField.place(relx=0.1, y=250, relwidth=0.8)

            link = Label(second_frame, text = "Link do arquivo no drive", bg = "#F59E1B")
            linkField = Entry(second_frame, bg = "#E0E0E0") 
            linkField.insert(0, lines[1])
            delete_info = lines[1] # Storing the link of the simulation if wanted to delete it later
            link.place(relx=0.1, y=298)
            linkField.place(relx=0.1, y=318, relwidth=0.8)

            rel_x = 0.1
            rel_y = 366
            height = 0
            for i in range(2,len(descriptions)):
                desc = Label(second_frame, text = descriptions[i], bg = "#F59E1B")
                descField = Label(second_frame, text = lines[i], bg = "#E0E0E0")
                desc.place(relx=rel_x, y=rel_y)
                descField.place(relx=rel_x, y=rel_y+20, relwidth=0.8)
                height += 150
                second_frame.configure(height=height) #Changing the height of the second_frame each time a button is added
                rel_y += 68

            new_column_buttom = Button(second_frame, text = "Adicionar novo parâmetro", fg = "Black", bg = "#F59E1B", command = lambda: add_column("simulacoes"), height = 2, width = 20)
            new_column_buttom.place(relx=0.3, rely=0.1)

            delete_buttom = Button(second_frame, text = "Excluir simulação", fg = "Black", bg = "#F59E1B", command = lambda: delete_simu(delete_info, gui_look_simu), height = 2, width = 20)
            delete_buttom.place(relx=0.5, rely=0.1)

            edit_buttom = Button(second_frame, text = "Editar algum valor", fg = "Black", bg = "#F59E1B", command = lambda: choose_parameter(lines, descriptions, "simulacoes"), height = 2, width = 20)
            edit_buttom.place(relx=0.7, rely=0.1)

            return_buttom = Button(second_frame, text = "Voltar", fg = "Black", bg = "#F59E1B", command = look_simulation, height = 2, width = 20)
            return_buttom.place(relx=0.1, rely=0.1)

def histogram_star(type, gui, enum):
    '''Generate and show histogram.'''
    gui.destroy()
    con = connect()
    cursor = con.cursor()
    if enum == 6:
        cursor.execute("select cl, cd from simulacoes") # all types of simulation
        type = "(incluindo todas as configurações)"
    else:
        cursor.execute("select cl, cd from simulacoes where config = "+str(enum))
    lines = cursor.fetchall()
    cl = []
    cd = []
    for line in lines:
        cl.append(float(line[0]))
        cd.append(float(line[1]))
    plt.hist(cl)
    plt.title("Cl simulações "+type)
    plt.xlabel("Coeficiente de Lift")
    plt.ylabel("Frequência")
    plt.show()
    plt.hist(cd)
    plt.title("Cd simulações "+type)
    plt.xlabel("Coeficiente de Drag")
    plt.ylabel("Frequência")
    plt.show()
    disconnect(con)

def choose_histogram():
    gui_choose = Toplevel()
    gui_choose.title("Escolher qual a configuração de simulação")
    gui_choose.geometry("350x250")

    second_frame = canvas(250, 350, gui_choose)
    second_frame.configure(background = "#202020")

    instructions = Label(second_frame, text = "Escolha qual a configuração de simulação.", fg = "black", bg = "#F59E1B", height = 2, width = 40)
    instructions.place(relx=0.1, y=65)

    options = ["Carro completo", "Asa traseira", "Asa dianteira", "Radiador", "Difusor", "Tudo"]
    cb = ttk.Combobox(second_frame, values=options)
    cb.place(relx=0.18, y = 170)

    confirm_button = Button(second_frame, text = "Confirmar", fg = "Black", bg = "#F59E1B", command=lambda: histogram_star(cb.get(), gui_choose, options.index(cb.get())+1), height = 2, width = 10)
    confirm_button.place(relx=0.68, y=170)
    

def look_simulation(gui):
    ''' Create the visual interface for the user select which simulation he wants to see '''
    gui.destroy()
    gui_look_simu = Toplevel()
    gui_look_simu.title("Ver simulação")
    gui_look_simu.configure(background = "#202020")
    gui_look_simu.geometry("830x700")

    # Creating a list with all simulation names in order to display in the Combobox format for the user to select
    con = connect()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM simulacoes")
    lines = cursor.fetchall()
    names = [] 
    for line in lines:
        names.append(line[0])
    disconnect(con)

    cb_simus = ttk.Combobox(gui_look_simu, values=names)
    cb_simus.set("Selecione uma simulação")
    cb_simus.place(relx=0.1, rely=0.03, relwidth=0.8)

    # Saving this data to be able to use in another function
    data_look_simu = []
    data_look_simu.append(cb_simus)
    data_look_simu.append(names)
    data_look_simu.append(gui_look_simu)
    data_look_simu.append(lines)

    show_buttom = Button(gui_look_simu, text = "Mostrar", fg = "Black", bg = "#F59E1B", command = lambda: show_simulation(data_look_simu), height = 2, width = 20)
    show_buttom.bind("<Return>", lambda event, arg1=data_look_simu : show_simulation(arg1))
    show_buttom.focus_force()
    show_buttom.place(relx=0.1, rely=0.1)

    histogram_buttom = Button(gui_look_simu, text = "Ver histograma", fg = "Black", bg = "#F59E1B", command = choose_histogram, height = 2, width = 20)
    histogram_buttom.place(relx=0.3, rely=0.1)

def show_test(data_look_test):
    ''' Shows the test on the screen '''
    chosen = data_look_test[0].get()

    # Searching on the database the simulation with the name chosen by the user
    for i in range(len(data_look_test[1])):
        if(data_look_test[1][i] == chosen):
            lines = data_look_test[3][i]

            #Displaying the test information on the screen
            gui_look_test = data_look_test[2]

            second_frame = canvas(800, 830, gui_look_test)
            second_frame.configure(background = "#202020")

            name = Label(second_frame, text = descriptions_tests[0], bg = "#F59E1B")
            nameField = Label(second_frame, text = lines[0], bg = "#E0E0E0")
            name.place(relx=0.1, y=170)
            nameField.place(relx=0.1, y=190, relwidth=0.8)

            delete_info =  lines[0] # Storing the name of the test if wanted to delete it later

            rel_x = 0.1
            rel_y = 238
            height = 0
            for i in range(1,4):
                desc = Label(second_frame, text = view_tests[i], bg = "#F59E1B")
                descField = Label(second_frame, text = lines[i], bg = "#E0E0E0")
                desc.place(relx=rel_x, y=rel_y)
                descField.place(relx=rel_x, y=rel_y+20, relwidth=0.8)
                height += 120
                second_frame.configure(height=height) #Changing the height of the second_frame each time a button is added
                rel_y += 68
            for i in range(4,11):
                desc = Label(second_frame, text = view_tests[i], bg = "#F59E1B")
                descField = Label(second_frame, text = lines[i+5], bg = "#E0E0E0")
                desc.place(relx=rel_x, y=rel_y)
                descField.place(relx=rel_x, y=rel_y+20, relwidth=0.8)
                height += 120
                second_frame.configure(height=height) #Changing the height of the second_frame each time a button is added
                rel_y += 68

            delete_buttom = Button(second_frame, text = "Excluir teste", fg = "Black", bg = "#F59E1B", command = lambda: delete_test(delete_info, gui_look_test), height = 2, width = 20)
            delete_buttom.place(relx=0.5, rely=0.1)

            return_buttom = Button(second_frame, text = "Voltar", fg = "Black", bg = "#F59E1B", command = look_test, height = 2, width = 20)
            return_buttom.place(relx=0.2, rely=0.1)

def look_test():
    ''' Creates the visual interface for the user select wich test he wants to see '''
    gui_look_test = Toplevel()
    gui_look_test.configure(background = "#202020")
    gui_look_test.title("Ver teste")
    gui_look_test.geometry("830x700")

    # Creating a list with all tests names in order to display in the Combobox format for the user to select
    con = connect()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM testes")
    lines = cursor.fetchall()
    names = [] 
    for line in lines:
        names.append(line[0])
    disconnect(con)

    cb_test = ttk.Combobox(gui_look_test, values=names)
    cb_test.set("Selecione um teste")
    cb_test.place(relx=0.1, rely=0.03, relwidth=0.8)

    # Saving this data to be able to use in another function
    data_look_test = []
    data_look_test.append(cb_test)
    data_look_test.append(names)
    data_look_test.append(gui_look_test)
    data_look_test.append(lines)

    show_buttom = Button(gui_look_test, text = "Mostrar", fg = "Black", bg = "#F59E1B", command = lambda: show_test(data_look_test), height = 2, width = 20)
    show_buttom.bind("<Return>", lambda event, arg1=data_look_test : show_test(arg1))
    show_buttom.focus_force()
    show_buttom.place(relx=0.1, rely=0.1)

def add_simulation_sql(data_simu):
    ''' Take the information that the user has entered and add it to the database '''
    con = connect()
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

    try:
        cursor.execute("INSERT INTO simulacoes "+written_columns+" VALUES "+written_values+"", written_infos)
        con.commit()
        messagebox.showinfo("Info", "Simulação adicionada com sucesso! Pode fechar esta aba.")
        disconnect(con)
    except Exception as inst:
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)          # __str__ allows args to be printed directly,
        messagebox.showerror("Erro", "Não foi possível adicionar a simulação. Verifique se todos os campos foram preenchidos corretamente.")
        disconnect(con)
    return 

def add_simulation():
    ''' Create the visual interface to add a new simulation. '''
    gui_add_simu = Toplevel()
    gui_add_simu.title("Adicionar nova simulação")
    gui_add_simu.geometry("830x700")

    second_frame = canvas(700, 830, gui_add_simu)
    second_frame.configure(background = "#202020")

    instructions = Label(second_frame, text = "Digite todas as informações e pressione o botão confirmar. Caso não tenha algum parâmetro, apenas deixe em branco.", fg = "black", bg = "#F59E1B", height = 2, width = 95)
    instructions.place(relx=0.1, y=70)

    # Creating the labels for the data and storing them on a list
    rel_x = 0.1
    rel_y = 130
    height = 0
    data_simu = []
    for i in range(len(descriptions)):
        desc = Label(second_frame, text = descriptions[i], bg = "#F59E1B")
        descField = Entry(second_frame, bg = "#E0E0E0")
        desc.place(relx=rel_x, y=rel_y)
        descField.place(relx=rel_x, y=rel_y+20, relwidth=0.8)
        data_simu.append(descField)
        height += 140
        second_frame.configure(height=height) #Changing the height of the second_frame each time a button is added
        rel_y += 68

    add_simu_sql = Button(second_frame, text = "Confirmar", fg = "Black", bg = "#F59E1B", command=lambda: add_simulation_sql(data_simu), height = 2, width = 20)
    add_simu_sql.place(relx=0.38, y=rel_y+20)

def calculate_cl_cd(con, cursor, name, vel, area_tunel, lift, drag, area_frontal):
    ''' Calculates the cl and cd value for the user '''
    p = 1.162
    area = area_frontal
    cl = (lift)/(0.5*p*(int(vel)**2)*area)
    cd = (drag)/(0.5*p*(int(vel)**2)*area)

    # wind tunnel values ​​correction count
    cl = cl*(1/((1 + ((1/4) * (area_frontal/area_tunel)))**2)) 
    cd = cd*(1/((1 + ((1/4) * (area_frontal/area_tunel)))**2)) 

    cursor.execute("UPDATE testes SET cl = "+"'"+str(cl)+"'"+" WHERE nome = "+"'"+str(name)+"'")
    cursor.execute("UPDATE testes SET cd = "+"'"+str(cd)+"'"+" WHERE nome = "+"'"+str(name)+"'")
    con.commit()
    return

def add_test_sql(data_test):
    ''' Takes teh information that the user has entered and add it to the database '''
    con = connect()
    cursor = con.cursor()

    # Putting in the proper formatting of the mySQL command
    written_columns = "("
    for i in range(len(columns_test)):
        written_columns += columns_test[i]
        if i != len(columns_test)-1:
            written_columns += ", "
    written_columns += ")"

    written_values = "("
    for i in range(len(columns_test)):
        written_values += "%s"
        if i != len(columns_test)-1:
            written_values += ", "
    written_values += ")"

    written_infos = []
    for i in range(len(descriptions_tests)):
        written_infos.append((data_test[i]).get())
    written_infos.append("0") # values ​​of the coefficients that will be replaced
    written_infos.append("0")

    try:
        lift = float(data_test[4].get()) + float(data_test[5].get()) + float(data_test[6].get()) + float(data_test[7].get()) - float(data_test[10].get()) # soma das balanças - peso do carro
        drag = float(data_test[8].get()) # célula de carga
        written_infos.append(lift)
        written_infos.append(drag)
        cursor.execute("INSERT INTO testes "+written_columns+" VALUES "+written_values+"", written_infos)
        con.commit()
        calculate_cl_cd(con, cursor, data_test[0].get(), float(data_test[3].get()), float(data_test[-3].get()), lift, drag, float(data_test[-1].get()))
        messagebox.showinfo("Info", "Teste adicionado com sucesso! Pode fechar esta aba.")
        disconnect(con)
    except Exception as error:
        print(error)
        messagebox.showerror("Erro", "Não foi possível adicionar o teste. Verifique se todos os campos foram preenchidos corretamente.")
        disconnect(con)
    return

def add_test():
    ''' Create the visual interface to add a new test. '''
    gui_add_test = Toplevel()
    gui_add_test.title("Adicionar novo teste")
    gui_add_test.geometry("830x700")

    second_frame = canvas(800, 830, gui_add_test)

    instructions = Label(second_frame, text = "Digite todas as informações e pressione o botão confirmar. Caso não tenha algum parâmetro, apenas deixe em branco.", fg = "black", bg = "#F59E1B", height = 2, width = 95)
    instructions.place(relx=0.1, y=70)

    # Creating the labels for the data and storing them on a list
    rel_x = 0.1
    rel_y = 130
    height = 0
    data_test = []
    for i in range(len(descriptions_tests)):
        desc = Label(second_frame, text = descriptions_tests[i], bg = "#F59E1B")
        descField = Entry(second_frame, bg = "#E0E0E0")
        desc.place(relx=rel_x, y=rel_y)
        descField.place(relx=rel_x, y=rel_y+20, relwidth=0.8)
        data_test.append(descField)
        height += 100
        second_frame.configure(height=height) #Changing the height of the second_frame each time a button is added
        rel_y += 68

    data_test[-3].insert(0, "10") # standard value; Section Area 
    data_test[-2].insert(0, "350") # standard value; Weight
    data_test[-1].insert(0, "1.08") # standard value; Frontal Area

    add_tests_sql = Button(second_frame, text = "Confirmar", fg = "black", bg = "#F59E1B", command=lambda: add_test_sql(data_test), height = 2, width = 20)
    add_tests_sql.place(relx=0.38, y=rel_y+20)

def add_coastdown():
    return

def add_velocidade_constante():
    return

def add_tufts():
    return

def add_tempo_volta():
    return

def redirect(gui, type):
    gui.destroy()
    if type == "Denso":
        add_test()
    elif type == "Coastdown":
        add_coastdown()
    elif type == "Velocidade Constante":
        add_velocidade_constante()
    elif type == "Tufts":
        add_tufts()
    else: # type == "Tempo de volta"
        add_tempo_volta()

def choose_test():
    gui_choose = Toplevel()
    gui_choose.title("Escolher qual o teste")
    gui_choose.geometry("350x250")

    second_frame = canvas(250, 350, gui_choose)
    second_frame.configure(background = "#202020")

    instructions = Label(second_frame, text = "Escolha qual o teste realizado.", fg = "black", bg = "#F59E1B", height = 2, width = 40)
    instructions.place(relx=0.1, y=65)

    options = ["Denso", "Coastdown", "Velocidade Constante", "Tufts", "Tempo de volta"]
    cb = ttk.Combobox(second_frame, values=options)
    cb.place(relx=0.18, y = 170)

    confirm_button = Button(second_frame, text = "Confirmar", fg = "Black", bg = "#F59E1B", command=lambda: redirect(gui_choose, cb.get()), height = 2, width = 10)
    confirm_button.place(relx=0.68, y=170)

def show_ansys(gui):
    ''' Create the visual interface to show the ansys results, with histograms. '''
    gui.destroy()
    con = connect()
    cursor = con.cursor()

    try:
        cursor.execute("SELECT downforce, drag from ansys where position = 'Front'")
        lines = cursor.fetchall()
        lifts_front= []
        drags_front = []
        for line in lines:
            lifts_front.append(float(line[0]))
            drags_front.append(float(line[1]))
        plt.hist(lifts_front)
        plt.title("Lift asa dianteira")
        plt.xlabel("Lift (N)")
        plt.ylabel("Frequência")
        plt.show()
        plt.hist(drags_front)
        plt.title("Drag asa dianteira")
        plt.xlabel("Drag (N)")
        plt.ylabel("Frequência")
        plt.show()


        cursor.execute("SELECT downforce, drag from ansys where position = 'Rear'")
        lines = cursor.fetchall()
        lifts_rear = []
        drags_rear = []
        for line in lines:
            lifts_rear.append(float(line[0]))
            drags_rear.append(float(line[1]))
        plt.hist(lifts_rear)
        plt.title("Lift asa traseira")
        plt.xlabel("Lift (N)")
        plt.ylabel("Frequência")
        plt.show()
        plt.hist(drags_rear)
        plt.title("Drag asa traseira")
        plt.xlabel("Drag (N)")
        plt.ylabel("Frequência")
        plt.show()

        messagebox.showinfo("Info", "Todos os histogramas já foram mostrados.")
        disconnect(con)
    except Exception as error:
        messagebox.showerror("Erro", "Algo deu errado. " + str(error))
        disconnect(con)

def choose_simulation():
    ''' Create the visual interface to choose a simulation (star or ansys). '''
    gui_choose_simu = Toplevel()
    gui_choose_simu.title("Escolher qual o tipo de simulação")
    gui_choose_simu.geometry("350x250")

    second_frame = canvas(250, 350, gui_choose_simu)
    second_frame.configure(background = "#202020")

    instructions = Label(second_frame, text = "Escolha o tipo de simulação para visualizar.", fg = "black", bg = "#F59E1B", height = 2, width = 40)
    instructions.place(relx=0.1, y=65)

    star_button = Button(second_frame, text = "Star", fg = "Black", bg = "#e8a848", command=lambda: look_simulation(gui_choose_simu), height = 2, width = 10)
    star_button.place(relx=0.6, y=150)

    ansys_button = Button(second_frame, text = "Ansys", fg = "Black", bg = "#e8a848", command=lambda: show_ansys(gui_choose_simu), height = 2, width = 10)
    ansys_button.place(relx=0.2, y=150)

def restart():
    ''' Restart the program. '''
    python = sys.executable
    os.execl(python, python, * sys.argv) 

def export(table):
    ''' Export the data from the database to an excel file. '''
    con = connect()
    try:
        df = pd.read_sql("select * from "+table, con)
        df.to_excel("dados_aero_"+table+".xlsx", index=False)
        messagebox.showinfo("Info", "Dados exportados com sucesso!")
        disconnect(con)
    except Exception as inst:
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)          # __str__ allows args to be printed directly
        messagebox.showerror("Erro", "Não foi possível exportar os dados. Verifique se o arquivo não está aberto.")
        disconnect(con)
    return

def disconnect(con):
    ''' Close the connection to the database. '''
    if con.is_connected():
        con.cursor().close()
        con.close()
    return

def connect():
    ''' Make the connection to the database. '''
    # https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
    con = mysql.connector.connect(host = 'us-east.connect.psdb.cloud', database = 'aero', user = '7uofst2j1uddch3emsp7', password = "pscale_pw_j8CDx4RqLqZNskkSi0JqoZwYUy1b6F7XeJ7TbZZZBQ7", ssl_ca= "cacert.pem")
    return con

if __name__ == "__main__" :
    ''' Configure the window interface '''
    gui = Tk()
    #gui.configure(bg = PhotoImage(file = "Imagens\\formigao.png"))
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
        #cursor.execute("set workload='olap'") https://planetscale.com/blog/supports-notes-from-the-field

    gui.geometry("500x500")
    gui.configure(background = "#202020")

    title = Label(gui, text = "Banco de Dados", bg = "#202020", fg = "white", font=("Arial", 38))
    title.place(x=50, y=50)
    title1 = Label(gui, text = "Aero", bg = "#202020", fg = "white", font=("Arial", 44))
    title1.place(x=170, y=120)

    creators = Label(gui, text = "Feito por Isa e Ale.", bg = "#202020", fg = "white", font=("Helvetica", 10))
    creators.place(x=10, y=450)

    menubar = Menu(gui)
    filemenu = Menu(menubar)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exportar excel infos Star", command = lambda: export("simulacoes"))
    filemenu.add_command(label="Exportar excel infos Ansys", command = lambda: export("ansys"))
    filemenu.add_command(label="Exportar excel infos Denso", command = lambda: export("testes"))
    menubar.add_cascade(label="Reiniciar", command = restart)
    menubar.add_cascade(label="Exportar", menu=filemenu)
    gui.config(menu=menubar)
    
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

    # Getting the columns from 'testes'
    cursor.execute("SHOW COLUMNS FROM testes")
    columns = cursor.fetchall()
    for i in range(len(columns)):
        columns_test.append(columns[i][0])

    disconnect(con)

    add_simu = Button(gui, text = "Adicionar Simulação Star", fg = "Black", bg = "#F59E1B", command = add_simulation, height = 2, width = 20)
    add_simu.place(relx = 0.16, rely = 0.5)

    add_test_button = Button(gui, text = "Adicionar Teste", fg = "Black", bg = "#F59E1B", command = choose_test, height = 2, width = 20)
    add_test_button.place(relx = 0.5, rely = 0.5)

    look_simu = Button(gui, text = "Ver Simulação", fg = "Black", bg = "#F59E1B", command = choose_simulation, height = 2, width = 20)
    look_simu.place(relx = 0.16, rely = 0.7)

    look_test_button = Button(gui, text = "Ver Testes Denso", fg = "Black", bg = "#F59E1B", command = look_test, height = 2, width = 20)
    look_test_button.place(relx = 0.5, rely = 0.7)

    gui.mainloop()