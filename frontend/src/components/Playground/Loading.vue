<template>

    <div v-loading="loading" class="hs-accordion-group" data-hs-accordion-always-open>
            <div class="hs-accordion active" id="hs-basic-always-open-heading-one">
                <button
                    class="hs-accordion-toggle hs-accordion-active:text-violet-500 py-3 inline-flex items-center gap-x-3 w-full font-semibold text-start text-neutral-800 hover:text-neutral-500 rounded-lg disabled:opacity-50 disabled:pointer-events-none dark:hs-accordion-active:text-violet-400 dark:text-neutral-200 dark:hover:text-neutral-400 outline-none dark:focus:text-neutral-400 text-lg"
                    aria-controls="hs-basic-always-open-collapse-one">
                    <svg class="hs-accordion-active:hidden block w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24"
                        height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                        stroke-linecap="round" stroke-linejoin="round">
                        <path d="M5 12h14" />
                        <path d="M12 5v14" />
                    </svg>
                    <svg class="hs-accordion-active:block hidden w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24"
                        height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                        stroke-linecap="round" stroke-linejoin="round">
                        <path d="M5 12h14" />
                    </svg>
                    误差图片
                </button>
                <div id="hs-basic-always-open-collapse-one"
                    class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300"
                    aria-labelledby="hs-basic-always-open-heading-one">
                </div>
                <div class="flex flex-wrap">
                    <img v-for="img in img_paths" :src="oss_path + img" alt="" class="w-4/5 max-w-md m-auto rounded-lg">
                </div>
            </div>
            <div class="h-10"></div>
            <button type="button" class="py-3 px-4 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-teal-500 text-white hover:bg-teal-600 disabled:opacity-50 disabled:pointer-events-none"
            @click="download_zip">
                一键下载结果
            </button>
    </div>
  </template>
  
<script lang="ts" setup>
import axios from 'axios'
import { Mountain } from 'lucide-vue-next'
import { ref } from 'vue'
import {onMounted,onUnmounted} from 'vue'
import { current_task, get_current_task,data_manage } from '@/util/task';
import { ta } from 'element-plus/es/locales.mjs';
import { useRouter } from 'vue-router';
import { oss_path } from '@/util/api';
const router = useRouter()

const loading = ref(true)
let intervalId: number | undefined = undefined
const img_paths = ref('')


onMounted(() => {
if (current_task.value.task_state === 'ready') {
    get_result()
    return
}
intervalId = window.setInterval(() => {
    axios.get('/api/task/',{ params: { task_id: router.currentRoute.value.params.id }}).then(res => {
        Object.assign(current_task.value, res.data.task);
        if(current_task.value.task_state === 'ready'){
            get_result()
        }
    })
  }, 1000);
});

onUnmounted(() => {
  if (intervalId !== undefined) {
    window.clearInterval(intervalId)
  }
})

const get_result = () => {
    axios.get('/api/result/',{ params: { task_id: router.currentRoute.value.params.id }}).then(res => {
        img_paths.value = res.data.img_results
        loading.value = false
        window.clearInterval(intervalId)
    })

}

const download_zip = () => {
    axios.get('/api/result_zip/', {
        params: { task_id: router.currentRoute.value.params.id },
        responseType: 'blob'  // 添加这一行
    }).then(res => {
        const url = window.URL.createObjectURL(new Blob([res.data]))
        const link = document.createElement('a')
        link.href = url
        link.setAttribute('download', current_task.value.task_name + '.zip')
        document.body.appendChild(link)
        link.click()
    })
}
</script>

<style>
body {
margin: 0;
}
.example-showcase .el-loading-mask {
z-index: 9;
--element-loading-background: rgba(0, 0, 0, 1);
}
</style>
  