<template>
  <div v-if="this.$store.state.username">
    <div style="margin: 245px"></div>
    <h1 style="text-align: center;font-size:40px" >Welcome {{this.$store.state.username}} !</h1>
    <div style="margin: 245px"></div>

  </div>
  <div v-else>
    <div style="margin: 150px 0"></div>

    <el-row :gutter="20">
      <el-col :span="5" offset="9">
        <div style=" padding:30px 30px 5px 30px ; box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1) " >
          <el-form size="small" >
            <el-form-item label="用户名" >
              <el-input v-model="username" ></el-input>
            </el-form-item>

            <el-form-item label="密码" >
              <el-input type="password" v-model="password" show-password></el-input>
            </el-form-item>

            <el-form-item>
              <div style="margin-left: 90px">
                <el-button type="primary"
                           plain icon="el-icon-plus"
                           @click="doLogin">提交</el-button>
              </div>
            </el-form-item>
          </el-form>
        </div>
      </el-col>
    </el-row>

    <div style="margin: 150px 0"></div>

  </div>
</template>

<script>
export default {
  data () {
    return {
      username: '',
      password:'',
    }
  },
  methods:{
    doLogin(){
      var that = this;
      this.$axios.request({
        url:this.$url+'login/',
        method:'POST',
        data: {
          username: this.username,
          password: this.password
        },
        responseType:'json'
      }).then(function (response) {
        var code = response.data['code']
        if (code === -1) {
          alert("密码错误！")
        } else {
          that.$store.commit('saveToken', response.data);
        }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
