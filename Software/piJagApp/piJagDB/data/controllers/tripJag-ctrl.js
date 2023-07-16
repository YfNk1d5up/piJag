const tripJag = require('../db/models/tripJag-model')

createTrip = (req, res) => {
    const body = req.body

    if (!body) {
        return res.status(400).json({
            success: false,
            error: 'You must provide an trip',
        })
    }

    const trip = new tripJag(body)

    if (!trip) {
        return res.status(400).json({ success: false, error: err })
    }

    trip
        .save()
        .then(() => {
            return res.status(201).json({
                success: true,
                id: trip._id,
                message: 'trip created!',
            })
        })
        .catch(error => {
            return res.status(400).json({
                error,
                message: 'trip not created!',
            })
        })
}

updateTrip = async (req, res) => {
    const body = req.body

    if (!body) {
        return res.status(400).json({
            success: false,
            error: 'You must provide a body to update',
        })
    }

    tripJag.findOne({ _id: req.params.id }, (err, trip) => {
        if (err) {
            return res.status(404).json({
                err,
                message: 'trip not found!',
            })
        }
        trip.name = body.name
        trip.start = body.start
        trip.end = body.end
        trip.obds = body.obds
        trip
            .save()
            .then(() => {
                return res.status(200).json({
                    success: true,
                    id: trip._id,
                    message: 'trip updated!',
                })
            })
            .catch(error => {
                return res.status(404).json({
                    error,
                    message: 'trip not updated!',
                })
            })
    })
}

deleteTrip = async (req, res) => {
    await tripJag.findOneAndDelete({ _id: req.params.id }, (err, trip) => {
        if (err) {
            return res.status(400).json({ success: false, error: err })
        }

        if (!trip) {
            return res
                .status(404)
                .json({ success: false, error: `trip not found` })
        }

        return res.status(200).json({ success: true, data: trip })
    }).catch(err => console.log(err))
}

getTripById = async (req, res) => {
    await tripJag.findOne({ _id: req.params.id }, (err, trip) => {
        if (err) {
            return res.status(400).json({ success: false, error: err })
        }

        if (!trip) {
            return res
                .status(404)
                .json({ success: false, error: `trip not found` })
        }
        return res.status(200).json({ success: true, data: trip })
    }).catch(err => console.log(err))
}

getTrips = async (req, res) => {
    await tripJag.find({}, (err, trip) => {
        if (err) {
            return res.status(400).json({ success: false, error: err })
        }
        if (!trip.length) {
            return res
                .status(404)
                .json({ success: false, error: `trip not found` })
        }
        return res.status(200).json({ success: true, data: trip })
    }).catch(err => console.log(err))
}

module.exports = {
    createTrip,
    updateTrip,
    deleteTrip,
    getTrips,
    getTripById,
}
