<template>
    <header
        class="flex flex-wrap sm:justify-start sm:flex-nowrap z-50 w-full text-sm sm:py-0 fixed top-0 bg-white/20 text-white disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 dark:bg-neutral-900/20 backdrop-blur-sm">
        <nav class="relative max-w-7xl w-full mx-auto p-2 sm:flex sm:items-center sm:justify-between sm:px-6 lg:px-8"
            aria-label="Global">
            <div class="flex items-center justify-between">
                <div class="sm:hidden">
                    <button type="button"
                        class="hs-collapse-toggle w-9 h-9 flex justify-center items-center text-sm font-semibold rounded-lg border border-neutral-200 text-neutral-800 hover:bg-neutral-100 disabled:opacity-50 disabled:pointer-events-none dark:text-white dark:border-neutral-700 dark:hover:bg-neutral-700 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600"
                        data-hs-collapse="#navbar-collapse-with-animation" aria-controls="navbar-collapse-with-animation"
                        aria-label="Toggle navigation">
                        <div class="hs-collapse-open:hidden">
                            <i class="ti ti-menu-2 text-lg"></i>
                        </div>

                        <div class="hs-collapse-open:block flex-shrink-0 hidden w-4 h-4">
                            <i class="ti ti-x text-lg"></i>
                        </div>
                    </button>
                </div>
            </div>
            <div id="navbar-collapse-with-animation"
                class="hs-collapse hidden overflow-hidden transition-all duration-300 basis-full grow sm:block">
                <div
                    class="flex flex-col gap-y-4 gap-x-0 mt-5 sm:flex-row sm:items-center sm:justify-end sm:gap-y-0 sm:gap-x-7 sm:mt-0 sm:ps-7">
                    <div class="font-medium text-neutral-500 hover:text-neutral-400 dark:text-neutral-400 dark:hover:text-neutral-500 select-none cursor-pointer text-lg"
                        @click="toggleDark()">
                        <i class="ti ti-sun-high" v-if="isDark"></i>
                        <i class="ti ti-moon-stars" v-else></i>
                    </div>

                    <!-- <RouterLink to="pricing">
                        <a
                            class="font-medium text-neutral-500 hover:text-neutral-400 dark:text-neutral-400 dark:hover:text-neutral-500">现在订阅</a>
                    </RouterLink> -->

                    <!-- <RouterLink to="/about">
                        <a
                            class="font-medium text-neutral-500 hover:text-neutral-400 dark:text-neutral-400 dark:hover:text-neutral-500">关于我们</a>
                    </RouterLink> -->


                    <!-- <RouterLink to="/login">
                        <a
                            class="flex items-center gap-x-2 font-medium text-neutral-500 hover:text-violet-600 sm:border-s sm:border-neutral-300 sm:my-6 sm:ps-6 dark:border-neutral-700 dark:text-neutral-400 dark:hover:text-violet-500">
                            登录
                        </a>
                    </RouterLink> -->
                </div>
            </div>
        </nav>
    </header>
</template>

<script lang="ts" setup>
import { is_login } from '@/util/user';
import { Clapperboard } from 'lucide-vue-next';
import { useDark, useToggle } from '@vueuse/core'

const isDark = useDark()
const toggleDark = useToggle(isDark)
</script>   