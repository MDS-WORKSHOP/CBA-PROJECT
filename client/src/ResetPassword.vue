<!-- create a new file in the client/src directory called ResetPassword.vue -->
<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'
const password = ref('')
const confirmPassword = ref('')
const route = useRoute()
const router = useRouter()
const token = route.query.token as string


const ResetPassword = (e: Event) => {
  e.preventDefault()
  console.log(token)
  // check if password and confirmPassword are the same
  if (password.value !== confirmPassword.value) {
    alert('Passwords do not match')
    return
  }
  axios.post('http://localhost:8000/api/password-reset-confirm/', { new_password: password.value, token })
    .then(res => {
      alert('Password reset successful')
      router.push('/login')
    })
    .catch(err => {
      console.log(err.message)
    })
}
</script>
<template>
  <div class="flex flex-col items-center my-2">
    <h1 class="text-3xl font-bold">Reset Password</h1>
    <form class="flex flex-col items-center" @submit="ResetPassword">
      <input type="password" v-model="password" placeholder="Password" class="p-2 m-6 border border-gray-300 rounded-md w-full">
      <input type="password" v-model="confirmPassword" placeholder="Confirm Password" class="p-2 m-2 border border-gray-300 rounded-md w-full">
      <button type="submit" class="bg-blue-500 text-white p-2 m-2 rounded-full w-full">Reset Password</button>
      <RouterLink to="/" class="text-blue-500">Login</RouterLink>
    </form>
  </div>
</template>