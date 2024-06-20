<template>
  <div class="relative w-full py-2">
    <input
      v-model="inputValue"
      :placeholder="props.placeholder"
      :type="props.type"
      class="py-4 border border-gray-300 w-full"
      :class="$slots.icon ? 'pl-8' : 'pl-4'"
      @input="updateValue"
      v-bind="$attrs"
    />
    <slot name="icon" />
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, ref, watch } from 'vue';

const props = defineProps({
  modelValue: String,
  placeholder: { type: String, default: 'Enter your text' },
  type: { type: String, default: 'text' },
});

const emit = defineEmits(['update:modelValue']);

const inputValue = ref(props.modelValue);

const updateValue = (event: any) => {
  inputValue.value = event.target.value;
  emit('update:modelValue', inputValue.value);
};

watch(() => props.modelValue, (newValue) => {
  inputValue.value = newValue;
});
</script>
