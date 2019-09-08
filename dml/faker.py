from __future__ import print_function

import datetime
import random

import cx_Oracle

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
dsn = cx_Oracle.makedsn("localhost", 32799, sid="ORCLCDB")
connection = cx_Oracle.connect("ajoy", "ajoy", dsn, encoding="UTF-8")
# connection.autocommit = True
dataToInsert = []

for i in range(1, 21):
    dataToInsert.append((i, "name" + str(i), "type" + str(i)))

cursor = connection.cursor()
# sql = ' ({}, \'{}\', \'{}\')'.format(i, 'name'+str(i), 'type'+str(i))
cursor.executemany("insert into AIRLINE values (:i, :j, :k)", dataToInsert)
cursor.close()

connection.commit()

cursor = connection.cursor()
cursor.execute("""
    SELECT *
    FROM Airline
    """)
for id, name, _ in cursor:
    print("Values:", id, name)

cursor = connection.cursor()
cursor.execute("""
    SELECT table_name, column_name, data_type
    FROM user_tab_cols;
    """)

def gen_data(column, type, i):
    if column == "ISSOLD":
        return int(random.getrandbits(1))
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
    for i in range(1, 21):
        data = []
        for indx, col in enumerate(cols):
            data.append(gen_data(col, types[indx], i))

        dataToInsert.append(tuple(data))

    print(sql)
    cursor.executemany(sql, dataToInsert)

connection.commit()
cursor.close()
