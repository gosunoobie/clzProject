<template>
  <div class="reserving-div" v-if="newFlightStore.reservingFlight">
    <div class="reserving-card">
      <p class="text-sm sm:text-base xl:text-xl">Reserving flight....</p>
      <n-spin size="small" />
    </div>
  </div>
  <main class="mx-[6px] xs:mx-5 md:mx-[50px] xl:mx-[100px] mb-2 xs:mb-5 font-['Poppins']">
    <section
      class="!w-[100vw] left-0 h-[71vh] DomesticFlightsBackground absolute bg-no-repeat bg-center bg-cover z-[-1] top-0"
    ></section>
    <h1 class="text-[28px] lg:text-[32px] font-bold pt-[30px] pb-[10px] text-white">
      Domestic Flights
    </h1>
    <FlightSearchBox />
    <DateSelector />
    <section class="flex flex-col lg:flex-row gap-5">
      <div class="hidden lg:block">
        <FlightFilters />
      </div>
      <FlightTabs />
    </section>
  </main>
  <NewFlightSelectedBookCard />
  <teleport to="body" v-if="newFlightStore.showFlightFilters">
    <section
      class="w-[100vw] flex justify-center items-center mt-[40px] h-[100vh] bg-[rgba(0,0,0,0.75)] fixed top-0 z-50"
    >
      <div class="block lg:hidden mx-5">
        <FlightFilters />
      </div>
    </section>
  </teleport>
</template>

<script setup lang="ts">
import FlightSearchBox from '@/components/domesticFlights/FlightSearchBox.vue'
import DateSelector from '@/components/domesticFlights/DateSelector.vue'
import FlightTabs from '@/components/domesticFlights/FlightTabs.vue'
import FlightFilters from '@/components/domesticFlights/FlightFilters.vue'
import NewFlightSelectedBookCard from '@/components/domesticFlights/NewSelectedFlightBookCard.vue'
import { NSpin } from 'naive-ui'
import { useNewFlightStore } from '@/stores/newFlightStore'
const newFlightStore = useNewFlightStore()
</script>
<style scoped>
.blur {
  filter: blur(4px);
  transition: 0.3s ease-in-out;
}

.reserving-div {
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  position: fixed;
  display: grid;
  overflow: hidden;
  place-items: center;
  text-align: center;
  z-index: 20;
  backdrop-filter: blur(4px);
  transition: 0.2s ease-in-out;
}

.reserving-card {
  display: flex;
  width: 250px;
  font-weight: bold;
  font-size: 20px;
  justify-content: center;
  align-items: center;
  background-color: white;
  flex-direction: row;
  gap: 10px;
  padding: 20px;
  border: 1px solid #e1e1e1;
  border-radius: 20px;
  box-shadow: 10px 10px 204px 45px rgba(0, 0, 0, 0.17);
  transition: 0.5s ease-in-out;
}
.DomesticFlightsBackground {
  background-image: url(../../assets/layout/image/flightBg.webp);
}
@media screen and (max-width: 670px) {
  .DomesticFlightsBackground {
    background-image: url(../../assets/layout/image/flightsBackgroundMoblie.png);
  }
}
</style>
