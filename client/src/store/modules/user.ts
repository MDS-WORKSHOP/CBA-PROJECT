import { defineStore } from 'pinia';
import { User } from '../../types/auth';
import userService from '../../services/user'

export const useUserStore = defineStore({
  id: 'user',
  state () {
    return {
      user: null as User | null,
    };
  },
  getters: {
    isAdmin: (state) => state.user?.role === 'admin',
  },
  actions: {
    setUser (user: User) {
      this.user = user;
    },
    async fetchUserData () {
      const user = await userService.fetchUser();
      if (user) {
        this.setUser(user);
      }
    },
  },

});
