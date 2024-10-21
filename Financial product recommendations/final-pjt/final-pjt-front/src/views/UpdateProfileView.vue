<template>
    <div class="center background-image">
    <form @submit.prevent="updateUser" class="signup-box" v-if="user">
        <h1>회원 정보 수정</h1>
        <hr>
        <div class="form-group">
        <label for="age">연령</label>
        <input class="form-control" type="number" id="age" v-model.trim="user.age">
        </div>
        <div class="form-group">
        <label for="asset">자산</label>
        <select class="form-control" id="asset" v-model="user.asset">
            <option v-for="option in assetCategories" :key="option" :value="option">{{ option }}</option>
        </select>
        </div>
        <div class="form-group">
        <label for="income">연봉</label>
        <select class="form-control" id="income" v-model="user.income">
            <option v-for="option in incomeCategories" :key="option" :value="option">{{ option }}</option>
        </select>
        </div>
        <div class="form-group">
        <label for="nickname">닉네임</label>
        <input class="form-control" type="text" id="nickname" v-model.trim="user.nickname">
        </div>
        <div class="right">
        <button type="submit" class="btn updatebutton">회원 정보 수정</button>
    </div>
    </form>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router';
const store = useCounterStore()

const username = ref(null)
const age = ref(null)
const asset = ref(null)
const income = ref(null)
const nickname = ref(null)
const router = useRouter()
const user = ref({});

const assetCategories = [
    '1억이하', '1억 ~ 3억', '3억 ~ 6억', '6억 ~ 10억', '10억이상'
]

const incomeCategories = [
    '1000만이하', '1000만 ~ 3000만', '3000만 ~ 6000만', '6000만 ~ 1억', '1억이상'
]

onMounted(() => {
    axios({
        method : 'get',
        url : `${store.API_URL}/accounts/user/`,
        headers: {
        Authorization: `Token ${store.token}`
    }}).then((response) => {
        user.value = response.data
        console.log(response.data)
    })
    })

const updateUser = () => {
    axios({
        method : 'put',
        url : `${store.API_URL}/accounts/update-user/`,
        data: {
        age: user.value.age,
        asset: user.value.asset,
        income: user.value.income,
        nickname: user.value.nickname,
        },
    headers: {
        Authorization: `Token ${store.token}`
    }}).then((response) => {
        console.log('수정하였습니다.')
        router.push({name: 'profile'})
    }).catch((error) => {console.log(error)})
    
    
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

.updatebutton {
    margin-top: 30px;
    padding: 10px;
    width: 150px;
    background: #2699E6;    
    border-radius: 10px;
    font-family: 'Plus Jakarta Sans';
    font-style: normal;
    font-weight: 700;
    font-size: 16px;
    line-height: 110%;
    letter-spacing: -0.03em;
    color: #FFFFFF;
    cursor : pointer
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

.right {
    display: flex;
    justify-content: right;
}
</style>
