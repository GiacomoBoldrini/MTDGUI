<template>
  <div class="hello">
    <div class="title">
      <h1>Run Keys</h1>
      <section class="ftco-section">
        <div class="container">
          <div class="row">
            <div class="col-md-12">
              <div class="table-wrap">
                <table class="table table-striped">
                  <thead>
                    <tr>
                      <th>RunKey Name</th>
                      <th>Configuration</th>
                      <th>Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(run, index) in runs" v-bind:key="index">
                      <td width="20%" class="name-col">{{ run.name }}</td>
                      <td width="60%" class="code-col">
                        <pre id="json">{{ run.request_config }} </pre>
                      </td>
                      <td width="20%" class="action-col">
                        <b-button
                          id="show-btn"
                          @click="$bvModal.show('bv-modal-example')"
                          class="btn btn-warning edit-btn"
                          >Edit</b-button
                        >
                        <b-modal id="bv-modal-example" hide-footer>
                          <template #modal-title>
                            Editing <code> {{ run.name }} </code>
                          </template>
                          <form>
                            <section class="InputForms">
                              <div class="form-group">
                                <label for="name_input">RunKey Name</label>
                                <input
                                  type="text"
                                  class="form-control"
                                  id="name_input"
                                  v-model="put_name"
                                />
                              </div>
                              <div class="form-group">
                                <div class="col-xs-2">
                                  <label for="body_input"
                                    >JSON RunKey config</label
                                  >
                                  <textarea
                                    class="form-control"
                                    id="body_input"
                                    rows="10"
                                    v-model="put_config"
                                  ></textarea>
                                </div>
                              </div>
                            </section>
                          </form>
                          <b-button
                            class="btn btn-primary"
                            block
                            @click="
                              put_run_on_db(run._id);
                              $bvModal.hide('bv-modal-example');
                            "
                            >Save</b-button
                          >
                        </b-modal>
                        <button
                          type="button"
                          class="btn btn-danger"
                          @click="delete_run_on_db(run._id)"
                        >
                          Delete
                        </button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </section>
      <ul>
        <li v-for="(run, index) in runs" v-bind:key="index"></li>
      </ul>
      <h1>Add new Run key</h1>
      <form>
        <section class="InputForms">
          <div class="form-group">
            <label for="name_input">RunKey Name</label>
            <input
              type="text"
              class="form-control"
              id="name_input"
              placeholder="your_new_runkey"
              v-model="request_name"
            />
          </div>
          <div class="form-group">
            <div class="col-xs-2">
              <label for="body_input">JSON RunKey config</label>
              <textarea
                class="form-control"
                id="body_input"
                rows="10"
                placeholder="{app: 'myapp.py', src: ...}"
                v-model="request_config"
              ></textarea>
            </div>
          </div>
        </section>
      </form>
    </div>
    <!-- <input type="text" class="name_field" v-model="request_name" />
    <input type="text" class="code_field" v-model="request_config" /> -->
    <button
      type="button"
      class="btn btn-primary savebutton"
      v-on:click="save_run_on_db"
    >
      Save
    </button>
  </div>
</template>

<script>
// import io from "socket.io-client";
import axios from "axios";

export default {
  name: "runkeys",
  data() {
    return {
      // socket: io("http://127.0.0.1:5000/", {
      //   transports: ["websocket"],
      // }),
      runs: [],
      post_run: {},
      request_name: "",
      request_config: "",
      msg: "",
      put_name: "",
      put_config: "",
    };
  },
  methods: {
    get_run_from_db() {
      console.log("Sent request to see db instances...");
      axios.get("/api/getRuns").then((r) => {
        this.runs = JSON.parse(r.data.run_list);
        console.log(this.runs);
        this.msg = r.data.msg;
        console.log(this.msg);
      });
    },
    save_run_on_db() {
      console.log("Sent request to save db instance...");
      this.post_run.name = this.request_name;
      this.post_run.request_config = this.request_config;
      console.log(this.post_run);
      axios.post("/api/postRun", this.post_run).then((r) => {
        this.msg = r.data.msg;
        console.log(this.msg);
        this.get_run_from_db();
      });
    },
    delete_run_on_db(id) {
      console.log("Sent request to delete db instance...");
      console.log(id);
      axios.delete("/api/deleteRun", { data: { _id: id } }).then((r) => {
        this.msg = r.data.msg;
        console.log(this.msg);
        this.get_run_from_db();
      });
    },
    put_run_on_db(id) {
      console.log(id);
      console.log(this.put_name);
      console.log(this.put_config);
      axios.put("/api/putRun", { data: { _id: id, name: this.put_name, config: this.put_config } }).then((r) => {
        this.msg = r.data.msg;
        console.log(this.msg);
        this.get_run_from_db();
      });
    },
  },
  mounted() {
    this.get_run_from_db();
    console.log(this.runs);
  },
  // mounted() {
  //   this.socket.on("connect", () => {
  //     console.log("Hey!");
  //   });
  //   this.socket.on("receive", (socket) => {
  //     this.received_m = socket.message;
  //     this.didReceived = true;
  //   });
  // },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello {
  text-align: center;
  margin-top: 2%;
}

h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: lower-latin;
  padding: 0;
}
li {
  /* display: inline-block; */
  margin: 0 10px;
}
a {
  color: #42b983;
}

.table-wrap {
  overflow-x: scroll;
}

.ftco-section {
  padding: 7em 0;
}

.row {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  margin-right: -15px;
  margin-left: -15px;
}

.col {
  -ms-flex-preferred-size: 0;
  flex-basis: 0;
  -webkit-box-flex: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
  max-width: 100%;
}

.col-md-12 {
  position: relative;
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
}

.table {
  width: 100%;
  margin-bottom: 1rem;
  color: #212529;
}
.table th,
.table td {
  padding: 0.75rem;
  vertical-align: top;
  border-top: 1px solid #dee2e6;
}

.table td code-col {
  padding: 0.75rem;
  vertical-align: top;
  border-top: 1px solid #dee2e6;
}

.table-striped tbody tr:nth-of-type(odd) {
  background-color: rgba(0, 0, 0, 0.05);
}

.InputForms {
  padding-right: 15%;
  padding-left: 15%;
  margin-top: 2%;
  margin-bottom: 2%;
}

.savebutton {
  padding: 1rem 20rem;
  margin-bottom: 5%;
}

</style>

