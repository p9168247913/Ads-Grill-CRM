<template>
  <div class="progress w-100 ">
    <div
      class="progress-bar"
      :class="[getClasses(color, variant)]"
      :style="{ width: percentage + '%', height: '4px', color: 'black', display: 'flex', alignItems: 'center', justifyContent: 'center', }" 
    >
      
    </div>
    <p style="font-size: 10px; margin-top: 4px;">{{ `${percentage}%` }}</p>
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
</style>
