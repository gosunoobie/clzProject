<template>
  <!-- <div class=" w-full lg:w-[25%] mt-0">
    <n-card style="background-color: #f4f4f4" title="Airlines">
      <n-skeleton text :repeat="2" />
      <n-skeleton text class="w-full lg:w-[60%]" />
    </n-card>
  </div> -->
  <n-skeleton
    text
    class="w-full rounded-md h-[72px] my-[15px]"
    v-if="newFlightStore.isFlightsLoading"
  />

  <div
    v-if="newFlightStore.isFlightsSearched && !newFlightStore.isFlightsLoading"
    class="hidden lg:block"
  >
    <section
      v-if="!newFlightStore.isShowingReturnFlights"
      class="flex justify-around px-5 py-3 rounded-lg mt-[15px] font-['Poppins'] font-semibold text-base bg-white"
    >
      <article v-for="(day, index) in newFlightStore.departureDateArrays" class="" :key="day.date">
        <aside
          @click="() => changeDeparutreDateAndCallApi(day.date)"
          :class="
            checkDepartureDate(day.date) ? 'selected cursor-pointer' : 'unselected cursor-pointer'
          "
        >
          <p class="text-center">
            {{ day.date }}
          </p>
          <p class="text-center">
            {{ day.day }}
          </p>
        </aside>
      </article>
    </section>
    <section
      v-else
      class="flex justify-around px-5 py-3 mt-[15px] rounded-lg font-['Poppins'] font-semibold text-base bg-white"
    >
      <article v-for="(day, index) in newFlightStore.returnDateArrays" class="" :key="day.date">
        <aside
          @click="() => changeReturnDateAndCallApi(day.date)"
          :class="checkReturnDate(day.date) ? 'selected' : 'unselected'"
        >
          <p class="text-center">
            {{ day.date }}
          </p>
          <p class="text-center">
            {{ day.day }}
          </p>
        </aside>
      </article>
    </section>
    <!-- <section class="flex gap-2">
      <article
        v-for="(day, index) in newFlightStore.returnDateArrays"
        class=""
        :key="day.date"
      >
        <aside
          @click="() => changeReturnDate(day.date, index)"
          :class="checkReturnDate(day.date) ? 'selected' : 'unselected'"
        >
          <p>
            {{ day.date }}
          </p>
          <p>
            {{ day.day }}
          </p>
        </aside>
      </article>
    </section> -->
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useNewFlightStore } from '../../stores/newFlightStore.ts'
const newFlightStore = useNewFlightStore()
import { NSkeleton } from 'naive-ui'

const selectedDateIndex = ref(0)

const changeDeparutreDateAndCallApi = (date) => {
  changeDepartureDate(date)
  newFlightStore.getDepartureFlightLists()
}
const changeDepartureDate = (date) => {
  const dayAfterTommorowDate = new Date()
  const dateComponents = date.split('/')
  const month = dateComponents[0]
  const day = dateComponents[1]
  const year = dateComponents[2]

  // Create a new date string in YYYY-MM-DD format
  const convertedDateString = `${year}-${month}-${day}`
  const selectedDate = new Date(convertedDateString)

  dayAfterTommorowDate.setDate(dayAfterTommorowDate.getDate() + 2)
  //  if (dayAfterTommorowDate >= selectedDate) return;
  newFlightStore.inputDepartureDate = convertedDateString
}
const changeReturnDateAndCallApi = (date) => {
  changeReturnDate(date)
  newFlightStore.getReturnFlightLists()
  newFlightStore.getDepartureFlightLists()
}

const changeReturnDate = (date) => {
  const returnDate = new Date(date)
  const dateComponents = date.split('/')
  const month = dateComponents[0]
  const day = dateComponents[1]
  const year = dateComponents[2]

  // Create a new date string in YYYY-MM-DD format
  const convertedDateString = `${year}-${month}-${day}`
  const selectedDate = new Date(convertedDateString)

  if (selectedDate <= returnDate) return
  newFlightStore.returnDate = convertedDateString
}
const checkDepartureDate = (date) => {
  const dateComponents = date.split('/')
  const month = dateComponents[0]
  const day = dateComponents[1]
  const year = dateComponents[2]

  // Create a new date string in YYYY-MM-DD format
  const formattedDate = `${year}-${month}-${day}`
  return formattedDate === newFlightStore.inputDepartureDate
}

const checkReturnDate = (date) => {
  const dateComponents = date.split('/')
  const month = dateComponents[0]
  const day = dateComponents[1]
  const year = dateComponents[2]

  // Create a new date string in YYYY-MM-DD format
  const formattedDate = `${year}-${month}-${day}`
  return formattedDate === newFlightStore.returnDate
}
</script>

<style scoped>
:deep(.selected) {
  color: red;
}
</style>
