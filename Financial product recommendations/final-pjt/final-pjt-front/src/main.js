
import  piniaPluginPersistedstate  from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import { useKakao } from 'vue3-kakao-maps/@utils'
import "@/assets/fonts.css"
const API_KEY = import.meta.env.VITE_API_KEY
useKakao(API_KEY, ['clusterer', 'services', 'drawing'])

const pinia = createPinia()
const app = createApp(App)
pinia.use(piniaPluginPersistedstate)


// app.use(createPinia())
app.use(pinia)
app.use(router)

app.mount('#app')
