import { defineStore } from 'pinia'
import { postAPI, getAPI } from '@/api'
import CountryArr from '../assets/country/Countries.json'
import type {
  SectorCode,
  CountryCode,
  FlightComponentDetails,
  FlightDetailResponse,
  BillingListModel,
  FlightBookingPayload,
  SelectedFlightType
} from '@/models/Flight.interface'
import router from '../router'
export const useNewFlightStore = defineStore('newFlightStore', {
  state: () => {
    return {
      // TODO: Make this sectors list be available from api
      sectors_list: [
        { value: 'BDP', label: 'BHADRAPUR' },
        { value: 'BWA', label: 'BHAIRAHAWA' },
        { value: 'BHR', label: 'BHARATPUR' },
        { value: 'BIR', label: 'BIRATNAGAR' },
        { value: 'DHI', label: 'DHANGADHI' },
        { value: 'JKR', label: 'JANAKPUR' },
        { value: 'JMO', label: 'JOMSOM' },
        { value: 'KTM', label: 'KATHMANDU' },
        { value: 'LUA', label: 'LUKLA' },
        { value: 'MTN', label: 'MOUNTAIN' },
        { value: 'KEP', label: 'NEPALGUNJ' },
        { value: 'PKR', label: 'POKHARA' },
        { value: 'RJB', label: 'RAJBIRAJ' },
        { value: 'RCH', label: 'RAMECHHAP' },
        { value: 'SIF', label: 'SIMARA' },
        { value: 'SKH', label: 'SURKHET' },
        { value: 'TMI', label: 'TUMLINGTAR' }
      ],
      isFlightsSearched: false,
      searchDepatureLocationQuery: '',
      searchReturnLocationQuery: '',
      searchNationalityQuery: 'Nepal',
      searchNationalityFinalQuery: {
        name: 'Nepal',
        prefix: '+977',
        code: 'NP'
      },
      showDepartureLocationDropDown: false,
      finalDepartureLocationQueryValue: null as SectorCode,
      finalReturnLocationQueryValue: null as SectorCode,
      showReturnLocationDropDown: false,
      isShowingReturnFlights: false,
      departureDateArrays: [],
      returnDateArrays: [],
      selectedDateIndex: 0,
      returnDate: null,
      inputDepartureDate: new Date().toISOString().slice(0, 10),
      flightSearchPayload: {
        adultPassenger: 1,
        childPassenger: null || 0,
        departureDate: new Date().toISOString().slice(0, 10),
        destinationLocationCode: '',
        nationality: 'NP',
        originLocationCode: '',
        seatClass: 'E',
        returnFlight: false
      },
      departureFlightLists: [] as FlightComponentDetails[],
      returnFlightLists: [] as FlightComponentDetails[],
      departureFlightAirlines: [],
      returnFlightAirlines: [],
      flightsDurationFilters: [
        {
          label: 'Shortest First',
          value: 'S'
        },
        {
          label: 'Longest First',
          value: 'L'
        }
      ],
      flightsPriceFilters: [
        {
          label: 'Lowest First',
          value: 'L'
        },
        {
          label: 'Highest First',
          value: 'H'
        }
      ],
      flightsTicketTypeFilters: [
        {
          label: 'Refundable',
          value: 'T'
        },
        {
          label: 'Non-Refundable',
          value: 'F'
        }
      ],
      selectedAirlinesFilter: [] as string[],
      showFlightFilters: false,
      isCurrentTabDeparture: true,
      selectedFlight: {} as SelectedFlightType | null,
      selectedTicketTypeFilter: '',
      selectedDurationTypeFilter: '',
      selectedTicketPricesFilter: '',
      filteredDepartureFlightLists: [],
      filteredReturnFlightLists: [],
      isFlightsLoading: false,
      flightDetail: null as FlightDetailResponse | null,
      bookingDetail: null,
      passengerForm: { adult: [], child: [] } as any,
      reservingFlight: false,
      creatingBooking: false,
      showPaymentModal: false,
      paymentTxnId: null,
      selectedBillingAddress: null,
      billingList: [] as BillingListModel[],
      loadingScreen: false
    }
  },
  getters: {
    getTripTypeTwoway(state) {
      return state.flightSearchPayload.returnFlight
    },
    getValidDepartureLocations(state) {
      return state.sectors_list.filter(
        (location: SectorCode) =>
          location.label.toUpperCase().includes(state.searchDepatureLocationQuery.toUpperCase()) ||
          location.value.toUpperCase().includes(state.searchDepatureLocationQuery.toUpperCase())
      )
    },
    getValidReturnLocations(state) {
      return state.sectors_list.filter(
        (location) =>
          location.label.toUpperCase().includes(state.searchReturnLocationQuery.toUpperCase()) ||
          location.value.toUpperCase().includes(state.searchReturnLocationQuery.toUpperCase())
      )
    },
    getFirstValidDepartureLocations(state): SectorCode {
      return state.sectors_list.filter(
        (location) =>
          location.label.toUpperCase().includes(state.searchDepatureLocationQuery.toUpperCase()) ||
          location.value.toUpperCase().includes(state.searchDepatureLocationQuery.toUpperCase())
      )[0]
    },
    getFirstValidReturnLocations(state) {
      return state.sectors_list.filter(
        (location) =>
          location.label.toUpperCase().includes(state.searchReturnLocationQuery.toUpperCase()) ||
          location.value.toUpperCase().includes(state.searchReturnLocationQuery.toUpperCase())
      )[0]
    },
    getValidCountries(state) {
      return CountryArr.filter(
        (country: CountryCode) =>
          country.name.toLowerCase().includes(state.searchNationalityQuery.toLowerCase()) ||
          country.code.toLowerCase().includes(state.searchNationalityQuery.toLowerCase())
      )
    },
    getFilteredReturnFlights(state) {
      const airlinesFilteredFlights = state.returnFlightLists.filter(
        (flight: FlightComponentDetails) =>
          state.selectedAirlinesFilter.includes(flight.AirlineName)
      )
      const validAirlinesFilteredFlights =
        airlinesFilteredFlights.length > 0 ? airlinesFilteredFlights : state.returnFlightLists
      const ticketTypeFilteredFlights = validAirlinesFilteredFlights.filter(
        (flight) => flight.Refundable === state.selectedTicketTypeFilter
      )
      const validTicketTypeFilteredFlights =
        state.selectedTicketTypeFilter.length > 0
          ? ticketTypeFilteredFlights
          : validAirlinesFilteredFlights

      const priceSortedFlightLists = [...validTicketTypeFilteredFlights].sort((flightA, flightB) =>
        state.selectedTicketPricesFilter === 'H'
          ? flightB.TotalPrice - flightA.TotalPrice
          : flightA.TotalPrice - flightB.TotalPrice
      )
      const durationSortedFlightLists = [...priceSortedFlightLists].sort((flightA, flightB) =>
        state.selectedDurationTypeFilter === 'L'
          ? parseInt(flightB.elpasedTime) - parseInt(flightA.elpasedTime)
          : parseInt(flightA.elpasedTime) - parseInt(flightB.elpasedTime)
      )
      if (state.selectedDurationTypeFilter.length > 0) return durationSortedFlightLists
      return priceSortedFlightLists
    },
    getFilteredDepartureFlights(state) {
      const airlinesFilteredFlights = state.departureFlightLists.filter(
        (flight: FlightComponentDetails) =>
          state.selectedAirlinesFilter.includes(flight.AirlineName)
      )
      const validAirlinesFilteredFlights =
        airlinesFilteredFlights.length > 0 ? airlinesFilteredFlights : state.departureFlightLists
      const ticketTypeFilteredFlights = validAirlinesFilteredFlights.filter(
        (flight) => flight.Refundable === state.selectedTicketTypeFilter
      )
      const validTicketTypeFilteredFlights =
        state.selectedTicketTypeFilter.length > 0
          ? ticketTypeFilteredFlights
          : validAirlinesFilteredFlights

      const priceSortedFlightLists = [...validTicketTypeFilteredFlights].sort((flightA, flightB) =>
        state.selectedTicketPricesFilter === 'H'
          ? flightB.TotalPrice - flightA.TotalPrice
          : flightA.TotalPrice - flightB.TotalPrice
      )
      const durationSortedFlightLists = [...priceSortedFlightLists].sort((flightA, flightB) =>
        state.selectedDurationTypeFilter === 'L'
          ? parseInt(flightB.elpasedTime) - parseInt(flightA.elpasedTime)
          : parseInt(flightA.elpasedTime) - parseInt(flightB.elpasedTime)
      )
      if (state.selectedDurationTypeFilter.length > 0) return durationSortedFlightLists
      return priceSortedFlightLists
    },
    durationLeft(state) {
      return state.flightDetail?.flightInfo[0].duration
    },

    billingListOptions(state) {
      return state.billingList.map((li: BillingListModel) => ({
        label: li.name,
        value: li.id
      }))
    }
  },
  actions: {
    setOriginLocationCode(code) {
      try {
        this.flightSearchPayload.originLocationCode = code
      } catch (error) {
        console.log(error)
      }
    },
    setTripTypeTwoway(isTwoway) {
      this.flightSearchPayload.returnFlight = isTwoway
    },
    setDestinationLocationCode(code) {
      try {
        this.flightSearchPayload.destinationLocationCode = code
      } catch (error) {
        console.log(error)
      }
    },
    setIsShowingReturnFlights(isReturnFlights) {
      this.isShowingReturnFlights = isReturnFlights
    },
    async getLocationSectorCodes() {
      try {
        const res = await getAPI('domestic/sector-code')
        this.sectors_list = res.data
      } catch (error) {}
    },
    interchangeDestination() {
      if (!this.searchDepatureLocationQuery || !this.searchReturnLocationQuery) return
      const tempQueryValue = this.searchDepatureLocationQuery
      const tempDepartureLocationObject = JSON.parse(
        JSON.stringify(this.finalDepartureLocationQueryValue)
      )
      const tempReturnLocationObject = JSON.parse(
        JSON.stringify(this.finalReturnLocationQueryValue)
      )

      this.searchDepatureLocationQuery = this.searchReturnLocationQuery
      this.finalDepartureLocationQueryValue = tempReturnLocationObject
      this.searchReturnLocationQuery = tempQueryValue
      this.finalReturnLocationQueryValue = tempDepartureLocationObject

      this.setOriginLocationCode(tempReturnLocationObject.value)
      this.setDestinationLocationCode(tempDepartureLocationObject.value)
    },
    setFlightsDurationFilter(value: string) {
      this.selectedDurationTypeFilter = this.selectedDurationTypeFilter === value ? '' : value
    },
    setFlightsTicketTypeFilter(value: string) {
      this.selectedTicketTypeFilter = this.selectedTicketTypeFilter === value ? '' : value
    },
    setFlightsTicketPriceFilter(value: string) {
      this.selectedTicketPricesFilter = this.selectedTicketPricesFilter === value ? '' : value
    },
    async getDepartureFlightLists() {
      try {
        this.isFlightsLoading = true
        this.flightSearchPayload.departureDate = this.inputDepartureDate
        this.selectedFlight = {}
        const res = await postAPI('search-flights', this.flightSearchPayload)
        this.departureFlightLists = res.data.flightsData
        for (let flight of this.departureFlightLists) {
          if (!this.departureFlightAirlines.includes(flight.airlineName)) {
            this.departureFlightAirlines.push(flight.airlineName)
          }
        }
        this.isFlightsSearched = true
        this.isFlightsLoading = false
      } catch (error) {
        this.isFlightsSearched = true
        this.isFlightsLoading = false
      }
    },
    async getReturnFlightLists() {
      try {
        const returnFlightPayload = { ...this.flightSearchPayload }
        returnFlightPayload.departureDate = this.returnDate
        returnFlightPayload.destinationLocationCode = this.flightSearchPayload.originLocationCode
        returnFlightPayload.originLocationCode = this.flightSearchPayload.destinationLocationCode
        const res = await postAPI('search-flights', returnFlightPayload)
        this.returnFlightLists = res.data.flightsData
        for (let flight of this.returnFlightLists) {
          if (!this.returnFlightAirlines.includes(flight.AirlineName)) {
            this.returnFlightAirlines.push(flight.AirlineName)
          }
        }
        this.isFlightsLoading = false
        this.isFlightsSearched = true
      } catch (error) {
        this.isFlightsSearched = true
        this.isFlightsLoading = false
      }
    },
    async getFlightDetail(reserveId: string) {
      try {
        this.isFlightsLoading = true
        const res = await getAPI(`reserve-track/${reserveId}`)
        this.isFlightsLoading = false
        this.flightDetail = res.data
        this.passengerForm.adult = []

        for (let i = 0; i < res.data.flightInfo[0].Adult; i++) {
          this.passengerForm.adult.push({
            first_name: null,
            gender: null,
            last_name: null,
            nationality: this.searchNationalityFinalQuery.code,
            passenger_title: null,
            passenger_type: 'ADULT'
          })
        }
        this.passengerForm.child = []
        for (let i = 0; i < res.data.flightInfo[0].Child; i++) {
          this.passengerForm.child.push({
            first_name: null,
            gender: null,
            last_name: null,
            nationality: this.searchNationalityFinalQuery.code,
            passenger_title: null,
            passenger_type: 'CHILD'
          })
        }
      } catch (error) {
        this.isFlightsLoading = false
        router.push('/flights')
      }
    },
    async reserveFlight(flightId: string | null = null) {
      try {
        this.reservingFlight = true
        const res = await postAPI('reserve', {
          flight_id: flightId
        })
        this.reservingFlight = false
        router.push(`/flights/${res.data.ReservationDetail.ReserveTrackId}`)
      } catch (e) {
        this.reservingFlight = false
      }
    },
    async reserveRoundFlight() {
      try {
        this.reservingFlight = true
        const departureFlightId = this.selectedFlight?.departureFlight
        const returnFlightId = this.selectedFlight?.returnFlight
        if (returnFlightId && departureFlightId) {
          const res = await postAPI('reserve', {
            flight_id: departureFlightId.FlightId,
            return_flight_id: returnFlightId.FlightId
          })
          this.reservingFlight = false
          router.push(`/flights/${res.data.ReservationDetail.ReserveTrackId}`)
        }
      } catch (e) {
        this.reservingFlight = false
      }
    },
    async getBillingAddress() {
      const res = await getAPI('billing-address')
      this.billingList = res.data || []
    },
    async createBooking(bookingPayload: any) {
      try {
        this.reservingFlight = true
        const { id, noOfAdults, noOfChild } = bookingPayload
        console.log(bookingPayload)
        const res = await postAPI('book-flights', {
          schedule: id,
          noOfAdults: noOfAdults,
          noOfChild: noOfChild
        })
        this.bookingDetail = res.data
        /* router.push({
          name: 'FlightDetail',
          query: {
scheduleId: res.data.schedule,
            noOfAdults: res.data.noOfAdults,
            noOfChild: res.data.noOfChild
          }
        }) */
        this.passengerForm.adult = []

        for (let i = 0; i < noOfAdults; i++) {
          this.passengerForm.adult.push({
            first_name: null,
            gender: null,
            last_name: null,
            nationality: this.searchNationalityFinalQuery.code,
            passenger_title: null,
            passenger_type: 'ADULT'
          })
        }
        this.passengerForm.child = []
        for (let i = 0; i < noOfChild; i++) {
          this.passengerForm.child.push({
            first_name: null,
            gender: null,
            last_name: null,
            nationality: this.searchNationalityFinalQuery.code,
            passenger_title: null,
            passenger_type: 'CHILD'
          })
        }

        console.log(noOfChild, noOfAdults, this.passengerForm)
        this.reservingFlight = false

        router.push(`/flight-detail/${res.data.schedule}`)
      } catch (error) {
        this.reservingFlight = false
      }
    }
    /* async createBooking(bookingPayload: FlightBookingPayload) {
      bookingPayload.billing_address = this.selectedBillingAddress

      try {
        this.creatingBooking = true
        const res = await postAPI('domestic/create-domestic-booking', bookingPayload)
        this.paymentTxnId = res.data[0].txnId
        this.creatingBooking = false
        this.showPaymentModal = true
      } catch (error) {
        this.creatingBooking = false
      }
    } */
  }
})
