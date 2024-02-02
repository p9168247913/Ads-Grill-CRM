<!-- Home.vue -->
<template>
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
    </head>
    <div class="wrapper" style="margin-bottom: 80px; ">
        <div class="content-page">
            <div class="container-fluid">
                <div style="margin-top: 20px;">
                    <div class="row">
                        <div class="col-md-6 col-lg-6 col-sm-12 mb-3">
                            <div class="input-group">
                                <span class="input-group-text text-body">
                                    <i class="fas fa-search" aria-hidden="true"></i>
                                </span>
                                <input type="text" v-model="searchTerm" class="form-control"
                                    placeholder="Search Issue..." />
                            </div>
                        </div>
                        <div class="col-md-6 col-lg-6 col-sm-12 d-flex justify-content-lg-end justify-content-md-end">
                            <div class="d-grid gap-2" style="display: flex!important; flex-direction: row;">
                                <button type="button" style="width: auto; height: 40px !important;"
                                    class="btn btn-sm btn-dark mb-0 px-2 py-1 mb-0 nav-link active" data-bs-toggle="modal"
                                    data-bs-target="#createIssue">
                                    <i class="fas fa-plus-circle text-success text-sm opacity-10"></i>&nbsp; &nbsp;Create
                                    Issue
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Modal for Create Issue -->
                <div class="modal fade" ref="createProjectModal" id="createIssue" tabindex="-1"
                    aria-labelledby="createProjectLabel" aria-hidden="true" @hidden="createSprints">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createProjectLabel">Create Issue</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body modalBody">
                                <form @submit="createIssues($event), resetValues()">
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="title" class="form-label">Title</label>
                                            <input type="text" class="form-control" v-model="issueData.title" required>
                                        </div>


                                        <div class="col-md-6 mb-3">
                                            <label for="sprint" class="form-label">Sprint</label>
                                            <!-- <input type="text" class="form-control" v-model="issueData.issue_name"
                                                required> -->
                                            <select class="form-select" v-model="issueData.sprint_id" required>
                                                <option value="">Select sprint</option>

                                                <option v-for="(sprint, index) in allSprints" :key="index"
                                                    :value="sprint.id">{{
                                                        sprint.name }}</option>
                                            </select>
                                        </div>

                                        <div class="col-md-6 mb-3">
                                            <label for="key" class="form-label">Key</label>
                                            <input type="text" class="form-control" v-model="issueData.key" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="reporter" class="form-label">Reporter</label>
                                            <!-- <input type="text" class="form-control" v-model="issueData.issue_name"
                                                required> -->
                                            <select class="form-select" v-model="issueData.reporter_id" required>
                                                <option value="">Select Reporter</option>
                                                <option v-for="(manager, index) in projectManagers" :key="index"
                                                    :value="manager.id">{{
                                                        manager.name }}</option>
                                            </select>
                                        </div>

                                        <!--<div class="col-md-6 mb-3">
                                            <label for="team lead" class="form-label">Team Lead</label>
                                           <input type="text" class="form-control" v-model="issueData.team_lead"
                                                required> 
                                            <select class="form-select" v-model="issueData.team_lead_id" !required>
                                                <option value="">Select Team Lead</option>
                                                <option value=18>Team lead 1</option>
                                                <option value=20>Team Lead 2</option>
                                                 <option v-for="(user, index) in teamLead" :key="index" :value="user.id">{{
                                                    user.name }}</option> -->
                                        <!-- </select> -->
                                        <!-- </div> -->

                                        <div class="col-md-6 mb-3">
                                            <label for="description" class="form-label">Description</label>
                                            <input type="text" class="form-control" v-model="issueData.description"
                                                required>
                                        </div>

                                        <div class="col-md-6 mb-3">
                                            <label for="expected time" class="form-label">Expected Time</label>
                                            <input type="duration" class="form-control" v-model="issueData.exp_duration"
                                                required>
                                        </div>

                                        <div class="col-md-6 mb-3">
                                            <label for="Assignee" class="form-label">Assignee</label>
                                            <!-- <input type="text" class="form-control" v-model="issueData.issue_name"
                                                required> -->
                                            <select class="form-select" v-model="issueData.assignee_id" required>
                                                <option value="">Select Assignee</option>
                                                <!-- <option value="18">Assignee 1</option>
                                                <option value="20">assignee 2</option> -->
                                                <option v-for="(assignee, index) in assignees" :key="index"
                                                    :value="assignee.id">{{
                                                        assignee.name }}</option>
                                            </select>
                                        </div>

                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">Type</label>
                                            <!-- <input type="text" class="form-control" v-model="issueData.issue_name"
                                                required> -->
                                            <select class="form-select" v-model="issueData.type" required>
                                                <option value="">Select Type</option>
                                                <option value="epic">Epic</option>
                                                <option value="story">Story</option>
                                                <option value="task">Task</option>
                                                <option value="subtask">Subtask</option>
                                                <option value="bug">Bug</option>

                                                <!-- <option v-for="(tag, index) in tags" :key="index" :value="tag.name">{{
                                                    tag.name }}</option> -->
                                            </select>
                                        </div>

                                        <div class="col-md-6 mb-3">
                                            <label for="priority" class="form-label">Priority</label>
                                            <!-- <input type="text" class="form-control" v-model="issueData.issue_name"
                                                required> -->
                                            <select class="form-select" v-model="issueData.priority" required>
                                                <option value="">Select Priority</option>
                                                <option value="lowest">Lowest</option>
                                                <option value="low">Low</option>
                                                <option value="medium">Medium</option>
                                                <option value="high">High</option>
                                                <option value="highest">Highest</option>
                                                <!-- <option v-for="(tag, index) in tags" :key="index" :value="tag.name">{{
                                                    tag.name }}</option> -->
                                            </select>
                                        </div>




                                        <div class="col-md-12 mb-3">
                                            <label for="issueName" class="form-label">Files</label>
                                            <input type="file" accept=".xlsx, .xlx, .pdf, .doc, .ppt" class="form-control" multiple
                                              @change="handleFileChange">
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

                <!--Table-->
                <div class="card" style="margin-top: 2rem;">
                    <div class="card-header pb-0">
                        <h6>ISSUES</h6>
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
                                <!-- <tbody v-for="(user, index) in paginatedUsers" :key="index">
                                  <tr>
                                      <td>
                                          <div class="d-flex px-2 py-1">
                                              <div>
                                                  <img src="" class="avatar avatar-sm me-3" alt="user1" />
                                              </div>
                                          </div>
                                      </td>
                                      <td>
                                          <div class="d-flex flex-column justify-content-center">
                                              <h6 class="mb-0 text-sm">{{ user.name }}</h6>
                                          </div>
                                      </td>
                                      <td>
                                          <div class="d-flex flex-column justify-content-center">
                                              <h6 class="mb-0 text-sm">{{ user.designation }}</h6>
                                          </div>
                                      </td>
                                      <td>
                                          <div class="d-flex flex-column justify-content-center">
                                              <h6 class="mb-0 text-sm">{{ user.role }}</h6>
                                          </div>
                                      </td>
                                      <td>
                                          <div class="d-flex flex-column justify-content-center">
                                              <h6 class="mb-0 text-sm">{{ user.contact_no }}</h6>
                                          </div>
                                      </td>
                                      <td>
                                          <div class="d-flex flex-column justify-content-center">
                                              <h6 class="mb-0 text-sm">{{ user.pincode }}</h6>
                                          </div>
                                      </td>
                                      <td class="align-middle" style="margin-left: 15px !important;">
                                          <i v-if="authUser.role == 'admin'"
                                              class="fas fa-pencil-alt text-primary fa-xs pr-4 edit-icon"
                                              data-bs-toggle="modal" data-bs-target="#edituser"
                                              style="margin-left: 20px; cursor: pointer;" @click="handleEditClick"></i>
                                          <i v-else class="fas fa-pencil-alt text-primary fa-xs pr-4"
                                              style="color: dodgerblue !important; margin-left: 20px; cursor: not-allowed;"></i>
  
                                          <i v-if="authUser.role == 'admin'"
                                              class="fas fa-trash text-danger m-3 fa-xs delete-icon" style="cursor: pointer;"
                                              @click="deleteUser" data-toggle="tooltip" data-original-title="Delete user"></i>
                                          <i v-else class="fas fa-trash text-danger m-3 fa-xs"
                                              style="cursor: not-allowed;"></i>
                                      </td>
                                  </tr>
                              </tbody> -->
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
import { BASE_URL } from '../../config/apiConfig';
import axios from 'axios';
import Noty from 'noty';
import Swal from 'sweetalert2';
import { mapState } from 'vuex'
// import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";
// import ArgonProgress from './ArgonProgress.vue'
// import VueProgressBar from 'vue-progressbar';
// import PaginationComponent from './Paginator/PaginatorComponent.vue';
// import router from "@/router";
export default {
    name: "backlogs",
    data() {
        return {
            headers: ['S.No.', 'Task Name', 'issue', 'Status', 'Task duration', 'Actual duration', 'Reporting Manager', 'Assignee', 'Actions'],
            allissues: [],
            searchTerm: '',
            allSprints: [],
            teamLead: [],
            assignees: [],
            projectManagers: [],
            selectedFiles:[],
            issueData: {
                project_id: '',
                sprint_id: '',
                reporter_id: '',
                team_lead_id: 17,
                attachments:[],
                title: '',
                key: '',
                description: '',
                type: '',
                priority: '',
                exp_duration: '',
                assignee_id: '',
            },

        };

    },

    components: {
    },
    computed: {
        ...mapState(['authUser', 'authToken']),
    },



    methods: {
        resetValues() {
            this.issueData = {
                sprint: '',
                reporter: '',
                team_lead: '',
                title: '',
                key: '',
                description: '',
                type: '',
                priority: '',
                exp_duration: '',
                assignee: '',
            }
        },

        async createIssues(e) {
            e.preventDefault()
           
            try {
            let project_id = localStorage.getItem('projectId')
            this.issueData.project_id = project_id

            let formData = new FormData();
            formData.append('project_id', this.issueData.project_id);
            formData.append('sprint_id', this.issueData.sprint_id);
            formData.append('reporter_id', this.issueData.reporter_id);
            formData.append('team_lead_id', this.issueData.team_lead_id);
            formData.append('title', this.issueData.title);
            formData.append('key', this.issueData.key);
            formData.append('description', this.issueData.description);
            formData.append('type', this.issueData.type);
            formData.append('priority', this.issueData.priority);
            formData.append('exp_duration', this.issueData.exp_duration);
            formData.append('assignee_id', this.issueData.assignee_id);
          

        for (let i = 0; i < this.selectedFiles.length; i++) {
          formData.append('attachments', this.selectedFiles[i]);
        }
                console.log(this.selectedFiles)

                this.$store.commit('showLoader');

                const response = await axios.post(`${BASE_URL}api/development/issues`, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                        token: this.authToken,
                    },
                    onUploadProgress: progressEvent => {
                        const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
                        this.uploadProgress = percentCompleted;
                    },
                });
                console.log(response)
                if (response.status === 201) {
                    Swal.fire({
                        title: response.data.message,
                        icon: 'success',
                    });
                }
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

        async getProjectManagers() {
            try {
                this.$store.commit('showLoader');
                const response = await axios.get(`${BASE_URL}api/development/getProjectManagers`, {
                    headers: {
                        token: this.authToken,
                    }
                })
                this.projectManagers = response.data.project_managers;
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

        async getTeamLead() {
            try {
                this.$store.commit('showLoader');
                const response = await axios.get(`${BASE_URL}api/development/getTeamLeaders`, {
                    headers: {
                        token: this.authToken,
                    }
                })
                this.projectManagers = response.data.project_managers;
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


        async getSprint() {
            let id = localStorage.getItem('projectId')
            try {
                this.$store.commit('showLoader');
                const response = await axios.get(`${BASE_URL}api/development/sprints?key=backlog&id=${id}`, {
                    headers: {
                        token: this.authToken,
                    }
                })
                if (response.status === 200) {
                    this.allSprints = response.data.sprintAndIssues
                }
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

        async getAssignees() {
            try {
                this.$store.commit('showLoader');
                const response = await axios.get(`${BASE_URL}api/development/getAssignees`, {
                    headers: {
                        token: this.authToken,
                    }
                })
                if (response.status === 200) {
                    // console.log(response)
                    this.assignees = response.data.Assignees
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.message,
                    timeout: 500,
                }).show()
                this.$store.commit('hideLoader');
            }
        },

        handleFileChange(e) {
      this.selectedFiles = e.target.files
    },

    },
    mounted() {
        this.getSprint();
        this.getAssignees();
        this.getProjectManagers();
    },
};

</script>

<style>
.issue-head {
    color: white;
}
</style>
      