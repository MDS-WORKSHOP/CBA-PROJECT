<template>
  <div class="flex flex-col h-screen">
    <header class="p-4 text-center font-bold text-xl flex justify-between items-center relative">
      <div></div>
      <RouterLink to="/"><span>CBA - AIR FRANCE KLM</span></RouterLink>
      <DropDown class="absolute right-24" />
    </header>
    <h1 class="text-4xl mb-4 mt-8 text-center text-[#051039] font-medium">Autorisation des demandes d’accès</h1>
    <div class="mx-28">
      <table class="min-w-full bg-white">
        <thead class="bg-white">
          <tr class="text-[#051039]">
            <th class="py-4 bg-white text-center border-0">Nom</th>
            <th class="py-4 bg-white text-center border-0">Prénom</th>
            <th class="py-4 bg-white text-center border-0">Site</th>
            <th class="py-4 bg-white text-center border-0">Date de demande d'accès</th>
            <th class="py-4 bg-white text-center border-0">Statut</th>
            <th class="py-4 bg-white text-center border-0">Autorisation</th>
          </tr>
        </thead>
        <tbody>
          <tr class="even:bg-white odd:bg-[#F9F9F9] border-0" v-for="client in clients" :key="client.id">
            <td class="py-4 text-center border-0">{{ client.first_name }}</td>
            <td class="py-4 text-center border-0">{{ client.last_name }}</td>
            <td class="py-4 text-center border-0">CDG</td>
            <td class="py-4 text-center border-0">{{ client.created_at }}</td>
            <td class="py-2 text-center border-0">
              <span class="p-2 w-24 inline-block text-center" :class="getClassByStatus(client.status)">{{ client.status }}</span>
            </td>
            <td class="py-4 text-center border-0">
              <button v-if="client.status === 'en attente'" class="py-1 px-2" @click="rejectRequest(client.id)"><Reject /></button>
              <button v-if="client.status === 'en attente'" class="py-1 px-2 mr-2"  @click="acceptRequest(client.id)"><Accept /></button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import DropDown from '../components/DropDown.vue';
import Accept from '../components/Icons/Accept.vue';
import Reject from '../components/Icons/Reject.vue';
import { useToast } from 'vue-toast-notification';
import api from '../services/api';

const toast = useToast();

interface Client {
  id: number;
  first_name: string;
  last_name: string;
  status: string;
  created_at: Date;
}

const clients = ref<Client[]>([]);

onMounted(() => {
  getUsers();
});

const getUsers = async () => {
  const response = await api.get('/access-requests/list/');
  const toto = response.data.map((request: any) => {
    request.created_at = convertDate(new Date(request.created_at));
    if (request.status === 'pending') {
      request.status = 'en attente'
    }
    else if (request.status === 'approved') {
      request.status = 'accepté'
    }
    else {
      request.status = 'refusé'
    }
    return request
  })
  console.log(toto);
  clients.value = toto;
};

const convertDate = (date: Date) => {
  const day = date.getDate();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const year = date.getFullYear();
  return `${day}/${month}/${year}`;
};

const rejectRequest = async (id: number) => {
  await api.post(`/access-requests/reject/${id}/`);
  toast.open({
    message: 'Demande refusée',
    type: 'success',
    duration: 5000,
    position: 'bottom'
  });
  const client = clients.value.find((client) => client.id === id);
  if (client) {
    client.status = 'refusé';
  }
};

const acceptRequest = async (id: number) => {
  await api.post(`/access-requests/approve/${id}/`);
  toast.open({
    message: 'Demande acceptée',
    type: 'success',
    duration: 5000,
    position: 'bottom'
  });
  const client = clients.value.find((client) => client.id === id);
  if (client) {
    client.status = 'accepté';
  }
}
const getClassByStatus = (status: string) => {
  console.log(status)
  switch (status) {
    case 'en attente':
      return 'bg-[#F9F9F9] text-[#969696] border-[1px] border-solid border-[#969696]'
    case 'accepté':
      return 'bg-[#A6E7D8] text-[#008767] border-[1px] border-solid border-[#008767]';
    case 'refusé':
      return 'bg-[#FFC5C5] text-[#DF0404] border-[1px] border-solid border-[#DF0404]';
    default:
      return 'bg-[#F9F9F9] text-[#969696] border-[1px] border-solid border-[#969696]';
  }
};
</script>

<style>
table {
  border-collapse: collapse;
  width: 80%;
  margin-top: 20px;
}

th,
td {
  border: 1px solid #ddd;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}

button {
  cursor: pointer;
}
</style>
