<!-- 剧本 -->

<template>
    <div style="margin-top:10px;margin-bottom:20px;">
        <label for="hs-select-label" class="block text-sm font-medium mb-2 dark:text-white">请选择你要清洗的数据</label>
        <select id="hs-select-label" class="py-3 px-4 pe-9 block w-4/5 border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
            @click="selectData" v-model="selected_ori_data">
            <option value="" disabled selected>原始数据列表</option>
            <option v-for="data in ori_datas" :value="data">{{ data.data_type + " : "+data.data_description}}</option>
        </select>
    </div>
    <div style="margin-top:12px;" v-if="selected_ori_data">
        <label for="hs-select-label" class="block text-sm font-medium mb-2 dark:text-white">请选择你想要删除的列数(保留时序数据特征)</label>
        <div class="flex flex-wrap" style="gap: 10px;">
            <div class="relative flex items-start" v-for="data in selected_deleted_cols">
                <div class="flex items-center h-5 mt-1">
                    <input id="hs-checkbox-delete" name="hs-checkbox-delete" type="checkbox" class="border-gray-200 rounded text-blue-600 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-gray-800 dark:border-gray-700 dark:checked:bg-blue-500 dark:checked:border-blue-500 dark:focus:ring-offset-gray-800" aria-describedby="hs-checkbox-delete-description"  v-model="checked_columns" :value="data">
                </div>
                <label for="hs-checkbox-delete" class="ms-3">
                    <span class="block text-sm font-semibold text-gray-800 dark:text-gray-300">{{ data }}</span>
                </label>
            </div>
        </div>
    </div>
    <div style="margin-top:10px; width: 50%;" v-if="selected_ori_data">
            <label for="hs-select-label" class="block text-sm font-medium mb-2 dark:text-white">时间顺序</label>
            <select id="hs-select-label" class="py-3 px-4 pe-9 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
                v-model="selected_is_reverse">
                <option value="" disabled selected>请选择时间顺序</option>
                <option v-for="(item, index) in is_reverse" :value="Object.values(item)[0]" :key="index">
                    {{ Object.keys(item)[0] }}
                </option>
            </select>
        </div>
    <div class="flex gap-4 mt-4" v-if="selected_ori_data">
        <button type="button" 
            class="py-3 px-4 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-teal-100 text-teal-800 hover:bg-teal-200 disabled:opacity-50 disabled:pointer-events-none dark:hover:bg-teal-900 dark:text-teal-500 dark:hover:text-teal-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
            @click="start_clean" >
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
import { pa } from 'element-plus/es/locale';
const cleaned_or_not = ref(false)

const ori_datas = ref<Array<{[key: string]: any}>>([])
const selected_ori_data = ref('')
const selected_deleted_cols = ref('')
const selected_is_reverse = ref('')
const is_reverse = ref([{'从旧到新':false}, {'从新到旧':true}])
const checked_columns= ref([])

const selectData = () => {
    axios.get('/api/ori_data/',{ params: { task_type: current_task.value.task_type }}).then(res => {
        if(res.data.ori_datas.length == 0){
            ori_datas.value = []
            alert("没有原始数据,请先上传数据")
        }
        Object.assign(ori_datas.value, res.data.ori_datas)
        selectDeletedCols()
    })
}

const selectDeletedCols = () => {
    axios.get('/api/data_cols/',{ params: { task_type: current_task.value.task_type,data_id: selected_ori_data.value.data_id}}).then(res => {
        if(res.data.data_cols.length == 0){
            ori_datas.value = []
            alert("取列数失败")
        }
        selected_deleted_cols.value = res.data.data_cols.split(',')
    })
}


const start_clean = () => {
    axios.post('/api/cleaned_data/', {algorithm : current_task.value.task_algorithm,ori_data: selected_ori_data.value,del_cols:checked_columns.value,is_reverse:selected_is_reverse.value }).then(res => {
        alert(res.data.message)
    })
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