<template>
  <article
    class="relative flex flex-col font=['Poppins']"
    v-click-away="() => handleClickOutside()"
  >
    <aside
      class="flex h-[30px] py-2 items-center bg-[#f2f2f2] rounded-none px-[10px] justify-center cursor-pointer gap-3"
      @click="handleInputBoxClick()"
    >
      <img
        :src="`/static/country/Countries/${newFlightStore.searchNationalityFinalQuery.code.toLowerCase()}.imageset/${newFlightStore.searchNationalityFinalQuery.code.toLowerCase()}.png`"
        :class="newFlightStore.searchNationalityFinalQuery.code === 'NP' ? 'h-5' : 'h-4'"
        alt=""
      />
      <input
        type="text"
        class="font-semibold bg-transparent outline-none w-[120px]"
        v-model="newFlightStore.searchNationalityQuery"
        ref="inputBoxReference"
        @click="showDropDown = true"
        @keydown.enter="selectCountryWithKeyboard"
      />
      <CaretDown class="h-4" />
    </aside>
    <aside
      class="absolute flex flex-col overflow-y-auto max-h-[220px] top-[30px] z-[6] bg-white w-full border-[1px]"
      v-if="showDropDown"
    >
      <div
        class="flex items-center hover:bg-[#E2E2E2] w-full cursor-pointer border-b-[1px]"
        @click="() => selectCountryName(country)"
        v-for="country in newFlightStore.getValidCountries"
      >
        <div class="flex items-center p-2">
          <img
            :src="`/static/country/Countries/${country.code.toLowerCase()}.imageset/${country.code.toLowerCase()}.png`"
            class="h-4 mr-4"
            alt=""
          />
          <p class="text-sm min-w-fit">
            {{ country.name }}
          </p>
        </div>
      </div>
    </aside>
  </article>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import CountryArr from '../../assets/country/Countries.json'
import { useNewFlightStore } from '../../stores/newFlightStore.ts'
import { CaretDown } from '@vicons/ionicons5'
import { CountryCode } from '../../models/Flight.interface'
const newFlightStore = useNewFlightStore()
const showDropDown = ref(false)
const inputBoxReference = ref(null)
// const validCountries = computed<CountryCode[]>({
//   get() {
//     return CountryArr.filter(
//       (country: CountryCode) =>
//         country.name
//           .toLowerCase()
//           .includes(newFlightStore.searchNationalityQuery.toLowerCase()) ||
//         country.code
//           .toLowerCase()
//           .includes(newFlightStore.searchNationalityQuery.toLocaleLowerCase())
//     );
//   },
// });
const handleInputBoxClick = () => {
  inputBoxReference.value.focus()
  showDropDown.value = true
}

const selectCountryName = (country: CountryCode) => {
  if (!country) return
  newFlightStore.searchNationalityQuery = country.name
  newFlightStore.searchNationalityFinalQuery = country
  newFlightStore.flightSearchPayload.nationality = country.code
  showDropDown.value = false
}
const handleClickOutside = () => {
  showDropDown.value = false
  let isValid = CountryArr.find(
    (country) => country.name.toLowerCase() === newFlightStore.searchNationalityQuery.toLowerCase()
  )
  if (!isValid) {
    newFlightStore.searchNationalityQuery = newFlightStore.searchNationalityFinalQuery.name
    newFlightStore.flightSearchPayload.nationality = newFlightStore.searchNationalityFinalQuery.code
  }
}
const selectCountryWithKeyboard = () => {
  showDropDown.value = false
  inputBoxReference.value.blur()
  selectCountryName(newFlightStore.getValidCountries[0])
}
</script>
<style scoped></style>
