import mysql.connector



db = mysql.connector.connect(
    host="127.0.0.1",
    user="maczo420all",
    passwd="Pomidor13",
    database="metryka",
)

mycursor = db.cursor()

mycursor.execute('SELECT * FROM woda ORDER BY id DESC, value DESC LIMIT 2')

for ziom in mycursor:
    print(ziom)