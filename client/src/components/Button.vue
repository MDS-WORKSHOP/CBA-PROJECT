<!-- src/components/Button.vue -->
<template>
  <button class="text-white w-full" :class="classes" @click="handleClick" :disabled="disabled">
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
  onClick: Function
})

const classes = computed(() => [
  props.color,
  props.size,
  props.disabled ? 'opacity-50 cursor-not-allowed' : ''
].join(' '))

const handleClick = (event: Event) => {
  if (!props.disabled && props.onClick) {
    props.onClick(event)
  }
}
</script>

<style scoped>

</style>
