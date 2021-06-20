<template>
  <div>
    <div style="margin: 30px 0;"></div>
    <div>
      <el-row :gutter="20">
        <el-col :span="17" offset="3">

          <el-input
            type="textarea"
            autosize
            maxlength="50"
            show-word-limit
            placeholder="请输入内容"
            v-model="content">
          </el-input>
        </el-col>
      </el-row>
      <div style="margin: 10px 0;"></div>
      <el-row :gutter="20">

        <el-col :span="2" offset="15">
          <el-input
            type="textarea"
            autosize
            maxlength="5"
            placeholder="奖励值"
            v-model="reward">
          </el-input>
        </el-col>


        <el-col :span="2" offset="1">
          <el-button
            @click="add">添加</el-button>
        </el-col>

      </el-row>
    </div>
    <div style="margin: 30px 0;"></div>
    <el-divider></el-divider>

    <div style="padding: 15px 0"></div>
    <el-row :gutter="20">
      <el-col :span="17" offset="3">
        <el-table
          border="true"
          @cell-click="cellClick"
          :data="dailyList"
          style="width: 100%">
          <el-table-column
            label="未完成日常"
            width="560">
            <template slot-scope="scope" >
              <el-input  v-if="scope.row.id===rowId&&scope.column.label===columnLabel" v-model="scope.row.content" @blur="loseFocus" >
              </el-input>
              <span style="margin-left: 20px" v-else>
                {{ scope.row.content}}
              </span>
            </template>
          </el-table-column>
          <el-table-column
            label="奖励值"
            width="100">
            <template slot-scope="scope">
              <el-input  v-if="scope.row.id===rowId&&scope.column.label===columnLabel" v-model="scope.row.reward" @blur="loseFocus" >
              </el-input>
              <span style="margin-left: 20px" v-else>
                {{ scope.row.reward}}
              </span>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button
                size="mini"
                @click="finishDaily(scope.row.id)">完成</el-button>
              <el-button
                size="mini"
                @click="changeDaily(scope.row.content,scope.row.reward,scope.row.id)">修改</el-button>
              <el-button
                size="mini"
                type="danger"
                @click="changeDaily(-1,-1,scope.row.id)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
    <div style="padding: 20px 0"></div>

    <el-divider></el-divider>
    <div style="padding: 15px 0"></div>
    <el-row :gutter="20">
      <el-col :span="17" offset="3">
        <el-table
          @cell-click="cellClick"
          border="true"
          :data="dailyList_"
          style="width: 100%">
          <el-table-column
            label="已完成日常"
            width="560">
            <template slot-scope="scope">
              <el-input  v-if="scope.row.id===rowId&&scope.column.label===columnLabel" v-model="scope.row.content" @blur="loseFocus" >
              </el-input>
              <span style="margin-left: 20px" v-else>
                {{ scope.row.content}}
              </span>
            </template>
          </el-table-column>
          <el-table-column
            label="奖励值"
            width="100">
            <template slot-scope="scope">
              <el-input  v-if="scope.row.id===rowId&&scope.column.label===columnLabel" v-model="scope.row.reward" @blur="loseFocus" >
              </el-input>
              <span style="margin-left: 20px" v-else>
                {{ scope.row.reward}}
              </span>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button
                size="mini"
                @click="changeDaily(scope.row.content,scope.row.reward,scope.row.id)">修改</el-button>
              <el-button
                size="mini"
                type="danger"
                @click="changeDaily(-1,-1,scope.row.id)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
    <div style="padding: 5px 0"></div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      content: '',
      endTime: '',
      reward: '',
      dailyList: '',
      dailyList_: '',
      rowId: -1,
      columnLabel: ''
    }
  },
  mounted: function () {
    this.getDaily()
    this.getDaily2()

  },
  methods: {
    loseFocus() {
      this.rowId = -1
      this.columnLabel = ''
    },
    cellClick(row, column) {
      this.rowId = row.id
      this.columnLabel = column.label
    },
    add: function () {
      const that = this;
      this.$axios.request({
        url: this.$url + 'buildDaily/',
        method: 'POST',
        data: {
          content: that.content,
          reward: that.reward,
          token: that.$store.state.token
        },
        responseType: 'json'
      }).then(function (response) {
        const code = response.data['code'];
        if (code === '-1') {
          alert("计划创建失败！")
        } else {
          alert('计划创建成功！')
          that.content = ''
          that.reward = ''
          that.getDaily()
        }
      })
    },
    getDaily: function () {
      const that = this;
      this.$axios.request({
        url: this.$url + 'getDaily/',
        method: 'POST',
        data: {
          state: 0,
          token: that.$store.state.token
        },
        responseType: 'json'
      }).then(function (response) {
        that.dailyList = response.data
      })
    },
    getDaily2: function () {
      const that = this;
      this.$axios.request({
        url: this.$url + 'getDaily/',
        method: 'POST',
        data: {
          state: 1,
          token: that.$store.state.token
        },
        responseType: 'json'
      }).then(function (response) {
        that.dailyList_ = response.data
      })
    },
    finishDaily: function (id) {
      const that = this;
      this.$axios.request({
        url: this.$url + 'finishDaily/',
        method: 'POST',
        data: {
          planId: id,
          token: that.$store.state.token
        },
        responseType: 'json'
      }).then(function (response) {
        that.getDaily()
        that.getDaily2()
        that.refresh()
      })
    },
    changeDaily: function (_content,_reward,_id) {
      const that = this;
      this.$axios.request({
        url: this.$url + 'changDaily/',
        method: 'POST',
        data: {
          id: _id,
          content: _content,
          reward: _reward,
          token: that.$store.state.token
        },
        responseType: 'json'
      }).then(function (response) {
        var code =response.data['code']
        if (code!==1)
          alert("修改失败！")
        else
          alert("修改成功！")
        that.getDaily()
        that.getDaily2()
      })
    },
    refresh() {
      const that = this;
      this.$axios.request({
        url: this.$url + 'refresh/',
        method: 'POST',
        data: {
          token: that.$store.state.token
        },
        responseType: 'json'
      }).then(function (response) {
        that.$store.commit('update', response.data);
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
