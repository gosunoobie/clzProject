<template>
  <div class="mt-5 text-center verifying-div" v-if="verifyingTxn">
    <div class="mt-8 verifying-card">
      <p class="text-sm sm:text-base xl:text-xl">Verifying transaction....</p>
      <p>Please don't close the tab yet.</p>
      <p><n-spin size="small" /></p>
    </div>
  </div>
  <div v-else class="pt-8 sm:pt-10 main-div">
    <!-- <h2>Thanks for trusting us!</h2> -->
    <NCard class="txn-info" v-if="txnInfo">
      <n-alert title="Successfully Verified Payment" type="success">
        <!-- <CustomButton 
          v-if="domesticTicketList.length > 0 || activityTicketList.length>0"
          label="Download Reciept"
          color="green"
          @click="goToInvoiceUrl"
          href = '/'
        >
          <template v-slot:leftIcon>
            <Icon color="white" size="20">
              <Newspaper />
            </Icon>
          </template>
        </CustomButton> -->

        <a
          :href="txnInfo.invoiceUrl"
          class="flex items-center gap-2 p-2 text-sm font-semibold text-white bg-green-700 rounded-md cursor-pointer w-fit"
          target="_blank"
          v-if="domesticTicketList.length > 0 || activityTicketList.length > 0"
        >
          <Newspaper class="w-5" />
          <p>Download Reciept</p>
        </a>
      </n-alert>

      <NDivider />
      <NSpace class="mt-3" justify="space-between">
        <NText> Transaction ID</NText>
        <NText> {{ txnInfo.txnId }}</NText>
      </NSpace>
      <NSpace class="mt-3" justify="space-between">
        <NText> Transaction Date</NText>
        <NText> {{ txnInfo.dateCreated }}</NText>
      </NSpace>
      <NSpace class="mt-3" justify="space-between">
        <NText> Payment Method</NText>
        <NText> {{ txnInfo.paymentMethodName }}</NText>
      </NSpace>
      <NSpace class="mt-3" justify="space-between">
        <NText> Status</NText>
        <NText> {{ txnInfo.status }}</NText>
      </NSpace>
      <NSpace class="mt-3" justify="space-between">
        <NText> Paid Amount</NText>
        <NText> $ 1293.64</NText>
      </NSpace>
      <NDivider />

      <div class="mt-3 text-center" v-if="generatingTicket">
        <n-spin size="large" type="success" />
        <NH3>Generating ticket .....</NH3>
      </div>
      <n-alert v-if="isPlasmaError" title="Error Fetching Ticket" type="error">
        Error Occurred When fetching Ticket. Please contact our customer support. Rest Assured your
        payment is successful.
      </n-alert>

      <div v-if="domesticTicketList.length > 0">
        <NH3>Flight Tickets : </NH3>

        <NSpace>
          <div class="mt-4" v-for="ticket in domesticTicketList">
            <!-- <CustomButton
              v-if="domesticTicketList.length > 0"
              :label="
                'Download Ticket : ' + ticket.firstName + ' ' + ticket.lastName
              "
              color="#5560c3"
              @click="() => ticketDownload(ticket.ticketUrl)"
            >
              <template v-slot:leftIcon>
                <Icon color="white" size="20">
                  <Ticket />
                </Icon>
              </template>
            </CustomButton> -->
            <a
              :href="ticket.ticketUrl"
              class="flex items-center gap-2 px-3 py-2 text-sm font-semibold text-white bg-[#5560c3] rounded-[5px] cursor-pointer w-fit"
              target="_blank"
            >
              <Ticket class="w-5" />
              <p>Download Ticket : {{ ticket.firstName }} {{ ticket.lastName }}</p>
            </a>
          </div>
        </NSpace>
      </div>
      <div v-if="activityTicketList.length > 0">
        <NH3>Activity Tickets : </NH3>
        <NSpace>
          <div v-for="ticket in activityTicketList">
            <a
              :href="ticket.ticketUrl"
              class="flex items-center gap-2 px-3 py-2 text-sm font-semibold text-white bg-[#5560c3] rounded-[5px] cursor-pointer w-fit"
              target="_blank"
            >
              <Ticket class="w-5" />
              <p>Download Ticket</p>
            </a>
          </div>
        </NSpace>
      </div>
      <div v-if="agodaHotelTicketList.length > 0">
        <div class="my-4">
          <h3 class="font-bold text-lg">Hotel Tickets :</h3>
          <p>Your hotel booking is succesfull. You can download ticket from below:</p>
        </div>
        <NSpace>
          <div v-for="ticket in agodaHotelTicketList">
            <a
              :href="ticket.ticketUrl"
              class="flex items-center gap-2 px-3 py-2 text-sm font-semibold text-white bg-[#5560c3] rounded-[5px] cursor-pointer w-fit"
              target="_blank"
            >
              <Ticket class="w-5" />
              <p>Download Ticket</p>
            </a>
          </div>
        </NSpace>
      </div>
      <CustomButton
        label="Ticket History"
        color="#ea2127"
        extra-class="justify-center w-full mt-4"
        @click="
          () => {
            $router.push(
              `/ticket-history/?isActivity=${
                activityTicketList.length > 0
              }&isDomesticFlight=${domesticTicketList.length > 0}&isHotel=${
                agodaHotelTicketList.length > 0
              }`
            )
          }
        "
      >
        <template v-slot:leftIcon>
          <Icon color="white" size="20">
            <History />
          </Icon>
        </template>
      </CustomButton>
    </NCard>
  </div>
</template>

<script setup lang="ts">
import { Ref, onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { TransactionType } from '../../models/Account.interface'
import {
  DomesticFlightTicketType,
  ActivityTicketType,
  AgodaTicketType
} from '../../models/Flight.interface'
import { getAPI, postAPI } from '../../api/index'
import CustomButton from '../../components/CustomElements/CustomButton.vue'

import { NCard, NText, NSpace, NAlert, NDivider, NSpin, NH3 } from 'naive-ui'
import { Newspaper, Ticket } from '@vicons/ionicons5'
import { Icon } from '@vicons/utils'
import { History } from '@vicons/fa'
import { usePaymentStore } from '../../stores/paymentStore'

const $route: any = useRoute()
const $router: any = useRouter()
const verifyingTxn = ref(false)
const txnInfo: Ref<TransactionType | null> = ref(null)
const domesticTicketList: Ref<DomesticFlightTicketType[]> = ref([])
const activityTicketList: Ref<ActivityTicketType[]> = ref([])
const agodaHotelTicketList: Ref<AgodaTicketType[]> = ref([])
const generatingTicket = ref(false)
const isPlasmaError = ref(false)
const paymentStore = usePaymentStore()
let esewaId = import.meta.env.VITE_ESEWA_ID

onMounted(() => {
  const provider: 'esewa' | 'khalti' = $route.params.provider
  if (['esewa', 'khalti'].includes(provider)) {
    // alert("invalid provider",providerType);
    if (provider === 'esewa') {
      let payload = {
        amt: parseInt($route?.query?.amt),
        rid: $route?.query?.refId,
        pid: $route?.query?.oid,
        scd: esewaId
      }
      verifyEsewaCheck(payload)
    }
    if (provider === 'khalti') {
      let payload = {
        pidx: $route?.query?.pidx,
        txn_id: $route?.query?.purchase_order_id
      }
      verifyKhaltiCheck(payload)
    }
    return
  }

  let payload = {
    txn_id: $route?.query?.purchase_order_id
  }
  verifyHBLCheck(payload)
})

const goToInvoiceUrl = () => {
  if (txnInfo.value) {
    window.location.href = txnInfo.value.invoiceUrl
  }
}
const ticketDownload = (ticketurl: string) => {
  window.location.href = ticketurl
}

const verifyKhaltiCheck = async (payload: any) => {
  try {
    verifyingTxn.value = true
    const res = await postAPI('billing/khalti/verify_payment', payload)
    verifyingTxn.value = false
    txnInfo.value = res.data
    getTicketList(res.data.txnId)
  } catch (e) {
    verifyingTxn.value = false
    $router.push({
      name: 'PaymentError'
    })
  }
}

const verifyEsewaCheck = async (payload: any) => {
  try {
    verifyingTxn.value = true
    const res = await postAPI('billing/esewa-web-callback', payload)
    verifyingTxn.value = false
    txnInfo.value = res.data
    getTicketList(res.data.txnId)
  } catch (error) {
    verifyingTxn.value = false
    $router.push({
      name: 'PaymentError'
    })
  }
}
const verifyHBLCheck = async (payload: any) => {
  try {
    verifyingTxn.value = true
    const txn_id = $route?.query?.orderNo
    const res = await getAPI(`billing/hbl-callback-verify`, `?orderNo=${txn_id}`)
    verifyingTxn.value = false
    txnInfo.value = res.data
    // getTicketList(res.data.txnId);
    getTicketList(txn_id)
  } catch (error) {
    verifyingTxn.value = false
    $router.push({
      name: 'PaymentError'
    })
  }
}

const getTicketList = async (txnId: any) => {
  generatingTicket.value = true

  try {
    generatingTicket.value = false
    const res: any = await getAPI(`billing/txn-ticket-list/${txnId}`)
    domesticTicketList.value = res.data.domesticTickets
    activityTicketList.value = res.data.activityTickets
    agodaHotelTicketList.value = res.data.hotelTickets
  } catch (error) {
    isPlasmaError.value = true
    verifyingTxn.value = false
    generatingTicket.value = false
  }
}
</script>

<style scoped>
.main-div {
  display: flex;
  justify-content: center;
}
.verifying-div {
  height: 100vh;
  background-color: rgba(141, 140, 140, 0.2);
  display: grid;
  overflow: hidden;
  place-items: center;
  text-align: center;
  z-index: 20;
  backdrop-filter: blur(4px);
  transition: 0.2s ease-in-out;
}
.verifying-card {
  display: flex;
  width: 250px;
  font-weight: bold;
  justify-content: center;
  align-items: center;
  background-color: white;
  flex-direction: column;
  gap: 10px;
  padding: 20px;
  border: 1px solid #e1e1e1;
  border-radius: 20px;
  box-shadow: 10px 10px 204px 45px rgba(0, 0, 0, 0.17);
  transition: 0.5s ease-in-out;
}
.txn-info {
  width: 60%;
}

@media only screen and (max-width: 794px) {
  .txn-info {
    width: 80%;
  }
}

@media only screen and (max-width: 600px) {
  .txn-info {
    width: 90%;
  }
}
</style>
