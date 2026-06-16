<script setup lang="ts">
    import DefaultLayout from '@/layouts/DefaultLayout.vue';
    import {Mouse} from '@lucide/vue'
</script>

<template>
    <DefaultLayout>
        <div>
            <h1 class="font-bold text-6xl">Hello, <span class="">student</span></h1>
            <h2 class="my-5 text-4xl font-semibold">Discover your achievements</h2>
        </div>
        <div class="mt-9">
            <div class="flex items-center-safe justify-between">
                <div>
                    <p class="font-bold text-center">Last achievements</p>
                </div>
                <div>
                    <button class="btn btn-soft">
                        <router-link to="/archievements">
                            See All Archievements
                        </router-link>
                    </button>
                </div>
            </div>
            <div class="my-10 flex flex-wrap gap-4 justify-center">
                <div class="card card-side bg-base-100 border-base-300 border">
                    <div class="card-body">
                        <h2 class="card-title">New movie is released!</h2>
                        <p>Click the button to watch on Jetflix app.</p>
                    </div>
                    <div class="flex justify-center items-center-safe rounded-r-2xl bg-base-300 px-7">
                        <Mouse/>
                    </div>
                </div>
                <div class="card card-side bg-base-100 border-base-300 border">
                    <div class="card-body">
                        <h2 class="card-title">New movie is released!</h2>
                        <p>Click the button to watch on Jetflix app.</p>
                    </div>
                    <div class="flex justify-center items-center-safe rounded-r-2xl bg-base-300 px-7">
                        <Mouse/>
                    </div>
                </div><div class="card card-side bg-base-100 border-base-300 border">
                    <div class="card-body">
                        <h2 class="card-title">New movie is released!</h2>
                        <p>Click the button to watch on Jetflix app.</p>
                    </div>
                    <div class="flex justify-center items-center-safe rounded-r-2xl bg-base-300 px-7">
                        <Mouse/>
                    </div>
                </div><div class="card card-side bg-base-100 border-base-300 border">
                    <div class="card-body">
                        <h2 class="card-title">New movie is released!</h2>
                        <p>Click the button to watch on Jetflix app.</p>
                    </div>
                    <div class="flex justify-center items-center-safe rounded-r-2xl bg-base-300 px-7">
                        <Mouse/>
                    </div>
                </div>
            </div>
    </div>
    </DefaultLayout>
</template>