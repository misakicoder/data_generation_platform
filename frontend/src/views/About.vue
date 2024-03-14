<template>
    <Navbar></Navbar>
    <div class="pt-24">

        <div class="max-w-5xl px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">
            <!-- Title -->
            <div class="max-w-2xl mx-auto text-center mb-10 lg:mb-14">
                <h2 class="text-2xl font-bold md:text-4xl md:leading-tight dark:text-white">产品团队</h2>
            </div>
            <!-- End Title -->

            <!-- Grid -->
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-8 md:gap-12">
                <template v-for="person in people">
                    <div class="text-center">
                        <img class="rounded-full w-24 h-24 mx-auto" :src="person.image" alt="Image Description">
                        <div class="mt-2 sm:mt-4">
                            <h3 class="font-medium text-neutral-800 dark:text-neutral-200">
                                {{ person.name }}
                            </h3>
                            <p class="text-sm text-neutral-600 dark:text-neutral-400">
                                {{ person.position }}
                            </p>
                        </div>
                    </div>
                </template>
            </div>
            <!-- End Grid -->
        </div>
    </div>

    <Footer></Footer>
</template>

<script lang="ts" setup>
import Footer from '@/components/Common/Footer.vue';
import Navbar from '@/components/Common/Navbar.vue';

const people = [
    {
        name: 'David Forren',
        position: 'Founder / CEO',
        image: 'https://images.unsplash.com/photo-1568602471122-7832951cc4c5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=2&w=900&h=900&q=80'
    },
    {
        name: 'Amil Evara',
        position: 'UI/UX Designer',
        image: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=2&w=900&h=900&q=80'
    },
    {
        name: 'Ebele Egbuna',
        position: 'Support Consultant',
        image: 'https://images.unsplash.com/photo-1548142813-c348350df52b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=2&w=900&h=900&q=80'
    },
    {
        name: 'Maria Powers',
        position: 'Director of sales',
        image: 'https://images.unsplash.com/photo-1598929213452-52d72f63e307?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=2&w=900&h=900&q=80'
    },
    {
        name: 'Delia Pawelke',
        position: 'Front-end Developer',
        image: 'https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=2&w=900&h=900&q=80'
    }
]
</script>