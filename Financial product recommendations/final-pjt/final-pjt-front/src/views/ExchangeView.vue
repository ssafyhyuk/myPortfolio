<template>
  <div class="center background-image">
    <div class="box">
      <header class="header">
        <h1>환율 계산기</h1>
      </header>
      <form v-if="isChange" @submit.prevent="calculator" class="form-center">
        <h4>팔 때</h4>
        <div class="form-row">
          <select v-model="selectedCategory" @change="calculator" class="category-select">
            <option value="">카테고리 선택</option>
            <option v-for="category in categories" :key="category.id" :value="category.id">
              {{ category.cur_nm }}
            </option>
          </select>
          <label for="money">액수</label>
          <input type="text" id="money" v-model="money" class="amount-input">
        </div>
        <div class="result-box">
          <p>{{ foreginResult }} {{ foregincheck }}</p>
        </div>
      </form>
      <form v-if="!isChange" @submit.prevent="foreginCalculator" class="form-center">
        <h4>살 때</h4>
        <div class="form-row">
          <select v-model="selectedCategory" @change="foreginCalculator" class="category-select">
            <option value="">카테고리 선택</option>
            <option v-for="category in categories" :key="category.id" :value="category.id">
              {{ category.cur_nm }}
            </option>
          </select>
          <label for="foreginMoney">액수</label>
          <input type="text" id="foreginMoney" v-model="foreginMoney" class="amount-input">
        </div>
        <div class="result-box">
          <p>{{ result }} KRW</p>
        </div>
      </form>
      <button @click.prevent="change" class="change-button">전환</button>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { onMounted, ref, watch } from 'vue';

const store = useCounterStore();
const money = ref(null);
const result = ref(null);
const categories = ref([]);
const foreginMoney = ref(null);
const foreginResult = ref(null);
const isChange = ref(false);
const foregincheck = ref(null);

onMounted(() => {
  store.getExchanges();
  categories.value = store.exchanges;
});

// 선택된 카테고리를 저장하는 변수
const selectedCategory = ref('');

// 카테고리 변경 시 호출되는 함수
const handleCategoryChange = () => {
  console.log('Selected category:', selectedCategory.value);
};

const calculator = () => {
  const selected = categories.value.find(category => category.id === selectedCategory.value);
  if (selected) {
    foreginResult.value = (money.value / selected.deal_bas_r).toFixed(4);
    foregincheck.value = selected.cur_unit;
  } else {
    foreginResult.value = '카테고리를 선택해주세요';
  }
};

const foreginCalculator = () => {
  const selected = categories.value.find(category => category.id === selectedCategory.value);
  if (selected) {
    result.value = (foreginMoney.value * selected.deal_bas_r).toFixed(4);
  } else {
    result.value = '카테고리를 선택해주세요';
  }
};

const change = () => {
  isChange.value = !isChange.value;
};

// 액수가 변경될 때마다 계산을 자동으로 실행
watch([money, selectedCategory], () => {
  if (isChange.value) {
    calculator();
  }
});

watch([foreginMoney, selectedCategory], () => {
  if (!isChange.value) {
    foreginCalculator();
  }
});
</script>

<style scoped>
.center {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-image: url('@/assets/beach.jpg');
  background-size: cover;
  background-position: center;
  font-family: 'BlueArchive', sans-serif;
}

.box {
  background-color: rgba(255, 255, 255, 0.85);
  border-radius: 20px;
  padding: 30px;
  width: 100%;
  max-width: 600px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.header {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}

.form-center {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
}

.form-row {
  display: flex;
  align-items: center;
  width: 100%;
  gap: 10px;
}

.category-select, .amount-input {
  flex: 1;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
}

.result-box {
  width: 100%;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  box-sizing: border-box;
  text-align: center;
}

p {
  font-size: 18px;
  color: #555;
}

.change-button {
  padding: 10px;
  width: 70px;
  font-size: 16px;
  background-color: #2699E6;
  color: white;
  border: none;
  border-radius: 10px;
  font-family: 'Plus Jakarta Sans';
  font-style: normal;
  font-weight: 700;
  cursor: pointer;
  transition: background-color 0.3s;
  line-height: 110%;
  margin-top: 10px;
  margin-left: 465px;
}

.change-button:hover {
  background-color: #0056b3;
}
</style>
