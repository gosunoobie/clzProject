import { defineStore } from 'pinia'
import { getAPI, patchAPI, postAPI } from '../api/index'
import { userEditModal, TransactionType } from '../models/Account.interface'
import { notify } from '@kyvg/vue3-notification'
import { useJwtStore } from './jwt'
import router from '../router/index'

const jwtStore = useJwtStore()
export const useAccountStore = defineStore('accountStore', {
  state: () => {
    return {
      userEditPayload: null as userEditModal | null,
      flightTicket: null as any,
      flightTicketLoading: true,
      activityTicketLoading: true,
      activityTicketCount: 0,
      ttCoinsHistory: null as any,
      ttCoinsTransactionCount: 0,
      ttCoinsLoading: true,
      transactionHistory: [] as TransactionType[],
      transactionHistoryCount: 0,
      transactionHistoryLoading: true,
      ttcoinsfaqs: null as any,
      ttcoinsDetails: null as any,
      activityTicket: null as any,
      hotelTicketList: null as any,
      hotelTicketCount: 0,
      cancellationResponse: null as any,
      isHotelTicketLoading: false,
      showModalRegister: false,
      isCancellationLoading: false
    }
  },
  getters: {
    getCancellationPolicies(state) {
      return state.cancellationResponse.cancellationSummary.cancellationPolicy
    }
  },
  actions: {
    async editUserData(data: any) {
      if (data.firstName === '' || data.lastName === '') {
        notify({
          text: 'First name and last name can not be blank',
          type: 'error',
          duration: 2000
        })
      } else {
        try {
          let response = await patchAPI('users/auth/update_info', data)
          jwtStore.UserDetail.firstName = response.data.firstName
          jwtStore.UserDetail.lastName = response.data.lastName
          jwtStore.UserDetail.mobileNumber = response.data.mobileNumber

          notify({
            text: 'Successfully updated profile',
            type: 'success',
            duration: 2000
          })
        } catch (e) {}
      }
    },
    async getFlightTickets() {
      try {
        const res = await getAPI('domestic/booking-list')
        this.flightTicket = res.data
        this.flightTicketLoading = false
      } catch (e) {}
    },
    async getActivityTickets() {
      try {
        const res = await getAPI('sp/customer-ticket-list')
        this.activityTicket = res.data['results']
        this.activityTicketCount = res.data['totalObjects']
        this.activityTicketLoading = false
      } catch (e) {
        console.log(e)
      }
    },
    async getHotelsTickets() {
      try {
        this.isHotelTicketLoading = true
        const res = await getAPI('hotels/hotel-tix-list')
        this.hotelTicketList = res.data
        this.hotelTicketCount = res.data.length
        console.log(res.data)
        this.isHotelTicketLoading = false
      } catch (e) {
        console.log(e)
        this.isHotelTicketLoading = false
      }
    },
    async cancelHotelBooking(id: number) {
      try {
        this.isCancellationLoading = true
        const res = await postAPI(`hotels/cancel-hotel-booking`, {
          bookingId: Number(id)
        })
        this.cancellationResponse = res.data
        console.log(res.data)
      } catch (e) {
        console.log(e)
      } finally {
        this.isCancellationLoading = false
      }
    },
    async confirmCancelHotelBooking(id: number) {
      try {
        const res = await postAPI(`hotels/confirm-cancel-hotel-booking`, {
          bookingId: this.cancellationResponse.cancellationSummary.bookingId,
          reference: this.cancellationResponse.cancellationSummary.reference,
          cancelReason: Number(id),
          refundRate: {
            currency: this.cancellationResponse.cancellationSummary.refundRate[0].currency,
            inclusive: this.cancellationResponse.cancellationSummary.refundRate[0].inclusive
          }
        }).then((res) => {
          notify({
            text: res.data,
            duration: 3000,
            type: 'success'
          })
          return res
        })
        this.cancellationResponse = res.data
        console.log(res.data)
      } catch (e) {
        console.log(e)
        notify({
          text: e.message,
          duration: 3000,
          type: 'error'
        })
      }
    },
    async getTTCoinsHistory() {
      try {
        const res = await getAPI('pf/loyalty-coin-history')
        this.ttCoinsHistory = res.data['results']
        // res);
        this.ttCoinsTransactionCount = res.data['totalObjects']
        this.ttCoinsLoading = false
      } catch (e) {
        console.log(e)
      }
    },
    async getTTCoinsDetails() {
      try {
        const res = await getAPI('users/auth/get_total_reward_coin')
        this.ttcoinsDetails = res.data
        console.log(res)
        this.ttCoinsTransactionCount = res.data['totalObjects']
      } catch (e) {
        console.log(e)
      }
    },
    async getTransactionHistory() {
      try {
        const res = await getAPI('transaction-history')
        this.transactionHistory = res.data['results']
        this.transactionHistoryCount = res.data['totalObjects']
        this.transactionHistoryLoading = false
      } catch (e) {
        console.log(e)
      }
    },
    async getTtCoinsFaqs() {
      try {
        const res = await getAPI('qs/tt-coin-questions')
        this.ttcoinsfaqs = res.data
        // this.transactionHistoryCount = res.data["totalObjects"];
        // this.transactionHistoryLoading = false;
      } catch (e) {
        console.log(e)
      }
    },
    async getGoogleLogin(accessToken) {
      try {
        const reqBody = {
          code: accessToken,
          fcm_token: '',
          fcm_type: ''
        }

        await postAPI('dj-rest-auth/google', reqBody, {
          withCredentials: true
        }).then(() => {
          jwtStore.isLoggedIn = true
          jwtStore.refreshAccessToken()
          router.push({
            name: 'Home'
          })
        })
      } catch (error) {
        router.push({
          name: 'RedirectPage'
        })
      }
    },
    async getFbLogin(accessToken) {
      try {
        const reqBody = {
          code: accessToken,
          fcm_token: '',
          fcm_type: ''
        }

        await postAPI('dj-rest-auth/facebook', reqBody, {
          withCredentials: true
        }).then(() => {
          jwtStore.isLoggedIn = true
          jwtStore.refreshAccessToken()
          router.push({
            name: 'Home'
          })
        })
      } catch (error) {
        router.push({
          name: 'RedirectPage'
        })
      }
    },
    async updateCountry(countryName, mobileNumber) {
      try {
        const payload = {
          mobile_number: mobileNumber,
          country: countryName
        }

        // console.log(userId,'this is the uesr id')
        // console.log(payload, ' this is the payload')
        let res = await postAPI(`users/auth/update_number`, payload)
        //  console.log('this is the response',res)
      } catch (error) {}
    }
  }
})

//billing/transaction-history/
