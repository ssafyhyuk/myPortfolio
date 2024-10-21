<!-- src/components/MyChart.vue -->
<template>
    <div class="charts">
      <Bar :data="savingChart" :options="chartOptions" />
    </div>
  </template>
  
  <script setup>
    import { useUserStore } from '@/stores/user'
    import { ref, computed } from 'vue'
    import { useSavingStore } from '@/stores/saving'
    import { Bar } from 'vue-chartjs'
    import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
    
    const store = useUserStore()
    const sastore = useSavingStore()
    
    const savingIds = computed(() => store.loginUser.savings.map(item => item.saving))
    const savings = computed(() => sastore.savings.filter(item => savingIds.value.includes(item.id)))
    const savingNames = computed(() => savings.value.map(item => item.fin_prdt_nm))
    const savingOptions = computed(() => sastore.savingoptions.filter(item => savingIds.value.includes(item.saving)))
    const savingRates = computed(() => {
      const groupedSaving = savingOptions.value.reduce((acc, cur) => {
        if (!acc[cur.fin_prdt_cd]) {
          acc[cur.fin_prdt_cd] = []
        }
        acc[cur.fin_prdt_cd].push(cur.intr_rate)
        return acc
      }, {})
      const result = []
      for (const key in groupedSaving) {
        const avg = groupedSaving[key].reduce((acc, cur) => acc + cur, 0) / groupedSaving[key].length;
        result.push(avg) 
      }
      return result
    })
    const savingRates2 = computed(() => {
      const groupedSaving = savingOptions.value.reduce((acc, cur) => {
        if (!acc[cur.fin_prdt_cd]) {
          acc[cur.fin_prdt_cd] = []
        }
        acc[cur.fin_prdt_cd].push(cur.intr_rate2)
        return acc
      }, {})
      const result = []
      for (const key in groupedSaving) {
        const avg = groupedSaving[key].reduce((acc, cur) => acc + cur, 0) / groupedSaving[key].length;
        result.push(avg) 
      }
      return result
    })
    
    ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
  
    const savingChart = {
    labels: savingNames.value,
    datasets: [
      {
        label: '저축금리',
        backgroundColor: '#16a34a',  // 여기야 여기!! 색깔 바꾸는 거 여기야!
        data: savingRates.value
      },
      {
        label: '최고우대금리',
        backgroundColor: '#facc15',  // 여기야 여기!! 색깔 바꾸는 거 여기야!
        data: savingRates2.value
      }
    ]
  }
  
    // const chartOptions = {
    //   responsive: true,
    //   maintainAspectRatio: false
    // }
  </script>
  
  <style scoped>
    /* .charts {
      width: 500px;
      height: 200px;
    } */
  </style>