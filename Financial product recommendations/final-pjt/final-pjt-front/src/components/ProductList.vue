<template>
    <div v-if="product" class="product-container">
        <div class="product-header">
            <p class="bank-name">{{ product.kor_co_nm }}</p>
            <router-link :to="{ name: 'productdetail', params: { str: product.fin_prdt_cd }}" class="product-name">
                {{ product.fin_prdt_nm }}
            </router-link>
        </div>
        <div class="product-options">
            <div v-for="option in options" :key="option.id" class="option">
                <p class="interest-rate">{{ option.save_trm }}개월</p>
                <p class="interest-rate">{{ option.intr_rate2 }}%</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import axios from 'axios';
import { onMounted, ref, watch } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { defineProps } from 'vue';

const store = useCounterStore();
const options = ref([]);
const { product } = defineProps({
    product: Object
});


const fetchOptions = () => {
    axios({
        method: 'get',
        url: `${store.API_URL}/products/deposit-products/options/${product.fin_prdt_cd}/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    }).then((response) => {
        options.value = response.data;
        console.log(options);
    }).catch((error) => console.error(error));
};

onMounted(fetchOptions);

watch(() => product, () => {
    fetchOptions();
});
</script>

<style scoped>
.product-container {
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.product-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #ccc;
    padding-bottom: 10px;
    margin-bottom: 10px;
}

.bank-name {
    font-weight: bold;
    width: 200px;
    text-align: left;
}

.product-name {
    flex-grow: 1;
    text-align: left;
    margin-left: 10px;
    text-decoration: none;
    color: #007bff;
    transition: color 0.3s;
}

.product-name:hover {
    color: #0056b3;
}

.product-options {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.option {
    background-color: rgba(240, 240, 240, 0.8);
    border-radius: 5px;
    padding: 10px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    text-align: center;
    height: 85px;
    width: 80px;
}

.interest-rate {
    font-size: 14px;
    font-weight: bold;
}
</style>
