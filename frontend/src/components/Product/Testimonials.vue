<template>
    <!-- Testimonials -->
    <div class="max-w-[85rem] px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">
        <!-- Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            <template v-for="testimonial in testimonials">
                <!-- Card -->
                <div
                    class="flex flex-col border border-neutral-200 shadow-sm rounded-xl dark:bg-neutral-900 dark:border-neutral-700 p-4 hover:scale-105 duration-200 m-1">

                    <div class="flex-auto p-4 md:p-6">
                        <blockquote class="relative">
                            <svg class="absolute -top-6 -start-8 h-16 w-16 text-neutral-100 dark:text-neutral-700" width="16"
                                height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"
                                aria-hidden="true">
                                <path
                                    d="M7.39762 10.3C7.39762 11.0733 7.14888 11.7 6.6514 12.18C6.15392 12.6333 5.52552 12.86 4.76621 12.86C3.84979 12.86 3.09047 12.5533 2.48825 11.94C1.91222 11.3266 1.62421 10.4467 1.62421 9.29999C1.62421 8.07332 1.96459 6.87332 2.64535 5.69999C3.35231 4.49999 4.33418 3.55332 5.59098 2.85999L6.4943 4.25999C5.81354 4.73999 5.26369 5.27332 4.84476 5.85999C4.45201 6.44666 4.19017 7.12666 4.05926 7.89999C4.29491 7.79332 4.56983 7.73999 4.88403 7.73999C5.61716 7.73999 6.21938 7.97999 6.69067 8.45999C7.16197 8.93999 7.39762 9.55333 7.39762 10.3ZM14.6242 10.3C14.6242 11.0733 14.3755 11.7 13.878 12.18C13.3805 12.6333 12.7521 12.86 11.9928 12.86C11.0764 12.86 10.3171 12.5533 9.71484 11.94C9.13881 11.3266 8.85079 10.4467 8.85079 9.29999C8.85079 8.07332 9.19117 6.87332 9.87194 5.69999C10.5789 4.49999 11.5608 3.55332 12.8176 2.85999L13.7209 4.25999C13.0401 4.73999 12.4903 5.27332 12.0713 5.85999C11.6786 6.44666 11.4168 7.12666 11.2858 7.89999C11.5215 7.79332 11.7964 7.73999 12.1106 7.73999C12.8437 7.73999 13.446 7.97999 13.9173 8.45999C14.3886 8.93999 14.6242 9.55333 14.6242 10.3Z"
                                    fill="currentColor" />
                            </svg>

                            <div class="relative z-10">
                                <p class="text-neutral-800 text-lg dark:text-white"><em>
                                        {{ testimonial.comment }}
                                    </em></p>
                            </div>
                        </blockquote>
                    </div>

                    <div class="p-4 rounded-b-xl md:px-6">
                        <h3 class="text-sm font-semibold text-neutral-800 sm:text-base dark:text-neutral-200">
                            {{ testimonial.name }}
                        </h3>
                        <p class="text-sm text-neutral-500">
                            {{ testimonial.position }}
                        </p>
                    </div>
                </div>
                <!-- End Card -->
            </template>
        </div>
        <!-- End Grid -->
    </div>
    <!-- End Testimonials -->
</template>

<script lang="ts" setup>
const testimonials = [
    {
        name: '张伟',
        position: '电影制作人',
        comment: '使用 FilmAction 真让我大开眼界。它不仅可以快速生成高质量的图像和场景，还可以根据我的需求进行个性化定制，这节省了我大量的时间和成本，让我能够更专注于创意和故事本身。'
    },
    {
        name: '李娜',
        position: '编剧',
        comment: '我一直在寻找能够将我的创意转化为视觉形式的工具，FilmAction 正好满足了我的需求。它能够快速生成符合我剧本的角色和场景，让我能更专注于故事的发展和情节的推敲。真的太棒了！'
    },
    {
        name: '刘洋',
        position: '大学生',
        comment: '我一直对电影制作充满兴趣，但苦于没有专业的设备和技能。使用 FilmAction，我可以轻松制作出自己的电影作品，真是太神奇了！它不仅操作简单，而且生成的画面效果也非常棒。我一直推荐给朋友们，让大家都能发挥创意和想象力。'
    }
]
</script>