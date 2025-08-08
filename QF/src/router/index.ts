import { createRouter, createWebHistory } from 'vue-router'
import Q from '@/views/Q.vue'
import QF from '@/views/QF.vue'
import QVPN from '@/views/QVPN.vue'
import QAPI from '@/views/QAPI.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Q
    },
    {
      path: '/get',
      name: 'get',
      props: (route) => ({ st: route.query.st, in: route.query.in, ot: route.query.ot, sz: route.query?.sz, sg: route.query?.sg }),
      component: QF
    },
    {
      path: '/api',
      name: 'api',
      component: QAPI
    },
    {
      path: '/qvpn',
      name: 'qvpn',
      component: QVPN,
      props: (route) => ({ url: route.query.url }),
    }
  ],
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
      }
    }
    return { top: 0 }
  },
})

export default router
