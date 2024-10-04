<template>
    <div class="container">
        <div class="charts">
            <Bar :data="savingChart1" />
        <!-- :options="chartOptions" -->
        </div>
        <div class="charts">
            <Bar :data="savingChart2" />
        <!-- :options="chartOptions" -->
        </div>
    </div>    
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { Bar } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
  
  const store = useCounterStore()
  const props = defineProps({
    savingoptions: Array
  })
  
  const savingNames1 = computed(() => props.savingoptions.filter(item => item.rsrv_type_nm === '정액적립식').map(item => item.save_trm + '개월'))
  const savingRates1 = computed(() => props.savingoptions.filter(item => item.rsrv_type_nm === '정액적립식').map(item => item.intr_rate))

  const savingNames2 = computed(() => props.savingoptions.filter(item => item.rsrv_type_nm === '자유적립식').map(item => item.save_trm + '개월'))
  const savingRates2 = computed(() => props.savingoptions.filter(item => item.rsrv_type_nm === '자유적립식').map(item => item.intr_rate))
  
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
  
  const savingChart1 = computed(() => ({
    labels: savingNames1.value,
    datasets: [
      {
        label: '정액적립식',
        backgroundColor: '#2699E6',
        data: savingRates1.value
      },
    ]    
  }))

  const savingChart2 = computed(() => ({
    labels: savingNames2.value,
    datasets: [
      {
        label: '자유적립식',
        backgroundColor: '#2699E6',
        data: savingRates2.value
      },
    ]    
  }))
  
  </script>
  
  <style scoped>
  
.charts {
  width: 400px;
  height: 200px;
}
  .container {
  display: flex;
  justify-content: space-around;
  align-items: center;
  gap: 20px;
  padding: 20px;
}
  </style>
  