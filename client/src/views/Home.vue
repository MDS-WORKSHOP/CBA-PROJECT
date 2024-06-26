<template>
  <div class="flex flex-col h-screen bg-gray-100">
    <header class="p-4 text-center font-bold text-xl flex justify-between items-center relative">
      <div></div>
      <RouterLink to="/"><span>CBA - AIR FRANCE KLM</span></RouterLink>
      <DropDown class="absolute right-24" />
    </header>
    <div class="flex-grow grid h-full grid-cols-12 p-4">
      <div class="col-span-1"></div>
      <div class="col-span-1"></div>
      <div class="col-span-1"></div>
      <div ref="messagesContainer" class="col-span-6 flex flex-col h-3/4 overflow-scroll">
        <div class="flex-grow p-4" ref="chatContainer">
          <div v-if="messages.length">
            <ChatMessage class="my-8" v-for="(message, index) in messages" :key="index" :message="message" />
            <div v-if="isLoading" class="font-medium flex flex-col justify-center pt-4">
              <div>
                <div class="flex items-center mb-2">
                  <GeorgeIcon :size="31" />
                  <p class="ml-2 font-bold text-gray-800">George</p>
                </div>
                <span class="p-2 rounded-lg text-sm">Je suis en train de réfléchir...</span>
              </div>
            </div>
          </div>
          <div v-else class="text-center text-3xl font-medium flex flex-col justify-center items-center">
            <div>
              <span>Bonjour, je suis George</span>
                <GeorgeIcon class="inline-block mx-2" />
                <br />
              <span>qu’est-ce que je peux faire pour vous ?</span>
            </div>
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
          <ChatInput @sendMessage="sendMessage" @toggleFileUploadModal="toggleFileUploadModal" @clearConv="clearConv" />
        </div>
        <div class="col-span-1"></div>
        <div class="col-span-1"></div>
        <div class="col-span-1"></div>
      </div>
    </div>
    <Modal :isVisible="isFileUploadModalVisible" @close="toggleFileUploadModal" />
  </div>
</template>

<script setup lang="ts">
import { ref, nextTick, onMounted } from 'vue';
import ChatMessage from '../components/Chat/ChatMessage.vue';
import ChatInput from '../components/Chat/ChatInput.vue';
import Modal from '../components/Chat/Modal.vue';
import DropDown from '../components/DropDown.vue';
import GeorgeIcon from '../components/Icons/GeorgeIcon.vue';
import api from '../services/api';
import { useUserStore } from '../store/modules/user';
import { useToast } from 'vue-toast-notification';

const messages = ref<{ sender: string, text: string }[]>([]);
const isLoading = ref(false);
const isFileUploadModalVisible = ref(false);
const chatContainer = ref<HTMLElement | null>(null);
const messagesContainer = ref<HTMLElement | null>(null);
const toast = useToast();


const ask = async (text: string) => {
  try {
    const conversionId = sessionStorage.getItem('conversionId');
    if (!conversionId) {
      const response = await api.post('/conversations/');
      sessionStorage.setItem('conversionId', response.data.id);
      return askQuestion(text, response.data.id);
    } else {
      return askQuestion(text, conversionId);
    }
  } catch (error) {
    console.error(error);
    return null;
  }
};

const askQuestion = async (text: string, conversionId: any) => {
  try {
    const response = await api.post('/ask/', { question: text, conversation_id: conversionId});
    return response.data.ai_response;
  } catch (error) {
    console.error(error);
    return null;
  }
};

const getUser = async () => {
  await useUserStore().fetchUserData();
};

const sendMessage = async (text: string) => {
  messages.value.push({ sender: 'user', text });
  scrollToBottom();
  isLoading.value = true;
  const response = await ask(text);
  if (response) {
    messages.value.push({ sender: 'bot', text: response });
    isLoading.value = false;
  }
  nextTick(() => {
    scrollToBottom();
  });
};

const scrollToBottom = () => {
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight;
  }
};

const toggleFileUploadModal = () => {
  isFileUploadModalVisible.value = !isFileUploadModalVisible.value;
};

const clearConv = () => {
  messages.value = [];
  sessionStorage.removeItem('conversionId');
  toast.open({
    message: 'Conversation effacée',
    type: 'success',
    duration: 5000,
    position: 'bottom'
  });
};

onMounted(() => {
  getUser();
  scrollToBottom();
});
</script>

<style scoped>
</style>
