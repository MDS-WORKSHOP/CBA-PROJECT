import { createWebHistory, createRouter } from 'vue-router'
import DefaultLayout from './layouts/DefaultLayout.vue'
import AuthLayout from './layouts/Auth.vue'
import Login from './views/Login.vue'
import RequestResetPassword from './views/RequestResetPassword.vue'
import ResetPassword from './views/ResetPassword.vue'
import Home from './views/Home.vue'
import RequestAcess from './views/RequestAcess.vue'
import Admin from './views/Admin.vue'

const routes = [
  {
    path: '/',
    component: DefaultLayout,
    children: [
      { path: '', component: Home },
      { path: '/admin', component: Admin }
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
  },
  {
    path: '/request-access',
    component: AuthLayout,
    children: [
      { path: '', component: RequestAcess }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const publicPages = ['/', '/login', '/request-reset-password', '/reset-password', '/request-access']
  const authRequired = !publicPages.includes(to.path)
  const loggedIn = localStorage.getItem('accessToken')

  if (authRequired && !loggedIn) {
    return next('/login')
  }

  next()
})

export default router
