import {
  createRouter,
  createWebHistory,
  type NavigationGuardNext,
  type RouteLocationNormalized
} from 'vue-router'
import { useJwtStore } from '../stores/jwt'

const authenticatedRoutes: string[] = ['Profile']

const router = createRouter({
  scrollBehavior(_, __, ___) {
    // always scroll to top
    return { top: 0 }
  },
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('../views/LandingPage.vue')
    },

    {
      path: '/login',
      name: 'Login',
      component: () => import('../views/LandingPage.vue')
    },
    {
      path: '/flights',
      name: 'FlightList',
      component: () => import('@/views/DomesticFlights/FlightLists.vue')
    },

    {
      path: '/profile',
      name: 'Profile',
      component: () => import('@/views/Accounts/ProfilePage.vue')
    },

    {
      path: '/flights/:id',
      name: 'FlightDetail',
      component: () => import('../views/DomesticFlights/FlightDetail.vue')
    }

    /* {
      path: '/redirect-error',
      name: 'RedirectPage',
      component: () => import('../views/RedirectPage.vue')
    }, */

    /* {
      name: 'notfound',
      path: '/:pathMatch(.*)*',
      component: () => import('../views/NotFound.vue')
    } */
  ]
})

export default router

export async function WaitUntilRefreshed(): Promise<void> {
  const JwtStore = useJwtStore()
  while (JwtStore.RefreshingToken) {
    await new Promise((resolve) => setTimeout(resolve, 100))
  }
}

router.beforeEach(
  async (to: RouteLocationNormalized, _: RouteLocationNormalized, next: NavigationGuardNext) => {
    const JwtStore = useJwtStore()

    if (to.name == 'Login' || to.name == 'Register') {
      await WaitUntilRefreshed()
      if (JwtStore.loggedIn) {
        next({ name: 'Home' })
      } else {
        next()
      }
    } else if (authenticatedRoutes.includes(to.name)) {
      await WaitUntilRefreshed()
      if (JwtStore.loggedIn) {
        next()
      } else {
        next({ name: 'NotFound' })
      }
    } else {
      next()
    }
  }
)
