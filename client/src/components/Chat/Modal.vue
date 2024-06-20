<template>
  <div v-if="props.isVisible" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
    <div class="relative flex flex-col justify-evenly bg-white p-6 rounded-lg w-3/4 h-3/4">
      <button @click="$emit('close')" class="text-gray-500 absolute top-0 right-0 mr-2">&times;</button>
      <div v-if="!isPdfPreviewVisible">
        <UploadFileModal @fileUploaded="handleFileUploaded" @close="close" />
      </div>
      <div v-else>
        <PdfPreviewForm :data="pdfData" @close="closePdfPreview" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import UploadFileModal from './UploadFileModal.vue';
import PdfPreviewForm from './PdfPreviewForm.vue';

const emit = defineEmits(['close']);

const props = defineProps({
  isVisible: Boolean
});

const isPdfPreviewVisible = ref(false);
const pdfData = ref(null);

const handleFileUploaded = (data) => {
  pdfData.value = data;
  isPdfPreviewVisible.value = true;
};


const closePdfPreview = () => {
  isPdfPreviewVisible.value = false;
  emit('close');
};
const close = () => {
  emit('close');
};
</script>

<style scoped>
</style>
