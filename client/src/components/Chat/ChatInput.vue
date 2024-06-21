<template>
  <div class="p-4 border-t border-gray-200 flex items-center">
    <div class="relative w-full flex">
      <span class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
        <LoopIcon />
      </span>
      <textarea
        v-model="message"
        @keydown.enter="submitMessage"
        class="w-full pl-12 pr-16 py-5 bg-[#051039] text-white resize-none overflow-hidden"
        placeholder="Poser votre question"
        rows="1"
        @input="adjustTextareaHeight"
        ref="textarea"
      ></textarea>
      <button @click="submitMessage" class="absolute inset-y-0 right-0 flex items-center pr-3 text-white">
        <div class="bg-[#FFFFFF] bg-opacity-25 p-2">
          <SendIcon />
        </div>
      </button>
    </div>
    <button @click="toggleFileUploadModal" class="ml-4 bg-[#0045B6] h-auto text-white p-3">
      <UploadIcon :size="42" />
    </button>
    <button @click="clearConv" class="ml-4 h-auto text-white p-3">
      <ReloadIcon :size="42" />
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import LoopIcon from '../Icons/LoopIcon.vue';
import SendIcon from '../Icons/SendIncon.vue';
import UploadIcon from '../Icons/UploadIcon.vue';
import ReloadIcon from '../Icons/Reloadicon.vue';

const message = ref('');
const textarea = ref(null);

const emit = defineEmits(['sendMessage', 'toggleFileUploadModal', 'clearConv']);

const submitMessage = (event) => {
  if (message.value.trim() !== '') {
    emit('sendMessage', message.value);
    message.value = '';
    resetTextareaHeight();
    event.preventDefault();
  }
};

const toggleFileUploadModal = () => {
  console.log('toggleFileUploadModal');
  emit('toggleFileUploadModal');
};

const clearConv = () => {
  emit('clearConv');
};

const adjustTextareaHeight = () => {
  const el = textarea.value;
  if (el) {
    el.style.height = 'auto';
    el.style.height = `${el.scrollHeight}px`;
  }
};

const resetTextareaHeight = () => {
  const el = textarea.value;
  if (el) {
    el.style.height = 'auto';
  }
};

onMounted(() => {
  adjustTextareaHeight();
});
</script>

<style scoped>
</style>
