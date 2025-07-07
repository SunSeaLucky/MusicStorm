<template>
  <div class="community-container">
    <div class="community-header">
      <h1 class="page-title">社区</h1>
      <button class="create-post-btn" @click="showCreatePost = true">发帖</button>
    </div>
    
    <!-- 发帖模态框 -->
    <div v-if="showCreatePost" class="post-modal">
      <div class="modal-content">
        <span class="close" @click="showCreatePost = false">&times;</span>
        <h2>创建新帖子</h2>
        <textarea v-model="newPost.content" placeholder="分享你的想法..."></textarea>
        <div class="referenced-music" v-if="currentTrack">
          <div class="music-item">
            <img :src="currentTrack.cover" class="music-cover">
            <div class="music-info">
              <div class="music-name">{{ currentTrack.name }}</div>
              <div class="music-artist">{{ currentTrack.artists.name }}</div>
            </div>
            <button @click="clearTrack" class="clear-track-btn">×</button>
          </div>
        </div>
        <button @click="selectTrack" class="select-track-btn">选择音乐</button>
        <button class="submit-btn" @click="submitPost">发布</button>
      </div>
    </div>

    <div class="post-list">
      <div v-for="post in posts" :key="post.id" class="post-card">
        <div class="post-header">
          <img src="https://www.bing.com/th/id/OIP.uwWLUS0SeweiTbLzvWqYYQAAAA?w=210&h=211&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2" class="user-avatar">
          <div class="user-info">
            <span class="username">{{ post.user_name }}</span>
            <span class="post-time">{{ post.time }}</span>
          </div>
        </div>

        <div class="post-content">
          {{ post.content }}
        </div>

        <div class="referenced-music">
          <div class="music-item" @click="playTrack(post)">
            <img :src="post.track_cover" class="music-cover">
            <div class="music-info">
              <div class="music-name">{{ post.track_name }}</div>
              <div class="music-artist">{{ post.track_artist }}</div>
            </div>
          </div>
        </div>

        <div class="post-actions">
          <button class="action-btn"><i class="icon-like">♥</i> {{ post.likes }}</button>
          <button class="action-btn"><i class="icon-comment">💬</i> 评论</button>
          <button class="action-btn"><i class="icon-share">↗</i> 分享</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import player from '@/utils/player';
import { useMusicStore } from '@/stores/music';
import axios from 'axios';

interface Post {
  id: string;
  user_id: string;
  user_name: string;
  user_avatar: string;
  content: string;
  time: string;
  track_id: string | number;
  track_name: string;
  track_artist: string;
  track_cover: string;
  track_url: string;
  likes: string;
  url: string;
}

const posts = ref<Post[]>([]);
const showCreatePost = ref(false);
const newPost = ref({
  content: '',
  track_id: '',
  track_name: '',
  track_artist: '',
  track_cover: ''
});

const musicStore = useMusicStore();
const currentTrack = ref<any>(null);
const user = ref({
  id: localStorage.getItem('userId') || '100',
  name: localStorage.getItem('username') || '匿名用户',
  avatar: localStorage.getItem('avatar') || 'https://www.bing.com/th/id/OIP.uwWLUS0SeweiTbLzvWqYYQAAAA?w=210&h=211&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2'
});

const fetchPosts = async () => {
  try {
    const headers = {
      "Accept": "*/*",
      "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
      "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJuYW1lIjoidGVzdCJ9LCJleHAiOjE3NTE5ODIyODF9.KjqCbUYoZIc3pBaIHYDGivD_XaREnyqBEeIzh9LZAJA",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/x-www-form-urlencoded",
      "Origin": "http://localhost:5173",
      "Pragma": "no-cache",
      "Referer": "http://localhost:5173/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-site",
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
      "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
      "sec-ch-ua-mobile": "?0",
    };

    const params = {
      "username": "test"
    };

    const response = await axios.get("http://sunsealucky.cn:8080/post/findAllPosts", {
      headers,
      params
    });

    // 将API返回的数据转换为Post接口格式
    posts.value = response.data.map((item: any) => ({
      id: item.id,
      user_id: item.user_id,
      user_name: item.user_name,
      user_avatar: item.user_avatar,
      content: item.content,
      time: item.time,
      track_id: item.track_id,
      track_name: item.track_name,
      track_artist: item.track_artist,
      track_cover: item.track_cover,
      track_url: item.track_url,
      likes: item.likes
      // url: item.url
    }));
  } catch (error) {
    console.error('获取社区帖子失败:', error);
  }
};

onMounted(() => {
  fetchPosts();
});

const selectTrack = () => {
  console.log(currentTrack);
  // 暂时使用当前播放的音乐作为示例
  if (musicStore.playSong) {
    currentTrack.value = {
      id: musicStore.playSong.id,
      name: musicStore.playSong.name,
      artists: musicStore.playSong.artists,
      cover: musicStore.playSong.cover
    };
    newPost.value.track_id = currentTrack.value.id;
    newPost.value.track_name = currentTrack.value.name;
    newPost.value.track_artist = currentTrack.value.artists.name;
    newPost.value.track_cover = currentTrack.value.cover;
  }
};

const clearTrack = () => {
  currentTrack.value = null;
  newPost.value.track_id = '';
  newPost.value.track_name = '';
  newPost.value.track_artist = '';
  newPost.value.track_cover = '';
};

const submitPost = async () => {
  try {
    const headers = {
      "Accept": "*/*",
      "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
      "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJuYW1lIjoidGVzdCJ9LCJleHAiOjE3NTE5ODIyODF9.KjqCbUYoZIc3pBaIHYDGivD_XaREnyqBEeIzh9LZAJA",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Origin": "http://localhost:5173",
      "Pragma": "no-cache",
      "Referer": "http://localhost:5173/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-site",
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
      "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
      "sec-ch-ua-mobile": "?0",
    };

    const params = {
      id: Date.now(),
      user_id: user.value.id,
      user_name: user.value.name,
      user_avatar: user.value.avatar,
      content: newPost.value.content,
      time: new Date().toISOString(),
      tracks_id: newPost.value.track_id || undefined,
      tracks_name: newPost.value.track_name || undefined,
      tracks_artist: newPost.value.track_artist || undefined,
      likes: "0"
    };

    // 构建查询字符串，自动过滤undefined值
    const query = Object.entries(params)
      .filter(([_, v]) => v !== undefined)
      .map(([k, v]) => `${k}=${encodeURIComponent(v as string | number | boolean)}`)
      .join('&');

    await axios.get(`http://sunsealucky.cn:8080/post/addPost?${query}`, { headers });
    
    showCreatePost.value = false;
    newPost.value = {
      content: '',
      track_id: '',
      track_name: '',
      track_artist: '',
      track_cover: ''
    };
    currentTrack.value = null;
    
    // 刷新帖子列表
    fetchPosts();
    
    // 添加成功提示
    // alert('发帖成功！');
  } catch (error) {
    console.error('发帖失败:', error);
    // 添加失败提示
    // alert('发帖失败，请稍后重试');
  }
};

const playTrack = (post: Post) => {
  // 更新当前播放歌曲信息
  const musicStore = useMusicStore();
  musicStore.playSong = {
    id: Number(post.track_id), // 转换为number类型
    name: post.track_name,
    artists: post.track_artist,
    album: '未知专辑',
    cover: post.track_cover,
    duration: 0,
    free: 0,
    mv: null,
    type: "song",
  };

  // 调用播放器播放
  player.initPlayer(true);
};
</script>

<style scoped lang="scss">
.community-container {
  padding: 20px;
  color: #e0e0e0;
  min-height: 100vh;

  .community-header {
     display: flex;
     justify-content: space-between;
     align-items: center;
     margin-bottom: 20px;
  }
}

.page-title {
  font-size: 24px;
  margin-bottom: 20px;
  color: #ffffff;
}

.post-list {
  display: grid;
  gap: 20px;
}

.post-card {
  background-color: rgba(30, 30, 30, 0.2);
  border-radius: 10px;
  padding: 16px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}

.post-header {
  display: flex;
  align-items: center;
  margin-bottom: 12px;
}

.user-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 12px;
  object-fit: cover;
}

.user-info {
  display: flex;
  flex-direction: column;
}

.username {
  font-weight: bold;
  font-size: 16px;
}

.post-time {
  font-size: 12px;
  color: #b3b3b3;
}

.post-content {
  margin-bottom: 16px;
  line-height: 1.5;
}

.referenced-music {
  background-color: rgba(30, 30, 30, 0.4);
  border-radius: 8px;
  padding: 12px;
  margin-bottom: 16px;
}

.music-item {
  display: flex;
  align-items: center;
  padding: 8px;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s;

  &:hover {
    background-color: #333333;
  }
}

.music-cover {
  width: 48px;
  height: 48px;
  border-radius: 4px;
  margin-right: 12px;
}

.music-info {
  flex: 1;
}

.music-name {
  font-weight: 500;
  margin-bottom: 4px;
}

.music-artist {
  font-size: 14px;
  color: #b3b3b3;
}

.post-actions {
  display: flex;
  gap: 16px;
}

.create-post-btn {
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 8px 16px;
  border-radius: 20px;
  cursor: pointer;
  margin-bottom: 20px;
  font-weight: bold;
  transition: all 0.2s;

  &:hover {
    background-color: rgba(0, 0, 0, 0.7);
    border-color: rgba(255, 255, 255, 0.4);
  }
}

.select-track-btn {
  background-color: rgba(0, 0, 0, 0.3);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
  margin-bottom: 15px;
  transition: all 0.2s;

  &:hover {
    background-color: rgba(0, 0, 0, 0.5);
  }
}

.clear-track-btn {
  background: none;
  border: none;
  color: #b3b3b3;
  font-size: 20px;
  cursor: pointer;
  padding: 0 8px;
  margin-left: 10px;

  &:hover {
    color: white;
  }
}

.post-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: #282828;
  padding: 20px;
  border-radius: 10px;
  width: 500px;
  max-width: 90%;
}

.modal-content h2 {
  margin-bottom: 20px;
}

.modal-content textarea {
  width: 100%;
  height: 150px;
  padding: 10px;
  margin-bottom: 15px;
  background-color: #333;
  border: none;
  border-radius: 5px;
  color: white;
  resize: none;
}

.close {
  float: right;
  font-size: 24px;
  cursor: pointer;
}

.music-selector {
  background-color: rgba(30, 30, 30, 0.4);
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.submit-btn {
  background-color: rgba(113, 3, 123, 0.678);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  width: 100%;
  font-weight: bold;
  transition: background-color 0.2s;

  &:hover {
    background-color: #1ed760;
  }
}

.action-btn {
  background: none;
  border: none;
  color: #b3b3b3;
  display: flex;
  align-items: center;
  gap: 4px;
  cursor: pointer;
  font-size: 14px;
  padding: 4px 8px;
  border-radius: 4px;
  transition: color 0.2s, background-color 0.2s;

  &:hover {
    color: #ffffff;
    background-color: rgba(255, 255, 255, 0.1);
  }
}
</style>
