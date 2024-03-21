<template>
    <nav aria-label="Page navigation" >
      <ul class="pagination justify-content-center" >
        <li class="page-item" :class="{ disabled: currentPage === 1 }" >
          <a class="page-link" href="#" @click="prevPage" :disabled="currentPage === 1">
            <i class="fas fa-chevron-left"></i>
          </a>
        </li>
        <li v-for="page in Math.ceil(filteredUsers.length / itemsPerPage)" :key="page" class="page-item"
          :class="{ active: currentPage === page }">
          <a class="page-link" href="#" @click="goToPage(page)"
            :class="{ 'text-primary': currentPage === page, 'text-white': currentPage === page }">{{ page }}</a>
        </li>
        <li class="page-item" :class="{ disabled: currentPage === Math.ceil(filteredUsers.length / itemsPerPage) }">
          <a class="page-link" href="#" @click="nextPage"
            :disabled="currentPage * itemsPerPage >= filteredUsers.length">
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
      itemsPerPage: {
        type: Number,
        required: true
      },
      filteredUsers: {
        type: Array,
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
      }
    }
  }
  </script>
  
  <style>
  /* Add your custom styling for the pagination component here */
  </style>
  