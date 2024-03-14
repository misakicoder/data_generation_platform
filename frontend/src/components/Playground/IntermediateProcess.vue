<template>
    <div class="flex flex-col">
        <div class="overflow-x-auto">
            <div class="p-1.5 min-w-full inline-block align-middle">
                <div class="rounded-lg overflow-hidden  border border-neutral-200 dark:border-neutral-700">
                    <table class="min-w-full divide-y divide-neutral-200 dark:divide-neutral-700">
                        <thead class="bg-neutral-50 dark:bg-neutral-700">
                            <tr>
                                <th scope="col"
                                    class="px-6 py-3 text-center text-xs font-medium text-neutral-500 uppercase dark:text-neutral-400 min-w-24">
                                    编号
                                </th>
                                <th scope="col"
                                    class="px-6 py-3 text-center text-xs font-medium text-neutral-500 uppercase dark:text-neutral-400 min-w-80">
                                    脚本
                                </th>
                                <th scope="col"
                                    class="px-6 py-3 text-center text-xs font-medium text-neutral-500 uppercase dark:text-neutral-400 min-w-80">
                                    <!-- 如果 scenes 全是 "" -->
                                    <button v-if="all_scene_empty"
                                        class="py-3 h-8 p-2 inline-flex justify-center items-center gap-x-2 text-xs font-medium rounded-lg border border-neutral-200 bg-white text-neutral-800 shadow-sm hover:bg-neutral-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-white dark:hover:bg-neutral-800 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600"
                                        @click="generate_speeches_all"
                                        :disabled="current_task.scripts.some((script: any) => script == '')">
                                        <i class="ti ti-library-photo"></i>
                                        一键生成旁白
                                    </button>
                                    <span v-else>旁白</span>
                                </th>
                                <th scope="col"
                                    class="px-6 py-3 text-center text-xs font-medium text-neutral-500 uppercase dark:text-neutral-400 min-w-80">
                                    <!-- 如果 scenes 全是 "" -->
                                    <button v-if="all_scene_empty"
                                        class="py-3 h-8 p-2 inline-flex justify-center items-center gap-x-2 text-xs font-medium rounded-lg border border-neutral-200 bg-white text-neutral-800 shadow-sm hover:bg-neutral-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-white dark:hover:bg-neutral-800 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600"
                                        @click="generate_scene_all"
                                        :disabled="current_task.scripts.some((script: any) => script == '')">
                                        <i class="ti ti-library-photo"></i>
                                        一键生成分镜
                                    </button>
                                    <span v-else>分镜</span>
                                </th>
                                <th scope="col"
                                    class="px-6 py-3 text-center text-xs font-medium text-neutral-500 uppercase dark:text-neutral-400 min-w-80">
                                    <button v-if="all_video_empty"
                                        class="py-3 h-8 p-2 inline-flex justify-center items-center gap-x-2 text-xs font-medium rounded-lg border border-neutral-200 bg-white text-neutral-800 shadow-sm hover:bg-neutral-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-white dark:hover:bg-neutral-800 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600"
                                        @click="generate_video_all"
                                        :disabled="current_task.scenes.some((scene: any) => scene == '')">
                                        <i class="ti ti-photo-video"></i>
                                        一键生成视频
                                    </button>
                                    <span v-else>视频</span>
                                </th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-neutral-200 dark:divide-neutral-700">
                            <template v-for="index in Array(current_task.frame_num).keys()">
                                <tr>
                                    <td
                                        class="px-6 py-7 whitespace-nowrap text-center text-sm font-medium text-neutral-800 dark:text-neutral-200 min-w-24">
                                        {{ index + 1 }}</td>
                                    <td
                                        class="py-4 whitespace-nowrap text-center text-sm text-neutral-800 dark:text-neutral-200 min-w-80">
                                        <Script :index="index"
                                            v-on:modify_script="modify_script(index, current_task.scripts[index])">
                                        </Script>
                                    </td>
                                    <td
                                        class="py-4 whitespace-nowrap text-center text-sm text-neutral-800 dark:text-neutral-200 min-w-80">
                                        <Speech :index="index"
                                            v-on:modify_speech="modify_speech(index, current_task.speeches[index])">
                                        </Speech>
                                    </td>
                                    <td
                                        class="py-4 whitespace-nowrap text-center text-sm text-neutral-800 dark:text-neutral-200 min-w-80">
                                        <Scene :index="index" v-on:regenerate="regenerate_scene(index)"
                                            v-on:generate_video="regenerate_video(index)">
                                        </Scene>
                                    </td>
                                    <td
                                        class="py-4 whitespace-nowrap text-center text-sm text-neutral-800 dark:text-neutral-200 min-w-80">
                                        <Video :index="index" v-on:regenerate="regenerate_video(index)"></Video>
                                    </td>
                                </tr>
                            </template>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import Script from "@/components/Playground/Script.vue"
import Speech from "@/components/Playground/Speech.vue"
import Scene from "@/components/Playground/Scene.vue"
import Video from '@/components/Playground/Video.vue';
import axios from 'axios';
import { computed, onMounted } from "vue";
import { current_task, update_current_task } from "@/util/task";

onMounted(() => {
    setTimeout(() => {
        get_scripts()
        get_speeches()
        get_scenes()
        get_videos()
    }, 100);
})

const all_scene_empty = computed(() => current_task.value.scenes.every(scene => scene === ''));
const all_video_empty = computed(() => current_task.value.videos.every(video => video === ''));

const get_scripts = () => {
    axios.get('/api/scripts/', { params: { task_id: current_task.value.task_id } }).then(res => {
        current_task.value.scripts = res.data.scripts
    })
}

const modify_script = (script_index: number, script: string) => {
    axios.post('/api/scripts/', { task_id: current_task.value.task_id, script_index: script_index, script: script }).then(_res => {
        get_scripts()
    })
}

const get_speeches = () => {
    axios.get('/api/speech/', { params: { task_id: current_task.value.task_id } }).then(res => {
        current_task.value.speeches = res.data.speech_descriptions
    })
}

const modify_speech = (speech_index: number, speech_description: string) => {
    axios.post('/api/scripts/', { task_id: current_task.value.task_id, speech_index: speech_index, speech_description: speech_description }).then(_res => {
        get_speeches()
    })
}

const get_scenes = () => {
    axios.get('/api/scenes/', { params: { task_id: current_task.value.task_id } }).then(res => {
        current_task.value.scenes = res.data.scenes
    })
}

const regenerate_scene = (scene_index: number) => {
    if (current_task.value.scripts[scene_index] == "") {
        return
    }

    current_task.value.scenes[scene_index] = ""
    axios.put('/api/scenes/', { task_id: current_task.value.task_id, scene_index: scene_index }).then(_res => {
        update_current_task()
    })
}

const get_videos = () => {
    axios.get('/api/videos/', { params: { task_id: current_task.value.task_id } }).then(res => {
        current_task.value.videos = res.data.videos
    })
}

const regenerate_video = (video_index: number) => {
    if (current_task.value.scenes[video_index] == "") {
        return
    }

    current_task.value.videos[video_index] = ""
    axios.put('/api/videos/', { task_id: current_task.value.task_id, video_index: video_index }).then(_res => {
        update_current_task()
    })
}

const generate_speeches_all = () => {
    current_task.value.status = 'pending'
    axios.put('/api/speech/', { task_id: current_task.value.task_id }).then(_res => {
        update_current_task()
    })
}

const generate_video_all = () => {
    for (let i = 0; i < current_task.value.frame_num; i++) {
        regenerate_video(i)
    }
}

const generate_scene_all = () => {
    for (let i = 0; i < current_task.value.frame_num; i++) {
        regenerate_scene(i)
    }
}
</script>
