import axios from 'axios';
import { INewsItem } from '../models';
import { EnvManager } from '../config';

export const getNewsByComments = async (): Promise<INewsItem[]> => {
    try {
        const response = await axios.get<INewsItem[]>(`${EnvManager.BACKEND_URL}/news/comments`);
        const data: INewsItem[] = response.data;
        return data
    } catch {
        throw new Error('Error fetching news');
    }
}

export const getNewsByPoints = async (): Promise<INewsItem[]> => {
    try {
        const response = await axios.get<INewsItem[]>(`${EnvManager.BACKEND_URL}/news/points`);
        const data: INewsItem[] = response.data;
        return data
    } catch {
        throw new Error('Error fetching news');
    }
}
