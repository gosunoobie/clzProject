<template>
  <n-skeleton
    text
    class="w-[240px] xl:w-[300px] min-w-[240px] xl:min-w-[300px]mt-4 rounded-sm lg:rounded-[20px] sm:h-[600px]"
    v-if="newFlightStore.isFlightsLoading"
  />
  <section
    class="w-full lg:w-[240px] xl:w-[300px] relative sticky top-[80px] my-[15px] min-w-[240px] xl:min-w-[300px] rounded-[20px] border-[1px] bg-white border-[#b1b1b1] h-fit"
    v-if="newFlightStore.isFlightsSearched && !newFlightStore.isFlightsLoading"
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      viewBox="0 0 512 512"
      class="w-8 absolute lg:hidden hover:scale-110 cursor-pointer hover:rotate-90 transition-all ease-in-out duration-500 top-[3%] xs:top-[2%] right-[6%]"
      @click="newFlightStore.showFlightFilters = false"
    >
      <path
        d="M448 256c0-106-86-192-192-192S64 150 64 256s86 192 192 192s192-86 192-192z"
        fill="none"
        stroke="currentColor"
        stroke-miterlimit="10"
        stroke-width="32"
      ></path>
      <path
        fill="none"
        stroke="currentColor"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="32"
        d="M320 320L192 192"
      ></path>
      <path
        fill="none"
        stroke="currentColor"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="32"
        d="M192 320l128-128"
      ></path>
    </svg>
    <h2 class="mt-[15px] pb-[10px] px-5 border-[#D9D9D9] border-b-[1px] text-xl font-bold">
      Filters
    </h2>
    <div class="flex flex-wrap flex-row lg:flex-col px-[10px]">
      <aside
        title="Duration"
        class="w-full filter-card border-[#D9D9D9] border-b-[1px] py-5 px-[10px]"
      >
        <h4 class="mb-2 text-lg font-semibold">Price</h4>
        <!-- <n-checkbox-group
          class="flex flex-wrap lg:flex-col gap-[6px]"
          v-model:value="newFlightStore.selectedTicketPricesFilter"
        >
          <n-checkbox value="L"> Lowest First </n-checkbox>
          <n-checkbox value="H"> Highest First </n-checkbox>
        </n-checkbox-group> -->
        <div class="flex flex-wrap lg:flex-col gap-[6px]">
          <n-checkbox
            v-for="(filter, index) in newFlightStore.flightsPriceFilters"
            :value="filter.value"
            :checked="filter.value === newFlightStore.selectedTicketPricesFilter"
            @update:checked="newFlightStore.setFlightsTicketPriceFilter(filter.value)"
            :key="index"
          >
            {{ filter.label }}
          </n-checkbox>
        </div>
      </aside>
      <aside title="Airlines" class="w-full py-5 filter-card px-[10px]">
        <!-- <aside
      title="Airlines"
      class="w-full filter-card border-[#D9D9D9] border-y-[1px] py-5"
      v-if="!newFlightStore.isShowingReturnFlights"
    > -->
        <h4 class="mb-2 text-base font-semibold sm:text-lg">Airlines</h4>
        <n-checkbox-group
          v-model:value="newFlightStore.selectedAirlinesFilter"
          v-if="newFlightStore.departureFlightAirlines.length > 0"
          class="flex flex-wrap lg:flex-col gap-[6px]"
        >
          <n-checkbox
            v-for="(name, index) in newFlightStore.departureFlightAirlines"
            :key="index"
            class="!text-xs sm:!text-sm filter-card-items"
            @update:checked="handleUpdateChecked"
            :value="name"
            >{{ name }}
          </n-checkbox>
        </n-checkbox-group>
        <p v-else>No Airlines Available</p>
      </aside>
      <!-- <aside title="Airlines" class="w-full py-5 filter-card" v-else>
      <h4 class="mb-2 text-base font-semibold sm:text-lg lg:text-xl">
        Airlines
      </h4>
      <div class="flex flex-wrap lg:flex-col gap-[6px]">
        <n-checkbox-group v-model:value="newFlightStore.selectedAirlinesFilter">
          <n-checkbox
            v-for="(name, index) in newFlightStore.returnFlightAirlines"
            :key="index"
            class="!text-xs sm:!text-sm filter-card-items"
            @update:checked="handleUpdateChecked"
            :value="name"
            >{{ name }}
          </n-checkbox>
        </n-checkbox-group>
      </div>
    </aside> -->
      <aside
        title="Ticket-Type"
        class="w-full filter-card border-[#D9D9D9] border-y-[1px] px-[10px] py-5"
      >
        <h4 class="mb-2 text-base font-semibold sm:text-lg">Ticket Type</h4>
        <!-- <n-checkbox-group
          class="flex flex-wrap lg:flex-col gap-[6px]"
          v-model:value="newFlightStore.selectedTicketTypeFilter"
        >
          <n-checkbox value="T"> Refundable </n-checkbox>
          <n-checkbox value="F"> Non-Refundable </n-checkbox>
        </n-checkbox-group> -->
        <div class="flex flex-wrap lg:flex-col gap-[6px]">
          <n-checkbox
            v-for="(filter, index) in newFlightStore.flightsTicketTypeFilters"
            :value="filter.value"
            :checked="filter.value === newFlightStore.selectedTicketTypeFilter"
            @update:checked="newFlightStore.setFlightsTicketTypeFilter(filter.value)"
            :key="index"
          >
            {{ filter.label }}
          </n-checkbox>
        </div>
      </aside>
      <aside
        title="Duration"
        class="w-full filter-card border-[#D9D9D9] border-b-[1px] px-[10px] py-5"
      >
        <h4 class="mb-2 text-base font-semibold sm:text-lg">Duration</h4>
        <div class="flex flex-wrap lg:flex-col gap-[6px]">
          <n-checkbox
            v-for="(filter, index) in newFlightStore.flightsDurationFilters"
            :value="filter.value"
            :checked="filter.value === newFlightStore.selectedDurationTypeFilter"
            @update:checked="newFlightStore.setFlightsDurationFilter(filter.value)"
            :key="index"
          >
            {{ filter.label }}
          </n-checkbox>
        </div>
      </aside>
    </div>
    <!-- 
    {{ newFlightStore.selectedTicketPricesFilter }}
    {{ newFlightStore.selectedAirlinesFilter }}
    {{ newFlightStore.selectedDurationTypeFilter }}
    {{ newFlightStore.selectedTicketTypeFilter }} -->
  </section>
</template>
<script setup lang="ts">
import { NCheckbox, NCheckboxGroup, NSkeleton } from 'naive-ui'
import { useNewFlightStore } from '../../stores/newFlightStore'

const newFlightStore = useNewFlightStore()
const handleUpdateChecked = () => {
  console.log('checked')
}
</script>
