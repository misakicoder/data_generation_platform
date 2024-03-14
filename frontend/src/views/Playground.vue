<template>
    <div class="relative min-h-screen">
        <Sidebar></Sidebar>

        <div class="pt-2 fixed z-20 w-96 top-4 right-2" v-if="current_task.status == 'pending'">
            <div class="mx-auto max-w-screen-2xl px-4 pb-4 md:px-8">
                <div
                    class="relative flex flex-wrap rounded-lg bg-violet-500 px-4 py-3 shadow-lg sm:flex-nowrap sm:items-center sm:justify-center sm:gap-3 sm:pr-8 md:px-8">
                    <div
                        class="order-1 mb-2 inline-flex w-11/12 max-w-screen-sm text-sm text-white sm:order-none sm:mb-0 sm:w-auto md:text-base justify-center items-center">
                        <i class="animate-spin ti ti-loader-quarter mr-2"></i>
                        <span class="text-sm"> 精彩正在生成，请稍作等待</span>
                    </div>
                </div>
            </div>
        </div>

        <div
            class="w-full min-h-screen h-full lg:pt-5 pt-20 pb-10 px-4 sm:px-6 md:px-8 xl:ps-72">
            <RouterView></RouterView>

            <template v-if="current_task.status == 'pending'">
                <div class="absolute top-0 start-0 w-full h-full bg-white/[.5] rounded-lg dark:bg-neutral-900/[.4]"></div>
                <div class="absolute top-1/2 start-1/2 transform -tranneutral-x-1/2 -tranneutral-y-1/2">
                    <div class="animate-spin inline-block w-6 h-6 border-[3px] border-current border-t-transparent text-violet-400 rounded-full dark:text-violet-500"
                        role="status" aria-label="loading">
                        <span class="sr-only">Loading...</span>
                    </div>
                </div>
            </template>
        </div>
    </div>
</template>

<script lang="ts" setup>
import Sidebar from "@/components/Playground/Sidebar.vue"
import { current_task } from "@/util/task";
</script>