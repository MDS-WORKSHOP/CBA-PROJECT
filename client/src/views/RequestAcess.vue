<template>
  <div class="flex flex-col items-center my-2 login-form">
    <h1 class="text-3xl text-title font-medium">Demande d’accès</h1>
    <form class="flex flex-col items-center w-full" @submit="submit">
      <CustomInput v-model="data.email" @input="clearErrors" type="email" placeholder="Email" class="w-full">
        <template #icon>
          <EmailIcon :size="24" class="absolute inset-y-6 left-0 pl-2" />
        </template>
      </CustomInput>
      <CustomInput v-model="data.password" @input="clearErrors" type="password" placeholder="Mot de passe" class="w-full">
        <template #icon>
          <LockIcon :size="24" class="absolute inset-y-6 left-0 pl-2" />
        </template>
      </CustomInput>
      <div class=" flex flex-row w-full gap-2">
        <CustomInput v-model="data.last_name" @input="clearErrors" type="text" placeholder="Nom" class="w-full" />
        <CustomInput v-model="data.first_name" @input="clearErrors" type="text" placeholder="Prénom" class="w-full" />
      </div>
      <Select v-model="data.site" :options="options" placeholder="Site" class="w-full my-2" />
      <Select v-model="data.profile" :options="optionsProfile" placeholder="Profile" class="w-full my-2" />
      <p v-if="errors" class="text-red-500">{{ errors }}</p>
      <Button type="submit" size="p-2" class="mt-5 py-4 mb-2">Confirmer ma demande</Button>
      <RouterLink to="/login" class="text-link mt-2">Me connecter</RouterLink>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import auth from '../services/auth';
import { Sites, Profiles, AccessRequestForm } from '../types/auth';
import Button from '../components/Button.vue'
import Select from '../components/Select.vue'
import CustomInput from '../components/Input.vue'
import LockIcon from '../components/Icons/LockIcon.vue';
import EmailIcon from '../components/Icons/EmailIcon.vue';
import { useToast } from 'vue-toast-notification';

const data = ref<AccessRequestForm>({
  email: '',
  password: '',
  last_name: '',
  first_name: '',
  site: '',
  profile: '',
})

const options = ref(Object.values(Sites))
const optionsProfile = ref(Object.values(Profiles))
const router = useRouter()
const errors = ref('')
const toast = useToast()

const submit = async (e: Event) => {
  e.preventDefault()
  try {
    console.log(data.value)
    await auth.requestAccess(data.value)
    toast.open({
      message: 'Votre demande a été envoyée',
      type: 'success',
      duration: 5000,
      position: 'bottom'
    })
    router.push('/login')
  } catch (error: any) {
    errors.value = error
    data.value = {
      email: '',
      password: '',
      last_name: '',
      first_name: '',
      site: '',
      profile: '',
    }
    console.error(error)
    toast.open({
      message: 'Erreur lors de la demande',
      type: 'error',
      duration: 5000,
      position: 'bottom'
    })
  }
}

const clearErrors = () => {
  errors.value = ''
}

</script>

<style scoped>
.login-form {
  width: 447px;
}

</style>
