<template>
    <div class="max-w-4xl px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">
        <div class="bg-white rounded-xl p-4 sm:p-7 dark:bg-neutral-900">
            <div class="mb-8">
                <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200">
                    个人信息
                </h2>
            </div>

            <form>
                <!-- Grid -->
                <div class="grid sm:grid-cols-12 gap-2 sm:gap-6">
                    <div class="sm:col-span-3">
                        <label class="inline-block text-sm text-gray-800 mt-2.5 dark:text-gray-200">
                            头像
                        </label>
                    </div>
                    <!-- End Col -->

                    <div class="sm:col-span-9">
                        <div class="flex items-center gap-5">
                            <img class="inline-block size-16 rounded-full ring-2 ring-white dark:ring-gray-800"
                                :src="user_avatar" alt="Image Description">
                        </div>
                    </div>
                    <!-- End Col -->

                    <div class="sm:col-span-3">
                        <label for="af-account-full-name"
                            class="inline-block text-sm text-gray-800 mt-2.5 dark:text-gray-200">
                            用户名
                        </label>
                    </div>
                    <!-- End Col -->

                    <div class="sm:col-span-9">
                        <div class="sm:flex">
                            <input id="af-account-full-name" type="text"
                                class="py-2 px-3 pe-11 block w-full border-gray-200 shadow-sm -mt-px -ms-px first:rounded-t-lg last:rounded-b-lg sm:first:rounded-s-lg sm:mt-0 sm:first:ms-0 sm:first:rounded-se-none sm:last:rounded-es-none sm:last:rounded-e-lg text-sm relative focus:z-10 focus:border-violet-500 focus:ring-violet-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
                                v-model="username" placeholder="用户名">
                        </div>
                    </div>
                    <!-- End Col -->

                    <div class="sm:col-span-3">
                        <label for="af-account-email"
                            class="inline-block text-sm text-gray-800 mt-2.5 dark:text-gray-200">
                            邮箱
                        </label>
                    </div>
                    <!-- End Col -->

                    <div class="sm:col-span-9">
                        <input id="af-account-email" type="email"
                            class="py-2 px-3 pe-11 block w-full border-gray-200 shadow-sm text-sm rounded-lg focus:border-violet-500 focus:ring-violet-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
                            placeholder="maria@site.com" v-model="email">
                    </div>
                    <!-- End Col -->

                    <div class="sm:col-span-3">
                        <label for="af-account-bio"
                            class="inline-block text-sm text-gray-800 mt-2.5 dark:text-gray-200">
                            个人简介
                        </label>
                    </div>
                    <!-- End Col -->

                    <div class="sm:col-span-9">
                        <textarea id="af-account-bio"
                            class="py-2 px-3 block w-full border-gray-200 border rounded-lg text-sm focus:border-violet-500 focus:ring-violet-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
                            rows="6" placeholder="Type your message..." v-model="desc"></textarea>
                    </div>
                    <!-- End Col -->
                </div>
                <!-- End Grid -->

                <div class="mt-5 flex justify-end gap-x-2">
                    <button type="button"
                        class="py-2 px-3 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-violet-600 text-white hover:bg-violet-700 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" @click="updateUserInfo">
                        更新
                    </button>
                </div>
            </form>
        </div>
        <!-- End Card -->
    </div>
    <!-- End Card Section -->
</template>

<script lang="ts" setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';

const user_avatar = ref<string>("https://images.unsplash.com/photo-1709642717827-9621f2a978a1?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw0fHx8ZW58MHx8fHx8")
const username = ref<string>("")
const email = ref<string>('')
const desc = ref<string>('')

const getUserInfo = () => {
    axios.get('/api/account/').then(res => {
        username.value = res.data.username
        email.value = res.data.email
        desc.value = res.data.desc
        user_avatar.value = res.data.user_avatar
    }).catch(err => {
        console.log(err)
    })
}

const updateUserInfo = () => {
    axios.post('/api/account/', {
        username,
        user_avatar,
        desc
    }).then(res => {
        console.log(res)
    }).catch(err => {
        console.log(err)
    })
}

onMounted(async () => {
    await getUserInfo()
})


</script>