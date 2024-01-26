<template>
  <div class="font-['Poppins']">
    <n-modal v-model:show="showExpireModal">
      <n-card
        style="width: 600px"
        title="Reservation Time Expired !"
        :bordered="false"
        size="huge"
        role="dialog"
        aria-modal="true"
      >
        <p><n-text>You will be redirected to search</n-text></p>
        <n-countdown
          v-if="newFlightStore.flightDetail?.flightInfo[0].duration"
          :duration="5000"
          :active="true"
          :on-finish="() => $router.push('/flights')"
        />
      </n-card>
    </n-modal>
    <n-modal v-model:show="newFlightStore.showPaymentModal">
      <n-card
        class="w-[360px] xs:w-[450px] sm:w-[500px] md:w-[550px]"
        :bordered="false"
        size="huge"
        role="dialog"
        aria-modal="true"
      >
        <NH3>Payment Mode</NH3>
        <NDivider />

        <form ref="esewaFormRef" :action="`${esewaAPIurl}/epay/main`" method="POST">
          <input
            :value="newFlightStore.flightDetail?.flightInfo[0].totalCommissionedCost"
            name="tAmt"
            type="hidden"
          />
          <input
            :value="newFlightStore.flightDetail?.flightInfo[0].totalCommissionedCost"
            name="amt"
            type="hidden"
          />
          <!--
          <input value="10" name="tAmt" type="hidden" />
          <input value="10" name="amt" type="hidden" />
-->
          <input :value="0" name="txAmt" type="hidden" />
          <input :value="0" name="psc" type="hidden" />
          <input :value="0" name="pdc" type="hidden" />
          <input :value="esewaId" name="scd" type="hidden" />
          <input :value="newFlightStore.paymentTxnId" name="pid" type="hidden" />
          <input :value="`${esewaSuccessUrl}/payment-success/esewa/`" type="hidden" name="su" />
          <input :value="`${esewaSuccessUrl}/payment-error/`" type="hidden" name="fu" />
        </form>
        <article
          class="logo-div flex flex-wrap w-full gap-2"
          v-if="
            (jwtStore.UserDetail.phoneVerified && jwtStore.UserDetail.nationality === 'Nepal') ||
            (jwtStore.UserDetail.nationality !== 'Nepal' &&
              jwtStore.UserDetail.nationality !== null &&
              jwtStore.UserDetail.nationality !== '')
          "
        >
          <div
            @click="handleEsewaPayment"
            v-if="newFlightStore.flightDetail.flightInfo[0].Currency === 'NPR'"
            class="bg-cover bg-no-repeat border-[#e8e8e8] rounded-md border-[1px] bg-center w-[48%] xs:w-[32%] gap-3 h-[7rem] cursor-pointer"
            :style="`background-image: url(${EsewaBox})`"
          ></div>
          <div
            @click="handleKhaltiPayment"
            v-if="newFlightStore.flightDetail.flightInfo[0].Currency === 'NPR'"
            class="bg-cover bg-no-repeat border-[#e8e8e8] rounded-md border-[1px] bg-center w-[48%] xs:w-[32%] gap-3 h-[7rem] cursor-pointer"
            :style="`background-image: url(${KhaltiBox})`"
          ></div>
          <div
            @click="handleHBLPayment"
            class="bg-cover bg-no-repeat border-[#e8e8e8] rounded-md border-[1px] bg-center w-[48%] xs:w-[32%] gap-3 h-[7rem] cursor-pointer"
            :style="`background-image: url(${HBLBox})`"
          ></div>
          <!--
          <div
            @click="handleNabilPayment"
            class="bg-cover rounded-md border-[1px] border-[#E8E8E8] bg-no-repeat bg-center w-[32%] gap-3 h-[7rem] cursor-pointer"
            :style="`background-image: url(${NabilBox})`"
          ></div>
-->
        </article>
        <div v-else>
          <h2 class="text-sm sm:text-base md:text-lg">Please verify your phone number</h2>
        </div>
      </n-card>
    </n-modal>
    <div class="flex-col search-main-div"></div>
    <div
      class="skeleton-loading-div flex-col-reverse px-1 items-center lg:items-start xs:px-5 lg:flex-row w-full lg:w-[90%]"
      v-if="newFlightStore.isFlightsLoading"
    >
      <!-- <h3>Loading ..</h3> -->
      <div class="skeleton-left w-full lg:w-[68%]">
        <FlightSkeleton />
        <n-card class="mt-3 primary-border">
          <n-skeleton class="w-1/2 h-7" />
          <NDivider />
          <n-skeleton class="mt-3 h-7" />
          <NDivider />
        </n-card>
        <n-card class="mt-3 primary-border">
          <n-skeleton class="w-1/2 h-7" />
          <NDivider />
          <n-skeleton class="mt-3 h-7" />
          <NDivider />
        </n-card>
      </div>
      <n-card class="skeleton-right mt-0 lg:mt-4 w-[340px] lg:w-[28%] primary-border">
        <n-skeleton class="w-1/2 h-7" />
        <NDivider />
        <n-skeleton class="mt-3 h-7" text :repeat="5" />
      </n-card>
    </div>

    <section
      class="main-flight-div p-0 lg:p-4 flex-col-reverse lg:flex-row w-[95%] lg:w-[97.5%] xl:w-[90%]"
    >
      <section class="left-side-detail w-full lg:w-[70%]">
        <n-tag v-if="newFlightStore.flightDetail?.flightInfo[0].duration" :bordered="false">
          Book within
          <n-countdown
            :duration="newFlightStore.flightDetail.flightInfo[0].duration"
            :active="true"
            :on-finish="() => reserveExpire()"
          />
        </n-tag>
        <n-form v-if="newFlightStore.flightDetail">
          <FlightComponent
            v-for="flight in newFlightStore.flightDetail?.flightInfo"
            :data="flight"
            :show-button="false"
            :show-color="false"
            :key="flight.FlightId"
          />
          <!-- {{ newFlightStore.flightDetail }} -->
          <n-card class="mt-3 primary-border" title="Contact Detail *">
            <n-grid x-gap="10" cols="1 s:2 m:2 l:2" :y-gap="0" responsive="screen">
              <n-gi>
                <n-input
                  class="mt-4"
                  type="text"
                  size="large"
                  placeholder="Full Name"
                  v-model:value="createBookingPayload.contactName"
                />
              </n-gi>
              <n-gi>
                <n-input
                  show-count
                  class="mt-4"
                  :maxlength="10"
                  :allow-input="onlyAllowNumber"
                  type="text"
                  size="large"
                  placeholder="Mobile Number"
                  v-model:value="createBookingPayload.contactMobile"
                />
              </n-gi>
              <n-gi>
                <n-input
                  class="mt-4"
                  type="text"
                  size="large"
                  placeholder="Email Address"
                  v-model:value="createBookingPayload.contactEmail"
                />
              </n-gi>
            </n-grid>
            <n-checkbox
              class="mt-4"
              v-model:checked="am_passenger"
              label="I am a passenger on this flight"
            />
          </n-card>

          <BillingAddress />

          <n-card class="mt-3 primary-border" v-if="newFlightStore.passengerForm">
            <NH3>Adult Passenger *</NH3>
            <div
              v-for="(_, index) in newFlightStore.passengerForm.adult"
              :key="index"
              class="mt-2"
              title="Contact Detail"
            >
              <n-grid class="!gap-3 !grid !grid-cols-1 md:!grid-cols-5 !w-full">
                <n-gi :span="1">
                  <n-select
                    size="large"
                    v-model:value="newFlightStore.passengerForm['adult'][index]['passenger_title']"
                    placeholder="Passenger Title "
                    :options="titleOption as SelectMixedOption[]"
                  />
                </n-gi>
                <n-gi :span="2">
                  <n-input
                    type="text"
                    size="large"
                    placeholder="First Name"
                    name="first_name"
                    v-model:value="newFlightStore.passengerForm['adult'][index]['first_name']"
                  />
                </n-gi>
                <n-gi :span="2">
                  <n-input
                    type="text"
                    size="large"
                    placeholder="Last Name"
                    v-model:value="newFlightStore.passengerForm['adult'][index]['last_name']"
                  />
                </n-gi>
              </n-grid>
            </div>
            <n-divider />
            <NH3 v-if="newFlightStore.passengerForm.child.length" class="mt-2">
              Child Passenger *</NH3
            >

            <div
              v-for="(_, index) in newFlightStore.passengerForm.child"
              :key="index"
              class="mt-3"
              title="Contact Detail"
            >
              <n-grid x-gap="10" :cols="5">
                <n-gi :span="1">
                  <n-select
                    size="large"
                    v-model:value="newFlightStore.passengerForm['child'][index]['passenger_title']"
                    placeholder="Passenger Title"
                    :options="titleOption as SelectMixedOption[]"
                  />
                </n-gi>
                <n-gi :span="2">
                  <n-input
                    type="text"
                    size="large"
                    placeholder="First Name"
                    name="first_name"
                    v-model:value="newFlightStore.passengerForm['child'][index]['first_name']"
                  />
                </n-gi>
                <n-gi :span="2">
                  <n-input
                    type="text"
                    size="large"
                    placeholder="Last Name"
                    v-model:value="newFlightStore.passengerForm['child'][index]['last_name']"
                  />
                </n-gi>
              </n-grid>
            </div>
          </n-card>

          <n-card v-if="newFlightStore.paymentTxnId" class="mt-2 primary-border">
            <CustomButton
              label="Start Payment"
              color="#ea2127"
              extraClass="mt-3 w-full justify-center"
              size="lg"
              @click="newFlightStore.showPaymentModal = true"
            >
              <template v-slot:leftIcon>
                <Icon color="white" size="20">
                  <Ticket />
                </Icon>
              </template>
            </CustomButton>
          </n-card>
          <n-card v-else class="mt-3 primary-border">
            <div>
              <n-checkbox
                class="mt-4"
                v-model:checked="accept_toc"
                label="Accept Our Agree Terms & condition"
              />
            </div>

            <CustomButton
              v-if="newFlightStore.creatingBooking"
              label="Creating Booking ..."
              color="#ea2127"
              extraClass="mt-3 w-full justify-center"
              size="lg"
            >
              <template v-slot:leftIcon>
                <Icon color="white">
                  <AirplaneSharp />
                </Icon>
              </template>
            </CustomButton>

            <CustomButton
              v-else
              label="Create Booking "
              :onClickFunction="createBooking"
              color="#ea2127"
              size="lg"
              icon-size="20"
              extra-class="justify-center w-full mt-3"
            >
              <template v-slot:leftIcon>
                <Icon color="white">
                  <AirplaneSharp />
                </Icon>
              </template>
            </CustomButton>
          </n-card>
        </n-form>
      </section>
      <aside class="pricing-detail mt-[22px] w-full lg:w-[30%]">
        <div
          class="min-w-[300px] w-full mx-auto lg:ml-auto max-w-[340px]"
          v-if="newFlightStore.flightDetail"
        >
          <div class="price-card">
            <n-card
              class="mb-1 lg:mb-10 primary-border"
              :key="priceInfo.FlightId"
              v-for="priceInfo in newFlightStore.flightDetail.flightInfo"
            >
              <NH3 type="error" strong class="text-primary-500">Price Detail</NH3>
              <n-divider />
              <NSpace v-if="priceInfo.Adult !== '0'" justify="space-between">
                <NText> Adult Fare</NText>
                <NText>
                  {{
                    new Intl.NumberFormat('en-IN', {
                      maximumSignificantDigits: 3
                    }).format(priceInfo.AdultFare)
                  }}
                  X {{ priceInfo.Adult }}</NText
                >
              </NSpace>
              <NSpace v-if="priceInfo.Child !== '0'" class="mt-3" justify="space-between">
                <NText> Child Fare</NText>
                <NText>
                  {{
                    new Intl.NumberFormat('en-IN', {
                      maximumSignificantDigits: 3
                    }).format(priceInfo.childFare)
                  }}
                  X {{ priceInfo.Child }}</NText
                >
              </NSpace>

              <NSpace class="mt-3" justify="space-between">
                <NText> Fuel Surchange</NText>
                <NText>
                  {{
                    new Intl.NumberFormat('en-IN', {
                      maximumSignificantDigits: 3
                    }).format(priceInfo.FuelSurcharge)
                  }}
                  X
                  {{ priceInfo.TotalPeople }}</NText
                >
              </NSpace>
              <NSpace class="mt-3" justify="space-between">
                <NText> Tax</NText>
                <NText>
                  {{
                    new Intl.NumberFormat('en-IN', {
                      maximumSignificantDigits: 3
                    }).format(priceInfo.Tax)
                  }}
                  X {{ priceInfo.TotalPeople }}</NText
                >
              </NSpace>
              <NSpace class="mt-3" justify="space-between">
                <NText> Discount</NText>
                <NText> {{ priceInfo.DiscountAmount }}</NText>
              </NSpace>
              <n-divider />
              <NSpace class="mt-3" justify="space-between">
                <NText :strong="true"> Total Amount</NText>
                <NText :strong="true">
                  NPR

                  {{
                    new Intl.NumberFormat('en-IN', {
                      maximumSignificantDigits: 3
                    }).format(priceInfo.totalCommissionedCost)
                  }}
                </NText>
              </NSpace>
            </n-card>
            <n-card v-if="newFlightStore.flightDetail.flightInfo.length > 1" class="primary-border">
              <NSpace class="mt-3" justify="space-between">
                <NText :strong="true"> Grand Total Amount</NText>
                <NText :strong="true">
                  NPR

                  {{
                    new Intl.NumberFormat('en-IN', {
                      maximumSignificantDigits: 3
                    }).format(newFlightStore.flightDetail.totalCost)
                  }}
                </NText>
              </NSpace>
            </n-card>
          </div>
        </div>
      </aside>
    </section>
  </div>
</template>
<script setup lang="ts">
import { onMounted, onUnmounted, ref, watch, type Ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import FlightComponent from '../../components/domesticFlights/FlightComponent.vue'
import { useFlightStore } from '../../stores/newFlightStore'
import { useNewFlightStore } from '../../stores/newFlightStore'
import HBLBox from '../../assets/payments/hblLogo.png'
import NabilBox from '../../assets/payments/nabilLogo.png'

import CustomButton from '../../components/CustomElements/CustomButton.vue'
import { notify } from '@kyvg/vue3-notification'
import {
  NCard,
  NCheckbox,
  NCountdown,
  NDivider,
  NForm,
  NGi,
  NGrid,
  NH3,
  NInput,
  NModal,
  NSelect,
  NSkeleton,
  NSpace,
  NText,
  NTag
} from 'naive-ui'
import BillingAddress from '../../components/domesticFlights/BillingAddress.vue'
import FlightSkeleton from '../../components/domesticFlights/flightSkeleton.vue'
import { BookingPayload, FlightBookingPayload } from '../../models/Flight.interface'
import { SelectOptionType } from '../../models/Flight.interface'
import { useJwtStore } from '../../stores/jwt'
import { postAPI, getAPI } from '../../api'
import { Icon } from '@vicons/utils'
import { AirplaneSharp, Ticket } from '@vicons/ionicons5'
import { SelectMixedOption } from 'naive-ui/es/select/src/interface'
import KhaltiBox from '../../assets/payments/KhaltiBox.png'

import EsewaBox from '../../assets/payments/EsewaBox.png'
const $route: any = useRoute()
const $router: any = useRouter()
const jwtStore: any = useJwtStore()
const showExpireModal = ref(false)
const am_passenger = ref(false)
const accept_toc = ref(false)
import { usePaymentStore } from '../../stores/paymentStore'
// const flightStore = useFlightStore();
const newFlightStore = useNewFlightStore()
const esewaFormRef = ref<HTMLFormElement | null>(null)
let esewaSuccessUrl = import.meta.env.VITE_ESEWA_SUCCESS_URL
let esewaAPIurl = import.meta.env.VITE_ESEWA_API_URL
let esewaId = import.meta.env.VITE_ESEWA_ID

const paymentStore = usePaymentStore()
//allow only number that starts with 9
const onlyAllowNumber = (value: string): boolean => !value || /^9\d*$/.test(value)

const titleOption: SelectOptionType[] = [
  {
    label: 'Mr',
    value: 'Mr'
  },
  {
    label: 'Ms',
    value: 'Ms'
  }
]

console.log('client id', esewaId)

onMounted(() => {
  let reserveId = $route.params.id
  newFlightStore.getFlightDetail(reserveId)
  newFlightStore.getBillingAddress()
})

onUnmounted(() => {
  // console.log("leaving page");
  newFlightStore.paymentTxnId = null
  newFlightStore.showPaymentModal = false
})

watch(
  () => newFlightStore.flightDetail?.flightInfo,
  () => {
    let duration = newFlightStore.flightDetail?.flightInfo[0].duration ?? 0
    if (duration < 1) {
      // console.log("date expired");
      $router.push('/flights')
    }
  }
)

watch(am_passenger, () => {
  if (am_passenger.value) {
    newFlightStore.passengerForm.adult[0].first_name = userDetail?.firstName
    newFlightStore.passengerForm.adult[0].last_name = userDetail?.lastName
    newFlightStore.passengerForm.adult[0].passenger_title = 'Mr'
  } else {
    newFlightStore.passengerForm.adult[0].first_name = ''
    newFlightStore.passengerForm.adult[0].last_name = ''
    newFlightStore.passengerForm.adult[0].passenger_title = ''
  }
})

const userDetail = jwtStore?.UserDetail

function hasNullOrEmptyValue(obj: any) {
  if (Array.isArray(obj)) {
    for (let i = 0; i < obj.length; i++) {
      if (hasNullOrEmptyValue(obj[i])) {
        return true
      }
    }
  } else if (typeof obj === 'object' && obj !== null) {
    for (let key in obj) {
      if (hasNullOrEmptyValue(obj[key])) {
        return true
      }
    }
  } else if (obj === null || obj === '') {
    return true
  }
  return false
}

const createBookingPayload: Ref<FlightBookingPayload> = ref({
  contactName: `${userDetail?.firstName} ${userDetail?.lastName}`,
  contactEmail: userDetail?.email,
  contactMobile: userDetail?.mobileNumber,
  bookings: []
})

const createBooking = () => {
  if (accept_toc.value === false) {
    notify({
      text: 'Please Accept Our Terms & Conditions',
      type: 'error',
      duration: 4000
    })
    return
  }

  let bookingInfo: BookingPayload
  if (newFlightStore?.flightDetail?.flightInfo) {
    createBookingPayload.value.bookings = []
    for (let li of newFlightStore.flightDetail.flightInfo) {
      bookingInfo = {
        flight_id: li.FlightId,
        passenger_details: []
      }
      for (let i in newFlightStore.passengerForm) {
        for (let val = 0; val < newFlightStore.passengerForm[i].length; val++) {
          newFlightStore.passengerForm[i][val]['gender'] =
            newFlightStore.passengerForm[i][val]['passenger_title'] === 'Mr' ? 'M' : 'F'
        }
        bookingInfo.passenger_details.push(...newFlightStore.passengerForm[i])
      }
      createBookingPayload.value.bookings.push(bookingInfo)
    }
  }

  if (hasNullOrEmptyValue(createBookingPayload.value)) {
    notify({
      title: 'Missing Fields',
      text: 'Please Fill All The Fields',
      type: 'error',
      duration: 4000
    })
  } else {
    // hit create booking api
    newFlightStore.createBooking(createBookingPayload.value)
  }

  // createBookingPayload.value.bookings=[]
}

const reserveExpire = () => {
  showExpireModal.value = true
}

//const handleHBLPayment = async () => {
//  await getAPI(
//    "billing/hbl-pre-payment",
//    `${newFlightStore.paymentTxnId}/android`
//  ).then((response) => {
//    window.location.href = response.data.paymentPageUrl;
//  });
//};

const handleHBLPayment = async () => {
  try {
    newFlightStore.loadingScreen = true
    const currencyType = newFlightStore.flightDetail.flightInfo[0].Currency

    await paymentStore.initiateHblPayment(newFlightStore.paymentTxnId, currencyType).then(() => {
      newFlightStore.loadingScreen = false
    })
  } catch (err) {
    newFlightStore.loadingScreen = false
  }
}
const handleNabilPayment = async () => {
  newFlightStore.loadingScreen = true
  await paymentStore.getNabilPayment(bookingResponse).then(() => {
    newFlightStore.loadingScreen = false
  })
}
const handleEsewaPayment = () => {
  try {
    newFlightStore.loadingScreen = true
    if (esewaFormRef.value) {
      newFlightStore.loadingScreen = false
      esewaFormRef.value?.submit()
    }
  } catch (err) {
    newFlightStore.loadingScreen = false
  }
}
const handleKhaltiPayment = async () => {
  try {
    newFlightStore.loadingScreen = true
    await postAPI('billing/khalti/inititiate_payment', {
      txn_id: newFlightStore.paymentTxnId
    }).then((res) => {
      newFlightStore.loadingScreen = false

      window.location.href = res.data.paymentUrl
    })
  } catch (err) {
    newFlightStore.loadingScreen = false
  }
}

const handleBackButton = () => {
  window.location.reload()
}

onMounted(() => {
  // window.addEventListener("popstate", handleBackButton);
})
</script>
<style lang="css" scoped>
.main-flight-div {
  display: flex;
  gap: 1rem;
  margin: auto;
  justify-content: center;
  margin-top: -50vh;
}

.left-side-detail {
  /* background-color: red; */
}

.pricing-detail {
  /* background-color: blue; */
  padding: 1rem;
}

.price-card {
  position: sticky;
  top: 7rem;
}

.search-main-div {
  width: 100%;
  height: 50vh;
  background-repeat: no-repeat;
  background-size: cover;
  background-image: url('../../assets/layout/image/flight_backdrop.png');
  align-items: center;
  justify-content: center;
}

img:hover {
  background-color: #f4f2f2;
  cursor: pointer;
}

.skeleton-loading-div {
  display: flex;
  margin: auto;
  gap: 1rem;
  justify-content: space-between;
  margin-top: -47.5vh;
}

@media only screen and (max-width: 800px) {
  :deep(.n-card__content) {
    padding: 16px 12px !important;
  }
}
/*
@media only screen and (max-width: 794px) {
  .main-flight-div {
    width: 95%;
    flex-direction: column-reverse;
    align-items: center;
  }

  .pricing-detail {
    width: 90%;
  }

  .left-side-detail {
    width: 90%;
  }
} */
</style>
