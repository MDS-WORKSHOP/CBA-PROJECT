<template>
  <div class="flex flex-col items-center justify-center h-screen">
    <h1 class="text-4xl font-bold mb-4">Autorisation des demandes d’accès</h1>
    <table class="min-w-full bg-white">
      <thead class=" bg-white">
        <tr class="text-[#051039]">
          <th class="py-2 bg-white text-center border-0">Nom</th>
          <th class="py-2 bg-white text-center border-0">Prénom</th>
          <th class="py-2 bg-white text-center border-0">Site</th>
          <th class="py-2 bg-white text-center border-0">Date de demande d'accès</th>
          <th class="py-2 bg-white text-center border-0">Statut</th>
          <th class="py-2 bg-white text-center border-0">Autorisation</th>
        </tr>
      </thead>
      <tbody>
        <tr class="even:bg-white odd:bg-[#F9F9F9] border-0" v-for="client in clients" :key="client.id">
          <td class="py-2 text-center border-0">{{ client.nom }}</td>
          <td class="py-2 text-center border-0">{{ client.prenom }}</td>
          <td class="py-2 text-center border-0">CDG</td>
          <td class="py-2 text-center border-0">{{ client.dateDemande }}</td>
          <td class="py-2 text-center border-0">
            <span class="p-2" :class="getClassByStatus('Refusé')">En attente</span>
          </td>
          <td class="py-2 text-center border-0">
            <button
              class="bg-green-500 text-white py-1 px-2 mr-2"
              @click="accepterClient(client.id)"
            >
              Accepter
            </button>
            <button
              class="bg-red-500 text-white py-1 px-2"
              @click="refuserClient(client.id)"
            >
              Refuser
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

interface Client {
  id: number;
  nom: string;
  prenom: string;
  dateDemande: string;
}

const clients = ref<Client[]>([
  { id: 1, nom: 'Dupont', prenom: 'Jean', dateDemande: '2023-06-01' },
  { id: 2, nom: 'Durand', prenom: 'Marie', dateDemande: '2023-06-05' },
  { id: 3, nom: 'Tcp', prenom: 'Push', dateDemande: '2023-06-02' },
]);

const accepterClient = (id: number) => {
  console.log(`Client accepté avec ID : ${id}`);
};

const refuserClient = (id: number) => {
  console.log(`Client refusé avec ID : ${id}`);
};
const getClassByStatus = (status: string) => {
  switch (status) {
    case 'En attente':
      return 'bg-gray-500';
    case 'Accepté':
      return 'bg-[#A6E7D8] text-[#008767] border-[1px] border-solid border-[#008767]';
    case 'Refusé':
      return 'bg-[#FFC5C5] text-[#DF0404] border-[1px] border-solid border-[#DF0404]';
    default:
      return 'bg-gray-500';
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
