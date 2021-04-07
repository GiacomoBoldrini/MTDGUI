<template>
  <div class="container">
    <div class="toppane">
      <h1>WEBGUI Main</h1>
    </div>
    <div class="leftpane">
      <div class="jumbotron jumbotron-fluid">
        <div class="container">
          <hr />
          <div>
            <b-card no-body>
              <b-tabs card>
                <b-tab title="Log" active>
                  <div class="log-overflow">
                    <b-card-text v-for="(log, index) in logs" :key="index">
                      <span class="logaction">{{ log.action }}: </span>
                      <span class="logbody">{{ log.body }} </span>
                    </b-card-text>
                  </div>
                </b-tab>
                <b-tab title="Plots">
                  <div class="log-overflow">
                    <graph-chart />
                  </div>
                </b-tab>
              </b-tabs>
            </b-card>
          </div>
        </div>
      </div>
    </div>
    <div class="rightpane">
      <div class="error-container" v-if="currentStatus === 7">
        <div class="blink">
          <b-badge variant="danger" class="errorbadge">ERROR</b-badge>
        </div>
      </div>
      <div class="status" v-if="currentStatus !== 0">
        <b-button-group size="lg">
          <b-button
            class="PrimaryButtons"
            v-for="(action, index) in actions.slice(0, -1)"
            :key="action.value"
            :variant="statCheck(action.value)"
            :disabled="statDisable(action.value)"
            @click="executeButton(index)"
            >{{ action.actionName }}</b-button
          >
        </b-button-group>
      </div>
      <hr />
      Configure
      <section class="configurations Service">
        <b-dropdown text="Select Service" variant="outline-primary" class="m-2">
          <b-dropdown-item
            href="#"
            v-for="(service, index) in services"
            v-bind:key="index"
            @click="updateService(service)"
            :disabled="isConfDis"
            >{{ service.name }}</b-dropdown-item
          >
        </b-dropdown>
        <b-badge variant="primary">{{ chose_service.name }}</b-badge>
      </section>
      <section class="configurations RunKey">
        <b-dropdown text="Select RunKey" variant="outline-primary" class="m-2">
          <b-dropdown-item
            href="#"
            v-for="(run, index) in runkeys"
            v-bind:key="index"
            @click="updateRun(run)"
            :disabled="isConfDis"
            >{{ run.name }}</b-dropdown-item
          >
        </b-dropdown>
        <b-badge variant="primary">{{ chose_run.name }}</b-badge>
      </section>
      <div class="configurations">
        <b-button
          variant="warning"
          :disabled="isConfDis"
          @click="updateConfigurations"
          >Configure</b-button
        >
      </div>
      <hr />
      Console
      <div class="configurations">
        <b-button
          class="console"
          variant="warning"
          :disabled="isRunDis"
          @click="updateRunning"
          >Run</b-button
        >
        <b-button
          class="console"
          variant="warning"
          :disabled="isPauseDis"
          @click="updatePause"
          >{{ paused }}</b-button
        >
        <b-button
          class="console"
          variant="warning"
          :disabled="isPauseDis"
          @click="updateStop"
          >Stop</b-button
        >
        <b-button class="console" variant="warning" @click="currentStatus = 7"
          >Toogle error</b-button
        >
      </div>
      <div class="configurations">
        <b-button
          class="restartRun"
          variant="danger"
          :disabled="isRestartDis"
          @click="updateRestart"
          >Restart Run</b-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import io from "socket.io-client";
import axios from "axios";
// import BarChart from "./BarChart";

export default {
  name: "webgui",
  // components: {
  //   BarChart,
  // },
  data() {
    return {
      socket: io("http://127.0.0.1:5000/", {
        transports: ["websocket"],
      }),
      currentStatus: 0,
      actions: [
        { actionName: "Initialize", value: 1 },
        { actionName: "Configured", value: 2 },
        { actionName: "Run", value: 3 },
        { actionName: "Pause", value: 4 },
        { actionName: "Resume", value: 5 },
        { actionName: "Stop", value: 6 },
        { actionName: "Error", value: 7 },
      ],
      runkeys: [],
      services: [],
      chose_service: "",
      chose_run: "",
      runConfig: {},
      paused: "Pause",
      logs: [],

      // for the graph
      datacollection: [1, 2, 3, 4, 5],
    };
  },
  methods: {
    addLog(theaction, themsg) {
      this.logs.unshift({
        action: theaction,
        body: themsg,
      });
    },
    statCheck(idx) {
      const style =
        this.actions[this.currentStatus - 1].value >= idx
          ? "success"
          : "warning";
      return style;
    },
    statDisable(idx) {
      return this.actions[this.currentStatus - 1].value >= idx;
    },
    get_services_from_db() {
      console.log("Sent request to see db instances...");
      axios.get("/api/getServices").then((r) => {
        this.services = JSON.parse(r.data.service_list);
        this.chose_service = this.services[0];
        this.msg = r.data.msg;
        this.addLog("DBQuery", "Queried service database");
      });
    },
    get_run_from_db() {
      console.log("Sent request to see db instances...");
      axios.get("/api/getRuns").then((r) => {
        this.runkeys = JSON.parse(r.data.run_list);
        this.chose_run = this.runkeys[0];
        this.msg = r.data.msg;
        this.addLog("DBQuery", "Queried run database");
      });
    },
    updateService(service) {
      this.chose_service = service;
      this.addLog("Selection", `Selected service ${this.chose_service.name}`);
    },
    updateRun(run) {
      this.chose_run = run;
      this.addLog("Selection", `Selected runkey ${this.chose_run.name}`);
    },
    updateInitialize() {
      axios.post("/api/actions/initialize").then((r) => {
        this.currentStatus = r.data.newstate;
        this.msg = r.data.msg;
        this.addLog("Initialize", this.msg);
      });
    },
    updateConfigurations() {
      this.runConfig = { service: this.chose_service, runkey: this.chose_run };
      this.addLog(
        "Selection",
        `Finalyzed configuration service ${this.chose_service.name} runkey ${this.chose_run.name}`,
      );
      axios.post("/api/actions/configure", this.runConfig).then((r) => {
        this.currentStatus = r.data.newstate;
        this.msg = r.data.msg;
        this.addLog("Configure", this.msg);
      });
    },
    updateRunning() {
      axios.post("/api/actions/start").then((r) => {
        this.currentStatus = r.data.newstate;
        this.msg = r.data.msg;
        this.addLog("Running", this.msg);
      });
    },
    updatePause() {
      console.log("Paused!");
      console.log(this.currentStatus);
      if (this.paused === "Pause") {
        axios.post("/api/actions/pause", this.runConfig).then((r) => {
          this.currentStatus = r.data.newstate;
          this.msg = r.data.msg;
          this.paused = "Resume";
          this.addLog("Pause", this.msg);
        });
      } else {
        axios.post("/api/actions/resume", this.runConfig).then((r) => {
          this.currentStatus = r.data.newstate;
          this.msg = r.data.msg;
          this.paused = "Pause";
          this.addLog("Resumed", this.msg);
        });
      }
    },
    updateStop() {
      axios.post("/api/actions/stop").then((r) => {
        console.log(r.data.newstate);
        this.currentStatus = r.data.newstate;
        this.msg = r.data.msg;
        this.addLog("Stop", this.msg);
      });
    },
    updateRestart() {
      axios.post("/api/actions/restart").then((r) => {
        this.currentStatus = r.data.newstate;
        this.msg = r.data.msg;
        this.addLog("Restart", this.msg);
      });

      this.updateInitialize();
    },
    executeButton(idx) {
      if (idx === 1) {
        this.updateConfigurations();
      } else if (idx === 2) {
        this.updateRunning();
      } else if (idx === 3) {
        this.updatePause();
      } else if (idx === 4) {
        this.updateStop();
      }
    },
  },
  computed: {
    isConfDis() {
      return (
        this.chose_service === "" ||
        this.chose_run === "" ||
        this.currentStatus !== 1
      );
    },
    isRunDis() {
      return this.currentStatus !== 2;
    },
    isPauseDis() {
      console.log("IsPauseDis");
      return (
        this.currentStatus <= 2 ||
        this.actions[this.currentStatus - 1].value === 6
      );
    },
    isRestartDis() {
      return 1 === 2;
      // return this.currentStatus !== 5;
    },
  },
  mounted() {
    this.socket.on("connect", () => {
      console.log("Connected!");
    });
    this.socket.on("receive", (socket) => {
      this.received_m = socket.message;
      this.didReceived = true;
    });

    this.get_services_from_db();
    this.get_run_from_db();
  },
  created() {
    console.log("created");
    // Check  if initialization succeded
    this.updateInitialize();
    // Send messsage to server when refrashing or closing the browser
    window.addEventListener(
      "beforeunload",
      () => {
        this.updateRestart();
      },
      false,
    );
  },
};
</script>

<style scoped>
.leftpane {
  width: 50%;
  height: 100%;
  float: left;
  padding-right: 2%;
  border-collapse: collapse;
}

.rightpane {
  width: 50%;
  height: 100%;
  padding-left: 2%;
  position: relative;
  float: right;
  border-collapse: collapse;
}

.toppane {
  width: 100%;
  height: 100px;
  text-align: center;
  display: block;
  padding: 3% 0;
}

.log-overflow {
  max-height: 30rem;
  overflow-y: auto;
}

.logaction {
  color: #0d6efd;
}

.status {
  text-align: center;
  margin: auto;
  margin-top: 3%;
  margin-bottom: 5%;
}

.box {
  width: 180px;
  height: 180px;
  margin: 15px auto;
  border-style: solid;
  border-width: 1px;
  border-color: rgba(119, 119, 119, 0.966);
  border-radius: 25px;
  position: relative;
  float: left;
  padding: 1%;
  margin: 1%;
}

.configurations {
  padding-top: 1%;
  padding-bottom: 1%;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

.badge {
  color: #0d6efd;
  background-color: white;
  border-color: #0d6efd;
  border-radius: 4px;
  border-style: solid;
  border-width: 1px;
  height: 35px;
  width: 10rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.error-container {
  display: flex;
  justify-content: center;
}

.errorbadge {
  color: #ff0000;
  background-color: white;
  border-color: #bb0707;
  border-radius: 4px;
  border-style: solid;
  border-width: 2px;
  height: 35px;
  width: 20rem;
}

.m-2 {
  height: 35px;
}

.console {
  margin-left: 1%;
  width: 10rem;
}

button:hover {
  border: 1px solid #0099cc;
  background-color: #00aacc;
  color: #ffffff;
  padding: 5px 10px;
}

.PrimaryButtons {
  pointer-events: none;
  border: 1px solid #999999;
  background-color: #cccccc;
  color: #666666;
}

.PrimaryButtons:disabled,
.PrimaryButtons[disabled] {
  border: 1px solid #556b2f;
  background-color: #228b22;
  color: white;
}

.blink {
  animation: blinker 1s linear infinite;
}

@keyframes blinker {
  50% {
    opacity: 0;
  }
}

.btn-group,
.btn-group-vertical {
  position: relative;
  display: block;
}

/* Media shrinking */
@media only screen and (min-width: 0px) and (max-width: 600px) {
  .leftpane {
    width: 100%;
    height: 100%;
    display: block;
    border-collapse: collapse;
  }

  .rightpane {
    width: 100%;
    height: 100%;
    display: block;
    border-collapse: collapse;
  }
}
</style>
