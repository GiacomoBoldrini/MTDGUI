<template>
  <div class="barPlots">
    <section class="but-col">
      <div>Console</div>
      <div>
        <b-button variant="primary" @click="startDummy">Start</b-button>
        <b-button variant="primary" @click="stopDummy">Stop</b-button>
        <b-button-group>
          <b-button variant="primary" @click="setNCols(1)">1</b-button>
          <b-button variant="primary" @click="setNCols(2)">2</b-button>
        </b-button-group>
      </div>
    </section>
    <div
      class="plot_div"
      v-for="(val, index) in the_vals"
      :key="index"
      :style="plotStyle"
    >
      <Plotly
        :data="val.values"
        :layout="val.layout"
        :display-mode-bar="false"
      ></Plotly>
      <div>
        <b-button pill @click="logY(index)">Log-y</b-button>
        <b-button pill @click="logX(index)">Log-x</b-button>
        <b-button pill @click="linY(index)">Lin-y</b-button>
        <b-button pill @click="linX(index)">Lin-x</b-button>
      </div>
    </div>
  </div>
</template>

<script>
import { Plotly } from "vue-plotly";
import io from "socket.io-client";

const x = [];
for (let i = 0; i < 500; i += 1) {
  x[i] = Math.random();
}

export default {
  export: "Dqm",
  components: {
    Plotly,
  },
  data() {
    return {
      height: 100,
      width: 100,
      ncols: 1,

      the_vals: [
        {
          values: [
            {
              x: [],
              type: "histogram",
              xbins: {
                end: 1,
                size: 0.1,
                start: 0.0,
              },
              marker: {
                color: "grey",
                // line: {
                //   color: "blue",
                //   width: 1,
                // },
              },
              error_y: {
                visible: true,
                type: "sqrt",
              },
            },
          ],
          layout: {
            title: "ciao",
            nbins: 10,
            color: "green",
            yaxis: {
              title: "y",
              type: "log",
              autorange: true,
            },
            xaxis: {
              title: "x",
              type: "linear",
            },
            bargap: 0.0,
            bargroupgap: 0.0,
          },
          config: {
            responsive: true,
            scrollZoom: true,
            displayModeBar: true,
          },
        },
        {
          values: [
            {
              x: [],
              type: "histogram",
              xbins: {
                end: 3,
                size: 0.2,
                start: -3,
              },
              marker: {
                color: "grey",
              },
              error_y: {
                visible: true,
                type: "sqrt",
              },
            },
          ],
          layout: {
            title: "miao",
            nbins: 10,
            yaxis: {
              type: "linear",
            },
            xaxis: {
              type: "linear",
            },
          },
          config: {
            responsive: true,
          },
        },
      ],
    };
  },
  computed: {
    plotStyle() {
      const width = this.width / this.ncols;
      const height = width;
      return {
        width: `${width}%`,
        height: `${height}%`,
        display: "inline-block",
        margin: 0,
      };
    },
  },
  methods: {
    setNCols(n) {
      this.ncols = n;
    },
    logY(idx) {
      const vals = this.the_vals;
      const theval = vals[idx];
      if (theval.layout.yaxis.type !== "log") {
        theval.layout.yaxis.type = "log";
      }
      vals[idx] = theval;
      this.the_vals = vals;
    },
    logX(idx) {
      const vals = this.the_vals;
      const theval = vals[idx];
      if (theval.layout.xaxis.type !== "log") {
        theval.layout.xaxis.type = "log";
      }
      vals[idx] = theval;
      this.the_vals = vals;
    },
    linY(idx) {
      const vals = this.the_vals;
      const theval = vals[idx];
      if (theval.layout.yaxis.type !== "linear") {
        theval.layout.yaxis.type = "linear";
      }
      vals[idx] = theval;
      this.the_vals = vals;
    },
    linX(idx) {
      const vals = this.the_vals;
      const theval = vals[idx];
      if (theval.layout.xaxis.type !== "linear") {
        theval.layout.xaxis.type = "linear";
      }
      vals[idx] = theval;
      this.the_vals = vals;
    },
    startDummy() {
      this.socket.emit("sendData");
    },
    stopDummy() {
      this.socket.emit("stopData");
    },
  },
  created() {
    this.socket = io("http://127.0.0.1:5000");
    console.log("mounted graphs");
    this.socket.on("connect", () => {
      console.log("Hey!");
    });
    this.socket.on("receiveData", (data) => {
      const vals = this.the_vals;

      let idx = data.updates[0].index;
      let v = data.updates[0].values;

      vals[idx].values[0].x = v;

      idx = data.updates[1].index;
      v = data.updates[1].values;

      vals[idx].values[0].x = v;

      this.the_vals = vals;
      console.log("Updated graphs...");
    });
    this.socket.on("updateSockets", (data) => {
      console.log(data);
    });
    this.socket.on("updatePlots", () => {
      const vals = this.the_vals;
      for (let i = 0; i < vals.length; i += 1) {
        vals[i].values[0].x = [];
      }
      this.the_vals = vals;
    });
  },
};
</script>

<style scoped>
.barPlots {
  text-align: center;
}
.but-col {
  margin: auto;
}
</style>
