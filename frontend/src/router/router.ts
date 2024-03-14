import { createRouter, createWebHistory } from "vue-router";
import { type IStaticMethods } from "preline/preline";
import Home from "@/views/Home.vue";
import Playground from "@/views/Playground.vue";
import All from "@/components/Playground/All.vue";

declare global {
  interface Window {
    HSStaticMethods: IStaticMethods;
  }
}

const routes = [
  { path: "/", component: Home },
  { path: "/playground",
    component: Playground,
    children: [
    {
      path: "all",
      component: All,
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
