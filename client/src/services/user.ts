import api from "./api";
import { User } from "../types/auth";

const fetchUser = async (): Promise<User | undefined> => {
  try {
    const response = await api.get("/current-user/");
    return response.data;
  } catch (error) {
    console.error(error);
    return undefined;
  }
}

export default {
  fetchUser,
};