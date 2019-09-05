from __future__ import print_function

import cx_Oracle

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
dsn = cx_Oracle.makedsn("localhost", 32799, sid="ORCLCDB")
connection = cx_Oracle.connect("ajoy", "ajoy", dsn, encoding="UTF-8")

cursor = connection.cursor()
cursor.execute("""
    SELECT *
    FROM Airline
    """)
for id, name, _ in cursor:
    print("Values:", id, name)


