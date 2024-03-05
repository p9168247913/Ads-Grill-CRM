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
                <input type="text" v-model="searchTerm" class="form-control" placeholder="Search by Project Name..." />
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
          <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="createProjectLabel">Create Project</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body modalBody">
                <form @submit="createProjects($event)">
                  <div class="row">
                    <div style="color: black;" class="col-md-6 mb-3">
                      <label for="client_name" class="form-label">Client Name</label>
                      <v-select v-model="selectedClient" :options="allClients" label="name"
                        placeholder="Select Client Name" />
                    </div>
                    <div class="col-md-6 mb-3">
                      <label for="reporter_id" class="form-label">Manager</label>
                      <select class="form-control" v-model="projectData.reporter_id">
                        <option value="">Select Manager</option>
                        <!-- <option value="18">Abhishek</option> -->
                        <!-- <option value="Pawan">Pawan</option> -->
                        <option v-for="(manager, index) in projectManager" :key="index" :value="manager.id">{{
          manager.name }}</option>
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
                        <!-- <option value="7">Shyam</option> -->
                        <option v-for="(tag, index) in team_lead" :key="index" :value="tag.id">{{
          tag.name }}</option>
                      </select>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-6 mb-3">
                      <label for="tech_stacks" class="form-label">Tech. Stack</label>
                      <input type="text" class="form-control" v-model="projectData.tech_stacks" required>
                    </div>
                    <div class="col-md-6 mb-3">
                      <label for="host_address" class="form-label">Host Address</label>
                      <input type="text" class="form-control" v-model="projectData.host_address">
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-12 mb-3">
                      <label for="projectName" class="form-label">Files</label>
                      <input type="file" accept=".xlsx, .xlx, .pdf, .doc, .ppt" class="form-control" multiple
                        @change="handleFileChange">
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

        <!-- Modal for Edit Project -->
        <div class="modal fade" ref="createProjectModal" id="editProject" tabindex="-1"
          aria-labelledby="createProjectLabel" aria-hidden="true" @hidden="editProjects">
          <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="createProjectLabel">Edit Project</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body modalBody">
                <form @submit="editProjects($event, updateProjectData.id)">
                  <div class="row">
                    <div style="color: black;" class="col-md-6 mb-3">
                      <label for="client_name" class="form-label">Client Name</label>
                      <v-select v-model="selectedClient" :options="allClients" label="name"
                        placeholder="Select Client Name" disabled />
                    </div>
                    <div class="col-md-6 mb-3">
                      <label for="reporter_id" class="form-label">Manager</label>
                      <select class="form-control" v-model="updateProjectData.reporter_id">
                        <option value="">Select Manager</option>
                        <option v-for="(manager, index) in projectManager" :key="index" :value="manager.id">{{
          manager.name }}</option>
                      </select>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-6 mb-3">
                      <label for="name" class="form-label">Project Name</label>
                      <input style="cursor:not-allowed;" type="text" class="form-control"
                        v-model="updateProjectData.name" @input="generateKey" required disabled>
                    </div>
                    <div class="col-md-6 mb-3">
                      <label for="key" class="form-label">Key</label>
                      <input style="cursor:not-allowed;" type="text" class="form-control"
                        v-model="updateProjectData.key" disabled required>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-6 mb-3">
                      <label for="type" class="form-label">Type</label>
                      <select class="form-control" v-model="updateProjectData.type" required>
                        <option value="">Select Type</option>
                        <option value="ERP">ERP</option>
                        <option value="CRM">CRM</option>
                        <!-- <option v-for="(tag, index) in tags" :key="index" :value="tag.name">{{
                          tag.name }}</option> -->
                      </select>
                    </div>
                    <div class="col-md-6 mb-3">
                      <label for="team_lead_id" class="form-label">Team Lead</label>
                      <select class="form-control" v-model="updateProjectData.team_lead_id" required>
                        <option value="">Select Team Lead</option>
                        <!-- <option value="7">Shyam</option> -->
                        <option v-for="(lead, index) in team_lead" :key="index" :value="lead.id">{{
          lead.name }}</option>
                      </select>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-6 mb-3">
                      <label for="tech_stacks" class="form-label">Tech. Stack</label>
                      <input type="text" class="form-control" v-model="updateProjectData.tech_stacks" required>
                    </div>
                    <div class="col-md-6 mb-3">
                      <label for="host_address" class="form-label">Host Address</label>
                      <input type="text" class="form-control" v-model="updateProjectData.host_address">
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-12 mb-3">
                      <label for="projectName" class="form-label">Files</label>
                      <input type="file" accept=".xlsx, .xlx, .pdf, .doc, .ppt" class="form-control" multiple
                        @change="handleUpdateFileChange">
                    </div>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                      @click="resetValues">Close</button>
                    <button type="submit" data-bs-dismiss="modal" class="btn btn-primary">Save</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>

        <vue-progress-bar :progress="uploadProgress" />

        <!-- Modal for Create Client -->
        <div class="modal fade" ref="createProjectModal" id="createClient" tabindex="-1"
          aria-labelledby="createProjectLabel" aria-hidden="true" @hidden="createProjects">
          <div class="modal-dialog modal-dialog-centered modal-lg">
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
        <div class="card" style="margin-top: 2rem; padding: 5px;">
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
                    <th style="color: #344767 !important;"
                      class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold action-head">
                      Actions</th>
                  </tr>
                </thead>
                <tbody v-for="(project, index) in paginatedProjects" :key="index">
                  <tr>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-left">
                        <h6 class="mb-0 text-sm">{{ (currentPage - 1) * itemsPerPage + index + 1 }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-row justify-content-left project-name">
                        <h6 style="margin-top: 14px;" @click="openProject(project.id)" class="mb-0 text-sm">{{
          project.name ?
            limitedTeamMembers(project.name) : '' }}
                        </h6>
                        <p class="show-more" v-if="project.name && project.name.length > 15" data-bs-toggle="modal"
                          data-bs-target="#showTeam" @mouseover="openModal(project.name)">
                          ...more
                        </p>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-left">
                        <h6 class="mb-0 text-sm">{{ project.key }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-left">
                        <h6 class="mb-0 text-sm">{{ project.client.name }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-left">
                        <h6 class="mb-0 text-sm">{{ project.type }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-left">
                        <h6 class="mb-0 text-sm">{{ project.reporter.name }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-row justify-content-left">
                        <h6 style="margin-top: 14px;" class="mb-0 text-sm">{{ project.team_members ?
          limitedTeamMembers(project.team_members) : '' }}
                        </h6>
                        <p class="show-more" v-if="project.team_members && project.team_members.length > 15"
                          data-bs-toggle="modal" data-bs-target="#showTeam" @click="openModal(project.team_members)">
                          ...more
                        </p>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-row justify-content-left">
                        <h6 style="margin-top: 14px;" class="mb-0 text-sm">{{ limitedTeamMembers(project.tech_stacks) }}
                        </h6>
                        <p class="show-more" v-if="project.tech_stacks && project.tech_stacks.length > 15"
                          data-bs-toggle="modal" data-bs-target="#showTeam" @click="openModal(project.tech_stacks)">
                          ...more
                        </p>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-left">
                        <h6 class="mb-0 text-sm">{{ project.team_lead.name }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-left">
                        <h6 class="mb-0 text-sm">
                          <argon-progress :percentage="project.progress" color="success" />
                        </h6>
                      </div>
                    </td>
                    <td style="padding-left: 30px;">
                      <div class="d-flex flex-column justify-content-center">
                        <a v-if="project.attachments.length" @click="getAttachmentUrl($event, project.id)">
                          <i class="fas fa-download"></i>
                        </a>
                        <span v-else>No Files</span>
                      </div>
                    </td>
                    <td class="align-middle d-md-table-cell actions">
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
                      <i data-bs-toggle="modal" data-bs-target="#editProject" @click="editModal(project)"
                        class="fas fa-pencil-alt text-primary fa-xs pr-4 edit-icon"
                        style="margin-left: 20px; cursor: pointer;"></i>
                      <i @click="deleteProject(project.id)" class="fas fa-trash text-danger m-3 fa-xs delete-icon"
                        style="cursor: pointer;"></i>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <PaginationComponent v-if="allProjects.length > itemsPerPage" :currentPage="currentPage"
            :itemsPerPage="itemsPerPage" :filteredUsers="filteredProjects" :prevPage="prevPage" :nextPage="nextPage"
            :goToPage="goToPage" />
        </div>

        <!-- Modal for detailed view -->
        <div class="modal fade" ref="createProjectModal" id="showTeam" tabindex="-1"
          aria-labelledby="createProjectLabel" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <span class="close" data-bs-dismiss="modal"
                style="position: absolute; top: 0; right: 0; margin-right: 20px;">&times;</span>
              <p style="color: black; margin-top: 10px;">{{ detailedTeamMembers }}</p>
            </div>
          </div>
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
import VueProgressBar from 'vue-progressbar';
import PaginationComponent from './Paginator/PaginatorComponent.vue';
import router from "@/router";

export default {
  name: "projects",
  data() {
    return {
      currentPage: 1,
      itemsPerPage: 10,
      uploadProgress: 0,
      modalOpen: false,
      detailedTeamMembers: "",
      searchTerm: '',
      isLoading: false,
      allClients: [],
      tags: [],
      searchText: '',
      selectedClient: null,
      selectedFiles: [],
      selectedUpdateFiles: [],
      headers: ['S.No.', 'Project Name', 'Key', 'Client Name', 'Type', 'Manager', 'Team Members', 'Technology', 'Team Lead', 'Progress', 'Files'],
      allProjects: [],
      existingKeys: [],
      projectManager: [],
      team_lead: [],
      projectData: {
        client_id: '',
        name: '',
        reporter_id: '',
        key: '',
        type: '',
        team_lead_id: '',
        tech_stacks: '',
        host_address: '',
      },
      updateProjectData: {
        id: '',
        client_id: '',
        name: '',
        reporter_id: '',
        key: '',
        type: '',
        team_lead_id: '',
        tech_stacks: '',
        host_address: '',
        status: '',
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
    VueProgressBar,
    PaginationComponent,
  },
  computed: {
    ...mapState(['authUser', 'authToken']),
    filteredProjects() {
      return this.allProjects.filter(project => {
        const searchLowerCase = this.searchTerm.toLowerCase() || ''
        return (
          project.name.toLowerCase().includes(searchLowerCase) ||
          project.key.toLowerCase().includes(searchLowerCase) ||
          project.client.name.toLowerCase().includes(searchLowerCase) ||
          project.type.toLowerCase().includes(searchLowerCase) ||
          project.status.toLowerCase().includes(searchLowerCase)
        );
      });
    },
    paginatedProjects() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      return this.filteredProjects.slice(startIndex, startIndex + this.itemsPerPage);
    }
  },
  methods: {
    nextPage() {
      if (this.currentPage * this.itemsPerPage < this.filteredProjects.length) {
        this.currentPage++;
      }
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    goToPage(page) {
      this.currentPage = page;
      const startIndex = (page - 1) * this.itemsPerPage;
      const endIndex = startIndex + this.itemsPerPage;
      this.displayedUsers = this.filteredProjects.slice(startIndex, endIndex);
    },
    limitedTeamMembers(teamMembers) {
      const maxLength = 15;
      return teamMembers && typeof teamMembers === 'string' && teamMembers.length >= maxLength
        ? teamMembers.substring(0, maxLength) + " "
        : teamMembers;
    },
    openModal(teamMembers) {
      this.detailedTeamMembers = teamMembers;
      this.modalOpen = true;
    },
    closeModal() {
      this.modalOpen = false;
    },
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
        host_address: '',
        attachments: []
      }
      this.clientData = {
        client_name: '',
        email: '',
        password: '',
        pincode: '',
      }
    },
    async getProjectManagers() {
      try {
        this.$store.commit('showLoader');
        const response = await axios.get(`${BASE_URL}api/development/getProjectManagers`, {
          headers: {
            token: this.authToken,
          }
        })
        this.projectManager = response.data.project_managers;
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
    async getAttachmentUrl(e, id) {
      e.preventDefault();
      try {
        const response = await axios.get(`${BASE_URL}api/development/projects/download?id=${id}`, {
          headers: {
            token: this.authToken
          },
          responseType: 'arraybuffer',
        });
        this.resetValues();
        if (response && response.status === 200 && response.data) {
          const filename = this.extractFilename(response);
          const blob = new Blob([response.data], { type: 'application/zip' });

          const link = document.createElement('a');
          link.href = window.URL.createObjectURL(blob);
          link.download = filename;

          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);

          Swal.fire({
            title: `Downloaded successfully!`,
            icon: 'success',
          });
        }
      } catch (error) {
        new Noty({
          text: 'An error occurred',
          timeout: 500,
        }).show();
      }
    },
    extractFilename(response) {
      const contentDisposition = response.headers['content-disposition'];
      if (contentDisposition) {
        const filenameMatch = contentDisposition.match(/filename=([^;]+)/);
        return filenameMatch ? filenameMatch[1] : 'download.zip';
      } else {
        return 'download.zip';
      }
    },
    async getProjects() {
      try {
        this.$store.commit('showLoader');
        const response = await axios.get(`${BASE_URL}api/development/projects?key=development`, {
          headers: {
            'Content-Type': "multipart/form-data",
            token: this.authToken,
          }
        })
        this.allProjects = response.data.projects;
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
        new Noty({
          type: 'warning',
          text: "Please select client!",
          timeout: 1000,
        }).show();
        return;
      }
      this.projectData.client_id = this.selectedClient.id;
      try {
        this.$store.commit('showLoader');
        let formData = new FormData();
        formData.append('client_id', this.projectData.client_id);
        formData.append('name', this.projectData.name);
        formData.append('key', this.projectData.key);
        formData.append('type', this.projectData.type);
        formData.append('reporter_id', this.projectData.reporter_id);
        formData.append('host_address', this.projectData.host_address);
        formData.append('tech_stacks', this.projectData.tech_stacks);
        formData.append('team_lead_id', this.projectData.team_lead_id);

        for (let i = 0; i < this.selectedFiles.length; i++) {
          formData.append('attachments', this.selectedFiles[i]);
        }
        const response = await axios.post(`${BASE_URL}api/development/projects`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'token': this.authToken,
          },
          onUploadProgress: progressEvent => {
            const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
            this.uploadProgress = percentCompleted;
          },
        });
        if (response.status === 201) {
          Swal.fire({
            title: response.data.message,
            icon: 'success',
          });
        }
        this.getProjects();
        this.$store.commit('hideLoader');
        this.resetValues();
      } catch (error) {
        new Noty({
          type: 'error',
          text: error.message,
          timeout: 500,
        }).show();
        this.$store.commit('hideLoader');
      }
    },
    async editProjects(e) {
      e.preventDefault();

      if (!this.selectedClient) {
        new Noty({
          type: 'warning',
          text: "Please select client!",
          timeout: 500,
        }).show();
        return;
      }
      try {
        this.$store.commit('showLoader');
        let updateFormData = new FormData();
        updateFormData.append('id', this.updateProjectData.id);
        updateFormData.append('client_id', this.updateProjectData.client.id);
        updateFormData.append('name', this.updateProjectData.name);
        updateFormData.append('key', this.updateProjectData.key);
        updateFormData.append('type', this.updateProjectData.type);
        updateFormData.append('reporter_id', this.updateProjectData.reporter_id);
        updateFormData.append('host_address', this.updateProjectData.host_address);
        updateFormData.append('tech_stacks', this.updateProjectData.tech_stacks);
        updateFormData.append('team_lead_id', this.updateProjectData.team_lead_id);

        for (let i = 0; i < this.selectedUpdateFiles.length; i++) {
          updateFormData.append("attachments", this.selectedUpdateFiles[i]);
        }

        const response = await axios.put(`${BASE_URL}api/development/projects`, updateFormData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'token': this.authToken,
          },
          onUploadProgress: progressEvent => {
            const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
            this.uploadProgress = percentCompleted;
          },
        });

        if (response.status === 200) {
          Swal.fire({
            title: response.data.message,
            icon: 'success',
          });
        }
        this.getProjects();
        this.$store.commit('hideLoader');
        this.resetValues();
      } catch (error) {
        new Noty({
          type: 'error',
          text: error.response.data.message,
          timeout: 500,
        }).show();
        this.$store.commit('hideLoader');
      }
    },
    editModal(project) {
      this.updateProjectData = { ...project, client_id: project.client.id, reporter_id: project.reporter.id, team_lead_id: project.team_lead.id };
      this.selectedClient = project.client
      this.selectedUpdateFiles = []
      this.isEditModalOpen = true;
    },
    async deleteProject(id) {
      Swal.fire({
        title: 'Are you sure?',
        text: 'You won\'t be able to revert this!',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Yes, delete it!'
      }).then(async (result) => {
        if (result.isConfirmed) {
          try {
            const response = await axios.delete(`${BASE_URL}api/development/projects?id=${id}`, {
              headers: {
                token: this.authToken
              }
            })
            this.getProjects();
            Swal.fire('Deleted!', response.data.message, 'success');
          } catch (error) {
            this.getProjects();
            Swal.fire('Deleted!', error.response.data.message, 'success');

          }
        }
      });
    },
    handleFileChange(e) {
      this.selectedFiles = e.target.files
    },
    handleUpdateFileChange(e) {
      this.selectedUpdateFiles = e.target.files
    },
    async createClient(e) {
      e.preventDefault();
      try {
        const response = await axios.post(`${BASE_URL}api/client/`, this.clientData)
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

    async getTeamLead() {
      try {
        const response = await axios.get(`${BASE_URL}api/development/getTeamLeaders`, {
          headers: {
            token: this.authToken
          }
        })
        if (response.status === 200) {
          this.team_lead = response.data.team_leaders
        }
      } catch (error) {
        new Noty({
          type: 'error',
          text: error.message,
          timeout: 500,
        }).show()
      }
    },
    async getClients() {
      try {
        this.$store.commit('showLoader')
        const response = await axios.get(`${BASE_URL}api/client/`, {
          headers: {
            token: this.authToken,
          }
        })
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
      var projectName = this.projectData.name ? this.projectData.name.toUpperCase().split(' ') : [];
      let key = '';

      if (projectName.length === 1) {
        key = projectName[0];
      } else if (projectName.length === 2) {
        key = `${projectName[0].charAt(0)}${projectName[1].charAt(0)}`;
      } else if (projectName.length > 2) {
        key = projectName.reduce((acc, curr) => acc + curr.charAt(0), '');
      }
      const randomNumber = Math.floor(1000 + Math.random() * 9000);
      let uniqueKey = key ? `${key}_${randomNumber}` : '';
      this.projectData.key = uniqueKey;
    },
    async openProject(id) {
      localStorage.setItem('projectId', id)
      try {
        const response = await axios.get(`${BASE_URL}api/development/sprints?key=active_sprint&id=${id}`, {
          headers: {
            'Content-Type': "multipart/form-data",
            token: this.authToken,
          }
        })
        if (response.data.activeSprintAndIssues) {
          router.push(`/active-sprints/${response.data.activeSprintAndIssues.activeSprint.id}`)
        } else {
          new Noty({
            type: 'warning',
            text: "No active sprints found!!",
            timeout: 2000,
            position: "top-center"
          }).show();
          return;
        }
      } catch (error) {
        new Noty({
          type: 'error',
          text: error,
          timeout: 2000,
          position: "top-center"
        }).show();
      }
    }
  },
  mounted() {
    this.getClients();
    this.getProjectManagers();
    this.getProjects();
    this.getTeamLead();
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

.project-name :hover {
  /* border: 1px solid red; */
  cursor: pointer;
  color: blue
}

.modal {
  display: none;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
}

.modal-content {
  background-color: #fefefe;
  margin: 5% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: rgb(100, 100, 100);
  text-decoration: none;
  cursor: pointer;
}

.show-more {
  color: blue;
  font-size: 12px;
  padding-top: 16px;
}

.show-more:hover {
  cursor: pointer;
}

.actions {
  margin-left: 15px !important;
  position: sticky;
  right: 0;
  z-index: 1;
  background-color: white !important;
}

.action-head {
  position: sticky;
  right: 0;
  z-index: 1;
  background-color: white !important;
}

@media (max-width: 576px) {
  .actions {
    margin-left: 15px !important;
    z-index: 1;
    position: relative;
  }

  .action-head {
    position: relative;

    z-index: 1;
  }
}
</style>