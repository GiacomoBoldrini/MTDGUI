<template>
  <nav class="navbar-is-link" role="navigation" aria-label="main navigation">
    <router-link to="/vue" class="navbar-item" active-class="is-active"
      >VueJS</router-link
    >
    <router-link to="/webgui-main" class="navbar-item" active-class="is-active"
      >Web GUI</router-link
    >
    <router-link to="/webcam" class="navbar-item" active-class="is-active"
      >Webcam</router-link
    >
    <router-link to="/dqm" class="navbar-item" active-class="is-active"
      >DQM</router-link
    >
    <router-link
      to="/trigger"
      class="navbar-item"
      active-class="is-active"
      v-if="isCompleteGui"
      >Trigger</router-link
    >
    <router-link
      to="/power"
      class="navbar-item"
      active-class="is-active"
      v-if="isCompleteGui"
      >Power</router-link
    >
  </nav>
</template>

<script>

export default {
  name: 'NavBar',
  data() {
    return {
      isCompleteGui: false,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.navbar-is-link {
    background-color: #1E90FF;
    margin: auto;
    margin-top: 0%;
    padding: 1%;
    display: flex;
    justify-content:space-between;
}

.navbar-item{
    color: white;
    padding-left: 5%;
    padding-right: 5%;
    position:relative;
    display: flex;
    text-decoration:none;
}
</style>
