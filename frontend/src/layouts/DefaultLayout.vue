<template>
  <div class="px-32 pt-5">
    <header class="navbar bg-base-100 shadow-sm rounded-4xl px-10 border-base-100">
      <div class="navbar-start">
        <router-link to="/" class=" text-xl font-bold text-primary">42Archievements</router-link>
      </div>
      <div class="navbar-center hidden lg:flex">
        <ul class="menu menu-horizontal space-x-6">
          <!-- <li><router-link to="/" class="font-semibold">Home</router-link></li>
          <li><router-link to="/" class="font-semibold">Archievements</router-link></li>
          <li><router-link to="/" class="font-semibold">staff</router-link></li> -->
        </ul>
      </div>
      <div class="navbar-end space-x-5">
        <p class="font-bold text-md">User</p>
        <a class="btn btn-neutral">Logout</a>
      </div>
    </header>

    <main class="my-20 px-10">
      <router-view />
      <slot></slot>
    </main>
  </div>
</template>