<template>
  <div class="center background-image">
    <form @submit.prevent="signUp" class="signup-box">
      <h1>회원가입</h1>
      <hr>
      <div class="form-group">
        <label for="username">아이디</label>
        <input class="form-control" type="text" id="username" v-model.trim="username" aria-describedby="emailHelp">
      </div>
      <div class="form-group">
        <label for="password1">패스워드</label>
        <input class="form-control" type="password" id="password1" v-model.trim="password1">
      </div>
      <div class="form-group">
        <label for="password2">패스워드 확인</label>
        <input class="form-control" type="password" id="password2" v-model.trim="password2">
      </div>
      <div class="form-group">
        <label for="age">연령</label>
        <input class="form-control" type="number" id="age" v-model.trim="age">
      </div>
      <div class="form-group">
        <label for="asset">자산</label>
        <select class="form-control" id="asset" v-model="asset">
          <option v-for="option in assetCategories" :key="option" :value="option">{{ option }}</option>
        </select>
      </div>
      <div class="form-group">
        <label for="income">연봉</label>
        <select class="form-control" id="income" v-model="income">
          <option v-for="option in incomeCategories" :key="option" :value="option">{{ option }}</option>
        </select>
      </div>
      <div class="form-group">
        <label for="nickname">닉네임</label>
        <input class="form-control" type="text" id="nickname" v-model.trim="nickname">
      </div>
      <button type="submit" class="btn btn-primary button-padding">가입하기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const age = ref(null)
const asset = ref(null)
const income = ref(null)
const nickname = ref(null)
const myImg = ref(null)

const assetCategories = [
  '1억이하', '1억 ~ 3억', '3억 ~ 6억', '6억 ~ 10억', '10억이상'
]

const incomeCategories = [
  '1000만이하', '1000만 ~ 3000만', '3000만 ~ 6000만', '6000만 ~ 1억', '1억이상'
]

const signUp = () => {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    age: age.value,
    asset: asset.value,
    income: income.value,
    nickname: nickname.value,
    myImg: myImg.value,
  }
  store.signUp(payload)
}
</script>

<style scoped>
  .center {
    display: flex;
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    height: 100vh; /* Full viewport height */
    font-family: 'BlueArchive', sans-serif;
  }
.signup-box {
  background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent white background */
  border-radius: 20px;
  padding: 20px;
  width: 1000px;
  height: 650px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for a lifted effect */
  backdrop-filter: blur(10px); /* Blur background for better readability */
  box-sizing: border-box;
}

.button-padding {
  padding: 7px 12px;
  margin-top: 30px;
  margin-left: 870px;
}

.background-image {
  width: 100%;
  height: 100vh;
  background-image: url('@/assets/kivotos.png');
  background-size: cover;
  background-position: center;
}

.form-group {
  margin-left: 10px;
}
</style>
