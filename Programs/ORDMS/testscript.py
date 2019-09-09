from __future__ import print_function

import datetime

import cx_Oracle

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.

dsn = cx_Oracle.makedsn("localhost", 32799, sid="ORCLCDB")
connection = cx_Oracle.connect("ordms", "ordms", dsn, encoding="UTF-8")

cursor = connection.cursor()
cursor.execute("""
    SELECT *
    FROM Airport
    """)
for id, name, type, run, country in cursor:
    print("Values:", id, name, type, country)


from cx_Oracle import ObjectType
agentType = connection.gettype("AGENT_OBJTYP")
countryType = connection.gettype("COUNTRY_OBJTYP")
passengerType = connection.gettype("PASSENGER_OBJTYP")

print(agentType.attributes)
agent = agentType.newobject()
agent.LICENSE_NUM = 1000
agent.MEMBERSHIP_NUM = 2000
country = countryType.newobject()
country.COUNTRY_NAME = "bd"
country.POPULATION = 5000
agent.COUNTRY = country
cursor = connection.cursor()
cursor.execute("insert into Airport (COUNTRY, AIRPORT_ID, AIRPORT_NAME, AIRPORT_TYPE, NUM_OF_RUNWAYS) values (:i, :j, :k, :l, :m)", [country, 3, "name2", "type2", 3])
cursor.close()


print(passengerType.attributes)
passenger = passengerType.newobject()
passenger.PASSPORT_NUM = 1000
passenger.DATE_OF_EXPIRY = datetime.datetime.now()
country = countryType.newobject()
country.COUNTRY_NAME = "bd"
country.POPULATION = 5000
passenger.COUNTRY = country
cursor = connection.cursor()
cursor.execute("insert into PNR values (:i, :j, :k, :l)", [1, "name1", "contact1", passenger])
cursor.close()


from cx_Oracle import ObjectType
cursor = connection.cursor()
print(countryType.attributes)
country = countryType.newobject()
# country.setelement("country_name", "name2")
# country.setelement("population", 2000)
country.COUNTRY_NAME = "name2"
country.POPULATION = 3000
cursor.execute("insert into Airport (COUNTRY, AIRPORT_ID, AIRPORT_NAME, AIRPORT_TYPE, NUM_OF_RUNWAYS) values (:i, :j, :k, :l, :m)", [country, 3, "name2", "type2", 3])
cursor.close()


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



