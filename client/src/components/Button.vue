<!-- src/components/Button.vue -->
<template>
  <button class="w-full text-lg font-bold" :class="classes" @click="handleClick" :disabled="disabled">
    <slot />
  </button>
</template>

<script setup lang="ts">
import { defineProps, computed } from 'vue'

const props = defineProps({
  type: { type: String, default: 'button' },
  color: { type: String, default: 'bg-blue-500' },
  size: { type: String, default: 'p-2' },
  disabled: { type: Boolean, default: false },
  outlined: { type: Boolean, default: false },
  onClick: Function
})

const classes = computed(() => [
  props.size,
  props.disabled ? 'opacity-50 cursor-not-allowed' : '',
  props.outlined ? 'border-button border-solid border-2 text-button' : 'bg-button text-white'
].join(' '))

const handleClick = (event: Event) => {
  if (!props.disabled && props.onClick) {
    props.onClick(event)
  }
}
</script>

<style scoped>

</style>
