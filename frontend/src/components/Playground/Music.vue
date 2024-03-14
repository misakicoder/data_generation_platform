<template>
    <div>
        <div
            class="h-full flex justify-center items-center border border-dashed border-neutral-200 dark:border-neutral-700 rounded-xl overflow-hidden">

            <!-- Textarea -->
            <div class="relative w-full" v-if="current_task.music_description_zh">
                <textarea id="hs-textarea-ex-1"
                    class="p-4 pb-12 block w-full rounded-lg text-sm focus:border-violet-500 focus:ring-violet-500 disabled:opacity-50 disabled:pointer-events-none  dark:border-neutral-700 dark:text-neutral-400 dark:focus:ring-neutral-600 outline-none text-pretty leading-6"
                    placeholder="音乐描述" v-model="current_task.music_description_zh" @blur="update_music_description_zh"
                    rows="5"></textarea>

                <!-- Toolbar -->
                <div class="absolute bottom-px inset-x-px p-2 rounded-b-md bg-white dark:bg-neutral-900">
                    <div class="flex justify-between items-center">
                        <div class="flex items-center">
                            <button type="button"
                                class="inline-flex flex-shrink-0 justify-center items-center h-8 rounded-lg text-neutral-500 hover:text-violet-500 focus:z-10 focus:outline-none focus:ring-2 focus:ring-violet-400 dark:hover:text-violet-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 text-sm"
                                @click="regenerate_music_description">
                                <i class="ti ti-rotate-clockwise mr-2"></i>
                                重新生成
                            </button>
                        </div>
                    </div>
                </div>
                <!-- End Toolbar -->
            </div>
            <!-- End Textarea -->
            <div class="flex flex-col w-full" v-else>
                <div class="flex animate-pulse w-full p-4">
                    <div class="w-full">
                        <ul class="space-y-3">
                            <li class="w-full h-2 bg-neutral-200 rounded-full dark:bg-neutral-700"></li>
                            <li class="w-full h-2 bg-neutral-200 rounded-full dark:bg-neutral-700"></li>
                            <li class="w-full inline-flex flex-row justify-between items-center">
                                <div class="w-5/12 h-2 bg-neutral-200 rounded-full dark:bg-neutral-700"></div>
                                <span
                                    class="text-xs cursor-pointer hover:scale-105 text-neutral-500 dark:text-neutral-200"
                                    @click="regenerate_music_description"><i class="ti ti-music"></i> 生成配乐描述</span>
                                <div class="w-5/12 h-2 bg-neutral-200 rounded-full dark:bg-neutral-700"></div>
                            </li>
                            <li class="w-full h-2 bg-neutral-200 rounded-full dark:bg-neutral-700"></li>
                            <li class="w-1/2 h-2 bg-neutral-200 rounded-full dark:bg-neutral-700"></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="mt-8">
            <div class="relative w-full flex items-center p-2 space-x-2" v-if="current_task.music">
                <audio controls class="flex-1 h-8">
                    <source :src="s3_music_path + current_task.music" type="audio/mpeg" />
                </audio>

                <button type="button"
                    class="inline-flex flex-shrink-0 justify-center items-center h-8 px-2 bg-white dark:bg-neutral-600 rounded-lg text-neutral-500 hover:text-violet-600 focus:z-10 focus:outline-none focus:ring-2 focus:ring-violet-500 dark:hover:text-violet-500 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600"
                    @click="regenerate_music">
                    <i class="ti ti-rotate-clockwise mr-2"></i>
                    <span class="text-sm"> 重新生成</span>
                </button>
            </div>
            <div class="flex flex-col" v-else>
                <div class="flex animate-pulse w-full">
                    <div
                        class="w-full h-28 flex flex-col  border shadow-sm rounded-xl dark:border-neutral-700 dark:shadow-neutral-700/[.7] bg-neutral-50  dark:bg-neutral-700">
                        <button
                            class="flex flex-auto flex-col justify-center items-center p-4 md:p-5 text-neutral-500 dark:text-neutral-200"
                            @click="regenerate_music" :disabled="!current_task.music_description_zh"
                            :class="{ 'hover:scale-105 cursor-pointer': current_task.music_description_zh }">
                            <i class="ti ti-vinyl text-xl"></i>
                            <span class="text-xs">生成配乐</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import axios from 'axios';
import { onMounted } from 'vue';
import { current_task, update_current_task } from "@/util/task";
import { s3_music_path } from '@/util/api';

onMounted(() => {
    setTimeout(() => {
        get_music_description()
        get_music()
    }, 100);
})

const get_music_description = () => {
    axios.get('/api/music_description/', { params: { task_id: current_task.value.task_id } }).then(res => {
        current_task.value.music_description_zh = res.data.music_description_zh
    })
}

const regenerate_music_description = () => {
    current_task.value.music_description_zh = ""
    axios.put('/api/music_description/', { task_id: current_task.value.task_id }).then(_res => {
        update_current_task()
    })
}

const update_music_description_zh = () => {
    axios.post('/api/music_description/', { task_id: current_task.value.task_id, music_description_zh: current_task.value.music_description_zh }).then(_res => {
        get_music_description()
    })
}

const get_music = () => {
    axios.get('/api/music/', { params: { task_id: current_task.value.task_id } }).then(res => {
        current_task.value.music = res.data.music
    })
}

const regenerate_music = () => {
    if (current_task.value.music_description_zh == "")
        return

    current_task.value.music = ""
    axios.put('/api/music/', { task_id: current_task.value.task_id }).then(_res => {
        update_current_task()
    })
}
</script>