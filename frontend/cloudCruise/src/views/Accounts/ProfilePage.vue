<script setup lang="ts">
// import { NCard, NAvatar, useMessage } from "naive-ui";

import { useAccountStore } from '../../stores/accountStore'
import { useJwtStore } from '../../stores/jwt'
import { ref, type Ref } from 'vue'
import { patchAPI } from '../../api'
import defaultProfileImg from '../../assets/account/defaultProfile.png'
const jwtStore = useJwtStore()
const accountStore = useAccountStore()

const editProfileName = ref(false)
const editProfileEmail = ref(false)
const editProfileImage = ref(false)
const imageSrc = ref(null)
const editProfilePhoneNumber = ref(false)
const firstNameInput = ref(jwtStore.UserDetail.firstName)
const lastNameInput = ref(jwtStore.UserDetail.lastName)
const emailInput = ref(jwtStore.UserDetail.email)
const phoneNumberInput = ref(jwtStore.UserDetail.mobileNumber)
const selectedFile = ref(null)
const imgUrl: Ref<null | string> = ref(null)

function onFileSelected(event: any) {
  selectedFile.value = event.target.files[0]
  imgUrl.value = URL.createObjectURL(event.target.files[0])
}

// const message = useMessage();

function updateProfile() {
  const data = {
    firstName: firstNameInput.value,
    lastName: lastNameInput.value
  }
  editProfileName.value = false
  accountStore.editUserData(data)

  //   message.success("Successfullhhy updated profile");
}

function updateProfilePhoneNumber() {
  const data = {
    mobileNumber: phoneNumberInput.value
  }
  editProfilePhoneNumber.value = false
  accountStore.editUserData(data)
}
function updateProfileEmail() {
  const data = {
    email: emailInput.value
  }
  accountStore.editUserData(data)
}
const updateProfileImg = async () => {
  let formData = new FormData()
  if (selectedFile.value) {
    formData.append('avatar', selectedFile.value)
  }
  const response = await patchAPI('users/auth/update_info', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })

  jwtStore.UserDetail.avatar = response.data.avatar
  editProfileImage.value = false
}
</script>
<template>
  <!-- <pre>{{ jwtStore.UserDetail }}</pre> -->

  <section
    v-if="editProfileImage"
    class="font-['Poppins'] absolute top-0 w-full h-[100vh] bg-[rgba(0,0,0,0.4)] z-10 flex items-center justify-center"
  >
    <div
      class="flex items-center justify-center w-[375px] xs:w-[450px] sm:w-[500px] lg:w-[580px] bg-white flex-col px-4 xs:px-7 rounded-md"
    >
      <div
        class="flex items-center justify-between w-full py-3 xs:py-4 border-b-[1px] border-[#b1b1b1]"
      >
        <h3 class="text-lg font-semibold">Select Profile Picture</h3>
        <button @click="() => (editProfileImage = false)">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="w-[16px] h-[16px]"
            viewBox="0 0 20 20"
            fill="none"
          >
            <path
              d="M2.98203 0.490874L10 7.50855L16.9816 0.527235C17.1358 0.363097 17.3216 0.231792 17.5278 0.141194C17.734 0.0505961 17.9564 0.00257135 18.1816 0C18.6638 0 19.1262 0.191544 19.4672 0.532495C19.8082 0.873445 19.9997 1.33587 19.9997 1.81805C20.0039 2.04095 19.9626 2.26236 19.8782 2.4687C19.7938 2.67504 19.6681 2.86195 19.5088 3.01797L12.4363 9.99928L19.5088 17.0715C19.8085 17.3646 19.9842 17.7616 19.9997 18.1805C19.9997 18.6627 19.8082 19.1251 19.4672 19.4661C19.1262 19.807 18.6638 19.9986 18.1816 19.9986C17.9499 20.0082 17.7187 19.9695 17.5027 19.885C17.2868 19.8005 17.0907 19.672 16.9271 19.5077L10 12.49L3.00021 19.4895C2.84659 19.6482 2.66306 19.7748 2.46023 19.8622C2.25739 19.9496 2.03926 19.9959 1.81842 19.9986C1.33623 19.9986 0.873778 19.807 0.532813 19.4661C0.191848 19.1251 0.000295822 18.6627 0.000295822 18.1805C-0.00394313 17.9576 0.0374137 17.7362 0.121828 17.5299C0.206243 17.3235 0.331935 17.1366 0.49119 16.9806L7.56371 9.99928L0.49119 2.92706C0.191536 2.63392 0.0158219 2.23695 0.000295822 1.81805C0.000295822 1.33587 0.191848 0.873445 0.532813 0.532495C0.873778 0.191544 1.33623 0 1.81842 0C2.25477 0.00545415 2.67294 0.181805 2.98203 0.490874Z"
              fill="black"
            />
          </svg>
        </button>
      </div>
      <p class="mt-8 mb-4 text-sm font-normal">
        Photo must be less than 2MB

        <!-- <img v-if="selectedFile" :src="imgUrl" alt="" height="40" srcset=""> -->
      </p>

      <label
        for="dropzone-file"
        class="flex flex-col items-center justify-center w-[100%] h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600 bg-no-repeat bg-cover bg-center"
        :style="`background-image: url('${imgUrl}') !important`"
      >
        <div class="flex flex-col items-center justify-center pt-5 pb-6">
          <svg
            class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 20 16"
          >
            <path
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
            />
          </svg>
          <p class="mb-2 text-sm text-gray-500 dark:text-gray-400">
            <span class="font-semibold">Click to upload</span> or drag and drop
          </p>
          <p class="text-xs text-gray-500 dark:text-gray-400">
            SVG, PNG, JPG or GIF (MAX. 800x400px)
          </p>
        </div>
        <input
          id="dropzone-file"
          type="file"
          class="hidden"
          name="filename"
          :value="imageSrc"
          @change="(e) => onFileSelected(e)"
        />
      </label>
      <h2 class="text-lg font-semibold">
        {{ imageSrc }}
      </h2>
      <button
        @click="updateProfileImg"
        class="bg-[#EA2127] rounded-[5px] text-white font-semibold text-base lg:text-lg px-4 py-1 my-4 ml-auto"
      >
        Save
      </button>
    </div>
  </section>
  <main
    class="profile-and-buttons mx-auto flex !flex-col my-0 items-center justify-center gap-[10px] px-[12px] xs:px-[16px] py-[20px] w-full xs:w-[97.5%] sm:w-[87.5%] md:w-[77.5%] lg:w-[65%] !font-['Poppins'] pt-6"
  >
    <div class="w-full">
      <header class="py-4 flex justify-between items-center border-[#e1e1e1] border-b-[1px]">
        <div class="">
          <h1 class="text-[22px] lg:text-[26px] sm:text-[28px] xl:text-[30px] font-bold">
            Personal Details
          </h1>
          <p class="text-sm xs:text-base sm:text-lg xl:text-xl font-nomral my-[10px]">
            View your info and discover its uses.
          </p>
        </div>

        <div class="flex flex-col gap-[10px] items-center relative">
          <!-- <img :src="jwtStore.UserDetail.avatar" class="" alt=""> -->
          <aside
            v-if="jwtStore.UserDetail.avatar"
            class="min-w-[70px] min-h-[70px] w-[70px] h-[70px] sm:w-[80px] sm:h-[80px] xl:!w-[90px] xl:!h-[90px] rounded-[50%] border-[1px] border-black bg-cover bg-center bg-no-repeat"
            :style="`background-image: url('${jwtStore.UserDetail.avatar}')`"
          ></aside>
          <img
            v-else
            :src="defaultProfileImg"
            class="min-w-[70px] min-h-[70px] w-[70px] h-[70px] sm:w-[80px] sm:h-[80px] xl:!w-[90px] xl:!h-[90px] rounded-[50%] border-[1px] border-black bg-cover bg-center bg-no-repeat"
          />

          <button
            @click="() => (editProfileImage = true)"
            class="absolute flex items-center justify-center gap-[5px] py-[3px] xs:py-[5px] px-[8px] xs:px-[13px] border-[#b1b1b1] border-[1px] rounded-[5px] bg-[#fff] bottom-[-5px]"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="11"
              height="11"
              viewBox="0 0 10 10"
              fill="none"
            >
              <path
                d="M9.63396 0.366044C9.39954 0.131668 9.08163 0 8.75014 0C8.41866 0 8.10075 0.131668 7.86633 0.366044L7.31538 0.916997L9.083 2.68462L9.63396 2.13367C9.86833 1.89925 10 1.58134 10 1.24986C10 0.91837 9.86833 0.600459 9.63396 0.366044ZM8.57776 3.18986L6.81014 1.42224L1.02441 7.20797C0.730528 7.5017 0.514493 7.86405 0.395837 8.26225L0.0148832 9.54083C-0.00350918 9.60253 -0.00488094 9.66805 0.0109131 9.73047C0.0267072 9.79288 0.0590796 9.84987 0.104605 9.89539C0.15013 9.94092 0.207116 9.97329 0.269531 9.98909C0.331946 10.0049 0.39747 10.0035 0.45917 9.98512L1.73775 9.60416C2.13595 9.48551 2.4983 9.26947 2.79203 8.97559L8.57776 3.18986Z"
                fill="#9E9E9E"
              />
            </svg>
            <p class="font-['Roboto'] text-[10px] xs:text-xs font-semibold text-[#b1b1b1]">Edit</p>
          </button>
        </div>
      </header>
      <article
        v-if="!editProfileName"
        class="flex justify-between border-b-[1px] border-[#e1e1e1] items-startm py-3 xs:py-4 sm:py-6 xl:py-7 px-0 text-sm xs:text-base sm:text-lg lg:text-xl xl:text-[22px]"
      >
        <h3 class="font-semibold w-[15%] xsm:w-[33.33%]">Name</h3>
        <div class="font-normal w-[33.33%]">
          {{ jwtStore.UserDetail.firstName }}
          {{ jwtStore.UserDetail.lastName }}
        </div>

        <div class="text-white flex justify-end items-center w-[33.33%]">
          <button
            @click="
              () => {
                editProfileName = true
              }
            "
            class="text-xs xs:text-sm sm:text-base lg:text-lg xl:text-xl text-[#EA2127] font-semibold"
          >
            Edit
          </button>
        </div>
      </article>
      <article
        v-else
        class="flex flex-col border-b-[1px] py-3 xs:py-4 sm:py-6 xl:py-7 px-0 border-[#e1e1e1]"
      >
        <div
          class="flex justify-between gap-2 items-start text-sm xs:text-base sm:text-lg lg:text-xl xl:text-[22px]"
        >
          <h3 class="font-semibold w-[25%]">Name</h3>
          <div
            class="flex w-[80%] xsm:w-[75%] flex-col gap-2 xsm:gap-0 xsm:flex-row justify-between"
          >
            <div class="flex flex-col w-full xsm:w-[47.5%] gap-2">
              <label
                for="firstName"
                class="text-sm font-semibold xs:text-base sm:text-lg lg:text-xl"
                >First Name</label
              >
              <input
                id="firstName"
                class="border-[1px] border-[#b1b1b1] px-[12px] rounded-[5px] py-[6px] max-w-full text-sm md:text-base lg:text-lg"
                type="text"
                v-model="firstNameInput"
              />
            </div>

            <div class="flex w-full xsm:w-[47.5%] flex-col gap-2">
              <label
                for="lastName"
                class="text-sm xs:text-base sm:text-lg lg:text-xl xl:text-[22px] font-semibold"
                >Last Name</label
              >
              <input
                id="lastName"
                class="max-w-full border-[1px] border-[#b1b1b1] px-[12px] rounded-[5px] py-[6px] text-sm md:text-base lg:text-lg"
                type="text"
                v-model="lastNameInput"
              />
            </div>
          </div>
        </div>
        <div class="flex justify-end w-full mt-4">
          <button
            @click="() => (editProfileName = false)"
            class="border-[1px] border-[#B1B1B1] rounded-[5px] text-black font-semibold text-sm sm:text-base lg:text-lg px-4 py-1"
          >
            Cancel
          </button>
          <button
            @click="updateProfile"
            class="bg-[#EA2127] rounded-[5px] text-white font-semibold text-sm sm:text-base lg:text-lg px-4 py-1 ml-3"
          >
            Save
          </button>
        </div>
      </article>
      <article
        v-if="editProfileEmail"
        class="flex flex-col border-b-[1px] py-3 xs:py-4 sm:py-6 xl:py-7 px-0 border-[#e1e1e1]"
      >
        <div
          class="flex justify-between gap-2 items-startm text-sm xs:text-base sm:text-lg lg:text-xl xl:text-[22px]"
        >
          <h3 class="font-semibold w-[25%]">Email</h3>
          <div class="flex flex-col w-[50%] gap-2">
            <label for="email" class="text-xl font-semibold">Email</label>
            <input
              id="email"
              class="border-[1px] border-[#b1b1b1] px-4 rounded-[5px] py-[6px] max-w-full text-lg"
              type="text"
              v-model="emailInput"
            />
          </div>
        </div>
        <div class="flex justify-end w-full mt-4">
          <button
            @click="
              () => {
                editProfileEmail = false
              }
            "
            class="border-[1px] border-[#B1B1B1] rounded-[5px] text-black font-semibold text-sm sm:text-base lg:text-lg px-4 py-1"
          >
            Cancel
          </button>
          <button
            @click="updateProfileEmail"
            class="bg-[#EA2127] rounded-[5px] text-white font-semibold text-sm sm:text-base lg:text-lg px-4 py-1 ml-3"
          >
            Save
          </button>
        </div>
      </article>
      <article
        v-else
        class="flex justify-start border-b-[1px] border-[#e1e1e1] items-start py-3 xs:py-4 sm:py-6 xl:py-7 px-0 text-sm xs:text-base sm:text-lg lg:text-xl xl:text-[22px]"
      >
        <div class="font-semibold w-[15%] xsm:w-[33.33%]">Email</div>
        <div class="flex items-center gap-3 font-normal sm:gap-5 w-fit">
          <aside>
            {{ jwtStore.UserDetail.email }}
          </aside>

          <aside>
            <div
              v-if="jwtStore.UserDetail.emailVerified"
              class="bg-[#34C759] px-2 py-[2px] xs:py-1 font-semibold rounded-md text-[10px] sm:text-xs lg:text-sm xl:text-base w-fit text-white"
            >
              Verified
            </div>
            <div
              v-else
              class="bg-[#EA2127] px-2 py-[2px] xs:py-1 font-semibold rounded-md text-[10px] sm:text-sm lg:text-base xl:text-lg w-fit text-white"
            >
              Not Verified
            </div>
          </aside>
        </div>
        <!-- <div class="text-white flex justify-end items-center w-[33.33%]"> -->

        <!-- <button @click="() => editProfileEmail = true"
            class="text-xs xs:text-sm sm:text-base lg:text-lg xl:text-xl text-[#EA2127] font-semibold">
            Edit
          </button> -->
        <!-- </div> -->
      </article>

      <article
        v-if="editProfilePhoneNumber"
        class="flex flex-col border-b-[1px] py-3 xs:py-4 sm:py-6 xl:py-7 px-0 border-[#e1e1e1]"
      >
        <div
          class="flex justify-between gap-2 items-start text-sm xs:text-base sm:text-lg lg:text-xl xl:text-[22px]"
        >
          <h3 class="font-semibold w-[25%]">Phone Number</h3>
          <div class="flex flex-col w-[80%] xsm:w-[60%] lg:w-[50%] gap-2">
            <label for="email" class="text-sm font-semibold sm:text-base lg:text-lg xl:text-xl"
              >Phone Number</label
            >
            <input
              id="email"
              class="border-[1px] border-[#b1b1b1] px-4 rounded-[5px] py-[6px] max-w-full text-sm md:text-base lg:text-lg"
              type="text"
              v-model="phoneNumberInput"
            />
          </div>
        </div>
        <div class="flex justify-end w-full mt-4">
          <button
            @click="
              () => {
                editProfilePhoneNumber = false
              }
            "
            class="border-[1px] border-[#B1B1B1] rounded-[5px] text-black font-semibold text-sm sm:text-base lg:text-lg px-4 py-1"
          >
            Cancel
          </button>
          <button
            @click="updateProfilePhoneNumber"
            class="bg-[#EA2127] rounded-[5px] text-white font-semibold text-sm sm:text-base lg:text-lg px-4 py-1 ml-3"
          >
            Save
          </button>
        </div>
      </article>
      <article
        v-else
        class="flex justify-between border-b-[1px] border-[#e1e1e1] items-start py-3 xs:py-4 sm:py-6 xl:py-7 px-0 text-sm xs:text-base lg:text-lg xl:text-xl 2xl:text-[22px]"
      >
        <h3 class="font-semibold w-[15%] xsm:w-[33.33%]">Phone Number</h3>
        <div class="font-normal w-[33.33%] flex gap-3 items-center">
          <aside>
            {{ jwtStore.UserDetail.mobileNumber }}
          </aside>

          <!-- <aside>
            <div v-if="jwtStore.UserDetail.phoneVerified"
              class="bg-[#34C759] px-2 py-[2px] xs:py-1 font-semibold rounded-md text-[10px] sm:text-xs lg:text-sm xl:text-base w-fit text-white">

              Verified
            </div>
            <div v-else class="bg-[#EA2127] px-2 py-[2px] xs:py-1 font-semibold rounded-md text-[10px] sm:text-xs lg:text-sm xl:text-base w-fit">
              Not Verified</div>
          </aside> -->
        </div>
        <div class="text-white flex justify-end items-center w-[33.33%]">
          <!-- 
          <button @click="() => editProfilePhoneNumber = true"
            class="text-xs xs:text-sm sm:text-base lg:text-lg xl:text-xl text-[#EA2127] font-semibold">
            Edit
          </button> -->
        </div>
      </article>
      <article
        class="flex justify-between border-b-[1px] border-[#e1e1e1] items-start py-3 xs:py-4 sm:py-6 xl:py-7 px-0 text-sm xs:text-base lg:text-lg xl:text-xl 2xl:text-[22px]"
      >
        <h3 class="font-semibold w-[15%] xsm:w-[33.33%]">Password</h3>
        <div class="font-normal w-[50%] sm:w-[33.33%] flex gap-3 items-center">
          <aside>Change Your password</aside>
        </div>
        <div class="text-white flex justify-end items-center w-[15%] sm:w-[33.33%]">
          <button
            @click="$router.push(`/change-password/${jwtStore.UserDetail.id}`)"
            class="text-xs xs:text-sm sm:text-base lg:text-lg xl:text-xl text-[#EA2127] font-semibold cursor-pointer"
          >
            Change
          </button>
        </div>
      </article>
    </div>
  </main>
</template>

<style scoped></style>
