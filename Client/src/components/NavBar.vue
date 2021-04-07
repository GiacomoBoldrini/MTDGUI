<template>
  <div>
    <nav class="navbar-is-link" role="navigation" aria-label="main navigation">
      <router-link to="/vue" class="navbar-item">Vue</router-link>
      <router-link to="/webgui" class="navbar-item">Web GUI</router-link>
      <router-link to="/dqm" class="navbar-item">DQM</router-link>
      <router-link to="/runreg" class="navbar-item">Run Registry</router-link>
      <router-link to="/service" class="navbar-item">Services</router-link>
      <router-link to="/runconf" class="navbar-item">RunKeys</router-link>
    </nav>

    <keep-alive include="webgui">
      <router-view></router-view>
    </keep-alive>
  </div>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.navbar-is-link {
  background-color: #1e90ff;
  height: 50px;
}

.navbar-item {
  float: left;
  padding: 12px;
  color: white;
  text-decoration: none;
  font-size: 17px;
  width: 16%;
  text-align: center;
  color: white;
}

.navbar-item:hover {
  color: #1e90ff;
  background-color: white;
  text-align: center;
  height: 100%;
  align-items: center;
  justify-content: center;
  justify-content: space-between;
}

.router-link-exact-active,
.router-link-active {
  color: #1e90ff;
  background-color: white;
  text-align: center;
  height: 100%;
  align-items: center;
  justify-content: center;
  justify-content: space-between;
}
</style>
