<!-- 剧本 -->

<template>
    <div style="margin-top:10px;" v-if="!data_manage.data_mark">
        <label for="hs-select-label" class="block text-sm font-medium mb-2 dark:text-white">请选择你要生成的数据</label>
        <select id="hs-select-label" class="py-3 px-4 pe-9 block w-4/5 border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
            @click="selectPreprocessedData" v-model="selected_preprocessed_data">
            <option value="" disabled selected>预处理数据列表</option>
            <option v-for="data in preprocessed_datas" :value="data">{{ data.data_type + " : "+data.data_description}}</option>
        </select>
    </div>
    <div style="margin-top:10px;" v-else>
        <label for="hs-select-label" class="block text-sm font-medium mb-2 dark:text-white">请选择你要生成的数据</label>
        <select id="hs-select-label" class="py-3 px-4 pe-9 block w-4/5 border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
            @click="selectMarkedPreprocessedData" v-model="selected_preprocessed_data">
            <option value="" disabled selected>标记的预处理数据列表</option>
            <option v-for="data in marked_processed_datas" :value="data" >{{ data.data_type + " : "+data.data_description}}</option>
        </select>
    </div>
    <div style="margin-top:10px;" v-if="selected_preprocessed_data">
        <label for="hs-select-label" class="block text-sm font-medium mb-2 dark:text-white">请选择你的模型</label>
        <select id="hs-select-label" class="py-3 px-4 pe-9 block w-4/5 border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
        @click="selectModels"v-model="selected_model" >
            <option value="" disabled selected>模型列表</option>
            <option v-for="data in models" :value="data">{{ data.model_description }}</option>
        </select>
    </div>
    <div style="margin-top:10px;" v-if="selected_model">
        <button type="button" 
                class="py-3 px-4 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-100 text-blue-800 hover:bg-blue-200 disabled:opacity-50 disabled:pointer-events-none dark:hover:bg-blue-800 dark:text-green-500 dark:hover:text-green-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
                @click="start_generate">
                开始生成
        </button>
    </div>
</template>
    
<script lang="ts" setup>
import { UploadFilled } from '@element-plus/icons-vue'
import { current_task, update_current_task,data_manage } from '@/util/task';
import axios from 'axios';
import { onMounted,ref } from 'vue';
const preprocessed_datas = ref<Array<{[key: string]: any}>>([])
const marked_processed_datas = ref<Array<{[key: string]: any}>>([])
const models = ref<Array<{[key: string]: any}>>([])
const selected_preprocessed_data = ref('')
const selected_model = ref('')

const selectPreprocessedData = () => {
    axios.get('/api/preprocessed_data/',{ params: { task_type: current_task.value.task_type,algorithm:current_task.value.task_algorithm }}).then(res => {
        if(res.data.preprocessed_datas.length == 0){
            preprocessed_datas.value = []
            alert("没有预处理过数据,请先预处理数据")
        }
        Object.assign(preprocessed_datas.value, res.data.preprocessed_datas)
    })
}

const selectMarkedPreprocessedData = () => {
    axios.get('/api/marked_preprocessed_data/',{ params: { task_type: current_task.value.task_type,algorithm:current_task.value.task_algorithm }}).then(res => {
        if(res.data.marked_preprocessed_datas.length == 0){
            marked_processed_datas.value = []
            alert("没有预处理过数据,请先预处理数据")
        }
        Object.assign(marked_processed_datas.value, res.data.marked_preprocessed_datas)
    })
}

const selectModels = () => {
    axios.get('/api/models/',{ params: { task_id : current_task.value.task_id, data_type:selected_preprocessed_data.value.data_type} }).then(res => {
        Object.assign(models.value, res.data.models)
    })
}

const start_generate = () => {
    axios.post('/api/result/',{ task_id: current_task.value.task_id, data_id:selected_preprocessed_data.value.data_id, model_id:selected_model.value.model_id }).then(res => {
        if (res.data.status == "success"){
            alert("生成成功")
        }
        alert("生成失败")
    })
}
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