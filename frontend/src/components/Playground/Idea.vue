<template>
    <!-- Content -->
    <div class="pt-24 max-w-lg mx-auto">
        <div class="w-full text-center mx-auto px-4 sm:px-6 lg:px-8">
            <h1
                class="flex  justify-center items-center text-xl font-bold text-neutral-800 sm:text-2xl dark:text-white">
                <span class="flex justify-center items-center font-semibold">
                    <Clapperboard :size="20" class="text-pink-500 dark:text-white" />
                    <span
                        class="dark:text-white bg-clip-text text-transparent bg-gradient-to-r from-pink-500 to-violet-500 pl-2">
                        FilmAction
                    </span>
                </span>
            </h1>
            <div
                class="mt-2 text-center m-auto flex flex-col justify-center items-center sm:flex-row text-md text-neutral-600 dark:text-neutral-400">
                <p>
                    释放您的导演天赋，
                </p>
                <p>
                    与 FilmAction 共创精彩
                </p>
            </div>
        </div>

        <div class="mt-10  w-full mx-auto px-4 sm:px-6 lg:px-8">
            <input type="text"
                class="py-3 px-4 block w-full border border-neutral-200 rounded-lg text-sm focus:border-violet-500 focus:ring-violet-500 focus:ring-1 focus:border disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:focus:ring-neutral-600"
                :placeholder="idea_hint" v-model="idea">

            <div class="mt-7 w-full flex flex-row justify-between">
                <div class="hs-dropdown relative inline-flex">
                    <button id="hs-dropdown-with-icons" type="button"
                        class="hs-dropdown-toggle py-3 px-4 inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border border-neutral-200 bg-white text-neutral-800 shadow-sm hover:bg-neutral-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-white dark:hover:bg-neutral-800 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 w-32">
                        {{ movie_style }}
                        <svg class="hs-dropdown-open:rotate-180 w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24"
                            height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                            stroke-linecap="round" stroke-linejoin="round">
                            <path d="m6 9 6 6 6-6" />
                        </svg>
                    </button>

                    <div class="hs-dropdown-menu transition-[opacity,margin] duration hs-dropdown-open:opacity-100 opacity-0 hidden w-32 bg-white z-10 shadow-md rounded-lg p-2 mt-2 divide-y divide-neutral-200 dark:bg-neutral-800 dark:border dark:border-neutral-700 dark:divide-neutral-700"
                        aria-labelledby="hs-dropdown-with-icons">
                        <div class="py-2 first:pt-0 last:pb-0">
                            <template v-for="_movie_style in movie_styles">
                                <div class="flex items-center gap-x-3.5 py-2 px-3 rounded-lg text-sm text-neutral-800 hover:bg-neutral-100 focus:outline-none focus:bg-neutral-100 dark:text-neutral-400 dark:hover:bg-neutral-700 dark:hover:text-neutral-300 dark:focus:bg-neutral-700 cursor-pointer"
                                    @click="movie_style = _movie_style">
                                    {{ _movie_style }}
                                </div>
                            </template>
                        </div>
                    </div>
                </div>
                <div class="hs-dropdown relative inline-flex">
                    <button id="hs-dropdown-with-icons" type="button"
                        class="hs-dropdown-toggle py-3 px-4 inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border border-neutral-200  text-neutral-800 shadow-sm hover:bg-neutral-50 disabled:opacity-50 disabled:pointer-events-none  dark:border-neutral-700 dark:text-white dark:hover:bg-neutral-800 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 w-32 bg-neutral-100 dark:bg-neutral-950 "
                        :class="{
                        'pointer-events-none': movie_style == '电影风格',
                        'bg-white dark:bg-transparent': movie_style != '电影风格'
                    }">
                        {{ movie_type }}
                        <svg class="hs-dropdown-open:rotate-180 w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24"
                            height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                            stroke-linecap="round" stroke-linejoin="round">
                            <path d="m6 9 6 6 6-6" />
                        </svg>
                    </button>
                    <div class="hs-dropdown-menu transition-[opacity,margin] duration hs-dropdown-open:opacity-100 opacity-0 hidden w-32 bg-white shadow-md rounded-lg p-2 mt-2 divide-y divide-neutral-200 dark:bg-neutral-800 dark:border z-10 dark:border-neutral-700 dark:divide-neutral-700"
                        aria-labelledby="hs-dropdown-with-icons">
                        <div class="py-2 first:pt-0 last:pb-0">

                            <template v-for="_movie_type in movie_types">
                                <div class="flex items-center gap-x-3.5 py-2 px-3 rounded-lg text-sm text-neutral-800 hover:bg-neutral-100 focus:outline-none focus:bg-neutral-100 dark:text-neutral-400 dark:hover:bg-neutral-700 dark:hover:text-neutral-300 dark:focus:bg-neutral-700 cursor-pointer"
                                    @click="movie_type = _movie_type">
                                    {{ _movie_type }}
                                </div>
                            </template>
                        </div>
                    </div>
                </div>
                <div class="hs-dropdown relative inline-flex">
                    <button id="hs-dropdown-with-icons" type="button"
                        class="hs-dropdown-toggle py-3 px-4 inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border border-neutral-200 bg-white text-neutral-800 shadow-sm hover:bg-neutral-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-white dark:hover:bg-neutral-800 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 w-32">
                        {{ movie_duration }}
                        <svg class="hs-dropdown-open:rotate-180 w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24"
                            height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                            stroke-linecap="round" stroke-linejoin="round">
                            <path d="m6 9 6 6 6-6" />
                        </svg>
                    </button>

                    <div class="hs-dropdown-menu transition-[opacity,margin] duration hs-dropdown-open:opacity-100 opacity-0 hidden w-32 bg-white z-10 shadow-md rounded-lg p-2 mt-2 divide-y divide-neutral-200 dark:bg-neutral-800 dark:border dark:border-neutral-700 dark:divide-neutral-700"
                        aria-labelledby="hs-dropdown-with-icons">
                        <div class="py-2 first:pt-0 last:pb-0">

                            <template v-for="_movie_duration in movie_durations">
                                <div class="flex items-center gap-x-3.5 py-2 px-3 rounded-lg text-sm text-neutral-800 hover:bg-neutral-100 focus:outline-none focus:bg-neutral-100 dark:text-neutral-400 dark:hover:bg-neutral-700 dark:hover:text-neutral-300 dark:focus:bg-neutral-700 cursor-pointer"
                                    @click="movie_duration = _movie_duration">
                                    {{ _movie_duration }}
                                </div>
                            </template>
                        </div>
                    </div>
                </div>
            </div>

            <div class="mt-7 gap-3 w-full flex flex-row justify-center">
                <button
                    class="py-3 h-10 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-medium rounded-lg border border-neutral-200 bg-white text-neutral-800 shadow-sm hover:bg-neutral-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-white dark:hover:bg-neutral-800 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600"
                    @click="create_movie" :disabled="unfilled">
                    <i class="ti ti-sparkles text-xl"></i>
                    高级模式
                </button>
                <button
                    class="flex-1 h-10 py-3 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-violet-500 text-white hover:bg-violet-600 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600"
                    @click="auto_create_movie" data-hs-overlay="#movie-generation" :disabled="unfilled">
                    <i class="ti ti-target-arrow text-xl"></i>
                    自动成片
                </button>
            </div>

            <div class="hs-overlay hidden size-full fixed top-0 start-0 z-[80] overflow-x-hidden overflow-y-auto"
                id="movie-generation">
                <div
                    class="hs-overlay-open:opacity-100 hs-overlay-open:duration-500 opacity-0 ease-out transition-all h-screen flex justify-center items-center w-screen">
                    <div
                        class="relative flex flex-col bg-white shadow-lg rounded-xl dark:bg-neutral-800 movie-generation-content">
                        <div class="absolute top-2 end-2">
                            <button type="button"
                                class="flex justify-center items-center size-7 text-sm font-semibold rounded-lg border border-transparent text-neutral-800 hover:bg-neutral-100 disabled:opacity-50 disabled:pointer-events-none dark:text-white dark:border-transparent dark:hover:bg-neutral-700 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600"
                                data-hs-overlay="#movie-generation">
                                <span class="sr-only">Close</span>
                                <svg class="flex-shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24"
                                    height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M18 6 6 18" />
                                    <path d="m6 6 12 12" />
                                </svg>
                            </button>
                        </div>

                        <div class="p-4 sm:p-14 text-center overflow-y-hidden">
                            <div class="mb-12">
                                <!-- idea -->
                                <div class="text-xl mb-8" v-if="current_task.idea">
                                    {{ current_task.idea }}
                                </div>
                                <!-- story -->
                                <div class="text-left leading-loose line-clamp-3"
                                    v-if="current_task.story && !current_task.scripts[current_task.frame_num - 1]">
                                    {{ current_task.story }}
                                </div>
                                <!-- scripts -->
                                <div class="text-left leading-loose text-sm"
                                    v-else-if="current_task.scripts[current_task.frame_num - 1] && !current_task.scenes[current_task.frame_num - 1]">
                                    {{ current_task.scripts[random_num] }}
                                </div>
                                <!-- scenes -->
                                <div class="text-left leading-loose"
                                    v-else-if="current_task.scenes[current_task.frame_num - 1] && !current_task.movie">
                                    <img :src="s3_img_path + current_task.scenes[random_num]" alt=""
                                        class="w-4/5 max-w-md m-auto rounded-lg">
                                </div>
                                <div v-if="current_task.movie">
                                    <video controls class="w-full max-w-md rounded-lg mx-auto">
                                        <source :src="s3_movie_path + current_task.movie" type="video/mp4" />
                                    </video>
                                </div>
                            </div>

                            <p class="mb-4">电影正在生成中，请耐心等待。</p>
                            <p class="text-sm">预计将于 5~10 分钟内完成 ☺️</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { computed, onMounted, ref, watch } from 'vue';
import axios from 'axios';
import router from '@/router/router';
import { Clapperboard } from 'lucide-vue-next';
import { current_task, get_current_task } from '@/util/task';
import { s3_img_path, s3_movie_path } from '@/util/api';

const idea = ref("")

const movie_styles = ref(["现代", "古风", "水墨风", "动漫", "赛博朋克风"])
const movie_style = ref("电影风格")
const movie_types = computed(() => {
    switch (movie_style.value) {
        case "现代":
            return ["剧情片", "喜剧片", "爱情片", "科幻片"]
        case "水墨风":
            return ["剧情片", "喜剧片", "爱情片", "武侠片", "奇幻片"]
        case "古风":
            return ["剧情片", "喜剧片", "爱情片", "武侠片", "奇幻片"]
        case "动漫":
            return ["剧情片", "喜剧片", "爱情片"]
        case "赛博朋克风":
            return ["剧情片", "爱情片", "科幻片"]
        default:
            break;
    }
})
const movie_type = ref("电影类型")
watch(movie_style, () => {
    movie_type.value = "电影类型"
})

const movie_durations = ref(["16 秒", "30 秒", "1 分钟", "2 分钟"])
const movie_duration = ref("电影时长")

const idea_hints = ref([
    "人工智能与人类情感纠葛",
    "主角穿越时空",
    "人类与外星人接触的电影",
    "年轻艺术家追求梦想",
    "普通人意外获得超能力"
])
const idea_hint = ref("主角穿越时空")

const duration2frames = (movie_duration: string) => {
    switch (movie_duration) {
        case "16 秒":
            return 4
        case "30 秒":
            return 8
        case "1 分钟":
            return 16
        case "2 分钟":
            return 32
        default:
            break;
    }
}

const random_num = ref(0)
onMounted(() => {
    setInterval(() => {
        random_num.value = Math.floor(Math.random() * current_task.value.frame_num)
    }, 6000)
})

const unfilled = computed(() => {
    if (idea.value == "" ||
        movie_type.value == "电影类型"
        || movie_style.value == "电影风格"
        || movie_duration.value == "电影时长") {
        return true
    }
    else {
        return false
    }
})
const create_movie = () => {
    axios.put("/api/task/", {
        idea: idea.value,
        movie_style: movie_style.value,
        movie_type: movie_type.value,
        frame_num: duration2frames(movie_duration.value)
    }).then(res => {
        const task_id = res.data.task_id
        router.push(`/playground/task/${task_id}`)
    })
}

const auto_create_movie = () => {
    axios.put("/api/task/auto/", {
        idea: idea.value,
        movie_style: movie_style.value,
        movie_type: movie_type.value,
        frame_num: duration2frames(movie_duration.value)
    }).then(res => {
        const task_id = res.data.task_id
        // router.push(`/playground/task/${task_id}`)

        current_task.value.task_id = task_id
        get_current_task()
        setInterval(() => {
            get_current_task()
        }, 4000)
    })
}

onMounted(() => {
    setInterval(() => {
        idea_hint.value = idea_hints.value[Math.floor(Math.random() * idea_hints.value.length)]
    }, 2000)
})
</script>

<style lang="scss">
@property --border-angle {
    syntax: "<angle>";
    inherits: true;
    initial-value: 0turn;
}

.movie-generation-content {
    @apply w-3/5 h-3/5 min-h-96 min-w-96 rounded-2xl border-transparent border-solid border-[5px];
    place-content: center;
    --main-bg: conic-gradient(from var(--border-angle), #fff4f4, #ffe9f6 5%, #dbdfff 60%, #fff4f4 95%);
    --border-angle: 0turn; // For animation.
    --gradient-border: conic-gradient(from var(--border-angle), transparent 25%, #08f, #f03 99%, transparent);
    background:
        // padding-box clip this background in to the overall element except the border.
        var(--main-bg) padding-box,
        // border-box extends this background to the border space
        var(--gradient-border) border-box,
        // Duplicate main background to fill in behind the gradient border. You can remove this if you want the border to extend "outside" the box background.
        var(--main-bg) border-box;

    background-position: center center;
    animation: bg-spin 6s linear infinite;

    @keyframes bg-spin {
        to {
            --border-angle: 1turn;
        }
    }
}

.dark {
    .movie-generation-content {
        @apply text-white;
        --main-bg: conic-gradient(from var(--border-angle), #213, #112 5%, #112 60%, #213 95%);
    }
}
</style>