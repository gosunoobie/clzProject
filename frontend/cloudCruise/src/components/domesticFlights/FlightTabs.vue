<template>
  <n-skeleton text class="w-full rounded-md h-[500px]" v-if="newFlightStore.isFlightsLoading" />

  <section
    class="w-full mt-[10px] sm:mt-[15px]"
    v-if="newFlightStore.isFlightsSearched && !newFlightStore.isFlightsLoading"
  >
    <header class="flex justify-between w-full bg-[#8a020d] rounded-[8px] px-5 py-[13px] mb-[5px]">
      <aside class="font-semibold text-sm lg:text-base text-white">
        {{ newFlightStore.flightSearchPayload.originlocationcode }} -
        {{ newFlightStore.flightSearchPayload.destinationLocationCode }}
      </aside>
      <aside class="flex items-center gap-3">
        <p class="text-sm lg:text-base font-normal text-white">
          {{
            newFlightStore.isCurrentTabDeparture
              ? newFlightStore.getFilteredDepartureFlights.length
              : newFlightStore.getFilteredReturnFlights.length
          }}
          results found
        </p>
        <p class="block lg:hidden bg-white w-[2px] h-6"></p>
        <div
          class="flex gap-3 items-center lg:hidden cursor-pointer"
          @click="newFlightStore.showFlightFilters = true"
        >
          <img :src="FilterIcon" class="airline-logo h-[20px]" />
          <p class="text-sm text-white font-semibold">Filter By</p>
        </div>
      </aside>
    </header>
    <div class="tab-buttons-container" v-if="newFlightStore.flightSearchPayload.returnFlight">
      <!-- TODO: Fix the issue where the departure tab hides after selecting return tab -->
      <button
        :class="!newFlightStore.isShowingReturnFlights ? 'activeTab' : 'inactiveTab'"
        @click="() => handleDepartureClick()"
      >
        Departure Flights
      </button>
      <button
        :class="newFlightStore.isShowingReturnFlights ? 'activeTab' : 'inactiveTab'"
        v-if="newFlightStore.flightSearchPayload.returnFlight"
        @click="() => handleReturnClick()"
      >
        Return Flights
      </button>
    </div>
    <article class="flex flex-col w-full">
      <FlightComponent
        v-if="!newFlightStore.isShowingReturnFlights"
        :data="flight"
        :key="flight.FlightId"
        v-for="flight in newFlightStore.getFilteredDepartureFlights"
      />
      <FlightComponent
        v-if="newFlightStore.isShowingReturnFlights"
        :data="flight"
        :key="flight.FlightId"
        v-for="flight in newFlightStore.getFilteredReturnFlights"
      />
      <div
        class="w-full bg-white flex flex-col gap-5 no-flights-box-shadow justify-center items-center rounded-[20px] h-[310px] xs:h-[400px] md:h-[475px] my-3"
        v-if="
          newFlightStore.isShowingReturnFlights &&
          newFlightStore.getFilteredReturnFlights.length === 0
        "
      >
        <img
          :src="NoFlightsImage"
          class="w-[70%] sm:w-[400px] md:w-[60%] rounded-[20px]"
          loading="lazy"
        />
        <h3 class="font-[Poppins] text-[#656565] font-semibold text-base md:text-lg lg:text-xl">
          Sorry! No matching flights found
        </h3>
      </div>
      <div
        class="w-full bg-white flex flex-col gap-5 no-flights-box-shadow justify-center items-center rounded-[20px] h-[310px] xs:h-[400px] md:h-[475px] my-3"
        v-if="
          !newFlightStore.isShowingReturnFlights &&
          newFlightStore.getFilteredDepartureFlights.length === 0
        "
      >
        <img
          :src="NoFlightsImage"
          class="w-[70%] sm:w-[400px] md:w-[60%] rounded-[20px]"
          loading="lazy"
        />
        <h3 class="font-[Poppins] text-[#656565] font-semibold text-base md:text-lg lg:text-xl">
          Sorry! No matching flights found
        </h3>
      </div>
    </article>
  </section>
</template>
<script setup lang="ts">
import { ref } from 'vue'
import { useNewFlightStore } from '@/stores/newFlightStore'
import FlightComponent from './FlightComponent.vue'
const newFlightStore = useNewFlightStore()
import { NSkeleton } from 'naive-ui'
import FilterIcon from '@/assets/flight/image/sort.png'
import NoFlightsImage from '@/assets/flight/image/noflights.png'

const showFlightFilters = ref(false)
const handleDepartureClick = () => {
  newFlightStore.setIsShowingReturnFlights(false)
  newFlightStore.isCurrentTabDeparture = true
  newFlightStore.interchangeDestination()
}
const handleReturnClick = () => {
  newFlightStore.setIsShowingReturnFlights(true)
  newFlightStore.isCurrentTabDeparture = false
  newFlightStore.interchangeDestination()
}
</script>
<style scoped>
.tab-buttons-container {
  background-color: white;
  overflow: hidden;
  border-radius: 8px;
  width: 100%;
  display: flex;
  gap: 10px;
  border: 1px solid #b1b1b1;
}

.activeTab,
.inactiveTab {
  outline: 0;
  border: 0;
  cursor: pointer;
  height: 100%;
  padding: 9px 30px;
  font-weight: 600;
  font-size: 16px;
  text-transform: uppercase;
  background-color: white;
  transition: 0.3s ease;
}

.activeTab {
  border-bottom: 2px solid #ea2127;

  color: #ea2127;
}

.inactiveTab {
  color: black;
}

.no-flights-box-shadow {
  box-shadow: 0px 4px 10px 0px rgba(0, 0, 0, 0.25);
}
@media screen and (max-width: 1038px) {
  .activeTab,
  .inactiveTab {
    font-weight: 600;
    font-size: 14px;
  }
}
@media screen and (max-width: 670px) {
  .activeTab,
  .inactiveTab {
    font-weight: 600;
    font-size: 12px;
  }
}
</style>
