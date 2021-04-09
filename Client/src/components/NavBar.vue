<template>
  <div>
    <nav
      class="navbar-is-link"
      role="navigation"
      aria-label="main navigation"
      id="topnav"
    >
      <router-link to="/vue" id="navbarI" class="navbar-item">Vue</router-link>
      <router-link to="/webgui" id="navbarI" class="navbar-item">Web GUI</router-link>
      <router-link to="/dqm" id="navbarI" class="navbar-item">DQM</router-link>
      <router-link to="/runreg" id="navbarI" class="navbar-item">Run Registry</router-link>
      <router-link to="/service" id="navbarI" class="navbar-item">Services</router-link>
      <router-link to="/runconf" id="navbarI" class="navbar-item">RunKeys</router-link>
      <router-link to="" class="dropdown-icon" @click.native="toogleBar()"
        >&#9776;</router-link
      >
    </nav>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  methods: {
    toogleBar() {
      const x = document.getElementById("topnav");
      if (x.className === "navbar-is-link") {
        x.className += " responsive";
      } else {
        x.className = "navbar-is-link";
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.navbar-is-link {
  background-color: #1e90ff;
  height: 50px;
}

.navbar-item,
.dropdown-icon {
  float: left;
  padding: 12px;
  color: white;
  text-decoration: none;
  font-size: 17px;
  width: 16%;
  text-align: center;
}

.navbar-item:hover,
.dropdown-icon:hover,
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

.dropdown-icon {
  display: none;
}

@media only screen and (min-width: 0px) and (max-width: 800px) {
  .navbar-item {
    display: none;
  }

  .dropdown-icon {
    display: block;
    float: right;
  }

}
</style>
