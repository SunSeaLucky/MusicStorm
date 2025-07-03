import axios from 'axios';
import type { AxiosResponse } from 'axios';

interface Post {
  id: string;
  user: {
    id: string;
    name: string;
    avatar: string;
  };
  content: string;
  time: string;
  tracks: Array<{
    id: string;
    name: string;
    artist: string;
    cover: string;
    url: string;
  }>;
  likes: number;
}

export const getCommunityPosts = async (): Promise<AxiosResponse<Post[]>> => {
  return axios.get('/community/posts');
};
