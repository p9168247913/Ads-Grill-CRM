<template>
  <div v-show="this.$store.state.layout === 'default'" class="min-height-400 position-absolute w-100"
    :class="`${this.$store.state.darkMode ? 'bg-transparent' : 'bg-custom1'}`"></div>
  <aside style="z-index: 3 !important;"
    class="my-3 overflow-auto border-0 sidenav navbar navbar-vertical navbar-expand-xs border-radius-xl" :class="`${this.$store.state.isRTL
      ? 'me-3 rotate-caret fixed-end'
      : 'fixed-start ms-3'
      } 
          ${this.$store.state.layout === 'landing'
        ? 'bg-transparent shadow-none'
        : ' '
      } ${this.$store.state.sidebarType}`" id="sidenav-main">
    <div class="sidenav-header">
      <i class="top-0 p-3 cursor-pointer fas fa-times text-secondary opacity-5 position-absolute end-0 d-none d-xl-none"
        aria-hidden="true" id="iconSidenav"></i>
      <li class="nav-item d-xl-none ps-3 d-flex flex-row-reverse align-items-end ">
        <button href="#" @click="toggleSidebar" class="p-0 nav-link text-white cross-button" id="iconNavbarSidenav">
          <div class="sidenav-toggler-inner">
            <i style=" color: black" class="fas fa-times"></i>
          </div>
        </button>
      </li>
      <router-link style="height:auto;" class="p-4 mb-3" to="">
        <img @click="home" style="width: 150px; height:58px; margin-top: 20px;" src="../../assets/img/logos/ag_logo.png"
          alt="main_logo" />
      </router-link>
    </div>
    <hr class="mt-1 horizontal dark" />
    <sidenav-list :cardBg="custom_class" class="mt-4" />
  </aside>
</template>
<script>
import SidenavList from "./SidenavList.vue";
import logo from "@/assets/img/logo-ct-dark.png";
import logoWhite from "@/assets/img/logo-ct.png";
import { mapMutations, mapActions, mapState } from "vuex";
import router from "@/router";

export default {
  name: "index",
  components: {
    SidenavList
  },
  data() {
    return {
      logo,
      logoWhite
    };
  },
  props: ["custom_class", "layout"],
  computed:{
    ...mapState(["authToken", "authUser"]),
  },
  methods: {
    ...mapMutations(["navbarMinimize", "toggleConfigurator"]),
    ...mapActions(["toggleSidebarColor"]),
    toggleSidebar() {
      this.toggleSidebarColor("bg-white");
      this.navbarMinimize();
    },
    home() {
      console.log(this.authUser.role);
      if (this.authUser.role === 'development') {
        router.push('/projects')
      } else {
        router.push('/dashboard')
      }
    }
  }
};
</script>
<style scoped>
.cross-button {
  margin-right: 20px;
  background-color: white;
  border: none;
  transform: scale(1.4);
  margin-top: 10px;
}

#sidenav-main {
  overflow: auto;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

#sidenav-main::-webkit-scrollbar {
  display: none;
}

.bg-custom1 {
  background-image: linear-gradient(to top, #37ecba 0%, #72afd3 100%);
}
</style>
