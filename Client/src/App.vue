<template>
  <div id="app">
    <NavBar />
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
  </div>
</template>


<script>
import NavBar from "./components/NavBar";

export default {
  name: "App",
  components: { NavBar },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  font-weight: bold;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin-top: 0px;
}
</style>
