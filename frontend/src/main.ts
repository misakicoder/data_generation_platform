import { createApp } from "vue";
import App from "./App.vue";
import router from "./router/router";
import "normalize.css";
import "preline/preline";
import "./style/style.scss";
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
// import '@/mockjs/index.ts'

const app = createApp(App);
app.use(ElementPlus)
app.use(router);
app.mount("#app");
