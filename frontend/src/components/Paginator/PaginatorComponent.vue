<template>
  <nav aria-label="Page navigation" style="margin-top: -20px; padding-top: 5px;">
    <ul class="pagination justify-content-center">
      <li class="page-item" :class="{ disabled: currentPage === 1 }">
        <a class="page-link" href="#" @click="prevPage(), getLeads()" :disabled="currentPage === 1">
          <i class="fas fa-chevron-left"></i>
        </a>
      </li>
      <li v-for="page in totalPages" :key="page" class="page-item" :class="{ active: currentPage === page }">
        <a class="page-link" href="#" @click="goToPage(page), getLeads()">
          {{ page }}
        </a>
      </li>
      <li class="page-item" :class="{ disabled: currentPage === totalPages }">
        <a class="page-link" href="#" @click="nextPage(), getLeads()" :disabled="currentPage === totalPages">
          <i class="fas fa-chevron-right"></i>
        </a>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  props: {
    currentPage: {
      type: Number,
      required: true
    },
    totalPages: {
      type: Number,
      required: true
    },
    prevPage: {
      type: Function,
      required: true
    },
    nextPage: {
      type: Function,
      required: true
    },
    goToPage: {
      type: Function,
      required: true
    },
    getLeads:{
      type: Function,
      required: true,
    }
  }
};
</script>

<style>
/* Add your custom styling for the pagination component here */
</style>
