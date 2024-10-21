<template>
    <div class="main-container">
        <div class="sidebar">
        <ul class="list">
            <h2>상품 종류</h2>
            <hr>
            <li><RouterLink :to="{ name: 'product' }" class="product"> 정기 예금 </RouterLink></li>
            <li><RouterLink :to="{ name: 'savingproduct' }" class="savingproduct"> 적금 </RouterLink></li>
        </ul>
        </div>
        <div class="center background-image">
        <div class="box">
            <header class="header">
            <h1>상품 소개</h1>
            </header>
            <select v-model="selectedCategory" @change="handleCategoryChange" class = "select">
            <option value="" disabled>은행 목록</option>
            <option v-for="category in store.depositproducts" :key="category.id" :value="category.kor_co_nm">
                {{ category.kor_co_nm }}
            </option>
            </select>
            <div v-if="filteredProducts.length === 0">해당 은행은 상품이 없습니다.</div>
            <ProductList 
            v-for="product in filteredProducts"
            :key="product.id"
            :product="product"/>
        </div>
        </div>
    </div>
</template>




<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import { ref, onMounted, computed } from 'vue';
import ProductList from '@/components/ProductList.vue';

const store = useCounterStore();
const selectedCategory = ref('');

const handleCategoryChange = () => {
console.log('Selected category:', selectedCategory.value);
};

const filteredProducts = computed(() => {
if (!selectedCategory.value) {
    return store.depositproducts;
}
return store.depositproducts.filter(product => product.kor_co_nm === selectedCategory.value);
});

onMounted(async () => {
try {
    await store.getDepositProducts();
} catch (error) {
    console.error(error);
}
});
</script>



<style scoped>
.main-container {
display: flex;
width: 100%;
height: 100vh;
font-family: 'BlueArchive', sans-serif;
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

.center {
display: flex;
justify-content: center;
align-items: center;
flex-direction: column;
}

.box {
background-color: rgba(255, 255, 255, 0.8);
border-radius: 20px;
padding: 20px;
width: 100%;
max-width: 1200px;
height: 80%;
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
backdrop-filter: blur(10px);
box-sizing: border-box;
overflow-y: scroll;
}

.header {
width: 100%;
display: flex;
flex-direction: column;
align-items: flex-start;
margin-bottom: 10px;
}

.header h1 {
width: 100%;
text-align: center;
margin-bottom: 20px;
}

.sidebar {
    position: absolute;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    height: 200px;
    width: 200px;
    left: 100px;
    top: 300px;
    background-color: rgba(255, 255, 255, 0.8);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    box-sizing: border-box;
    border-radius: 20px;
    backdrop-filter: blur(10px);
}

.sidebar h2 {
margin-top: 0;
}

.sidebar ul {
list-style: none;
padding: 0;
}

.sidebar ul li {
margin-bottom: 10px;
}
.select {
    margin-bottom: 20px;
    margin-left: 5px;
}

.product {
    text-decoration: none;
}

.savingproduct {
    text-decoration: none;
}

.list {
    margin-top: 10px;
    margin-left: 10px;
}
</style>

