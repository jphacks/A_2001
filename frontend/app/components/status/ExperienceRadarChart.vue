<script>
import { Radar } from 'vue-chartjs';

export default {
  extends: Radar,
  props: ['status'],
  mounted() {
    const exps = Object.values(this.status.exps);
    const labels = exps.map(({ name }) => name);
    const expList = exps.map(({ total_exp: totalExp }) => totalExp);
    const datasets = [
      {
        label: '経験値',
        backgroundColor: 'rgba(255,99,132,0.2)',
        borderColor: 'rgba(255,99,132,1)',
        pointBackgroundColor: 'rgba(255,99,132,1)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgba(255,99,132,1)',
        data: expList,
      },
    ];

    this.renderChart(
      { labels, datasets },
      { responsive: true, maintainAspectRatio: false }
    );
  },
};
</script>
