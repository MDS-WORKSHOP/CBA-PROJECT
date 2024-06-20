<template>
  <div ref="dropdown" class="relative inline-block">
    <div @click="toggleDropdown" class="cursor-pointer flex items-center justify-center h-16">
      <Account />
    </div>

    <div v-if="isOpen" class="origin-top absolute right-1/2 transform translate-x-1/2 mt-2 w-56 shadow-lg bg-white ring-1 ring-black ring-opacity-5">
      <div>
        <h2 class="text-center font-normal text-white bg-[#0045B6] p-2 text-xl">ACCÈS AU COMPTE</h2>
        <div class="px-6 py-2 cursor-pointer font-normal hover:bg-gray-100 flex justify-between items-center text-lg" @click="logout">
          <Exit />
          <span class="pr-2">Me déconnecter</span>
        </div>
        <hr />
        <div class="px-6 py-2 cursor-pointer font-normal hover:bg-gray-100 flex justify-between items-center text-lg" @click="requestAccess">
          <Access />
          <span>Demande d’accès</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import Account from './Icons/AccountIcon.vue';
import Exit from './Icons/ExitIcon.vue';
import Access from './Icons/Access.vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const isOpen = ref(false);
const dropdown = ref<HTMLElement | null>(null);

const toggleDropdown = () => {
  isOpen.value = !isOpen.value;
};

const logout = () => {
  localStorage.removeItem('accessToken');
  document.cookie = 'refreshToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
  router.push('/login');
};

const requestAccess = () => {
  router.push('/admin');
};

const handleClickOutside = (event: MouseEvent) => {
  if (dropdown.value && !dropdown.value.contains(event.target as Node)) {
    isOpen.value = false;
  }
};

onMounted(() => {
  document.addEventListener('click', handleClickOutside);
});

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
});
</script>

<style scoped>
</style>
