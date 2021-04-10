<template>
  <div>
    <nav
      class="navbar-is-link"
      role="navigation"
      aria-label="main navigation"
      id="topnav"
    >
      <ul class="theList">
        <li>
          <router-link
            to=""
            class="dropdown-icon neverActive"
            @click.native="toogleBar()"
            >&#9776;</router-link
          >
        </li>
        <li><router-link to="/vue" class="navbar-item">Vue</router-link></li>
        <li>
          <router-link to="/webgui" class="navbar-item">Web GUI</router-link>
        </li>
        <li><router-link to="/dqm" class="navbar-item">DQM</router-link></li>
        <li>
          <router-link to="/runregistry" class="navbar-item"
            >Run Registry</router-link
          >
        </li>
        <li>
          <router-link to="/service" class="navbar-item">Services</router-link>
        </li>
        <li>
          <router-link to="/runconf" class="navbar-item">RunKeys</router-link>
        </li>
      </ul>
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
  margin: 0 0;
  margin-bottom: 2%;
  padding: 0 0;
}

.theList {
  display: block;
  list-style: none;
  padding: 0 0;
  margin: 0 0;
}

.navbar-item,
.dropdown-icon {
  float: left;
  padding: 12px;
  color: white;
  text-decoration: none;
  font-size: 20px;
  width: 16.66%;
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

@media only screen and (min-width: 0px) and (max-width: 900px) {
  .navbar-item {
    display: none;
  }

  .dropdown-icon,
  .dropdown-icon:hover {
    display: block;
    width: 100%;
    text-align: right;
  }

  nav.navbar-is-link.responsive {
    height: 200px;
  }

  nav.navbar-is-link.responsive ul.theList li a.navbar-item:hover,
  .router-link-exact-active,
  .router-link-active {
    color: #1e90ff;
    background-color: white;
  }

  nav.navbar-is-link.responsive ul.theList li a.neverActive,
  nav.navbar-is-link ul.theList li a.neverActive {
    color: white;
    background-color: #1e90ff;
  }

  nav.navbar-is-link.responsive ul.theList li a.navbar-item {
    display: block;
    float: none;
    padding: 0 0;
    text-decoration: none;
    font-size: 17px;
    width: 100%;
    text-align: center;
    height: 15%;
  }

  nav.navbar-is-link.responsive ul.theList li a.dropdown-icon {
    display: block;
    width: 100%;
  }

  nav.navbar-is-link.responsive ul.theList {
    display: inline;
  }
}
</style>
