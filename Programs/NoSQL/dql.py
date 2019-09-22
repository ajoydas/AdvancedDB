import datetime
import pymongo
from bson import ObjectId
from faker import Faker
import pprint

fake = Faker()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["advancedDB"]
country_col = mydb["country"]
flight_col = mydb["flight"]
ticket_col = mydb["ticket"]
airline_col = mydb["airline"]

countries = list(country_col.find())
"""
========================================================================================================
                                            Buying ticket online | Agent                      
========================================================================================================
"""
agent = True

"""
==================================================================================
                  Showing the available seats of a flight                 
==================================================================================
"""

# Find empty seats
flights = list(flight_col.aggregate([
  {
    "$match": {
      "seats.issued": False
    }
  },
  {
    "$project": {
      "seats": {
        "$filter": {
          "input": "$seats",
          "as": "seat",
          "cond": {
            "$eq": [
              "$$seat.issued",
              False
            ]
          }
        }
      }
    }
  }
]))

random_flight = flights[fake.random_int(0, len(flights)-1)]
random_seat = random_flight["seats"][fake.random_int(0, len(random_flight["seats"])-1)]
print("Updating seat with flight id: "+str(random_flight["_id"])+" seat id: "+str(random_seat["_id"]))

count = 20
pnrssrs = []
for n in range(fake.random_int(0, count // 4)):
    pnrssr = {
        "_id": ObjectId(),
        "service": fake.name()
    }
    pnrssrs.append(pnrssr)

pnr = {
    "_id": ObjectId(),
    "name": fake.name(),
    "contact_information": fake.address(),
    "passenger_id": countries[fake.random_int(0, count - 1)]["passengers"][fake.random_int(0, count // 2 - 1)]["_id"],
    "services": pnrssrs
}

boarding_pass = {
    "_id": ObjectId(),
}

if agent:
    ticket = {
        "_id": ObjectId(),
        "seat_id": random_seat["_id"],
        "pnr": pnr,
        "agent_id": countries[fake.random_int(0, count - 1)]["agents"][fake.random_int(0, count // 2 - 1)]["_id"],
        "boarding_pass": boarding_pass
    }
else:
    ticket = {
        "_id": ObjectId(),
        "seat_id": random_seat["_id"],
        "pnr": pnr,
        "agent_id": None,
        "boarding_pass": boarding_pass
    }

ticket_col.append(ticket)

# updating seat status
result = flight_col.update({"seats._id": random_seat["_id"]},
    {"$set":{"seats.$.issued": True}},
    multi= False, upsert= False
)

print(result)

"""
========================================================================================================
                                Issue boarding pass to passengers                 
========================================================================================================
"""
# Find empty boarding pass
tickets = list(ticket_col.find({"boarding_pass": None}))
pprint.pprint(tickets)

random_ticket = tickets[fake.random_int(0, len(tickets)-1)]
print("Issuing ticket for ticket id: "+ str(random_ticket["_id"]))
boarding_pass = {
    "_id": ObjectId(),
    "issue_time": fake.date_time(tzinfo=None, end_datetime=None),
}
result = ticket_col.update({"_id": random_ticket["_id"]},
    {"$set":{"boarding_pass": boarding_pass}},
    multi= False, upsert= False
)

print(result)
"""
========================================================================================================
                                Display the flight list and departure time                 
========================================================================================================
"""
flights = list(flight_col.find({},{"departure_time":1}))
pprint.pprint(flights)


"""
========================================================================================================
                                Display the flight list and arrival time                 
========================================================================================================
"""
flights = list(flight_col.find({},{"arrival_time":1}))
pprint.pprint(flights)


"""
========================================================================================================
                    List of on-board passengers of a flight of an airline in a date                 
========================================================================================================
"""
flight
