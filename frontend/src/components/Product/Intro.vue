<template>
    <!-- Hero -->
    <div
        class="relative overflow-hidden before:absolute before:top-0 before:start-1/2 before:bg-no-repeat before:bg-top before:w-full before:h-full before:-z-[1] before:transform before:-tranneutral-x-1/2">
        <div class="max-w-[85rem] mx-auto px-4 sm:px-6 lg:px-8 py-32">
            <!-- Title -->
            <div class="mt-5 max-w-xl text-center mx-auto">
                <h1 class="block font-bold text-neutral-800 text-4xl md:text-5xl lg:text-6xl dark:text-neutral-200">
                    <span class="bg-clip-text text-transparent bg-gradient-to-r from-pink-500 to-violet-500">
                        想象力
                    </span>
                    照进现实
                </h1>
            </div>
            <!-- End Title -->

            <div
                class="mt-6 max-w-3xl text-center m-auto flex flex-col justify-center items-center sm:flex-row text-lg text-neutral-600 dark:text-neutral-400">
                <p>
                    释放您的导演天赋，
                </p>
                <p>
                    与 FilmAction 共创精彩
                </p>
            </div>

            <!-- Buttons -->
            <div class="mt-8 gap-3 flex justify-center">
                <RouterLink :to="is_login ? '/playground/all' : '/login'">
                    <div
                        class="inline-flex justify-center items-center gap-x-3 text-center text-white text-sm font-medium rounded-full focus:outline-none focus:ring-2 py-3 px-4 dark:focus:ring-offset-neutral-800 bg-gradient-to-r from-pink-500 to-violet-500 hover:scale-105 duration-200">
                        <i class="ti ti-arrow-loop-right text-lg"></i>
                        即刻体验
                    </div>
                </RouterLink>
            </div>
            <!-- End Buttons -->
        </div>
    </div>
    <!-- End Hero -->
</template>

<script lang="ts" setup>
import { is_login } from '@/util/user';

</script>