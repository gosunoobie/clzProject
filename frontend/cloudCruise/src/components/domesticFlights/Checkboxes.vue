<template>
  <aside class="flex items-center gap-4 mr-2 md:gap-[20px]">
    <label class="text-xs checkbox-container gap-1 xs:text-sm !font-['Poppins']">
      <input
        id="oneway"
        type="radio"
        :value="false"
        v-model="newFlightStore.flightSearchPayload.returnFlight"
      />
      <div class="checkmark-container">
        <span class="capitalize checkmark-label"> one way </span>
        <span class="checkmark"></span>
        <span class="checkbox-back"></span>
      </div>
    </label>
    <label class="text-xs checkbox-container gap-1 xs:text-sm !font-['Poppins']">
      <input
        id="twoway"
        type="radio"
        :value="true"
        v-model="newFlightStore.flightSearchPayload.returnFlight"
      />
      <div class="checkmark-container">
        <span class="capitalize checkmark-label"> Two way </span>
        <span class="checkmark"></span>
        <span class="checkbox-back"></span>
      </div>
    </label>
  </aside>
</template>
<script lang="ts" setup>
import { useNewFlightStore } from '@/stores/newFlightStore'

const newFlightStore = useNewFlightStore()
</script>
<style>
.checkbox-container {
  display: flex;
  position: relative;
  align-items: center;
  padding-left: 30px;
  padding-right: 12px;
  padding-top: 5px;
  padding-bottom: 5px;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  font-family: sans-serif, 'Poppins';
}

/* Hide the browser's default checkbox */
.checkbox-container input {
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

/* Create a custom checkbox */
.checkmark {
  position: absolute;
  top: 10px;
  left: 12px;
  height: 15px;
  width: 15px;
  border-radius: 50%;
  border: 1px solid black;
  z-index: 2;
}

.checkbox-back {
  position: absolute;
  width: 100%;
  height: 100%;
  left: 0%;
  top: 2px;
  border-radius: 16px;
  z-index: 0;
}

.checkbox-container input:checked ~ div > .checkbox-back {
  background-color: #f8babc;
}

/* On mouse-over, add a grey background color */
.checkbox-container input:checked + div {
  font-weight: 600;
  height: 100%;
  width: 100%;
}

/* When the checkbox is checked, add a blue background */
.checkbox-container input:checked ~ div > .checkmark {
  background-color: #ea2127;
  border: none;
}

/* Create the checkmark/indicator (hidden when not checked) */
.checkmark:after {
  content: '';
  position: absolute;
  display: none;
}

/* Show the checkmark when checked */
.checkbox-container input:checked ~ div > .checkmark::after {
  display: block;
}

.checkmark-label {
  position: relative;
  z-index: 1;
  top: 2px;
}

.checkbox-container input:checked ~ .checkbox-container {
  font-weight: 600;
  font-size: 14px;
  border-radius: 16px;
}

/* Style the checkmark/indicator */
.checkbox-container .checkmark:after {
  left: 4.75px;
  top: 1.45px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 2.5px 2.5px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}

@media only screen and (max-width: 475px) {
  .checkmark {
    position: absolute;
    top: 8px;
    left: 12px;
    height: 15px;
    width: 15px;
    border-radius: 50%;
    border: 1px solid black;
    z-index: 2;
  }
  .checkbox-container input:checked ~ .checkbox-container {
    font-weight: 600;
    font-size: 12px;
    border-radius: 16px;
  }
}
</style>
