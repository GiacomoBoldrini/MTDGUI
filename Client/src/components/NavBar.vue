<template>
  <nav class="navbar-is-link" role="navigation" aria-label="main navigation">
    <router-link to="/vue" class="navbar-item" active-class="is-active"
      >Vue</router-link
    >
    <router-link to="/webgui-main" class="navbar-item" active-class="is-active"
      >Web GUI</router-link
    >
    <router-link to="/dqm" class="navbar-item" active-class="is-active"
      >DQM</router-link
    >
    <router-link to="/runreg" class="navbar-item" active-class="is-active"
      >Run Registry</router-link
    >
    <router-link to="/service" class="navbar-item" active-class="is-active"
      >Services</router-link
    >
    <router-link to="/runconf" class="navbar-item" active-class="is-active"
      >RunKeys</router-link
    >
  </nav>
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
  margin: auto;
  margin-top: 0%;
  padding: 1%;
  display: flex;
  justify-content: space-between;
}

.navbar-item {
  color: white;
  padding-left: 5%;
  padding-right: 5%;
  position: relative;
  display: flex;
  text-decoration: none;
}
</style>
