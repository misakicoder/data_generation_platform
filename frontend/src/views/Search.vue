<template>
</template>

<script lang="ts" setup>
import axios from "axios";
import { onMounted, ref } from 'vue';
import { IMovieStyle, IMovieType } from "@/type";

let movies = ref([]);

//获取管理员审核推荐作品（recommend）
const get_movies = (movie_type: IMovieType, movie_style: IMovieStyle) => {
  axios.get('/api/search/movies', {
    params: {
      movie_type: movie_type,
      movie_style: movie_style,
      keyword: ""
    }
  }).then((res) => {
    movies.value = res.data['movies'];
    console.log("get movies success")
  }).catch(() => {
    console.log("get movies failed")
  })
};

onMounted(async () => {
  const movie_type = "剧情片"
  const movie_style = "古风"
  await get_movies(movie_type, movie_style)
})
</script>