import pyodbc
server = 'alexasql.database.windows.net'
database = 'AdventureWorks2016'
username = 'cmps253'
password = 'Cmps205!'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT top 10 * from Person.Person")
row = cursor.fetchone()

while row:
   print(row[0]," "+row[4])
   row = cursor.fetchone()
x=input("please enter a name: ")
cursor.execute("select * from Person.Person where firstname= \'" + x + "\'")
y=cursor.fetchone()
print(y)
y=cursor.fetchone()
