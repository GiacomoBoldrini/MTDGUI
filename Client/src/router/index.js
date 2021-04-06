import Vue from "vue";
import Router from "vue-router";
import HelloWorld from "@/components/HelloWorld";
import Service from "@/components/services";
import RunKeys from "@/components/runkeys";
import WebGui from "@/components/webgui";
import Dqm from "@/components/dqm";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/vue",
      name: "HelloWorld",
      component: HelloWorld,
    },
    {
      path: "/service",
      name: "services",
      component: Service,
    },
    {
      path: "/runconf",
      name: "runkeys",
      component: RunKeys,
    },
    {
      path: "/webgui",
      name: "webgui",
      component: WebGui,
    },
    {
      path: "/dqm",
      name: "dqm",
      component: Dqm,
    },
  ],
});
