<template>
    <div class="center background-image">
        <form @submit.prevent="createArticle" class="create-box">
            <h1>게시글 작성</h1>
            <div class="form-group">
                <label for="title">제목 :</label>
                <input class="form-control" type="text" id="title" v-model.trim="title" aria-describedby="emailHelp">
            </div>
            <div class="form-group">
                <label for="content">내용 :</label>
                <textarea class="form-control content" id="content" v-model.trim="content"></textarea><br>
            </div>
            <button type="submit" class="btn btn-primary button-padding">게시글 작성</button>
        </form>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const store = useCounterStore();
const title = ref(null);
const content = ref(null);
const router = useRouter();

const createArticle = function () {
    axios({
        method: 'post',
        url: `${store.API_URL}/articles/`,
        data: {
            title: title.value,
            content: content.value,
        },
        headers: {
            Authorization: `Token ${store.token}`
        }
    }).then(() => {
        router.push({ name: 'article' });
    }).catch(err => console.log(err));
};
</script>

<style scoped>
.button-padding {
    padding: 7px 12px;
    margin-top: 10px;
}
.center {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    flex-direction: column;
}
.content {
    height: 600px;
}
.create-box {
    width: 1200px; /* 너비 조정 */
    max-width: 90%; /* 반응형 디자인을 위해 최대 너비 설정 */
    border: 1px solid rgba(0, 0, 0, 0.2);
    padding: 30px 20px;
    border-radius: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    background-color: white;
}
.background-image {
    width: 100%;
    height: 100vh; /* 전체 화면 높이에 맞추기 */
    background-image: url('@/assets/kivotos.png');
    background-size: cover;
    background-position: center;
    font-family: 'BlueArchive', sans-serif;
}
</style>
