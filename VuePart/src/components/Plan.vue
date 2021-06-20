<template>
  <div>
    <div>
      <div style="margin: 30px 0;"></div>

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

        <el-col :span="2" offset="10">
          <el-input
            type="textarea"
            autosize
            maxlength="5"
            placeholder="奖励值"
            v-model="reward">
          </el-input>
        </el-col>

        <el-col :span="3" offset="1">
          <el-date-picker
            v-model="endTime"
            type="datetime"
            size="small"
            value-format="yyyy-MM-dd HH:mm:ss"
            placeholder="选择日期时间">
          </el-date-picker>
<!--          <timer-picker v-model="endTime"></timer-picker>-->
        </el-col>

        <el-col :span="2" offset="2">
          <el-button
            @click="add">添加</el-button>
        </el-col>

      </el-row>
    </div>
    <div style="margin: 30px 0;"></div>

    <el-divider></el-divider>

    <el-row :gutter="20">
      <div style="margin: 50px 0;"></div>
      <el-col :span="17" offset="3">
        <el-table
          border="true"
          @cell-click="cellClick"
          :data="planList"
          style="width: 100%">
          <el-table-column
            label="计划内容"
            width="340">
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
            width="80">
            <template slot-scope="scope">
              <el-input
                v-if="scope.row.id===rowId&&scope.column.label===columnLabel" v-model="scope.row.reward" @blur="loseFocus" >
              </el-input>
              <span style="margin-left: 20px" v-else>
                {{ scope.row.reward}}
              </span>
            </template>
          </el-table-column>
          <el-table-column
            label="截止日期"
            width="250">
            <template slot-scope="scope">
              <el-date-picker
                v-if="scope.row.id===rowId&&scope.column.label===columnLabel"
                @blur="loseFocus"
                v-model="scope.row.endTime"
                type="datetime"
                size="small"
                value-format="yyyy-MM-dd HH:mm:ss"
                placeholder="选择日期时间">
              </el-date-picker>
              <span style="margin-left: 5px" v-else>{{ scope.row.endTime}}</span>

            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button
                size="mini"
                @click="finishPlan(scope.row.id)">完成</el-button>
              <el-button
                size="mini"
                @click="changePlan(scope.row.content,scope.row.reward,scope.row.endTime,scope.row.id)">修改</el-button>
              <el-button
                size="mini"
                type="danger"
                @click="changePlan(-1,-1,-1,scope.row.id)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
    <div style="margin: 50px 0;"></div>


    <div style="padding: 85px 20px">

    </div>
  </div>
</template>

<script>
import TimerPicker from "./TimerPicker";

export default {
  data() {
    return {
      content: '',
      endTime: '',
      reward: '',
      planList: '',
      rowId: -1,
      columnLabel: ''
    }
  },
  components:{TimerPicker},
  mounted: function () {
    this.getPlan()
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
        url: this.$url + 'buildPlan/',
        method: 'POST',
        data: {
          content: that.content,
          // endTime:moment().utc().format('YYYY-MM-DD HH:mm:ss'),
          endTime: that.endTime,
          reward: that.reward,
          token: that.$store.state.token
        },
        responseType: 'json'
      }).then(function (response) {
        const code = response.data['code'];
        if (code === -1) {
          alert("计划创建失败！")
        } else {
          alert('计划创建成功！')
          that.content = ''
          that.endTime = ''
          that.reward = ''
          that.getPlan()
        }
      })
    },
    getPlan: function () {
      const that = this;
      this.$axios.request({
        url: this.$url + 'getPlan/',
        method: 'POST',
        data: {
          state: 0,
          token: that.$store.state.token
        },
        responseType: 'json'
      }).then(function (response) {
        that.planList = response.data
        for(let i=0;i<that.planList.length;i++) {
          that.planList[i].endTime=that.planList[i].endTime.replace('Z',' ')
          that.planList[i].endTime=that.planList[i].endTime.replace('T',' ')
        }

        that.forEach(element => {
          element["show"] = false
        });

      })
    },
    finishPlan: function (id) {
      const that = this;
      this.$axios.request({
        url: this.$url + 'finishPlan/',
        method: 'POST',
        data: {
          planId: id,
          token: that.$store.state.token
        },
        responseType: 'json'
      }).then(function (response) {
        that.getPlan()
        that.refresh()
      })
    },
    changePlan: function (_content,_reward,_endTime,_id) {
      const that = this;
      this.$axios.request({
        url: this.$url + 'changePlan/',
        method: 'POST',
        data: {
          id: _id,
          content: _content,
          reward: _reward,
          endTime: _endTime,
          token: that.$store.state.token
        },
        responseType: 'json'
      }).then(function (response) {
        var code =response.data['code']
        if (code!==1)
          alert("修改失败！")
        else
          alert("修改成功！")
        that.getPlan()
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
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-carousel__item h3 {
  color: #475669;
  font-size: 18px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}
</style>
