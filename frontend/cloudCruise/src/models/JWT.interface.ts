export interface UserLoginInfo {
  username: string | null
  password: string | null
}

export interface JWT {
  data: {
    access: string
    refresh?: string
    user?: any
  }
}

export interface DecodedJWTPayload {
  exp: number
  jti: string
  token_type: string
  user_id: number
  username: string
  userDetail: any
}
