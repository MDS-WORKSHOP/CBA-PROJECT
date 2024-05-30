import api from "./api";
import { Auth } from "../types/auth";

const login = async (email: string, password: string): Promise<Auth | undefined> => {
  try {
    console.log(email, password);
    const response = await api.post("/token/", { email, password });
    localStorage.setItem("accessToken", response.data.access);
    document.cookie = `refreshToken=${response.data.refresh}`;
  } catch (error) {
    console.error(error);
    return undefined;
  }
}

export default {
  login,
};