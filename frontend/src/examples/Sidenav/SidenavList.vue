<template>
  <div class="collapse navbar-collapse w-auto h-auto h-100" id="sidenav-collapse-main">
    <ul class="navbar-nav">
      <li class="nav-item">
        <sidenav-item url="/dashboard" :class="getRoute() === 'dashboard' ? 'active' : ''"
          :navText="this.$store.state.isRTL ? 'لوحة القيادة' : 'Dashboard'">
          <template v-slot:icon>
            <i class="ni ni-tv-2 text-primary text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <li @click="isAreaExpendedTogeller(), colapseShowTogeller()" class="nav-item">
        <sidenav-item url="" :class="{
          'active': getRoute() === '',
          'collapsed': isCollapseShow
        }" :navText="this.$store.state.isRTL ? 'لوحة القيادة' : 'Employees'" data-toggle="collapse"
          :aria-expanded="isAreaExpended">
          <template v-slot:icon>
            <i class="ni ni-tv-2 text-primary text-sm opacity-10"></i>
          </template>
          <!-- <span class="ml-4"></span> -->
          <!-- <i class="las la-angle-right iq-arrow-right arrow-active"></i>
          <i class="las la-angle-down iq-arrow-right arrow-hover"></i> -->
        </sidenav-item>
        <ul id="" class="iq-submenu collapse list-unstyled" :class="{ 'show': isCollapseShow }"
          data-parent="#iq-sidebar-toggle">
          <li class="nav-item">
            <sidenav-item class="emp-li" :url="getRoutePath('Development')" :class="getRoute() === 'dashboard collapsed' ? 'active' : ''"
              :navText="this.$store.state.isRTL ? 'لوحة القيادة' : 'Development'" data-toggle="collapse"
              aria-expanded="false">
              <template v-slot:icon>
                <i class="ni ni-tv-2 text-primary text-sm opacity-10"></i>
              </template>
              <router-link :to="getRoutePath('Development')"> <span class="ml-0">Development</span></router-link>

            </sidenav-item>
          </li>
          <li class=" ">
            <sidenav-item class="emp-li" :url="getRoutePath('sales')" :class="getRoute() === 'dashboard collapsed' ? 'active' : ''"
              :navText="this.$store.state.isRTL ? 'لوحة القيادة' : 'Sales'" data-toggle="collapse" aria-expanded="false">
              <template v-slot:icon>
                <i class="ni ni-tv-2 text-primary text-sm opacity-10"></i>
              </template>
              <router-link :to="getRoutePath('sales')"></router-link>
            </sidenav-item>
          </li>
          <li class=" ">
            <sidenav-item class="emp-li" :url="getRoutePath('hrms')" :class="getRoute() === 'dashboard collapsed' ? 'active' : ''"
              :navText="this.$store.state.isRTL ? 'لوحة القيادة' : 'HRMS'" data-toggle="collapse" aria-expanded="false">
              <template v-slot:icon>
                <i class="ni ni-tv-2 text-primary text-sm opacity-10"></i>
              </template>
              <router-link :to="getRoutePath('hrms')"></router-link>
            </sidenav-item>
          </li>
        </ul>
      </li>
      <li class="nav-item">
        <sidenav-item url="/tables" :class="getRoute() === 'tables' ? 'active' : ''"
          :navText="this.$store.state.isRTL ? 'الجداول' : 'Tables'">
          <template v-slot:icon>
            <i class="ni ni-calendar-grid-58 text-warning text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item">
        <sidenav-item url="/billing" :class="getRoute() === 'billing' ? 'active' : ''"
          :navText="this.$store.state.isRTL ? 'الفواتیر' : 'Billing'">
          <template v-slot:icon>
            <i class="ni ni-credit-card text-success text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item">
        <sidenav-item url="/virtual-reality" :class="getRoute() === 'virtual-reality' ? 'active' : ''" :navText="this.$store.state.isRTL ? 'الواقع الافتراضي' : 'Virtual Reality'
          ">
          <template v-slot:icon>
            <i class="ni ni-app text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item">
        <sidenav-item url="/rtl-page" :class="getRoute() === 'rtl-page' ? 'active' : ''" navText="RTL">
          <template v-slot:icon>
            <i class="ni ni-world-2 text-danger text-sm opacity-10"></i>
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
          ACCOUNT PAGES
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
      <li class="nav-item">
        <sidenav-item url="/signin" :class="getRoute() === 'signin' ? 'active' : ''"
          :navText="this.$store.state.isRTL ? 'تسجيل الدخول' : 'Sign In'">
          <template v-slot:icon>
            <i class="ni ni-single-copy-04 text-danger text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item">
        <sidenav-item url="/signup" :class="getRoute() === 'signup' ? 'active' : ''"
          :navText="this.$store.state.isRTL ? 'اشتراك' : 'Sign Up'">
          <template v-slot:icon>
            <i class="ni ni-collection text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
    </ul>
  </div>
  <div class="pt-3 mx-3 mt-3 sidenav-footer">
    <sidenav-card :class="cardBg" textPrimary="Need Help?" textSecondary="Please check our docs" />
  </div>
</template>
<script>
import SidenavItem from "./SidenavItem.vue";
import SidenavCard from "./SidenavCard.vue";

// export default {
// name: "SidenavList",
// props: {
//   cardBg: String
// },
// data() {
//   return {
//     title: "Argon Dashboard 2",
//     controls: "dashboardsExamples",
//     isActive: "active"
//   };
// },
// components: {
//   SidenavItem,
//   SidenavCard
// },
// methods: {
//   getRoute() {
//     const routeArr = this.$route.path.split("/");
//     return routeArr[1];
//   }
// }
// };
export default {
  name: "SidenavList",
  props: {
    cardBg: String
  },
  components: {
    SidenavItem,
    SidenavCard
  },
  data() {
    return {
      isCollapseShow: false,
      isAreaExpended: false,
      title: "Argon Dashboard 2",
      controls: "dashboardsExamples",
      isActive: "active"
    }
  },
  methods: {
    colapseShowTogeller() {
      this.isCollapseShow = !this.isCollapseShow
    },
    isAreaExpendedTogeller() {
      this.isAreaExpended = !this.isAreaExpended
    },
    getRoutePath(val) {
      const prefixURL = '/employees'
      let urlP = `${prefixURL}/${val}`
      return urlP
    },
    getRoute() {
      const routeArr = this.$route.path.split("/");
      return routeArr[1];
    }
  }
}
</script>
<style>
.emp-li{
  margin-left: 30px !important;
}
</style>