from __future__ import print_function

import datetime
import random

import cx_Oracle
from faker import Faker

fake = Faker()

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
dsn = cx_Oracle.makedsn("localhost", 32799, sid="ORCLCDB")
connection = cx_Oracle.connect("rdms", "rdms", dsn, encoding="UTF-8")
cursor = connection.cursor()

def gen_data(column, type, i):
    if column == "ISSOLD":
        return int(random.getrandbits(1))
    if column == "GATE_NUM":
        return fake.random_int(0, 10)
    if type == "NUMBER":
        return i
    if type == "VARCHAR2":
        return column+str(i)
    if type == "DATE":
        return datetime.datetime.now() + datetime.timedelta(hours=i)
    if type == "TIMESTAMP":
        return datetime.datetime.now() + datetime.timedelta(hours=i)


tabs = ['Airline', 'Aeroplane', 'Country', 'Airport', 'Flight', 'Passenger',
        'Seat', 'Agent', 'Ticket', 'BoardingPass', 'PNR', 'FlightDestination', 'PNRSSR', 'Distance']

counter = 10000
start = datetime.datetime.now()

for tab in tabs:
    print("Generating fake data for table:", tab)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT column_name, data_type
        FROM user_tab_cols where table_name = upper(:t)
        """, [tab])

    cols = []
    types = []
    sql = "insert into "+tab+" values ("
    count = 1
    for column_name, data_type in cursor:
        print(column_name + ' '+ data_type)
        cols.append(column_name)
        types.append(data_type)

        if count > 1:
            sql += ","
        sql += ":"+ str(count)
        count +=1
    sql += ")"

    dataToInsert = []
    for i in range(1, counter):
        data = []
        for indx, col in enumerate(cols):
            data.append(gen_data(col, types[indx], i))

        dataToInsert.append(tuple(data))

    print(sql)
    cursor.executemany(sql, dataToInsert)

connection.commit()
cursor.close()

end = datetime.datetime.now()
print("Took: "+ str((end-start).microseconds/1000)+" mili sec")