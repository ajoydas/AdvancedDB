from __future__ import print_function

import cx_Oracle

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
dsn = cx_Oracle.makedsn("localhost", 32799, sid="ORCLCDB")
connection = cx_Oracle.connect("rdms", "rdms", dsn, encoding="UTF-8")

cursor = connection.cursor()
cursor.execute("""
    SELECT *
    FROM Airline
    """)
for id, name, _ in cursor:
    print("Values:", id, name)


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

