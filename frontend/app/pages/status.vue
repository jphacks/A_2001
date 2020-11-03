<template>
  <div class="animated fadeIn">
    <b-card-group columns class="card-columns cols-2">
      <b-card header="経験値">
        <div class="chart-wrapper">
          <ExperienceRadarChart :status="status" />
        </div>
      </b-card>
      <b-card header="経験値">
        <div class="chart-wrapper">
          <ExperiencePieChart :status="status" />
        </div>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
import ExperienceRadarChart from '~/components/status/ExperienceRadarChart';
import ExperiencePieChart from '~/components/status/ExperiencePieChart';

export default {
  name: 'Charts',
  components: {
    ExperienceRadarChart,
    ExperiencePieChart,
  },
  fetch() {
    // TODO: APIから取ってくる
    this.status = {
      exps: {
        2: {
          name: 'Vue.js入門',
          exp: 1412,
        },
        10: {
          name: 'React入門',
          exp: 2000,
        },
        41: {
          name: '競プロ',
          exp: 2412,
        },
        1010: {
          name: '研究',
          exp: 200,
        },
      },
      level: 0,
      title: 'Vueマスター',
    };
  },
  data() {
    return {
      status: {},
    };
  },
  fetchOnServer: false,
};
</script>
