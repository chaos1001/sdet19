import Vue from 'vue'
import App1 from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import api from './api/api'

Vue.config.productionTip = false
// 将管理api的api.js和vue关联起来
Vue.prototype.$api = api

new Vue({
  vuetify,
  router,
  render: h => h(App1)
}).$mount('#app')
