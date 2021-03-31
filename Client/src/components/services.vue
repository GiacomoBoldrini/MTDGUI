<template>
  <div class="hello">
    <div class="title">
      <h1>Service Keys</h1>
      <button v-on:click="testing">Test socket!</button>
    </div>
  </div>
</template>

<script>
import io from "socket.io-client";

export default {
  name: "services",
  data() {
    return {
      socket: io("http://127.0.0.1:5000/", {
        transports: ["websocket"],
      }),
    };
  },
  methods: {
    testing() {
      console.log("Pinged server...");
      this.socket.emit(
        "testing", { message: "Ciaone mi chiamo Giacomo, Web development è un casino" });
    },
  },
  mounted() {
    this.socket.on("connect", () => {
      console.log("Hey!");
    });
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello {
  text-align: center;
}

h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
