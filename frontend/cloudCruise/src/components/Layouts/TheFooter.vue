<template>
  <section
    class="grid grid-cols-2 lg:grid-cols-4 px-5 gap-y-5 xs:px-[8%] !text-white font-[Poppins] bg-primary-400 py-[40px]"
  >
    <aside class="">
      <h2 class="text-2xl font-bold mb-5">Legal</h2>
      <div class="flex flex-col gap-[10px] text-xl font-normal">
        <p
          class="inline font-normal transition-all duration-300 ease-in cursor-pointer max-w-fit links"
        >
          Privacy Policy
        </p>
        <p
          class="inline font-normal transition-all duration-300 ease-in cursor-pointer max-w-fit links"
        >
          Terms & Conditions
        </p>
        <p
          class="inline font-normal transition-all duration-300 ease-in cursor-pointer max-w-fit links"
        >
          Activity Policy
        </p>
        <p
          class="inline font-normal transition-all duration-300 ease-in cursor-pointer max-w-fit links"
        >
          Experiences Policy
        </p>
      </div>
    </aside>
    <aside class="flex lg:items-center flex-col">
      <div class="flex flex-col">
        <h2 class="text-2xl font-bold mb-5">Company</h2>
        <div class="flex flex-col gap-[10px] text-xl font-normal">
          <a
            class="inline font-normal transition-all duration-300 ease-in cursor-pointer max-w-fit links"
            href="#"
            >About</a
          >
          <a
            class="inline font-normal transition-all duration-300 ease-in cursor-pointer max-w-fit links"
            href="#"
            >Contact</a
          >
        </div>
      </div>
    </aside>
    <aside class="flex items-start lg:items-center flex-col">
      <SocialIconsComponent />
    </aside>
    <aside class="flex lg:flex-col items-end">
      <div class="flex flex-col">
        <h2 class="text-2xl font-bold mb-5">Download</h2>
        <div class="flex flex-col gap-[10px] text-xl font-normal">
          <!-- <a href="https://apps.apple.com/us/app/trip-turbo/id6471469699" class="w-full">
            <img
              :src="AppStoreIcon"
              loading="lazy"
              class="scale-[0.90] lg:scale-1 w-[210px] h-[60px] transition-all duration-500 ease-in-out hover:scale-105"
            />
          </a>
          <a href="https://apps.apple.com/us/app/trip-turbo/id6471469699" class="w-full">
            <img
              :src="GooglePlayIcon"
              loading="lazy"
              class="scale-[0.90] lg:scale-1 w-[210px] h-[60px] transition-all duration-500 ease-in-out hover:scale-105"
            />
          </a> -->
        </div>
      </div>
    </aside>
  </section>
</template>

<script setup lang="ts">
/* import AppStoreIcon from '@/assets/icons/apple.png'
import GooglePlayIcon from '@/assets/icons/googleplay.png' */
import SocialIconsComponent from '@/components/Layouts/SocialIconsComponent.vue'
</script>

<style scoped>
.links {
  background-size: 0% 2px;
  background-image: linear-gradient(90deg, white, white);
  background-position: left bottom;
  text-decoration: none;
  background-repeat: no-repeat;
}

.links:hover {
  background-size: 100% 2px;
}
</style>
