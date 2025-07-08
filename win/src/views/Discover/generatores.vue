<!--
Music Generation View
Handles music generation based on text description
-->
<template>
  <div class="discover-generatores">
    <h1>音乐生成</h1>
    <div class="input-area">
      <textarea 
        v-model="description" 
        placeholder="请输入音乐描述..."
        class="description-input"
      ></textarea>
      <button @click="generateMusic" class="generate-btn">生成音乐</button>
    </div>

    <div class="result-area" v-if="generatedSong">
      <SongCard 
        :song="generatedSong"
        :index="0"
        @click="playSong"
      />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import SongCard from '@/components/Card/SongCard.vue'

interface Song {
  id: number
  name: string
  artists: Array<{id: number, name: string, cover?: string, alias?: string[]}>
  album: {id: number, name: string, cover?: string, alias?: string[]}
  duration: number
  cover: string
  free: 0 | 1 | 4 | 8
  mv: number | null
  type: 'song' | 'radio'
  audioUrl: string
  originCoverType?: number
  alia?: string
}

const description = ref('')
const generatedSong = ref<Song | null>(null)

const generateMusic = () => {
  // 模拟音乐生成
  generatedSong.value = {
    id: Date.now(),
    name: `生成的音乐 - ${description.value.substring(0, 10)}`,
    artists: [{id: 1, name: 'AI音乐生成器'}],
    album: {id: 1, name: 'AI创作专辑'},
    duration: 180,
    cover: '/public/images/album.jpg',
    free: 0,
    mv: null,
    type: 'song',
    audioUrl: '/public/audio/sample.mp3',
    originCoverType: 1,
    alia: 'AI生成音乐'
  }
}

const playSong = () => {
  if (generatedSong.value) {
    console.log('播放音乐:', generatedSong.value.name)
    // 这里应该调用播放器逻辑
  }
}
</script>

<style scoped>
.discover-generatores {
  padding: 30px;
  max-width: 800px;
  margin: 0 auto;
  background-color: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  animation: fadeIn 0.5s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

h1 {
  text-align: center;
  margin-bottom: 30px;
  color: #fff;
  font-size: 28px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.input-area {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 30px;
}

.description-input {
  width: 100%;
  min-height: 150px;
  padding: 15px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  resize: vertical;
  background-color: rgba(255, 255, 255, 0.05);
  color: #fff;
  font-size: 16px;
  transition: all 0.3s ease;
}

.description-input:focus {
  outline: none;
  border-color: #1db954;
  box-shadow: 0 0 0 2px rgba(29, 185, 84, 0.2);
}

.description-input::placeholder {
  color: rgba(255, 255, 255, 0.4);
}

.generate-btn {
  padding: 12px 24px;
  background: linear-gradient(135deg, #1db954 0%, #1ed760 100%);
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 500;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.generate-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.generate-btn:active {
  transform: translateY(0);
}

.result-area {
  margin-top: 30px;
  animation: fadeIn 0.5s ease-out;
}
</style>
