import { createSelector } from 'reselect';

const getState = state => state;

//  General getters
export const getIp = createSelector(getState, state => state.ip);
export const getPort = createSelector(getState, state => state.port);
export const getPassword = createSelector(getState, state => state.password);