<template>
    <Navbar></Navbar>

    <div class="h-screen flex justify-center w-full">
        <div class="dark:bg-neutral-900 bg-white flex h-full items-center w-full">
            <div class="w-full max-w-md mx-auto p-6 mb-12">
                <div
                    class="mt-7 border border-neutral-200 rounded-xl shadow-sm dark:bg-neutral-800 dark:border-neutral-700">
                    <div class="p-4 sm:p-7">
                        <div class="text-center">
                            <h1 class="block text-2xl font-bold text-neutral-800 dark:text-white">注册</h1>
                            <p class="mt-2 text-sm text-neutral-600 dark:text-neutral-400">
                                已有账号？
                                <RouterLink to="/login">
                                    <span
                                        class="text-violet-600 decoration-2 hover:underline font-medium dark:focus:outline-none dark:focus:outline-1 dark:focus:outline-neutral-600">
                                        现在登录
                                    </span>
                                </RouterLink>
                            </p>
                        </div>

                        <div class="mt-5">
                            <!-- Form -->
                            <form>
                                <div class="grid gap-y-4">
                                    <!-- Form Group -->
                                    <div>
                                        <label for="email" class="block text-sm mb-2 dark:text-white">
                                            邮箱
                                        </label>
                                        <div class="flex gap-x-3">
                                            <input type="email" id="email" name="email"
                                                class="py-3 px-4 block w-full border border-neutral-200 rounded-md text-sm focus:border-violet-500 focus:outline-violet-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:focus:outline-neutral-600"
                                                required aria-describedby="email-error" v-model="email">
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
                                    <div>
                                        <label for="email" class="block text-sm mb-2 dark:text-white">
                                            验证码
                                        </label>
                                        <div class="relative">
                                            <input type="code" id="code" name="code"
                                                class="py-3 px-4 block w-full border border-neutral-200 rounded-lg text-sm focus:border-violet-500 focus:outline-violet-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:focus:outline-neutral-600"
                                                required aria-describedby="email-error" v-model="code">
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
                                        <div class="flex justify-between items-center">
                                            <label for="password" class="block text-sm mb-2 dark:text-white">
                                                密码
                                            </label>
                                        </div>
                                        <div class="relative">
                                            <input type="password" id="password" name="password"
                                                class="py-3 px-4 block w-full border border-neutral-200 rounded-lg text-sm focus:border-violet-500 focus:outline-violet-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:focus:outline-neutral-600"
                                                required aria-describedby="password-error" v-model="password"
                                                @keydown.enter.native='register'>
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
                                        @click="register">注册</div>
                                </div>
                            </form>
                            <!-- End Form -->
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <Footer class="absolute bottom-0"></Footer>
</template>

<script lang="ts">
import Footer from '@/components/Common/Footer.vue';
import Navbar from '@/components/Common/Navbar.vue';
import axios from 'axios';

export default {
    methods: {
        getVerifyCode() {
            if (this.email === '') {
                alert('请输入有效的邮箱');
                return;
            }
            axios.post('/api/account/verifycode/', {
                email: this.email,
            }).then((response) => {
                if (response.data.code == 0) {
                    alert(response.data.message)
                }
            }).catch((error) => {
                console.error(error);
            });
        },
        register() {
            if (this.email === '' || this.code === '' || this.password === '') {
                alert('请输入有效的邮箱和密码');
                return;
            }
            axios.post('/api/account/register/', {
                email: this.email,
                verify_code: this.code,
                password: this.password,
            }).then((response) => {
                if (response.data.status === 'ready') {
                    alert('注册成功');
                    this.$router.push('/login');
                }
                else {
                    alert('注册失败');
                }
            }).catch((error) => {
                console.error(error);
            });
        },
    },
    data() {
        return {
            email: '',
            password: '',
            code: '',
        };
    },
    components: { Navbar, Footer }
};
</script>