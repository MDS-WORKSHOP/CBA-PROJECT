<template>
  <div class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
    <div class="relative flex flex-col justify-evenly bg-white p-6 rounded-lg w-3/4 h-3/4">
      <button @click="$emit('close')" class="text-gray-500 absolute top-0 right-0 mr-2">&times;</button>
      <div class="flex justify-center mb-4">
        <div class="flex flex-col">
          <h2 class="text-xl font-bold text-center">Extraction de données</h2>
          <span class="text-[#969696] text-center w-[330px] mb-6">Récupérez les informations de vos documents PDF et EXCEL de manière plus rapide.</span>
          <div class="flex flex-col items-center mt-4">
            <Select v-model="data.type" :options="options" placeholder="Choisissez votre type de document" class="w-full my-2" />
          </div>
        </div>
      </div>
      <div v-if="!isLoading" class="flex flex-col items-center justify-center border-2 border-dashed border-gray-300 p-4 text-center w-full h-5/6" @dragover.prevent @drop.prevent="handleDrop" @click="triggerFileInput">
        <Button :disabled="data.type === ''" size="p-2" class="mt-5 py-4 mb-2 max-w-md">Sélectionner votre document</Button>
        <p>Ou déposer votre document ici</p>
        <input type="file" ref="fileInput" :disabled="data.type === ''" class="hidden" accept=".pdf" @change="handleFileChange" />
      </div>
      <div v-else class="flex flex-col items-center justify-center w-full h-5/6">
        <p>Chargement...</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import Button from '../Button.vue';
import api from '../../services/api';
import Select from '../Select.vue';

const emit = defineEmits(['close', 'fileUploaded']);

const file = ref<File | null>(null);
const fileInput = ref<HTMLInputElement | null>(null);
const isLoading = ref(false);

const data = ref({
  type: '',
});

const options = ref([
  "DigitizingSignalOscilloscope",
  "ACPowerSupply",
  "DCLoad",
  "DigitalMultimeter",
  "ProgrammableFunctionGenerator",
  "SynchroResolverModule",
  "OpticalAttenuator",
  "OpticalSwitch",
  "OpticalPowermeter",
  "VideoPatternGenerator",
  "HighLevelPressureGenerator",
  "LowLevelPressureGenerator",
]);

const triggerFileInput = () => {
  if (fileInput.value) {
    fileInput.value.click();
  }
};

const handleFileChange = async (event: Event) => {
  const target = event.target as HTMLInputElement;
  const files = target.files;
  if (files) {
    file.value = files[0];
    await uploadFile();
  }
};

const handleDrop = async (event: DragEvent) => {
  event.preventDefault();
  const files = event.dataTransfer?.files;
  if (files) {
    file.value = files[0];
    await uploadFile();
  }
};

const uploadFile = async () => {
  if (file.value) {
    isLoading.value = true;
    const response = await sendDoc();
    setTimeout(() => {
      const data = {
        pdfFile: file.value,
        form: response.info
      };
      emit('fileUploaded', data);
      isLoading.value = false;
    }, 1000);
  }
};

const sendDoc = async() => {
  const formData = new FormData();
  formData.append('file', file.value as File);
  formData.append('schemma', data.value.type);
  console.log(formData);
  const response = await api.post('/documents/upload/', formData, {
  headers: {
    'Content-Type': 'multipart/form-data'
  }
});
  console.log(response.data);
  return {info: response.data};
}
</script>

<style scoped>
.hidden {
  display: none;
}
</style>
