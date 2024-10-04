<template>
  <div>
    <header>
      <nav>
        <header>
          <nav class="menu">
            <RouterLink :to="{ name: 'product' }" class="product"> 상품 소개 </RouterLink>
            <RouterLink :to="{ name: 'exchange' }" class="exchange"> 환율 계산기 </RouterLink>
            <RouterLink :to="{ name: 'map' }" class="map"> 주변 은행 찾기 </RouterLink>
            <RouterLink :to="{ name: 'article' }" class="article-list"> 게시판 </RouterLink>
            <div>
              <template v-if="!store.isLogin">
                <RouterLink :to="{ name: 'signup' }" class="signup">회원가입</RouterLink>
                <RouterLink :to="{ name: 'login' }" class="login-button">
                  <p>로그인</p>
                </RouterLink>
              </template>
              <template v-else>
                <RouterLink :to="{ name: 'profile' }" class="signup">내 정보</RouterLink>
                <button @click="store.logout" class="login-button">로그아웃</button>
              </template>
            </div>
          </nav>
        </header>
        <RouterLink :to="{ name: 'home' }" class="logo">
          <img src="@/assets/logo.png" alt="logo" height="50px">
        </RouterLink>
      </nav>
    </header>
    <RouterView/>
    <div>
      <div @click="changeBot">
        <img v-if="changeKazusa" src="@/assets/kazusa.png" alt="챗봇" class="chat-bot">
        <img v-else :key = "gifkey" src="@/assets/kazusa.gif" alt="챗봇" class="chat-bot">
      </div>
      <div class="chat-box" v-if="!changeKazusa">
        <div class="chat-history">
          <div v-for="(entry, index) in chatHistory" :key="index" class="chat-bubble">
            <p><strong>질문:</strong> {{ entry.question }}</p>
            <p><strong>답변:</strong> {{ entry.answer }}</p>
          </div>
        </div>
        <form @submit.prevent="sendChat" @keyup.enter="sendChat" class="chat-form">
          <textarea name="chat" id="chat" cols="30" rows="3" v-model="chat"></textarea>
          <input type="submit" value="전송">
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useCounterStore } from './stores/counter';
import { ref } from 'vue';
import axios from 'axios';

const store = useCounterStore();
const changeKazusa = ref(true);
const chat = ref('');
const chatHistory = ref([]);

const changeBot = () => {
  changeKazusa.value = !changeKazusa.value;
};

const sendChat = () => {
  const question = chat.value;
  axios({
    method: 'post',
    url: `${store.API_URL}/products/products-recommend/`,
    data: { question },
    headers: { Authorization: `Token ${store.token}` }
  })
    .then((response) => {
      chat.value = '';
      chatHistory.value.push({
        question,
        answer: response.data.answer
      });
    })
    .catch((err) => console.log(err));
};
</script>

<style scoped>
.logo {
  position: absolute;
  width: 79px;
  left: 165px;
  top: 8px;
}

.product, .exchange, .map, .article-list, .signup {
  position: absolute;
  height: 24px;
  top: calc(50% - 24px/2);
  font-family: 'Roboto';
  font-style: normal;
  font-size: 14px;
  line-height: 24px;
  color: #929ECC;
  text-decoration: none;
}

.product {
  left: 31.53%;
}

.exchange {
  left: 40.33%;
}

.map {
  left: 49.14%;
}

.article-list {
  left: 58.94%;
}

.signup {
  left: 80.53%;
}

.menu {
  position: relative;
  width: 1960px;
  height: 60px;
  background: #FBFBFD;
  font-family: 'BlueArchive', sans-serif;
}

header {
  font-family: 'BlueArchive', sans-serif;
}

.login-button {
  display: flex;
  position: absolute;
  width: 132px;
  height: 40px;
  left: 1670px;
  top: 10px;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  color: #FFFFFF;
  background-color: #4E47FF;
  text-decoration: none;
}

.login-button p {
  margin: 0;
  line-height: 40px;
}

.chat-bot {
  position: absolute;
  width: 200px;
  height: 300px;
  top: 710px;
  left: 1700px;
  cursor: pointer;
}

.chat-box {
  position: absolute;
  top: 300px;
  left: 1450px;
  height: 400px;
  width: 420px;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 10px;
  padding: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  z-index: 100;
}

.chat-history {
  flex-grow: 1;
  overflow-y: scroll;
}

.chat-bubble {
  background: #f1f1f1;
  border-radius: 10px;
  padding: 10px;
  margin-bottom: 10px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
}

.chat-bubble p {
  margin: 0;
}

.chat-form {
  display: flex;
  flex-direction: column;
}

textarea {
  width: 100%;
  border-radius: 5px;
  padding: 5px;
  margin-bottom: 10px;
}

input[type="submit"] {
  align-self: flex-end;
  padding: 5px 10px;
  border: none;
  border-radius: 5px;
  background-color: #4E47FF;
  color: white;
  cursor: pointer;
}
</style>
