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
          background-image: linear-gradient(to top, #37ecba 0%, #72afd3 100%);
          margin-right: -24px;
          margin-left: -34%;
        ">
        <span class="mask bg-gradient-success opacity-6"></span>
      </div>
      <div class="card shadow-lg mt-n12">
        <div class="card-body p-3">
          <div class="row gx-4">
            <div class="col-auto">
              <div class="avatar avatar-xl position-relative">
                <img :src="getProfilePic(userData)"
                  alt="profile_image" class="shadow-sm w-100 border-radius-lg" />
              </div>
            </div>
            <div class="col-auto my-auto">
              <div class="h-100">
                <h5 class="mb-1">{{ authUser.name }}</h5>
                <p class="mb-0 font-weight-bold text-sm">{{ authUser.email }}</p>
              </div>
            </div>
            <div class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0" style=" z-index: 0;">
              <div class="nav-wrapper position-relative end-0">
                <ul class="p-1 bg-transparent nav nav-pills" role="tablist">
                  <li class="nav-item col-lg-auto col-md-auto col-sm-auto w-100" style="width: 200px !important;"
                    @click="doLogout">
                    <button style="width: 120px !important; height: 40px !important; z-index: 0 !important;"
                      class="btn btn-sm btn-dark float-right nav-link active ">
                      <i class="bi bi-box-arrow-right" style="color: white; height: 20px"></i> &nbsp;&nbsp;
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
                <argon-button color="success" size="sm" class="ms-auto" @click="confirmSaveChanges()"> <i
                    class="bi bi-save-fill" style="color: white;"></i> &nbsp;&nbsp; Save</argon-button>
              </div>
            </div>
            <div class="card-body">
              <p class="text-uppercase text-sm">User Information</p>
              <div class="mb-3 col-md-6">
                <label for="profileImage" class="form-label">Profile Picture</label>
                <input accept=".jpeg, .png, .jpg" type="file" class="form-control" id="profileImage"
                  @change="onImageChange($event)" />
              </div>
              <div class="row">
                <div class="col-md-6">
                  <label for="name" class="form-control-label">Name</label>
                  <input class="form-control" type="text" v-model="capitalizedName" />
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
                  <input class="form-control" type="password" :disabled="!userData.oldPassword && userData.newPassword"
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
import Swal from 'sweetalert2';
import Noty from "noty";
import router from "@/router";
import { BASE_URL } from "../config/apiConfig";
import defaultProfilePic from "../assets/img/User_Image.png"

const body = document.getElementsByTagName("body")[0];

export default {
  name: "profile",
  computed: {
    ...mapState(["authToken", "authUser"]),
    ...mapMutations(["setAuthToken", "setAuthUser"]),
    capitalizedName: {
      get() {
        return this.userData.name;
      },
      set(value) {
        const formattedName = value.replace(/\b\w/g, (match) => match.toUpperCase());
        this.userData.name = formattedName;
      }
    }
  },
  data() {
    return {
      showMenu: false,
      selectedFiles: [],
      userData: {
        id: '',
        name: '',
        email: '',
        designation: '',
        role: '',
        contact_no: '',
        profile_pic: '',
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
    getProfilePic(manager) {
      return manager.profile_pic ? `data:image/jpeg;base64,${manager.profile_pic}` : defaultProfilePic;
    }, 
    toggleShowClass() {
      this.isshowActivated = !this.isshowActivated;
    },
    fixedNavbar() {
      this.isFixedNavbar = window.scrollY > 1
    },
    async doLogout() {
      const result = await Swal.fire({
        title: 'Are you sure you want to logout?',
        text: "You will be logged out of your account.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: '✔ Yes, logout',
        cancelButtonText: '✖ No, stay'
      });

      if (result.isConfirmed) {
        try {
          const response = await axios.get(`${BASE_URL}api/logout/`);
          if (response.status === 200) {
            new Noty({
              type: 'success',
              text: response.data.message,
              timeout: 1000,
              layout: 'topCenter'
            }).show();
            router.push('/signin');
            this.logout();
          }
        } catch (error) {
          new Noty({
            type: 'error',
            text: error.response?.data?.detail || error.response?.data?.message || 'An error occurred during logout',
            timeout: 1000,
          }).show();
        }
      }
    },
    async confirmSaveChanges() {
      const result = await Swal.fire({
        title: 'Are you sure you want to save changes?',
        text: "Any unsaved changes will be lost if you navigate away from this page.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: '✔ Yes, save changes',
        cancelButtonText: '✖ No, cancel'
      });

      if (result.isConfirmed) {
        await this.saveChanges();
      }
    },
    async saveChanges() {
      try {
        this.$store.commit('showLoader');
        const formData = new FormData();

        if (this.userData.oldPassword && this.userData.newPassword !== this.userData.confirmPassword) {
          new Noty({
            type: 'error',
            text: "Confirm Password should be the same as New Password!",
            timeout: 1000,
            layout: 'topCenter'
          }).show();
          this.$store.commit('hideLoader')
          return;
        }
        formData.append('userID', this.userData.id)
        formData.append('name', this.userData.name)
        formData.append('email', this.userData.email)
        formData.append('designation', this.userData.designation)
        formData.append('role', this.userData.role)
        formData.append('contact_no', this.userData.contact_no)
        formData.append('pincode', this.userData.pincode)
        formData.append('oldPassword', this.userData.oldPassword)
        formData.append('newPassword', this.userData.newPassword)
        formData.append('confirmPassword', this.userData.confirmPassword)
        if (this.selectedFiles.length) {
          for (let i = 0; i < this.selectedFiles.length; i++) {
            formData.append('profile_pic', this.selectedFiles[i])
          }
        }
        const response = await axios.put(`${BASE_URL}api/users/`, formData, {
          headers: {
            'Content-Type': "multipart/form-data",
            token: this.authToken,
          }
        });
        if (response.status == 200) {
          Swal.fire({
            title: response.data.message,
            icon: 'success',
          })
          this.userData.oldPassword = ''
          this.userData.newPassword = ''
          this.userData.confirmPassword = ''
          setTimeout(() => {
            // window.location.reload();

            new Noty({
              type: 'info',
              text: 'Please re-login to see profile changes',
              timeout: 1000,
            }).show()
          }, 100)
        }
        this.$store.commit('hideLoader');
      }
      catch (error) {
        new Noty({
          type: 'error',
          text: error.response.data.detail ? error.response.data.detail : error.response.data.message,
          timeout: 1000,
        }).show()
        this.$store.commit('hideLoader');
      }
    },
    onImageChange(e) {
      let fileInput = e.target;
      let file = fileInput.files[0];
      if (!file) {
        new Noty({
          type: 'error',
          text: 'No file selected.',
          timeout: 2000,
        }).show();
        fileInput.value = '';
        return;
      }

      if (!file.type.match('image.*')) {
        new Noty({
          type: 'error',
          text: 'Please select an image file.',
          timeout: 2000,
        }).show();
        fileInput.value = '';
        return;
      }

      if (file.size > 409600) {
        new Noty({
          type: 'error',
          text: 'Please select an image file less than 400KB.',
          timeout: 2000,
        }).show();
        fileInput.value = '';
      }
      this.selectedFiles = [file];
    },
    setUserDataFromLocalStorage() {
      this.userData.id = this.authUser.id
      this.userData.name = this.authUser.name
      this.userData.email = this.authUser.email
      this.userData.designation = this.authUser.designation
      this.userData.contact_no = this.authUser.contact_no
      this.userData.role = this.authUser.role
      this.userData.pincode = this.authUser.pincode
      this.userData.profile_pic = this.authUser.profile_pic
    }
  },
  mounted() {
    this.$store.state.isAbsolute = true;
    setNavPills();
    setTooltip();
    this.setUserDataFromLocalStorage();
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
<style></style>
