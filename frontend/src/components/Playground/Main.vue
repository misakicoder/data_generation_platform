<template>
    <div>
        <div class="min-h-30 flex flex-col bg-green-500 border shadow-sm rounded-xl dark:bg-slate-900 dark:border-gray-700 dark:shadow-slate-700/[.7]">
            <div class="flex flex-auto flex-col justify-center items-center p-4 md:p-5">
                <p class="mt-2 text-red-500 dark:text-yellow-400">
                当前任务选择的算法是:{{ current_task.task_algorithm }}
                </p>
            </div>
        </div>

        <div class="hs-accordion-group" data-hs-accordion-always-open>
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
                    上传数据
                </button>
                <div id="hs-basic-always-open-collapse-one"
                    class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300"
                    aria-labelledby="hs-basic-always-open-heading-one">
                    <Upload></Upload>
                </div>
            </div>

            <div class="hs-accordion active" id="hs-basic-always-open-heading-two">
                <button
                    class="hs-accordion-toggle hs-accordion-active:text-violet-500 py-3 inline-flex items-center gap-x-3 w-full font-semibold text-start text-neutral-800 hover:text-neutral-500 rounded-lg disabled:opacity-50 disabled:pointer-events-none dark:hs-accordion-active:text-violet-400 dark:text-neutral-200 dark:hover:text-neutral-400 outline-none dark:focus:text-neutral-400 text-lg"
                    aria-controls="hs-basic-always-open-collapse-two">
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
                    选择相应的算法
                </button>
                <div id="hs-basic-always-open-collapse-two"
                    class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300"
                    aria-labelledby="hs-basic-always-open-heading-two">
                    <!-- <IntermediateProcess></IntermediateProcess> -->
                    <Algorithm></Algorithm>
                </div>
            </div>

            <div class="hs-accordion active" id="hs-basic-always-open-heading-three" v-if="data_manage.data_clean">
                <button
                    class="hs-accordion-toggle hs-accordion-active:text-violet-500 py-3 inline-flex items-center gap-x-3 w-full font-semibold text-start text-neutral-800 hover:text-neutral-500 rounded-lg disabled:opacity-50 disabled:pointer-events-none dark:hs-accordion-active:text-violet-400 dark:text-neutral-200 dark:hover:text-neutral-400 outline-none dark:focus:text-neutral-400 text-lg"
                    aria-controls="hs-basic-always-open-collapse-three">
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
                    数据清洗
                </button>
                <div id="hs-basic-always-open-collapse-three"
                    class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300"
                    aria-labelledby="hs-basic-always-open-heading-three">
                    <!-- <Music></Music> -->
                    <Data_clean></Data_clean>
                </div>
            </div>

            <div class="hs-accordion active" id="hs-basic-always-open-heading-four" v-if="data_manage.data_mark">
                <button
                    class="hs-accordion-toggle hs-accordion-active:text-violet-500 py-3 inline-flex items-center gap-x-3 w-full font-semibold text-start text-neutral-800 hover:text-neutral-500 rounded-lg disabled:opacity-50 disabled:pointer-events-none dark:hs-accordion-active:text-violet-400 dark:text-neutral-200 dark:hover:text-neutral-400 outline-none dark:focus:text-neutral-400 text-lg"
                    aria-controls="hs-basic-always-open-collapse-four">
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
                    数据标注
                </button>
                <div id="hs-basic-always-open-collapse-four"
                    class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300"
                    aria-labelledby="hs-basic-always-open-heading-four">
                    <Data_mark></Data_mark>
                </div>
            </div>

            <div class="hs-accordion active" id="hs-basic-always-open-heading-four" v-if="data_manage.data_preprocess">
                <button
                    class="hs-accordion-toggle hs-accordion-active:text-violet-500 py-3 inline-flex items-center gap-x-3 w-full font-semibold text-start text-neutral-800 hover:text-neutral-500 rounded-lg disabled:opacity-50 disabled:pointer-events-none dark:hs-accordion-active:text-violet-400 dark:text-neutral-200 dark:hover:text-neutral-400 outline-none dark:focus:text-neutral-400 text-lg"
                    aria-controls="hs-basic-always-open-collapse-four">
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
                    数据预处理
                </button>
                <div id="hs-basic-always-open-collapse-four"
                    class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300"
                    aria-labelledby="hs-basic-always-open-heading-four">
                    <Data_preprocess></Data_preprocess>
                    <!-- <Movie></Movie> -->
                </div>
            </div>

            <div class="hs-accordion active" id="hs-basic-always-open-heading-four" v-if="data_manage.data_generate">
                <button
                    class="hs-accordion-toggle hs-accordion-active:text-violet-500 py-3 inline-flex items-center gap-x-3 w-full font-semibold text-start text-neutral-800 hover:text-neutral-500 rounded-lg disabled:opacity-50 disabled:pointer-events-none dark:hs-accordion-active:text-violet-400 dark:text-neutral-200 dark:hover:text-neutral-400 outline-none dark:focus:text-neutral-400 text-lg"
                    aria-controls="hs-basic-always-open-collapse-four">
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
                    数据生成
                </button>
                <div id="hs-basic-always-open-collapse-four"
                    class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300"
                    aria-labelledby="hs-basic-always-open-heading-four">
                    <Data_generate></Data_generate>
                </div>
            </div>

        </div>
    </div>
</template>

<script lang="ts" setup>
import Upload from "@/components/Playground/Upload.vue"
import Algorithm from "@/components/Playground/Algorithm.vue"
import Data_clean from "@/components/Playground/Data_clean.vue"
import Data_mark from "@/components/Playground/Data_mark.vue"
import Data_generate from "@/components/Playground/Data_generate.vue"
import Data_preprocess from "@/components/Playground/Data_preprocess.vue"
import { onMounted, watch } from "vue";
import { current_task, get_current_task,data_manage } from "@/util/task";
// import SuperMovie from "./SuperMovie.vue";
import router from "@/router/router";
import { ref } from "vue";





</script>