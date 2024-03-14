<!-- 剧本 -->

<template>
    <div style="margin-top:10px;">
        <label for="hs-select-label" class="block text-sm font-medium mb-2 dark:text-white">请选择你的模型</label>
        <select id="hs-select-label" class="py-3 px-4 pe-9 block w-4/5 border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600">
            <option selected>模型列表</option>
            <option v-for="data in tableData">{{ data.date }}</option>
        </select>
    </div>
    <div style="margin-top:10px;">
        <label for="hs-select-label" class="block text-sm font-medium mb-2 dark:text-white">请选择你的数据</label>
        <select id="hs-select-label" class="py-3 px-4 pe-9 block w-4/5 border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600">
            <option selected>数据列表</option>
            <option v-for="data in tableData">{{ data.date }}</option>
        </select>
    </div>
    <div style="margin-top:10px;">
        <button type="button" 
                class="py-3 px-4 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-100 text-blue-800 hover:bg-blue-200 disabled:opacity-50 disabled:pointer-events-none dark:hover:bg-blue-800 dark:text-green-500 dark:hover:text-green-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
                @click="start_clean">
                开始生成
        </button>
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
</style>