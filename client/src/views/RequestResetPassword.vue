<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import auth from '../services/auth';
import Button from '../components/Button.vue'
import CustomInput from '../components/Input.vue'
import EmailIcon from '../components/Icons/EmailIcon.vue'
const email = ref('')
const router = useRouter()

const submit = async (e: Event) => {
  e.preventDefault()
  try {
    await auth.requestResetPassword(email.value)
    alert('Un email vous a été envoyé pour réinitialiser votre mot de passe')
  } catch (error) {
    console.error(error)
  }
}

</script>

<template>
  <div class="flex flex-col items-center my-2 login-form gap-y-7">
    <h1 class="text-3xl text-title font-medium">Réinitialiser votre mot de passe</h1>
    <p class="text-center">Saisissez votre adresse email et nous vous enverrons un lien pour réinitialiser votre mot de passe.</p>
    <form class="flex flex-col items-center w-full" @submit="submit">
      <CustomInput v-model="email" type="email" placeholder="Email" class="w-full">
        <template #icon>
          <EmailIcon :size="28" class="absolute inset-y-6 left-0 pl-2" />
        </template>
      </CustomInput>
      <Button type="submit" size="p-2" class="mt-5 py-4 mb-2">Envoyer le lien</Button>
      <RouterLink to="/login" class="text-blue-500 mt-2">Me connecter</RouterLink>
    </form>
  </div>
</template>

<style scoped>
.login-form {
  width: 447px;
}

</style>
