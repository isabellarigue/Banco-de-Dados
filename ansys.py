from datetime import datetime
import mysql.connector
import os

# Name of the directory containing the reports
directory = "Reports/Rear_Reports"

files = os.listdir(directory)

# If you want to add the link of the simulation, put it in the variable below
link = ""

# Getting the date
date = datetime.now().strftime('%Y/%m/%d')

# Connect to the database
file = open("Others/password.txt", "r")
password = file.readline()
con = mysql.connector.connect(host = 'us-east.connect.psdb.cloud', database = 'aero', user = '7uofst2j1uddch3emsp7', password = password)

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ", db_info)  

for report in files:
    # Opening the report and getting the drag and downforce values
    # Ex: lines[5] = "airfoil                   (13.989227 -33.100513 0)                      (0.044925034 -0.03932257 0)                   (14.034152 -33.139836 0) "
    with open(f'{directory}/{report}', "r") as f:
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
    con.cursor().execute("INSERT INTO ansys (nome, dia, downforce, drag, link, position, setups, setupRatio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (report, date, downforce, drag, link, "position", "setups", "setupRatio"))
    con.commit()

# Name of the directory containing the wing points
directory = "Reports/Rear"
position = "Rear"

# List all the files in the directory
files = os.listdir(directory)

# Iterate over each file in the directory
for points in files:
    # Check if the file has a .txt extension
    if points.endswith(".txt"):
        # Extract the report number from the file name
        report_number = "Report-" + points.split(".t")[0] + ".txt"
        
        # Query the database to check if the report exists
        query = f"SELECT * FROM ansys WHERE nome = '{report_number}'"
        cursor = con.cursor()
        cursor.execute(query)

        # Clear any unread result sets
        row = cursor.fetchall()
        
        # If the report exists, update the database with the new information
        if row:
            with open(os.path.join(directory, points), "r") as f:
                lines = list(reversed(f.readlines(-1)))
                count = i = 0
                aux = True
                var = True
                while aux:
                    i = 0
                    setups = ""
                    auxiliar = True
                    while auxiliar: 
                        character = lines[count][0]
                        if character == "*":
                            #Getting the last line which will be updated in the setupRatio column
                            if count == 0:
                                setupRatio = ""
                                i = 1
                                while lines[count][i+24] != "*":
                                    setupRatio += lines[count][i+24]
                                    i += 1
                                count += 1
                                break
                            #Getting the next lines which will be updated in the setup column
                            if count !=0:
                                while "*.*.Setup:" in lines[count]:
                                    if lines[count][i+11] == "*":
                                        setups += "\n"
                                        count += 1
                                        i = 0
                                        break                              
                                    else:
                                        setups += lines[count][i+11]
                                        i += 1
                        else:
                            auxiliar = False
                    if character != "*":
                        aux = False
                # Update the database with the new information
                sql = f"UPDATE ansys SET position='{position}', setupRatio='{setupRatio}', setups='{setups}' WHERE nome = '{report_number}'"
                cursor.execute(sql)
                con.commit()
                
            f.close()
        else:
            # Open the file in append mode
            with open("Reports\{position}_sem_Report.txt", "a") as file:
                # Write the string to the file
                file.write(report_number + "\n")

print("The end")