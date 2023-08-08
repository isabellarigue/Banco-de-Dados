# Aerodynamics Database 

For portuguese version click [here](Others/README-pt.md).

This is a database that is actually being used. That way, to make the repository public I created a copy of the database and put it on a server just for testing. So, it is possible to see and use the application, but with fictitious data.

## What is it?

A Database is basically a place where we centralize data, inside tables. With this, it is much easier and faster to access information.

So, this project proposes the creation of a database for the Aerodynamics division of the Unicamp E-Racing team, in order to store the data from simulations and tests, in an effective and centralized way. Seeking to facilitate the interaction with MySQL (chosen database), a graphical interface was also created in Python, which acts as an intermediary between the user and the server, so that it is more intuitive to add and change data in the software, export spreadsheets and view histograms.

## How to use?

It can be used in application format by downloading the executable. In that case you won't need MySQL, Python or any other library. If you are using a Windows system, you can use the [installer](https://drive.google.com/file/d/1qlQoe134umh2fFCPD2QyyyIHBFntRI25/view?usp=sharing) to get the app. Another option is to download the [build folder](build), available here in this repository, note that this mode tends to take a little longer. Once downloaded, change the password.txt file (located in the Others folder) by typing the password in the space indicated, then you can open the app_script.exe. The interface tends to be intuitive, no prior knowledge is needed, so just read the commands and warnings shown on the screen. 

Furthermore, it is possible to run the code directly to access the application. In this case, you must have Python installed, in addition to some libraries, they are:

### Required Libraries

- tkinter
- mysql-connector
- sys
- os
- pandas
- matplotlib
- numpy
- datetime

## Which tables are available?

At the moment the tables available to store data are:

- STAR-CCM+ simulations
- Ansys simulations
- Denso wind tunnel tests
- Coastdown tests

There are some other tables created for other possible tests, but they are not fully implemented.

## Default values

In the [values.csv](Others/values.csv) file there are some default values ​​to facilitate the insertion of new data. These automatically appear in the interface, in the corresponding places. If you want to change some of these values, just modify it in the csv itself and save it, but remember to be careful with the formatting.

## Ansys code

When we run a simulation on Ansys, .txt files are generated for the report and the airfoil points. To facilitate the insertion of this data into the database, the code [ansys.py](ansys.py) was created to automate this process. Note that it is necessary to indicate the correct directories in the code for it to work. 

## Some comments

- The server used is PlanetScale;
- A daily backup of the database is made, but even so, care must be taken when handling it, especially when deleting files!;
- Internet is needed to connect to the server, so there is also an offline mode that only works locally;
- For the table of tests in the wind tunnel, correction calculations are made for the value of the measured coefficients, since there is a deformation of the flow lines confined inside a tunnel;
- Be careful with the unit of measurement and formatting;
- Be careful with the password, do not leave it exposed, as it gives full access to the database!

## Common mistakes

Be careful when typing the password in the password.txt file, make sure that there is no invisible space after or before the text, otherwise it may give an error. Another important point is that if the .py code is running directly, it is necessary to install the mysql-connector library with the command "pip install mysql-connector-python", written that way. Finally, remember to run the executable as an administrator, to avoid any permission issues on the directories!
