<template>
    <div>
        <!-- Sidebar Toggle -->
        <div
            class="fixed top-0 inset-x-0 z-20 border-y px-4 sm:px-6 md:px-8 xl:hidden dark:bg-neutral-900 dark:border-neutral-700 bg-white">
            <div class="flex items-center py-4">
                <button type="button" class="text-neutral-500 hover:text-neutral-600" data-hs-overlay="#docs-sidebar"
                    aria-controls="docs-sidebar" aria-label="Toggle navigation">
                    <span class="sr-only">Toggle Navigation</span>
                    <i class="ti ti-menu-2 text-lg"></i>
                </button>

                <!-- Breadcrumb -->
                <ol class="ms-3 flex items-center whitespace-nowrap" aria-label="Breadcrumb">
                    <li class="flex items-center text-sm text-neutral-800 dark:text-neutral-400">
                        <span class="flex justify-center items-center font-semibold">
                            <img src="/fish.png" alt="Image" class="w-9 h-9 mr-2">
                            <span class="text-black-500 bg-clip-text text-transparent bg-black pl-2">
                                DataGeneartion
                            </span>
                        </span>
                        <i class="ti ti-chevron-right text-lg"></i>
                    </li>
                    <li class="text-sm font-semibold text-neutral-800 truncate dark:text-neutral-400"
                        aria-current="page">
                        制作影片
                    </li>
                </ol>
                <!-- End Breadcrumb -->
            </div>
        </div>
        <!-- End Sidebar Toggle -->

        <!-- Sidebar -->
        <div id="docs-sidebar"
            class="hs-overlay hs-overlay-open:translate-x-0 -translate-x-full transition-all duration-300 transform hidden fixed top-0 start-0 bottom-0 z-[60] w-64 bg-white border-e border-neutral-200 pt-7 overflow-y-auto lg:block lg:translate-x-0 lg:end-auto lg:bottom-0 [&::-webkit-scrollbar]:w-2 [&::-webkit-scrollbar-thumb]:rounded-full [&::-webkit-scrollbar-track]:bg-neutral-100 [&::-webkit-scrollbar-thumb]:bg-neutral-300 dark:[&::-webkit-scrollbar-track]:bg-neutral-700 dark:[&::-webkit-scrollbar-thumb]:bg-neutral-500 dark:bg-neutral-800 dark:border-neutral-700">
            <div class=" flex flex-col justify-between h-full">
                <div class="px-6">
                    <RouterLink to="/">
                        <div class="flex items-center text-xl font-semibold">
                            <img src="/fish.png" alt="Image" class="w-9 h-9 mr-2">
                            <span class="text-black-500 bg-clip-text text-transparent bg-black pl-2">
                                DataGeneartion
                            </span>
                        </div>
                    </RouterLink>
                </div>

                <RouterLink to="/playground/idea">
                    <div
                        class="flex items-center gap-x-3.5 py-2 px-2.5 text-sm rounded-lg bg-violet-500 text-white hover:bg-violet-600 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 cursor-pointer mx-6 my-4">
                        <i class="ti ti-plus text-lg"></i>
                        开始新任务
                    </div>
                </RouterLink>

                <nav class="hs-accordion-group p-6 w-full flex flex-col flex-wrap overflow-y-auto flex-1">
                    <ul class="space-y-1.5">
                        <template v-for="task of task_list.values()">
                            <li>
                                <RouterLink :to="'/playground/task/' + task.task_id">
                                    <div
                                        class="flex items-center gap-x-3.5 py-2 px-2.5 text-sm text-neutral-700 rounded-lg hover:bg-neutral-100 dark:hover:bg-neutral-900 dark:text-white dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 cursor-pointer text-ellipsis">
                                        {{ task.idea }}
                                    </div>
                                </RouterLink>
                            </li>
                        </template>
                    </ul>
                </nav>

                <div class="hs-accordion-group p-6 w-full flex flex-col flex-wrap">
                    <ul class="space-y-1.5">
                        <li>
                            <RouterLink to="/my">
                                <div
                                    class="flex items-center gap-x-3.5 py-2 px-2.5  text-sm text-neutral-700 rounded-lg hover:bg-neutral-100 dark:hover:bg-neutral-900 dark:text-white dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 cursor-pointer">
                                    <i class="ti ti-home text-lg"></i>
                                    我的
                                </div>
                            </RouterLink>
                        </li>
                        <li>
                            <RouterLink to="/playground/setting">
                                <div
                                    class="flex items-center gap-x-3.5 py-2 px-2.5  text-sm text-neutral-700 rounded-lg hover:bg-neutral-100 dark:hover:bg-neutral-900 dark:text-white dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 cursor-pointer">
                                    <i class="ti ti-settings-2 text-lg"></i>
                                    设置
                                </div>
                            </RouterLink>
                        </li>
                        <li>
                            <div class="flex items-center gap-x-3.5 py-2 px-2.5  text-sm text-neutral-700 rounded-lg hover:bg-neutral-100 dark:hover:bg-neutral-900 dark:text-white dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 cursor-pointer"
                                @click="logout">
                                <i class="ti ti-logout text-lg"></i>
                                退出
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- End Sidebar -->
    </div>
</template>

<script lang="ts" setup>
import router from "@/router/router";
import { onMounted } from "vue";
import { get_all_my_tasks, task_list } from '@/util/task';
import { Clapperboard } from "lucide-vue-next";
import { useDark, useToggle } from '@vueuse/core'

const isDark = useDark()
const toggleDark = useToggle(isDark)

onMounted(() => {
    get_all_my_tasks()
})

const logout = () => {
    router.push('/')
}
</script>