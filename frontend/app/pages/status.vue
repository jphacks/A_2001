<template>
  <div class="animated fadeIn container">
    <template v-if="!$fetchState.pending">
      <b-card-group columns class="card-columns cols-2">
        <b-card header="Radar chart">
          <div class="chart-wrapper">
            <ExperienceRadarChart :status="status" />
          </div>
        </b-card>
        <b-card header="Pie chart">
          <div class="chart-wrapper">
            <ExperiencePieChart :status="status" />
          </div>
        </b-card>
      </b-card-group>
      <b-card header="Heatmap">
        <div class="chart-wrapper">
          <ExperienceHeatMap :status="status" />
        </div>
      </b-card>
      <b-card header="Line chart">
        <div class="chart-wrapper">
          <ExperienceLineChart :status="status" />
        </div>
      </b-card>
    </template>
  </div>
</template>

<script>
import ExperienceRadarChart from '~/components/status/ExperienceRadarChart';
import ExperiencePieChart from '~/components/status/ExperiencePieChart';
import ExperienceLineChart from '~/components/status/ExperienceLineChart';
import ExperienceHeatMap from '~/components/status/ExperienceHeatMap';

export default {
  name: 'Charts',
  components: {
    ExperienceRadarChart,
    ExperiencePieChart,
    ExperienceHeatMap,
    ExperienceLineChart,
  },
  fetchOnServer: false,
  async fetch() {
    const status = await this.$api.$get('/api/users').catch((err) => {
      console.log(err);
    });
    this.status = status;
  },
  data() {
    return {
      status: {},
    };
  },
};
</script>
