<!-- 剧本 -->

<template>
<div class="flex gap-4">
    <div v-for="(algo, index) in algorithms" :key="index">
        <div class="flex flex-col bg-white border border-t-4 border-t-blue-600 shadow-sm rounded-xl dark:bg-slate-900 dark:border-gray-700 dark:border-t-blue-500 dark:shadow-slate-700/[.7]">
            <div class="p-4 md:p-5">
                <h3 class="text-lg font-bold text-gray-800 dark:text-white">
                {{ algo }}
                </h3>
                <p class="mt-2 text-gray-500 dark:text-gray-400">
                With supporting text below as a natural lead-in to additional content.
                </p>
                <a class="mt-3 inline-flex items-center gap-x-1 text-sm font-semibold rounded-lg border border-transparent text-blue-600 hover:text-blue-800 disabled:opacity-50 disabled:pointer-events-none dark:text-blue-500 dark:hover:text-blue-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" href="#" @click="handleClick">
                    Card link
                </a>
            </div>
        </div>
    </div>
</div>
</template>

<script lang="ts" setup>
import { UploadFilled } from '@element-plus/icons-vue'
import { current_task, update_current_task } from '@/util/task';
import axios from 'axios';
import { onMounted } from 'vue';

const algorithms: string[] = ['Algorithm 1', 'Algorithm 2', 'Algorithm 3'];

const handleClick = () => {
    alert("点击了")
}
// onMounted(() => {
//     setTimeout(() => {
//         get_story()
//     }, 100);
// })

// const generate_scripts = () => {
//     current_task.value.status = 'pending'
//     axios.put('/api/scripts/', { task_id: current_task.value.task_id }).then(_res => {
//         update_current_task()
//     })
// }

// const get_story = () => {
//     current_task.value.status = 'pending'
//     axios.get('/api/story/', { params: { task_id: current_task.value.task_id } }).then(res => {
//         let story = res.data.story
//         story.replace(/\"/g, '')
//         story = story.replace(/\\n/g, '\n')
//         current_task.value.story = story

//         if (current_task.value.story == "") {
//             regenerate_story()
//         }
//         else {
//             current_task.value.status = 'ready'
//         }
//     })
// }

// const regenerate_story = () => {
//     current_task.value.story = ""
//     axios.put('/api/story/', { task_id: current_task.value.task_id }).then(_res => {
//         update_current_task()
//     })
// }

// const modify_story = () => {
//     axios.post('/api/story/', { task_id: current_task.value.task_id, story: current_task.value.story }).then(_res => {
//         get_story()
//     })
// }
</script>

<style scoped>
  .card-container {
    display: flex;
    flex-wrap: nowrap;
  }
  .card {
    width: 200px;
    height: 300px;
    margin-right: 10px;
  }
</style>