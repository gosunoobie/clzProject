<template>
  <section class="fixed top-0 z-[99]">
    <nav
      class="flex items-center nav-bar-container px-[5%] md:px-0 navbar-show transition-all ease-in-out"
      :class="{ 'navbar--hidden': !homeStore.showNavbar }"
    >
      <!-- <nav
      class="flex items-center nav-bar-container px-[5%] md:px-0 navbar-show transition-all ease-in-out duration-500"
    > -->
      <aside class="flex items-center justify-between w-full md:ml-0 md:justify-around">
        <div class="flex gap-2 items-center cursor-pointer" @click="$router.push('/')">
          <img
            :src="CloudCruiseLogo"
            alt="CloudCruise Logo"
            class="cursor-pointer w-[90px] mxs:w-[55px]"
          />
          <p class="text-xl font-semibold text-primary-500">Cloud Cruise</p>
        </div>
        <div class="flex items-center nav-bar">
          <a
            @click="
              () => {
                currentTab = 0
                $router.push({ name: 'FlightList' })
              }
            "
            :class="[
              'tab-button transition-all duration-200 ease-in-out',
              { active: currentTab === 0 }
            ]"
          >
            Flights
          </a>
          <!-- <a
            @click="
              () => {
                currentTab = 1
                $router.push({ name: 'Activities' })
              }
            "
            :class="[
              'tab-button transition-all duration-200 ease-in-out',
              { active: currentTab === 1 }
            ]"
            >Activities
          </a>
          <a
            @click="
              () => {
                currentTab = 0
                $router.push({ name: 'Hotels' })
              }
            "
            :class="[
              'tab-button transition-all duration-200 ease-in-out',
              { active: currentTab === 0 }
            ]"
          >
            Hotels
          </a> -->
          <!--
          <a
            class="relative flex items-center gap-2"
            @click="
              () => {
                currentTab = 2;
                toggleDropdown();
              }
            "
            :class="[
              'tab-button transition-all duration-200 ease-in-out',
              { active: currentTab === 2 },
            ]"
            >Services
            <Icon size="15">
              <CaretUp v-if="dropdown" />
              <CaretDown v-else />
            </Icon>

            <div
              :class="`menu-dropdown z-[19] !duration-[600] ease-in-out transition-all ${
                dropdown ? 'show-drop' : ''
              }`"
              ref="dropdownRef"
              v-click-away="dropdown && clickAwayFunc"
            >
              <a @click="$router.push({ name: 'FlightList' })">
                <div class="dropdown-item">
                  <div class="dropdown-item-img">
                    <img
                      src="../../assets/layout/image/plane.png"
                      alt="plane image"
                      loading="lazy"
                    />
                  </div>
                  <div class="dropdown-item-desc">
                    <div class="item-title">Flights</div>
                    <div class="item-desc">
                      Find a flexible flight for your next trip
                    </div>
                  </div>
                </div>
              </a>
              <a @click="$router.push({ name: 'Activities' })">
                <div class="dropdown-item">
                  <div class="dropdown-item-img">
                    <img
                      src="../../assets/layout/image/activity.png"
                      loading="lazy"
                      alt="activity image"
                    />
                  </div>
                  <div class="dropdown-item-desc">
                    <div class="item-title">Activities</div>
                    <div class="item-desc">
                      Challenege yourself with a thrill
                    </div>
                  </div>
                </div>
              </a>
            </div>
          </a>
          -->
          <!-- <a
            @click="
              () => {
                currentTab = 3;
                $router.push({ name: 'Contact' });
              }
            "
            :class="[
              'tab-button transition-all duration-200 ease-in-out',
              { active: currentTab === 3 },
            ]"
            >Contact</a
          > -->
          <a
            @click="
              () => {
                currentTab = 4
                $router.push({ name: 'Blog' })
              }
            "
            :class="[
              'tab-button transition-all duration-200 ease-in-out',
              { active: currentTab === 4 }
            ]"
            >Blog</a
          >
        </div>
        <div>
          <n-dropdown
            v-if="jwtStore.isLoggedIn"
            trigger="click"
            :options="options"
            size="huge"
            style="border-radius: 5px; font-weight: 500; font-family: 'Poppins'"
          >
            <img
              v-if="jwtStore?.UserDetail?.avatar"
              :src="jwtStore?.UserDetail?.avatar"
              alt="profile pic"
              loading="lazy"
              class="mr-4 profile-img md:mr-0"
            />
            <img
              v-else
              :src="defaultProfileImg"
              loading="lazy"
              alt=" default profile pic"
              class="mr-4 profile-img md:mr-0"
            />
          </n-dropdown>
          <a
            href="#"
            v-else
            @click="jwtStore.showSignInModel.value = true"
            :class="{ 'navbar-top': homeStore.showNavbar }"
            class="flex items-center justify-center gap-[10px] py-2 px-4 mr-4 text-sm font-semibold border-0 text-white border-none rounded-[5px] md:text-base md:px-[20px] bg-primary-400 md:mr-u"
          >
            <img
              class="h-[20px]"
              loading="lazy"
              src="../../assets/layout/image/userLogo.png"
              alt="user logo"
            />
            Sign in
          </a>
        </div>
      </aside>
      <div
        class="menu-btn p-4 pr-0 w-fit md:w-[60px] cursor-pointer hover:scale-110 duration-300 transition-all ease-out border-l-[1px] border-l-[#9F9F9F]"
        @click="toggleResponsiveDropdown"
      >
        <img
          src="../../assets/layout/image/menu-drop-icon.png"
          alt="drop down menu icon"
          loading="lazy"
          class="max-w-[22.5px] min-w-[22.5px]"
        />
      </div>
    </nav>
    <div
      :class="`responsive-menu-dropdown  !w-[100vw] left-[-100%] !duration-300 ease-out transition-all !z-[9] ${
        responsiveDropdown ? 'show-dropdown' : ''
      }`"
      v-click-away="clickAwayResponsiveFunc"
    >
      <ul style="padding-left: 0; padding-bottom: 0">
        <li @click="$router.push({ name: 'FlightList' }), (responsiveDropdown = false)">
          <p>Flights</p>
        </li>
        <li @click="$router.push({ name: 'Activities' }), (responsiveDropdown = false)">
          <p>Activities</p>
        </li>
        <!--    <li>
          <div>
            <n-collapse arrow-placement="right">
              <n-collapse-item name="1">
                <template #header>
                  <span
                    class="collaspe-header-link font-['Roboto'] font-thin text-xl"
                    ><b>Services</b></span
                  >
                </template>
                <a
                  class="responsive-list-menu-link"
                  @click="
                    $router.push('/flights'), (responsiveDropdown = false)
                  "
                  active
                >
                  <div class="dropdown-item">
                    <div class="dropdown-item-img">
                      <img
                        src="../../assets/layout/image/plane.png"
                        alt="plane image"
                        loading="lazy"
                      />
                    </div>
                    <div class="dropdown-item-desc">
                      <div class="item-title">Flights</div>
                      <div class="item-desc">
                        Find a flexible flight for your next trip
                      </div>
                    </div>
                  </div>
                </a>
                <a
                  @click="
                    $router.push('/activities'), (responsiveDropdown = false)
                  "
                  class="responsive-list-menu-link"
                >
                  <div class="dropdown-item">
                    <div class="dropdown-item-img">
                      <img
                        src="../../assets/layout/image/activity.png"
                        alt="activity image"
                        loading="lazy"
                      />
                    </div>
                    <div class="dropdown-item-desc">
                      <div class="item-title">Activities</div>
                      <div class="item-desc">
                        Challenege yourself with a thrill
                      </div>
                    </div>
                  </div>
                </a>
              </n-collapse-item>
            </n-collapse>
          </div>
        </li>
        -->
        <li @click="$router.push({ name: 'Contact' }), (responsiveDropdown = false)">
          <p>Contact</p>
        </li>
        <li @click="$router.push({ name: 'Blog' }), (responsiveDropdown = false)">
          <p>Blog</p>
        </li>
      </ul>
    </div>
  </section>

  <teleport to="body" v-if="jwtStore.showModal.value">
    <SignninModel @close-Modal="closeSignInModel" />
  </teleport>
</template>

<script setup lang="ts">
import { ref, watchEffect, h, onMounted, watch, onBeforeUnmount } from 'vue'
import { NDropdown, NCollapse, NCollapseItem } from 'naive-ui'
import SignninModel from '../Account/SigninModel.vue'
import { useJwtStore } from '../../stores/jwt'
import router from '../../router/index'
import { NIcon } from 'naive-ui'
import { UserCircleRegular, SuitcaseRolling, Coins, SignOutAlt, Receipt } from '@vicons/fa'
import defaultProfileImg from '../../assets/account/defaultProfile.png'
import { useHomeStore } from '../../stores/homeStore.ts'
import { useRoute } from 'vue-router'
import CloudCruiseLogo from '/logo.png'

const navChangingRoutes = ['About', 'Blog', 'FlightList', 'Activities', 'Hotels']
const currentRouteName = ref('')
const isAllowedNavChangingRoute = ref(true)
const route = useRoute()

// Update route name on component mount and route changes
onMounted(() => {
  updateRouteName()
})

watch(
  () => route.name,
  () => {
    updateRouteName()

    if (navChangingRoutes.includes(currentRouteName.value)) {
      isAllowedNavChangingRoute.value = true
      homeStore.showNavbar = true
    } else {
      isAllowedNavChangingRoute.value = false
      homeStore.showNavbar = false
    }
  }
)

function updateRouteName() {
  currentRouteName.value = route.name || 'Unknown Route'
}
const jwtStore = useJwtStore()
const homeStore = useHomeStore()
const lastScrollPosition = ref(0)
// const onScroll = () => {
//   const currentScrollPosition =
//     window.pageYOffset || document.documentElement.scrollTop;
//   if (currentScrollPosition < 0) {
//     return;
//   }
//   if (Math.abs(currentScrollPosition - lastScrollPosition.value) < 60) {
//     return;
//   }
//   homeStore.showNavbar = currentScrollPosition < lastScrollPosition.value;
//   lastScrollPosition.value = currentScrollPosition;
// };
const onScroll = () => {
  const currentScrollPosition = document.documentElement.scrollTop
  if (currentScrollPosition < 0) {
    return
  }
  homeStore.showNavbar = currentScrollPosition === 0 && isAllowedNavChangingRoute.value
}

onMounted(() => {
  window.addEventListener('scroll', onScroll)
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', onScroll)
})
// import {  UserAvatarFilledAlt } from "@vicons/carbon";

// watchEffect(()=>{
// console.log(jwtStore.isLoggedIn)

// },jwtStore.isLoggedIn)

const dropdown = ref(false)
const responsiveDropdown = ref(false)
const currentTab = ref(6)
// const showModal = jwtStore.showSignInModel
const showModalRegister = ref(false)

const documentBody = document.querySelector('body')

watch(responsiveDropdown, () => {
  if (responsiveDropdown.value) homeStore.showNavbar = false
  else homeStore.showNavbar = true
})

watchEffect(() => {
  if (jwtStore.showSignInModel.value) {
    documentBody.style.overflow = 'hidden'
  } else {
    documentBody.style.overflow = 'auto'
  }
}, jwtStore.showSignInModel.value)

function toggleDropdown() {
  dropdown.value = !dropdown.value
}

function toggleResponsiveDropdown() {
  responsiveDropdown.value = !responsiveDropdown.value
}

const clickAwayResponsiveFunc = () => {
  // responsiveDropdown.value = false;
}

const closeSignInModel = () => {
  jwtStore.showSignInModel.value = false
}
// function toggleModal() {
//   showModal.value = !showModal.value;
//   showModalRegister.value = !showModalRegister.value;
// }

// const childMsg = ref("");

// watch(childMsg, toggleModal);

const options = [
  {
    label: 'View Profile',
    key: 'View Profile',
    // icon: renderIcon("../src/assets/layout/image/profile.png"),

    props: {
      onClick: () => {
        router.push('/profile')
      }
    },
    icon() {
      return h(NIcon, null, {
        default: () => h(UserCircleRegular)
      })
    }
  },
  /* {
    label: 'My Trips',
    key: 'My Trips',
    icon() {
      return h(NIcon, null, {
        default: () => h(SuitcaseRolling)
      })
    },
    props: {
      onClick: () => {
        router.push('/ticket-history')
      }
    }
  }, */
  /* {
    label: 'TT Coin',
    key: 'TT Coin',
    icon() {
      return h(NIcon, null, {
        default: () => h(Coins)
      })
    },
    props: {
      onClick: () => {
        router.push('/tt-coins')
      }
    }
  }, */
  {
    label: 'Transaction History',
    key: 'Transaction History',
    icon() {
      return h(NIcon, null, {
        default: () => h(Receipt)
      })
    },
    props: {
      onClick: () => {
        router.push('/transaction-history')
      }
    }
  },
  {
    label: 'Sign Out',
    key: 'Sign Out',
    icon() {
      return h(NIcon, null, {
        default: () => h(SignOutAlt)
      })
    },
    props: {
      onClick: () => {
        jwtStore.clearJWT()
        router.push('/')
      }
    }
    // props: {
    //         onClick: () => {
    //           window.location.href = "http://127.0.0.1:8000/logout/"
    //         }
    //       }
  }
]

// const responsiveOptions = [
//   {
//     label: 'Home',
//     key: 'Home',
//   },
//   {
//     label: "About",
//     key: "About",
//   },
//   {
//     key: 'Services',
//     type: 'render',
//     render: renderCollapse(),
//   },
//   {
//     label: 'Contact',
//     key: 'Contact',
//   },
//   {
//     label: 'Blog',
//     key: 'Blog',
//   }
// ]

// function handleSelect(key: string | number) {
//   message.info(String(key));
// }

// function handleSelectResponsive(key: string | number) {
//   message.info(String(key))
// }
</script>

<style scoped>
.navbar-top {
  background: none;
  border: 1px solid white;
}

.navbar-show {
  position: fixed;
  width: 100vw;
  /* box-shadow: 0 2px 15px rgba(71, 120, 120, 0.5); */
  transform: translate3d(0, 0, 0);
  display: flex;
  width: 100%;
  height: 70px;
  justify-content: space-around;
  /* box-shadow: 0px 3px 5px -3px rgba(0, 0, 0, 0.5); */
  align-items: center;
  position: fixed;
  top: 0px;
  z-index: 9;
  opacity: 1;
  background-color: rgba(89, 89, 89, 0.4);
  border-bottom: 1px solid rgba(89, 89, 89, 0);

  color: white;
}
.navbar--hidden {
  box-shadow: none;
  /* transform: translate3d(0, -100%, 0); */
  opacity: 1;
  border-bottom: 1px solid #e8e8e8;
  background-color: white;

  color: black;
}
.tab-button {
  cursor: pointer;
  /* background-image: linear-gradient(90deg, white, white) !important; */
  background-size: 0% 5px !important;
  background-position: left bottom !important;
  line-height: 3.9 !important;
  padding: 0 0.5rem;
}
.active {
  /* color: red !important; */
  background-size: 120% 5px !important;
  /* background-image: linear-gradient(90deg, red, red) !important; */
  background-position: left bottom !important;
  text-decoration: none !important;
  background-repeat: no-repeat !important;
  line-height: 3.9 !important;
  border-radius: 2px;
}

.responsive-menu-dropdown {
  position: absolute;
  font-size: 20px;
  font-family: 'Roboto';
  background-color: white;
  width: 100%;
  box-shadow: 0px 3px 5px -3px rgba(0, 0, 0, 0.5);
  opacity: 0.6;
  display: none;
}

.responsive-menu-dropdown > ul {
  list-style: none;
  margin-block-end: 0;
  margin-block-start: 0;
  /* border-bottom: 2px solid #D9D9D9; */
}

.responsive-menu-dropdown > ul > li {
  /* border-bottom: 1px solid #d9d9d9; */
  border-bottom: 1px solid rgba(177, 177, 177, 0.25);
  padding-top: 15px;
  padding-left: 40px;
  padding-bottom: 15px;

  /* width: 100%; */
}

.responsive-menu-dropdown > ul > li > a {
  text-decoration: none;
  color: black;
}

/* .collaspe-header-link {
  font-size: 20px;
  text-decoration: none;
  color: black;
  font-weight: 100;
} */
/* .collaspe-header-link:hover,
:active,
:focus {
  font-size: 20px;
  text-decoration: none;
  color: var(--tripturbo-red);
} */
.responsive-menu-dropdown > ul > li > a:hover {
  text-decoration: none;
  color: var(--tripturbo-red);
}

.responsive-list-menu-link {
  text-decoration: none;
  color: black;
}

.responsive-list-menu-link:hover {
  text-decoration: none;
  color: var(--tripturbo-red);
}

.back-icon {
  width: 20px;
  height: 20px;
}

.menu-btn {
  display: none;
}

.profile-img {
  object-fit: cover;
  height: 55px;
  width: 55px;
  border-radius: 55px;
  cursor: pointer;
  /* border: 2px solid var(--tripturbo-red); */
}

.modal-title {
  position: relative;
  border-bottom: 1px solid #b1b1b1;
  font-family: 'Roboto';
}

.nav-bar {
  display: flex;
  height: 2rem;
  gap: 2rem;
  font-size: medium;
  font-family: 'Poppins';
  margin: 5px;
  font-weight: 500;
}

.nav-bar > a,
.menu-dropdown > a {
  font-size: 18px;
  text-decoration: none;
}

/* .nav-bar > a:focus,
.menu-dropdown > a:focus {
  font-weight: bold;
  color: var(--tripturbo-red);
  text-decoration: none;
} */

.nav-bar > a:hover,
.menu-dropdown > a:hover {
  color: var(--tripturbo-red);
}

/* .nav-bar>a:active,
.menu-dropdown>a:active {
  color: var(--tripturbo-red);
  font-weight: bolder;
} */

/* .active {
  background-color: red;
} */

.nav-fix {
  position: sticky;
  top: 0;
  overflow: visible;
  width: 100%;
  z-index: 999;
  border-radius: 0%;
}

.dropdown-image {
  width: 12px;
  height: 8px;
  background-color: white;
}

.menu-dropdown {
  position: absolute;
  top: -400px;
  display: grid;
  width: 355px;
  font-weight: 400;
  gap: 10px;
  padding: 24px 20px;
  text-align: inherit;
  text-decoration: none;
  background-color: white;
  border: 0px;
  border-radius: 5px;
  /* box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); */
  box-shadow: 0px 5px 8px -3px rgba(0, 0, 0, 0.75);
  z-index: 50;
  left: -100%;
  opacity: 0.6;
}

.menu-dropdown.show-drop {
  top: 58px;
  opacity: 1;
}

.dropdown-item {
  width: 100%;
  display: flex;
  gap: 16px;
  align-items: center;
  border-bottom: 1px solid rgba(177, 177, 177, 0.25);
  padding-bottom: 10px;
}

.dropdown-item-img {
  max-width: 60px;
  min-width: 60px;
  max-height: 60px;
  padding-right: 3px;
}

.dropdown-item-desc {
  display: flex;
  flex-direction: column;
  text-align: left;
  line-height: normal !important;
}

.item-title {
  font-weight: 600;
  font-size: 16px;
  margin-bottom: 4px;
}

.item-desc {
  font-size: 14px;
  font-weight: 400;
  line-height: 16px;
  color: var(--description-light);
}

@media (max-width: 1165px) {
  .nav-bar {
    gap: 2rem;
  }
}

@media (max-width: 800px) {
  .menu-btn {
    display: block;
  }

  .nav-bar {
    display: none;
  }

  .dropdown-item {
    padding-top: 10px;
  }

  :deep(
      .n-collapse .n-collapse-item .n-collapse-item__content-wrapper .n-collapse-item__content-inner
    ) {
    padding-top: 0px !important;
  }

  .responsive-menu-dropdown {
    left: 0 !important;
    top: -600px !important;
    display: block;
  }

  .responsive-menu-dropdown.show-dropdown {
    top: 70px !important;
    opacity: 1;
  }
}

@media (max-width: 475px) {
  .responsive-menu-dropdown > ul > li {
    padding-top: 10px;
    padding-bottom: 10px;
  }
  .responsive-menu-dropdown > ul > li > p {
    font-size: 16px;
    text-decoration: none;
  }
}
/* @media (max-width : 890px ) {} */
</style>
