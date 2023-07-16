import { Store } from "pullstate";
import { get, getObject, set, setObject, addObject } from './IonicStorage';

const ParamStore = new Store({
    
    ip: "",
    port: "",
    password: ""
});

export default ParamStore;

export const changePassword = (pwd) => {

    ParamStore.update(s => {
        set("pwd", pwd);
        s.password = pwd;
    });
}
export const changeIp = (ip) => {

    ParamStore.update(s => {
        set("ip", ip);
        s.ip = ip;
    });
}
export const changePort = (port) => {

    ParamStore.update(s => {
        set("port", port);
        s.port = port;
    });
}
