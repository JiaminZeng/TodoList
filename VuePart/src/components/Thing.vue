<template>
  <div>
    <div style="margin: 30px 0;"></div>
    <div>
      <el-row :gutter="40">
        <el-col :span="5" offset="5">

          <el-input
            type="textarea"
            autosize
            maxlength="10"
            show-word-limit
            placeholder="请输入兑换物名称"
            v-model="content">
          </el-input>
        </el-col>
        <el-col :span="4" offset="2">
          <el-input
            type="textarea"
            autosize
            maxlength="4"
            placeholder="请输入消耗值"
            v-model="cost">
          </el-input>
        </el-col>
        <el-col :span="2" offset="1">
          <el-button
            size="small"
            @click="add">添加</el-button>
        </el-col>
      </el-row>
      <div style="margin: 10px 0;"></div>
    </div>
    <div style="margin: 40px 0;"></div>

    <el-divider></el-divider>
    <div style="margin: 50px 0;"></div>
    <el-row :gutter="20">
      <el-col :span="14" offset="5">
        <el-table
          @cell-click="cellClick"
          border="true"
          :data="thingList"
          style="width: 100%">
          <el-table-column
            label="兑换物"
            width="260">
            <template slot-scope="scope">
              <el-input  v-if="scope.row.id===rowId&&scope.column.label===columnLabel" v-model="scope.row.content" @blur="loseFocus" >
              </el-input>
              <span style="margin-left: 20px" v-else>
                {{ scope.row.content}}
              </span>
            </template>
          </el-table-column>
          <el-table-column
            label="花费"
            width="100">
            <template slot-scope="scope">
              <el-input  v-if="scope.row.id===rowId&&scope.column.label===columnLabel" v-model="scope.row.cost" @blur="loseFocus" >
              </el-input>
              <span style="margin-left: 5px" v-else>
                {{ scope.row.cost}}
              </span>
            </template>
          </el-table-column>
          <el-table-column
            label="总兑换次数"
            width="100">
            <template slot-scope="scope">
              <span style="margin-left: 5px">{{ scope.row.totalGet}}</span>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button
                size="mini"
                @click="exchangeAction(scope.row.id)">兑换</el-button>
              <el-button
                size="mini"
                @click="changeThing(scope.row.content,scope.row.cost,scope.row.id)">修改</el-button>
              <el-button
                size="mini"
                type="danger"
                @click="changeThing(-1,-1,scope.row.id)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
    <div style="margin: 284px 0;"></div>


  </div>
</template>

<script>
export default {
  data() {
    return {
      content: '',
      cost:'',
      thingList: '',
      rowId: -1,
      columnLabel: ''
    }
  },
  mounted: function () {
    this.getThing()
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
        url: this.$url + 'createThing/',
        method: 'POST',
        data: {
          content: that.content,
          cost: that.cost,
          token: that.$store.state.token
        },
        responseType: 'json'
      }).then(function (response) {
        const code = response.data['code'];
        if (code === -1) {
          alert("物品添加失败！")
        } else {
          alert('物品添加成功！')
          that.content = ''
          that.cost = ''
          that.getThing()
        }
      })
    },
    getThing: function () {
      const that = this;
      this.$axios.request({
        url: this.$url + 'getThing/',
        method: 'POST',
        data: {
          token: that.$store.state.token
        },
        responseType: 'json'
      }).then(function (response) {
        that.thingList = response.data
      })
    },
    exchangeAction: function (id) {
      const that = this;
      this.$axios.request({
        url: this.$url + 'exchangeAction/',
        method: 'POST',
        data: {
          id: id,
          token: that.$store.state.token
        },
        responseType: 'json'
      }).then(function (response) {
        var code =response.data['code']
        if (code!==1)
          alert("兑换失败！")
        that.getThing()
        that.refresh()
      })
    },
    changeThing: function (_content,_cost,_id) {
      const that = this;
      this.$axios.request({
        url: this.$url + 'changeThing/',
        method: 'POST',
        data: {
          id: _id,
          content: _content,
          cost: _cost,
          token: that.$store.state.token
        },
        responseType: 'json'
      }).then(function (response) {
        var code =response.data['code']
        if (code!==1)
          alert("修改失败！")
        else
          alert("修改成功！")
        that.getThing()
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
