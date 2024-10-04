import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {

  const API_URL = 'http://70.12.102.181:8000'
  // const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const articles = ref([])
  const depositproducts = ref([])
  const savingproducts = ref([])
  const exchanges = ref([])
  const router = useRouter()
  const user = ref(null)

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  


  const signUp = function (payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2 
    axios({
      method : 'post',
      url : `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
    .then((response) => {
      const password = password1
      login({ username, password })
    })
    .catch((err) => console.log(err)) 
  }

  const login = function (payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url : `${API_URL}/accounts/login/`,
        data: {
          username, password
        } 
      }).then((response) => {
        user.value = username
        token.value = response.data.key
        router.push({ name : 'home'})
      })
      .catch((err) => console.log(err))
  }

  const logout = function () {
    axios({
      method : 'post',
      url : `${API_URL}/accounts/logout/`,

    }).then((response) => {
      token.value = null
      router.push({ name : 'home'})
    }).catch((err) => console.log(err))
  }

  const getArticles = function() {
    axios({
      method : 'get',
      url: `${API_URL}/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    }).then((response) => {
      articles.value = response.data
      console.log(response.data)
    }).catch((err) => console.log(err))
  }

  const getDepositProducts = function() {
    axios({
      method : 'get',
      url: `${API_URL}/products/deposit-products`,
    }).then((response) => {
      depositproducts.value = response.data
      console.log(response.data)
    }).catch((err) => console.log(err))
  }

  const getSavingProducts = function() {
    axios({
      method : 'get',
      url: `${API_URL}/products/saving-products`,
    }).then((response) => {
      savingproducts.value = response.data
      console.log(response.data)
    }).catch((err) => console.log(err))
  }

  const getExchanges = function() {
    axios({
      method : 'get',
      url: `${API_URL}/exchanges`,
    }).then((response) => {
      exchanges.value = response.data
    }).catch((err) => console.log(err))
  }
  

  return { articles, API_URL, signUp, login, getArticles, getDepositProducts, getSavingProducts, getExchanges, token, isLogin, exchanges, user, depositproducts, savingproducts, logout }
}, {persist : true})
