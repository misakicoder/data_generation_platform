<!-- 剧本 -->

<template>
    <div class="flex gap-4">
        <button type="button" 
            class="py-3 px-4 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-pink-100 text-pink-800 hover:bg-pink-200 disabled:opacity-50 disabled:pointer-events-none dark:hover:bg-pink-900 dark:text-pink-500 dark:hover:text-pink-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
            @click="start_clean">
            开始标注
        </button>
        <button type="button" 
            class="py-3 px-4 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-pink-100 text-pink-800 hover:bg-pink-200 disabled:opacity-50 disabled:pointer-events-none dark:hover:bg-pink-900 dark:text-pink-500 dark:hover:text-pink-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
            @click="start_clean">
            下一条
        </button>
    </div>
    <div
            class="py-3 flex items-center text-sm text-neutral-800 before:flex-[1_1_0%] before:border-t before:border-neutral-200 before:me-6 after:flex-[1_1_0%] after:border-t after:border-neutral-200 after:ms-6 dark:text-white dark:before:border-neutral-600 dark:after:border-neutral-600"
            v-if="cleaned_or_not"
            >
            需要标注的数据
    </div>
    <el-table :data="tableData" style="width: 100%" v-if="cleaned_or_not">
        <el-table-column v-for="(value, key) in tableData[0]" :key="key" :prop="key" :label="key" width="180" />
    </el-table>
    <div class="py-3 flex items-center text-sm text-neutral-800 before:flex-[1_1_0%] before:border-t before:border-neutral-200 before:me-6 after:flex-[1_1_0%] after:border-t after:border-neutral-200 after:ms-6 dark:text-white dark:before:border-neutral-600 dark:after:border-neutral-600" v-if="cleaned_or_not">
        <input type="text" class="py-2 px-3 block w-4/5 border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600" style="color: white;" placeholder="请输入你的标注信息">
        <div style="margin-left: 10px;"> <!-- 加大距离的地方 -->
            <button type="button" class="py-0.8 px-3 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-pink-100 text-pink-800 hover:bg-pink-200 disabled:opacity-50 disabled:pointer-events-none dark:hover:bg-pink-900 dark:text-pink-500 dark:hover:text-pink-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" @click="start_clean">
                提交
            </button>
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
        name: 'Mike',
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