const mongoose = require('mongoose')
const Schema = mongoose.Schema

const obdJag = new Schema(
    {
        name: { type: String, required: true },
        pid: { type: String, required: true },
        unit: { type: String, required: true },
        rate: { type: Number, required: true },
    },
    { timestamps: true },
)

module.exports = mongoose.model('obd', obdJag)
