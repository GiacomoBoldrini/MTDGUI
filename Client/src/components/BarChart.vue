<template>
  <div id="ciao">
    <Plotly
      :data="data"
      :layout="layout"
      :display-mode-bar="false"
      :key="data.x"
    ></Plotly>
  </div>
</template>

<script>
import { Plotly } from "vue-plotly";

const x = [];
for (let i = 0; i < 500; i += 1) {
  x[i] = Math.random();
}

export default {
  export: "BarChart",
  components: {
    Plotly,
  },
  data() {
    return {
      data: [
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
      layout: {
        title: "ciao",
        nbins: 10,
      },
      config: {
        responsive: true,
      },
    };
  },
  methods: {
    setX() {
      const xs = [];
      for (let i = 0; i < 500; i += 1) {
        xs[i] = Math.random();
      }
      this.x = xs;
      console.log(this.x);
      Plotly.newPlot("ciao", this.data, this.layout);
    },
    start() {
      setInterval(this.setX, 2000);
    },
  },
  mounted() {
    this.start();
  },
};
</script>
