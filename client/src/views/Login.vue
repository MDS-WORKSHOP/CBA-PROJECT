<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import auth from '../services/auth';
import Button from '../components/Button.vue'
import CustomInput from '../components/Input.vue'
import LockIcon from '../components/Icons/LockIcon.vue';
import EmailIcon from '../components/Icons/EmailIcon.vue';
const email = ref('')
const password = ref('')
const router = useRouter()

const submit = async (e: Event) => {
  e.preventDefault()
  try {
    await auth.login(email.value, password.value)
    const accessToken = localStorage.getItem('accessToken')
    if (accessToken) {
      router.push('/')
    }
  } catch (error) {
    console.error(error)
  }
}

</script>

<template>
  <div class="flex flex-col items-center my-2 login-form">
    <h1 class="text-3xl text-title font-medium">Connexion</h1>
    <form class="flex flex-col items-center w-full" @submit="submit">
      <CustomInput v-model="email" type="email" placeholder="Email" class="w-full">
        <template #icon>
          <EmailIcon :size="24" class="absolute inset-y-6 left-0 pl-2" />
        </template>
      </CustomInput>
      <CustomInput v-model="password" type="password" placeholder="Password" class="w-full">
        <template #icon>
          <LockIcon :size="24" class="absolute inset-y-6 left-0 pl-2" />
        </template>
      </CustomInput>
      <Button type="submit" size="p-2" class="mt-5 py-4 mb-2">Me connecter</Button>
      <RouterLink to="/request-reset-password" class="text-link mt-2">Mot de passe oublié ?</RouterLink>
      <div class="border-solid border-t-[1.5px] border-[#DDDDDD] w-full my-8"></div>
      <RouterLink to="/request-access" class="w-full">
        <Button outlined type="submit" color="border-button" size="p-2" class="mt-5 py-4 mb-2">Demande d'accès</Button>
      </RouterLink>
    </form>
  </div>
</template>

<style scoped>
.login-form {
  width: 447px;
}

</style>
