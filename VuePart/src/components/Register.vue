<template>
  <div >

    <el-row :gutter="20">
      <div style="margin: 100px 0"></div>
      <el-col :span="5" offset="9">
        <div style=" padding:30px 30px 5px 30px ; box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1) " >
      <el-form size="small" >
        <el-form-item label="用户名" >
          <el-input v-model="username" ></el-input>
        </el-form-item>

        <el-form-item label="密码" >
          <el-input type="password" v-model="password" show-password></el-input>
        </el-form-item>

        <el-form-item label="确认密码">
          <el-input type="password"  v-model="repeatPassword" show-password></el-input>
        </el-form-item>

        <el-form-item>
          <div style="margin-left: 88px">
          <el-button type="primary"
                     plain icon="el-icon-plus"
                     @click="DoRegister">提交</el-button>
          </div>
        </el-form-item>
      </el-form>
      </div>
      </el-col>
    </el-row>
    <div style="margin: 120px 0"></div>


  </div>
</template>

<script>
export default {
  data () {
    return {
      username: '',
      password: '',
      repeatPassword: '',
    }
  },
  methods:{
    DoRegister(){
      var that = this;
      if (this.repeatPassword !== this.password) {
        alert("密码不一致");
        this.username = ''
        this.repeatPassword = ''
        return
      }
      this.$axios.request({
        url : this.$url+'register/',
        method: 'POST',
        data: {
          username: this.username,
          password: this.password,
        },
        responseType:'json'
      }).then(function (response) {
        var code =  response.data['code']
        if(code ===-1) {
          alert("用户已存在，注册失败！")
          return
        }
        alert("注册成功！")
        that.$store.commit('saveToken', response.data);
      })
    }
  }
}
</script>

<style scoped>

</style>
