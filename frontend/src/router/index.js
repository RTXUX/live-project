import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/type/1',
    name: 'type1',
    component: Home
  },
  {
    path: '/type/2',
    name: 'data2',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Data2.vue')
  },
  {
    path: '/type/3',
    name: 'data3',
    component: ()=> import('../views/Data3.vue')
  },
  {
    path: '/type/4',
    name: 'data4',
    component: () => import('../views/Data4.vue')
  }
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
