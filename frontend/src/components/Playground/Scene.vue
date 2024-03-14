<template>
    <div>
        <div class="relative w-full" v-if="current_task.scenes[props.index]">
            <img class="w-72 h-auto rounded-lg inline-block" :src="s3_img_path + current_task.scenes[props.index]"
                alt="...">

            <!-- Toolbar -->
            <div class="absolute top-px inset-x-px p-2 rounded-b-md w-72 m-auto">
                <div class="flex justify-end items-center gap-x-1">
                    <!-- Button Group -->
                    <button type="button"
                        class="inline-flex flex-shrink-0 justify-center items-center h-8 w-8 bg-white dark:bg-neutral-600 rounded-lg text-neutral-500 hover:text-violet-600 focus:z-10 focus:outline-none focus:ring-2 focus:ring-violet-500 dark:hover:text-violet-500 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600"
                        @click="regenerate_me">
                        <i class="ti ti-rotate-clockwise"></i>
                    </button>
                </div>
            </div>
            <!-- End Toolbar -->
        </div>
        <div class="flex justify-center items-center" v-else>
            <div class="flex animate-pulse w-72 opacity-80">
                <div
                    class="w-72 h-[10.4rem] flex flex-col  border shadow-sm rounded-xl dark:border-neutral-700 dark:shadow-neutral-700/[.7] bg-neutral-50  dark:bg-neutral-700">
                    <div class="flex flex-auto flex-col justify-center items-center p-4 md:p-5" @click="regenerate_me"
                        :disabled="!current_task.scripts[index]"
                        :class="{ 'hover:scale-105 cursor-pointer': current_task.scripts[index] }">
                        <i class="ti ti-photo-scan text-xl"></i>
                        <span class="text-xs">生成分镜图片</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { s3_img_path } from '@/util/api';
import { current_task } from '@/util/task';

const props = defineProps(["index"]);
const emit = defineEmits(['regenerate'])

const regenerate_me = () => {
    emit("regenerate");
}
</script>