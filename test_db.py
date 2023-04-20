import mysql.connector
import time


db = mysql.connector.connect(
    host="127.0.0.1",
    user="maczo420all",
    passwd="Pomidor13",
    database="metryka",
)

mycursor = db.cursor()

mycursor.execute('SELECT * FROM woda ORDER BY id DESC, value DESC LIMIT 2')


"""    for ziom in mycursor:
        tup = ziom
        value = tup[1]
        print(value)"""


def send_to_ts():
    for ziom in mycursor:
        tup = ziom
        value = tup[1]
        values.append(value)

