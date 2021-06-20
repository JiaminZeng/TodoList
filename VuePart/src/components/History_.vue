<template>

  <div>
    <h1>已完成计划:</h1>
    <el-row :gutter="20">
      <el-col :span="19" offset="2">
        <el-table
          border="true"
          :data="finished"
          style="width: 100%">
          <el-table-column
            label="计划内容"
            width="460">
            <template slot-scope="scope">
              <span style="margin-left: 5px">{{ scope.row.content}}</span>
            </template>
          </el-table-column>
          <el-table-column
            label="计划奖励"
            width="100">
            <template slot-scope="scope">
              <span style="margin-left: 5px">{{ scope.row.reward}}</span>
            </template>
          </el-table-column>
          <el-table-column
            label="创建时间"
            width="200">
            <template slot-scope="scope">
              <i class="el-icon-time"></i>
              <span style="margin-left: 5px">{{scope.row.buildTime | timeFilter}}</span>
            </template>
          </el-table-column>
          <el-table-column
            label="完成时间"
            width="200">
            <template slot-scope="scope">
              <i class="el-icon-time"></i>
              <span style="margin-left: 5px">{{ scope.row.endTime |timeFilter  }}</span>
            </template>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
    <el-divider></el-divider>
    <h1>过期计划:</h1>
    <el-row :gutter="20">
      <el-col :span="19" offset="2">
        <el-table
          border="true"
          :data="unfinished"
          style="width: 100%">
          <el-table-column
            label="计划内容"
            width="460">
            <template slot-scope="scope">
              <span style="margin-left: 5px">{{ scope.row.content}}</span>
            </template>
          </el-table-column>
          <el-table-column
            label="计划奖励"
            width="100">
            <template slot-scope="scope">
              <span style="margin-left: 5px">{{ scope.row.reward}}</span>
            </template>
          </el-table-column>
          <el-table-column
            label="创建时间"
            width="200">
            <template slot-scope="scope">
              <i class="el-icon-time"></i>
              <span style="margin-left: 5px">{{scope.row.buildTime | timeFilter}}</span>
            </template>
          </el-table-column>
          <el-table-column
            label="过期时间"
            width="200">
            <template slot-scope="scope">
              <i class="el-icon-time"></i>
              <span style="margin-left: 5px">{{ scope.row.endTime |timeFilter  }}</span>
            </template>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
    <el-divider></el-divider>
    <h1>兑换历史:</h1>
    <el-row :gutter="20">
      <el-col :span="19" offset="2">
        <el-table
          border="true"
          :data="exchangeHistory"
          style="width: 100%">
          <el-table-column
            label="兑换物名称"
            width="460">
            <template slot-scope="scope">
              <span style="margin-left: 5px">{{ scope.row.content}}</span>
            </template>
          </el-table-column>
          <el-table-column
            label="兑换花费"
            width="200">
            <template slot-scope="scope">
              <span style="margin-left: 5px">{{ scope.row.cost}}</span>
            </template>
          </el-table-column>
          <el-table-column
            label="兑换时间"
            width="300">
            <template slot-scope="scope">
              <i class="el-icon-time"></i>
              <span style="margin-left: 5px">{{ scope.row.buildTime |timeFilter  }}</span>
            </template>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      finished: '',
      unfinished: '',
      exchangeHistory: '',
    }
  },
  mounted: function () {
    this.getPlan1()
    this.getPlan2()
    this.getChangeHistory()
  },
  filters: {
    timeFilter: function (value) {
      value=value.replace('T', ' ')
      value=value.replace('Z', ' ')
      return value
    }
  },
  methods: {
    getPlan1: function () {
      const that = this;
      this.$axios.request({
        url: this.$url + 'getPlan/',
        method: 'POST',
        data: {
          state: 1,
          token: that.$store.state.token
        },
        responseType: 'json'
      }).then(function (response) {
        that.finished = response.data

      })
    },
    getPlan2: function () {
      const that = this;
      this.$axios.request({
        url: this.$url + 'getPlan/',
        method: 'POST',
        data: {
          state: 2,
          token: that.$store.state.token
        },
        responseType: 'json'
      }).then(function (response) {
        that.unfinished = response.data
      })
    },
    getChangeHistory: function () {
      const that = this;
      this.$axios.request({
        url: this.$url + 'getChangeHistory/',
        method: 'POST',
        data: {
          token: that.$store.state.token
        },
        responseType: 'json'
      }).then(function (response) {
        that.exchangeHistory = response.data
      })
    },
  }
}
</script>

<style scoped>
  h1 {
    margin-left: 60px;
  }
</style>
