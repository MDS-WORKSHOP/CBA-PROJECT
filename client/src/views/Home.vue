<script setup lang="ts">
import { ref, nextTick, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import ChatMessage from '../components/Chat/ChatMessage.vue';
import ChatInput from '../components/Chat/ChatInput.vue';
import Modal from '../components/Chat/Modal.vue';

const messages = ref<{ sender: string, text: string }[]>([]);
const isLoading = ref(false);
const isFileUploadModalVisible = ref(false);
const chatContainer = ref<HTMLElement | null>(null);
const router = useRouter();
const messagesContainer = ref<HTMLElement | null>(null);
import api from '../services/api';

const ask = async (text: string) => {
  try {
    const response = await api.post('/ask/', { question: text });
    console.log(response.data)
    return response.data.ai_response;
    isLoading.value = false;
  } catch (error) {
    console.error(error);
    return null;
  }
};

const sendMessage = async (text: string) => {
  messages.value.push({ sender: 'user', text });
  isLoading.value = true;
  const response = await ask(text);
  if (response) {
    messages.value.push({ sender: 'bot', text: response });
  }
  nextTick(() => {
    scrollToBottom();
  });
  // setTimeout(() => {
  //   messages.value.push({ sender: 'bot', text: 'Je suis George, que puis-je faire pour vous ?' });
  //   isLoading.value = false;
  //   nextTick(() => {
  //     scrollToBottom();
  //   });
  // }, 1000);
};

const scrollToBottom = () => {
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight;
  }
};

const toggleFileUploadModal = () => {
  isFileUploadModalVisible.value = !isFileUploadModalVisible.value;
};

const logout = () => {
  localStorage.removeItem('accessToken');
  document.cookie = 'refreshToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
  router.push('/login');
};

onMounted(() => {
  scrollToBottom();
});
</script>

<template>
  <div class="flex flex-col h-screen bg-gray-100">
    <header class="p-4 text-center font-bold text-2xl flex justify-between items-center">
      <div></div>
      <span>CBA - AIR FRANCE KLM</span>
      <button class="bg-red-500 text-white p-2 m-2" @click="logout">Déconnexion</button>
    </header>
    <div class="flex-grow grid grid-cols-12 p-4">
      <div class="col-span-1"></div>
      <div class="col-span-1"></div>
      <div class="col-span-1"></div>
      <div ref="messagesContainer" class="col-span-6 flex flex-col h-3/4 overflow-scroll">
        <div class="flex-grow p-4" ref="chatContainer">
          <div>
            <ChatMessage class="my-8" v-for="(message, index) in messages" :key="index" :message="message" />
          </div>
        </div>
      </div>
      <div class="col-span-1"></div>
      <div class="col-span-1"></div>
      <div class="col-span-1"></div>
    </div>
    <div class="fixed bottom-0 left-0 w-full bg-gray-100 p-4">
      <div class="grid grid-cols-12">
        <div class="col-span-1"></div>
        <div class="col-span-1"></div>
        <div class="col-span-1"></div>
        <div class="col-span-6">
          <ChatInput @sendMessage="sendMessage" @toggleFileUploadModal="toggleFileUploadModal" />
        </div>
        <div class="col-span-1"></div>
        <div class="col-span-1"></div>
        <div class="col-span-1"></div>
      </div>
    </div>
    <Modal :isVisible="isFileUploadModalVisible" @close="toggleFileUploadModal" />
  </div>
</template>

<style scoped>
</style>
