<template>
    <div class = "background-image">
    <div class="container" v-if="product">
        <h1>상품 상세</h1>
        <hr>
        <div class="product-details">
        <p><span class="label">상품 명:</span> {{ product.fin_prdt_nm }}</p>
        <p><span class="label">가입 대상 :</span> {{ product.join_member }}</p>
        <p><span class="label">가입 제한 :</span> {{ product.join_deny }}</p>
        <p><span class="label">가입 방법 :</span> {{ product.join_way }}</p>
        <p><span class="label">우대 조건 :</span> {{ product.spcl_cnd }}</p>
        <p><span class="label">만기 후 이자율 :</span> {{ product.mtrt_int }}</p>
        <p><span class="label">최고 한도 :</span> {{ product.max_limit }}</p>
        <p><span class="label">기타 유의사항 :</span> {{ product.etc_note }}</p>
    </div>
    <div class = "right">
        <button @click.prevent="productSignout" class="signup" v-if="isProductSignedUp">상품 해지</button>
        <button @click.prevent="productSignup" class="signup" v-else>상품 가입</button>   
    </div>
    <h1>저축기간별 저축금리</h1>
    <hr>
    <MyChart 
        :depositoptions="depositoptions"
    />
    </div>
</div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useCounterStore } from '@/stores/counter';
import { useRoute } from 'vue-router';
import MyChart from '@/components/MyChart.vue'

const store = useCounterStore()
const route = useRoute()
const product = ref([])
const depositproducts = ref([])
const depositoptions = ref([])

axios({
    method: 'get',
    url: `${store.API_URL}/products/deposit-products/options/${route.params.str}/`,
    headers : {
        Authorization: `Token ${store.token}`
    }
}).then((response) => {
    depositoptions.value = response.data
}).catch((error) => console.log(error))


onMounted(() => {
    axios({
        method : 'get',
        url : `${store.API_URL}/products/deposit-products/detail/${route.params.str}/`,
        headers : {
            Authorization: `Token ${store.token}`
        }
    }).then((response) => {
        product.value = response.data
    }).catch((error) => console.log(error))

    axios({
    method: 'get',
    url: `${store.API_URL}/accounts/deposit-products-list/`,
    headers: {
        Authorization: `Token ${store.token}`
    }
    }).then((response) => {
    console.log(response.data);
    depositproducts.value = response.data;
    console.log(response.data);
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
    console.log(response.data);
    }).catch((error) => {
    console.log(error);
    });
})
const isProductSignedUp = computed(() => {
    return depositproducts.value.some(item => item.fin_prdt_nm === product.value.fin_prdt_nm);
});


const productSignup = () => {
    axios({
        method : 'get',
        url : `${store.API_URL}/products/deposit-products/join/${route.params.str}/`,
        headers : {
            Authorization: `Token ${store.token}`
        }
    }).then((response) => {
        console.log('가입되었습니다.')
        location.reload();
    }).catch((error) => console.log(error))
}

const productSignout = () => {
    axios({
        method: 'get',
        url: `${store.API_URL}/products/deposit-products/remove/${route.params.str}/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    }).then((response) => {
        console.log('해지되었습니다.')
        location.reload();
    }).catch((error) => console.log(error))
}
</script>

<style scoped>
.container {
background-color: white; /* DodgerBlue background color */
color: black;
padding: 20px;
border-radius: 10px;
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
max-width: 1000px;
margin: 20px auto;
font-family: 'BlueArchive', sans-serif;
}

.product-details {
display: flex;
flex-direction: column;
gap: 10px;
margin-left: 10px;
}

.product-details p {
margin: 0;
padding: 10px;
background: rgba(255, 255, 255, 0.2);
border-radius: 5px;
}

.label {
font-weight: bold;
color: #1E90FF; /* Gold color for labels */
}

.product-details p:hover {
background: rgba(255, 255, 255, 0.3);
}

.background-image {
flex: 1;
background-image: url('@/assets/kivotos.png');
background-size: cover;
background-position: center;
display: flex;
justify-content: center;
align-items: center;
min-height: 100vh;
}

.signup{
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
    cursor : pointer
}

.right {
    display: flex;
    justify-content: right;
    margin-top: 20px;
}

</style>
  