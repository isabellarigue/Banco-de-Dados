# Naca airfoil generator
import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt
from numpy import cos
from numpy import arctan


series = int(input('Digite aqui a série de perfis NACA desejada (4 ou 5):'))
alarm = False

if series == 4:
    alarm = False
    print('Foi selecionada a "Four digits NACA series"')
    print('Para esse tipo de aerofólio, será gerado um perfil de asa definido por 4 dígitos:')
    print('1° dígito: cambagem máxima do perfil em % do tamanho da corda da asa.')
    print('2° dígito: distância do ponto de cambagem máx do bordo de ataque em décimos de corda.')
    print('3° e 4° dígitos: espessura máx do perfil em % da corda.')
    camber = int(input('Insira o primeiro dígito:'))
    dist_max_camber = int(input('Insira o segundo dígito:'))
    max_thickness = int(input('Insira os dois últimos dígitos(máx = 30):'))
    if camber == 0 and dist_max_camber == 0:
        t = max_thickness/100
        lista_x = np.linspace(0, 1, num=200)
        positive_y_coordinates = []
        negative_y_coordinates = []
        for x in lista_x:
            y = 5*t*(0.2969*sqrt(x)-0.1260*(x)-0.3516*(x*x)+0.2843*(x*x*x)-0.1036*(x*x*x*x))
            positive_y_coordinates.append(y)
            negative_y_coordinates.append(-y)
        plt.plot(lista_x, positive_y_coordinates)
        plt.plot(lista_x, negative_y_coordinates)
        plt.grid(True)
        plt.yticks(np.arange(-0.4,0.5,0.1))
        plt.show()
    if camber != 0:
        c = 1
        t = max_thickness/100
        pc = dist_max_camber/10
        lista_x = np.linspace(0, 1, num=200)
        upper_y_coordinates = []
        lower_y_coordinates = []
        camber_bent_coordinates =[]
        for x in lista_x:
            if 0 <= x <= pc:
                mean_camber_bent_one = ((camber/100)/(pc*pc))*(2*pc*x-(x*x))
                camber_bent_coordinates.append(mean_camber_bent_one)
                derivative = (2*(camber/100)/(pc*pc))*(pc-x)
                theta = arctan(derivative)
                upper_yt = (t/0.2)*(0.2969*sqrt(x)-0.1260*(x)-0.3516*(x*x)+0.2843*(x*x*x)-0.1036*(x*x*x*x))
                lower_yt = -(t/0.2)*(0.2969*sqrt(x)-0.1260*(x)-0.3516*(x*x)+0.2843*(x*x*x)-0.1036*(x*x*x*x))
                y_upper_final_coordinates = mean_camber_bent_one + (upper_yt*cos(theta))
                upper_y_coordinates.append(y_upper_final_coordinates)
                y_lower_final_coordinates = mean_camber_bent_one + (lower_yt*cos(theta))
                lower_y_coordinates.append(y_lower_final_coordinates)
            if pc <= x <= c:
                mean_camber_bent_two = ((camber/100)/((1-pc)*(1-pc)))*((1-(2*pc))+2*pc*x-(x*x))
                camber_bent_coordinates.append(mean_camber_bent_two)
                derivative = (2*(camber/100)/((1-pc)*(1-pc)))*(pc-x)
                theta = arctan(derivative)
                upper_yt = (t/0.2)*(0.2969*sqrt(x)-0.1260*(x)-0.3516*(x*x)+0.2843*(x*x*x)-0.1036*(x*x*x*x))
                lower_yt = -(t/0.2)*(0.2969*sqrt(x)-0.1260*(x)-0.3516*(x*x)+0.2843*(x*x*x)-0.1036*(x*x*x*x))
                y_upper_final_coordinates = mean_camber_bent_two + (upper_yt*cos(theta))
                upper_y_coordinates.append(y_upper_final_coordinates)
                y_lower_final_coordinates = mean_camber_bent_two + (lower_yt*cos(theta))
                lower_y_coordinates.append(y_lower_final_coordinates)
        plt.plot(lista_x, camber_bent_coordinates)
        plt.plot(lista_x, upper_y_coordinates)
        plt.plot(lista_x, lower_y_coordinates)
        plt.grid(True)
        plt.yticks(np.arange(-0.4,0.5,0.1))
        plt.show()
if series == 5:
    alarm = False
    print('Foi selecionada a "Five digits NACA series"')
    print('Para esse tipo de aerofólio, será gerado um perfil de asa definido por 5 dígitos:')
    print('1° dígito: um dígito único que multiplicado por 3/20 representa o Cl no ângulo de ataque ideal (é diferente do Cl normal!) (valor de Cl min = 0.005 e max = 1).')
    print('2º dígito: este valor dividido por 20 dá a distância do ponto de cambagem máx do bordo de ataque em % da corda.')
    print('3° dígito: indica o tipo de linha de cambagem, sendo 0 p/ normal e 1 p/ refletida.')
    print('Os 2° e 3° dígitos são dados em conjunto e são tabelados, a seguir os valores possíveis:')
    print('10; 20; 30; 40; 50; 21; 31; 41 e 51')
    print('4° e 5° dígitos: espessura máx do perfil em % da corda.')
    first = int(input('Insira o primeiro dígito:'))
    cl = first * 3/20
    second = int(input('Insira os 2° e 3° dígitos:'))
    max_thickness = int(input('Insira os 4° e 5° dígitos:'))
    t = max_thickness/100
    lista_x = lista_x = np.linspace(0, 1, num=200)
    upper_y_coordinates = []
    lower_y_coordinates = []
    camber_bent_coordinates = []
    if second == 10:
        r = 0.0580
        k1 = 361.400
    if second == 20:
        r = 0.1260
        k1 = 51.640
    if second == 30:
        r = 0.2025
        k1 =15.957
    if second == 40:
        r = 0.2900
        k1 = 6.643
    if second == 50:
        r = 0.3910	
        k1 = 3.230
    if second == 21:
        r = 0.1300	
        k1 = 51.990	
        div = 0.000764
    if second == 31:
        r = 0.2170	
        k1 = 15.793	
        div = 0.00677
    if second == 41:
        r = 0.3180	
        k1 = 6.520	
        div = 0.0303
    if second == 51:
        r = 0.4410	
        k1 = 3.191	
        div = 0.1355
    if (second % 2) == 0:
        for x in lista_x:
            if 0 <= x < r:
                yc = (k1/6)*((x**3)-3*r*(x**2)+(r**2)*(3-r)*x)
                camber_bent_coordinates.append(yc)
                gradient = (k1/6)*(3*(x*x)-(6*r*x)+((r*r)*(3-r)))
                theta = arctan(gradient)
                upper_yt = (t/0.2)*(0.2969*sqrt(x)-0.1260*(x)-0.3516*(x*x)+0.2843*(x*x*x)-0.1036*(x*x*x*x))
                lower_yt = -(t/0.2)*(0.2969*sqrt(x)-0.1260*(x)-0.3516*(x*x)+0.2843*(x*x*x)-0.1036*(x*x*x*x))
                y_upper_final_coordinates = yc + (upper_yt*cos(theta))
                upper_y_coordinates.append(y_upper_final_coordinates)
                y_lower_final_coordinates = yc + (lower_yt*cos(theta))
                lower_y_coordinates.append(y_lower_final_coordinates)
            if r <= x <= 1:
                yc = ((k1*(r**3))/6)*(1-x)
                camber_bent_coordinates.append(yc)
                gradient = - ((k1*(r**3))/6)
                theta = arctan(gradient)
                upper_yt = (t/0.2)*(0.2969*sqrt(x)-0.1260*(x)-0.3516*(x*x)+0.2843*(x*x*x)-0.1036*(x*x*x*x))
                lower_yt = -(t/0.2)*(0.2969*sqrt(x)-0.1260*(x)-0.3516*(x*x)+0.2843*(x*x*x)-0.1036*(x*x*x*x))
                y_upper_final_coordinates = yc + (upper_yt*cos(theta))
                upper_y_coordinates.append(y_upper_final_coordinates)
                y_lower_final_coordinates = yc + (lower_yt*cos(theta))
                lower_y_coordinates.append(y_lower_final_coordinates)
        plt.plot(lista_x, camber_bent_coordinates)
        plt.plot(lista_x, upper_y_coordinates)
        plt.plot(lista_x, lower_y_coordinates)
        plt.grid(True)
        plt.yticks(np.arange(-0.4,0.5,0.1))
        plt.show()
    if (second % 2) == 1:
        for x in lista_x:
            if 0 <= x < r:
                yc = (k1/6)*(((x-r)**3)-div*((1-r)**3)*x-(r**3)*x+(r**3))
                camber_bent_coordinates.append(yc)
                gradient = (k1/6)*(3*((x-r)**2)-div*((1-r)**3)-(r**3))
                theta = arctan(gradient)
                upper_yt = (t/0.2)*(0.2969*sqrt(x)-0.1260*(x)-0.3516*(x*x)+0.2843*(x*x*x)-0.1036*(x*x*x*x))
                lower_yt = -(t/0.2)*(0.2969*sqrt(x)-0.1260*(x)-0.3516*(x*x)+0.2843*(x*x*x)-0.1036*(x*x*x*x))
                y_upper_final_coordinates = yc + (upper_yt*cos(theta))
                upper_y_coordinates.append(y_upper_final_coordinates)
                y_lower_final_coordinates = yc + (lower_yt*cos(theta))
                lower_y_coordinates.append(y_lower_final_coordinates)
            if r <= x <= 1:
                yc = (k1/6)*(div*((x-r)**3)-div*((1-r)**3)*x-(r**3)*x+(r**3))
                camber_bent_coordinates.append(yc)
                gradient = (k1/6)*(3*div*((x-r)**2)-div*((1-r)**3)-(r**3))
                theta = arctan(gradient)
                upper_yt = (t/0.2)*(0.2969*sqrt(x)-0.1260*(x)-0.3516*(x*x)+0.2843*(x*x*x)-0.1036*(x*x*x*x))
                lower_yt = -(t/0.2)*(0.2969*sqrt(x)-0.1260*(x)-0.3516*(x*x)+0.2843*(x*x*x)-0.1036*(x*x*x*x))
                y_upper_final_coordinates = yc + (upper_yt*cos(theta))
                upper_y_coordinates.append(y_upper_final_coordinates)
                y_lower_final_coordinates = yc + (lower_yt*cos(theta))
                lower_y_coordinates.append(y_lower_final_coordinates)
        plt.plot(lista_x, camber_bent_coordinates)
        plt.plot(lista_x, upper_y_coordinates)
        plt.plot(lista_x, lower_y_coordinates)
        plt.grid(True)
        plt.yticks(np.arange(-0.4,0.5,0.1))
        plt.show()
if series != 4 and series != 5:
    alarm = True
    if alarm is True:
        print('Foi selecionada uma série inválida para perfis NACA')