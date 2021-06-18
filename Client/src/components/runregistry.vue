<template>
  <div class="hello">
    <div class="title">
      <h1>Run Registry</h1>
      <hr />
      <section class="fetch-button">
        <button
          type="button"
          class="btn btn-primary"
          @click="get_services_from_db"
        >
          Fetch Database
        </button>
      </section>
      <section class="ftco-section">
        <div class="container">
          <div class="row">
            <div class="col-md-12">
              <div class="table-wrap">
                <table class="table table-striped">
                  <thead>
                    <tr>
                      <th>Number</th>
                      <th>Date</th>
                      <th>Status</th>
                      <th>Reco</th>
                      <th>Service Key</th>
                      <th>Run Key</th>
                      <th>Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="(run, index) in runDatabase.slice().reverse()"
                      v-bind:key="index"
                    >
                      <td width="5%" class="name-col">{{ index }}</td>
                      <td width="15%" class="code-col">
                        <pre id="json">{{ run.time }} </pre>
                      </td>
                      <td width="20%" class="action-col">
                        <div class="status">
                          <b-button-group size="sm" class="stats">
                            <b-button
                              class="PrimaryButtons"
                              v-for="action in actions.slice(0, -1)"
                              :key="action.value"
                              :variant="statCheck(action.value, run.status)"
                              :disabled="statDisable(action.value, run.status)"
                              >{{ action.actionName }}</b-button
                            >
                          </b-button-group>
                        </div>
                      </td>
                      <td width="15%" class="action-col">
                        {{ run.recostep }}
                      </td>
                      <td width="15%" class="action-col">
                        {{ run.configuration.service.name }}
                      </td>
                      <td width="20%" class="action-col">
                        {{ run.configuration.runkey.name }}
                      </td>
                      <td width="10%" class="action-col">
                        <button type="button" class="btn btn-primary">
                          Inspect
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
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "runregistry",
  data() {
    return {
      runDatabase: [],
      msg: "",
      actions: [
        { actionName: "Initialize", value: 1 },
        { actionName: "Configured", value: 2 },
        { actionName: "Run", value: 3 },
        { actionName: "Pause", value: 4 },
        { actionName: "Resume", value: 5 },
        { actionName: "Stop", value: 6 },
        { actionName: "Error", value: 7 },
      ],
    };
  },
  methods: {
    get_services_from_db() {
      console.log("Sent request to see db instances...");
      axios.get("/api/getRunReg").then((r) => {
        console.log(r.data);
        this.runDatabase = JSON.parse(r.data.run_reg);
        console.log(this.runDatabase);
        this.msg = r.data.msg;
        console.log(this.msg);
      });
    },
    statCheck(idx, status) {
      const style = status >= idx ? "success" : "warning";
      return style;
    },
    statDisable(idx, status) {
      return status >= idx;
    },
  },
  mounted() {
    this.get_services_from_db();
  },
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

.fetch-button {
  padding: 2%;
}

.table-wrap {
  overflow-x: scroll;
}

.ftco-section {
  padding: 0 0;
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

.PrimaryButtons {
  pointer-events: none;
  border: 1px solid #556b2f;
  background-color: #be1616;
  color: white;
}

.PrimaryButtons:disabled,
.PrimaryButtons[disabled] {
  border: 1px solid #556b2f;
  background-color: #228b22;
  color: white;
}
</style>
