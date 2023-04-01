const data_fields = Object.keys(db.data.findOne())
let data_fields_query = data_fields.reduce((prev, cursor, idx, array) => {
  prev[cursor] = 1
  return prev
}, {});

const Catamarans_fields = Object.keys(db.Catamarans.findOne())
let Catamarans_fields_query = Catamarans_fields.reduce((prev, cursor, idx, array) => {
  prev[`${cursor}`] = 1
  return prev
}, {});

db.Catamarans.aggregate([
  {
    $lookup: {
      from: "data",
      let: { make: "$Make", variant: "$Variant" },
      pipeline: [
        {
          $match: {
            $expr: {
              $and: [
                { $eq: ["$make", "$$make"] },
                { $eq: ["$model", "$$variant"] }
              ]
            }
          }
        },
        {
          $project: {
            _id: 0,
            ...data_fields_query
          }
        }
      ],
      as: "joined_data"
    }
  },
  {
    $project: {
      ...Catamarans_fields_query,
      joined_data: { $arrayElemAt: ["$joined_data", 0] }
    }
  },
//  {
//    $unwind: "$joined_data"
//  },
  {
    $replaceRoot: {
      newRoot: { $mergeObjects: ["$joined_data", "$$ROOT"] }
    }
  },
  {
    $project: {
      "joined_data": 0
    }
  }
])



const Monohulled_fields = Object.keys(db.Monohulled.findOne())
let Monohulled_fields_query = Monohulled_fields.reduce((prev, cursor, idx, array) => {
  prev[`${cursor}`] = 1
  return prev
}, {});

db.Monohulled.aggregate([
  {
    $lookup: {
      from: "data",
      let: { make: "$Make", variant: "$Variant" },
      pipeline: [
        {
          $match: {
            $expr: {
              $and: [
                { $eq: ["$make", "$$make"] },
                { $eq: ["$model", "$$variant"] }
              ]
            }
          }
        },
        {
          $project: {
            _id: 0,
            ...data_fields_query
          }
        }
      ],
      as: "joined_data"
    }
  },
  {
    $project: {
      ...Monohulled_fields_query,
      joined_data: { $arrayElemAt: ["$joined_data", 0] }
    }
  },
//  {
//    $unwind: "$joined_data"
//  },
  {
    $replaceRoot: {
      newRoot: { $mergeObjects: ["$joined_data", "$$ROOT"] }
    }
  },
  {
    $project: {
      "joined_data": 0
    }
  }
])
