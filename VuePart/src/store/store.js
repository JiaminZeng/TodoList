import Vue from 'vue'
import Vuex from 'vuex'
import Cookie from 'vue-cookies'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
      username: Cookie.get('username'),
      token: Cookie.get('token'),
      remainingRewards: Cookie.get('remainingRewards'),
      totalDailyTasks: Cookie.get('totalDailyTasks'),
      totalPlanTasks: Cookie.get('totalPlanTasks')
    },
    mutations: {
      saveToken: function (state, data) {
        state.username = data.username;
        state.token = data.token;
        state.remainingRewards = data.remainingRewards;
        state.totalDailyTasks = data.totalDailyTasks;
        state.totalPlanTasks = data.totalPlanTasks;

        Cookie.set('username', data.username, '20min');
        Cookie.set('token', data.token, '20min');
        Cookie.set('remainingRewards', data.remainingRewards, '60min');
        Cookie.set('totalDailyTasks', data.totalDailyTasks, '60min');
        Cookie.set('totalPlanTasks', data.totalPlanTasks, '60min');
      },
      clearToken: function (state) {
        state.username = null;
        state.token = null;
        state.remainingRewards = null;
        state.totalDailyTasks = null;
        state.totalPlanTasks = null;

        Cookie.remove('username');
        Cookie.remove('token');
        Cookie.remove('remainingRewards');
        Cookie.remove('totalDailyTasks');
        Cookie.remove('totalPlanTasks');
      },
      update: function (state, data) {
        state.remainingRewards = data.remainingRewards;
        state.totalDailyTasks = data.totalDailyTasks;
        state.totalPlanTasks = data.totalPlanTasks;
        Cookie.set('remainingRewards', data.remainingRewards, '60min');
        Cookie.set('totalDailyTasks', data.totalDailyTasks, '60min');
        Cookie.set('totalPlanTasks', data.totalPlanTasks, '60min');
      }
    }
  }
)
