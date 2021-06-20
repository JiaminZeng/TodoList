<template>
  <div class="block">
    <el-date-picker
      v-model="value1"
      type="datetime"
      value-format="yyyy-MM-dd HH:mm:ss"
      placeholder="选择日期时间">
    </el-date-picker>
  </div>
</template>

<script>
export default {
  data() {
    return {
      value1: '',
    };
  },
  props:['value'],
  methods:{
      back() {
        this.$emit('input',this.value1)
      }
  },
  watch: {
    value1: function () {
      this.back()
    }
  }
};
</script>
