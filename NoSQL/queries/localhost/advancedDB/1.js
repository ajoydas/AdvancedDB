// Buying ticket online 

// 5d87bc30d2ff9c3c914dcc4c

// db.flight.update({"seats._id": ObjectId("5d87bc30d2ff9c3c914dcc4c")}, 
//     {$set:{'seats.$.issued': true}}, 
//     { multi: false, upsert: false}
// )

// db.flight.find({"seats._id": Ob"5d87bc30d2ff9c3c914dcc56"})

db.flight.aggregate([
  {
    $match: {
      "seats._id": ObjectId("5d87bc30d2ff9c3c914dcc56")
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
              "$$seat._id",
              ObjectId("5d87bc30d2ff9c3c914dcc56")
            ]
          }
        }
      }
    }
  }
])