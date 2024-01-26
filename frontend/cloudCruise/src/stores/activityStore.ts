// stores/counter.js
import { defineStore } from 'pinia'
import { postAPI, getAPI } from '../api'
import {
  ServiceListType,
  ActivityPricingType,
  InventoryType,
  AvailabilityPayloadType,
  BookingResponseType,
  AvailabilityResponse
} from '../models/Activity.interface'

import CountryArr from '../assets/country/Countries.json'
interface serachQueryType {
  search?: string
  service_name?: string
  rating?: number
}
export const useActivityStore = defineStore('activityStore', {
  state: () => {
    return {
      showVirtualGallery: { value: false },
      serviceList: [] as ServiceListType[],
      // activityList: [] as ActivityListType[],
      popularDestinationList: [],
      activityList: [] as any,
      trackedActivityList: [] as any,
      currentServiceProviderActivityList: [] as any,
      searchActivityQuery: {} as serachQueryType,
      isActivityLoading: true as boolean,
      isActivityOverviewLoading: true as boolean,
      isActivityPricingTableLoading: true as boolean,
      isActivityPolicyloading: true as boolean,
      isActivityFaqsLoading: true as boolean,
      isActivityReviewLoading: true as boolean,
      isActivityFiltersLoading: true as boolean,
      isInventoryLoading: false as boolean,
      ispaginationLoading: false as boolean,
      activityDetail: {
        id: null as null | number,
        overview: null as any,
        bookingPolicy: null as any,
        cancelPolicy: null as any,
        questions: null as any,
        review: null as any,
        pricing: [] as ActivityPricingType[]
      },
      activitySelection: {
        inventoryList: [] as InventoryType[],
        availabilityData: {} as AvailabilityResponse,
        checkAvailabilityPayload: {} as AvailabilityPayloadType,
        bookingResponse: {} as BookingResponseType
      },
      loadingScreen: false,

      participantDetails: [],
      searchNationalityQuery: 'Nepal',
      searchNationalityFinalQuery: {
        name: 'Nepal',
        prefix: '+977',
        code: 'NP'
      },
      participantNationality: 'NP'
    }
  },
  getters: {
    getNepaliPrices(state) {
      return state.activityDetail.pricing.filter(
        (price: ActivityPricingType) => price.nationality === 'Nepali'
      )
    },
    getForeignersPrices(state) {
      return state.activityDetail.pricing.filter(
        (price: ActivityPricingType) => price.nationality === 'Foreigners'
      )
    },
    inventoryList(state) {
      return state.activitySelection.inventoryList
    },
    availabilityRanges(state) {
      return state.activitySelection.availabilityData?.allRanges || []
    },
    availabilityPrice(state) {
      return state.activitySelection.availabilityData?.priceInfo
    },
    availabilityPayload(state) {
      return state.activitySelection.checkAvailabilityPayload
    },
    availabilityData(state) {
      return state.activitySelection.availabilityData
    },

    getValidCountries(state) {
      return CountryArr.filter(
        (country: CountryCode) =>
          country.name.toLowerCase().includes(state.searchNationalityQuery.toLowerCase()) ||
          country.code.toLowerCase().includes(state.searchNationalityQuery.toLowerCase())
      )
    },

    getCurrencyType(state) {
      return state.participantNationality === 'NP' || state.participantNationality === 'IN'
        ? 'NPR'
        : 'USD'
    },
    getCurrentBookingId(state) {
      return state.activitySelection.bookingResponse.id
    }
  },

  actions: {
    async getAllServices() {
      try {
        this.isActivityFiltersLoading = true
        const res = await getAPI('sp/service-list')

        this.serviceList = res.data.results
        this.isActivityFiltersLoading = false
      } catch (error) {
        this.isActivityFiltersLoading = false
      }
    },
    async getPopularDestinations() {
      try {
        this.isActivityOverviewLoading = true

        const res = await getAPI('tk/popular-destination/?page=1&page_size=40')
        this.popularDestinationList = res.data.results
      } catch (error) {}
    },
    async getTrackedActivityList(page: null | number = null) {
      try {
        page === null ? (this.isActivityLoading = true) : (this.ispaginationLoading = true)
        let query = `?page_size=10&${page && `page=${page}`}`
        const res = await getAPI('sp/tracked-activities-list', query)
        if (page) {
          this.activityList.currentPage = res.data.currentPage
          this.activityList.next = res.data.next
          this.activityList.results.data.push(...res.data.results.data)
          this.trackedActivityList.currentPage = res.data.currentPage
          this.trackedActivityList.next = res.data.next
          this.trackedActivityList.results.data.push(...res.data.results.data)
        } else {
          this.activityList = res.data
          this.trackedActivityList = res.data
        }
        page === null ? (this.isActivityLoading = false) : (this.ispaginationLoading = false)
      } catch (error) {
        page === null ? (this.isActivityLoading = false) : (this.ispaginationLoading = false)
      }
    },
    async getFilteredActivityList(page: null | number = null) {
      try {
        page === null ? (this.isActivityLoading = true) : (this.ispaginationLoading = true)

        let query = `?`
        for (let li in this.searchActivityQuery) {
          query += `${li}=${this.searchActivityQuery[li as keyof serachQueryType]}&`
        }

        let query_params = query + `&page_size=10&${page && `page=${page}`}`

        const res = await getAPI('sp/service-provider-list', query_params)
        if (page) {
          this.activityList.currentPage = res.data.currentPage
          this.activityList.next = res.data.next
          this.activityList.results.data.push(...res.data.results.data)
        } else {
          this.activityList = res.data
        }

        page === null ? (this.isActivityLoading = false) : (this.ispaginationLoading = false)
      } catch (error) {
        page === null ? (this.isActivityLoading = false) : (this.ispaginationLoading = false)
      }
    },
    async getCurrentServiceProviderFilteredActivityList(page: null | number = null, name: string) {
      try {
        let query = `?search=${name}`

        let query_params = query + `&page_size=10&${page && `page=${page}`}`

        const res = await getAPI('sp/service-provider-list', query_params)
        if (page) {
          this.currentServiceProviderActivityList = res.data
        } else {
          this.currentServiceProviderActivityList = res.data
        }
      } catch (error) {
        console.log(error)
      }
    },
    async getPopularDestinationActivityList(page: null | number = null, name: string) {
      try {
        let query = `?service_name=&search=${name}`

        let query_params = query + `&page_size=10&${page && `page=${page}`}`

        const res = await getAPI('sp/service-provider-list', query_params)
        if (page) {
          this.currentServiceProviderActivityList = res.data
        } else {
          this.currentServiceProviderActivityList = res.data
        }
      } catch (error) {
        console.log(error)
      }
    },
    async getActivityOverview(id: number) {
      try {
        this.isActivityOverviewLoading = true

        const res = await getAPI(`sp/service-and-provider-detail/${id}`)
        this.activityDetail.id = res.data.id
        this.activityDetail.overview = res.data
        this.isActivityOverviewLoading = false
      } catch (error) {
        this.isActivityOverviewLoading = false
      }
    },
    async getActivityPricing(id: number) {
      try {
        this.isActivityPricingTableLoading = true

        const res = await getAPI(`sp/pricing`, `?service_and_provider_id=${id}`)
        this.activityDetail.pricing = res.data || []
        this.isActivityPricingTableLoading = false
      } catch (error) {
        this.isActivityPricingTableLoading = false
      }
    },
    async getActivityCancelationPolicy(id: number) {
      try {
        this.isActivityPolicyloading = true

        if (this.activityDetail.cancelPolicy) {
          if (this.activityDetail.cancelPolicy.serviceAndProviderId === id) {
            this.isActivityPolicyloading = false

            return
          }
        }
        const res = await getAPI(`bk/activity-cancel-policy/${id}`)
        this.activityDetail.cancelPolicy = res.data
        this.isActivityPolicyloading = false
      } catch (error) {
        this.isActivityPolicyloading = false
      }
    },
    async getActivityBookingPolicy(id: number) {
      try {
        if (this.activityDetail.bookingPolicy) {
          if (this.activityDetail.bookingPolicy.providerPolicy.ofServiceAndProvider == id) {
            return
          }
        }
        const res = await getAPI(`bk/booking-policy/${id}`)
        this.activityDetail.bookingPolicy = res.data
      } catch (error) {}
    },

    async getActivityReviews(id: number) {
      try {
        this.isActivityReviewLoading = true
        if (this.activityDetail.review) {
          if (this.activityDetail.review.ofServiceAndProvider == id) {
            this.isActivityReviewLoading = false

            return
          }
        }
        const res = await getAPI(`sp/user-review/${id}`)
        this.activityDetail.review = res.data
        this.isActivityReviewLoading = false
      } catch (error) {
        this.isActivityReviewLoading = false
      }
    },
    async getActivityFaqs(id: number) {
      try {
        this.isActivityFaqsLoading = true

        if (this.activityDetail.questions) {
          if (this.activityDetail.questions[0].serviceAndProviderId === id) {
            this.isActivityFaqsLoading = false

            return
          }
        }
        const res = await postAPI(`qs/eq/service_questions_with_answer`, {
          service_and_provider_id: id
        })
        this.activityDetail.id = res.data.id
        this.activityDetail.questions = res.data
        this.isActivityFaqsLoading = false
      } catch (error) {
        this.isActivityFaqsLoading = false
      }
    },
    async getInventoryList(id: number) {
      this.isInventoryLoading = true
      try {
        const res = await getAPI(`sp/inventory`, `?service_and_provider_id=${id}`)
        this.activitySelection.inventoryList = res.data || []
        this.isInventoryLoading = false
      } catch (error) {
        this.isInventoryLoading = false
      }
    },
    async getBookingAvailablity(availabilityPayload: AvailabilityPayloadType, nextBtn: Function) {
      try {
        this.loadingScreen = true
        const res = await postAPI(`bk/check-booking-availability-list`, availabilityPayload)
        this.activitySelection.availabilityData = res.data
        this.activitySelection.checkAvailabilityPayload = availabilityPayload

        this.loadingScreen = false

        nextBtn()
      } catch (error) {
        this.loadingScreen = false
      }
    },
    async createActivityBooking(bookingPayload: AvailabilityPayloadType, nextBtn: Function) {
      try {
        this.loadingScreen = true
        const res = await postAPI(`bk/create-booking`, bookingPayload)
        this.activitySelection.bookingResponse = res.data

        const participantList = [] as any
        const participantTypes = this.availabilityPrice.detailCost.map((item: any) => {
          const { ageGroup, nationality, noOfPeople, noOfTicket } = item
          return {
            first_name: '',
            last_name: '',
            nationality,
            title: 'Mr',
            participant_type: ageGroup,
            noOfPeople,
            noOfTicket
          }
        })

        // adding both noOfPeople and noOfTicket as only one can exist at a time.i.e noOfPeople or noOfTicket (adding so that a if statement is not required)

        for (let participantObject of participantTypes) {
          for (let i = 0; i < participantObject.noOfPeople + participantObject.noOfTicket; i++) {
            const { first_name, last_name, title, nationality, participant_type } =
              participantObject

            participantList.push({
              booking_id: this.activitySelection.bookingResponse.id,
              first_name,
              last_name,
              title,
              nationality,
              participant_type
            })
          }
        }
        this.participantDetails = participantList.reverse()
        this.loadingScreen = false

        nextBtn()
      } catch (error) {
        this.loadingScreen = false
      }
    }
  }
})
