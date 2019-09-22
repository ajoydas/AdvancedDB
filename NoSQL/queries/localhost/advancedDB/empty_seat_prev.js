db.airline.aggregate([
  {
    "$unwind": "$aeroplanes"
  },
  {
    "$unwind": "$aeroplanes.flights"
  },
  {
    "$unwind": "$aeroplanes.flights.seats"
  },
  {
    "$match": {
      "aeroplanes.flights.seats.ticket": null
    }
  },
  {
    "$project": {
      "aeroplanes": 1,
    }
  },
 
])