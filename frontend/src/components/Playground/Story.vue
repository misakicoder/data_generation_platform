<!-- 剧本 -->
<template>
    <div
        class="h-full flex justify-center items-center border border-dashed border-neutral-200 dark:border-neutral-700 rounded-xl overflow-hidden">
        <!-- Textarea -->
        <div class="relative w-full" v-if="current_task.story">
            <textarea id="hs-textarea-ex-1"
                class="p-4 pb-12 block w-full border-neutral-200 rounded-lg text-sm focus:border-violet-500 focus:ring-violet-500 disabled:opacity-50 disabled:pointer-events-none  dark:border-neutral-700 dark:text-neutral-400 dark:focus:ring-neutral-600 outline-none text-pretty leading-6"
                rows="12" placeholder="正在生成中，请稍等……" v-model="current_task.story" @blur="modify_story"></textarea>

            <!-- Toolbar -->
            <div class="absolute bottom-px inset-x-px p-2 rounded-b-md bg-white dark:bg-neutral-900">
                <div class="flex justify-between items-center">
                    <!-- Button Group -->
                    <div class="flex items-center">
                        <!-- Mic Button -->
                        <button type="button"
                            class="inline-flex flex-shrink-0 justify-center items-center h-8 rounded-lg text-neutral-500 hover:text-violet-500 focus:z-10 focus:outline-none focus:ring-2 focus:ring-violet-400 dark:hover:text-violet-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 text-sm"
                            @click="regenerate_story">
                            <i class="ti ti-rotate-clockwise mr-2"></i>
                            重新生成
                        </button>
                        <!-- End Mic Button -->
                    </div>
                    <!-- End Button Group -->

                    <!-- Button Group -->
                    <div class="flex items-center gap-x-1">
                        <!-- Send Button -->
                        <button type="button"
                            class="inline-flex flex-shrink-0 justify-center items-center h-8 text-sm px-2 rounded-lg text-white bg-violet-500 hover:bg-violet-400 focus:z-10 focus:outline-none focus:ring-2 focus:ring-violet-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600"
                            @click="generate_scripts">
                            <i class="ti ti-dual-screen mr-2"></i>生成分镜脚本
                        </button>
                        <!-- End Send Button -->
                    </div>
                    <!-- End Button Group -->
                </div>
            </div>
            <!-- End Toolbar -->
        </div>
        <!-- End Textarea -->

        <div class="flex flex-col w-full" v-else>
            <div class="flex animate-pulse w-full p-4">
                <div class="w-full">
                    <ul class="space-y-3">
                        <li class="w-full h-2 bg-neutral-200 rounded-full dark:bg-neutral-700" v-for="_i in 14"></li>
                        <li class="w-1/2 h-2 bg-neutral-200 rounded-full dark:bg-neutral-700"></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { current_task, update_current_task } from '@/util/task';
import axios from 'axios';
import { onMounted } from 'vue';

onMounted(() => {
    setTimeout(() => {
        get_story()
    }, 100);
})

const generate_scripts = () => {
    current_task.value.status = 'pending'
    axios.put('/api/scripts/', { task_id: current_task.value.task_id }).then(_res => {
        update_current_task()
    })
}

const get_story = () => {
    current_task.value.status = 'pending'
    axios.get('/api/story/', { params: { task_id: current_task.value.task_id } }).then(res => {
        let story = res.data.story
        story.replace(/\"/g, '')
        story = story.replace(/\\n/g, '\n')
        current_task.value.story = story

        if (current_task.value.story == "") {
            regenerate_story()
        }
        else {
            current_task.value.status = 'ready'
        }
    })
}

const regenerate_story = () => {
    current_task.value.story = ""
    axios.put('/api/story/', { task_id: current_task.value.task_id }).then(_res => {
        update_current_task()
    })
}

const modify_story = () => {
    axios.post('/api/story/', { task_id: current_task.value.task_id, story: current_task.value.story }).then(_res => {
        get_story()
    })
}
</script>