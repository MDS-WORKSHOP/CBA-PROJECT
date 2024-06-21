export interface Auth {
  accessToken: string;
  refreshToken: string;
}

export interface AuthState {
  accessToken: string | null;
  refreshToken: string | null;
}

export interface  AccessRequestForm{
  email: string;
  password: string;
  last_name: string;
  first_name: string;
  site: Sites | string;
  profile: Profiles | string;
}

export enum Sites {
  CDG = 'CDG',
  ORY = 'ORY',
  VLR = 'VLR',
}

export enum Profiles {
  BT = 'BT',
  CD = 'CD',
}

export interface User {
  id: number;
  email: string;
  first_name: string;
  last_name: string;
  site: Sites;
  profile: Profiles;
  role: string;
}