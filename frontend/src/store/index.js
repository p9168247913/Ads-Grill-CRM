import { createStore } from 'vuex';

const store = createStore({
  state: {
    authToken: localStorage.getItem('token') || null,
    authUser:{
      email: localStorage.getItem('email') || "",
      role:localStorage.getItem('role') || "",
      name: localStorage.getItem('name') || "",
      contact_no: localStorage.getItem('contact_no') || "",
      pincode: localStorage.getItem('pincode') || "",
      designation: localStorage.getItem('designation') || ""
    },
  },
  mutations: {
    setAuthToken(state, token) {
      state.authToken = token;
      localStorage.setItem('token', token)
    },
    setAuthUser(state, user) {
      state.authUser = user
      localStorage.setItem('email', user.email)
      localStorage.setItem('role', user.role)
      localStorage.setItem('name', user.name)
      localStorage.setItem('contact_no', user.contact_no)
      localStorage.setItem('pincode', user.pincode)
      localStorage.setItem('designation', user.designation)
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
    }
  },
  actions: {
    logout({commit}){
      commit('clearAuthUser')
      commit('setAuthToken', null)
    }
  },
  getters: {
    isAuthenticated: (state) => !!state.authToken,
  },

})

export default store

