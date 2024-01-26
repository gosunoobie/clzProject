import { defineStore } from 'pinia'
// import router from "../router/index";
import BlogType from '../models/Blog.interface'
const homeUrl = import.meta.env.VITE_HOME_BACKEND_API

export const useHomeStore = defineStore('homeStore', {
  state: () => {
    return {
      blogsArr: [] as BlogType[],
      faqsArr: [],
      policiesArr: [],
      termsArr: [],
      showNavbar: true
    }
  },
  getters: {
    getBlogData:
      (state) =>
      (param: string | string[]): BlogType[] => {
        return state.blogsArr.filter((item) => {
          if (Array.isArray(param)) {
            // Handle an array of slugs, returning an array of matching blog posts.
            return param.includes(item.slug)
          } else {
            // Handle a single slug, returning an array with a single matching blog post.
            return item.slug === param
          }
        })
      }
  },

  actions: {
    async getBlogApi() {
      try {
        if (this.blogsArr.length > 0) return
        await fetch(`${homeUrl}/cs/api/blog/`)
          .then((data) => data.json())
          .then((data) => {
            const temp = data.results
            console.log(temp, 'this is store')
            this.blogsArr = [...temp]
          })
      } catch (e) {
        console.log('could not find the data')
      }
    },
    async getFaqsApi() {
      try {
        if (this.faqsArr.length > 0) return
        await fetch(`${homeUrl}/api/faqs/`)
          .then((data) => data.json())
          .then((data) => {
            const temp = data
            console.log(temp, 'this is store')
            this.faqsArr = [...temp]
          })
      } catch (e) {
        console.log('could not find the data')
      }
    },
    async getPoliciesApi() {
      try {
        if (this.policiesArr.length > 0) return
        await fetch(`${homeUrl}/api/policy/`)
          .then((data) => data.json())
          .then((data) => {
            const temp = data
            console.log(temp, 'this is store')
            this.policiesArr = [...temp]
          })
      } catch (e) {
        console.log('could not find the data')
      }
    },
    async getTermsApi() {
      try {
        if (this.termsArr.length > 0) return
        await fetch(`${homeUrl}/api/terms/`)
          .then((data) => data.json())
          .then((data) => {
            const temp = data
            console.log(temp, 'this is store')
            this.termsArr = [...temp]
          })
      } catch (e) {
        console.log('could not find the data')
      }
    }
  }
})
