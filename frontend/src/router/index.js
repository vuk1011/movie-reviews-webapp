import { createRouter, createWebHistory } from 'vue-router'
import MovieView from '@/views/MovieView.vue'
import HomeView from '@/views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movies/:id',
    name: 'movie',
    component: MovieView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router