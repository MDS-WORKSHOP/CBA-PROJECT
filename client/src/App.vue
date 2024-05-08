<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const message = ref('')
const fetchMessage = async () => {
  const { data } = await axios.get('http://localhost:8000/chatbot/test/') 
  message.value = data.status === 'success' ? data.message : 'Erreur'
}
</script>

<template>
  <div class="flex flex-col items-center my-2">
    <h1 class="text-3xl font-bold">Page de test</h1>
    <span>Test de la connexion</span>
    <button class="bg-sky-500 hover:bg-sky-300 px-5 py-2 text-sm leading-5 rounded-full font-semibold text-white" @click="fetchMessage">Test</button>
    <p v-if="message" class="text-lg mt-2">{{ message }}</p>
  </div>
</template>

<style scoped>

</style>
