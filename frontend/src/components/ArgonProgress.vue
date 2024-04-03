<template>
  <div class="progress-container" ref="progressContainer" style="height: 40px; padding-top: 3px; " >
    <div class="progress-bar mt-3" :class="[getClasses(color, variant)]"
      :style="{width: progressBarWidth, marginTop: '10px', height: '4px', color: 'black', display: 'flex', alignItems: 'center', justifyContent: 'center' }">
    </div>
    <p style="font-size: 10px; margin-top: 4px; text-align: center;">{{ `${displayedPercentage}%` }}</p>
  </div>
</template>

<script>
export default {
  name: "argon-progress",
  props: {
    color: {
      type: String,
      default: "primary",
    },
    variant: {
      type: String,
      default: "fill",
    },
    percentage: String,
  },
  data() {
    return {
      progressBarWidth: '0%',
      displayedPercentage: '0',
    };
  },
  mounted() {
    this.calculateProgressBarWidth();
  },
  watch: {
    percentage() {
      this.calculateProgressBarWidth();
    },
  },
  methods: {
    getClasses: (color, variant) => {
      let colorValue;

      if (variant === "gradient") {
        colorValue = `bg-gradient-${color}`;
      } else {
        colorValue = `bg-${color}`;
      }

      return `${colorValue}`;
    },
    calculateProgressBarWidth() {
      const containerWidth = this.$refs.progressContainer.offsetWidth;
      const actualProgressBarWidth = (parseFloat(this.percentage) / 100) * containerWidth;
      this.progressBarWidth = `${actualProgressBarWidth}px`;
      this.displayedPercentage = this.percentage;
    },
    isLightColor: (color) => {
      return color.startsWith("bg-dark");
    },
  },
};
</script>

<style>
.text-dark {
  color: #343a40;
}

.progress-container {
  margin: 0;
  padding: 0;
  text-align: center; 
}
</style>
