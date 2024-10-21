<template>
  <div class="center">
    <div class="com-box">
      <h3>{{ user.nickname }}님의 프로필</h3>
      <hr>
      <div class="profile-container">
        <img :src="user.image" alt="프로필 이미지" class="profile-image">
        <div class="profile-details">
          <p><strong>아이디:</strong> {{ user.username }}</p>
          <p><strong>닉네임:</strong> {{ user.nickname }}</p>
          <p><strong>나이:</strong> {{ user.age }}</p>
          <p><strong>연봉:</strong> {{ user.income }}</p>
          <p><strong>자산:</strong> {{ user.asset }}</p>
          <p><strong>가입 상품 : </strong>
            <span v-for="depositproduct in depositproducts" :key="depositproduct.id">&nbsp{{ depositproduct.fin_prdt_nm }}&nbsp</span>
            <span v-for="savingproduct in savingproducts" :key="savingproduct.id">&nbsp{{ savingproduct.fin_prdt_nm }}&nbsp</span>
          </p>
        </div>
      </div>
      <div class="action-buttons">
        <router-link :to="{ name: 'updateprofile' }" class="btn updatebutton">회원 정보 수정</router-link>
        <button @click="confirmDelete" class="btn btn-danger deletebutton">회원 탈퇴</button>
      </div>
    </div>

    <div v-if="showConfirmDialog" class="confirm-dialog">
      <div class="confirm-dialog-content">
        <p>정말 회원 탈퇴를 하시겠습니까?</p>
        <div class="confirm-buttons">
          <button @click="deleteUser" class="btn btn-danger">확인</button>
          <button @click="cancelDelete" class="btn btn-secondary">취소</button>
        </div>
      </div>
    </div>
  </div>
</template>


  
<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const store = useCounterStore();
const user = ref({});
const router = useRouter();
const depositproducts = ref([]);
const savingproducts = ref([]);
const showConfirmDialog = ref(false);

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/user/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  }).then((response) => {
    user.value = response.data;
    console.log(user.value);
  }).catch((error) => {
    console.log(error);
  });

  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/deposit-products-list/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  }).then((response) => {
    console.log(response.data);
    depositproducts.value = response.data;
  }).catch((error) => {
    console.log(error);
  });

  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/saving-products-list/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  }).then((response) => {
    savingproducts.value = response.data;
  }).catch((error) => {
    console.log(error);
  });
});

const confirmDelete = () => {
  showConfirmDialog.value = true;
};

const cancelDelete = () => {
  showConfirmDialog.value = false;
};

const deleteUser = () => {
  axios({
    method: 'delete',
    url: `${store.API_URL}/accounts/update-user/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  }).then((response) => {
    console.log('탈퇴되었습니다.');
    // Redirect to home or login page after deletion
    router.push('/login');
  }).catch((error) => {
    console.log(error);
  });
  showConfirmDialog.value = false;
};
</script>

  
<style scoped>
.center {
  display: flex;
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
  height: 100vh; /* Full viewport height */
  background-image: url('@/assets/desk.jpg');
  background-size: cover;
  background-position: center;
  font-family: 'BlueArchive', sans-serif;
}

.com-box {
  background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent white background */
  border-radius: 20px;
  padding: 20px;
  width: 800px;
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for a lifted effect */
  backdrop-filter: blur(10px); /* Blur background for better readability */
  box-sizing: border-box;
}

.profile-container {
  display: flex;
  flex-direction: row; /* Horizontal layout */
  align-items: center;
  width: 100%;
  margin-top: 20px;
}

.profile-image {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  object-fit: cover;
  margin-right: 20px;
}

.profile-details {
  display: flex;
  flex-direction: column;
}

.profile-details p {
  margin: 5px 0;
}

.action-buttons {
  display: flex;
  justify-content: flex-end;
  width: 100%;
  margin-top: auto;
}

.btn {
  margin: 10px;
}

.confirm-dialog {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.confirm-dialog-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.confirm-buttons {
  display: flex;
  justify-content: space-between;
  font-family: 'Plus Jakarta Sans';
font-style: normal;
font-weight: 700;
font-size: 16px;
  margin-top: 10px;
  width: 100%;
}

.updatebutton {
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

.deletebutton {
  font-family: 'Plus Jakarta Sans';
font-style: normal;
font-weight: 700;
font-size: 16px;
cursor : pointer;
border-radius: 10px;
}
</style>



  