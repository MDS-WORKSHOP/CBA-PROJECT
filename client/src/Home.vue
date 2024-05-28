<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'
const email = ref('')
const password = ref('')
const route = useRoute()
const router = useRouter()
const showPassord = ref(false)
const Login = (e: Event) => {
  e.preventDefault()
  axios.post('http://localhost:8000/api/token/', { email: email.value, password: password.value })
    .then(res => {
      localStorage.setItem('accessToken', res.data.access)
      document.cookie = `refreshToken=${res.data.refresh}`
      alert('Login successful')
      router.push('/')
    })
    .catch(err => {
      console.log(err.message)
      alert('Login failed')
    })
}
</script>


<template>
  <div class="flex flex-col items-center my-2">
    <h1 class="text-3xl font-bold">Authentification</h1>
    <form class="flex flex-col items-center" @submit="Login">
      <input type="email" v-model="email" placeholder="Email" class="p-2 m-6 border border-gray-300 rounded-md w-full">
      <input type="password" v-model="password" placeholder="Password" class="p-2 m-2 border border-gray-300 rounded-md w-full">
      <button type="submit" class="bg-blue-500 text-white p-2 m-2 rounded-full w-full">Login</button>
      <RouterLink to="/request-reset-password" class="text-blue-500">Forgot password?</RouterLink>
    </form>
  </div>
</template>

<style scoped>

</style>
