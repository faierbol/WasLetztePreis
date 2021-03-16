export interface IUserProfile {
    email: string;
    is_active: boolean;
    is_superuser: boolean;
    full_name: string;
    id: number;
}

export interface IUserProfileUpdate {
    email?: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IUserProfileCreate {
    email: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IAdvert {
    title: string;
    description: string;
    price: number;
    location: string;
    category: string;
    inactive: boolean;
    rating: number;
    image_link: string;
    owner_id: number;
    id: number;
}

export interface IAdvertUpdate {
    title?: string;
    description?: string;
    price?: number;
    location?: string;
    category?: string;
    inactive?: boolean;
    rating?: number;
    image_link?: string;
}

export interface IAdvertCreate {
    title: string;
    description?: string;
    price: number;
    location?: string;
    category?: string;
    inactive?: boolean;
    rating?: number;
    image_link?: string;
}
