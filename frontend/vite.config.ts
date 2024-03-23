import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      "/api": {
        // hack: 服务器
        // target: "http://0.0.0.0:8000/",
        // 本地
        target: "http://127.0.0.1:8000/",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
  // add @ to alias
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),
    },
  },
});
