<template>
  <div class="jumbotron-container">
    <div fluid class="jumbotron jumbotron-fluid bg">
      <div class="container">
        <h1 class="text-white display-1 text-nowrap text-monospace">
          SHIBAFU
          <i class="fa fa-check"></i>
        </h1>
        <p class="h2 text-secondary text-block">
          <span class="text-light">S</span>tatus
          <span class="text-light">H</span>eatmap and
          <span class="text-light">I</span>llustration of
          <span class="text-light">B</span>lah blah
          <span class="text-light">A</span>ctivities
          <span class="text-light">F</span>or
          <span class="text-light">U</span>ser's motivation
        </p>
        <b-button pill variant="primary" @click="transition"
          >{{ message }}
          <b-icon
            animation="cylon"
            icon="chevron-right"
            shift-h="4"
            variant="white"
            ><b-icon-chevron-right
          /></b-icon>
        </b-button>
      </div>
    </div>
    <b-container>
      <b-row>
        <b-col class="d-flex align-items-center flex-column"
          ><b-icon icon="bar-chart-line" class="icon"
            ><b-icon-bar-chart-line
          /></b-icon>
          <h3>今までにこなしたタスクが経験値として見ることができる</h3></b-col
        >
        <b-col class="d-flex align-items-center flex-column"
          ><b-icon icon="grid3x2-gap" class="icon"
            ><b-icon-grid3x2-gap
          /></b-icon>
          <h3>ヒートマップによるタスクの視覚化</h3></b-col
        >
        <b-col class="d-flex align-items-center flex-column"
          ><b-icon icon="list-task" class="icon"><b-icon-list-task /></b-icon>
          <h3>細かいタスク管理</h3></b-col
        >
      </b-row>
    </b-container>
  </div>
</template>

<script>
import {
  BIcon,
  BIconChevronRight,
  BIconBarChartLine,
  BIconGrid3x2Gap,
  BIconListTask,
} from 'bootstrap-vue';
export default {
  layout: 'clean',
  components: {
    BIcon,
    BIconChevronRight,
    BIconBarChartLine,
    BIconGrid3x2Gap,
    BIconListTask,
  },
  computed: {
    message() {
      return this.$store.state.login.isLoggedin ? 'ステータスへ' : 'Login';
    },
  },
  methods: {
    transition() {
      if (this.$store.state.login.isLoggedin) {
        this.$router.push('/status');
      } else {
        this.$router.push('/login');
      }
    },
  },
};
</script>

<style scoped>
.jumbotron-container {
  width: 100vw;
  height: 100vh;
  background-color: #d9ead5;
  overflow-x: hidden;
}

.jumbotron-container > div {
  padding-top: 30vh;
  padding-bottom: 10vh;
}

.bg {
  background: url('/img/shibafu.jpg') center no-repeat;
  background-size: cover;
  position: relative;
  width: 100%;
  height: 100vh;
}

.icon {
  width: 70%;
  height: 70%;
}
</style>
