import axios from 'axios'

const api = axios.create({
    baseURL: 'http://159.31.65.235:3000/api',
})

export const insertOBD = payload => api.post(`/obd`, payload)
export const getAllOBDs = () => api.get(`/obds`)
export const updateOBDById = (id, payload) => api.put(`/obd/${id}`, payload)
export const deleteOBDById = id => api.delete(`/obd/${id}`)
export const getOBDById = id => api.get(`/obd/${id}`)


export const insertTrip = payload => api.post(`/trip`, payload)
export const getAllTrips = () => api.get(`/trips`)
export const updateTripById = (id, payload) => api.put(`/trip/${id}`, payload)
export const deleteTripById = id => api.delete(`/trip/${id}`)
export const getTripById = id => api.get(`/trip/${id}`)

const apis = {
    insertOBD,
    getAllOBDs,
    updateOBDById,
    deleteOBDById,
    getOBDById,
    insertTrip,
    getAllTrips,
    updateTripById,
    deleteTripById,
    getTripById,
}

export default apis