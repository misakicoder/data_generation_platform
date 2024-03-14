<template>
  <Navbar></Navbar>
  <div class="p-8 pt-24 max-w-7xl m-auto">
    <div class="my-12 text-2xl font-extrabold dark:text-neutral-100">最热榜</div>
    <div class="grid sm:grid-cols-1 lg:grid-cols-2 grid-flow-dense gap-8">
      <div class="relative" v-for="trending_movie in trending_movies">
        <RouterLink :to="'/movie/' + trending_movie.id">
          <div
            class="relative flex flex-col w-full h-fit bg-center bg-cover rounded-xl overflow-hidden hover:shadow-lg transition dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 hover:scale-105 duration-200 cursor-pointer shadow-lg">
            <img :src="trending_movie.cover" alt="" srcset="" class="w-full" />
            <div class="bottom-0 absolute w-full p-6 bg-gradient-to-t from-black to-transparent">
              <h3 class="text-2xl text-white/[.9] group-hover:text-white font-bold my-4">
                {{ trending_movie.name }}
              </h3>
              <div class="flex justify-between items-center">
                <div class="flex w-full sm:items-center gap-x-5 sm:gap-x-3">
                  <img class="size-8 rounded-full" :src="trending_movie.user_avatar" alt="Image Description" />
                  <span class="font-semibold text-sm text-neutral-200">
                    {{ trending_movie.user_name }}
                  </span>
                  <span class="text-neutral-200 text-sm ml-auto">
                    {{ trending_movie.publish_day }}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </RouterLink>
      </div>
    </div>

    <div class="my-12 text-2xl font-extrabold dark:text-neutral-100">最新榜</div>
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="latest_movie in latest_movies" class="relative">
        <RouterLink :to="'/movie/' + latest_movie.id">
          <div
            class="relative flex flex-col w-full h-fit bg-center bg-cover rounded-xl overflow-hidden hover:shadow-lg transition dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 hover:scale-105 duration-200 cursor-pointer shadow-sm">
            <img :src="latest_movie.cover" alt="" srcset="" class="w-full" />
            <div class="bottom-0 absolute w-full p-4 bg-gradient-to-t from-black to-transparent">
              <h3 class="text-lg text-white/[.9] group-hover:text-white font-bold my-2">
                {{ latest_movie.name }}
              </h3>
              <div class="flex justify-between items-center">
                <div class="flex w-full sm:items-center gap-x-5 sm:gap-x-3">
                  <img class="size-6 rounded-full" :src="latest_movie.user_avatar" alt="Image Description" />
                  <span class="font-semibold text-xs text-neutral-200">
                    {{ latest_movie.user_name }}
                  </span>
                  <span class="text-neutral-200 text-xs ml-auto">
                    {{ latest_movie.publish_day }}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </RouterLink>
      </div>
    </div>
  </div>
  <Footer></Footer>
</template>

<script lang="ts" setup>
import Footer from "@/components/Common/Footer.vue";
import Navbar from "@/components/Common/Navbar.vue";
import axios from "axios";
import { onMounted, ref } from 'vue';
import { IMovieStyle, IMovieType } from "@/type";

interface IMovie {
  id: string
  cover: string
  name: string
  user_avatar: string
  user_name: string
  publish_day: string
}
let trending_movies = ref<IMovie[]>([]);
let latest_movies = ref<IMovie[]>([]);

//获取管理员审核推荐作品（recommend）
const get_trending_movies = async (num: number, movie_type: IMovieType, movie_style: IMovieStyle) => {
  axios.get('/api/community/recommend', {
    params: {
      num: num,
      movie_type: movie_type,
      movie_style: movie_style
    }
  }).then((res) => {
    trending_movies.value = res.data['movies'];
  })
};

//获取最新作品
const get_latest_movies = async (num: number, movie_type: IMovieType, movie_style: IMovieStyle) => {
  axios.get('/api/community/latest', {
    params: {
      num: num,
      movie_type: movie_type,
      movie_style: movie_style
    }
  }).then(res => {
    latest_movies.value = res.data['movies'];
  })
};


onMounted(async () => {
  get_latest_movies(2, "", "")
  get_trending_movies(8, "", "")
})
</script>
