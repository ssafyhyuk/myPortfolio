<template>
  <div class="center">
    <div class="com-box">
      <div v-if="article" class="content-wrapper">
        <h2>{{ article.title }}</h2>
        <p class="right">{{ article.nickname }}</p>
        <hr>
        <div class="contentbox">
          <p>{{ article.content }}</p>
        </div>
        <div class = "centerbox">
        <div class="likebox">
          <span>{{ likeUserCount }}</span>
          <img src="@/assets/추천.png" alt="추천" @click="likeAritcle" class="likebutton">
        </div>
      </div>
        <div class="articlebuttonbox" v-if="isOwner(article)">
          <button @click="updateArticle" class="articlebutton">수정</button>
          <button @click="deleteArticle" class="articlebutton">삭제</button>
        </div>
      </div>
      <footer class="full-width-footer">
        <ul class="comment-list">
          <div v-for="comment in comments" :key="comment.id">
            <div class="comment-wrapper">
              <div class="nickname">{{ comment.nickname }}</div>
              <div class="comment">{{ comment.content }}</div>
            </div>
            <div class = "buttonbox" v-if="isOwner(comment)">
              <button @click="changeCommentBoolean(comment)" class="commentbutton">수정</button>
              <button @click="deleteComment(comment)" class="commentbutton">삭제</button>
            </div>
            <hr>
            <form @submit.prevent="updateComment(comment)" v-if="comment.editing">
              <textarea v-model="comment.content" class="newComment" id="commentContent"></textarea>
              <div class="right">
              <input type="submit" value="댓글 수정" class = "commentbutton">
            </div>
            </form>
          </div>
        </ul>
        <span class = "nicknamecreate">{{ nickname }}</span>
        <textarea type="text" v-model="newComment" class="newComment"></textarea>
        <div class = "right">
        <button @click="addComment" class = "commentbutton">댓글 추가</button>
      </div>
      </footer>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useCounterStore } from '@/stores/counter';
import { useRoute, useRouter } from 'vue-router';

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const newComment = ref('');
const comments = ref([]);
const nickname = ref(null);

const isOwner = (item) => {
  return item.nickname === nickname.value;
}


onMounted(() => {
  axios({
      method : 'get',
      url : `${store.API_URL}/articles/detail/${route.params.id}/`,
      headers : {
          Authorization: `Token ${store.token}`
      }
  }).then((response) => {
      article.value = response.data
  }).catch((error) => console.log(error));

  axios({
      method : 'get',
      url : `${store.API_URL}/articles/comments/${route.params.id}/`,
      headers : {
          Authorization: `Token ${store.token}`
      }
  }).then((response) => {
      comments.value = response.data.map(comment => ({
        ...comment,
        editing: false
      }));
  }).catch((error) => console.log(error));

  axios({
    method : 'get',
    url : `${store.API_URL}/accounts/user/`,
    headers : {
          Authorization: `Token ${store.token}`
      }
  }).then((response) => {
    nickname.value = response.data.nickname
  }).catch((error) => console.log(error));
})

const updateArticle = () => {
  router.push({ name: 'updatearticle', params: { id: route.params.id } })
}

const deleteArticle = () => {
  axios({
      method: 'delete',
      url: `${store.API_URL}/articles/detail/${route.params.id}/`,
      headers: {
          Authorization: `Token ${store.token}`
      }
  }).then(() => {
      alert('게시글이 삭제되었습니다.')
      router.push({ name: 'article' })
  }).catch((error) => console.log(error))
}

const addComment = () => {
  axios({
      method: 'post',
      url: `${store.API_URL}/articles/comments/${route.params.id}/create/`,
      data: {
          content: newComment.value,
      },
      headers: {
          Authorization: `Token ${store.token}`
      }
  }).then((response) => {
      comments.value.push({
        ...response.data,
        editing: false
      });
      newComment.value = '';  // 댓글 추가 후 입력 필드 초기화
  }).catch(err => console.log(err));
};

const deleteComment = (comment) => {
  axios({
      method: 'delete',
      url: `${store.API_URL}/articles/comments/${route.params.id}/${comment.id}/`,
      headers: {
          Authorization: `Token ${store.token}`
      }
  }).then(() => {
      comments.value = comments.value.filter(c => c.id !== comment.id);
  }).catch(err => console.log(err));
};

const updateComment = (comment) => {
  axios({
      method: 'put',
      url: `${store.API_URL}/articles/comments/${route.params.id}/${comment.id}/`,
      data: {
          content: comment.content
      },
      headers: {
          Authorization: `Token ${store.token}`
      }
  }).then((response) => {
      const index = comments.value.findIndex(c => c.id === comment.id);
      if (index !== -1) {
          comments.value[index] = response.data;
          comments.value[index].editing = false;
      }
  }).catch(err => console.log(err));
};

const changeCommentBoolean = (comment) => {
  comment.editing = !comment.editing;
}

const likeAritcle = () => {
  axios({
    method : 'get',
    url : `${store.API_URL}/articles/like/${route.params.id}/`,
      headers : {
          Authorization: `Token ${store.token}`
      }
  }).then(() => {
    console.log('좋아요');
    location.reload(); // 페이지 새로고침
  }).catch((err) => console.log(err))
}

const likeUserCount = computed(() => article.value.like_users.length);
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
  position: relative; /* 부모 요소에 대해 상대적 위치 설정 */
}

.full-width-footer {
  margin-top: 15px;
  width: 100%; /* Set the width to 100% */
  font-family: 'BlueArchive', sans-serif;
}

.comment-list {
  list-style: none;
  padding: 0;
}

.contentbox {
  min-height: 400px;
  width: 100%;
  font-family: 'BlueArchive', sans-serif;
}

.likebox {
  padding: 10px;
  padding-left: 20px;
  border: 1px solid black;
}
.centerbox {
  display: flex;
  justify-content: center;
  align-items: center; /* 세로 가운데 정렬 */
  margin-bottom: 40px;
}
.articlebuttonbox {
  display: flex;
  justify-content: right;
  padding-bottom: 10px;
  border-bottom: solid 1px black;
}
.articlebutton {
  background-color: #2699E6;
  color: white; /* 파란색 */
  border-radius: 5px;
  padding: 5px 10px;
  font-family: 'Plus Jakarta Sans';
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  margin-top: 10px;
  margin-right: 8px;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}
.commentbutton {
  background-color: #2699E6;
  color: white; /* 파란색 */
  border-radius: 5px;
  padding: 5px 10px;
  font-family: 'Plus Jakarta Sans';
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  margin-top: 10px;
  margin-right: 8px;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.likebutton {
  margin-left: 30px;
  width: 80px;
  height: 80px;
}

.buttonbox{
  display: flex;
  justify-content: right;
}
.comment-wrapper {
  display: flex;
  align-items: flex-start; /* 닉네임과 댓글이 위에서부터 정렬되도록 설정 */
}

.nickname {
  width: 180px;
  margin-right: 10px; /* 닉네임과 댓글 사이의 간격을 조정 */
}

.comment {
  display: inline-block;
  width: calc(100% - 180px);
  flex-grow: 1; /* 댓글이 가능한 넓은 공간을 차지하도록 설정 */
  overflow-wrap: break-word; /* 긴 텍스트 줄 바꿈 설정 */
}
.content-wrapper {
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
  font-family: 'BlueArchive', sans-serif;
}

.newComment {
  width: 100%;
  margin-top: 10px;
}
.right {
  display: flex;
  justify-content: right;
}

</style>

