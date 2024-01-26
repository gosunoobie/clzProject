import { createApp } from 'vue'
import App from './App.vue'
import './assets/main.css'
import { createPinia } from 'pinia'
import router from './router'
import Notifications from '@kyvg/vue3-notification'
import VueClickAway from 'vue3-click-away'
/* import { register } from 'swiper/element/bundle' */
/* import { createHead } from '@vueuse/head' */
const app = createApp(App)
const pinia = createPinia()
/* const head = createHead() */
app.use(pinia)
/* app.use(head) */
app.use(router)
app.use(Notifications)
app.use(VueClickAway)

/* register() */
app.mount('#app')
