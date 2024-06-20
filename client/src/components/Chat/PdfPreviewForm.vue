<template>
  <div class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
    <div class="relative flex flex-col bg-white p-6 rounded-lg w-3/4 h-3/4">
      <button @click="$emit('close')" class="text-gray-500 absolute top-0 right-0 mr-2">&times;</button>
      <div class="flex flex-row h-full">
        <div class="w-1/2 h-full overflow-auto">
          <h2 class="text-xl font-bold text-center mb-4">Aperçu du PDF</h2>
          <iframe v-if="pdfUrl" :src="pdfUrl" class="w-full h-full"></iframe>
        </div>
        <div class="w-1/2 h-full overflow-auto p-4">
          <h2 class="text-xl font-bold text-center mb-4">Informations du PDF</h2>
          <form @submit.prevent="submitForm">
            <div v-for="(value, key) in formData" :key="key" class="mb-4">
              <label :for="key" class="block text-gray-700">{{ key }}</label>
              <input :id="key" v-model="formData[key]" class="w-full p-2 border rounded" />
            </div>
            <button type="submit" class="bg-blue-500 text-white p-2 rounded">Soumettre</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue';

const props = defineProps({
  data: {
    type: Object,
    default: () => ({})
  }
});
const emit = defineEmits(['close']);

const pdfUrl = computed(() => {
  if (props.data.pdfFile) {
    return URL.createObjectURL(new Blob([props.data.pdfFile], { type: 'application/pdf' }));
  }
  return null;
});

const formData = ref<{ [key: string]: any }>({ ...props.data.form });

const submitForm = () => {
  console.log('Form data submitted:', formData.value);
  // Envoyer les données au back-end si nécessaire
  emit('close');
};

watch(() => props.data, (newData) => {
  formData.value = { ...newData.form };
});
</script>

<style scoped>
</style>
