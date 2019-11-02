
<template>
  <div class="home">
    <h3>50以下</h3>
    <el-table :data="data1" style="width: 100%">
      <el-table-column prop="店铺名称" label="店铺名称"/>
      <el-table-column prop="评分" label="评分" />
      <el-table-column prop="平均价格" label="平均价格" />
      <el-table-column prop="详细地址" label="详细地址" />
    </el-table>
    <h3>50-100</h3>
    <el-table :data="data2" style="width: 100%">
      <el-table-column prop="店铺名称" label="店铺名称"/>
      <el-table-column prop="评分" label="评分" />
      <el-table-column prop="平均价格" label="平均价格" />
      <el-table-column prop="详细地址" label="详细地址" />
    </el-table>
    <h3>100-200</h3>
    <el-table :data="data3" style="width: 100%">
      <el-table-column prop="店铺名称" label="店铺名称"/>
      <el-table-column prop="评分" label="评分" />
      <el-table-column prop="平均价格" label="平均价格" />
      <el-table-column prop="详细地址" label="详细地址" />
    </el-table>
    <h3>200以上</h3>
    <el-table :data="data4" style="width: 100%">
      <el-table-column prop="店铺名称" label="店铺名称"/>
      <el-table-column prop="评分" label="评分" />
      <el-table-column prop="平均价格" label="平均价格" />
      <el-table-column prop="详细地址" label="详细地址" />
    </el-table>

  </div>
</template>

<script>
  /* eslint-disable */
  // @ is an alias to /src
  import G2 from "@antv/g2"
  import axios from "axios"
  import consts from "@/assets/consts"
  export default {
    name: 'data2',
    components: {

    },
    data () {
      return {
        data1: null,
        data2: null,
        data3: null,
        data4: null

      }
    },
    methods: {

    },
    mounted() {
      axios.get(consts.apiBase + "data/2").then((response) => {
        this.data1 = response.data["<50"].slice(0,5);
        this.data2 = response.data["50-100"].slice(0,5);
        this.data3 = response.data["100-200"].slice(0,5);
        this.data4 = response.data[">200"].slice(0,5);
      })

    }
  }
</script>


