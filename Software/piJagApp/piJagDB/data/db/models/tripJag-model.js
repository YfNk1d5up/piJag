const mongoose = require('mongoose')
const Schema = mongoose.Schema

const tripJag = new Schema(
    {
        name: { type: String, required: true },
        start: { type: Date, default: Date.now },
        end: {type: Date},
        obds: [
            {
              obdId: {
                type: mongoose.Schema.Types.ObjectId,
                ref: "obd",
              },
              data: {type : Array},
            },
          ],
    },
    { timestamps: true },
)

module.exports = mongoose.model('trip', tripJag)
