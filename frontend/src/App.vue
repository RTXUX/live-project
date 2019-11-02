<template>
  <div id="app">
    <div id="nav">
      <router-link to="/type/1">最受欢迎商圈</router-link> |
      <router-link to="/type/2">性价比最高店铺</router-link> |
      <router-link to="/type/3">美食聚集地</router-link> |
      <router-link to="/type/4">服饰</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>

export default {
  name: 'app',
  components: {
  }
}
</script>

<style>

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
