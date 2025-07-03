<template>
  <div class="community-container">
    <h1 class="page-title">音乐社区</h1>
    
    <div class="post-list">
      <div v-for="post in posts" :key="post.id" class="post-card">
        <div class="post-header">
          <img :src="post.user.avatar" class="user-avatar">
          <div class="user-info">
            <span class="username">{{ post.user.name }}</span>
            <span class="post-time">{{ post.time }}</span>
          </div>
        </div>
        
        <div class="post-content">
          {{ post.content }}
        </div>
        
        <div class="referenced-music">
          <div v-for="track in post.tracks" :key="track.id" 
               class="music-item"
               @click="playTrack(track)">
            <img :src="track.cover" class="music-cover">
            <div class="music-info">
              <div class="music-name">{{ track.name }}</div>
              <div class="music-artist">{{ track.artist }}</div>
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
import { ref } from 'vue';
// import { onMounted } from 'vue';
import player from '@/utils/player';
import { useMusicStore } from '@/stores';
// import { getCommunityPosts } from '@/api/community';

interface Track {
  id: string | number;
  name: string;
  artist: string;
  cover: string;
  url: string;
}

interface Post {
  id: string;
  user: {
    id: string;
    name: string;
    avatar: string;
  };
  content: string;
  time: string;
  tracks: Track[];
  likes: number;
}

const posts = ref<Post[]>([]);
const loading = ref(false);
const error = ref<Error | null>(null);

// const fetchPosts = async () => {
//   try {
//     loading.value = true;
//     const { data } = await getCommunityPosts();
//     posts.value = data.map(post => ({
//       ...post,
//       tracks: post.tracks.map(track => ({
//         ...track,
//         id: track.id.toString()
//       }))
//     }));
//   } catch (err: unknown) {
//     error.value = err instanceof Error ? err : new Error(String(err));
//     console.error('获取社区帖子失败:', err);
//   } finally {
//     loading.value = false;
//   }
// };

// onMounted(() => {
//   fetchPosts();
// });

const playTrack = (track: Track) => {
  // 更新当前播放歌曲信息
  const musicStore = useMusicStore();
  musicStore.playSong = {
    id: Number(track.id), // 转换为number类型
    name: track.name,
    artists: track.artist,
    album: '未知专辑',
    cover: track.cover,
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
  background-color: #121212;
  color: #e0e0e0;
  min-height: 100vh;
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
  background-color: #1e1e1e;
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
  background-color: #282828;
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
