<template>
  <div>
    <n-popconfirm :show-icon="false">
      <template #trigger>
        <CustomButton
          class="!text-xs xs:!text-sm !py-[5px] rounded-none h-full min-w-[150px]"
          v-if="true"
          :label="`${
            newFlightStore.flightSearchPayload.adultPassenger +
            newFlightStore.flightSearchPayload.childPassenger
          } ${
            newFlightStore.flightSearchPayload.adultPassenger +
              newFlightStore.flightSearchPayload.childPassenger >
            1
              ? 'Passengers'
              : 'Passenger'
          } `"
          color="#f2f2f2"
          textColor="black"
        >
          <template v-slot:leftIcon>
            <img :src="PassengerIcon" alt="" class="w-[16px] sm:w-[20px]" />
          </template>
          <template v-slot:rightIcon>
            <Icon>
              <CaretDown />
            </Icon>
          </template>
        </CustomButton>
      </template>
      <template #action>
        <n-card title="" class="dropdown-card !font-['Poppins']" size="small">
          <div class="adult-passenger passenger-count-div">
            <label for="adult">Adult</label>
            <small>12 yrs & above</small>
            <n-input-number
              id="adult"
              class="text-center"
              button-placement="both"
              placeholder=" "
              :min="1"
              :max="Math.min(9 - newFlightStore.flightSearchPayload.childPassenger)"
              v-model:value="newFlightStore.flightSearchPayload.adultPassenger"
            ></n-input-number>
          </div>
          <div class="child-passenger passenger-count-div !font-['Poppins']">
            <label for="child-passenger">Child</label>
            <small>Under 12 yrs</small>
            <n-input-number
              id="child-passenger"
              button-placement="both"
              class="text-center"
              placeholder=" "
              :min="0"
              :max="Math.min(9 - newFlightStore.flightSearchPayload.adultPassenger)"
              v-model:value="newFlightStore.flightSearchPayload.childPassenger"
            ></n-input-number>
          </div>
          <!-- <n-button class="apply-pasenger" color="#EA2127">Apply</n-button> -->
        </n-card>
      </template>
    </n-popconfirm>
  </div>
</template>

<script setup lang="ts">
import { useNewFlightStore } from '../../stores/newFlightStore.js'
const newFlightStore = useNewFlightStore()
import PassengerIcon from '../../assets/services/passenger.png'
import { NCard, NInputNumber, NPopconfirm } from 'naive-ui'
import { CaretDown, Search } from '@vicons/ionicons5'
import { Icon } from '@vicons/utils'
import CustomButton from '../CustomElements/CustomButton.vue'
</script>

<style scoped>
.passenger-count-div {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
}

.passenger-count-div label {
  font-weight: 600;
}

.apply-pasenger {
  width: 100%;
}
.dropdown-card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: 0;
  padding: 0px;
}

.dropdown-card div,
n-button {
  margin: 5px;
}

.n-input-number {
  width: 100px;
}
</style>
