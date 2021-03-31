import Vue from "vue";
import Router from "vue-router";
import HelloWorld from "@/components/HelloWorld";
import Service from "@/components/services";
import RunKeys from "@/components/runkeys";

Vue.use(Router);

export default new Router({
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
  ],
});
