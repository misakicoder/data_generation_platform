<template>
    <div>
        <div v-if="current_task.movie" class="relative">
            <video controls class="w-full h-auto rounded-lg inline-block">
                <source :src="s3_movie_path + current_task.movie" type="video/mp4" />
            </video>
            <div class="absolute top-px inset-x-px p-2 rounded-b-md w-full m-auto">
                <div class="flex justify-end">
                    <!-- 重新生成 -->
                    <button type="button"
                        class="inline-flex flex-shrink-0 justify-center items-center h-8 w-8 bg-white dark:bg-neutral-600 rounded-lg text-neutral-500 hover:text-violet-600 focus:z-10 focus:outline-none focus:ring-2 focus:ring-violet-500 dark:hover:text-violet-500 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600"
                        @click="generate_movie">
                        <i class="ti ti-rotate-clockwise"></i>
                    </button>
                </div>
            </div>
        </div>

        <div class="flex animate-pulse w-full opacity-80" v-else>
            <div
                class="w-full min-h-96 flex flex-col  border shadow-sm rounded-xl dark:border-neutral-700 dark:shadow-neutral-700/[.7] bg-neutral-50  dark:bg-neutral-700">
                <div class="flex flex-auto flex-col justify-center items-center p-4 md:p-5 text-neutral-500 dark:text-neutral-200"
                    @click="generate_movie" :disabled="!movie_generation_able"
                    :class="{ 'hover:scale-105 cursor-pointer': movie_generation_able }">
                    <i class="ti ti-movie text-xl"></i>
                    <span class="text-xs">合成成片</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { current_task, update_current_task } from '@/util/task';
import { computed, onMounted } from 'vue';
import { s3_movie_path } from '@/util/api';
import axios from 'axios';

const movie_generation_able = computed(() => {
    if (current_task.value.music == "")
        return false
    if (current_task.value.videos.some((video: any) => video == ""))
        return false
    if (current_task.value.scenes.some((scene: any) => scene == ""))
        return false
    return true
})

onMounted(() => {
    setTimeout(() => {
        get_movie()
    }, 100);
})

const get_movie = () => {
    axios.get('/api/movie/', { params: { task_id: current_task.value.task_id } }).then((res) => {
        current_task.value.movie = res.data.movie
    })
}

const generate_movie = () => {
    if (current_task.value.music == "")
        return
    // 如果 current_task.value.videos 有空的，就不生成
    if (current_task.value.videos.some((video: any) => video == ""))
        return
    axios.put('/api/movie/', { task_id: current_task.value.task_id }).then(_res => {
        update_current_task()
    })
}
</script>