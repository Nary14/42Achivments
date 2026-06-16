import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Archievements from '@/views/Archievements.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/archievements',
      name: 'archievements',
      component: Archievements,
    },
  ],
})

export default router
