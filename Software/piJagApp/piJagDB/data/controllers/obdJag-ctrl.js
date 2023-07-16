const obdJag = require('../db/models/obdJag-model')

createOBD = (req, res) => {
    const body = req.body

    if (!body) {
        return res.status(400).json({
            success: false,
            error: 'You must provide an obd',
        })
    }

    const obd = new obdJag(body)

    if (!obd) {
        return res.status(400).json({ success: false, error: err })
    }

    obd
        .save()
        .then(() => {
            return res.status(201).json({
                success: true,
                id: obd._id,
                message: 'obd created!',
            })
        })
        .catch(error => {
            return res.status(400).json({
                error,
                message: 'obd not created!',
            })
        })
}

updateOBD = async (req, res) => {
    const body = req.body

    if (!body) {
        return res.status(400).json({
            success: false,
            error: 'You must provide a body to update',
        })
    }

    obdJag.findOne({ _id: req.params.id }, (err, obd) => {
        if (err) {
            return res.status(404).json({
                err,
                message: 'obd not found!',
            })
        }
        obd.name = body.name
        obd.pid = body.pid
        obd.rate = body.rate
        obd
            .save()
            .then(() => {
                return res.status(200).json({
                    success: true,
                    id: obd._id,
                    message: 'obd updated!',
                })
            })
            .catch(error => {
                return res.status(404).json({
                    error,
                    message: 'obd not updated!',
                })
            })
    })
}

deleteOBD = async (req, res) => {
    await obdJag.findOneAndDelete({ _id: req.params.id }, (err, obd) => {
        if (err) {
            return res.status(400).json({ success: false, error: err })
        }

        if (!obd) {
            return res
                .status(404)
                .json({ success: false, error: `obd not found` })
        }

        return res.status(200).json({ success: true, data: obd })
    }).catch(err => console.log(err))
}

getOBDById = async (req, res) => {
    await obdJag.findOne({ _id: req.params.id }, (err, obd) => {
        if (err) {
            return res.status(400).json({ success: false, error: err })
        }

        if (!obd) {
            return res
                .status(404)
                .json({ success: false, error: `obd not found` })
        }
        return res.status(200).json({ success: true, data: obd })
    }).catch(err => console.log(err))
}

getOBDs = async (req, res) => {
    await obdJag.find({}, (err, obd) => {
        if (err) {
            return res.status(400).json({ success: false, error: err })
        }
        if (!obd.length) {
            return res
                .status(404)
                .json({ success: false, error: `obd not found` })
        }
        return res.status(200).json({ success: true, data: obd })
    }).catch(err => console.log(err))
}

module.exports = {
    createOBD,
    updateOBD,
    deleteOBD,
    getOBDs,
    getOBDById,
}