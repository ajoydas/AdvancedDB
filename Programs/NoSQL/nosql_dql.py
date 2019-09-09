import datetime
import pymongo
from faker import Faker

fake = Faker()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["advancedDB"]
mycol = mydb["advancedDB"]

# print(mycol)

"""
========================================================================================================
                                            Buying ticket online 
                   @pnr
                   @passenger info
                   @ticket info
                   @flight info
                   @airport info
                   @agent info                         
========================================================================================================
"""

passenger_info = {
    "passport_number": fake.uuid4(),
    "country": {
        "name": fake.country(),
        "population": fake.random_int(0, 1000000000)
    },
    "date_of_expiry": fake.date(pattern="%Y-%m-%d", end_datetime=None)
}

pnr = {
    "name": fake.name(),
    "contact_information": fake.address(),
    "passenger": passenger_info
}

airline = {
    "name": fake.sentence(),
    "type": "Asd-1-3"
}

aeroplane = {
    "model": fake.sentence(),
    "capacity": fake.random_int(0, 2500),
    "airline": airline
}

seat = {
    "seat_no": fake.random_int(1, 200),
    "type": "A",
    "price": fake.random_int(500, 2000),
    "isSold": "true"
}

airport_country = {
    "name": fake.country(),
    "population": fake.random_int(500, 20000000)
}

airport = {
    "name": fake.name(),
    "type": "adsasdqwe",
    "num_of_runways": fake.random_int(1, 15),
    "country": airport_country
}

flight = {
    "flight_number": fake.uuid4(),
    "seat": seat,
    "aeroplane": aeroplane,
    "departure_date": fake.date(pattern="%Y-%m-%d", end_datetime=None),
    "departure_time": fake.date_time(tzinfo=None, end_datetime=None),
    "gate_number": fake.random_int(1, 15),
    "airport": airport
}

airport_id_as_source = airport

airport_id_as_dest = {
    "name": fake.name(),
    "type": "qwpoqipq",
    "num_of_runways": fake.random_int(1, 15),
    "country": {
        "name": fake.country(),
        "population": fake.random_int(0, 1000000000)
    }
}

data = {
    "boarding_pass": {
        "ticket": {
            "pnr": pnr,
            "flight": flight
        }
    },
    "distance": {
        "airport_id_as_source": airport_id_as_source,
        "airport_id_as_dest": airport_id_as_dest,
        "distance": fake.random_int(500, 150000)
    }
}

x = mycol.insert_one(data)

print(x)
