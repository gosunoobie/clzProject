import { defineStore } from 'pinia'
import { jwtDecode } from 'jwt-decode'

import type { UserLoginInfo, JWT } from '../models/JWT.interface'
import API from '../api/jwt'
import router from '../router'

export const useJwtStore = defineStore('jwt', {
  state: () => {
    return {
      AccessToken: '',
      isLoggedIn: false,
      RefreshingToken: true,
      DecodedPayload: {} as any,
      UserDetail: {} as any,
      registerUserId: null,
      showSignInModel: { value: false }
    }
  },
  getters: {
    loggedIn: (state) => {
      return state.isLoggedIn
    },
    showModal: (state) => {
      return state.showSignInModel
    }
  },
  actions: {
    refreshingToken() {
      this.RefreshingToken = true
    },
    async setIsLoggedIn(value: boolean) {
      //   LocalStorage.set("isLoggedIn", value);
      this.isLoggedIn = value
    },
    async getJWT(user: UserLoginInfo) {
      const detail = (await API.getJWT(user)) as JWT

      this.AccessToken = detail.data.access
      this.registerUserId = detail.data.user.id

      const decodedPayload = jwtDecode(detail.data.access) as any
      this.DecodedPayload = decodedPayload
      this.UserDetail = detail.data.user
      this.isLoggedIn = true
    },
    async refreshAccessToken() {
      let detail = (await API.refreshAccessToken()) as JWT
      // console.log('this is refreshing')
      let decodedPayload: any = {} as any
      let isLoggedIn = false
      // console.log("detail", detail);
      if (!detail || !detail.data.access) {
        const loggedIn = this.isLoggedIn
        detail = { data: { access: '' } } as JWT
        if (loggedIn) {
          router.push({ name: 'Home' })
        }
      } else {
        decodedPayload = jwtDecode(detail.data.access)
        isLoggedIn = true
      }
      this.AccessToken = detail?.data?.access
      this.DecodedPayload = decodedPayload
      this.isLoggedIn = isLoggedIn
      this.UserDetail = detail.data.user
      this.RefreshingToken = false
      this.registerUserId = detail.data.user.id
    },

    // async refreshSocialAccessToken(){
    //   let detail = (await API.refreshAccessToken()) as JWT;
    //   console.log('this is detail',detail)

    //   let decodedPayload: any = {} as any;
    //   let isLoggedIn = false;
    //   // console.log("detail")
    //   if (!detail || !detail.data.access) {
    //     const loggedIn = this.isLoggedIn;
    //     detail = { data: { access: "" } } as JWT;
    //     if (loggedIn) {
    //       router.push({ name: "Home" });
    //     }
    //   } else {
    //     decodedPayload = jwtDecode(detail.data.access);
    //     isLoggedIn = true;
    //   }
    //   this.AccessToken = detail?.data?.access;
    //   this.DecodedPayload = decodedPayload;
    //   this.isLoggedIn = isLoggedIn;
    //   this.UserDetail = detail.data.user;
    //   this.RefreshingToken = false;
    //   if(detail.data.user.accountProvider === "Tripturbo")
    //   console.log('wow')
    // },

    async clearJWT() {
      await API.clearJWT()
      this.AccessToken = ''
      this.isLoggedIn = false
      this.DecodedPayload = {} as any
      this.UserDetail = {}
    }
  }
})
