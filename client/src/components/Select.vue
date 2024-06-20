<template>
  <select v-model="modelValue" class="py-4 border border-gray-300 w-full pl-3 outline-none">
    <option value="" disabled>{{ props.placeholder }}</option>
    <option v-for="option in props.options" :value="option">{{ option }}</option>
  </select>
</template>

<script setup lang="ts">
import { defineProps } from 'vue'
const modelValue = defineModel()
const props = defineProps({
  options: { type: Array, default: () => [] },
  placeholder: { type: String, default: 'Select an option' },
})
</script>
