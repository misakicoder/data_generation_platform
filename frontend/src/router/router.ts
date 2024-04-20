import { createRouter, createWebHistory } from "vue-router";
import { type IStaticMethods } from "preline/preline";
import Home from "@/views/Home.vue";
import Playground from "@/views/Playground.vue";
import All from "@/components/Playground/All.vue";
import Main from "@/components/Playground/Main.vue";
import Login from "@/views/Login.vue";
import Loading from "@/components/Playground/Loading.vue";

declare global {
  interface Window {
    HSStaticMethods: IStaticMethods;
  }
}

const routes = [
  { path: "/", component: Home },
  { path: "/login", component: Login },
  { path: "/playground",
    component: Playground,
    children: [
    {
      path: "all",
      component: All,
    },
    {
      path: "main/:id?",
      component: Main,
    },
    {
      path: "loading/:id?",
      component: Loading,
    }
  ],}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.afterEach((_to, _from, failure) => {
  if (!failure) {
    setTimeout(() => {
      window.HSStaticMethods.autoInit();
    }, 100);
  }
});

export default router;
