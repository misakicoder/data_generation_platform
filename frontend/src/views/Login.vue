<template>
    <Navbar></Navbar>

    <div class="h-screen flex justify-center w-full">
        <div class="dark:bg-neutral-900 bg-white flex h-full items-center w-full">
            <div class="w-full max-w-md mx-auto p-6 mb-20">
                <div
                    class="mt-7 border border-neutral-200 rounded-xl shadow-sm dark:bg-neutral-800 dark:border-neutral-700">
                    <div class="p-4 sm:p-7">
                        <div class="text-center">
                            <h1 class="block text-2xl font-bold text-neutral-800 dark:text-white">登录</h1>
                        </div>

                        <div class="mt-5">
                            <!-- Form -->
                            <form>
                                <div class="grid gap-y-4">
                                    <!-- Form Group -->
                                    <div>
                                        <label for="phone_number" class="block text-sm mb-2 dark:text-white">
                                            电话号码
                                        </label>
                                        <div class="flex gap-x-3">
                                            <input type="phone_number" id="phone_number" name="phone_number"
                                                class="py-3 px-4 block w-full border border-neutral-200 rounded-md text-sm focus:border-violet-500 focus:outline-violet-500 disabled:opacity-50 disabled:pointer-events-none white:bg-neutral-900 white:border-neutral-700 white:text-neutral-400 white:focus:outline-neutral-600"
                                                v-model="phone_number">
                                            <button type="button"
                                                class="w-24 h-[2.875rem] flex-shrink-0 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-md border border-transparent bg-violet-500 text-white hover:bg-violet-600 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-neutral-600"
                                                @click="getVerifyCode">
                                                获取验证码
                                            </button>
                                            <div
                                                class="hidden absolute inset-y-0 end-0 items-center pointer-events-none pe-3">
                                                <svg class="h-5 w-5 text-red-500" width="16" height="16"
                                                    fill="currentColor" viewBox="0 0 16 16" aria-hidden="true">
                                                    <path
                                                        d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 4a.905.905 0 0 0-.9.995l.35 3.507a.552.552 0 0 0 1.1 0l.35-3.507A.905.905 0 0 0 8 4zm.002 6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z" />
                                                </svg>
                                            </div>
                                        </div>
                                        <p class="hidden text-xs text-red-600 mt-2" id="email-error">Please include a
                                            valid
                                            email address so we can get back to you</p>
                                    </div>
                                    <!-- End Form Group -->

                                    <!-- Form Group -->
                                    <div>
                                        <label for="verify_code" class="block text-sm mb-2 dark:text-white">
                                            验证码
                                        </label>
                                        <div class="relative">
                                            <input type="verify_code" id="verify_code" name="verify_code"
                                                class="py-3 px-4 block w-full border border-neutral-200 rounded-lg text-sm focus:border-violet-500 focus:outline-violet-500 disabled:opacity-50 disabled:pointer-events-none white:bg-neutral-900 white:border-neutral-700 white:text-neutral-400 white:focus:outline-neutral-600"
                                                v-model="verify_code">
                                            <div
                                                class="hidden absolute inset-y-0 end-0 items-center pointer-events-none pe-3">
                                                <svg class="h-5 w-5 text-red-500" width="16" height="16"
                                                    fill="currentColor" viewBox="0 0 16 16" aria-hidden="true">
                                                    <path
                                                        d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 4a.905.905 0 0 0-.9.995l.35 3.507a.552.552 0 0 0 1.1 0l.35-3.507A.905.905 0 0 0 8 4zm.002 6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z" />
                                                </svg>
                                            </div>
                                        </div>
                                        <p class="hidden text-xs text-red-600 mt-2" id="password-error">8+ characters
                                            required
                                        </p>
                                    </div>
                                    <!-- End Form Group -->

                                    <div class="w-full py-3 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-violet-500 text-white hover:bg-violet-600 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:outline-1 dark:focus:outline-neutral-600 cursor-pointer"
                                        @click="login">登录</div>
                                </div>
                            </form>
                            <!-- End Form -->
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- <Footer class="absolute bottom-0"></Footer> -->
</template>
<script lang="ts" setup>
import Footer from '@/components/Common/Footer.vue';
import Navbar from '@/components/Common/Navbar.vue';
import router from '@/router/router';
import { is_login } from '@/util/user';
import axios from 'axios';
import { el } from 'element-plus/es/locale';
import { reactive, ref } from 'vue';


const phone_number = ref('');

const verify_code = ref('');

const getVerifyCode = () => {
    if (phone_number.value == '') {
        alert('电话号码不能为空');
        return;
    }

    axios.post('/api/verify_code/',{phone_num : phone_number.value}).then(res => {
        if (res.data.status == 'success') {
            alert('验证码已发送');
        } else {
            alert('验证码发送失败');
        }
    }).catch(err => {
        console.error(err);
    })
}

const login = () => {
    if (phone_number.value == '' || verify_code.value == '') {
        alert('电话号码或密码不能为空');
        return;
    }

    axios.post('/api/login/', {phone_num : phone_number.value,verification_code : verify_code.value}).then(res => {
        if (res.data.status == 'success') {
            is_login.value = true;
            router.push('/playground/all');
        } else if (res.data.status == 'Invalid verification'){
            alert('验证码错误');
        } else {
            alert('登录失败');
        }
    }).catch(err => {
        console.error(err);
    })
}
</script>