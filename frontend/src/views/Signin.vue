<template>

  <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
  </head>
  <div class="container top-0 position-sticky z-index-sticky">
    <div class="row">
      <div class="col-12">
      </div>
    </div>
  </div>
  <main class="mt-0 main-content">
    <section>
      <div class="page-header min-vh-100">
        <div class="container">
          <div class="row">
            <div class="mx-auto col-xl-4 col-lg-5 col-md-7 d-flex flex-column mx-lg-0">
              <div style="margin: auto;">
                <img src="../assets/img/logos/ag_logo.png" style=" width: 150px !important;" alt="">
              </div>
              <div class="card card-plain"
                style="margin-top: 20px; box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px !important;">
                <div class="pb-0 card-header text-start">
                  <h4 class="font-weight-bolder"><u>Sign In</u></h4>
                  <p class="mb-0">Enter your email and password to sign in</p>
                </div>
                <div class="card-body">
                  <form role="form">
                    <div class="col-md-10 col-lg-12 col-sm-12 mb-3">
                      <div class="input-group">
                        <input v-model="email" type="email" class="form-control" placeholder="Email.." />
                      </div><br />
                      <div class="input-group">
                        <input v-model="pswd" type="password" class="form-control" placeholder="Password" size="lg" />
                      </div>
                    </div>
                    <div class="mb-3">
                    </div>
                    <argon-switch id="rememberMe">Remember me</argon-switch>
                    <div class="text-center">
                      <argon-button class="mt-4" variant="gradient" color="success" fullWidth size="lg"
                        @click="doLogin">Sign in</argon-button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
            <div
              class="top-0 my-auto text-center col-6 d-lg-flex d-none h-100 pe-0 position-absolute end-0 justify-content-center flex-column">
              <div
                class="position-relative bg-gradient-primary h-100 m-3 px-7 border-radius-lg d-flex flex-column justify-content-center overflow-hidden"
                style="background-size: cover;">
                <span class="mask bg-gradient-success opacity-6"></span>
                <img src="../assets/img/login/01.png" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import ArgonSwitch from "@/components/ArgonSwitch.vue";
import ArgonButton from "@/components/ArgonButton.vue";
import Noty from "noty"
import axios from "axios"
import { mapMutations } from "vuex";
import { mapState } from "vuex";
import router from "@/router";
const body = document.getElementsByTagName("body")[0];
import { BASE_URL } from "../config/apiConfig";

export default {
  name: "signin",
  components: {
    ArgonSwitch,
    ArgonButton,
  },
  created() {
    this.$store.state.hideConfigButton = true;
    this.$store.state.showNavbar = false;
    this.$store.state.showSidenav = false;
    this.$store.state.showFooter = false;
    body.classList.remove("bg-gray-100");
  },
  beforeUnmount() {
    this.$store.state.hideConfigButton = false;
    this.$store.state.showNavbar = true;
    this.$store.state.showSidenav = true;
    this.$store.state.showFooter = true;
    body.classList.add("bg-gray-100");
  },
  data() {
    return {
      email: '',
      pswd: '',
      loading: false,
    }
  },
  computed: {
    ...mapState(['authToken', 'authUser'])
  },
  methods: {
    ...mapMutations(['setAuthToken', 'setAuthUser']),
    async doLogin(e) {
      e.preventDefault();
      if (!this.email) {
        new Noty({
          type: 'warning',
          text: 'Please enter email',
          timeout: 3000,
          layout: 'topCenter'
        }).show();
        return;
      }
      if (!this.pswd) {
        new Noty({
          type: 'warning',
          text: 'Please enter password',
          timeout: 3000,
          layout: 'topCenter'
        }).show();
        return;
      }
      try {
        this.$store.commit('showLoader')
        const response = await axios.post(`${BASE_URL}api/login/`, {
          "username": this.email,
          "password": this.pswd
        })
        if (response.data.status == 'Success') {
          new Noty({
            type: 'success',
            text: response.data.message,
            timeout: 1000,
            layout: 'topCenter'
          }).show()
          this.storeAuthToken(response.headers['token'], response.data.user)
          setTimeout(() => {
            if (this.authUser.role == "development") {
              router.push('/projects')
              this.$store.commit('hideLoader')
            }
            else { 
              router.push('/dashboard') 
              this.$store.commit('hideLoader')
            }
          }, 1000);
          this.$store.commit('hideLoader')
        }
        else if (response.data.status == 'Failed') {
          new Noty({
            type: 'error',
            text: response.data.message,
            timeout: 3000,
            layout: 'topCenter'
          }).show()
          this.$store.commit('hideLoader')
        }
        this.$store.commit('hideLoader')
      } catch (error) {
        new Noty({
          type: 'error',
          text: error.response.data.message ? error.response.data.message :error.response.data.detail,
          timeout: 3000,
          layout: 'topCenter'
        }).show()
        this.$store.commit('hideLoader')
      }
    },
    storeAuthToken(token, user) {
      if (token !== 'undefined' && user) {
        this.setAuthToken(token)
        this.setAuthUser(user)
      }
    },
  },
};

</script>
