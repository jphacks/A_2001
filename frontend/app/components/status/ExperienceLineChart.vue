<script>
import { Line } from 'vue-chartjs';

export default {
  extends: Line,
  props: {
    status: {
      type: Object,
      required: true,
    },
  },
  data: () => {
    return {
      chartWidth: 20,
    };
  },
  mounted() {
    this.$refs.canvas.width = 0;

    const exps = Object.values(this.status.exps);
    const colors = exps.map((_, index) => {
      return `hsl(${(360 * index) / exps.length}, 75%, 75%)`;
    });
    const datasets = exps.map((val, i) => {
      const { total_exp: totalExp } = val;
      return {
        data: this.generateData(val.exp, totalExp),
        label: val.name,
        backgroundColor: colors[i],
        hoverBackgroundColor: colors[i],
        fill: true,
      };
    });
    const labels = [];
    for (let i = 0; i < this.chartWidth; i++) {
      const date = new Date();
      date.setDate(date.getDate() - i);
      date.setHours(0);
      date.setMinutes(0);
      date.setSeconds(0);
      labels.push(this.getDateString(date));
    }

    this.renderChart(
      {
        datasets,
        labels,
      },
      {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          xAxes: [
            {
              type: 'time',
              time: {
                unit: 'day',
                displayFormats: {
                  quarter: 'MMM D',
                },
              },
            },
          ],
          yAxes: [
            {
              gridLines: {
                color: '#FFFFFF',
                zeroLineWidth: 0,
              },
              stacked: true,
              ticks: {
                min: 0,
              },
            },
          ],
        },
      }
    );
  },
  methods: {
    generateData(exps, totalExp) {
      const data = [];
      let sum = totalExp;
      for (const exp of Object.values(exps)) {
        data.push(sum - exp);
        sum -= exp;
      }
      return data;
    },
    getDateString(date) {
      return (
        date.getFullYear() +
        '-' +
        ('0' + (date.getMonth() + 1)).slice(-2) +
        '-' +
        ('0' + date.getDate()).slice(-2)
      );
    },
  },
};
</script>
