<template>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Webkit | Responsive Bootstrap 4 Admin Dashboard Template</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
  </head>
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
                <h5 class="mb-1">{{ authUser.name }}</h5>
                <p class="mb-0 font-weight-bold text-sm">{{ authUser.email }}</p>
              </div>
            </div>
            <div class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0">
              <div class="nav-wrapper position-relative end-0">
                <ul class="p-1 bg-transparent nav nav-pills" role="tablist">
                  <li class="nav-item col-lg-auto col-md-auto col-sm-auto w-100" style="width: 200px !important;"
                    @click="doLogout">
                    <button style="width: 150px !important; height: 35px !important;"
                      class="btn btn-sm btn-dark float-right mb-0 px-2 py-1 mb-0 nav-link active">
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
                <argon-button color="success" size="sm" class="ms-auto" @click="saveChanges()">Save</argon-button>
              </div>
            </div>
            <div class="card-body">
              <p class="text-uppercase text-sm">User Information</p>
              <div class="mb-3 col-md-6">
                <label for="profileImage" class="form-label">Profile Picture</label>
                <input type="file" class="form-control" id="profileImage" @change="onImageChange" />
              </div>
              <div class="row">
                <div class="col-md-6">
                  <label for="name" class="form-control-label">Name</label>
                  <input class="form-control" type="text" v-model="userData.name" />
                </div>
                <div class="col-md-6">
                  <label for="email" class="form-control-label">Email address</label>
                  <input class="form-control" disabled type="email" v-model="userData.email" />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label">Designation</label>
                  <input class="form-control" disabled type="text" v-model="userData.designation" />
                </div>
                <div class="col-md-6">
                  <label for="example-text-input" class="form-control-label">Role</label>
                  <input class="form-control" disabled type="text" v-model="userData.role" />
                </div>
              </div>
              <hr class="horizontal dark" />
              <p class="text-uppercase text-sm">Contact Information</p>
              <div class="row">
                <div class="col-md-4">
                  <label for="example-text-input" class="form-control-label">Mobile Number</label>
                  <input class="form-control" type="text" v-model="userData.contact_no" />
                </div>
                <div class="col-md-4">
                  <label for="example-text-input" class="form-control-label">Postal code</label>
                  <input class="form-control" type="text" v-model="userData.pincode" />
                </div>
              </div>
              <p class="text-uppercase text-sm" style="margin-top: 30px;">Change Password</p>
              <div class="row">
                <div class="col-md-4">
                  <label for="example-text-input" class="form-control-label">Old Password</label>
                  <input class="form-control" type="password" v-model="userData.oldPassword" />
                </div>
                <div class="col-md-4">
                  <label for="example-text-input" class="form-control-label">New Password</label>
                  <input class="form-control" type="password" :disabled="!userData.oldPassword"
                    v-model="userData.newPassword" />
                </div>
                <div class="col-md-4">
                  <label for="example-text-input" class="form-control-label">Confirm Password</label>
                  <input class="form-control" type="password" :disabled="!userData.oldPassword"
                    v-model="userData.confirmPassword" />
                </div>
              </div>
              <hr class="horizontal dark" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import setNavPills from "@/assets/js/nav-pills.js";
import setTooltip from "@/assets/js/tooltip.js";
import ArgonButton from "@/components/ArgonButton.vue";
import { mapState, mapMutations, mapActions } from "vuex";
import axios from "axios";
import Noty from "noty";
import router from "@/router";
import { BASE_URL } from "../config/apiConfig";

const body = document.getElementsByTagName("body")[0];

export default {
  name: "profile",
  computed: {
    ...mapState(["authToken", "authUser"]),
    ...mapMutations(["setAuthToken", "setAuthUser"]),
  },
  data() {
    return {
      showMenu: false,
      userData: {
        name: '',
        email: '',
        designation: '',
        role: '',
        contact_no: '',
        pincode: '',
        password: '',
        oldPassword: '',
        newPassword: '',
        confirmPassword: '',
      }
    };
  },
  components: {
    ArgonButton
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
      const role = localStorage.getItem('role')
      axios.get(`${BASE_URL}api/logout/`).
        then((r) => {
          if (r.status == 200) {
            new Noty({
              type: 'success',
              text: r.data.message,
              timeout: 1000,
              layout: 'topCenter'
            }).show()
            if (role === 'client') {
              router.push('/client-signin')
            } else {
              router.push('/signin')
            }
            this.logout()
          }
        })
    },
    async saveChanges() {
      if (this.userData.newPassword && this.userData.newPassword !== this.confirmPassword) {
        new Noty({
          type: 'error',
          text: "Confirm Password should be the same as New Password!",
          timeout: 1000,
          layout: 'topCenter'
        }).show();
        return;
      }
      // console.log(this.userData);
      // try {
      //   const response =  await axios.put(`${BASE_URL}api/user`, this.userData)
      //   console.log(response.data);
      // } catch (error) {
      //   console.log(error);
      // }
    },
    onImageChange(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onloadend = () => {
          this.userData.profileImage = reader.result;
        };
        reader.readAsDataURL(file);
      }
    }
  },
  mounted() {
    this.$store.state.isAbsolute = true;
    setNavPills();
    setTooltip();
    this.userData = { ...this.authUser };
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
<style>
</style>
