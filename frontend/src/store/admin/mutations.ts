import {IAdvert, IUserProfile} from '@/interfaces';
import { AdminState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const mutations = {
    setUsers(state: AdminState, payload: IUserProfile[]) {
        state.users = payload;
    },
    setUser(state: AdminState, payload: IUserProfile) {
        const users = state.users.filter((user: IUserProfile) => user.id !== payload.id);
        users.push(payload);
        state.users = users;
    },
    setAdverts(state: AdminState, payload: IAdvert[]) {
        state.adverts = payload;
    },
    setAdvert(state: AdminState, payload: IAdvert) {
        const adverts = state.adverts.filter((advert: IAdvert) => advert.id !== payload.id);
        adverts.push(payload);
        state.adverts = adverts;
    },
};

const { commit } = getStoreAccessors<AdminState, State>('');

export const commitSetUser = commit(mutations.setUser);
export const commitSetUsers = commit(mutations.setUsers);
export const commitSetAdvert = commit(mutations.setAdvert);
export const commitSetAdverts = commit(mutations.setAdverts);
