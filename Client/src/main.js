// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";

// socket
// import io from "socket.io-client";
// import VueSocketIOExt from "vue-socket.io-extended";

import { BootstrapVue, IconsPlugin, BootstrapVueIcons } from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";


import App from "./App";
import router from "./router";
import Graph from "./components/dqm";

Vue.component("graph-chart", Graph);

Vue.config.productionTip = false;
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(BootstrapVueIcons);


// const socket = io("http://127.0.0.1:5000/");
// Vue.use(VueSocketIOExt, socket);

/* eslint-disable no-new */
new Vue({
  el: "#app",
  router,
  components: { App },
  template: "<App/>",
});
