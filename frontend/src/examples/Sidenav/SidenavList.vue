<template>
  <div class="collapse navbar-collapse w-auto h-auto h-100" id="sidenav-collapse-main">
    <ul class="navbar-nav" v-if="authUser.role !== 'client' || authUser.role!=='contact'">

      <!--Dashboard-->
      <li class="nav-item" v-if="authUser.role !== 'development' && authUser.role !== 'client' && authUser.role !== 'contact'">
        <sidenav-item url="/dashboard" :class="getRoute() === 'dashboard' ? 'active' : ''"
          :navText="this.$store.state.isRTL ? 'لوحة القيادة' : 'Dashboard'">
          <template v-slot:icon>
            <i class="ni ni-tv-2 text-primary text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <!-- Employee -->
      <li v-if="authUser.role!== 'contact'" @click="isAreaExpendedTogeller(), colapseShowTogeller(), toggleEmploymentDropdown()" class="nav-item"
        :class="{ 'active': isEmployeeActive }">
        <sidenav-item url="" :class="{ 'collapsed': isCollapseShow }"
          :navText="this.$store.state.isRTL ? 'لوحة القيادة' : 'Employees'" data-toggle="collapse"
          :aria-expanded="isAreaExpended">
          <template v-slot:icon>
            <i class="fas fa-users text-primary text-sm opacity-10"></i>
          </template>
        </sidenav-item>

        <ul v-if="isEmploymentDropdownOpen" @click.stop
          class="iq-submenu collapse list-unstyled iq-submenu collapse list-unstyled"
          :class="{ 'show': isCollapseShow }" data-parent="#iq-sidebar-toggle">
          <li class=" "
            v-if="authUser.role !== 'development' && authUser.role !== 'leads' && authUser.role !== 'sales' && authUser.role !== 'contact'">
            <sidenav-item class="emp-li" :url="getRoutePath('hrms')" :class="{ 'active': getRoute() === 'hrms' }"
              :navText="this.$store.state.isRTL ? 'لوحة القيادة' : 'HRMS'" data-toggle="collapse" aria-expanded="false">

              <template v-slot:icon>
                <i class="fas fa-clipboard-list text-info text-sm opacity-10"></i>
              </template>
              <router-link :to="getRoutePath('hrms')"></router-link>
            </sidenav-item>
          </li>
          <li class="nav-item" v-if="authUser.role !== 'leads' && authUser.role !== 'sales' && authUser.role !== 'contact'">
            <sidenav-item class="emp-li" :url="getRoutePath('development')"
              :class="{ 'active': getRoute() === 'development' }"
              :navText="this.$store.state.isRTL ? 'لوحة القيادة' : 'Development'" data-toggle="collapse"
              aria-expanded="false">
              <template v-slot:icon>
                <i class="fas fa-code text-info text-sm opacity-10"></i>
              </template>
              <router-link :to="getRoutePath('development')"> <span class="ml-0">Development</span></router-link>
            </sidenav-item>
          </li>
          <li class=" " v-if="authUser.role !== 'development' && authUser.role !== 'contact'">
            <sidenav-item class="emp-li" :url="getRoutePath('sales')" :class="{ 'active': getRoute() === 'sales' }"
              :navText="this.$store.state.isRTL ? 'لوحة القيادة' : 'Sales'" data-toggle="collapse"
              aria-expanded="false">
              <template v-slot:icon>
                <i class="fas fa-shopping-cart text-success text-sm opacity-10"></i>
              </template>
              <router-link :to="getRoutePath('sales')"></router-link>
            </sidenav-item>
          </li>
          <li class="" v-if="authUser.role !== 'development' && authUser.role !== 'contact'">
            <sidenav-item class="emp-li" :url="getRoutePath('leads')" :class="{ 'active': getRoute() === 'leads' }"
              :navText="this.$store.state.isRTL ? 'لوحة القيادة' : 'Leads'" data-toggle="collapse"
              aria-expanded="false">
              <template v-slot:icon>
                <i class="fas fa-user-friends text-success text-sm opacity-10"></i>
              </template>
              <router-link :to="getRoutePath('leads')"></router-link>
            </sidenav-item>
          </li>
        </ul>
      </li>

      <!-- Projects -->
      <li v-if="authUser.role !== 'leads' && authUser.role !== 'sales' && authUser.role !== 'contact'" class="nav-item">
        <sidenav-item url="/projects" :class="getRoute() === 'projects' ? 'active' : ''"
          :navText="this.$store.state.isRTL ? 'مشاريع' : 'Projects'">
          <template v-slot:icon>
            <i class="fas fa-tasks text-info text-sm opacity-10"></i>
          </template>
          <router-link to="/projects">Projects</router-link>
        </sidenav-item>
      </li>

      <!--Active Sprints-->
      <li class="nav-item" v-if="authUser.role !== 'leads' && authUser.role !== 'sales' && authUser.role !== 'contact'">
        <sidenav-item url="/active-sprints" :class="getRoute() === 'active-sprints' ? 'active' : ''"
          :navText="this.$store.state.isRTL ? 'مشاريع نشطة' : 'Active Sprints'">
          <template v-slot:icon>
            <i class="fas fa-clock text-info text-sm opacity-10"></i>
          </template>
          <router-link to="/active-sprints">Active Sprints</router-link>
        </sidenav-item>
      </li>

      <!--Backlogs-->
      <li class="nav-item" v-if="authUser.role !== 'leads' && authUser.role !== 'client' && authUser.role !== 'sales' && authUser.role !== 'contact'">
        <sidenav-item url="/backlogs" :class="getRoute() === 'backlogs' ? 'active' : ''"
          :navText="this.$store.state.isRTL ? 'مشاريع نشطة' : 'Backlogs'">
          <template v-slot:icon>
            <i class="fas fa-list-alt text-info text-sm opacity-10"></i>
          </template>
          <router-link to="/backlogs">Backlogs</router-link>
        </sidenav-item>
      </li>

      <!--Issues-->
      <li class="nav-item" v-if="authUser.role !== 'leads' && authUser.role !== 'client' && authUser.role !== 'sales' && authUser.role !== 'contact'">
        <sidenav-item url="/issues" :class="getRoute() === 'issues' ? 'active' : ''"
          :navText="this.$store.state.isRTL ? 'مشاريع نشطة' : 'Issues'">
          <template v-slot:icon>
            <i class="fas fa-exclamation-circle text-info text-sm opacity-10"></i>
          </template>
          <router-link to="/issues">Issues</router-link>
        </sidenav-item>
      </li>

      <!--Investment-->
      <!-- <li
        v-if="authUser.role !== 'admin' && authUser.role !== 'leads' && authUser.role !== 'development' && authUser.role !== 'client' && authUser.role !== 'sales' && authUser.role !== 'contact'"
        class="nav-item">
        <sidenav-item url="/investment" :class="getRoute() === 'tables' ? 'active' : ''"
          :navText="this.$store.state.isRTL ? 'الجداول' : 'Investment'">
          <template v-slot:icon>
            <i class="fa fa-inr text-primary text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li> -->

      <!-- Sales -->
      <li v-if="authUser.role !== 'leads' && authUser.role !== 'development' && authUser.role !== 'client' && authUser.role !== 'contact'"
        class="nav-item">
        <sidenav-item url="/sales" :class="getRoute() === 'billing' ? 'active' : ''"
          :navText="this.$store.state.isRTL ? 'الفواتیر' : 'Sales'">
          <template v-slot:icon>
            <i class="fas fa-shopping-cart text-success text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <!--Leads-->
      <li class="nav-item"
        v-if="authUser.role !== 'development' && authUser.role !== 'client' && authUser.role !== 'sales' && authUser.role !== 'contact'">
        <sidenav-item url="/leads" :class="getRoute() === 'virtual-reality' ? 'active' : ''" :navText="this.$store.state.isRTL ? 'الواقع الافتراضي' : 'Leads'
          ">
          <template v-slot:icon>
            <i class="fa fa-cogs text-primary text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <!-- Profit-->
      <!-- <li class="nav-item"
        v-if="authUser.role !== 'admin' && authUser.role !== 'leads' && authUser.role !== 'development' && authUser.role !== 'client' && authUser.role !== 'sales' && authUser.role !== 'contact'">
        <sidenav-item url="/profit" :class="getRoute() === 'profit' ? 'active' : ''" navText="Profit">
          <template v-slot:icon>
            <i class="fas fa-chart-line text-success text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li> -->

      <!-- Templates -->
      <li class="nav-item"
      v-if="authUser.role == 'contact' && authUser.designation == 'contact'"
      >
        <sidenav-item url="/templates" :class="getRoute() === 'templates' ? 'active' : ''" :navText="this.$store.state.isRTL ? 'الواقع الافتراضي' : 'Templates'
          ">

          <template v-slot:icon>
            <i class="fa fa-cogs text-primary text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item"
      v-if="authUser.role == 'contact' && authUser.designation == 'contact'">
        <sidenav-item url="/template2" :class="getRoute() === 'template2' ? 'active' : ''" navText="Template2">
          <template v-slot:icon>
            <i class="fa fa-cogs text-primary text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>


      <li class="mt-3 nav-item">
        <h6 v-if="this.$store.state.isRTL" class="text-xs ps-4 text-uppercase font-weight-bolder opacity-6"
          :class="this.$store.state.isRTL ? 'me-4' : 'ms-2'">
          صفحات المرافق
        </h6>
        <h6 v-else class="text-xs ps-4 text-uppercase font-weight-bolder opacity-6"
          :class="this.$store.state.isRTL ? 'me-4' : 'ms-2'">
          ACCOUNT
        </h6>
      </li>

      <li class="nav-item">
        <sidenav-item url="/profile" :class="getRoute() === 'profile' ? 'active' : ''"
          :navText="this.$store.state.isRTL ? 'حساب تعريفي' : 'Profile'">
          <template v-slot:icon>
            <i class="ni ni-single-02 text-dark text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>


    </ul>
    <ul class="navbar-nav" v-else>
      <li class="nav-item">
        <sidenav-item url="/dashboard" :class="getRoute() === 'dashboard' ? 'active' : ''"
          :navText="this.$store.state.isRTL ? 'لوحة القيادة' : 'Dashboard'">

          <template v-slot:icon>
            <i class="ni ni-tv-2 text-primary text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="mt-3 nav-item">
        <h6 v-if="this.$store.state.isRTL" class="text-xs ps-4 text-uppercase font-weight-bolder opacity-6"
          :class="this.$store.state.isRTL ? 'me-4' : 'ms-2'">
          صفحات المرافق
        </h6>
        <h6 v-else class="text-xs ps-4 text-uppercase font-weight-bolder opacity-6"
          :class="this.$store.state.isRTL ? 'me-4' : 'ms-2'">
          ACCOUNT
        </h6>
      </li>
      <li class="nav-item">
        <sidenav-item url="/profile" :class="getRoute() === 'profile' ? 'active' : ''"
          :navText="this.$store.state.isRTL ? 'حساب تعريفي' : 'Profile'">

          <template v-slot:icon>
            <i class="ni ni-single-02 text-dark text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
    </ul>
  </div>
</template>

<script>
import SidenavItem from "./SidenavItem.vue";
import { mapState } from 'vuex'

export default {
  name: "SidenavList",
  props: {
    cardBg: String
  },
  components: {
    SidenavItem,
  },
  data() {
    return {
      isCollapseShow: false,
      isAreaExpended: false,
      title: "Argon Dashboard 2",
      controls: "dashboardsExamples",
      isActive: "active",
      isEmploymentDropdownOpen: false,
      isProjectDropdownOpen: false,
      projectId: localStorage.getItem('projectId')
    }
  },
  methods: {
    isEmployeeActive() {
      if (this.getRoute() === 'development' ||
        this.getRoute() === 'sales' ||
        this.getRoute() === 'hrms') {
        console.log(true)
      } else {
        console.log(false)
      }
    },
    colapseShowTogeller() {
      this.isCollapseShow = !this.isCollapseShow;
    },
    isAreaExpendedTogeller() {
      this.isAreaExpended = !this.isAreaExpended;
    },
    getRoutePath(val) {
      const prefixURL = '/employees';
      return `${prefixURL}/${val}`;
    },
    getRoute() {
      const routeArr = this.$route.path.split("/");
      return routeArr[1];
    },
    toggleEmploymentDropdown() {
      this.isEmploymentDropdownOpen = true;
    },
    toggleProjectDropdown() {
      this.isProjectDropdownOpen = !this.isProjectDropdownOpen;
    },
    closeEmploymentDropdown(event) {
      if (
        this.isEmploymentDropdownOpen &&
        !this.$refs.employmentDropdown.contains(event.target)
      ) {
        this.isEmploymentDropdownOpen = false;
      }
    },
    closeDropdownOnSidebarClick() {
      this.isEmploymentDropdownOpen = false;
    }
  },
  computed: {
    ...mapState(['authUser']),

    mounted() {
      return document.addEventListener("click", this.closeEmploymentDropdown);
    },
    beforeUnmount() {
      return document.removeEventListener("click", this.closeEmploymentDropdown);
    },
  }
}
</script>

<style>
.emp-li {
  margin-left: 30px !important;
}
</style>