from __future__ import print_function

import datetime
import random

import cx_Oracle

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
dsn = cx_Oracle.makedsn("localhost", 32799, sid="ORCLCDB")
connection = cx_Oracle.connect("ordms", "ordms", dsn, encoding="UTF-8")
countryType = connection.gettype("COUNTRY_OBJTYP")
agentType = connection.gettype("AGENT_OBJTYP")
passengerType = connection.gettype("PASSENGER_OBJTYP")

destType = connection.gettype("FLIGHTDESTINATION_OBJTYP")
destArrayType = connection.gettype("FLIGHTDESTINATION_ARRAY")

cursor = connection.cursor()

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
    if type == "COUNTRY_OBJTYP":
        country = countryType.newobject()
        country.COUNTRY_NAME = column+str(i)
        country.POPULATION = 1000 * i
        return country
    if type == "AGENT_OBJTYP":
        agent = agentType.newobject()
        agent.LICENSE_NUM = 1000 * i
        agent.MEMBERSHIP_NUM = 2000 * i
        country = countryType.newobject()
        country.COUNTRY_NAME = "country"+str(i)
        country.POPULATION = 3000 * i
        agent.COUNTRY = country
        return agent
    if type == "PASSENGER_OBJTYP":
        passenger = passengerType.newobject()
        passenger.PASSPORT_NUM = 1000 * i
        passenger.DATE_OF_EXPIRY = datetime.datetime.now() + datetime.timedelta(hours=i)
        country = countryType.newobject()
        country.COUNTRY_NAME = "country"+str(i)
        country.POPULATION = 3000 * i
        passenger.COUNTRY = country
        return passenger
    if type == "FLIGHTDESTINATION_ARRAY":
        dests = destArrayType.newobject()
        dest1 = destType.newobject()
        dest1.AIRPORT_ID_DEST = i
        dest1.ARRIVAL_TIME = datetime.datetime.now() + datetime.timedelta(hours=i)
        dests.append(dest1)
        return dests



tabs = ['Airline', 'Aeroplane', 'Airport', 'Flight',
        'Seat', 'PNR', 'Ticket', 'BoardingPass', 'PNRSSR', 'Distance']

counter = 21


for tab in tabs:
    print("Generating fake data for table:", tab)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT column_name, data_type
        FROM user_tab_cols where table_name = upper(:t)
        """, [tab])

    cols = []
    types = []
    sql = "("
    col_names = "("
    count = 1
    for column_name, data_type in cursor:
        print(column_name + ' '+ data_type)
        if column_name[0:3] == "SYS":
            continue
        cols.append(column_name)
        types.append(data_type)

        if count > 1:
            sql += ","
            col_names += ","
        sql += ":"+ str(count)
        col_names += column_name
        count +=1
    sql += ")"
    col_names += ")"

    dataToInsert = []
    for i in range(1, counter):
        data = []
        for indx, col in enumerate(cols):
            print(col)
            data.append(gen_data(col, types[indx], i))
        dataToInsert.append(tuple(data))

    generated_sql = "insert into "+tab+" "+ col_names + " values"+ sql
    print(generated_sql)
    cursor.executemany(generated_sql, dataToInsert)

connection.commit()
cursor.close()
