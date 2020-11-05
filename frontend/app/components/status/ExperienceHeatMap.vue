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
      maxMinutes: 1440,
    };
  },
  mounted() {
    // とりあえず今から40日分？
    const exps = Object.values(this.status.exps);
    const datasets = exps.map((val, i) => {
      const bgColor = this.generateColor(val.exp, i + 1, exps.length);
      return {
        data: new Array(this.mapWidth).fill(1),
        label: val.name,
        borderWidth: 0.2,
        borderColor: '#FFFFFF',
        backgroundColor: bgColor,
        hoverBackgroundColor: bgColor,
      };
    });
    const labels = [];
    for (let i = 0; i < this.mapWidth; i++) {
      const date = new Date();
      date.setDate(date.getDate() - i);
      date.setHours(0);
      date.setMinutes(0);
      date.setSeconds(0);
      labels.unshift(this.getDateString(date));
    }

    const minDisplayDate = new Date();
    minDisplayDate.setDate(minDisplayDate.getDate() - this.mapWidth);
    minDisplayDate.setHours(0);
    minDisplayDate.setMinutes(0);
    minDisplayDate.setSeconds(0);
    const maxDisplayDate = new Date();
    maxDisplayDate.setHours(23);
    maxDisplayDate.setMinutes(59);
    maxDisplayDate.setSeconds(59);
    this.renderChart(
      { labels, datasets },
      {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          xAxes: [
            {
              type: 'time',
              time: {
                unit: 'day',
                min: minDisplayDate,
                max: maxDisplayDate,
                displayFormats: {
                  quarter: 'MMM D',
                },
              },
              gridLines: {
                color: '#FFFFFF',
              },
              barPercentage: 0.99,
              categoryPercentage: 0.99,
              stacked: true,
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
        legend: {
          display: true,
          labels: {
            fontColor: 'rgb(255, 99, 132)',
          },
        },
        tooltips: {
          callbacks: {
            label: (tooltipItem) => {
              const exp = exps[tooltipItem.datasetIndex].exp;
              const dateString = this.getDateString(
                new Date(tooltipItem.xLabel)
              );
              return (exp[dateString] ?? 0) + 'min';
            },
          },
        },
      }
    );
  },
  methods: {
    generateColor(exp, index, divNum) {
      const date = new Date();
      date.setHours(0);
      date.setMinutes(0);
      date.setSeconds(0);

      const colors = [];
      const maxExp = Math.max(...Object.values(exp));
      for (let i = 0; i < this.mapWidth; i++) {
        const dateString = this.getDateString(date);
        const expVal = exp[dateString] ?? 0;
        const value = Math.min(1, expVal / this.maxMinutes);
        const saturation = value * 100;
        const lightness = -value * 67 + 97;

        colors.unshift(
          `hsl(${(360 * index) / divNum}, ${saturation}%, ${lightness}%)`
        );
        date.setDate(date.getDate() - 1);
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
