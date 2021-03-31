// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";

// socket
// import io from "socket.io-client";
// import VueSocketIOExt from "vue-socket.io-extended";

import App from "./App";
import router from "./router";

Vue.config.productionTip = false;

// const socket = io("http://127.0.0.1:5000/");
// Vue.use(VueSocketIOExt, socket);

/* eslint-disable no-new */
new Vue({
  el: "#app",
  router,
  components: { App },
  template: "<App/>",
});
