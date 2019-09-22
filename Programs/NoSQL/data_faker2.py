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
distance_col = mydb["distance"]

country_col.delete_many({})
airline_col.delete_many({})
flight_col.delete_many({})
ticket_col.delete_many({})
distance_col.delete_many({})


count = 20
countries = []
airport_list = []
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
    airport_list.extend(airports)

x = country_col.insert_many(countries)
print(x)

# distance
distances = []
for i in range(len(airport_list)):
    for j in range(i+1, len(airport_list)):
        distance = {
            "airport1": airport_list[i]["_id"],
            "airport2": airport_list[j]["_id"],
            "distance": fake.random_int(0, 10000)
        }
        distances.append(distance)

x = distance_col.insert_many(distances)
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


            dests = []
            for n in range(fake.random_int(0, count//4)):
                dest = {
                    "airport_id": countries[fake.random_int(0, count-1)]["airports"][fake.random_int(0, count//2-1)]["_id"],
                    "arrival_time": fake.date_time(tzinfo=None, end_datetime=None),
                }
                dests.append(dest)

            flight = {
                "_id": ObjectId(),
                "aeroplane_id": aeroplane["_id"],
                "departure_time": fake.date_time(tzinfo=None, end_datetime=None),
                "gate_number": fake.random_int(1, 15),
                "airport_id_as_source": countries[fake.random_int(0, count-1)]["airports"][fake.random_int(0, count//2-1)]["_id"],
                "dests": dests,
                "seats": seats
            }
            flights.append(flight)


    airline = {
        "_id": ObjectId(),
        "name": fake.word(),
        "type": fake.word(),
        "aeroplanes": aeroplanes
    }

    airlines.append(airline)


x = airline_col.insert_many(airlines)
print(x)
x = flight_col.insert_many(flights)
print(x)
x = ticket_col.insert_many(tickets)
print(x)
