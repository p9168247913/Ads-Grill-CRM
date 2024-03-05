<template>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Webkit | Responsive Bootstrap 4 Admin Dashboard Template</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
    </head>
    <div class="wrapper" style="margin-bottom: 80px; ">
        <div v-if="projectKey" class="content-page">
            <div class="container-fluid">
                <!-- <h6 class="sprint-head">Backlogs</h6> -->
                <div style="margin-top: 20px;">
                    <div class="row">
                        <div class="col-md-6 col-lg-6 col-sm-12 mb-3">
                            <div class="input-group">
                                <span class="input-group-text text-body">
                                    <i class="fas fa-search" aria-hidden="true"></i>
                                </span>
                                <input type="text" v-model="searchTerm" class="form-control"
                                    placeholder="Search Sprint..." />
                            </div>
                        </div>
                        <div class="col-md-6 col-lg-6 col-sm-12 d-flex justify-content-lg-end justify-content-md-end">
                            <div class="d-grid gap-2" style="display: flex!important; flex-direction: row;">
                                <button type="button" style="width: auto; height: 40px !important;"
                                    class="btn btn-sm btn-dark mb-0 px-2 py-1 mb-0 nav-link active" data-bs-toggle="modal"
                                    data-bs-target="#createSprint">
                                    <i class="fas fa-plus-circle text-success text-sm opacity-10"></i>&nbsp; &nbsp;Create
                                    Sprint
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Modal for Create Sprint -->
                <div class="modal fade" ref="createSprintModal" id="createSprint" tabindex="-1"
                    aria-labelledby="createProjectLabel" aria-hidden="true" @hidden="createSprints">
                    <div class="modal-dialog modal-dialog-centered">
                        <div style="padding-bottom: 5px;" class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createProjectLabel">Create Sprint</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body modalBody" style="padding-top: 20px;">
                                <form @submit="createSprints($event)">
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">Sprint Name</label>
                                            <input type="text" class="form-control" v-model="sprintData.name"
                                                @input="generateKey()">
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">Key</label>
                                            <input type="text" class="form-control" v-model="sprintData.key" disabled>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="key" class="form-label">Start Date</label>
                                            <input type="datetime-local" class="form-control"
                                                v-model="sprintData.start_date" :min="currentDateTime()">
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">End Date</label>
                                            <input type="datetime-local" class="form-control" v-model="sprintData.end_date"
                                                :min="sprintData.start_date" :disabled="sprintData.start_date === ''">
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="projectName" class="form-label">Duration</label>
                                            <input type="text" class="form-control" :disabled="true"
                                                :value="calculateDuration()">
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">Goal</label>
                                            <input type="text" class="form-control" v-model="sprintData.goal">
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="projectName" class="form-label">Reporter</label>
                                            <select class="form-control" v-model="sprintData.reporter_id">
                                                <option value="">Select Type</option>
                                                <option value="18">Abhishek</option>
                                                <!-- <option v-for="(tag, index) in tags" :key="index" :value="tag.name">{{
                                                    tag.name }}</option> -->
                                            </select>
                                        </div>
                                    </div>
                                    <div class="row" style="height: 300px; overflow: auto;">
                                        <div class="col-md-12 mb-3">
                                            <label for="projectName" class="form-label">Description</label>
                                            <QuillEditor required ref="editor" :modules="modules" theme="snow"
                                                toolbar="full" />
                                        </div>
                                    </div>
                                    <div class="modal-footer" style="z-index: 99999999;">
                                        <button type="button" class="btn btn-secondary close" data-bs-dismiss="modal"
                                            @click="resetValues">Close</button>
                                        <button type="submit" data-bs-dismiss="modal"
                                            class="btn btn-primary">Create</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Modal for Edit Sprint -->
                <div class="modal fade" ref="createProjectModal" id="editSprint" tabindex="-1"
                    aria-labelledby="createProjectLabel" aria-hidden="true" @hidden="createProjects">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createProjectLabel">Edit Sprint</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body modalBody" style="padding-top: 20px; ">
                                <form @submit="editSprint($event)">
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">Sprint Name</label>
                                            <input type="text" class="form-control" v-model="updatedSprintData.name"
                                                @input="generateKey()" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">Key</label>
                                            <input type="text" class="form-control" v-model="updatedSprintData.key" disabled
                                                required>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="key" class="form-label">Start Date</label>
                                            <input type="datetime-local" class="form-control"
                                                v-model="updatedSprintData.start_date" :min="updatedSprintData.start_date"
                                                required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">End Date</label>
                                            <input type="datetime-local" class="form-control"
                                                v-model="updatedSprintData.end_date" :min="updatedSprintData.start_date"
                                                :disabled="updatedSprintData.start_date === ''" required>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="projectName" class="form-label">Duration</label>
                                            <input type="text" class="form-control" :disabled="true"
                                                :value="calculateUpdateDuration()" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">Goal</label>
                                            <input type="text" class="form-control" v-model="updatedSprintData.goal"
                                                required>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="projectName" class="form-label">Reporter</label>
                                            <select class="form-control" v-model="updatedSprintData.reporter_id" required>
                                                <option value="">Select Type</option>
                                                <option value="18">Abhishek</option>
                                                <!-- <option v-for="(tag, index) in tags" :key="index" :value="tag.name">{{
                                                    tag.name }}</option> -->
                                            </select>
                                        </div>
                                    </div>
                                    <div class="row" style="height: 300px; overflow: auto;">
                                        <div class="col-md-12 mb-3">
                                            <label for="projectName" class="form-label">Description</label>
                                            <QuillEditor required ref="editEditor" :modules="modules" theme="snow"
                                                toolbar="full" />
                                        </div>
                                    </div>
                                    <div class="modal-footer" style="z-index:99999999;">
                                        <button type="button" class="btn btn-secondary close" data-bs-dismiss="modal"
                                            @click="resetValues">Close</button>
                                        <button type="submit" data-bs-dismiss="modal" class="btn btn-primary">Save</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>

                <!--Table-->
                <div v-if="filteredSprints.length" class="card" style="margin-top: 2rem;">
                    <div class="card-header pb-0">
                        <h6>SPRINTS</h6>
                    </div>
                    <div class="card-body px-0 pt-0 pb-1">
                        <div class="table-responsive p-1">
                            <div class="align-items-center mb-0 sprint-card" v-for="(sprint, index) in filteredSprints"
                                :key="index">
                                <div class="align-items-center mb-0" style="display:flex; justify-content: space-between;">
                                    <div style="display: flex; gap: 20px; align-items: center;">
                                        <div class="d-flex flex-row justify-content-center">
                                            <span class="mb-0 text-sm"><i @click="toggleDropdown(index)"
                                                    class="fa fa-chevron-down drop-icon"></i></span>
                                        </div>
                                        <div class="d-flex flex-row justify-content-center">
                                            <h6 class="mb-0 text-sm">{{ sprint.project.key }}</h6>
                                        </div>
                                        <div class="d-flex flex-row justify-content-center">
                                            <h6 class="mb-0 text-sm" style="white-space: nowrap;">{{ sprint.name }}</h6>
                                        </div>
                                        <div class="d-flex flex-row justify-content-center ">
                                            <p class="mb-0 text-sm" style="font-size: smaller; white-space: nowrap;">{{
                                                formatDate(sprint.start_date)
                                            }} - {{ formatDate(sprint.end_date) }}</p>
                                        </div>
                                        <div class="d-flex flex-row justify-content-center">
                                            <p class="mb-0 text-sm" style="font-size: smaller;white-space: nowrap;">({{
                                                sprint.issues.length }}
                                                issues)</p>
                                        </div>
                                    </div>
                                    <div class="col text-end ">
                                        <div class="col text-end" style="white-space: nowrap;">
                                            <span v-if="sprint.is_started"
                                                style="height: 30px; padding: 2px 5px;border-radius: 4px;font-weight: bold; font-size: small; background-color: rgb(215, 215, 215);">
                                                Started
                                            </span>
                                            <button class="btn btn-link dropdown-open" type="button"
                                                id="dropdownMenuButton2" data-bs-toggle="dropdown" aria-expanded="false">
                                                <i class="fas fa-ellipsis-h"></i>
                                            </button>
                                            <ul class="dropdown-menu dropdown-menu-end"
                                                aria-labelledby="dropdownMenuButton2">
                                                <li @click="setSprint(sprint)" data-bs-toggle="modal"
                                                    data-bs-target="#editSprint"><a class="dropdown-item" href="#"><i
                                                            class="fas fa-edit text-success"></i>&nbsp;&nbsp;Edit</a>
                                                </li>
                                                <li @click="deleteSprint(sprint.id)"><a class="dropdown-item" href="#"><i
                                                            class="fas fa-trash-alt text-danger"></i>&nbsp;&nbsp;Delete</a>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                                <div class="issue-card">
                                    <div v-show="sprint.showDropdown">
                                        <table v-if="sprint.issues.length" class="table align-items-center mb-0">
                                            <thead>
                                                <tr>
                                                    <th style="color: #344767 !important;"
                                                        class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold">
                                                        Sr No.</th>
                                                    <th style="color: #344767!important;"
                                                        class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold">
                                                        Issue Name</th>
                                                    <th style="color: #344767!important;"
                                                        class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold">
                                                        Status</th>
                                                    <th style="color: #344767!important;"
                                                        class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold">
                                                        Priority</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr v-for="(issue, issueIndex) in sprint.issues" :key="issueIndex">
                                                    <td style="padding-left: 25px;">
                                                        <div class="d-flex flex-column justify-content-center">
                                                            <h6 class="mb-0 text-sm">{{ issueIndex + 1 }}</h6>
                                                        </div>
                                                    </td>

                                                    <td style="padding-left: 25px;">
                                                        <div class="d-flex flex-column justify-content-center">
                                                            <h6 class="mb-0 text-sm">{{
                                                                issue.title }}</h6>
                                                        </div>
                                                    </td>
                                                    <td style="padding-left: 25px;">
                                                        <div class="d-flex flex-column justify-content-center">
                                                            <h6 class="mb-0 text-sm">{{
                                                                issue.status }}</h6>
                                                        </div>
                                                    </td>
                                                    <td style="padding-left: 25px;">
                                                        <div class="d-flex flex-column justify-content-center">
                                                            <h6 class="mb-0 text-sm">{{
                                                                issue.priority }}</h6>
                                                        </div>
                                                    </td>
                                                </tr>
                                            </tbody>

                                        </table>
                                        <table v-else>
                                            <tr style="margin: auto;">
                                                <span style="color: rgb(253, 97, 97);">No issues found!</span>
                                            </tr>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div v-else>
                    <p>No sprints found</p>
                </div>
            </div>
        </div>
        <div v-else>
        </div>
    </div>
</template>
      
<script>
import { BASE_URL } from '../../config/apiConfig';
import axios from 'axios';
import Noty from 'noty';
import { mapState } from 'vuex'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import '@popperjs/core/dist/umd/popper.min.js';
import Popper from 'popper.js';
window.Popper = Popper;
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import Swal from 'sweetalert2';
export default {
    name: "backlogs",
    data() {
        return {
            searchTerm: '',
            allSprints: [],
            editorInstance: null,
            sprintData: {
                name: '',
                key: '',
                start_date: '',
                end_date: '',
                goal: '',
                project_id: '',
                reporter_id: '',
                description: '',
                exp_duration: '',
            },
            updatedSprintData: {
                id: '',
                reporter_id: '',
                name: '',
                key: '',
                description: '',
                exp_duration: '',
                start_date: '',
                end_date: '',
                goal: '',
                status: '',
            },
            projectKey: localStorage.getItem("projectId"),
        };
    },
    components: {
        QuillEditor,
    },
    computed: {
        ...mapState(['authUser', 'authToken']),
        filteredSprints() {
            return this.allSprints.filter(sprint => {
                const searchLowerCase = this.searchTerm.toLowerCase() || ''
                return (
                    sprint.name.toLowerCase().includes(searchLowerCase) ||
                    sprint.start_date.toLowerCase().includes(searchLowerCase)
                );
            });

        },
    },
    created() {
        this.projectKey = localStorage.getItem("projectId");

        if (!this.projectKey) {
            this.showSweetAlert();
        } else {
            // this.loadActiveSprints();
        }
    },
    methods: {
        saveContent(e) {
            e.preventDefault()
            if (this.$refs.editor) {
                const quillEditor = this.$refs.editor;
                if (quillEditor) {
                    const htmlContent = quillEditor.getHTML();
                    return htmlContent
                } else {
                    console.error('rootHTML method is not available');
                }
            } else {
                console.error('Quill editor reference not found');
            }
        },
        formatDate(dateString) {
            const options = { day: 'numeric', month: 'short' };
            const date = new Date(dateString);
            return date.toLocaleDateString('en-US', options);
        },
        resetValues() {
            this.sprintData = {
                name: '',
                key: '',
                start_date: '',
                end_date: '',
                goal: '',
                reporter_id: '',
                description: '',
                exp_duration: '',
            }
            const quillEditor = this.$refs.editor;
            if (quillEditor) {
                const htmlContent = quillEditor.setHTML("");
                htmlContent
            } else {
                console.error('rootHTML method is not available');
            }
        },
        generateKey() {
            var sprintData = this.sprintData.name ? this.sprintData.name.toUpperCase().split(' ') : [];
            var updatedSprintData = this.updatedSprintData.name ? this.updatedSprintData.name.toUpperCase().split(' ') : [];
            let key = '';
            let key2 = '';

            if (sprintData.length === 1 || updatedSprintData.length === 1) {
                key = sprintData[0];
                key2 = updatedSprintData[0];
            } else if (sprintData.length === 2 || updatedSprintData.length === 2) {
                key = `${sprintData[0].charAt(0)}${sprintData[1].charAt(0)}`;
                key2 = `${updatedSprintData[0].charAt(0)}${updatedSprintData[1].charAt(0)}`;
            } else if (sprintData.length > 2 || updatedSprintData.length > 2) {
                key = sprintData.reduce((acc, curr) => acc + curr.charAt(0), '');
                key2 = updatedSprintData.reduce((acc, curr) => acc + curr.charAt(0), '');
            }
            const randomNumber = Math.floor(1000 + Math.random() * 9000);
            let uniqueKey = key ? `${key}_${randomNumber}` : '';
            let uniqueKey2 = key2 ? `${key2}_${randomNumber}` : '';
            this.sprintData.key = uniqueKey;
            this.updatedSprintData.key = uniqueKey2;
        },
        currentDateTime() {
            const now = new Date();
            const formattedDateTime = now.toISOString().slice(0, 16);
            return formattedDateTime;
        },
        calculateDuration() {
            const startDate = new Date(this.sprintData.start_date);
            const endDate = new Date(this.sprintData.end_date);

            if (isNaN(startDate) || isNaN(endDate)) {
                // If either date is missing, return an empty string
                return '';
            }

            const diffInMilliseconds = endDate - startDate;

            const minutes = Math.floor(diffInMilliseconds / (1000 * 60) % 60);
            const hours = Math.floor(diffInMilliseconds / (1000 * 60 * 60) % 24);
            const days = Math.floor(diffInMilliseconds / (1000 * 60 * 60 * 24) % 7);
            const weeks = Math.floor(diffInMilliseconds / (1000 * 60 * 60 * 24 * 7) % 4);
            const months = Math.floor(diffInMilliseconds / (1000 * 60 * 60 * 24 * 30));

            let formattedDuration = '';

            if (months > 0) {
                formattedDuration += `${months}m `;
            }
            if (weeks > 0) {
                formattedDuration += `${weeks}w `;
            }
            if (days > 0) {
                formattedDuration += `${days}d `;
            }
            if (hours > 0) {
                formattedDuration += `${hours}h `;
            }
            if (minutes > 0) {
                formattedDuration += `${minutes}m`;
            }

            this.sprintData.exp_duration = formattedDuration.trim();

            return formattedDuration.trim();
        },
        calculateUpdateDuration() {
            const startDate = new Date(this.updatedSprintData.start_date);
            const endDate = new Date(this.updatedSprintData.end_date);

            if (isNaN(startDate) || isNaN(endDate)) {
                // If either date is missing, return an empty string
                return '';
            }

            const diffInMilliseconds = endDate - startDate;

            const minutes = Math.floor(diffInMilliseconds / (1000 * 60) % 60);
            const hours = Math.floor(diffInMilliseconds / (1000 * 60 * 60) % 24);
            const days = Math.floor(diffInMilliseconds / (1000 * 60 * 60 * 24) % 7);
            const weeks = Math.floor(diffInMilliseconds / (1000 * 60 * 60 * 24 * 7) % 4);
            const months = Math.floor(diffInMilliseconds / (1000 * 60 * 60 * 24 * 30));

            let formattedDuration = '';

            if (months > 0) {
                formattedDuration += `${months}m `;
            }
            if (weeks > 0) {
                formattedDuration += `${weeks}w `;
            }
            if (days > 0) {
                formattedDuration += `${days}d `;
            }
            if (hours > 0) {
                formattedDuration += `${hours}h `;
            }
            if (minutes > 0) {
                formattedDuration += `${minutes}m`;
            }

            this.updatedSprintData.exp_duration = formattedDuration.trim();

            return formattedDuration.trim();
        },
        async createSprints(e) {
            e.preventDefault();
            const description = this.saveContent(e);
            const project_id = localStorage.getItem("projectId");
            this.sprintData.description = description;
            this.sprintData.project_id = project_id;
            try {
                this.$store.commit('showLoader');
                const response = await axios.post(`${BASE_URL}api/development/sprints`, this.sprintData, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                        token: this.authToken,
                    }
                })
                console.log(response);
                if (response.status === 201) {
                    this.getAllSprints();
                    this.resetValues()
                    Swal.fire({
                        title: response.data.message,
                        icon: 'success',
                    });
                    this.$refs.createSprintModal.classList.remove('show');
                    this.$refs.createSprintModal.setAttribute('aria-hidden', 'true');
                    this.$refs.createSprintModal.style.display = 'none';
                    this.removeModalBackdrop();
                } else {
                    new Noty({
                        type: 'error',
                        text: response.data.message,
                        timeout: 500,
                    }).show()
                }
                this.$store.commit('hideLoader');
            } catch (error) {
                this.$store.commit('hideLoader');
                new Noty({
                    type: 'error',
                    text: error.response.data.message,
                    timeout: 500,
                }).show()
            }
        },
        setSprint(sprint) {
            this.updatedSprintData = {
                id: sprint.id,
                name: sprint.name,
                reporter_id: sprint.reporter.id,
                key: sprint.key,
                goal: sprint.goal,
                status: sprint.status,
            }
            this.updatedSprintData.start_date = new Date(sprint.start_date).toISOString().slice(0, 16);
            this.updatedSprintData.end_date = new Date(sprint.end_date).toISOString().slice(0, 16);
            this.updatedSprintData.exp_duration = sprint.exp_duration;
            const quillEditor = this.$refs.editEditor;
            if (quillEditor) {
                quillEditor.setHTML(sprint.description);

            }
        },
        async editSprint(e) {
            e.preventDefault();
            const quillEditor = this.$refs.editEditor;
            this.updatedSprintData.project_id = this.projectKey
            if (quillEditor) {
                const htmlContent = quillEditor.getHTML();
                this.updatedSprintData.description = htmlContent
            }
            try {
                this.$store.commit('showLoader');
                const response = await axios.put(`${BASE_URL}api/development/sprints`, this.updatedSprintData, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                        token: this.authToken,
                    }
                })
                if (response.status === 200) {
                    this.getAllSprints();
                    this.resetValues()
                    Swal.fire({
                        title: response.data.message,
                        icon: 'success',
                    });
                    this.$refs.createSprintModal.classList.remove('show');
                    this.$refs.createSprintModal.setAttribute('aria-hidden', 'true');
                    this.$refs.createSprintModal.style.display = 'none';
                    this.removeModalBackdrop();
                } else {
                    new Noty({
                        type: 'error',
                        text: response.data.message,
                        timeout: 500,
                    }).show()
                }
                this.$store.commit('hideLoader');
            } catch (error) {
                this.$store.commit('hideLoader');
                new Noty({
                    type: 'error',
                    text: error.response.data.message,
                    timeout: 500,
                }).show()
            }
        },
        async deleteSprint(id) {
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
                        const response = await axios.delete(`${BASE_URL}api/development/sprints?id=${id}`, {
                            headers: {
                                token: this.authToken
                            }
                        })
                        this.getAllSprints();
                        Swal.fire('Deleted!', response.data.message, 'success');
                    } catch (error) {
                        this.getAllSprints();
                        Swal.fire('Error!', error.response.data.message, 'error');
                    }
                }
            });
        },
        removeModalBackdrop() {
            const modalBackdrop = document.getElementsByClassName('modal-backdrop');
            if (modalBackdrop.length > 0) {
                document.body.classList.remove('modal-open');
                document.body.removeChild(modalBackdrop[0]);
            }
        },
        toggleDropdown(index) {
            this.allSprints[index].showDropdown = !this.allSprints[index].showDropdown;
        },
        async getAllSprints() {
            try {
                this.$store.commit('showLoader');
                const response = await axios.get(`${BASE_URL}api/development/sprints?key=backlog&id=${this.projectKey}`, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                        token: this.authToken,
                    }
                });
                this.allSprints = response.data.sprintAndIssues
                this.$store.commit('hideLoader');
            } catch (error) {
                console.log(error);
                new Noty({
                    type: 'error',
                    text: error.response.data.detail,
                    timeout: 500,
                }).show()
                this.$store.commit('hideLoader');
            }
        },
        showSweetAlert() {
            Swal.fire({
                icon: 'info',
                title: 'Select Project',
                text: 'Please select a project.',
                confirmButtonText: 'OK',
            }).then(() => {
                this.$router.push('/projects');
            });
        },
        getPriorityIcon(priority) {
            switch (priority) {
                case 'low':
                    return 'low-icon';
                case 'lowest':
                    return 'lowest-icon';
                case 'medium':
                    return '../../assets/img/priorityImages1/medium.png';
                case 'high':
                    return 'high-icon';
                case 'highest':
                    return 'highest-icon';
                default:
                    return 'default-icon';
            }
        },
    },
    mounted() {
        this.getAllSprints();
        this.filteredSprints

    },
    watch: {
        'sprintData.start_date': function (newStartDate) {
            if (this.sprintData.end_date < newStartDate) {
                this.sprintData.end_date = newStartDate;
            }
        },
        '$route.params.key': function (newKey, oldKey) {
            if (newKey !== oldKey) {
                this.projectKey = newKey || null;
            }
        },
    }
};
</script>

<style scoped>
::v-deep .ql-container {
    max-height: 300px;
}

::v-deep .ql-editor img {
    width: 150px;
    height: auto;
    margin: 5px;
    border-radius: 8px;
    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
}

::v-deep .ql-editor {
    height: auto;
    max-height: 300px;
    overflow-y: auto;
    color: black;
}

::v-deep .ql-tooltip {
    position: fixed;
    left: 50% !important;
    transform: translateX(-50%) !important;
    max-height: 500px;
    overflow-y: auto;
    z-index: 99;
}

.priority-icon {
    width: 20px;
    height: 20px;
}

.low-icon {
    background-image: url('../../assets/img/priorityImages1/low.png');
}

.lowest-icon {
    background-image: url('../../assets/img/priorityImages1/lowest.png');
}

.medium-icon {
    background-image: url('../../assets/img/priorityImages1/medium.png');
}

.high-icon {
    background-image: url('../../assets/img/priorityImages1/high.png');
}

.highest-icon {
    background-image: url('../../assets/img/priorityImages1/highest.png');
}

.modalBody {
    max-height: calc(100vh - 150px);
    overflow: auto;
}

@media (max-width: 576px) {
    .modal-dialog {
        max-width: 99%;
        margin: auto;
    }

    .sprint-card {
        gap: 40px;
    }
}

@media (min-width: 577px) and (max-width: 992px) {
    .modal-dialog {
        max-width: 80%;
        margin: auto;
    }
}

@media (min-width: 993px) {
    .modal-dialog {
        max-width: 50%;
        margin: auto;
    }
}

.close :hover {
    cursor: pointer;
    border: 1px solid red;
    z-index: 999999999999999999999;

}

.drop-icon {
    padding: 5px;
    border-radius: 10px;
}

.drop-icon:hover {
    background-color: lightgray;
    cursor: pointer;
}

.sprint-head {
    color: white;
}

.sprint-card {
    width: auto;
    padding-left: 10px;
    overflow: auto;
    margin: auto;
    margin-bottom: 15px !important;
    border-radius: 8px;
    box-shadow: rgba(0, 0, 0, 0.09) 0px 2px 1px, rgba(0, 0, 0, 0.09) 0px 2px 2px, rgba(0, 0, 0, 0.09) 0px 2px 2px, rgba(117, 117, 117, 0.09) 0px 2px 2px, rgba(117, 117, 117, 0.09) 0px 2px 2px;
}

.issue-card {
    margin: auto;
    width: auto;
    border-radius: 8px;
}
</style>
      