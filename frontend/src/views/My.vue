<template>
    <Navbar></Navbar>

    <div class="pt-24">
        <div class="mx-auto max-w-screen-2xl px-4 md:px-8">
            <!-- text - start -->
            <div class="mb-10 md:mb-16">
                <h2
                    class="mb-4 text-center text-2xl font-bold text-neutral-800 dark:text-neutral-50 md:mb-6 lg:text-3xl">
                    我的作品</h2>

                <p class="mx-auto max-w-screen-md text-center text-neutral-500 dark:text-neutral-200 md:text-lg">
                    用故事点亮荧幕，世界因您的创意而惊叹。
                </p>
            </div>
            <!-- text - end -->

            <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
                <div v-for=" task  in  task_list " class="relative">
                    <RouterLink :to="'playground/task/' + task.task_id">
                        <div
                            class="relative flex flex-col w-full  h-full bg-center bg-cover rounded-xl overflow-hidden hover:shadow-lg transition dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 hover:scale-105 duration-200 cursor-pointer shadow-sm">
                            <img :src="s3_img_path + task.scenes[0]" alt="" srcset="" class="w-full"
                                v-if="task.scenes[0]">
                            <div class="absolute inset-0 h-full w-full flex justify-center items-center dark:text-neutral-100"
                                v-else>
                                <i class="ti ti-photo-bolt text-2xl"></i>
                            </div>
                            <div class=" bottom-0 absolute w-full p-4 bg-gradient-to-t from-black/20 to-transparent">
                                <h3 class="text-lg text-white/[.9] group-hover:text-white font-bold my-2">
                                    {{ task.idea }}
                                </h3>
                                <div class="flex justify-between items-center">
                                    <div class="flex w-full sm:items-center gap-x-5 sm:gap-x-3">
                                        <span class=" text-neutral-100 text-xs">
                                            发布日期
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </RouterLink>
                </div>
            </div>
        </div>
    </div>

    <Footer></Footer>
</template>

<script lang="ts" setup>
import { onMounted } from 'vue';
import { get_all_my_tasks, task_list } from '@/util/task';
import { s3_img_path } from '@/util/api';
import Navbar from '@/components/Common/Navbar.vue';
import Footer from '@/components/Common/Footer.vue';

onMounted(() => {
    get_all_my_tasks()
})
</script>
