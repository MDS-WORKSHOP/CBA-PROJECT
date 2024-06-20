import api from "./api";
import { Auth } from "../types/auth";
import { AccessRequestForm } from "../types/auth";

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

const requestResetPassword = async (email: string): Promise<void> => {
  try {
    await api.post("/password-reset-request/", { email });
  } catch (error) {
    console.error(error);
  }
}

const resetPassword = async (password: string, token: string): Promise<void> => {
  try {
    await api.post("/password-reset-confirm/", { password, token });
  } catch (error) {
    console.error(error);
  }
}

const requestAccess = async (form: AccessRequestForm): Promise<void> => {
  const { email, password, last_name, first_name, site, profile } = form;
  try {
    await api.post("/access-requests/", { email, password, last_name, first_name, site, profile, reason: 'authorization' });
  } catch (error) {
    console.error(error);
  }
}

export default {
  login,
  requestResetPassword,
  resetPassword,
  requestAccess,
};