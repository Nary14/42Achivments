<script setup lang="ts">
    import DefaultLayout from '@/layouts/DefaultLayout.vue';
    import {Mouse} from '@lucide/vue'
    import {Search} from '@lucide/vue'
</script>

<template>
    <DefaultLayout>
        <div>
            <h1 class="font-bold text-6xl">Archievements</h1>
            <h2 class="my-5 text-4xl font-semibold">Let's claim your achievements</h2>
        </div>
        <div class="mt-9">
            <div class="flex items-center-safe justify-between flex-wrap">
                <div>
                    <p class="font-bold text-center">All Achievements</p>
                </div>
                <ul class="menu menu-vertical lg:menu-horizontal bg-base-200 rounded-box">
                    <li><a>All</a></li>
                    <li><a>Project</a></li>
                    <li><a>Social</a></li>
                    <li><a>Scolarity</a></li>
                    <li><a>Pedagogy</a></li>
                </ul>
                <div>
                    <label class="input">
                        <Search />
                        <input type="search" required placeholder="Search" />
                    </label>
                </div>
            </div>
            <div class="my-10 flex flex-wrap gap-4 justify-center">
                <div class="card card-side bg-base-100 border-base-300 border">
                    <div class="flex justify-center items-center-safe rounded-l-md bg-base-300 px-7">
                        <Mouse/>
                    </div>
                    <div class="card-body">
                        <h2 class="card-title">New movie is released!</h2>
                        <p>Click the button to watch on Jetflix app.</p>
                        <div class="justify-end card-actions mt-5 mb-0">
                            <button class="btn btn-md">Claim Now</button>
                        </div>
                    </div>
                </div>
                <div class="card card-side bg-base-100 border-base-300 border">
                    <div class="flex justify-center items-center-safe rounded-l-md bg-base-300 px-7">
                        <Mouse/>
                    </div>
                    <div class="card-body">
                        <h2 class="card-title">New movie is released!</h2>
                        <p>Click the button to watch on Jetflix app.</p>
                        <div class="justify-end card-actions mt-5 mb-0">
                            <button class="btn btn-md">Claim Now</button>
                        </div>
                    </div>
                </div>
                <div class="card card-side bg-base-100 border-base-300 border">
                    <div class="flex justify-center items-center-safe rounded-l-md bg-base-300 px-7">
                        <Mouse/>
                    </div>
                    <div class="card-body">
                        <h2 class="card-title">New movie is released!</h2>
                        <p>Click the button to watch on Jetflix app.</p>
                        <div class="justify-end card-actions mt-5 mb-0">
                            <button class="btn btn-md">Claim Now</button>
                        </div>
                    </div>
                </div>
                <div class="card card-side bg-base-100 border-base-300 border">
                    <div class="flex justify-center items-center-safe rounded-l-md bg-base-300 px-7">
                        <Mouse/>
                    </div>
                    <div class="card-body">
                        <h2 class="card-title">New movie is released!</h2>
                        <p>Click the button to watch on Jetflix app.</p>
                        <div class="justify-end card-actions mt-5 mb-0">
                            <button class="btn btn-md">Claim Now</button>
                        </div>
                    </div>
                </div>
            </div>
    </div>
    </DefaultLayout>
</template>