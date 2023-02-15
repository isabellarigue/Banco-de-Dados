from datetime import datetime
import mysql.connector
import os

# Name of the directory containing the reports
directory = "Reports"

files = os.listdir(directory)

# If you want to add the link of the simulation, put it in the variable below
link = ""

# Getting the date
date = datetime.now().strftime('%Y/%m/%d')

# Connect to the database
con = mysql.connector.connect(host = '192.168.0.116', database = 'Aero', user = 'root', password = '')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ", db_info)  

for report in files:
    # Opening the report and getting the drag and downforce values
    # Ex: lines[5] = "airfoil                   (13.989227 -33.100513 0)                      (0.044925034 -0.03932257 0)                   (14.034152 -33.139836 0) "
    with open(f'Reports/{report}', "r") as f:
        lines = f.readlines()
        count = i = 0
        for character in lines[5]:
            i += 1
            if character == "(" or character == ")":
                count += 1
            if count == 5:
                drag = ""
                downforce = ""
                while lines[5][i] != " ":
                    drag += lines[5][i]
                    i += 1
                i += 1
                while lines[5][i] != " ":
                    downforce += lines[5][i]
                    i += 1
                break
    f.close()

    # Inserting the report information into the database
    con.cursor().execute("INSERT INTO ansys (nome, dia, downforce, drag, link) VALUES (%s, %s, %s, %s, %s)", (report, date, downforce, drag, link))
    con.commit()

    print("Sucess")
