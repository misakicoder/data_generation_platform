<!-- 剧本 -->

<template>

    <div style="margin-top:10px;" v-if = "!data_manage.data_mark">
        <label for="hs-select-label" class="block text-sm font-medium mb-2 dark:text-white">请选择你要预处理的数据</label>
        <select id="hs-select-label" class="py-3 px-4 pe-9 block w-4/5 border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
            @click="select_cleanedData" v-model="selected_cleaned_or_marked_data">
            <option value="" disabled selected>已清理数据列表</option>
            <option v-for="data in cleaned_datas" :value="data">{{ data.data_type + " : "+data.data_description}}</option>
        </select>
    </div>
    <div style="margin-top:10px;" v-else>
        <label for="hs-select-label" class="block text-sm font-medium mb-2 dark:text-white">请选择你要预处理的数据</label>
        <select id="hs-select-label" class="py-3 px-4 pe-9 block w-4/5 border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
            @click="select_markedData" v-model="selected_cleaned_or_marked_data">
            <option value="" disabled selected>已标记数据列表</option>
            <option v-for="data in marked_datas" :value="data">{{ data.data_type + " : "+data.data_description}}</option>
        </select>
    </div>
    <div class="flex gap-4 mt-4" v-if="selected_cleaned_or_marked_data">
        <button type="button" 
            class="py-3 px-4 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-teal-100 text-teal-800 hover:bg-teal-200 disabled:opacity-50 disabled:pointer-events-none dark:hover:bg-teal-900 dark:text-teal-500 dark:hover:text-teal-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
            @click="start_preprocess">
            开始预处理
        </button>
    </div>
    <!-- <div
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
    </div> -->

</template>
    
<script lang="ts" setup>
import { UploadFilled } from '@element-plus/icons-vue'
import { current_task, update_current_task,data_manage } from '@/util/task';
import axios from 'axios';
import { onMounted,ref } from 'vue';
import { da } from 'element-plus/es/locales.mjs';
const preprocess_or_not = ref(false)

const cleaned_datas = ref<Array<{[key: string]: any}>>([])
const marked_datas = ref<Array<{[key: string]: any}>>([])
const selected_cleaned_or_marked_data = ref('')

const select_cleanedData = () => {
    axios.get('/api/cleaned_data/',{ params: { task_type: current_task.value.task_type,algorithm:current_task.value.task_algorithm }}).then(res => {
        if(res.data.cleaned_datas.length == 0){
            cleaned_datas.value = []
            alert("没有清洗过数据,请先清洗数据")
        }
        Object.assign(cleaned_datas.value, res.data.cleaned_datas)
    })
}

const select_markedData = () => {
    axios.get('/api/marked_data/',{ params: { task_type: current_task.value.task_type,algorithm:current_task.value.task_algorithm }}).then(res => {
        if(res.data.marked_datas.length == 0){
            marked_datas.value = []
            alert("没有标记过数据,请先标记数据")
        }
        Object.assign(marked_datas.value, res.data.marked_datas)
    })
}

const start_preprocess = () => {
    axios.post('/api/preprocessed_data/',{cleaned_or_marked_data:selected_cleaned_or_marked_data.value}).then(res => {
        if(res.data.status == "success"){
            alert("预处理成功")
        }
        else{
            alert("预处理失败")
        }
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
    .separator {
        border-top: 1px solid #ddd;
        margin: 20px 0;
    }
</style>