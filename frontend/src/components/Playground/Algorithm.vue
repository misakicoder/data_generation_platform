<!-- 剧本 -->

<template>
<div class="flex gap-4">
    <div v-for="(algorithm, index) in algorithm_list" :key="index">
        <div class="flex flex-col bg-white border border-t-4 border-t-blue-600 shadow-sm rounded-xl dark:bg-slate-900 dark:border-gray-700 dark:border-t-blue-500 dark:shadow-slate-700/[.7]">
            <div class="p-4 md:p-5">
                <h3 class="text-lg font-bold text-gray-800 dark:text-white">
                {{ algorithm.algorithm_name }}
                </h3>
                <p class="mt-2 text-gray-500 dark:text-gray-400">
                {{ algorithm.algorithm_description }}
                </p>
                <a class="mt-3 inline-flex items-center gap-x-1 text-sm font-semibold rounded-lg border border-transparent text-blue-600 hover:text-blue-800 disabled:opacity-50 disabled:pointer-events-none dark:text-blue-500 dark:hover:text-blue-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" href="#" 
                  @click="selectAlgorithm(index)">
                    选择此算法
                </a>
            </div>
        </div>
    </div>
</div>
</template>

<script lang="ts" setup>
import { UploadFilled } from '@element-plus/icons-vue'
import { current_task,algorithm_list,get_current_task,get_algorithm_list
  ,get_data_manager} from '@/util/task';
import axios from 'axios';
import { onMounted,watch } from 'vue';
import router from "@/router/router";
import { get } from 'http';
import Data_preprocess from './Data_preprocess.vue';
import Data_generate from './Data_generate.vue';



onMounted(async () => {
    const task_id = router.currentRoute.value.params.id as string
    current_task.value.task_id = task_id
    get_current_task()
})


watch(() => router.currentRoute.value.params.id,(newVal) => {
    current_task.value.task_id = newVal as string
    get_current_task()
})


const selectAlgorithm = (index : number) => {
  axios.post('/api/data_manager/', {
      task_id: current_task.value.task_id,
      task_algorithm: algorithm_list.value[index].algorithm_name,
      data_clean : true,
      data_mark : algorithm_list.value[index].need_mark,
      data_preprocess : true,
      data_generate : true,
  }).then(res => {
      if (res.data.status == 'success') {
          get_data_manager()
      } else {
          alert('选择算法失败')
      }
  }).catch(err => {
      console.error(err)
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