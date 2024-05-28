<!-- create a new file in the client/src directory called Home1.vue -->
<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()
const Logout = () => {
  localStorage.removeItem('accessToken')
  document.cookie = 'refreshToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;'
  router.push('/login')
}
</script>
<template>
  <div class="flex flex-col items-center my-2">
    <h1 class="text-3xl font-bold">Home</h1>
    <p>Welcome to the home page</p>
    <button class="bg-red-500 text-white p-2 m-2 rounded-full" @click="Logout">Logout</button>
  </div>
</template>