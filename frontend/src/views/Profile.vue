<template>
  <main>
    <div class="container-fluid">
      <div class="page-header min-height-300" style="
          background-image: url('https://images.unsplash.com/photo-1531512073830-ba890ca4eba2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80');
          margin-right: -24px;
          margin-left: -34%;
        ">
        <span class="mask bg-gradient-success opacity-6"></span>
      </div>
      <div class="card shadow-lg mt-n6">
        <div class="card-body p-3">
          <div class="row gx-4">
            <div class="col-auto">
              <div class="avatar avatar-xl position-relative">
                <img src="../assets/img/team-1.jpg" alt="profile_image" class="shadow-sm w-100 border-radius-lg" />
              </div>
            </div>
            <div class="col-auto my-auto">
              <div class="h-100">
                <h5 class="mb-1">Sayo Kravits</h5>
                <p class="mb-0 font-weight-bold text-sm">Public Relations</p>
              </div>
            </div>
            <div class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0">
              <div class="nav-wrapper position-relative end-0">
                <ul class="p-1 bg-transparent nav nav-pills" role="tablist">
                  <li class="nav-item col-lg-auto col-md-auto col-sm-auto w-100" style="width: 200px !important;"
                    @click="doLogout">
                    <button style="width: 150px !important; height: 35px !important;" class="btn btn-sm btn-dark float-right mb-0 px-2 py-1 mb-0 nav-link active">
                      <span class="ms-1" style="color: white;">Logout</span>
                    </button>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="py-4 container-fluid">
      <div class="row">
        <div class="col-md-12">
          <div class="card">
            <div class="card-header pb-0">
              <div class="d-flex align-items-center">
                <p class="mb-0">Edit Profile</p>
                <argon-button color="success" size="sm" class="ms-auto">Save</argon-button>
              </div>
            </div>
            <div class="card-body">
              <p class="text-uppercase text-sm">User Information</p>
              <div class="row">
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label">Username</label>
                  <argon-input type="text" value="lucky.jesse" />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label">Email address</label>
                  <argon-input type="email" value="jesse@example.com" />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label">First name</label>
                  <input class="form-control" type="text" value="Jesse" />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label">Last name</label>
                  <argon-input type="text" value="Lucky" />
                </div>
              </div>
              <hr class="horizontal dark" />
              <p class="text-uppercase text-sm">Contact Information</p>
              <div class="row">
                <div class="col-md-12">
                  <label for="example-text-input" class="form-control-label">Address</label>
                  <argon-input type="text" value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09" />
                </div>
                <div class="col-md-4">
                  <label for="example-text-input" class="form-control-label">City</label>
                  <argon-input type="text" value="New York" />
                </div>
                <div class="col-md-4">
                  <label for="example-text-input" class="form-control-label">Country</label>
                  <argon-input type="text" value="United States" />
                </div>
                <div class="col-md-4">
                  <label for="example-text-input" class="form-control-label">Postal code</label>
                  <argon-input type="text" value="437300" />
                </div>
              </div>
              <hr class="horizontal dark" />
              <p class="text-uppercase text-sm">About me</p>
              <div class="row">
                <div class="col-md-12">
                  <label for="example-text-input" class="form-control-label">About me</label>
                  <argon-input type="text" value="A beautiful Dashboard for Bootstrap 5. It is Free and Open Source." />
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- <div class="col-md-4">
          <profile-card />
        </div> -->
      </div>
    </div>
  </main>
</template>

<script>
import setNavPills from "@/assets/js/nav-pills.js";
import setTooltip from "@/assets/js/tooltip.js";
// import ProfileCard from "./components/ProfileCard.vue";
import ArgonInput from "@/components/ArgonInput.vue";
import ArgonButton from "@/components/ArgonButton.vue";
import { mapState, mapMutations, mapActions } from "vuex";
import axios from "axios";
import Noty from "noty";
import router from "@/router";

const body = document.getElementsByTagName("body")[0];

export default {
  name: "profile",
  computed: {
    ...mapState(["authToken", "authUser"]),
    ...mapMutations(["setAuthToken", "setAuthUser"]),
  },
  data() {
    return {
      showMenu: false
    };
  },
  components: {
    // ProfileCard, 
    ArgonInput, ArgonButton
  },
  methods: {
    ...mapActions(["logout"]),
    toggleShowClass() {
      this.isshowActivated = !this.isshowActivated;
    },
    fixedNavbar() {
      this.isFixedNavbar = window.scrollY > 1
    },
    doLogout() {
      axios.get('http://127.0.0.1:8000/api/logout/').
        then((r) => {
          if (r.status == 200) {
            new Noty({
              type: 'success',
              text: r.data.message,
              timeout: 500,
              layout: 'topCenter'
            }).show()
            this.logout()
            // window.location.reload();
            setTimeout(() => {
              router.push('/signin')
            }, 1000)
          }
        })
    },
  },
  mounted() {
    this.$store.state.isAbsolute = true;
    setNavPills();
    setTooltip();
  },
  beforeMount() {
    this.$store.state.imageLayout = "profile-overview";
    this.$store.state.showNavbar = false;
    this.$store.state.showFooter = true;
    this.$store.state.hideConfigButton = true;
    body.classList.add("profile-overview");
  },
  beforeUnmount() {
    this.$store.state.isAbsolute = false;
    this.$store.state.imageLayout = "default";
    this.$store.state.showNavbar = true;
    this.$store.state.showFooter = true;
    this.$store.state.hideConfigButton = false;
    body.classList.remove("profile-overview");
  }
};
</script>
