import { createApp } from 'vue'
import './style.css'
import router from './router'
import { createPinia } from 'pinia';
import ToastPlugin from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-default.css';
import App from './App.vue'

const app = createApp(App);
const pinia = createPinia();

app.use(router);
app.use(pinia);
app.use(ToastPlugin);
app.mount('#app');
