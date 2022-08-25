import pyodbc
server='HYDTRNG9\SQLEXPRESS'
database='siva'
username='sa'
password='admin@23'
cxcn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


mycursor=cxcn.cursor()
res=mycursor.execute("select * from emp")
myrecs=res.fetchall();
print(myrecs)