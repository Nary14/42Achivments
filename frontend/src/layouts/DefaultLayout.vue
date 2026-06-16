<template>
  <div class="px-32 pt-10">
    <header class="navbar bg-base-100 shadow-sm rounded-4xl px-10 border-b border-b-emerald-300">
      <div class="navbar-start">
        <p class=" text-xl font-bold text-primary">42Archivement</p>
      </div>
      <div class="navbar-center hidden lg:flex">
        <ul class="menu menu-horizontal px-1">
          <!-- <li><router-link to="/">Archivement</router-link></li>
          <li><router-link to="/">staff</router-link></li> -->
        </ul>
      </div>
      <div class="navbar-end space-x-10">
        <p class="font-bold text-md">User</p>
        <a class="btn btn-primary">Logout</a>
      </div>
    </header>

    <main class="content">
      <router-view />
    </main>
  </div>
</template>