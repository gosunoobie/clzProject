<template>
  <aside class="my-2 relative w-full" :class="`${rootClass}`">
    <div class="relative w-full">
      <div class="flex w-full">
        <input
          :id="props.label"
          v-bind="$attrs"
          aria-describedby="outlined_success_help"
          :class="`block px-2.5 pb-2.5 pt-4  !w-full text-base text-gray-[#b1b1b1] bg-transparent rounded-[5px] border-[1px] appearance-none focus:border-[#b1b1b1] border-[#b1b1b1] focus:outline-none focus:ring-0 peer ${
            errorMessage && '!border-[#d21e23]'
          } `"
          placeholder=""
          v-model="syncValue"
          autocomplete="off"
        />

        <label
          :for="props.label"
          :class="`absolute text-sm font-medium bg-white text-black duration-300 transform -translate-y-4 scale-[0.9] top-2 z-10 left-2  px-1 peer-focus:px-1 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-[0.9] peer-focus:-translate-y-4  ${
            errorMessage && '!text-[#d21e23] jiggle'
          } ${labelClass}`"
          >{{ props.label }} <span class="text-primary-400">{{ props.extraLabel }}</span></label
        >
        <ErrorRound
          v-if="errorMessage"
          color="#d21e23"
          class="w-6 absolute top-1/2 translate-y-[-50%] right-2"
        />
      </div>
    </div>
    <p
      id="outlined_error"
      :class="`text-[11.25px] font-normal start-3  absolute text-[#d21e23] duration-[400ms]  ease-in-out transition-all ${
        errorMessage ? 'error' : 'success'
      } `"
    >
      {{ errorMessage }}
    </p>
  </aside>
</template>
<script lang="ts"></script>
<script setup lang="ts">
import { defineEmits, onMounted, defineProps, computed } from 'vue'
import { useField } from 'vee-validate'
import { ErrorRound } from '@vicons/material'
const emit = defineEmits(['update:modelValue'])
const props = defineProps({
  modelValue: {
    type: [String, Number, Object],
    required: true
  },
  validator: {
    type: [String, Object],
    required: true
  },
  label: {
    type: String,
    required: true
  },
  extraLabel: {
    type: String,
    required: false
  },
  rootClass: {
    type: String,
    required: false
  },
  labelClass: {
    type: String,
    required: false
  }
})
const syncValue = computed({
  get() {
    return value.value
  },
  set(data) {
    value.value = data
    emit('update:modelValue', data)
  }
})

const { value, errorMessage } = useField(props.label, props.validator)

onMounted(() => {
  if (props.modelValue) value.value = props.modelValue
})
</script>

<style scoped>
.error {
  margin-top: 0.2em;
  opacity: 1;
}
.success {
  margin-top: -0.3em;
  opacity: 0;
}
.jiggle {
  animation: 350ms horizontal-shaking forwards ease-in;

  animation-delay: 100ms;
}

@keyframes horizontal-shaking {
  0% {
    left: 0px;
    margin-left: 8px;
  }
  10% {
    left: -1.5px;
    margin-left: 8px;
  }
  25% {
    left: 1.5px;
    margin-left: 8px;
  }
  40% {
    left: -1.5px;
    margin-left: 8px;
  }
  55% {
    left: 1.5px;
    margin-left: 8px;
  }
  70% {
    left: -1.5px;
    margin-left: 8px;
  }
  85% {
    left: 1.5px;
    margin-left: 8px;
  }
  100% {
    left: 0px;
    margin-left: 8px;
  }
}
</style>
