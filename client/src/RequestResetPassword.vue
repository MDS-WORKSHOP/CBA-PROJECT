<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
const email = ref('')
const RequestResetPassword = (e: Event) => {
  e.preventDefault()
  axios.post('http://localhost:8000/api/password-reset-request/', { email: email.value })
    .then(res => {
      alert('Password reset link sent to your email')
    })
    .catch(err => {
      console.log(err.message)
    })
}
</script>
<template>
  <div class="flex flex-col items-center my-2">
    <h1 class="text-3xl font-bold">Request Reset Password</h1>
    <form class="flex flex-col items-center" @submit="RequestResetPassword">
      <input type="email" v-model="email" placeholder="Email" class="p-2 m-6 border border-gray-300 rounded-md w-full">
      <button type="submit" class="bg-blue-500 text-white p-2 m-2 rounded-full w-full">Request Reset Password</button>
      <RouterLink to="/login" class="text-blue-500">Login</RouterLink>
    </form>
  </div>
</template>