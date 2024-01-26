<script setup lang="ts">
import { RouterView } from 'vue-router'
import { NMessageProvider } from 'naive-ui'
import { NConfigProvider, GlobalThemeOverrides } from 'naive-ui'
import TheHeader from '@/components/Layouts/TheHeader.vue'
import Footer from '@/components/Layouts/TheFooter.vue'
import { onBeforeMount } from 'vue'
import { useJwtStore } from './stores/jwt'

const JwtStore = useJwtStore()
onBeforeMount(async () => {
  await JwtStore.refreshAccessToken()
})
const themeOverrides: GlobalThemeOverrides = {
  common: {
    primaryColor: '#ea2127',
    primaryColorHover: '#FF0000'
  },
  Button: {
    textColor: '#FF0000'
  },
  Select: {
    peers: {
      InternalSelection: {
        textColor: '#FF0000'
      }
    }
  },
  Steps: {
    splitorColorFinish: '#34C759',
    indicatorBorderColorFinish: '#34C759',
    indicatorColorFinish: 'transparent',
    indicatorColorProcess: '#34C759',
    indicatorBorderColorProcess: '#34C759',
    indicatorTextColorFinish: '#34C759'
  }
}
</script>

<template>
  <n-config-provider :theme-overrides="themeOverrides">
    <n-message-provider>
      <TheHeader />
      <notifications position="top center" classes="my-notification" />
      <div style="margin-top: 70px; min-height: 80vh">
        <RouterView />
      </div>
      <Footer />
    </n-message-provider>
  </n-config-provider>
</template>

<style>
.my-notification.success {
  margin: 2px 5px 5px;
  padding: 20px;
  font-size: 12px;
  color: #ffffff;
  background: #68cd86;
  border-left-color: #42a85f;
}

.my-notification.warn {
  margin: 2px 5px 5px;
  padding: 20px;
  font-size: 12px;
  color: #ffffff;
  background: #ffb648;
  border-left-color: #f48a06;
}

.my-notification.error {
  margin: 2px 5px 5px;
  padding: 20px;
  font-size: 12px;
  color: #ffffff;
  background: #e54d42;
  border-left-color: #b82e24;
}
</style>
