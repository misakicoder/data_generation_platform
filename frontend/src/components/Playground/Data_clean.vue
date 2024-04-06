<!-- 剧本 -->

<template>
    <div style="margin-top:10px;">
        <label for="hs-select-label" class="block text-sm font-medium mb-2 dark:text-white">请选择你要清洗的数据</label>
        <select id="hs-select-label" class="py-3 px-4 pe-9 block w-4/5 border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
            @click="selectData">
            <option selected>原始数据列表</option>
            <option v-for="data in ori_datas">{{ data.data_description + data.data_id}}</option>
        </select>
    </div>
    <div class="flex gap-4 mt-4">
        <button type="button" 
            class="py-3 px-4 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-teal-100 text-teal-800 hover:bg-teal-200 disabled:opacity-50 disabled:pointer-events-none dark:hover:bg-teal-900 dark:text-teal-500 dark:hover:text-teal-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
            @click="start_clean">
            开始清洗
        </button>
    </div>
    <!-- <div
            class="py-3 flex items-center text-sm text-neutral-800 before:flex-[1_1_0%] before:border-t before:border-neutral-200 before:me-6 after:flex-[1_1_0%] after:border-t after:border-neutral-200 after:ms-6 dark:text-white dark:before:border-neutral-600 dark:after:border-neutral-600">
            清洗前数据
    </div> -->
    <!-- <el-table :data="tableData" style="width: 100%">
        <el-table-column v-for="(value, key) in tableData[0]" :key="key" :prop="key" :label="key" width="180" />
    </el-table> -->
    <!-- <div class="py-3 flex items-center text-sm text-neutral-800 before:flex-[1_1_0%] before:border-t before:border-neutral-200 before:me-6 after:flex-[1_1_0%] after:border-t after:border-neutral-200 after:ms-6 dark:text-white dark:before:border-neutral-600 dark:after:border-neutral-600"
        v-if="cleaned_or_not">
            
            清洗后数据
    </div >
    <el-table :data="tableData" style="width: 100%" v-if="cleaned_or_not">
        <el-table-column v-for="(value, key) in tableData[0]" :key="key" :prop="key" :label="key" width="180" />
    </el-table> -->
</template>
    
<script lang="ts" setup>
import { UploadFilled } from '@element-plus/icons-vue'
import { current_task, update_current_task } from '@/util/task';
import axios from 'axios';
import { onMounted,ref } from 'vue';
const cleaned_or_not = ref(false)

const ori_datas = ref<Array<{[key: string]: any}>>([])

const selectData = () => {
    axios.get('/api/ori_data/').then(res => {
        Object.assign(ori_datas.value, res.data.ori_datas)
    })
}

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