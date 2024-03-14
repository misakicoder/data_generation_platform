<script lang="ts" setup>
import { Clapperboard } from 'lucide-vue-next';
</script>

<template>
    <footer class="w-full max-w-[85rem] py-10 px-4 sm:px-6 lg:px-8 mx-auto">
        <!-- Grid -->
        <div class="text-center">
            <div>
                <router-link to="/">
                    <div class="flex-none text-xl font-semibold text-black dark:text-white dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600"
                        aria-label="Brand">
                        <div class="flex justify-center items-center text-xl font-semibold">
                            <Clapperboard :size="20" class="text-pink-500 dark:text-white" />
                            <span
                                class="dark:text-white bg-clip-text text-transparent bg-gradient-to-r from-pink-500 to-violet-500 pl-2">
                                FilmAction
                            </span>
                        </div>
                    </div>
                </router-link>
            </div>
            <!-- End Col -->

            <!-- Social Brands -->
            <div class="mt-3 space-x-2">
                <div
                    class="inline-flex justify-center items-center w-10 h-10 text-center text-neutral-800 hover:bg-neutral-100 rounded-full focus:outline-none focus:ring-2 focus:ring-violet-600 focus:ring-offset-2 focus:ring-offset-white transition dark:text-neutral-200 dark:hover:text-neutral-200 dark:hover:bg-neutral-800 cursor-pointer">
                    <i class="ti ti-brand-wechat"></i>
                </div>
                <div
                    class="inline-flex justify-center items-center w-10 h-10 text-center text-neutral-800 hover:bg-neutral-100 rounded-full focus:outline-none focus:ring-2 focus:ring-violet-600 focus:ring-offset-2 focus:ring-offset-white transition dark:text-neutral-200 dark:hover:text-neutral-200 dark:hover:bg-neutral-800 cursor-pointer">
                    <i class="ti ti-brand-tiktok-filled"></i>
                </div>
                <div
                    class="inline-flex justify-center items-center w-10 h-10 text-center text-neutral-800 hover:bg-neutral-100 rounded-full focus:outline-none focus:ring-2 focus:ring-violet-600 focus:ring-offset-2 focus:ring-offset-white transition dark:text-neutral-200 dark:hover:text-neutral-200 dark:hover:bg-neutral-800 cursor-pointer">
                    <i class="ti ti-notebook"></i>
                </div>
            </div>
            <!-- End Social Brands -->
        </div>
        <!-- End Grid -->
    </footer>
</template>