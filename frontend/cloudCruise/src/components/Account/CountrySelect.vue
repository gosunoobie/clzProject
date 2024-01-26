<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { useActivityStore } from '../../stores/activityStore'
import dropDownIcon from '../../assets/layout/image/Vectordropdown.png'
import countryArr from '../../assets/country/Countries.json'
import { defineEmits } from 'vue'
const emit = defineEmits(['selected'])
const selectInputBox = ref(null)
const searchCountryQuery = ref('Nepal')
const currentCountryCode = ref('NP')

let isDropdownOpenFrom = ref(false)

let activityStore = useActivityStore()

const filteredServices = computed(() => {
  return countryArr.filter((service) => {
    return service.name.toLowerCase().includes(searchCountryQuery.value.toLowerCase())
  })
})

// console.log(searchCountryQuery.value, "this is the quey");

const clickServiceItem = (service_name: string, service_code: string) => {
  activityStore.searchActivityQuery.service_name = service_name
  searchCountryQuery.value = service_name
  isDropdownOpenFrom.value = false
  currentCountryCode.value = service_code
  // console.log(selectInputBox.value);
  selectInputBox?.value.blur()
  emit('selected', service_name)
}

watch(searchCountryQuery, () => {
  if (searchCountryQuery.value.length < 1) {
    activityStore.searchActivityQuery = {}
  }
})
</script>

<template>
  <article
    class="border-[1px] border-[#b1b1b1] flex items-center rounded-md w-full justify-between relative cursor-pointer"
    v-click-away="() => (isDropdownOpenFrom = false)"
  >
    <div
      @click="selectInputBox.focus(), (isDropdownOpenFrom = true)"
      class="flex items-center justify-between w-full px-3"
      id="from"
      ref="customInputDiv"
    >
      <aside class="flex flex-col w-3/4">
        <!-- <p class="text-[10px] font-semibold">Select Country</p> -->
        <div class="icon-and-input">
          <div>
            <img
              :src="`/static/country/Countries/${currentCountryCode.toLowerCase()}.imageset/${currentCountryCode.toLowerCase()}.png`"
              class="w-6 mr-4"
              alt=""
            />
          </div>
          <input
            v-model="searchCountryQuery"
            type="text"
            ref="selectInputBox"
            @change="isDropdownOpenFrom = true"
            class="sector-input text-sm sm:text-[15px] font-normal h-[38px] sm:h-[45px] w-full outline-none"
            placeholder="Your Country"
          />
        </div>
      </aside>

      <div class="">
        <img
          :src="dropDownIcon"
          alt="location"
          class="min-w-[12px] max-w-[12px] min-h-[8px] max-h-[8px] md:w-4"
        />
      </div>
    </div>
    <article
      class="location-filter-dropdown w-full rounded-md max-h-[200px]"
      v-if="isDropdownOpenFrom"
    >
      <aside v-if="filteredServices.length">
        <div
          class="flex items-center text-xs font-semibold location sm:text-[15px] sm:font-bold"
          v-for="(service, id) in filteredServices"
          :key="id"
          :value="service.name"
          @click="() => clickServiceItem(service.name, service.code)"
        >
          <img
            :src="`/static/country/Countries/${service.code.toLowerCase()}.imageset/${service.code.toLowerCase()}.png`"
            class="w-6 mr-4"
            alt=""
          />
          <!-- <img src='../../assets/country/Countries/af.imageset/af.png' class="w-6 mr-4" alt=""> -->

          <p>{{ service.name }}</p>

          <span class="ml-auto">{{ service.prefix }}</span>
        </div>
      </aside>
      <aside v-else>
        <div class="no-results">No results found</div>
      </aside>
    </article>
  </article>
</template>

<style scoped>
.location-filter-dropdown {
  position: absolute;
  top: 100%;
  background-color: white;
  border: 1px solid #b1b1b1;
  padding: 6px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  left: 0;
  height: fit-content;
  overflow: auto;
  z-index: 10;
}

.location-filter-dropdown::-webkit-scrollbar {
  width: 8px;
  /* Set the width of the scrollbar */
}

.location-filter-dropdown::-webkit-scrollbar-track {
  background-color: #f8f2f2;
  /* Set the color of the scrollbar track */
}

.location-filter-dropdown::-webkit-scrollbar-thumb {
  background-color: #d2cfcf;
  /* Set the color of the scrollbar thumb */
}

.location {
  /* background-color: rgb(211, 197, 197); */
  padding: 10px;
  border-radius: 5px;
  font-weight: 400;
}

.location:hover {
  background-color: #f2f2f2;
  cursor: pointer;
}

.custom-location-input:target-within {
  border: 2px solid black;
}

.icon-and-input {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.sector-input {
  border: 0px solid black;
  outline: 0;
  background: none;

  width: 100%;
  cursor: pointer;
}

.tt_select:focus {
  border: 1px solid red !important;
}
</style>
