<template>
    <div id="app">
      <navBar v-if="authToken && authUser.email && authUser.role"></navBar>
      <sideBar v-if="authToken && authUser.email && authUser.role"></sideBar>
    <router-view></router-view>
  </div>
</template>

<script>
import navBar from '@/components/navBar.vue'
import sideBar from '@/components/sideBar.vue'
import { mapState } from "vuex"

export default {
  name: 'App',
  components: {
    navBar,
    sideBar,
  },
  computed:{
    ...mapState(['authToken', 'authUser'])
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
