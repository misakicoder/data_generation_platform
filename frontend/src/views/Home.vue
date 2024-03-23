<template>
    <div>
        <img :src="example_image" alt="Image" class="fixed top-0 h-full w-full object-cover">

        <div class="h-screen w-full flex justify-center items-center absolute">
            <div class="text-center py-12 px-6 sm:px-6 lg:px-10" style="position:absolute;left:550px;top:100px">
                <h1 class="text-4xl flex justify-center items-center text-center my-4">
                    <img src="/fish.png" alt="Image" class="w-9 h-9 mr-2">
                    <span class="text-black-500 bg-clip-text text-transparent bg-black pl-2">
                        全面的数据生成平台
                    </span>
                </h1>
                <div>
                    <RouterLink to = '/login'>
                        <div
                            class="inline-flex m-3 justify-center items-center gap-x-3 text-center text-white font-medium rounded-md focus:outline-none focus:ring-2 py-1 px-4 bg-gradient-to-r from-blue-500 to-violet-500 hover:scale-105 duration-200 text-lg">
                            <i class="ti ti-arrow-loop-right text-lg"></i>
                            开始生成
                        </div>
                    </RouterLink>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
// import { is_login } from '@/util/user';

// random video
const example_image = "/backend.jpg";

</script>

<style></style>