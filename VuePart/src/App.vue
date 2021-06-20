<template>
  <div id="app">
    <div>
      <el-container>
        <el-header>
          <div v-if="this.$store.state.username">
            <el-row :gutter="20" class="el-font">
              <el-col :span="3" offset="10">用户名： <a>{{ this.$store.state.username }}</a></el-col>
              <el-col :span="3">奖励值：<a>{{ this.$store.state.remainingRewards }}</a></el-col>
              <el-col :span="3">总完成计划数：<a>{{ this.$store.state.totalPlanTasks }}</a></el-col>
              <el-col :span="3">总完成日常数：<a>{{ this.$store.state.totalDailyTasks }}</a></el-col>
              <el-col :span="2"><el-button type="primary" plain icon="el-icon-circle-close" ><a @click="logout"><router-link to="/login">注销</router-link></a></el-button></el-col>
            </el-row>

          </div>
          <div v-else>
            <el-row :gutter="20" >

              <el-col :span="2" :offset="20">
                <el-button type="primary" plain icon="el-icon-user" ><router-link to="/login">登录</router-link></el-button>
              </el-col>

              <el-col :span="1" >
                <el-button type="primary" plain icon="el-icon-circle-plus-outline" ><router-link to="/register">注册</router-link></el-button>
              </el-col>

            </el-row>

          </div>
        </el-header>

        <el-container >
          <el-aside width="200px" v-if="this.$store.state.username">
            <el-menu
              class="el-menu-vertical-demo"
              text-color="#99a9bf"
              router ="true"
              active-text-color="#99a9bf">
              <el-menu-item index="/plan">计&nbsp;&nbsp;划</el-menu-item>
              <el-menu-item index="/daily">日&nbsp;&nbsp;常</el-menu-item>
              <el-menu-item index="/thing">兑&nbsp;&nbsp;换</el-menu-item>
              <el-menu-item index="/history">历&nbsp;&nbsp;史</el-menu-item>

            </el-menu>
          </el-aside>

          <el-main >
            <router-view/>
          </el-main>

        </el-container>
      </el-container>
      <el-footer>
        <Timer></Timer>
      </el-footer>
    </div>


  </div>
</template>

<script>
import Timer from "./components/Timer";

export default {

  components:{Timer},
  name: 'App',
  data() {
    return {

    }
  },
  methods: {
    logout( ) {
      const that = this;
      that.$store.commit('clearToken');
    }
  }
}
</script>

<style>
    .el-header, .el-footer {
      background-color: #B3C0D1;
      color: #333;
      text-align: center;
      line-height: 60px;
    }

    .el-aside {
      background-color: #D3DCE6;
      color: #333;
      text-align: center;
    }

    .el-main {
      background-color: #E9EEF3;
      color: #333;
    }

    body > .el-container {
      margin-bottom: 40px;
    }

    .el-font {
      font-size: 18px;
      font-family: Arial,sans-serif;
    }
    .bg-purple-dark {
      background: #99a9bf;
    }
</style>
