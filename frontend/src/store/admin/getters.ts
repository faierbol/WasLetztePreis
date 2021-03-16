import { AdminState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const getters = {
    adminUsers: (state: AdminState) => state.users,
    adminOneUser: (state: AdminState) => (userId: number) => {
        const filteredUsers = state.users.filter((user) => user.id === userId);
        console.log(filteredUsers);
        if (filteredUsers.length > 0) {
            return { ...filteredUsers[0] };
        }
    },
    adminAdverts: (state: AdminState) => state.adverts,
    adminOneAdvert: (state: AdminState) => (advertId: number) => {
        const filteredAdverts = state.adverts.filter((advert) => advert.id === advertId);
        if (filteredAdverts.length > 0) {
            return { ...filteredAdverts[0] };
        }
    },
};

const { read } = getStoreAccessors<AdminState, State>('');

export const readAdminOneUser = read(getters.adminOneUser);
export const readAdminUsers = read(getters.adminUsers);

export const readAdminAdverts = read(getters.adminAdverts);
export const readAdminOneAdvert = read(getters.adminOneAdvert);
