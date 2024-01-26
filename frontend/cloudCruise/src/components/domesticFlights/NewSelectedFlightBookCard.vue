<template>
  <section
    v-if="
      newFlightStore.flightSearchPayload.returnFlight && selectedDeparture && selectedReturnFlight
    "
    class="fixed z-10 bottom-0 xs:border-b-[#b1b1b1] xs:border-b-[1px] xs:rounded-lg rounded-[0px] bg-white w-full h-fit"
  >
    <section
      class="flex justify-around py-3 2xl:py-5 px-3 xs:px-5 lg:px-12 xl:px-24 border-[#9e9e9e] border-t-[1px]"
    >
      <article class="flex">
        <img
          :src="getAirlineLogoUrl(selectedDeparture.Airline)"
          class="w-[45px] xl:w-[55px] h-[32px] xl:h-[40px] mt-1 hidden md:block"
        />

        <div class="flex flex-col justify-between xs:ml-[15px] xs:mr-[28px]">
          <h4 class="font-bold xs:font-semibold text-sm xs:text-base xl:text-lg">
            Departure Flight
          </h4>
          <footer class="">
            <h5 class="text-xs xl:text-sm font-medium">
              {{ selectedDeparture.AirlineName }}
            </h5>
            <p class="text-xs xl:text-sm font-medium">
              {{ selectedDeparture.FlightDate }}
              <span class="ml-[10px]">
                {{ selectedDeparture.DepartureTime }}
              </span>
            </p>
          </footer>
        </div>

        <div class="flex-col justify-between hidden sm:flex">
          <h4 class="text-primary-400 text-sm font-medium mt-1">
            {{ selectedDeparture.FlightNo }}
          </h4>
          <h4 class="text-sm font-medium">
            {{ selectedDeparture.Currency }}
            {{ new Intl.NumberFormat('en-IN', {}).format(selectedDeparture.totalCommissionedCost) }}
          </h4>
        </div>
      </article>
      <article class="flex">
        <img
          :src="getAirlineLogoUrl(selectedReturnFlight.Airline)"
          class="w-[45px] xl:w-[55px] h-[32px] xl:h-[40px] mt-1 hidden lg:block"
        />
        <div class="flex flex-col justify-between xs:ml-[15px] xs:mr-[28px]">
          <h4 class="font-bold xs:font-semibold text-sm xs:text-base xl:text-lg">Return Flight</h4>
          <footer class="">
            <h5 class="text-xs xl:text-sm font-medium">
              {{ selectedReturnFlight.AirlineName }}
            </h5>
            <p class="text-xs xl:text-sm font-medium">
              {{ selectedReturnFlight.FlightDate }}
              <span class="ml-[10px]">
                {{ selectedReturnFlight.DepartureTime }}
              </span>
            </p>
          </footer>
        </div>

        <div class="flex-col justify-between hidden sm:flex">
          <h4 class="text-primary-400 text-sm font-medium mt-1">
            {{ selectedReturnFlight.FlightNo }}
          </h4>
          <h4 class="text-sm font-medium">
            {{ selectedReturnFlight.Currency }}
            {{
              new Intl.NumberFormat('en-IN', {}).format(selectedReturnFlight.totalCommissionedCost)
            }}
          </h4>
        </div>
      </article>
      <aside class="flex flex-col gap-[2px]">
        <h5 class="font-semibold text-sm xl:text-base xl:text-lg">
          {{ selectedReturnFlight.Currency }}
          {{
            new Intl.NumberFormat('en-IN', {}).format(
              selectedDeparture.totalCommissionedCost + selectedReturnFlight.totalCommissionedCost
            )
          }}
        </h5>
        <div
          class="px-3 sm:px-5 py-2 cursor-pointer bg-primary-400 rounded-md text-sm xl:text-base text-white font-bold"
          @click="
            () => {
              jwtStore.isLoggedIn
                ? newFlightStore.reserveRoundFlight()
                : (jwtStore.showSignInModel.value = true)
            }
          "
          type="submit"
        >
          Book Now
        </div>
      </aside>
    </section>
  </section>
</template>
<script setup lang="ts">
import { NCard, NText, NButton } from 'naive-ui'
import { useNewFlightStore } from '../../stores/newFlightStore'
import { useJwtStore } from '../../stores/jwt'
import { COLORS } from '../../constants/colors'
import { computed } from 'vue'
import CustomButton from '../CustomElements/CustomButton.vue'
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
}
const newFlightStore = useNewFlightStore()
const jwtStore = useJwtStore()

const selectedDeparture = computed(() => {
  return newFlightStore.selectedFlight.departureFlight
})

const selectedReturnFlight = computed(() => {
  return newFlightStore.selectedFlight.returnFlight
})
</script>
<style scoped>
.main-div {
  display: flex;
  justify-content: space-between;
}
</style>
