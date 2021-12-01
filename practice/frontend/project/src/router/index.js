import Vue from 'vue'
import VueRouter from 'vue-router'
import Task from '../views/Task.vue'
import Layout from '../views/Layout.vue'
import Testcase from '../views/Testcase.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    // 重定向
    redirect: "/layout"
  },
  {
    path: '/layout',
    name: 'Layout',
    component: Layout,
    children:[
      {
        path: '/task',
        name: 'Task',
        component: Task,
      },
      {
        path: '/testcase',
        name: 'Testcase',
        component: Testcase,
      }
    ]
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
