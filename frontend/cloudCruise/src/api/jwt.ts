import { postAPI } from './index'
import type { UserLoginInfo } from '../models/JWT.interface'
import { Action } from './actions'

export default new (class JWTAPI {
  public async getJWT(user: UserLoginInfo) {
    const response = await postAPI(Action.Token, user, {
      withCredentials: true
    })
    return response
  }

  public async refreshAccessToken() {
    try {
      const response = await postAPI(
        Action.RefreshToken,
        {},
        {
          withCredentials: true
        }
      )
      return response
    } catch (error) {}
  }

  public async clearJWT() {
    const response = await postAPI(
      Action.ClearToken,
      {},
      {
        withCredentials: true
      }
    )
    localStorage.removeItem('state')

    return response
  }
})()
