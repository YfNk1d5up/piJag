const express = require('express')

const obdCtrl = require('../controllers/obdJag-ctrl')
const tripCtrl = require('../controllers/tripJag-ctrl')

const router = express.Router()

router.post('/obd', obdCtrl.createOBD)
router.put('/obd/:id', obdCtrl.updateOBD)
router.delete('/obd/:id', obdCtrl.deleteOBD)
router.get('/obd/:id', obdCtrl.getOBDById)
router.get('/obds', obdCtrl.getOBDs)

router.post('/trip', tripCtrl.createTrip)
router.put('/trip/:id', tripCtrl.updateTrip)
router.delete('/trip/:id', tripCtrl.deleteTrip)
router.get('/trip/:id', tripCtrl.getTripById)
router.get('/trips', tripCtrl.getTrips)


module.exports = router
