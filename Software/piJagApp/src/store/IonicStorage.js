import { Storage, Drivers } from "@ionic/storage";

var storage = false;

export const createStore = (name = "__mydb") => {

    storage = new Storage({
        
        name,
        driverOrder: [Drivers.IndexedDB, Drivers.LocalStorage]
    });

    storage.create();
}


export const set = (key, val) => {

    storage.set(key, val);
}

export const get = async key => {

    const val = await storage.get(key);
    return val;
}

export const remove = async key => {

    await storage.remove(key);
}

export const clear = async () => {

    await storage.clear();
}

export const setObject = async (key, index, val) => {

    const all = await storage.get(key);
    const objIndex = await all.findIndex(a => parseInt(a.index) === parseInt(index));

    all[objIndex] = val;
    set(key, all);
}

export const addObject = async (key, val) => {

    const all = await storage.get(key);

    set(key, [...all,val]);
}

export const removeObject = async (key, index) => {

    const all = await storage.get(key);
    const objIndex = await all.findIndex(a => parseInt(a.index) === parseInt(index));

    all.splice(objIndex, 1);
    set(key, all);
}

export const getObject = async (key, index) => {

    const all = await storage.get(key);
    const obj = await all.filter(a => parseInt(a.index) === parseInt(index))[0];
    return obj;
}