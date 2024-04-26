import { defineStore } from 'pinia'
import { postAPI, getAPI } from '../api'

export const usePaymentStore = defineStore('paymentStore', {
  state: () => {
    return {
      provider: '',
      todayUsdPrice: null
    }
  },
  getters: {
    providerType: (state) => {
      return state.provider
    }
  },
  actions: {
    async getTodaysUsdPrice() {
      try {
        const response = await getAPI('pf/currency-conversion')
        this.todayUsdPrice = response.data.usdPrice
      } catch (error) {
        console.log('error while pre payment')
      }
    },
    async getPrePayment(txnId: string) {
      try {
        await getAPI('billing/hbl-pre-payment', `${txnId}/website/NPR`).then((response) => {
          window.location.href = response.data.paymentPageUrl
          this.provider = response.data.provider
        })
      } catch (error) {
        console.log('error while pre payment')
      }
    },
    async initiateHblPayment(txnId: string, currency: string) {
      try {
        await getAPI('billing/hbl-pre-payment', `${txnId}/website/${currency}`).then((response) => {
          window.location.href = response.data.paymentPageUrl
          this.provider = response.data.provider
        })
      } catch (error) {
        console.log(error)
      }
    },
    async getNabilPayment(bookingInfo) {
      try {
        await fetch(
          `https://dev.cloudcruise.com/billing/nabil-payment-request/${bookingInfo.value.txnId}/website/NPR`
        )
          .then((response) => response.json())
          .then((response) => {
            window.location.href = response.data.paymentURL
            this.provider = response.data.provider
          })
      } catch (error) {
        console.log('error while pre payment')
      }
    }
  }
})
