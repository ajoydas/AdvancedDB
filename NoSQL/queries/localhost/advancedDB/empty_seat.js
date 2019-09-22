// db.flight.aggregate([
//   {
//     "$unwind": "$seats"
//   },
//   {
//     "$match": {
//       "seats.issued": false
//     }
//   },
//   {
//     "$project": {
//       "seats": 1,
//     }
//   },
 
// ])


db.flight.aggregate([
  {
    $match: {
      "seats.issued": false
    }
  },
  {
    $project: {
      seats: {
        $filter: {
          input: "$seats",
          as: "seat",
          cond: {
            $eq: [
              "$$seat.issued",
              false
            ]
          }
        }
      }
    }
  }
])