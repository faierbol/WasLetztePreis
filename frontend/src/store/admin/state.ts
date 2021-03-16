import {IAdvert, IUserProfile} from '@/interfaces';

export interface AdminState {
    users: IUserProfile[];
    adverts: IAdvert[];
}
