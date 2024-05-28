import { createWebHistory, createRouter } from 'vue-router'

import Home from './Home.vue'
import RequestResetPassword from './RequestResetPassword.vue'
import ResetPassword from './ResetPassword.vue'
import Home1 from './Home1.vue'

const routes = [
  { path: '/', component: Home1 },
  { path: '/login', component: Home },
  { path: '/request-reset-password', component: RequestResetPassword },
  { path: '/reset-password', component: ResetPassword },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})
router.beforeEach((to, from, next) => {
  const publicPages = ['/login', '/request-reset-password', '/reset-password']
  const authRequired = !publicPages.includes(to.path)
  const loggedIn = localStorage.getItem('accessToken')
  if (authRequired && !loggedIn) {
    return next('/login')
  }
  next()
})
export default router