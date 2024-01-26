<template>
  <div class="flex flex-col gap-[5px] xs:gap-0 xs:flex-row relative grow font-['Poppins']">
    <article
      class="relative xsm:min-w-[290px] sm:min-w-[300px] md:min-w-[360px] lg:min-w-[200px] w-full xs:w-1/2 flex items-center bg-white rounded-md border-[1px] border-[#b1b1b1]"
      v-click-away="() => handleDepartureLocationClickOutside()"
    >
      <aside
        class="flex items-center justify-between h-full px-5 py-[6px] xs:py-[10px] xl:pl-[20px]"
        @click="() => handleDepartureOuterSelection()"
      >
        <div class="flex flex-col">
          <p class="font-medium text-xs md:text-sm text-[#9e9e9e] mb-0 lg:mb-[2px]">From</p>
          <input
            type="text"
            v-model="newFlightStore.searchDepatureLocationQuery"
            @keydown.enter="selectDeparutreLocationWithKeyboard"
            @click="newFlightStore.showDepartureLocationDropDown = true"
            placeholder="eg: KATHMANDU "
            class="outline-none w-full text-sm xs:text-base lg:text-lg font-semibold text-[#595959]"
            ref="departureInputBox"
          />
        </div>
        <img
          :src="LocationIcon"
          alt=""
          class="absolute right-[20px] xs:right-2 top-1/4 h-[24px] sm:h-[30px]"
        />
      </aside>
      <aside
        class="absolute z-[6] top-[105%] xs:top-[75px] w-full left-0 flex flex-col overflow-y-auto max-h-[270px] bg-white border-b-[1px] border-x-[1px]"
        v-if="newFlightStore.showDepartureLocationDropDown"
      >
        <div class="" v-for="location in newFlightStore.getValidDepartureLocations">
          <p
            class="text-sm xl:text-base hover:bg-[#f2f2f2] px-4 py-3 cursor-pointer border-b-[1px]"
            @click="() => selectDepartureLocationName(location)"
          >
            {{ location.label }} ({{ location.value }})
          </p>
        </div>
      </aside>
    </article>
    <div class="min-w-[24px] md:min-w-[30px] 2xl:min-w-[32.5px] relative">
      <div
        class="absolute transform -translate-x-1/2 -translate-y-1/2 top-1/2 left-[85%] xs:left-1/2 z-[5]"
      >
        <img
          :src="FromToIcon"
          alt=""
          class="min-h-[32px] min-w-[32px] max-h-[40px] xs:max-h-auto rotate-90 xs:rotate-0 xs:min-h-[40px] xs:min-w-[40px] sm:min-h-[45px] sm:min-w-[45px] 2xl:min-h-[45px] 2xl:min-w-[45px] cursor-pointer"
          @click="newFlightStore.interchangeDestination"
        />
      </div>
    </div>

    <article
      class="relative w-full xs:w-1/2 flex items-center bg-white rounded-md border-[1px] border-[#b1b1b1]"
      v-click-away="() => handleReturnLocationClickOutside()"
    >
      <aside
        class="flex items-center justify-between w-full h-full pl-6 py-[6px] xs:py-[10px]"
        @click="() => handleReturnOuterSelection()"
      >
        <div class="flex flex-col">
          <p class="font-medium text-xs md:text-sm text-[#9e9e9e] mb-0 lg:mb-[2px]">To</p>
          <input
            type="text"
            v-model="newFlightStore.searchReturnLocationQuery"
            @keydown.enter="selectReturnLocationWithKeyboard"
            @click="newFlightStore.showReturnLocationDropDown = true"
            placeholder="eg: POKHARA"
            class="outline-none w-full text-sm xs:text-base lg:text-lg font-semibold text-[#595959]"
            ref="returnInputBox"
          />
        </div>
        <img
          :src="LocationIcon"
          alt=""
          class="absolute right-[20px] xs:right-2 top-1/4 h-[24px] sm:h-[30px]"
        />
      </aside>
      <aside
        class="absolute z-[6] top-[105%] xs:top-[75px] w-full left-0 flex flex-col overflow-y-auto max-h-[180px] xs:max-h-[270px] bg-white border-b-[1px] border-x-[1px]"
        v-if="newFlightStore.showReturnLocationDropDown"
      >
        <div class="" v-for="location in newFlightStore.getValidReturnLocations">
          <p
            class="text-sm xl:text-base hover:bg-[#f2f2f2] px-4 py-3 cursor-pointer border-b-[1px]"
            @click="() => selectReturnLocationName(location)"
          >
            {{ location.label }} ({{ location.value }})
          </p>
        </div>
      </aside>
    </article>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useNewFlightStore } from '@/stores/newFlightStore'
import FromToIcon from '@/assets/flight/image/fromto.png'
import LocationIcon from '@/assets/flight/image/location.png'
import { SectorCode } from '@/models/Flight.interface'

const newFlightStore = useNewFlightStore()
const departureInputBox = ref(null)
const returnInputBox = ref(null)
onMounted(() => {
  // newFlightStore.getLocationSectorCodes();
})

const handleReturnOuterSelection = () => {
  returnInputBox.value.focus()
  newFlightStore.showReturnLocationDropDown = true
}
const handleDepartureOuterSelection = () => {
  departureInputBox.value.focus()
  newFlightStore.showDepartureLocationDropDown = true
}

const selectDepartureLocationName = (location: SectorCode) => {
  if (!location) return
  newFlightStore.searchDepatureLocationQuery = location.label
  newFlightStore.finalDepartureLocationQueryValue = location
  newFlightStore.setOriginLocationCode(location.value)
  newFlightStore.showDepartureLocationDropDown = false
}
const selectDeparutreLocationWithKeyboard = () => {
  newFlightStore.showDepartureLocationDropDown = false
  departureInputBox.value.blur()
  selectDepartureLocationName(newFlightStore.getFirstValidDepartureLocations)
}
const selectReturnLocationWithKeyboard = () => {
  newFlightStore.showReturnLocationDropDown = false

  returnInputBox.value.blur()
  selectReturnLocationName(newFlightStore.getFirstValidReturnLocations)
}
const handleDepartureLocationClickOutside = () => {
  newFlightStore.showDepartureLocationDropDown = false

  if (!newFlightStore.finalReturnLocationQueryValue) return
  let isValid = newFlightStore.sectors_list.find(
    (location) =>
      location.label.toUpperCase() === newFlightStore.searchDepatureLocationQuery.toUpperCase()
  )
  if (!isValid) {
    if (!newFlightStore.finalDepartureLocationQueryValue)
      return (newFlightStore.searchDepatureLocationQuery = '')

    newFlightStore.searchDepatureLocationQuery =
      newFlightStore.finalDepartureLocationQueryValue.label
  } else {
    newFlightStore.searchDepatureLocationQuery = isValid.label
    if (newFlightStore.finalDepartureLocationQueryValue)
      newFlightStore.finalDepartureLocationQueryValue = isValid
  }
}
const selectReturnLocationName = (location) => {
  if (!location) return
  newFlightStore.searchReturnLocationQuery = location.label
  newFlightStore.finalReturnLocationQueryValue = location
  newFlightStore.setDestinationLocationCode(location.value)
  newFlightStore.showReturnLocationDropDown = false
}
const handleReturnLocationClickOutside = () => {
  newFlightStore.showReturnLocationDropDown = false

  if (!newFlightStore.finalDepartureLocationQueryValue) return
  let isValid = newFlightStore.sectors_list.find(
    (location) =>
      location.label.toUpperCase() === newFlightStore.searchReturnLocationQuery.toUpperCase()
  )
  if (!isValid) {
    if (!newFlightStore.finalReturnLocationQueryValue)
      return (newFlightStore.searchReturnLocationQuery = '')

    newFlightStore.searchReturnLocationQuery = newFlightStore.finalReturnLocationQueryValue.label
  } else {
    newFlightStore.searchReturnLocationQuery = isValid.label
    if (newFlightStore.finalReturnLocationQueryValue)
      newFlightStore.finalReturnLocationQueryValue = isValid
  }
}
</script>

<style scoped></style>
