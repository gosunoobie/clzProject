<template>
  <section
    class="bg-white rounded-[20px] px-[10px] xs:px-4 sm:px-5 xl:px-[30px] py-[10px] xs:py-[18px] xl:py-[20px] flex flex-col gap-[10px] xs:gap-4 md:gap-6 xl:gap-[30px]"
  >
    <header class="flex justify-between">
      <div class="flex flex-col md:flex-row gap-3 xl:gap-[30px]">
        <Checkboxes />
        <div class="flex gap-[15px] xs:gap-5 xl:gap-[30px]">
          <Passengers />

          <nationalityBox />
        </div>
      </div>
    </header>
    <footer class="flex justify-between flex-col lg:flex-row w-full gap-3 xl:gap-5">
      <LocationBoxes />
      <div
        class="flex flex-col xs:flex-row gap-[10px] xsm:gap-6 md:gap-[30px] lg:gap-3 xl:gap-5 w-full lg:w-auto"
      >
        <Calenders />
        <button
          @click="
            () => {
              searchFlights()
              $router.push({ name: 'FlightList' })
            }
          "
          class="w-full flex items-center gap-2 text-base xsm:text-lg md:text-xl font-bold rounded-[5px] w-1/2 lg:w-[120px] py-[13px] xl:w-[150px] justify-center text-white uppercase bg-primary-400"
        >
          Search
        </button>
      </div>
    </footer>
    <!-- <pre>

    <footer class="flex w-full bg-green-600">
      <article class="w-[1000px]">this</article>
      <aside class="bg-red-600 w-full">
        <input type="text" />
      </aside>
    </footer>
{{ newFlightStore.flightSearchPayload }}</pre> -->
  </section>
</template>

<script setup lang="ts">
import Checkboxes from './Checkboxes.vue'
import nationalityBox from './nationalityBox.vue'
import Passengers from './Passengers.vue'
import LocationBoxes from './LocationBoxes.vue'
import Calenders from './Calenders.vue'
import { useNewFlightStore } from '../../stores/newFlightStore'
const newFlightStore = useNewFlightStore()
const searchFlights = () => {
  newFlightStore.getDepartureFlightLists()
  if (newFlightStore.flightSearchPayload.returnFlight) {
    newFlightStore.getReturnFlightLists()
  }
}
</script>
<style scoped></style>
