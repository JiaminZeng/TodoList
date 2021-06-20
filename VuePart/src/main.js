// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store/store' //vuex
import axios from 'axios'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);
Vue.prototype.$axios = axios;
Vue.prototype.$url = 'http://127.0.0.1:8000/';
Vue.config.productionTip = false;
/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,   //vuex
  router,
  components: { App},

  template: '<App/>'
});
