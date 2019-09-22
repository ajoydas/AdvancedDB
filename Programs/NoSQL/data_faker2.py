import datetime
import pymongo
from bson import ObjectId
from faker import Faker

fake = Faker()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["advancedDB"]
country_col = mydb["country"]
flight_col = mydb["flight"]
ticket_col = mydb["ticket"]
airline_col = mydb["airline"]

country_col.delete_many({})
airline_col.delete_many({})
flight_col.delete_many({})
ticket_col.delete_many({})


count = 20
countries = []
for i in range(0, count):
    airports = []
    for j in range(0, count//2):
        airport = {
            "_id": ObjectId(),
            "name": fake.name(),
            "type": "adsasdqwe",
            "num_of_runways": fake.random_int(1, 15),
        }
        airports.append(airport)

    agents = []
    for j in range(0, count//2):
        agent = {
            "_id": ObjectId(),
            "license_num": fake.random_int(0, 2500),
            "membership_num": fake.random_int(0, 2500)
        }
        agents.append(agent)

    passengers = []
    for j in range(0, count//2):
        passenger = {
            "_id": ObjectId(),
            "passport_number": fake.uuid4(),
            "date_of_expiry": fake.date(pattern="%Y-%m-%d", end_datetime=None)
        }
        passengers.append(passenger)

    country = {
        "_id": ObjectId(),
        "name": fake.country(),
        "population": fake.random_int(0, 1000000000),
        "airports": airports,
        "agents": agents,
        "passengers" : passengers
    }

    countries.append(country)
x = country_col.insert_many(countries)
print(x)


airlines = []
flights = []
tickets = []
for i in range(1, count):
    aeroplanes = []
    for j in range(0, count // 2):
        aeroplane = {
            "_id": ObjectId(),
            "model": fake.sentence(),
            "capacity": fake.random_int(0, 2500),
        }
        aeroplanes.append(aeroplane)

        for k in range(0, count // 4):
            seats = []
            for l in range(0, count // 4):
                seat = {
                    "_id": ObjectId(),
                    "type": "A",
                    "price": fake.random_int(500, 2000),
                    # "ticket": ticket if fake.random_int(0, 1) else None
                }
                seats.append(seat)

                pnrssrs = []
                for n in range(fake.random_int(0, count//4)):
                    pnrssr =  {
                        "_id": ObjectId(),
                        "service": fake.name()
                    }
                    pnrssrs.append(pnrssr)

                pnr = {
                    "_id": ObjectId(),
                    "name": fake.name(),
                    "contact_information": fake.address(),
                    "passenger_id": countries[fake.random_int(0, count-1)]["passengers"][fake.random_int(0, count//2-1)]["_id"],
                    "services" : pnrssrs
                }

                boarding_pass = {
                    "_id": ObjectId(),
                    "issue_time": fake.date_time(tzinfo=None, end_datetime=None),
                }

                if fake.random_int(0, 1) :
                    ticket = {
                        "_id": ObjectId(),
                        "seat_id": seat["_id"],
                        "pnr": pnr,
                        "agent_id": countries[fake.random_int(0, count-1)]["agents"][fake.random_int(0, count//2-1)]["_id"],
                        "boarding_pass": boarding_pass if fake.random_int(0, 1) else None
                    }
                    seat["issued"] = True
                    tickets.append(ticket)
                else:
                    seat["issued"] = False

            flight = {
                "_id": ObjectId(),
                "aeroplane_id": aeroplane["_id"],
                "departure_date": fake.date(pattern="%Y-%m-%d", end_datetime=None),
                "departure_time": fake.date_time(tzinfo=None, end_datetime=None),
                "gate_number": fake.random_int(1, 15),
                "airport_id_as_source": countries[fake.random_int(0, count-1)]["airports"][fake.random_int(0, count//2-1)]["_id"],
                "airport_id_as_dest": countries[fake.random_int(0, count-1)]["airports"][fake.random_int(0, count//2-1)]["_id"],
                "arrival_date": fake.date(pattern="%Y-%m-%d", end_datetime=None),
                "arrival_time": fake.date_time(tzinfo=None, end_datetime=None),
                "seats": seats
            }
            flights.append(flight)


    airline = {
        "_id": ObjectId(),
        "name": fake.sentence(),
        "type": "Asd-1-3",
        "aeroplanes": aeroplanes
    }

    airlines.append(airline)


x = airline_col.insert_many(airlines)
print(x)
x = flight_col.insert_many(flights)
print(x)
x = ticket_col.insert_many(tickets)
print(x)
