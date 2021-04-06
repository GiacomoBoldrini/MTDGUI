<template>
  <div class="barPlots">
    <section class="but-col">
      <div>Console</div>
      <div>
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
                size: 0.01,
                start: 0.0,
              },
            },
          ],
          marker_color: "green",
          marker: {
            color: "green",
          },
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
                end: 1,
                size: 0,
                start: 0.1,
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
    setX() {
      for (let z = 0; z < 2; z += 1) {
        const xs = [];
        for (let i = 0; i < 500; i += 1) {
          xs[i] = Math.random();
        }
        const vals = this.the_vals;
        vals[z].values[0].x = xs;
        this.the_vals = vals;
      }
    },
    start() {
      // setInterval(this.setX, 2000);
      this.setX();
    },
  },
  mounted() {
    console.log("mounted graphs");
    this.start();
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
