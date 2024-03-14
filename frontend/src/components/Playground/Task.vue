<template>
    <div>
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
                    生成剧本
                </button>
                <div id="hs-basic-always-open-collapse-one"
                    class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300"
                    aria-labelledby="hs-basic-always-open-heading-one">
                    <Story></Story>
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
                    生成脚本、分镜、视频
                </button>
                <div id="hs-basic-always-open-collapse-two"
                    class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300"
                    aria-labelledby="hs-basic-always-open-heading-two">
                    <IntermediateProcess></IntermediateProcess>
                </div>
            </div>

            <div class="hs-accordion active" id="hs-basic-always-open-heading-three">
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
                    生成配乐
                </button>
                <div id="hs-basic-always-open-collapse-three"
                    class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300"
                    aria-labelledby="hs-basic-always-open-heading-three">
                    <Music></Music>
                </div>
            </div>

            <div class="hs-accordion active" id="hs-basic-always-open-heading-four">
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
                    合成成片
                </button>
                <div id="hs-basic-always-open-collapse-four"
                    class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300"
                    aria-labelledby="hs-basic-always-open-heading-four">
                    <Movie></Movie>
                </div>
            </div>

            <!-- <div class="hs-accordion active" id="hs-basic-always-open-heading-four">
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
                    超分插帧
                </button>
                <div id="hs-basic-always-open-collapse-four"
                    class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300"
                    aria-labelledby="hs-basic-always-open-heading-four">
                    <SuperMovie></SuperMovie>
                </div>
            </div> -->
        </div>
    </div>
</template>

<script lang="ts" setup>
import { current_task, get_current_task } from "@/util/task";
import { onMounted, watch } from "vue";
import Story from "@/components/Playground/Story.vue"
import IntermediateProcess from "@/components/Playground/IntermediateProcess.vue"
import Movie from "@/components/Playground/Movie.vue"
import Music from "@/components/Playground/Music.vue"
// import SuperMovie from "./SuperMovie.vue";
import router from "@/router/router";

onMounted(() => {
    const task_id = router.currentRoute.value.params.task_id as string
    current_task.value.task_id = task_id

    get_current_task()
    // todo: 丑陋！因为同时生成图片、视频时，多个 update_current_task() 并行，如果生成一张图片，status就是ready，导致后面的图片生成不会显示
    setInterval(() => {
        get_current_task()
    }, 4000)
})

watch(router.currentRoute, () => {
    // reset current_task
    Object.assign(current_task.value, {
        task_id: "",
        idea: "",
        movie_type: "",
        frame_num: 0,
        status: "ready",
        story: "",
        scripts: [],
        scenes: [],
        videos: [],
        music_description_zh: "",
        music: "",
        movie: "",
    })

    const task_id = router.currentRoute.value.params.task_id as string
    current_task.value.task_id = task_id
    get_current_task()
})
</script>