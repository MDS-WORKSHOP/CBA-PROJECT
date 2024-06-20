<template>
  <div class="p-4 border-t border-gray-200 flex items-center">
    <div class="relative w-full">
      <span class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
        <LoopIcon />
      </span>
      <input
        type="text"
        v-model="message"
        @keydown.enter="submitMessage"
        class="w-full pl-12 py-5 bg-[#051039] text-white"
        placeholder="Poser votre question"
      />
      <button @click="submitMessage" class="absolute inset-y-0 right-0 flex items-center pr-3 text-white">
        <div class="bg-[#FFFFFF] bg-opacity-25 p-2">
          <SendIcon />
        </div>
      </button>
    </div>
    <button @click="toggleFileUploadModal" class="ml-4 bg-[#0045B6] h-auto text-white p-3">
      <UploadIcon :size="42" />
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import LoopIcon from '../Icons/LoopIcon.vue';
import SendIcon from '../Icons/SendIncon.vue';
import UploadIcon from '../Icons/UploadIcon.vue';

const message = ref('');

const emit = defineEmits(['sendMessage', 'toggleFileUploadModal']);

const submitMessage = () => {
  if (message.value !== '') {
    emit('sendMessage', message.value);
    message.value = '';
  }
};

const toggleFileUploadModal = () => {
  console.log('toggleFileUploadModal');
  emit('toggleFileUploadModal');
};
</script>

<style scoped>
</style>
