<template>
  <div class="center">
    <div class="com-box">
      <div v-if="article" class="content-wrapper">
        <form @submit.prevent="updateArticle">
          <textarea v-model="article.title" id="title" class="title-textarea">{{ article.title }}</textarea>
          <div>
            <label for="content">내용</label>
            <textarea v-model="article.content" id="content" class="content-textarea">{{ article.content }}</textarea>
          </div>
          <div class="right">
            <button type="submit" class="articlebutton">저장</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter';
import { useRoute, useRouter } from 'vue-router';

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)

onMounted(() => {
  axios({
      method: 'get',
      url: `${store.API_URL}/articles/detail/${route.params.id}/`,
      headers: {
          Authorization: `Token ${store.token}`
      }
  }).then((response) => {
      article.value = response.data
  }).catch((error) => console.log(error))
})

const updateArticle = () => {
  axios({
      method: 'put',
      url: `${store.API_URL}/articles/detail/${route.params.id}/`,
      headers: {
          Authorization: `Token ${store.token}`
      },
      data: {
          title: article.value.title,
          content: article.value.content
      }
  }).then(() => {
      alert('게시글이 수정되었습니다.')
      router.push({ name: 'articledetail', params: { id: route.params.id } })
  }).catch((error) => console.log(error))
}
</script>

<style scoped>
.center {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-image: url('@/assets/desk.jpg');
  background-size: cover;
  background-position: center;
  text-align: left;
}

.com-box {
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 20px;
  padding: 20px;
  width: 1000px;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(10px);
  box-sizing: border-box;
  overflow-y: scroll;
  height: 80%;
  position: relative;
}

.content-wrapper {
  display: flex;
  flex-direction: column;
  width: 100%;
  font-family: 'BlueArchive', sans-serif;
}

form {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.title-textarea,
.content-textarea {
  width: 100%;
  margin-bottom: 10px;
  padding: 10px;
  font-family: 'BlueArchive', sans-serif;
}

.content-textarea {
  height: 200px;
}

.articlebutton {
  background-color: #2699E6;
  color: white;
  border-radius: 5px;
  padding: 5px 10px;
  font-family: 'Plus Jakarta Sans';
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  margin-top: 10px;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.articlebutton:hover {
  background-color: #0056b3;
}

.right {
  display: flex;
  justify-content: right;
}
</style>
