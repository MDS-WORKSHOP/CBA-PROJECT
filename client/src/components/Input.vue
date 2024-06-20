
<template>
  <div class="relative w-full py-2">
    <input
      v-model="modelValue"
      :placeholder="props.placeholder"
      :type="props.type"
      class="py-4 border border-gray-300 w-full"
      :class="$slots.icon ? 'pl-8' : 'pl-4'"
      v-bind="$attrs"
    />
    <slot name="icon" />
  </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue'

const modelValue = defineModel()
const props = defineProps({
  placeholder: { type: String, default: 'Enter your text' },
  type: { type: String, default: 'text' },
})

</script>
