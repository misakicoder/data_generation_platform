<template>
    <!-- Card Section -->
    <div class="max-w-5xl px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">
        <div
            class="py-3 flex items-center text-sm text-neutral-800 before:flex-[1_1_0%] before:border-t before:border-neutral-200 before:me-6 after:flex-[1_1_0%] after:border-t after:border-neutral-200 after:ms-6 dark:text-white dark:before:border-neutral-600 dark:after:border-neutral-600">
            数据生成
        </div>
        <!-- Grid -->
        <div class="grid grid-cols-3 lg:grid-cols-4 gap-4 sm:gap-4  mt-5">
            <!-- Card -->
            
            <div v-for="item in generate_items" :key="item.title" :to="item.link" @click="create_task(item.type)">
                <div
                    class="group flex flex-col  bg-white border shadow-sm rounded-xl hover:shadow-md transition dark:bg-neutral-900 dark:border-neutral-800 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 cursor-pointer hover:scale-105">
                    <div class="p-4 md:p-5">
                        <div class="flex">
                            <span class="mt-1 flex-shrink-0 w-5 h-5 text-neutral-800 dark:text-neutral-200 text-xl">
                                <i :class="item.icon"></i>
                            </span>

                            <div class="grow ms-5">
                                <h3 class=" font-semibold text-neutral-800  dark:text-neutral-200">
                                    {{ item.title }} </h3>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- End Card -->
        </div>
        <div
            class="py-3 flex items-center text-sm text-neutral-800 before:flex-[1_1_0%] before:border-t before:border-neutral-200 before:me-6 after:flex-[1_1_0%] after:border-t after:border-neutral-200 after:ms-6 dark:text-white dark:before:border-neutral-600 dark:after:border-neutral-600">
            数据预测
        </div>
        <!-- Grid -->
        <div class="grid grid-cols-3 lg:grid-cols-3 gap-4 sm:gap-4  mt-5">
            <!-- Card -->
            <div v-for="item in predict_items" :key="item.title" :to="item.link" @click="create_task(item.type)" >
                <div
                    class="group flex flex-col bg-white border shadow-sm rounded-xl hover:shadow-md transition dark:bg-neutral-900 dark:border-neutral-800 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 cursor-pointer hover:scale-105">
                    <div class="p-4 md:p-5">
                        <div class="flex">
                            <span class="mt-1 flex-shrink-0 w-5 h-5 text-neutral-800 dark:text-neutral-200 text-xl">
                                <i :class="item.icon"></i>
                            </span>

                            <div class="grow ms-5">
                                <h3 class=" font-semibold text-neutral-800  dark:text-neutral-200">
                                    {{ item.title }} </h3>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- End Card -->
        </div>
        <!-- End Grid -->


        <!-- Grid -->
    </div>
    <!-- End Card Section -->
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import axios from 'axios';
import { current_task } from '@/util/task';
import { useRouter } from 'vue-router';

const router = useRouter();

const generate_items = ref([
    {
        title: '负荷数据生成',
        icon: 'ti ti-vinyl',
        link: '/playground/main',
        type: 'load_generate'
    },
    {
        title: '天气数据生成',
        icon: 'ti ti-vinyl',
        link: '/playground/main',
        type: 'weather_generate'
    },
    {
        title: '股票数据生成',
        icon: 'ti ti-vinyl',
        link: '/playground/main',
        type: 'stock_generate'
    },
    {
        title: '图片数据生成',
        icon: 'ti ti-vinyl',
        link: '/playground/main',
        type: 'image_generate'
    }
])

const predict_items = ref([
    {
        title: '负荷数据预测',
        icon: 'ti ti-vinyl',
        link: '/playground/main',
        type: 'load_predict'
    },
    {
        title: '天气数据预测',
        icon: 'ti ti-vinyl',
        link: '/playground/main',
        type: 'weather_predict'
    },
    {
        title: '股票数据预测',
        icon: 'ti ti-vinyl',
        link: '/playground/main',
        type: 'stock_predict'
    }
])

const create_task = (task_type:string) => {
    axios.post('/api/task/', {task_type: task_type}).then(res => {
        if (res.data.status == 'success') {
            Object.assign(current_task.value, res.data.task);
            console.log('create task success');
            router.push('/playground/main/' + current_task.value.task_id);
        } else {
            console.log('create task failed');
        }
    }).catch(err => {
        console.error(err);
    })
}

</script>

<style lang="scss"></style>