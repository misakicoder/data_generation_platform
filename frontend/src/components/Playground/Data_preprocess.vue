<!-- 剧本 -->

<template>
    <div class="flex gap-4">
        <button type="button" 
            class="py-3 px-4 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-200 text-blue-800 hover:bg-blue-300 disabled:opacity-50 disabled:pointer-events-none dark:hover:bg-blue-900 dark:text-blue-500 dark:hover:text-blue-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
            @click="start_clean">
        开始预处理
        </button>
    </div>
    <div
            class="py-3 flex items-center text-sm text-neutral-800 before:flex-[1_1_0%] before:border-t before:border-neutral-200 before:me-6 after:flex-[1_1_0%] after:border-t after:border-neutral-200 after:ms-6 dark:text-white dark:before:border-neutral-600 dark:after:border-neutral-600"
            >
            执行的预处理过程
    </div>
    
    <div class="flex flex-col bg-green-200 border shadow-sm rounded-xl mb-4 dark:bg-slate-900 dark:border-gray-700 dark:shadow-slate-700/[.7]">
        <div class="p-4 md:p-5 mb-4" v-for="data in tableData" >
            <h3 class="text-lg font-bold text-gray-800 dark:text-white">
                {{ data.date }}
            </h3>
            <p class="mt-1 text-gray-500 dark:text-gray-400">
                {{ data.name }}
            </p>
            <a class="mt-2 py-2 px-3 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-green-600 text-white hover:bg-green-700 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" href="#">
                {{ data.address }}
            </a>
            <div class="separator">

            </div>
        </div>
    </div>

</template>
    
<script lang="ts" setup>
import { UploadFilled } from '@element-plus/icons-vue'
import { current_task, update_current_task } from '@/util/task';
import axios from 'axios';
import { onMounted,ref } from 'vue';
const cleaned_or_not = ref(false)

const tableData = [
    {
        date: '2016-05-03',
        name: 'Tom',
        address: 'No. 189, Grove St, Los Angeles',
    },
    {
        date: '2016-05-02',
        name: 'Tom',
        address: 'No. 189, Grove St, Los Angeles',
    },
    {
        date: '2016-05-04',
        name: 'Tom',
        address: 'No. 189, Grove St, Los Angeles',
    },
    {
        date: '2016-05-01',
        name: 'Tom',
        address: 'No. 189, Grove St, Los Angeles',
    },
]

const start_clean = () => {
    alert("点击了")
    cleaned_or_not.value = !cleaned_or_not.value
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
    .separator {
        border-top: 1px solid #ddd;
        margin: 20px 0;
    }
</style>