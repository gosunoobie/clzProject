<script setup lang="ts">
import Plane from '../../assets/flight/image/plane.png'
import PlaneSm from '../../assets/flight/image/planesm.png'
import Clock from '../../assets/flight/image/clock.png'
import Luggage from '../../assets/flight/image/luggage.png'
import SeatClass from '../../assets/flight/image/star.png'
import { computed, type PropType } from 'vue'
import { FlightList } from '../../models/Flight.interface'
// import { useRouter } from "vue-router";
import { useNewFlightStore } from '../../stores/newFlightStore'
import { useJwtStore } from '../../stores/jwt'
import CoinImg from '../../assets/account/coin.png'

import GUA from '../../assets/flight/image/GUA.jpeg'
import S1 from '../../assets/flight/image/S1.jpeg'
import SHA from '../../assets/flight/image/SHA.jpeg'
import YT from '../../assets/flight/image/YT.jpeg'
import U4 from '../../assets/flight/image/U4.jpeg'

const airlineLogo = {
  GUA: GUA,
  S1: S1,
  SHA: SHA,
  YT: YT,
  U4: U4
}

function getAirlineLogoUrl(airlineName: string) {
  return airlineLogo[airlineName]
  // if(airlineName === "GUA"){
  //   return GUA
  // }
  // if(airlineName === "S1"){
  //   return S1
  // }
  // if(airlineName === "SHA"){
  //   return SHA
  // }
  // if(airlineName === "YT"){
  //   return YT
  // }
  // if(airlineName === "U4"){
  //   return U4
  // }
}
// import GUA from '../../assets/flight/image/GUA.jpeg'
// import GUA from '../../assets/flight/image/GUA.jpeg'

const jwtStore = useJwtStore()
// const $router: any = useRouter();

const newFlightStore = useNewFlightStore()
const props = defineProps({
  data: {
    type: Object as PropType<FlightList>,
    default: null
  },
  showButton: {
    type: Boolean,
    default: true
  },
  showColor: {
    type: Boolean,
    default: true
  }
})

const selectFlight = (flight: FlightList) => {
  if (newFlightStore.isCurrentTabDeparture) {
    newFlightStore.selectedFlight.departureFlight = flight
  } else {
    newFlightStore.selectedFlight.returnFlight = flight
  }
}

const isSelected = computed(() => {
  if (props.showColor) {
    return [
      newFlightStore.selectedFlight?.departureFlight?.flightId,
      newFlightStore.selectedFlight?.returnFlight?.flightId
    ].includes(data.flightId)
  }
  return false
})

const createBooking = (data: any) => {
  newFlightStore.createBooking(data)
}

const { data } = props
</script>

<template>
  <div
    @click="selectFlight(data)"
    :class="
      isSelected
        ? 'selected-flight flight-container p-[10px] sm:px-[15px] sm:py-[10px]'
        : 'flight-container p-[10px] sm:px-[15px] sm:py-[10px]'
    "
  >
    <div class="flight-details px-0 py-0 xs:py-[10px] gap-0 mxs:gap-[10px] sm:gap-[20px]">
      <div class="flight-details-top">
        <div
          class="flight-details-left gap-[4px] mxs:gap-[6px] xsm:gap-[10px] ml-0 mxs:ml-1 xsm:ml-[1rem]"
        >
          <!-- <img :src="data.AirlineLogo" class="airline-logo h-[24px] sm:h-[30px]" /> -->

          <img :src="data.airline" class="airline-logo h-[24px] sm:h-[30px]" />
          <!-- 
          <div class="h-[30px] w-[30px] sm:h-[40px] sm:w-[40px] bg-no-repeat bg-center bg-contain rounded-[50%] "  :style="`background-image: url('http://usbooking.org/us/apiImages/${data.Airline}') !important`" >

          </div> -->
          <p class="text-sm font-semibold xsm:text-base md:text-xl w-[65px] xs:w-auto">
            {{ data.airlineName }}
          </p>
          <p class="text-[10px] font-medium md:font-normal md:text-xs text-[#EA2127]">
            {{ data.flightNo }}
          </p>
          <!-- Date: {{ data.FlightDate }} -->
        </div>
        <div class="flight-details-right !font-['Roboto']">
          <p
            v-if="data.refundable"
            class="text-[10px] text-right xxs:text-xs refundable md:text-sm mr-[10px] mxs:mr-[39px] xsm:mr-[45px]"
          >
            Refundable
          </p>
          <p
            v-else
            class="text-[10px] text-right xxs:text-xs md:text-sm !text-[#FF8A00] mr-[10px] mxs:mr-[39px] xsm:mr-[45px]"
          >
            Non-refundable
          </p>
        </div>
      </div>
      <div class="justify-between flight-details-bottom sm:justify-around">
        <div class="arrival-departure ml-1 xxs:ml-2 xsm:ml-[2rem]">
          <div class="departure">
            <p class="text-sm font-semibold sm:text-base md:text-xl departure-time">
              {{ data.departureTime }}
            </p>
            <p class="hidden text-xs font-semibold sm:text-sm sm:block">
              {{ data.departure }}
            </p>
            <p class="block text-xs font-semibold sm:text-sm sm:hidden">
              {{ data.departureCode }}
            </p>
          </div>
          <img :src="Plane" alt="" class="mx-[2px] xs:mx-2 hidden sm:w-[100px] md:w-[120px]" />
          <img
            :src="PlaneSm"
            alt=""
            class="mx-[2px] xs:mx-2 w-[60px] xxs:w-[75px] sm:w-[100px] md:w-[120px]"
          />
          <div class="arrival">
            <p class="text-sm font-semibold sm:text-base md:text-xl">
              {{ data.arrivalTime }}
            </p>
            <p class="hidden text-xs font-semibold sm:text-sm 2xl:text-base sm:block">
              {{ data.arrival }}
            </p>
            <p class="block text-xs font-semibold sm:text-sm 2xl:text-base sm:hidden">
              {{ data.arrivalCode }}
            </p>
          </div>
        </div>
        <div class="hidden text-xs sm:flex md:text-sm elpased-time bottom-details 2xl:text-base">
          <p>Duration</p>
          <div class="bottom-details-static">
            <img :src="Clock" alt="" class="!h-[12px] xxs:!h-[15px]" />
            <p>{{ data.elapsedTime }} min</p>
          </div>
        </div>
        <div class="hidden text-xs sm:flex md:text-sm luggage bottom-details 2xl:text-base">
          <p>Luggage</p>
          <div class="bottom-details-static">
            <img :src="Luggage" alt="" class="!h-[12px] xxs:!h-[15px]" />
            <p>{{ data.freeBaggage }} KG</p>
          </div>
        </div>
        <div class="hidden text-xs sm:flex md:text-sm seat-class bottom-details 2xl:text-base">
          <p>Class</p>
          <div class="bottom-details-static">
            <img :src="SeatClass" alt="" class="!h-[12px] xxs:!h-[15px]" />
            <p>{{ data.flightClassCode }}</p>
          </div>
        </div>

        <div
          class="flex flex-wrap gap-[2px] xxs:gap-[6px] xs:gap-[10px] xsm:gap-4 sm:hidden w-[65px] mxs:w-[120px] xsm:w-[126px]"
        >
          <div
            class="flex text-[10px] sm:text-xs md:text-sm elpased-time bottom-details 2xl:text-base"
          >
            <div class="bottom-details-static">
              <img :src="Clock" alt="" class="!h-[12px] xxs:!h-[15px]" />
              <p>{{ data.elapsedTime }} min</p>
            </div>
          </div>
          <div class="flex text-[10px] sm:text-xs md:text-sm luggage bottom-details 2xl:text-base">
            <div class="bottom-details-static">
              <img :src="Luggage" alt="" class="!h-[12px] xxs:!h-[15px]" />
              <p>Kg</p>
            </div>
          </div>
          <div
            class="flex text-[10px] sm:text-xs md:text-sm seat-class bottom-details 2xl:text-base"
          >
            <div class="bottom-details-static">
              <img :src="SeatClass" alt="" class="!h-[12px] xxs:!h-[15px]" />
              <p>class {{ data.flightClassCode }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="pricing-details ml-2 sm:ml-[15px]">
      <div class="flex flex-col gap-[2px] text-xs font-bold md:text-sm 2xl:text-base">
        <s class="old-price" v-if="data.discountAmount > 0"
          >{{ data.currency }}
          {{ data.totalPrice.toLocaleString('en-IN') }}
          {{}}
        </s>
        <p class="new-price">
          {{ data.currency }}
          {{ data.totalCommissionedCost.toLocaleString('en-IN') }}
        </p>
      </div>
      <aside class="flex items-end my-[3px] xs:my-1 sm:my-[6px]">
        <div class="flex items-center justify-center gap-[6px] lg:gap-[10px] pb-[6px]">
          <!-- <img
            :src="CoinImg"
            alt=""
            class="h-[14px] w-[14px] sm:h-[18px] sm:w-[18px] lg:h-[20px] lg:w-[20px]"
          /> -->
          <!-- <p class="text-[10px] font-semibold xs:text-xs">
            {{ data.rewardCoins }}
          </p> -->
        </div>
      </aside>

      <!-- <button @click="goToFlightDetail(`${ data.FlightId }`)" class="book-btn">Book Now</button> -->
      <button
        v-if="props.showButton && !newFlightStore.flightSearchPayload.returnFlight"
        @click="
          () => {
            jwtStore.isLoggedIn ? createBooking(data) : (jwtStore.showSignInModel.value = true)
          }
        "
        class="px-4 py-2 text-xs sm:text-sm book-btn"
      >
        Book Now
      </button>
      <!-- @click="flightStore.reserveFlight(`${data.FlightId}`)" -->
      <button
        v-if="props.showButton && newFlightStore.flightSearchPayload.returnFlight"
        class="px-3 py-2 text-xs md:px-4 md:py-2 md:text-sm book-btn"
        @click="selectFlight(data)"
      >
        {{ isSelected ? 'Selected' : 'Select Flight' }}
      </button>
    </div>
  </div>
</template>

<style scoped>
.flight-container {
  display: flex;
  border: 1px solid #dddddd;
  border-radius: 10px;
  align-items: center;
  width: 100%;
  margin-top: 10px;
  background-color: white;
  transition: 0.2s ease;
  cursor: pointer;
}

.flight-container:hover {
  border: 1px solid #ea2127;
}

.flight-details {
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex-grow: 1;
  border-right: 2px solid #b1b1b1;
  height: 100%;
}

.flight-details-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-direction: row;
  gap: 10px;
}

.flight-details-left {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-direction: row;
}

.airline-logo {
  object-fit: contain;
}

.refundable {
  color: #34c759;
}

.flight-details-bottom {
  display: flex;
  align-items: center;
}

img {
  object-fit: contain;
}

.bottom-details {
  flex-direction: column;
  height: fit-content;
  gap: 2px;
}

.bottom-details p {
  color: gray;
}

.bottom-details-static {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 4px;
}

.bottom-details-static img {
  object-fit: contain;
}

.arrival-departure {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

.pricing-details {
  display: flex;
  flex-direction: column;
  justify-content: center;

  height: 100%;
  align-items: center;
}

.old-price {
  color: #ea2127;
}

.book-btn {
  background-color: #ea2127;
  color: white;
  font-weight: 700;
  outline: 0;
  border: 0;
  border-radius: 5px;
  cursor: pointer;
  transition: 0.1s ease-in;
}

.book-btn:hover {
  background-color: #b80006;
}

.selected-flight {
  background-color: #fde5e5;
  border: 1px solid #ea2127;
}
</style>
