<template>
    <Navbar></Navbar>

    <div class="max-w-2xl m-auto pt-24">
        <RouterLink to="/community">
            <div
                class="inline-flex items-center gap-x-1 text-sm text-neutral-800 hover:text-violet-500 dark:text-neutral-200 dark:hover:text-violet-400">
                <i class="ti ti-chevron-left"></i>
                上一页
            </div>
        </RouterLink>

        <div class="flex justify-between items-center my-6">
            <div class="flex w-full sm:items-center gap-x-5 sm:gap-x-3">
                <div class="flex-shrink-0">
                    <img class="size-12 rounded-full" :src="movie_info.user_avatar" alt="Image Description">
                </div>

                <div class="grow">
                    <div class="flex justify-between items-center gap-x-2">
                        <div>
                            <div class="hs-tooltip inline-block [--trigger:hover] [--placement:bottom]">
                                <div class="hs-tooltip-toggle sm:mb-1 block text-start cursor-pointer">
                                    <span class="font-semibold text-neutral-800 dark:text-neutral-200">
                                        {{ movie_info.user_name }}
                                    </span>
                                </div>
                            </div>

                            <ul class="text-xs text-neutral-500">
                                <li
                                    class="inline-block relative pe-6 last:pe-0 last-of-type:before:hidden before:absolute before:top-1/2 before:end-2 before:-translate-y-1/2 before:size-1 before:bg-neutral-300 before:rounded-full dark:text-neutral-400 dark:before:bg-neutral-600">
                                    {{ movie_info.publish_day }}
                                </li>
                            </ul>
                        </div>

                        <!-- <div>
                            <button type="button"
                                class="py-1.5 px-2.5 inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border border-neutral-200 bg-white text-neutral-800 shadow-sm hover:bg-neutral-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-white dark:hover:bg-neutral-800 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600">
                                <i class="ti ti-user-plus"></i>
                                关注
                            </button>
                        </div> -->
                    </div>
                </div>
            </div>
        </div>
        <!-- End Avatar Media -->

        <!-- Content -->
        <div class="space-y-5 md:space-y-8">
            <div class="rounded-xl overflow-hidden my-12">
                <video controls class="w-full rounded-xl">
                    <source :src="movie_info.movie_url" type="video/mp4">
                    Your browser does not support HTML5 video.
                </video>
            </div>

            <p class="leading-loose text-neutral-800 dark:text-neutral-200 text-pretty">
                {{ movie_info.story }}</p>

            <div>
                <template v-for="tag in movie_info.tags">
                    <a
                        class="m-1 inline-flex items-center gap-1.5 py-2 px-3 rounded-full text-sm bg-neutral-100 text-neutral-800 hover:bg-   -200 dark:bg-neutral-800 dark:hover:bg-neutral-700 dark:text-neutral-200 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600">
                        {{ tag }}
                    </a>
                </template>
            </div>
        </div>
        <!-- End Content -->
    </div>

    <div class="sticky bottom-6 inset-x-0 text-center">
        <div class="inline-block bg-white shadow-md rounded-full py-3 px-4 dark:bg-neutral-800">
            <div class="flex items-center gap-x-1.5">
                <!-- Button -->
                <div class="hs-tooltip inline-block">
                    <button type="button"
                        class="hs-tooltip-toggle flex items-center gap-x-2 text-sm text-neutral-500 hover:text-neutral-800 dark:text-neutral-400 dark:hover:text-neutral-200 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600">
                        <i class="ti ti-heart"></i>
                        {{ movie_info.like_num }}
                        <span
                            class="hs-tooltip-content hs-tooltip-shown:opacity-100 hs-tooltip-shown:visible opacity-0 transition-opacity inline-block absolute invisible z-10 py-1 px-2 bg-neutral-900 text-xs font-medium text-white rounded shadow-sm dark:bg-black"
                            role="tooltip">
                            喜欢
                        </span>
                    </button>
                </div>
                <!-- Button -->

                <!-- <div class="block h-3 border-e border-neutral-300 mx-3 dark:border-neutral-600"></div> -->

                <!-- Button -->
                <!-- <div class="hs-tooltip inline-block">
                    <button type="button"
                        class="hs-tooltip-toggle flex items-center gap-x-2 text-sm text-neutral-500 hover:text-neutral-800 dark:text-neutral-400 dark:hover:text-neutral-200 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600">
                        <i class="ti ti-message"></i>
                        16
                        <span
                            class="hs-tooltip-content hs-tooltip-shown:opacity-100 hs-tooltip-shown:visible opacity-0 transition-opacity inline-block absolute invisible z-10 py-1 px-2 bg-neutral-900 text-xs font-medium text-white rounded shadow-sm dark:bg-black"
                            role="tooltip">
                            评论
                        </span>
                    </button>
                </div> -->
                <!-- Button -->

                <div class="block h-3 border-e border-neutral-300 mx-3 dark:border-neutral-600"></div>

                <!-- Button -->
                <div class="hs-dropdown relative inline-flex">
                    <button type="button" id="blog-article-share-dropdown"
                        class="hs-dropdown-toggle flex items-center gap-x-2 text-sm text-neutral-500 hover:text-neutral-800 dark:text-neutral-400 dark:hover:text-neutral-200 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600">
                        <i class="ti ti-share-2"></i>
                        分享
                    </button>
                    <div class="hs-dropdown-menu w-56 transition-[opacity,margin] duration hs-dropdown-open:opacity-100 opacity-0 hidden mb-1 z-10 bg-neutral-900 shadow-md rounded-xl p-2 dark:bg-black"
                        aria-labelledby="blog-article-share-dropdown">
                        <a
                            class="flex items-center gap-x-3.5 py-2 px-3 rounded-lg text-sm text-neutral-400 hover:bg-white/10 focus:outline-none focus:ring-2 focus:ring-neutral-400">
                            <i class="ti ti-link"></i>
                            复制链接
                        </a>
                    </div>
                </div>
                <!-- Button -->
            </div>
        </div>
    </div>

    <div class="max-w-2xl m-auto my-12">
        <div class="my-4 text font-extrabold dark:text-neutral-100">猜你喜欢</div>

        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
            <div v-for=" recommend_movie  in  recommend_movies " class="relative">
                <RouterLink :to="'/movie/' + recommend_movie.id">
                    <div
                        class="relative flex flex-col w-full  h-fit bg-center bg-cover rounded-xl overflow-hidden hover:shadow-lg transition dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 hover:scale-105 duration-200 cursor-pointer shadow-sm">
                        <img :src="recommend_movie.cover" alt="" srcset="" class="w-full">
                        <div class=" bottom-0 absolute w-full p-4 bg-gradient-to-t from-black to-transparent">
                            <h3 class="text-lg text-white/[.9] group-hover:text-white font-bold my-2">{{
                        recommend_movie.name }}
                            </h3>
                            <div class="flex justify-between items-center">
                                <div class="flex w-full sm:items-center gap-x-5 sm:gap-x-3">
                                    <img class="size-4 rounded-full" :src="recommend_movie.user_avatar"
                                        alt="Image Description">
                                    <span class="font-semibold text-xs text-neutral-200 ">
                                        {{ recommend_movie.user_name }}
                                    </span>
                                    <span class=" text-neutral-200 text-xs  ml-auto">
                                        {{ recommend_movie.publish_day }}
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
import Footer from '@/components/Common/Footer.vue';
import Navbar from '@/components/Common/Navbar.vue';
import { reactive } from 'vue';

const example_video_list = [
    "https://filmaction.s3.us-west-2.amazonaws.com/LincolnCar.mov",
    "https://filmaction.s3.us-west-2.amazonaws.com/perfume.mp4"
]
// random video
const example_video = example_video_list[Math.floor(Math.random() * example_video_list.length)]

const movie_info = reactive({
    user_name: "小李",
    user_avatar: "https://plus.unsplash.com/premium_photo-1670006626745-ccaf6151cb2a?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8",
    publish_day: "2023.12.29",
    movie_url: example_video,
    story: " 在一个风雨交加的夜晚，退休侦探约翰在家中翻阅旧案件档案，试图寻找多年前未解之谜的线索。他的目光停留在一张泛黄的照片上，那是他年轻时与搭档艾米丽的合影，两人正站在一起庆祝解决的一个大案。然而，艾米丽在一次调查中神秘失踪，案件至今悬而未决。约翰的手指轻轻滑过照片，心中涌起一股复杂的情感。他决定重新开启这个尘封的案件，希望能找到艾米丽的下落，为这段未了的过去画上句号。随着调查的深入，约翰逐渐揭开了一个涉及高层权力、贪婪与背叛的阴谋，而真相远比他想象的更加扑朔迷离。",
    tags: ["剧情片", "现代"],
    like_num: 999
})

const recommend_movies = [
    {
        name: "下山啦",
        cover: "https://images.unsplash.com/photo-1708802844519-6d46be069851?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHx0b3BpYy1mZWVkfDV8aG1lbnZRaFVteE18fGVufDB8fHx8fA%3D%3D",
        id: "123",
        user_name: "李",
        publish_day: "2023.12.31",
        user_avatar: "https://plus.unsplash.com/premium_photo-1670006626745-ccaf6151cb2a?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8"
    },
    {
        name: "哦莫，集装箱",
        cover: "https://images.unsplash.com/photo-1708715812650-48b7eb25b303?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHx0b3BpYy1mZWVkfDEwfGhtZW52UWhVbXhNfHxlbnwwfHx8fHw%3D",
        id: "123",
        user_name: "李",
        publish_day: "2023.12.31",
        user_avatar: "https://plus.unsplash.com/premium_photo-1670006626745-ccaf6151cb2a?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8"
    },
    {
        name: "盛开的鲜花",
        cover: "https://images.unsplash.com/photo-1708094101137-e928ca5d4292?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHx0b3BpYy1mZWVkfDE2fGhtZW52UWhVbXhNfHxlbnwwfHx8fHw%3D",
        id: "123",
        user_name: "李",
        publish_day: "2023.12.31",
        user_avatar: "https://plus.unsplash.com/premium_photo-1670006626745-ccaf6151cb2a?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8"
    },
    {
        name: "兰兰天",
        cover: "https://images.unsplash.com/photo-1708619274103-73baf7d44c4c?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHx0b3BpYy1mZWVkfDMwfGhtZW52UWhVbXhNfHxlbnwwfHx8fHw%3D",
        id: "123",
        user_name: "李",
        publish_day: "2023.12.31",
        user_avatar: "https://plus.unsplash.com/premium_photo-1670006626745-ccaf6151cb2a?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8"
    },
    {
        name: "刺猬",
        cover: "https://images.unsplash.com/photo-1708616204690-ca98326191b4?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHx0b3BpYy1mZWVkfDMxfGhtZW52UWhVbXhNfHxlbnwwfHx8fHw%3D",
        id: "123",
        user_name: "李",
        publish_day: "2023.12.31",
        user_avatar: "https://plus.unsplash.com/premium_photo-1670006626745-ccaf6151cb2a?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8"
    },
    {
        name: "吃货你才是",
        cover: "https://images.unsplash.com/photo-1708380649843-8d0c75ecf3b7?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHx0b3BpYy1mZWVkfDM3fGhtZW52UWhVbXhNfHxlbnwwfHx8fHw%3D",
        id: "123",
        user_name: "李",
        publish_day: "2023.12.31",
        user_avatar: "https://plus.unsplash.com/premium_photo-1670006626745-ccaf6151cb2a?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8"
    },
]
</script>