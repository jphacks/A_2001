<script>
import { Bar } from 'vue-chartjs';
export default {
  extends: Bar,
  props: {
    status: {
      type: Object,
      required: true,
    },
  },
  data: () => {
    return {
      mapWidth: 40,
    };
  },
  mounted() {
    // とりあえず今から40日分？
    // const exps = Object.values(this.status.exps);
    // const expList = exps.map(({ total_exp }) => total_exp);
    const datasets = [];
    const expsLength = Object.keys(this.status.exps).length;
    const expsEntries = Object.entries(this.status.exps);
    for (let index = 0; index < expsLength; index++) {
      datasets.push({
        data: new Array(this.mapWidth).fill(1),
        borderWidth: 0.2,
        borderColor: '#FFFFFF',
        backgroundColor: this.generateColor(
          expsEntries[index][1].exp,
          index + 1,
          expsLength
        ),
      });
    }
    const labels = [];
    for (let i = 1; i < this.mapWidth + 1; i++) {
      labels.push(i);
    }

    this.renderChart(
      { labels, datasets },
      {
        responsive: true,
        maintainAspectRatio: false,
        title: {
          display: true,
          text: 'Heat Map Sample',
          fontSize: 18,
        },
        legend: {
          display: false,
        },
        scales: {
          xAxes: [
            {
              gridLines: {
                color: '#FFFFFF',
              },
              barPercentage: 0.99,
              categoryPercentage: 0.99,
              stacked: true,
              ticks: {
                min: 0,
                display: false,
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
                stepSize: 1,
                display: false,
              },
            },
          ],
        },
      }
    );
  },
  methods: {
    generateColor(exp, index, divNum) {
      const date = new Date();
      const colors = [];
      const maxExp = Math.max(...Object.values(exp));
      for (let i = 0; i < this.mapWidth; i++) {
        date.setDate(date.getDate() - 1);
        const dateString = this.getDateString(date);
        let lightness = null;

        if (exp[dateString]) {
          lightness = `${String(
            Math.round((exp[dateString] / maxExp) * 100)
          )}%`;
        } else {
          lightness = '0%';
        }

        colors.push(`hsl(${(360 * index) / divNum}, 75%, ${lightness})`);
      }

      return colors;
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
