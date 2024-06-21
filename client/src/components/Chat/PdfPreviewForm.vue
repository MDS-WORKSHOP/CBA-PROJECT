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
          <form @submit.prevent="submitForm" class="bg-[#F9F9F9] px-6">
            <template v-for="(value, key) in formData" :key="key" class="mb-4 p-4">
              <div v-if="value !== null && value !== '' && !(Array.isArray(value) && value.length === 0)" class="px-2 py-3">
                <label :for="key" class="block text-[#051039] normal-case">{{ key }}</label>
                <input :id="key" v-model="formData[key]" class="w-full bg-[#F9F9F9] pt-2 px-2 pb-6 border-b-2 outline-none" readonly />
              </div>
            </template>
            <Button type="submit" size="p-2" class="mt-5 py-4 mb-2">Valider les informations</Button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue';
import Button from '../Button.vue';
import { useToast } from 'vue-toast-notification';

const props = defineProps({
  data: {
    type: Object,
    default: () => ({})
  }
});
const emit = defineEmits(['close']);
const toast = useToast();

const pdfUrl = computed(() => {
  if (props.data.pdfFile) {
    return URL.createObjectURL(new Blob([props.data.pdfFile], { type: 'application/pdf' }));
  }
  return null;
});

const formData = ref<{ [key: string]: any }>({ ...props.data.form });

const submitForm = () => {
  toast.open({
    message: 'Document envoyé avec succès',
    type: 'success',
    duration: 5000,
    position: 'bottom'
  });
  emit('close');
};

watch(() => props.data, (newData) => {
  formData.value = { ...newData.form };
});
</script>

<style scoped>
</style>
