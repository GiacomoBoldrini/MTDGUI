<template>
  <div class="hello">
    <div class="title">
      <h1>Service Keys</h1>
      <button v-on:click="testing">Test socket!</button>
      <button v-on:click="request">Receive from server!</button>
      <p v-if=didReceived> {{ received_m }} </p>
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
      didReceived: false,
      received_m: "",
    };
  },
  methods: {
    testing() {
      console.log("Pinged server...");
      this.socket.emit(
        "testing", { message: "Ciaone mi chiamo Giacomo, Web development è un casino" });
    },
    request() {
      console.log("Receive from server...");
      this.socket.emit("receive");
    },
  },
  mounted() {
    this.socket.on("connect", () => {
      console.log("Hey!");
    });
    this.socket.on("receive", (socket) => {
      this.received_m = socket.message;
      this.didReceived = true;
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
