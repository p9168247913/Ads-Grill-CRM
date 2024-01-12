<!-- Home.vue -->
<template>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Webkit | Responsive Bootstrap 4 Admin Dashboard Template</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
  </head>
  <div class="wrapper" style="margin-bottom: 80px; ">
    <div class="content-page">
      <div class="container-fluid">
        <div v-if="isLoading" class="loader"></div>
        <div style="margin-top: 20px;">
          <div class="row">
            <div class="col-md-6 col-lg-6 col-sm-12 mb-3">
              <div class="input-group">
                <span class="input-group-text text-body">
                  <i class="fas fa-search" aria-hidden="true"></i>
                </span>
                <input type="text" v-model="searchTerm" @change="filterUsers" class="form-control"
                  placeholder="Search by Project Name..." />
              </div>
            </div>
            <div class="col-md-6 col-lg-6 col-sm-12 d-flex justify-content-lg-end justify-content-md-end">
              <div class="d-grid gap-2" style="display: flex!important; flex-direction: row;">
                <button type="button" style="width: auto; height: 40px !important;"
                  class="btn btn-sm btn-dark mb-0 px-2 py-1 mb-0 nav-link active" data-bs-toggle="modal"
                  data-bs-target="#createProject">
                  <i class="fas fa-plus-circle text-success text-sm opacity-10"></i>&nbsp; &nbsp;Create Project
                </button>
                <button type="button" style="width: auto; height: 40px !important;"
                  class="btn btn-sm btn-dark mb-0 px-2 py-1 mb-0 nav-link active" data-bs-toggle="modal"
                  data-bs-target="#createClient">
                  <i class="fas fa-plus-circle text-success text-sm opacity-10"></i>&nbsp; &nbsp;Create Client
                </button>
              </div>
            </div>
          </div>
        </div>
        <!-- Modal for Create Project -->
        <div class="modal fade" ref="createProjectModal" id="createProject" tabindex="-1"
          aria-labelledby="createProjectLabel" aria-hidden="true" @hidden="createProjects">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="createProjectLabel">Create Project</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body modalBody">
                <form @submit="createProjects($event)">
                  <div class="row">
                    <div class="col-md-6 mb-3">
                      <label for="client_name" class="form-label">Client Name</label>
                      <v-select v-model="selectedClient" :options="allClients" label="name"
                        placeholder="Select Client Name" />
                    </div>
                    <div class="col-md-6 mb-3">
                      <label for="reporter_id" class="form-label">Manager</label>
                      <select class="form-control" v-model="projectData.reporter_id">
                        <option value="">Select Manager</option>
                        <option value="18">Abhishek</option>
                        <!-- <option value="Pawan">Pawan</option> -->
                        <!-- <option v-for="(tag, index) in tags" :key="index" :value="tag.name">{{
                          tag.name }}</option> -->
                      </select>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-6 mb-3">
                      <label for="name" class="form-label">Project Name</label>
                      <input type="text" class="form-control" v-model="projectData.name" @input="generateKey" required>
                    </div>
                    <div class="col-md-6 mb-3">
                      <label for="key" class="form-label">Key</label>
                      <input type="text" class="form-control" v-model="projectData.key" disabled required>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-6 mb-3">
                      <label for="type" class="form-label">Type</label>
                      <select class="form-control" v-model="projectData.type" required>
                        <option value="">Select Type</option>
                        <option value="ERP">ERP</option>
                        <option value="CRM">CRM</option>
                        <!-- <option v-for="(tag, index) in tags" :key="index" :value="tag.name">{{
                          tag.name }}</option> -->
                      </select>
                    </div>
                    <div class="col-md-6 mb-3">
                      <label for="team_lead_id" class="form-label">Team Lead</label>
                      <select class="form-control" v-model="projectData.team_lead_id" required>
                        <option value="">Select Team Lead</option>
                        <option value="7">Shyam</option>
                        <!-- <option v-for="(tag, index) in tags" :key="index" :value="tag.name">{{
                          tag.name }}</option> -->
                      </select>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-6 mb-3">
                      <label for="tech_stacks" class="form-label">Tech. Stack</label>
                      <input type="text" class="form-control" v-model="projectData.tech_stacks" required>
                    </div>
                    <div class="col-md-6 mb-3">
                      <label for="hostAddress" class="form-label">Host Address</label>
                      <input type="text" class="form-control" v-model="projectData.hostAddress">
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-12 mb-3">
                      <label for="projectName" class="form-label">Files</label>
                      <input type="file" accept=".xlsx, .xlx, .pdf, .doc, .ppt" class="form-control" multiple>
                    </div>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                      @click="resetValues">Close</button>
                    <button type="submit" class="btn btn-primary">Create</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>

        <!-- Modal for Create Client -->
        <div class="modal fade" ref="createProjectModal" id="createClient" tabindex="-1"
          aria-labelledby="createProjectLabel" aria-hidden="true" @hidden="createProjects">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="createProjectLabel">Create Client</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body modalBody">
                <form @submit="createClient($event), resetValues()">
                  <div class="row">
                    <div class="col-md-6 mb-3">
                      <label for="client_name" class="form-label">Client Name</label>
                      <input type="text" class="form-control" v-model="clientData.name" required>
                    </div>
                    <div class="col-md-6 mb-3">
                      <label for="email" class="form-label">Email</label>
                      <input type="email" class="form-control" v-model="clientData.email" required>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-6 mb-3">
                      <label for="password" class="form-label">Password</label>
                      <input type="password" class="form-control" v-model="clientData.password" required>
                    </div>
                    <div class="col-md-6 mb-3">
                      <label for="pincode" class="form-label">Pincode</label>
                      <input type="text" class="form-control" v-model="clientData.pincode" required>
                    </div>
                  </div>

                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                      @click="resetValues">Close</button>
                    <button type="submit" data-bs-dismiss="modal" class="btn btn-primary">Create</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>

        <!--Table-->
        <div class="card" style="margin-top: 2rem;">
          <div class="card-header pb-0">
            <h6>PROJECTS</h6>
          </div>
          <div class="card-body px-0 pt-0 pb-2">
            <div class="table-responsive p-0">
              <table class="table align-items-center mb-0">
                <thead>
                  <tr>
                    <th style="color: #344767 !important;"
                      class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold"
                      v-for="(head) in headers" :key="head">{{ head }}</th>
                  </tr>
                </thead>
                <tbody v-for="(project, index) in allProjects" :key="index">
                  <tr>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-center">
                        <h6 class="mb-0 text-sm">{{ index + 1 }}</h6>
                      </div>
                    </td>
                    
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-center">
                        <h6 class="mb-0 text-sm">{{ project.name }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-center">
                        <h6 class="mb-0 text-sm">{{ project.key }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-center">
                        <h6 class="mb-0 text-sm">{{ project.client_id }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-center">
                        <h6 class="mb-0 text-sm">{{ project.type }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-center">
                        <h6 class="mb-0 text-sm">{{ project.reporter_id }}</h6>
                      </div>
                    </td>
                    
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-center">
                        <h6 class="mb-0 text-sm"></h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-center">
                        <h6 class="mb-0 text-sm">{{ project.tech_stacks }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-center">
                        <h6 class="mb-0 text-sm">{{ project.team_lead_id }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-center">
                        <h6 class="mb-0 text-sm">
                          <argon-progress percentage="25" color="success"/>
                        </h6>
                      </div>
                    </td>
                    <td class="align-middle" style="margin-left: 15px !important;">
                      <!-- <i v-if="authUser.role == 'admin'"
                                            class="fas fa-pencil-alt text-primary fa-xs pr-4 edit-icon"
                                            data-bs-toggle="modal" data-bs-target="#edituser"
                                            style="margin-left: 20px; cursor: pointer;" @click="handleEditClick"></i>
                                        <i v-else class="fas fa-pencil-alt text-primary fa-xs pr-4"
                                            style="color: dodgerblue !important; margin-left: 20px; cursor: not-allowed;"></i> -->

                      <!-- <i v-if="authUser.role == 'admin'"
                                            class="fas fa-trash text-danger m-3 fa-xs delete-icon" style="cursor: pointer;"
                                            @click="deleteUser" data-toggle="tooltip" data-original-title="Delete user"></i>
                                        <i v-else class="fas fa-trash text-danger m-3 fa-xs"
                                            style="cursor: not-allowed;"></i> -->

                      <i class="fas fa-pencil-alt text-primary fa-xs pr-4"
                        style="color: dodgerblue !important; margin-left: 20px; cursor: not-allowed;"></i>
                      <i class="fas fa-trash text-danger m-3 fa-xs" style="cursor: not-allowed;"></i>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <!-- <PaginationComponent :currentPage="currentPage" :itemsPerPage="itemsPerPage" :filteredUsers="filteredUsers"
                    :prevPage="prevPage" :nextPage="nextPage" :goToPage="goToPage" /> -->
        </div>
      </div>
    </div>
  </div>
</template>
    
<script>
import { BASE_URL } from '../config/apiConfig';
import axios from 'axios';
import Noty from 'noty';
import Swal from 'sweetalert2';
import { mapState } from 'vuex'
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";
import ArgonProgress from './ArgonProgress.vue'

export default {
  name: "projects",
  data() {
    return {
      searchTerm: '',
      isLoading: false,
      allClients: [],
      tags: [],
      searchText: '',
      selectedClient: null,
      selectedFiles: [],
      headers: ['S.No.', 'Project Name', 'Key', 'Client Name', 'Type', 'Manager', 'Team Members', 'Technology', 'Team Lead', 'Progress', 'Actions'],
      allProjects: [],
      existingKeys: [],
      projectData: {
        client_id: '',
        name: '',
        reporter_id: '',
        key: '',
        type: '',
        team_lead_id: '',
        tech_stacks: '',
        hostAddress: '',
        attachments: []
      },
      clientData: {
        name: '',
        email: '',
        password: '',
        pincode: '',
      }
    };
  },
  components: {
    vSelect,
    ArgonProgress,
  },
  computed: {
    ...mapState(['authUser', 'authToken']),
  },
  methods: {

    resetValues() {
      this.selectedClient = ''
      this.projectData = {
        client_id: this.selectedClient,
        name: '',
        reporter_id: '',
        key: '',
        type: '',
        manager: '',
        team_lead_id: '',
        tech_stacks: this.tech_stacks,
        hostAddress: '',
        attachments: []
      }
      this.clientData = {
        client_name: '',
        email: '',
        password: '',
        pincode: '',
      }
    },
    async getProjects() {
      try {
        this.$store.commit('showLoader');
        const response = await axios.get(`${BASE_URL}api/development/projects`, {
          headers: {
            'Content-Type': "multipart/form-data",
            token: this.authToken,
          }
        })
        this.allProjects = response.data.projects;
        console.log("resp", this.allProjects);
        this.$store.commit('hideLoader');
      } catch (error) {
        new Noty({
          type: 'error',
          text: error.message,
          timeout: 500,
        }).show()
        this.$store.commit('hideLoader');
      }
    },
    async createProjects(e) {
      e.preventDefault();
      if (!this.selectedClient) {
        alert('Please select a Client');
        return;
      }
      this.projectData.client_id = this.selectedClient.id
      try {
        this.$store.commit('showLoader')
        const response = await axios.post(`${BASE_URL}api/development/projects`, this.projectData, {
          headers: {
            'Content-Type': "multipart/form-data",
            token: this.authToken,
          }
        })
        console.log("resp", response.data);
        if (response.status == 201) {
          Swal.fire({
            title: response.data.message,
            icon: 'success',
          })
        }
        this.$store.commit('hideLoader')
      } catch (error) {
        new Noty({
          type: 'error',
          text: error.message,
          timeout: 500,
        }).show()
        this.$store.commit('hideLoader')
      }

    },
    async createClient(e) {
      e.preventDefault();
      console.log(this.clientData);
      try {
        const response = await axios.post(`${BASE_URL}api/client/`, this.clientData)
        console.log(response.data);
        if (response.status == 201) {
          Swal.fire({
            title: "Client created successfully!",
            icon: 'success',
          })
        }
      } catch (error) {
        new Noty({
          type: 'error',
          text: error.message,
          timeout: 500,
        }).show()
      }
    },
    // async getLeadsInfo() {
    //   try {
    //     const response = await axios.get(`${BASE_URL}api/leadinfo/`)
    //     this.tags = response.data.leadInfoData['leadTag']

    //   } catch (error) {
    //     new Noty({
    //       type: 'error',
    //       text: error.message,
    //       timeout: 500,
    //     }).show()
    //   }
    // },
    async getClients() {
      try {
        this.$store.commit('showLoader')
        const response = await axios.get(`${BASE_URL}api/client/`)
        this.allClients = response.data.clients
        this.$store.commit('hideLoader')
      } catch (error) {
        new Noty({
          type: 'error',
          text: error.message,
          timeout: 500,
        }).show()
        this.$store.commit('hideLoader')

      }
    },
    generateKey() {
      const projectName = this.projectData.name.toLowerCase().split(' ');
      let key = '';

      if (projectName.length === 1) {
        key = projectName[0]
      } else if (projectName.length === 2) {
        key = `${projectName[0].charAt(0)}${projectName[1].charAt(0)}`;
      } else {
        key = projectName.reduce((acc, curr) => acc + curr.charAt(0), '');
      }

      let count = 1;
      let uniqueKey = key + 1;

      while (this.existingKeys.includes(uniqueKey)) {
        count++;
        uniqueKey = `${key}${count.toString().padStart(2, '0')}`;
      }
      this.projectData.key = uniqueKey;
    },
  },
  mounted() {
    this.getClients();
    this.getProjects();
  }
};
</script>

<style>
:root {
  --vs-line-height: 1.8;
}

.vs__selected {
  line-height: var(--vs-line-height);
}

.vs__dropdown-option {
  line-height: 2;
}

.vs__search,
.vs__search:focus {
  line-height: var(--vs-line-height);
}

/* Loader styles */
.loader {
  display: inline-block;
  width: 80px;
  height: 80px;
}

.loader::after {
  content: " ";
  display: block;
  width: 30px;
  height: 30px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: loader 1.2s linear infinite;
}

@keyframes loader {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}
</style>