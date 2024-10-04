<template>
  <!-- {{ depositoptions }} -->
  <div class="charts">
    <Bar :data="savingChart" />
    <!-- :options="chartOptions" -->
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

const store = useCounterStore()
const props = defineProps({
  depositoptions: Array
})

const savingNames = computed(() => props.depositoptions.map(item => item.save_trm + '개월'))
const savingRates = computed(() => props.depositoptions.map(item => item.intr_rate))

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const savingChart = computed(() => ({
  labels: savingNames.value,
  datasets: [
    {
      label: '저축금리',
      backgroundColor: '#2699E6',
      data: savingRates.value
    },
  ]    
}))

</script>

<style scoped>
.charts {
  width: 500px;
  height: 300px;
  margin: auto;
  /* display: flex;
  justify-content: center;
  align-content: center; */
}
</style>
