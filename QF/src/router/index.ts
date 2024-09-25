import { createRouter, createWebHistory } from 'vue-router'
import Q from '../views/Q.vue'

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
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      props: (route) => ({ st: route.query.st, in: route.query.in, ot: route.query.ot, sz: route.query?.sz, sg: route.query?.sg }),
      component: () => import('../views/QF.vue')
    },
    {
      path: '/qvpn',
      name: 'qvpn',
      component: () => import('../views/QVPN.vue'),
      props: (route) => ({ url: route.query.url }),
    }
  ]
})

export default router
