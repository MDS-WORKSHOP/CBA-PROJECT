import { createWebHistory, createRouter } from 'vue-router'
import DefaultLayout from './layouts/DefaultLayout.vue'
import AuthLayout from './layouts/Auth.vue'
import Login from './Login.vue'
import RequestResetPassword from './RequestResetPassword.vue'
import ResetPassword from './ResetPassword.vue'
import Home from './Home.vue'

const routes = [
  {
    path: '/',
    component: DefaultLayout,
    children: [
      { path: '', component: Home }
    ]
  },
  {
    path: '/login',
    component: AuthLayout,
    children: [
      { path: '', component: Login }
    ]
  },
  {
    path: '/request-reset-password',
    component: AuthLayout,
    children: [
      { path: '', component: RequestResetPassword }
    ]
  },
  {
    path: '/reset-password',
    component: AuthLayout,
    children: [
      { path: '', component: ResetPassword }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const publicPages = ['/', '/login', '/request-reset-password', '/reset-password']
  const authRequired = !publicPages.includes(to.path)
  const loggedIn = localStorage.getItem('accessToken')

  if (authRequired && !loggedIn) {
    return next('/login')
  }

  next()
})

export default router
