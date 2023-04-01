const fields = Object.keys(db.data.findOne())
const query1 = {
    $project: {
        _id: 0,
//      field1: { $cond: [{ $eq: ["$field1", null] }, 1, 0] },
    },
}
const query2 = {
    $group: {
        _id: null,
        total_count: {$sum: 1},
//      field1_null_count: { $sum: "$field1" },
    }
}
const query3 = {
    $project: {
        _id: 0,
        total_count: 1,
//      field1_null_percent: { $multiply: [{ $divide: ["$field1_null_count", { $size: "$data" }] }, 100] },
    }
}

for (const field of fields) {
    if (field === '_id' || field === 'total_count') continue;
    query2.$group[`${field}_null_count`] = {$sum: {$cond: [{$eq: [`$${field}`, null]}, 1, 0]}}
    query3.$project[`${field}_null_percent`] = {$multiply: [{$divide: [`$${field}_null_count`, "$total_count"]}, 100]}
}


db.data.aggregate([
    query1,
    query2,
    query3,
])

/*
output：
[
  {
    "beam_null_percent": 1.632903621853898,
    "cabins_null_percent": 39.987722529158994,
    "classes_null_percent": 0.1841620626151013,
    "currentPrice_null_percent": 0,
    "engineFuelType_null_percent": 16.89379987722529,
    "engineHours_null_percent": 66.04051565377532,
    "engineMake_null_percent": 22.578268876611418,
    "engineModel_null_percent": 43.621853898096994,
    "engineType_null_percent": 32.16697360343769,
    "engineYear_null_percent": 54.499693063228975,
    "freshWaterTank_null_percent": 32.302025782688766,
    "fuelTank_null_percent": 30.20257826887661,
    "fuelTpe_null_percent": 1.1049723756906076,
    "heads_null_percent": 12.74401473296501,
    "holdingTank_null_percent": 65.6353591160221,
    "hullMaterial_null_percent": 0.1841620626151013,
    "hullShape_null_percent": 66.13873542050338,
    "lengthOverall_null_percent": 2.0380601596071206,
    "length_null_percent": 0.1841620626151013,
    "location_null_percent": 0.748925721301412,
    "make_null_percent": 0.1841620626151013,
    "maxBridgeClearance_null_percent": 87.03499079189687,
    "model_null_percent": 0.5279312461632903,
    "name_null_percent": 0,
    "singleBerths_null_percent": 70.81645181092695,
    "totalPower_null_percent": 29.048496009821978,
    "total_count": 8145,
    "url_null_percent": 0,
    "year_null_percent": 0.1841620626151013
  }
]
 */