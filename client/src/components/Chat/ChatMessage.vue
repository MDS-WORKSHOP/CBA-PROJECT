<template>
  <div class="flex flex-col mb-4 items-start overflow-visible">
    <div class="mr-4 flex items-center mb-2">
      <div class="w-8 h-8 rounded-full overflow-hidden flex items-center justify-center" :class="{'bg-gray-300': message.sender === 'user'}">
        <p v-if="props.message.sender === 'user'" class="font-bold text-gray-800 ">{{ botInitial }}</p>
        <GeorgeIcon :size="31" v-else />
      </div>
      <p class="ml-2 font-bold text-gray-800">{{ props.message.sender === 'user' ? 'Vous' : 'George' }}</p>
    </div>
    <div class="mt-2">
      <span class="p-2 rounded-lg text-sm">{{ props.message.text }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, PropType } from 'vue';
import GeorgeIcon from '../Icons/GeorgeIcon.vue';

interface Message {
  sender: string;
  text: string;
}

const props = defineProps<{
  message: Message
}>();
const botInitial = ref<string>('G');
</script>
