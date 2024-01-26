<template>
  <button
    @click="customClickFunction"
    :class="`${
      props.extraClass
    } custom-btn flex gap-2 outline-none border-none px-3 py-2 xs:px-[6px] xs:py-[10px] rounded-[4px] font-['Poppins'] items-center text-sm font-semibold   ${
      props.size === 'lg' ? 'size-large' : ''
    }`"
    :style="customStyle"
    :disabled="props.disabled"
    :type="props.type"
  >
    <slot name="leftIcon"></slot>
    {{ props.label }}
    <slot name="rightIcon"></slot>
  </button>
</template>
<script setup lang="ts">
import { PropType, ref } from 'vue'

type ButtonType = 'button' | 'submit' | 'reset'
const props = defineProps({
  label: {
    type: String,
    required: true
  },
  size: {
    type: String,
    default: 'md'
  },
  type: {
    type: String as PropType<ButtonType>,
    default: 'button'
  },
  disabled: {
    type: Boolean,
    default: false
  },
  color: {
    type: String,
    default: '#f3f3f3'
  },
  onClickFunction: {
    type: Function,
    default: null
  },
  textColor: {
    type: String,
    default: 'white'
  },
  extraClass: {
    type: String,
    default: ''
  }
})

const customClickFunction = () => {
  if (props.onClickFunction) {
    props.onClickFunction()
  }
}

let customStyle = ref(
  `background-color:${props.color} !important;color:${props.textColor} !important`
)
</script>
<style scoped>
.custom-btn {
}

.size-large {
  padding: 10px 8px;
}

.custom-btn:hover {
  opacity: 0.7;
  transition: ease-in;
}

.custom-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
