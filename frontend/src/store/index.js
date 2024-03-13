import { createStore } from "vuex";

export default createStore({
  state: {
    isLoading:false,
    authClient:{
      email: localStorage.getItem('email') || "",
      role:localStorage.getItem('role') || "",
      name: localStorage.getItem('name') || "",
    },
    authToken: localStorage.getItem('token') || '',
    authUser:{
      id:localStorage.getItem('id') || "",
      email: localStorage.getItem('email') || "",
      role:localStorage.getItem('role') || "",
      name: localStorage.getItem('name') || "",
      contact_no: localStorage.getItem('contact_no') || "",
      pincode: localStorage.getItem('pincode') || "",
      designation: localStorage.getItem('designation') || "",
      profile_pic:localStorage.getItem('profile_pic') || ""
    },
    hideConfigButton: false,
    isPinned: true,
    showConfig: false,
    sidebarType: "bg-white",
    isRTL: false,
    mcolor: "",
    darkMode: false,
    isNavFixed: false,
    isAbsolute: false,
    showNavs: true,
    showSidenav: true,
    showNavbar: true,
    showFooter: true,
    showMain: true,
    layout: "default"
  },
  mutations: {
    toggleConfigurator(state) {
      state.showConfig = !state.showConfig;
    },
    navbarMinimize(state) {
      const sidenav_show = document.querySelector(".g-sidenav-show");

      if (sidenav_show.classList.contains("g-sidenav-hidden")) {
        sidenav_show.classList.remove("g-sidenav-hidden");
        sidenav_show.classList.add("g-sidenav-pinned");
        state.isPinned = true;
      } else {
        sidenav_show.classList.add("g-sidenav-hidden");
        sidenav_show.classList.remove("g-sidenav-pinned");
        state.isPinned = false;
      }
    },
    sidebarType(state, payload) {
      state.sidebarType = payload;
    },
    navbarFixed(state) {
      if (state.isNavFixed === false) {
        state.isNavFixed = true;
      } else {
        state.isNavFixed = false;
      }
    },
    setAuthToken(state, token) {
      state.authToken = token;
      localStorage.setItem('token', token)
    },
    setAuthUser(state, user) {
      state.authUser = user
      localStorage.setItem('id', user.id)
      localStorage.setItem('email', user.email)
      localStorage.setItem('role', user.role)
      localStorage.setItem('name', user.name)
      localStorage.setItem('contact_no', user.contact_no)
      localStorage.setItem('pincode', user.pincode)
      localStorage.setItem('designation', user.designation)
      localStorage.setItem('profile_pic', user.profile_pic)
    },
    setAuthClient(state, user) {
      state.authClient = user
      localStorage.setItem('email', user.email)
      localStorage.setItem('role', user.role)
      localStorage.setItem('name', user.name)
    },
    clearAuthClient(state){
      state.authClient = {
        email: "",
        role: "",
        name:''
      };
      localStorage.removeItem('email')
      localStorage.removeItem('role')
      localStorage.removeItem('name')
      localStorage.removeItem('projectId')
      localStorage.removeItem('id')
    },
    clearAuthUser(state){
      state.authUser = {
        email: "",
        role: ""
      };
      localStorage.removeItem('email')
      localStorage.removeItem('role')
      localStorage.removeItem('name')
      localStorage.removeItem('contact_no')
      localStorage.removeItem('pincode')
      localStorage.removeItem('designation')
      localStorage.removeItem('profile_pic')
      localStorage.removeItem('projectId')
      localStorage.removeItem('id')
    },
    clearAuthToken(){
      localStorage.removeItem("token")
      this.state.authToken=''
    },
    showLoader(state){
      state.isLoading = true
    },
    hideLoader(state){
      state.isLoading=false
    }
  },
  actions: {
    toggleSidebarColor({ commit }, payload) {
      commit("sidebarType", payload);
    },
    logout({commit}){
      commit('clearAuthUser')
      commit('clearAuthToken', "")
    }
  },
  getters: {
    isAuthenticated: (state) => !!state.authToken,
  }
});
