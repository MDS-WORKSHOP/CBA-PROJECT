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
  site: Sites | null;
  profile: Profiles | null;
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
