<script setup lang="ts">
import { NCard, NGi, NGrid, NInput, NSelect, useMessage, NText } from 'naive-ui'
import { ref } from 'vue'
import { postAPI } from '../../api/index'

import { useNewFlightStore } from '../../stores/newFlightStore'
import CustomButton from '../../components/CustomElements/CustomButton.vue'
const newFlightStore = useNewFlightStore()

const message = useMessage()

const onlyAllowNumber = (value: string) => !value || /^\d+$/.test(value)
const formValue = ref({
  name: '',
  address: '',
  panOrVatNum: null
})

const addBillingAddress = async (e: Event) => {
  e.preventDefault()
  if (formValue.value.address.trim().length < 1 || formValue.value.name.trim().length < 1) {
    message.error('Name and Address are required!')
    return
  }
  const res = await postAPI('billing/billing-address', formValue.value)
  newFlightStore.billingList.push(res.data)
  newFlightStore.selectedBillingAddress = res.data.id
  message.success('Successfully Added New Billing Address')
}
</script>

<template>
  <NCard class="mt-3 primary-border" title="Billing Detail (Optional) ">
    <n-text
      >Users are required to provide their billing address to continue their transaction process. If
      the user has no billing address in the list, then they are required to add a new billing
      address.</n-text
    >

    <div class="mt-10">
      <n-select
        v-model:value="newFlightStore.selectedBillingAddress"
        size="large"
        :options="newFlightStore.billingListOptions"
      />
      <div class="mt-3 text-center">
        <n-text class="text-gray">OR</n-text>
      </div>
      <form @submit="addBillingAddress" class="mt-4">
        <n-text>Users can add their billing address here. </n-text>
        <n-grid x-gap="10" cols="1 s:2 m:2 l:2" :y-gap="0" responsive="screen">
          <n-gi>
            <NInput
              type="text"
              v-model:value="formValue.name"
              size="large"
              class="mt-3"
              placeholder="Name"
              aria-required="true"
            />
          </n-gi>
          <n-gi>
            <NInput
              v-model:value="formValue.address"
              type="text"
              size="large"
              class="mt-3"
              placeholder="Address"
              aria-required="true"
            />
          </n-gi>
          <n-gi>
            <NInput
              v-model:value="formValue.panOrVatNum"
              maxlength="9"
              :allow-input="onlyAllowNumber"
              type="text"
              size="large"
              class="mt-3"
              placeholder="Pan / Vat (Optional)"
            />
          </n-gi>
          <n-gi>
            <CustomButton
              label="Add Billing Address"
              color="#ea2127"
              extraClass="mt-3 !p-2"
              size="lg"
              type="submit"
            />
          </n-gi>
        </n-grid>
      </form>
    </div>
  </NCard>
</template>

<style lang=""></style>
