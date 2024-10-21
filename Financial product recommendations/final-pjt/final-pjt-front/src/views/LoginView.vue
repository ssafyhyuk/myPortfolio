<template>
    <div class = "center background-image">
            <form @submit.prevent="login" class = "login-box">
                <h1>로그인</h1>
                <hr>
                <div class="form-group">
                    <label for="username">username</label>
                    <input class="form-control" type="text" id = "username" v-model.trim="username" aria-describedby="emailHelp">
                    <!-- <small id="usernameHelp" class="form-text text-muted">We'll never share your email with anyone else.</small> -->
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input class="form-control" type="password" id = "password" v-model.trim="password">
                </div>
                <div class = "right">
                <button type="submit" class="login" >login</button>
            </div>
            </form>
    </div>
</template>

<script setup>

import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router'

const store = useCounterStore()


const username = ref(null)
const password = ref(null)

const login = function() {
    const payload = {
        username: username.value,
        password: password.value
    }
    store.login(payload)
}


</script>

<style scoped>
.button-padding {
    padding: 7px 12px;
    margin-top: 10px;
}
.center {
    display: flex;
    justify-content: center;
    align-items: center; /* 수직 정렬 추가 */
    min-height: 100vh; /* 뷰포트 높이의 100%로 설정하여 수직 중앙 정렬 보장 */
    flex-direction: column; /* 수직 방향 정렬 */
    font-family: 'BlueArchive', sans-serif;
}
.form-group {
    margin-bottom: 10px;
}
.login-box {
    border: 1px solid rgba(0, 0, 0, 0.2);
    padding: 30px 20px;
    border-radius: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 부드러운 그림자 효과 */
    background-color: white;
    width: 500px;
    height: 350px;
}
.background-image {
width: 1900px;
height: 1400px;
background-image: url('@/assets/kivotos.png');
background-size: cover;
background-position: center;
}

.login {
    padding: 10px;
    width: 100px;
    background: #2699E6;    
    border-radius: 10px;
    font-family: 'Plus Jakarta Sans';
    font-style: normal;
    font-weight: 700;
    font-size: 16px;
    line-height: 110%;
    letter-spacing: -0.03em;
    color: #FFFFFF;
    cursor : pointer;
    margin-top : 20px;
}

.right {
    display: flex;
    justify-content: right;
}
</style>