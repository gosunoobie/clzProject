<template>
  <div
    :class="`flex items-center justify-center w-full xs:w-1/2 lg:w-auto flex-row bottom-right gap-[6px] lg:gap-[10px] min-w-[290px] sm:min-w-[300px] md:min-w-[360px] lg:min-w-auto font-['Poppins'] ${
      newFlightStore.flightSearchPayload.returnFlight && '!gap-[0px] !lg:gap-[0px]'
    }`"
  >
    <aside
      :class="`'min-w-[250px] w-full border-[#b1b1b1] border-[1px] rounded-[5px] px-3 md:px-[20px] py-[6px] xs:py-[8px] bg-white' + ${
        newFlightStore.flightSearchPayload.returnFlight &&
        '!w-1/2 lg:w-auto lg:max-w-[180px] xl:max-w-[205px] rounded-tr-[0px] rounded-br-[0] border-r-[0px] lg:min-w-[180px]'
      }`"
      @click="() => departureDateInputReference.showPicker()"
    >
      <div class="flex gap-2 mb-[2px] lg:mb-[6px]">
        <img :src="CalenderIcon" alt="" class="w-4 sm:w-[18px] bg-white" />
        <p class="text-[#9E9E9E] font-medium text-xs lg:text-sm">Departure Date</p>
      </div>
      <div class="relative icon-and-input outline-none date-sector-input">
        <input
          type="date"
          :min="todaysDate"
          v-model="newFlightStore.inputDepartureDate"
          class="w-full text-sm xs:text-base lg:text-lg font-semibold date-sector-input text-[#595959]"
          ref="departureDateInputReference"
        />
      </div>
    </aside>
    <aside
      v-if="newFlightStore.getTripTypeTwoway"
      :class="`w-1/2 lg:w-auto  lg:max-w-[180px] xl:max-w-[205px] lg:min-w-[180px]  border-[#b1b1b1] border-[1px] rounded-[5px] px-3 md:px-[20px] py-[6px] xs:py-[8px] bg-white ${
        newFlightStore.flightSearchPayload.returnFlight && 'rounded-tl-[0px] rounded-bl-[0px]'
      }`"
      @click="() => returnDateInputReference.showPicker()"
    >
      <div class="flex gap-2 mb-[2px] lg:mb-[6px]">
        <img :src="CalenderIcon" alt="" class="w-4 sm:w-[18px] bg-white" />
        <p class="text-[#9E9E9E] font-medium text-xs lg:text-sm">Return Date</p>
      </div>
      <div class="relative icon-and-input date-sector-input">
        <input
          :min="newFlightStore.inputDepartureDate"
          v-model="newFlightStore.returnDate"
          type="date"
          class="w-full text-sm xs:text-base lg:text-lg font-semibold date-sector-input text-[#595959]"
          ref="returnDateInputReference"
        />
      </div>
    </aside>
    <!-- <input
      type="date"
      v-model="newFlightStore.inputDepartureDate"
      :min="todaysDate"
    />
    <input
      type="date"
      v-model="newFlightStore.returnDate"
      :min="newFlightStore.inputDepartureDate"
    /> -->
    <!-- <pre
      >{{
        newFlightStore.inputDepartureDate
      }},this is the input departure date</pre
    > -->
    <!-- <pre>{{ newFlightStore.returnDate }}, this is the input return date</pre> -->
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watchEffect } from 'vue'
import { useNewFlightStore } from '../../stores/newFlightStore.ts'
import { DatesArray } from '../../components/domesticFlights/utils/dateselect.ts'
const newFlightStore = useNewFlightStore()
const todaysDate = new Date().toISOString().slice(0, 10)
import CalenderIcon from '../../assets/flight/image/calender.png'
const departureDateInputReference = ref(null)
const returnDateInputReference = ref(null)
watchEffect(() => {
  const departureDate = new Date(newFlightStore.inputDepartureDate)
  const returnDate = new Date(newFlightStore.returnDate)
  if (departureDate > returnDate) {
    departureDate.setDate(departureDate.getDate() + 1)
    newFlightStore.returnDate = departureDate.toISOString().slice(0, 10)
  }
  newFlightStore.departureDateArrays = DatesArray(newFlightStore.inputDepartureDate)
  newFlightStore.returnDateArrays = DatesArray(newFlightStore.returnDate)
  console.log('this is the render')
}, newFlightStore.inputDepartureDate)
</script>

<style scoped>
input[type='date']::-webkit-calendar-picker-indicator {
  display: none;
}
.date-sector-input {
  border: 0px solid black;
  outline: none;
  background-color: white !important;
  cursor: pointer;
}
:deep(.n-button__content) {
  background: red !important;
}

input[type='date']::-webkit-clear-button,
input[type='date']::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type='date'] {
  overflow: hidden;
}
</style>
