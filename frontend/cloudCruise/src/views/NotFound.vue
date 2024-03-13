<template>
  <section class="bg-white">
    <div class="container flex items-center min-h-[50vh] px-6 py-12 mx-auto">
      <div class="flex flex-col items-center mx-auto text-center">
        <p class="p-3 text-sm font-medium text-blue-500 rounded-full bg-blue-50 dark:bg-gray-800">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="2"
            stroke="currentColor"
            class="w-6 h-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M12 9v3.75m9-.75a9 9 0 11-18 0 9 9 0 0118 0zm-9 3.75h.008v.008H12v-.008z"
            />
          </svg>
        </p>
        <h1 class="mt-3 text-2xl font-semibold text-gray-800">Page not found</h1>
        <p class="mt-4 text-gray-500">
          The page you are looking for doesn't exist. Here are some helpful links:
        </p>

        <div class="flex items-center w-full mt-6 gap-x-3 sm:w-auto">
          <CustomButton
            @click="$router.push('/flights')"
            label="Search Flights"
            color="#f15d5d"
            size="lg"
          >
            <template v-slot:leftIcon>
              <Icon color="white" size="20">
                <Airplane />
              </Icon>
            </template>
          </CustomButton>
          <CustomButton
            @click="$router.push('/')"
            label="Go Home"
            color="#e2e2e2"
            size="lg"
            text-color="#333"
          >
            <template v-slot:leftIcon>
              <Icon color="#333" size="20">
                <HomeOutline />
              </Icon>
            </template>
          </CustomButton>
        </div>
      </div>
    </div>
  </section>
</template>
<script setup lang="ts">
import { Icon } from '@vicons/utils'
import CustomButton from '../components/CustomElements/CustomButton.vue'
import { Airplane, HomeOutline } from '@vicons/ionicons5'
import { Biking } from '@vicons/fa'
</script>
<style lang=""></style>
