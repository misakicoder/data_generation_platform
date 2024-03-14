<template>
    <!-- Features -->
    <div class="max-w-[85rem] px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">
        <div class="relative p-6 md:p-16">
            <!-- Grid -->
            <div class="relative z-10 lg:grid lg:grid-cols-12 lg:gap-16 lg:items-center">
                <div class="mb-10 lg:mb-0 lg:col-span-6 lg:col-start-8 lg:order-2">
                    <h2 class="text-2xl text-neutral-800 font-bold sm:text-3xl dark:text-neutral-200">
                        无论资历深浅，FilmAction都能满足您对电影的探索与体验。
                    </h2>

                    <!-- Tab Navs -->
                    <nav class="grid gap-4 mt-5 md:mt-10" aria-label="Tabs" role="tablist">
                        <button type="button"
                            class="hs-tab-active:bg-white hs-tab-active:shadow-md hs-tab-active:hover:border-transparent text-start hover:bg-neutral-200 p-4 md:p-5 rounded-xl dark:hs-tab-active:bg-neutral-900 dark:hover:bg-neutral-700 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600 active"
                            id="tabs-with-card-item-1" data-hs-tab="#tabs-with-card-1" aria-controls="tabs-with-card-1"
                            role="tab">
                            <span class="flex">
                                <i
                                    class="ti ti-automatic-gearbox text-3xl flex-shrink-0 mt-2 h-6 w-6 md:w-7 md:h-7 hs-tab-active:text-violet-500 text-neutral-800 dark:hs-tab-active:text-violet-400 dark:text-neutral-200"></i>

                                <span class="grow ms-6">
                                    <span
                                        class="block text-lg font-semibold hs-tab-active:text-violet-500 text-neutral-800 dark:hs-tab-active:text-violet-400 dark:text-neutral-200">全自动电影制作</span>
                                    <span
                                        class="block mt-1 text-neutral-800 dark:hs-tab-active:text-neutral-200 dark:text-neutral-200">利用先进的AI技术，无论是剧本创作、角色设定、影片生成还是后期剪辑，FilmAction都能独立完成。</span>
                                </span>
                            </span>
                        </button>

                        <button type="button"
                            class="hs-tab-active:bg-white hs-tab-active:shadow-md hs-tab-active:hover:border-transparent text-start hover:bg-neutral-200 p-4 md:p-5 rounded-xl dark:hs-tab-active:bg-neutral-900 dark:hover:bg-neutral-700 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600"
                            id="tabs-with-card-item-2" data-hs-tab="#tabs-with-card-2" aria-controls="tabs-with-card-2"
                            role="tab">
                            <span class="flex">
                                <i
                                    class="ti ti-photo-sensor-3 text-3xl flex-shrink-0 mt-2 h-6 w-6 md:w-7 md:h-7 hs-tab-active:text-violet-500 text-neutral-800 dark:hs-tab-active:text-violet-400 dark:text-neutral-200"></i>
                                <span class="grow ms-6">
                                    <span
                                        class="block text-lg font-semibold hs-tab-active:text-violet-500 text-neutral-800 dark:hs-tab-active:text-violet-400 dark:text-neutral-200">多元电影主题与风格</span>
                                    <span
                                        class="block mt-1 text-neutral-800 dark:hs-tab-active:text-neutral-200 dark:text-neutral-200">无论是科幻、悬疑、喜剧还是剧情片，用户都能在FilmAction中找到心仪的创作方向。</span>
                                </span>
                            </span>
                        </button>

                        <button type="button"
                            class="hs-tab-active:bg-white hs-tab-active:shadow-md hs-tab-active:hover:border-transparent text-start hover:bg-neutral-200 p-4 md:p-5 rounded-xl dark:hs-tab-active:bg-neutral-900 dark:hover:bg-neutral-700 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600"
                            id="tabs-with-card-item-3" data-hs-tab="#tabs-with-card-3" aria-controls="tabs-with-card-3"
                            role="tab">
                            <span class="flex">
                                <i
                                    class="ti ti-movie text-3xl flex-shrink-0 mt-2 h-6 w-6 md:w-7 md:h-7 hs-tab-active:text-violet-500 text-neutral-800 dark:hs-tab-active:text-violet-400 dark:text-neutral-200"></i>
                                <span class="grow ms-6">
                                    <span
                                        class="block text-lg font-semibold hs-tab-active:text-violet-500 text-neutral-800 dark:hs-tab-active:text-violet-400 dark:text-neutral-200">高质量视效与叙事能力</span>
                                    <span
                                        class="block mt-1 text-neutral-800 dark:hs-tab-active:text-neutral-200 dark:text-neutral-200">通过深度学习和大量的数据训练，FilmAction能够模拟出专业级的电影制作效果，为用户带来震撼体验。</span>
                                </span>
                            </span>
                        </button>
                    </nav>
                    <!-- End Tab Navs -->
                </div>
                <!-- End Col -->

                <div class="lg:col-span-6">
                    <div class="relative">
                        <!-- Tab Content -->
                        <div>
                            <div id="tabs-with-card-1" role="tabpanel" aria-labelledby="tabs-with-card-item-1">
                                <img class="shadow-xl shadow-neutral-200 rounded-xl dark:shadow-neutral-900/[.2] max-w-lg"
                                    src="https://images.unsplash.com/photo-1605629921711-2f6b00c6bbf4?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&h=1220&q=80"
                                    alt="Image Description">
                            </div>

                            <div id="tabs-with-card-2" class="hidden" role="tabpanel"
                                aria-labelledby="tabs-with-card-item-2">
                                <img class="shadow-xl shadow-neutral-200 rounded-xl dark:shadow-neutral-900/[.2] max-w-lg"
                                    src="https://images.unsplash.com/photo-1665686306574-1ace09918530?ixlib=rb-4.0.3&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&h=1220&q=80"
                                    alt="Image Description">
                            </div>

                            <div id="tabs-with-card-3" class="hidden" role="tabpanel"
                                aria-labelledby="tabs-with-card-item-3">
                                <img class="shadow-xl shadow-neutral-200 rounded-xl dark:shadow-neutral-900/[.2] max-w-lg"
                                    src="https://images.unsplash.com/photo-1598929213452-52d72f63e307?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&h=1220&q=80"
                                    alt="Image Description">
                            </div>
                        </div>
                        <!-- End Tab Content -->

                        <!-- SVG Element -->
                        <div class="hidden absolute top-0 end-0 tranneutral-x-20 md:block lg:tranneutral-x-20">
                            <svg class="w-16 h-auto text-orange-500" width="121" height="135" viewBox="0 0 121 135"
                                fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M5 16.4754C11.7688 27.4499 21.2452 57.3224 5 89.0164" stroke="currentColor"
                                    stroke-width="10" stroke-linecap="round" />
                                <path d="M33.6761 112.104C44.6984 98.1239 74.2618 57.6776 83.4821 5" stroke="currentColor"
                                    stroke-width="10" stroke-linecap="round" />
                                <path d="M50.5525 130C68.2064 127.495 110.731 117.541 116 78.0874" stroke="currentColor"
                                    stroke-width="10" stroke-linecap="round" />
                            </svg>
                        </div>
                        <!-- End SVG Element -->
                    </div>
                </div>
                <!-- End Col -->
            </div>
            <!-- End Grid -->

            <!-- Background Color -->
            <div class="absolute inset-0 grid grid-cols-12 w-full h-full">
                <div
                    class="col-span-full lg:col-span-7 lg:col-start-6 bg-neutral-100 w-full h-5/6 rounded-xl sm:h-3/4 lg:h-full dark:bg-white/[.075]">
                </div>
            </div>
            <!-- End Background Color -->
        </div>
    </div>
    <!-- End Features -->
</template>

<script lang="ts" setup>
</script>