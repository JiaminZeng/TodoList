import Vue from 'vue'
import Router from 'vue-router'
import Login from "../components/Login"
import Register from "../components/Register"
import Plan from "../components/Plan";
import Daily from "../components/Daily";
import Thing from "../components/Thing";
import History_ from "../components/History_";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path:'/',
      redirect:'Login'
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/plan',
      name: 'Plan',
      component: Plan
    },
    {
      path: '/daily',
      name: 'Daily',
      component: Daily
    },
    {
      path: '/thing',
      name: 'Thing',
      component: Thing
    },
    {
      path: '/history',
      name: 'History',
      component: History_
    },
  ],
  mode: 'history'
})

