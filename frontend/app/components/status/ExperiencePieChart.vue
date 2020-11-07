<script>
import { Pie } from 'vue-chartjs';

export default {
  extends: Pie,
  props: ['status'],
  mounted() {
    const exps = Object.values(this.status.exps);
    const labels = exps.map(({ name }) => name);
    const expList = exps.map(({ total_exp: totalExp }) => totalExp);
    const colors = exps.map((_, index) => {
      return `hsl(${(360 * index) / exps.length}, 75%, 75%)`;
    });
    const datasets = [
      {
        backgroundColor: colors,
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
