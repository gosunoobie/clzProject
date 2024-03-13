<template>
  <section
    class="font-['Poppins'] fixed top-0 w-full max-h-[100vh] h-[100vh] bg-[rgba(0,0,0,0.4)] z-[999] flex justify-center items-center overflow-y-scroll"
  >
    <!-- <pre class="w-24 h-24 bg-red-800">{{ model }}</pre> -->

    <form
      @keydown.enter="loginUser"
      @submit.prevent="loginUser"
      v-if="!toggle"
      class="flex mx-2 items-center py-2 justify-center w-[380px] xs:w-[400px] sm:w-[475px] bg-white flex-col px-4 xs:px-6 sm:px-8 rounded-md"
    >
      <header
        class="flex items-center justify-between w-full py-3 xs:py-4 sm:py-5 border-b-[1px] border-[#b1b1b1]"
      >
        <h3 class="text-base font-bold xs:text-lg sm:text-xl">Sign in / Register</h3>
        <button @click="emit('closeModal')" type="button">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="w-[14px] xs:w-[16px] h-[14px] xs:h-[16px]"
            viewBox="0 0 20 20"
            fill="none"
          >
            <path
              d="M2.98203 0.490874L10 7.50855L16.9816 0.527235C17.1358 0.363097 17.3216 0.231792 17.5278 0.141194C17.734 0.0505961 17.9564 0.00257135 18.1816 0C18.6638 0 19.1262 0.191544 19.4672 0.532495C19.8082 0.873445 19.9997 1.33587 19.9997 1.81805C20.0039 2.04095 19.9626 2.26236 19.8782 2.4687C19.7938 2.67504 19.6681 2.86195 19.5088 3.01797L12.4363 9.99928L19.5088 17.0715C19.8085 17.3646 19.9842 17.7616 19.9997 18.1805C19.9997 18.6627 19.8082 19.1251 19.4672 19.4661C19.1262 19.807 18.6638 19.9986 18.1816 19.9986C17.9499 20.0082 17.7187 19.9695 17.5027 19.885C17.2868 19.8005 17.0907 19.672 16.9271 19.5077L10 12.49L3.00021 19.4895C2.84659 19.6482 2.66306 19.7748 2.46023 19.8622C2.25739 19.9496 2.03926 19.9959 1.81842 19.9986C1.33623 19.9986 0.873778 19.807 0.532813 19.4661C0.191848 19.1251 0.000295822 18.6627 0.000295822 18.1805C-0.00394313 17.9576 0.0374137 17.7362 0.121828 17.5299C0.206243 17.3235 0.331935 17.1366 0.49119 16.9806L7.56371 9.99928L0.49119 2.92706C0.191536 2.63392 0.0158219 2.23695 0.000295822 1.81805C0.000295822 1.33587 0.191848 0.873445 0.532813 0.532495C0.873778 0.191544 1.33623 0 1.81842 0C2.25477 0.00545415 2.67294 0.181805 2.98203 0.490874Z"
              fill="black"
            />
          </svg>
        </button>
      </header>

      <aside class="w-full">
        <h4 class="pt-3 pb-2 text-sm font-semibold xs:pt-4 sm:text-base">Email Address:</h4>
        <div
          class="flex gap-2 border-[#B1B1B1] border-[1px] rounded-[5px] w-full px-3 sm:px-4 items-center"
        >
          <img :src="envelope" class="w-[16px] h-[16px] sm:w-[20px] sm:h-[20px]" alt="" />
          <input
            autocomplete="on"
            required
            type="email"
            placeholder="Please enter you email address"
            v-model="loginData.username"
            class="text-sm sm:text-base font-normal h-[38px] sm:h-[42.5px] w-full outline-none"
          />
        </div>
      </aside>
      <aside class="w-full">
        <h4 class="pt-3 pb-2 text-sm font-semibold xs:pt-4 sm:text-base">Password:</h4>
        <div
          class="flex gap-2 border-[#B1B1B1] border-[1px] rounded-[5px] w-full px-4 items-center"
        >
          <img :src="password" class="w-[16px] sm:w-[20px] h-[16px] sm:h-[20px]" alt="" />
          <input
            autocomplete="on"
            required
            :type="showPassword ? 'text' : 'password'"
            v-model="loginData.password"
            placeholder="Enter your password"
            class="text-base font-normal h-[38px] sm:h-[42.5px] w-full outline-none"
          />
          <img
            v-if="showPassword"
            :src="eyeinvis"
            class="min-w-[20px] min-h-[20px] max-w-[20px] max-h-[20px] sm:min-w-[20px] sm:min-h-[20px] sm:max-w-[20px] sm:ßmax-h-[20px] cursor-pointer"
            alt=""
            @click="
              () => {
                showPassword = false
              }
            "
          />

          <div v-else>
            <img
              :src="eyevis"
              class="min-w-[20px] min-h-[20px] max-w-[20px] max-h-[20px] sm:min-w-[20px] sm:min-h-[20px] sm:max-w-[20px] sm:ßmax-h-[20px] cursor-pointer"
              alt=""
              @click="
                () => {
                  showPassword = true
                }
              "
            />
          </div>
        </div>
      </aside>

      <p
        @click="forgotPasswordRedirect"
        class="font-['Poppins'] text-[11px] xs:text-xs sm:text-sm mt-2 xs:mt-3 cursor-pointer mb-3 xs:mb-4 ml-auto text-[#2033DE] underline font-semibold"
      >
        Forgot Password?
      </p>

      <button
        class="bg-[#EA2127] text-sm xs:text-base sm:text-xl font-bold text-white rounded-[5px] w-full py-2 sm:py-[10px] text-center uppercase mb-4 xs:mb-5"
        type="submit"
      >
        Continue
      </button>
      <h3
        class="w-full text-center after:w-[28.5%] xs:after:w-[32.5%] sm:after:w-[27.5%] relative after:absolute before:absolute before:left-0 before:h-[2px] before:w-[28.5%] xs:before:w-[32.5%] sm:before:w-[27.5%] before:top-[50%] after:flex before:bg-[#b1b1b1] text-[#9E9E9E] font-bold text-base xs:text-lg sm:text-xl after:h-[2px] after:top-[50%] after:rounded-md after:bg-[#b1b1b1] after:right-0"
      >
        Sign Up With
      </h3>
      <div class="flex gap-5 my-2 xs:my-3 sm:my-5">
        <!-- <GoogleLoginButton />
        <FacebookLoginButton /> -->
      </div>

      <h3 class="mb-4 text-base font-normal xs:text-lg sm:mb-6 sm:text-xl">
        Don't have an account?
        <span @click="toggleDiv" class="text-[#EA2127] font-bold cursor-pointer underline">
          Register
        </span>
      </h3>
    </form>

    <form
      v-else
      @submit.prevent="registerUser"
      @keydown.enter="registerUser"
      class="mx-2 flex items-center py-0 sm:pt-2 justify-center w-[380px] xs:w-[425px] sm:w-[475px] bg-white flex-col px-4 xs:px-6 sm:px-8 rounded-md mb-[2rem] mt-[5rem] sm:my-0"
    >
      <header
        class="flex items-center justify-between w-full py-3 xs:py-4 border-b-[1px] border-[#b1b1b1]"
      >
        <h3 class="text-base font-bold xs:text-lg sm:text-xl">Sign in / Register</h3>
        <button @click="$emit('closeModal')" type="button">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="w-[14px] xs:w-[16px] h-[14px] xs:h-[16px]"
            viewBox="0 0 20 20"
            fill="none"
          >
            <path
              d="M2.98203 0.490874L10 7.50855L16.9816 0.527235C17.1358 0.363097 17.3216 0.231792 17.5278 0.141194C17.734 0.0505961 17.9564 0.00257135 18.1816 0C18.6638 0 19.1262 0.191544 19.4672 0.532495C19.8082 0.873445 19.9997 1.33587 19.9997 1.81805C20.0039 2.04095 19.9626 2.26236 19.8782 2.4687C19.7938 2.67504 19.6681 2.86195 19.5088 3.01797L12.4363 9.99928L19.5088 17.0715C19.8085 17.3646 19.9842 17.7616 19.9997 18.1805C19.9997 18.6627 19.8082 19.1251 19.4672 19.4661C19.1262 19.807 18.6638 19.9986 18.1816 19.9986C17.9499 20.0082 17.7187 19.9695 17.5027 19.885C17.2868 19.8005 17.0907 19.672 16.9271 19.5077L10 12.49L3.00021 19.4895C2.84659 19.6482 2.66306 19.7748 2.46023 19.8622C2.25739 19.9496 2.03926 19.9959 1.81842 19.9986C1.33623 19.9986 0.873778 19.807 0.532813 19.4661C0.191848 19.1251 0.000295822 18.6627 0.000295822 18.1805C-0.00394313 17.9576 0.0374137 17.7362 0.121828 17.5299C0.206243 17.3235 0.331935 17.1366 0.49119 16.9806L7.56371 9.99928L0.49119 2.92706C0.191536 2.63392 0.0158219 2.23695 0.000295822 1.81805C0.000295822 1.33587 0.191848 0.873445 0.532813 0.532495C0.873778 0.191544 1.33623 0 1.81842 0C2.25477 0.00545415 2.67294 0.181805 2.98203 0.490874Z"
              fill="black"
            />
          </svg>
        </button>
      </header>
      <div class="flex w-full gap-5">
        <aside class="w-1/2">
          <h4 class="pt-3 pb-[0.4rem] text-sm font-semibold sm:text-[15px]">First Name:</h4>

          <div
            class="flex gap-2 relative border-[#B1B1B1] border-[1px] rounded-[5px] w-full px-4 items-center"
          >
            <img :src="userIcon" class="w-[16px] h-[16px] sm:w-[20px] sm:h-[20px]" alt="" />
            <input
              autocomplete="on"
              required
              type="text"
              id="first_name"
              placeholder="First name"
              v-model="registerData.first_name"
              class="text-sm sm:text-[15px] font-normal h-[38px] sm:h-[42.5px] w-full outline-none"
            />
          </div>
        </aside>
        <aside class="w-1/2">
          <h4 class="pt-3 pb-[0.4rem] text-sm font-semibold sm:text-[15px]">Last Name:</h4>
          <div
            class="flex gap-2 border-[#B1B1B1] border-[1px] rounded-[5px] w-full px-4 items-center"
          >
            <img :src="userIcon" class="w-[16px] h-[16px] sm:w-[20px] sm:h-[20px]" alt="" />
            <input
              autocomplete="on"
              required
              type="text"
              placeholder="Last name"
              v-model="registerData.last_name"
              class="text-sm sm:text-[15px] font-normal h-[38px] sm:h-[42.5px] w-full outline-none"
            />
          </div>
        </aside>
      </div>

      <aside class="w-full">
        <h4 class="pt-3 pb-[0.4rem] text-sm font-semibold sm:text-[15px]">Country :</h4>
        <!-- <div class="flex gap-2   border-[#B1B1B1] border-[1px] rounded-[5px] w-full px-4 items-center">

  <img :src="mobile" class="w-[16px] h-[16px] sm:w-[20px] sm:h-[20px]" alt="">
  <input 
  autocomplete="on" required  maxlength="10" type="text" placeholder="Please enter your mobile number" v-model="registerData.mobile_number"
    class="text-sm sm:text-[15px] font-normal h-[38px] sm:h-[42.5px] w-full outline-none">
</div> -->
        <CountrySelect @selected="AddCountry" />
      </aside>

      <aside class="w-full" v-if="registerData.nationality === 'Nepal'">
        <h4 class="pt-3 pb-[0.4rem] text-sm font-semibold sm:text-[15px]">Mobile Number:</h4>
        <div
          class="flex gap-2 border-[#B1B1B1] border-[1px] rounded-[5px] w-full px-4 items-center"
        >
          <img :src="mobile" class="w-[16px] h-[16px] sm:w-[20px] sm:h-[20px]" alt="" />
          <input
            autocomplete="on"
            required
            maxlength="10"
            type="text"
            placeholder="Please enter your mobile number"
            v-model="registerData.mobile_number"
            class="text-sm sm:text-[15px] font-normal h-[38px] sm:h-[42.5px] w-full outline-none"
          />
        </div>
      </aside>

      <aside class="w-full">
        <h4 class="pt-3 pb-[0.4rem] text-sm font-semibold sm:text-[15px]">Email Address:</h4>
        <div
          class="flex gap-2 border-[#B1B1B1] border-[1px] rounded-[5px] w-full px-4 items-center"
        >
          <img :src="envelope" class="w-[16px] h-[16px] sm:w-[20px] sm:h-[20px]" alt="" />
          <input
            autocomplete="on"
            required
            type="email"
            placeholder="Please enter your email address"
            v-model="registerData.email"
            class="text-sm sm:text-[15px] font-normal h-[38px] sm:h-[42.5px] w-full outline-none"
          />
        </div>
      </aside>

      <aside class="w-full">
        <h4 class="pt-3 pb-[0.4rem] text-sm font-semibold sm:text-[15px]">Your Password:</h4>
        <div
          class="flex gap-2 border-[#B1B1B1] border-[1px] rounded-[5px] w-full px-4 items-center"
        >
          <img :src="password" class="w-[20px] h-[20px]" alt="" />
          <input
            autocomplete="on"
            required
            :type="showPassword ? 'text' : 'password'"
            v-model="registerData.password"
            placeholder="Enter your password"
            class="text-sm sm:text-[15px] font-normal h-[38px] sm:h-[42.5px] w-full outline-none"
          />
          <img
            v-if="showPassword"
            :src="eyeinvis"
            class="min-w-[20px] min-h-[20px] max-w-[20px] max-h-[20px] sm:min-w-[20px] sm:min-h-[20px] sm:max-w-[20px] sm:ßmax-h-[20px] cursor-pointer"
            alt=""
            @click="
              () => {
                showPassword = false
              }
            "
          />

          <div v-else>
            <img
              :src="eyevis"
              class="min-w-[20px] min-h-[20px] max-w-[20px] max-h-[20px] sm:min-w-[20px] sm:min-h-[20px] sm:max-w-[20px] sm:ßmax-h-[20px] cursor-pointer"
              alt=""
              @click="
                () => {
                  showPassword = true
                }
              "
            />
          </div>
        </div>
      </aside>

      <aside class="w-full">
        <h4 class="pt-3 pb-[0.4rem] text-sm font-semibold sm:text-[15px]">Confirm Password:</h4>
        <div
          class="flex gap-2 border-[#B1B1B1] border-[1px] rounded-[5px] w-full px-4 items-center"
        >
          <img :src="password" class="w-[20px] h-[20px]" alt="" />
          <input
            autocomplete="on"
            required
            :type="showPassword ? 'text' : 'password'"
            v-model="registerData.password_confirm"
            placeholder="Enter your password"
            class="text-sm sm:text-[15px] font-normal h-[38px] sm:h-[42.5px] w-full outline-none"
          />
          <img
            v-if="showPassword"
            :src="eyeinvis"
            class="min-w-[20px] min-h-[20px] max-w-[20px] max-h-[20px] sm:min-w-[20px] sm:min-h-[20px] sm:max-w-[20px] sm:ßmax-h-[20px] cursor-pointer"
            alt=""
            @click="
              () => {
                showPassword = false
              }
            "
          />

          <div v-else>
            <img
              :src="eyevis"
              class="min-w-[20px] min-h-[20px] max-w-[20px] max-h-[20px] sm:min-w-[20px] sm:min-h-[20px] sm:max-w-[20px] sm:ßmax-h-[20px] cursor-pointer"
              alt=""
              @click="
                () => {
                  showPassword = true
                }
              "
            />
          </div>
        </div>
      </aside>

      <div class="flex w-full gap-2 mt-4">
        <input
          autocomplete="on"
          v-model="termsCheckbox"
          type="checkbox"
          class="w-[16px] xs:w-[20px]"
          name=""
          id=""
        />
        <a href="/terms" class="text-sm font-normal">
          Accept our
          <span class="font-bold text-sm text-[#EA2127] cursor-pointer"> Terms & Conditions </span>
        </a>
      </div>

      <button
        :disabled="!termsCheckbox"
        type="submit"
        ref=""
        class="bg-[#EA2127] text-sm xs:text-base sm:text-xl font-bold text-white rounded-[5px] w-full py-2 sm:py-[10px] text-center uppercase my-4 xs:my-5"
      >
        Continue
      </button>
    </form>
  </section>
</template>

<style scoped>
/* .signup-line::after {
  content: '';
} */

:deep(button:disabled, button[disabled]) {
  opacity: 0.65;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Firefox */
input[type='number'] {
  -moz-appearance: textfield;
}
</style>
<script setup lang="ts">
import { type Ref, ref } from 'vue'
// import { FormInst } from "naive-ui";
import { useJwtStore } from '../../stores/jwt'
import { UserLoginInfo } from '../../models/JWT.interface'
import envelope from '../../assets/layout/image/envelope.png'
import password from '../../assets/layout/image/password.png'
import mobile from '../../assets/layout/image/mobile.png'
import eyevis from '../../assets/layout/image/eyevis.png'
import eyeinvis from '../../assets/layout/image/eyeinvis.png'
import { useRouter } from 'vue-router'
import userIcon from '../../assets/account/UserIcon.png'
import { postAPI } from '../../api'
import CountrySelect from './CountrySelect.vue'
/* import GoogleLoginButton from '../Google/GoogleLoginButton.vue'
import FacebookLoginButton from './FacebookLoginButton.vue' */
const termsCheckbox = ref(false)
const showPassword = ref(false)
const jwtStore = useJwtStore()

const $router: any = useRouter()

const emit = defineEmits(['response', 'toogleHeader', 'closeModal'])
let loginData: Ref<UserLoginInfo> = ref({
  username: null,
  password: null,
  fcm_token: 'asdfasdf#asdf;lkn',
  fcm_type: 'android'
})

const FB = ref(null)
const model = ref(null)
const scope = ref(null)

const handleFbLogin = (res) => {
  console.log(res)
}
const handleSdkInit = ({ FB, scope }) => {
  FB.value = FB
  scope.value = scope
}

const forgotPasswordRedirect = () => {
  $router.push(`/forgot-password`)
  jwtStore.showSignInModel.value = false
}

let registerData = ref({
  email: null,
  first_name: null,
  last_name: null,
  mobile_number: '',
  password: null,
  password_confirm: null,
  role: 'Customer',
  nationality: 'Nepal'
})

function AddCountry(countryName) {
  registerData.value.nationality = countryName
}

async function loginUser() {
  await jwtStore.getJWT(loginData.value)
  emit('closeModal')
}
async function registerUser() {
  if (registerData.value.first_name === '') registerData.value.first_name = null

  if (registerData.value.last_name === '') registerData.value.last_name = null

  if (registerData.value.nationality !== 'Nepal') registerData.value.mobile_number = ''

  console.log(registerData)
  let data = await postAPI('users/auth', registerData.value)
  jwtStore.registerUserId = data.data.id
  emit('closeModal')
}
const rules = {
  username: {
    required: true,
    message: 'Please input your username',
    trigger: 'blur'
  },
  password: {
    required: true,
    message: 'Please input your password',
    trigger: ['blur']
  }
}
const toggle = ref(false)

function toggleDiv() {
  toggle.value = !toggle.value
  emit('toogleHeader', toggle.value)
}
</script>
