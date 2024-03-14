<template>
    <div>
        <div class="relative w-full" v-if="current_task.speeches[props.index]">
            <textarea id="hs-textarea-ex-1"
                class="p-4 pb-12 block w-full border border-neutral-200 rounded-lg text-sm focus:border-violet-500 focus:ring-violet-500 disabled:opacity-50 disabled:pointer-events-none  dark:border-neutral-700 dark:text-neutral-400 dark:focus:ring-neutral-600 outline-none"
                rows="5" placeholder="旁白……" v-model="current_task.speeches[props.index]"
                @blur="modify_speech"></textarea>
        </div>
        <div class="flex flex-col" v-else>
            <div class="flex animate-pulse w-full p-4">
                <div class="w-full">
                    <ul class="space-y-3">
                        <li class="w-full h-2 bg-neutral-200 rounded-full dark:bg-neutral-700" v-for="_i in 2"></li>
                        <li class="w-1/2 h-2 bg-neutral-200 rounded-full dark:bg-neutral-700"></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { current_task } from '@/util/task';

const props = defineProps(["index"]);
const emit = defineEmits(['modify_speech'])

const modify_speech = () => {
    emit("modify_speech");
}
</script>