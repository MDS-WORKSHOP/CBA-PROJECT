<!-- create a new file in the client/src directory called ResetPassword.vue -->
<script setup lang="ts">
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import auth from '../services/auth';
import Button from '../components/Button.vue'
import CustomInput from '../components/Input.vue'
import LockIcon from '../components/Icons/LockIcon.vue';
import { useToast } from 'vue-toast-notification';
const password = ref('')
const confirmPassword = ref('')
const route = useRoute()
const router = useRouter()
const token = route.query.token as string
const toast = useToast()


const submit = async (e: Event) => {
  e.preventDefault()
  if (password.value !== confirmPassword.value) {
    toast.open({
      message: 'Les mots de passe ne correspondent pas',
      type: 'error',
      duration: 5000,
      position: 'bottom'
    })
    return
  }
  try {
    await auth.resetPassword(password.value, token)
    toast.open({
      message: 'Votre mot de passe a été réinitialisé',
      type: 'success',
      duration: 5000,
      position: 'bottom'
    })
    router.push('/login')
  } catch (error) {
    console.error(error)
  }
}
</script>
<template>
  <div class="flex flex-col items-center my-2 reset-form">
    <h1 class="text-3xl text-title font-medium">Reset Password</h1>
    <form class="flex flex-col items-center w-full" @submit="submit">
      <CustomInput v-model="password" type="password" placeholder="Password" class="w-full">
        <template #icon>
          <LockIcon :size="24" class="absolute inset-y-6 left-0 pl-2" />
        </template>
      </CustomInput>
      <CustomInput v-model="confirmPassword" type="password" placeholder="Password" class="w-full">
        <template #icon>
          <LockIcon :size="24" class="absolute inset-y-6 left-0 pl-2" />
        </template>
      </CustomInput>
      <Button type="submit" size="p-2" class="mt-5 py-4 mb-2">Reset Password</Button>
      <RouterLink to="/" class="text-blue-500">Login</RouterLink>
    </form>
  </div>
</template>

<style scoped>
.reset-form {
  width: 447px;
}

</style>
