import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import '@/assets/css/bootstrap.min.css';
import '@/assets/css/fontawesome.min.css';
import '@/assets/js/bootstrap.bundle.min.js';

window.process = {
  env: {
    NODE_ENV: 'development'
  }
}

const app = createApp(App);
app.use(router);
app.mount('#app');
