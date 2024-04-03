<template>

    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
    </head>
    <div class="wrapper" style="margin-bottom: 80px;">
        <div class="content-page">
            <div class="container-fluid" style="margin-top: 30px;">
                <div style="display: flex; justify-content: space-between;">
                    <h5 style="margin-left: 1rem;" class="sprint-head">{{ sprintData.activeSprint ?
                        sprintData.activeSprint.name : "" }}</h5>
                    <button @click="addIssue" type="button" style="width: auto; height: 40px !important;"
                        class="btn btn-sm btn-dark mb-0 px-2 py-1 mb-0 nav-link active" data-bs-toggle="modal"
                        data-bs-target="#createIssue">
                        <i class="fas fa-plus-circle text-success text-sm opacity-10"></i>&nbsp;
                        &nbsp;Add Issue
                    </button>
                </div>

                <div style="margin-top: 3rem;" class="row">
                    <div class="col-md-6 col-lg-4 mb-3">
                        <div class="border issue-div">
                            <p class="card-head">TO DO</p>
                            <div v-if="sprintData.issues && sprintData.issues.to_do.length > 0">
                                <div class="issue-card" v-for="(issue, index) in sprintData.issues.to_do" :key="index">
                                    <div class="row p-2 align-items-center">
                                        <p style="font-size: 12px; font-weight: bold;" class="col">{{ issue.title }}</p>
                                        <div class="col text-end">
                                            <button class="btn btn-link issue-card-btn dropdown-open" type="button"
                                                id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
                                                <i class="fas fa-ellipsis-h"></i>
                                            </button>
                                            <ul style="background-color: gainsboro;"
                                                class="dropdown-menu dropdown-menu-end"
                                                aria-labelledby="dropdownMenuButton">
                                                <!-- <li data-bs-toggle="modal" data-bs-target="#editIssue"><a
                                                        class="dropdown-item" href="#"><i
                                                            class="fas fa-edit text-success"></i>&nbsp;&nbsp;Edit</a>
                                                </li> -->
                                                <li v-if="this.authUser.designation === 'project_manager' || this.authUser.designation === 'team_lead'"
                                                    @click="deleteIssue(issue.id)"><a class="dropdown-item" href="#"><i
                                                            class="fas fa-trash-alt text-danger"></i>&nbsp;&nbsp;Delete</a>
                                                </li>
                                                <li v-else @click="notAllowed" style="cursor: not-allowed !important;">
                                                    <a class="dropdown-item" href="#"><i
                                                            class="fas fa-trash-alt text-danger"></i>&nbsp;&nbsp;Delete</a>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="row align-items-center "
                                        style="margin-left: 2px;width: 95%; margin-top: -20px;">
                                        <img style="width: 45px;" class="sc-1j9o0vm-0 dMMVlq" alt="Story"
                                            src="https://static.vecteezy.com/ti/vecteur-libre/p3/421699-icone-de-documentss-gratuit-vectoriel.jpg"
                                            aria-describedby="5673val-tooltip">
                                        <p class="story-name col-10 ps-0"
                                            style="margin-top: 15px; font-size: 12px; font-weight: bold;">{{
                        this.projectName }}</p>
                                    </div>
                                </div>
                            </div>
                            <div v-else class="no-issue">
                                No issues here
                                <!-- <button @click="addIssue"
                                    style="font-weight: bold;padding: 5px 8px; border: none; border-radius: 4px; background-color: rgb(65,225,190);">
                                    + Add</button> -->
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-4 mb-3">
                        <div class="border issue-div" style="">
                            <p class="card-head">IN PROGRESS</p>
                            <div v-if="sprintData.issues && sprintData.issues.in_progress.length > 0">
                                <div class="issue-card" v-for="(issue, index) in sprintData.issues.in_progress"
                                    :key="index">
                                    <div class="row p-2 align-items-center">
                                        <p style="font-size: 12px; font-weight: bold;" class="col">{{ issue.title }}</p>
                                        <div class="col text-end">
                                            <button class="btn btn-link issue-card-btn dropdown-open" type="button"
                                                id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
                                                <i class="fas fa-ellipsis-h"></i>
                                            </button>
                                            <ul style="background-color: gainsboro;"
                                                class="dropdown-menu dropdown-menu-end"
                                                aria-labelledby="dropdownMenuButton">
                                                <!-- <li data-bs-toggle="modal" data-bs-target="#editIssue"><a
                                                        class="dropdown-item" href="#"><i
                                                            class="fas fa-edit text-success"></i>&nbsp;&nbsp;Edit</a>
                                                </li> -->
                                                <li
                                                    v-if="this.authUser.designation === 'project_manager' || this.authUser.designation === 'team_lead'">
                                                    <a class="dropdown-item" href="#"><i
                                                            class="fas fa-trash-alt text-danger"></i>&nbsp;&nbsp;Delete</a>
                                                </li>
                                                <li v-else @click="notAllowed" style="cursor: not-allowed !important;">
                                                    <a class="dropdown-item" href="#"><i
                                                            class="fas fa-trash-alt text-danger"></i>&nbsp;&nbsp;Delete</a>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="row align-items-center "
                                        style="margin-left: 2px;width: 95%; margin-top: -20px;">
                                        <img style="width: 45px;" class="sc-1j9o0vm-0 dMMVlq" alt="Story"
                                            src="https://static.vecteezy.com/ti/vecteur-libre/p3/421699-icone-de-documentss-gratuit-vectoriel.jpg"
                                            aria-describedby="5673val-tooltip">
                                        <p class="story-name col-10 ps-0"
                                            style="margin-top: 15px; font-size: 12px; font-weight: bold;">{{
                        this.projectName }}</p>
                                    </div>
                                </div>
                            </div>
                            <div v-else class="no-issue">
                                No issues here
                                <!-- <button @click="addIssue"
                                    style="font-weight: bold;padding: 5px 8px; border: none; border-radius: 4px; background-color: rgb(65,225,190);">
                                    + Add</button> -->
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-4 mb-3">
                        <div class="border issue-div">
                            <p class="card-head">DONE</p>
                            <div v-if="sprintData.issues && sprintData.issues.done.length > 0">
                                <div class="issue-card" v-for="(issue, index) in sprintData.issues.done" :key="index">
                                    <div class="row p-2 align-items-center">
                                        <p style="font-size: 12px; font-weight: bold;" class="col">{{ issue.title }}</p>
                                        <div class="col text-end">
                                            <button class="btn btn-link issue-card-btn dropdown-open" type="button"
                                                id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
                                                <i class="fas fa-ellipsis-h"></i>
                                            </button>
                                            <ul style="background-color: gainsboro;"
                                                class="dropdown-menu dropdown-menu-end"
                                                aria-labelledby="dropdownMenuButton">
                                                <!-- <li data-bs-toggle="modal" data-bs-target="#editIssue"><a
                                                        class="dropdown-item" href="#"><i
                                                            class="fas fa-edit text-success"></i>&nbsp;&nbsp;Edit</a>
                                                </li> -->
                                                <li
                                                    v-if="this.authUser.designation === 'project_manager' || this.authUser.designation === 'team_lead'">
                                                    <a class="dropdown-item" href="#"><i
                                                            class="fas fa-trash-alt text-danger"></i>&nbsp;&nbsp;Delete</a>
                                                </li>
                                                <li v-else @click="notAllowed" style="cursor: not-allowed !important;">
                                                    <a class="dropdown-item" href="#"><i
                                                            class="fas fa-trash-alt text-danger"></i>&nbsp;&nbsp;Delete</a>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="row align-items-center "
                                        style="margin-left: 2px;width: 95%; margin-top: -20px;">
                                        <img style="width: 40px;" class="sc-1j9o0vm-0 dMMVlq" alt="Story"
                                            src="https://static.vecteezy.com/ti/vecteur-libre/p3/421699-icone-de-documentss-gratuit-vectoriel.jpg"
                                            aria-describedby="5673val-tooltip">
                                        <p class="story-name col-10 ps-0"
                                            style="margin-top: 15px; font-size: 12px; font-weight: bold;">{{
                        this.projectName }}</p>
                                    </div>
                                </div>
                            </div>
                            <div v-else class="no-issue">
                                No issues here
                                <!-- <button @click="addIssue"
                                    style="font-weight: bold;padding: 5px 8px; border: none; border-radius: 4px; background-color: rgb(65,225,190);">
                                    + Add</button> -->
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Modal for Create Sprint -->
            <div class="modal fade" ref="createProjectModal" id="createProject" tabindex="-1"
                aria-labelledby="createProjectLabel" aria-hidden="true" @hidden="createProjects">
                <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="createProjectLabel">Create Sprint</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body modalBody">
                            <form @submit="saveContent($event), resetValues()">
                                <div class="row">
                                    <div class="col-md-6 mb-3">
                                        <label for="type" class="form-label">Sprint Name</label>
                                        <input type="text" class="form-control" v-model="sprintData.sprint_name">
                                    </div>
                                    <div class="col-md-6 mb-3">
                                        <label for="projectName" class="form-label">Duration</label>
                                        <input type="text" class="form-control" v-model="sprintData.sprintDuration">
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-md-6 mb-3">
                                        <label for="key" class="form-label">Start Date</label>
                                        <input type="datetime-local" class="form-control" v-model="sprintData.startDate"
                                            :min="currentDateTime()" />
                                    </div>
                                    <div class="col-md-6 mb-3">
                                        <label for="type" class="form-label">End Date</label>
                                        <input type="datetime-local" class="form-control" v-model="sprintData.endDate"
                                            :min="sprintData.startDate" />
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-md-6 mb-3">
                                        <label for="type" class="form-label">Goal</label>
                                        <input type="text" class="form-control" v-model="sprintData.goal">
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

            <!-- Modal for Edit Issue -->
            <div class="modal fade" ref="createProjectModal" id="editIssue" tabindex="-1"
                aria-labelledby="createProjectLabel" aria-hidden="true" @hidden="createProjects">
                <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="createProjectLabel">Edit Issue</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body modalBody">
                            <form @submit="saveContent($event), resetValues()">
                                <div class="row">
                                    <div class="col-md-6 mb-3">
                                        <label for="task_name" class="form-label">Title</label>
                                        <input type="text" class="form-control" v-model="sprintData.task_name">
                                    </div>
                                    <div class="col-md-6 mb-3">
                                        <label for="sprint_name" class="form-label">Sprint Name</label>
                                        <!-- <input type="text" class="form-control" v-model="sprintData.sprint_name"
                                                required> -->
                                        <select class="form-select" v-model="sprintData.sprint_name">
                                            <option value="">Select Sprint Name</option>
                                            <option value="Sprint 1">Sprint 1</option>
                                            <option value="Sprint 2">Sprint 2</option>
                                            <!-- <option v-for="(tag, index) in tags" :key="index" :value="tag.name">{{
                                                    tag.name }}</option> -->
                                        </select>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-md-6 mb-3">
                                        <label for="expectedDuration" class="form-label">Estimated duration</label>
                                        <input type="text" class="form-control" v-model="sprintData.expectedDuration">
                                    </div>
                                    <div class="col-md-6 mb-3">
                                        <label for="actualDuration" class="form-label">Actual duration</label>
                                        <input type="text" class="form-control" v-model="sprintData.actualDuration">
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-md-6 mb-3">
                                        <label for="reportingManager" class="form-label">Reporting Manager</label>
                                        <select class="form-select" v-model="sprintData.reportingManager">
                                            <option value="">Select Sprint Name</option>
                                            <option value="Abhishek">Abhishek</option>
                                            <option value="Pawan">Pawan</option>
                                            <!-- <option v-for="(tag, index) in tags" :key="index" :value="tag.name">{{
                                                    tag.name }}</option> -->
                                        </select>
                                    </div>
                                    <div class="col-md-6 mb-3">
                                        <label for="assignee" class="form-label">Assignee</label>
                                        <select class="form-select" v-model="sprintData.assignee">
                                            <option value="">Assignee</option>
                                            <option value="Shantanu">Shantanu</option>
                                            <option value="Pushkaraj">Pushkaraj</option>
                                            <!-- <option v-for="(tag, index) in tags" :key="index" :value="tag.name">{{
                                                    tag.name }}</option> -->
                                        </select>
                                    </div>
                                    <div class="col-md-12 mb-3">
                                        <label for="type" class="form-label">Description</label>
                                        <QuillEditor required ref="editor" :modules="modules" theme="snow"
                                            toolbar="full" />
                                    </div>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                                        @click="resetValues">Close</button>
                                    <button type="submit" class="btn btn-primary">Save</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { BASE_URL } from '../../config/apiConfig';
import axios from 'axios';
import { mapState } from 'vuex';
import Swal from 'sweetalert2';
import Noty from 'noty';
import { QuillEditor } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import router from "@/router";

export default {
    name: "active-sprint",
    data() {
        return {
            projectKey: localStorage.getItem("projectId"),
            projectName: localStorage.getItem("projectname"),
            editorInstance: null,
            sprintData: {},
            updateSprintData: {}
        };
    },
    components: {
        QuillEditor,
    },
    computed: {
        ...mapState(['authUser', 'authToken']),
    },
    created() {
        const projectId = localStorage.getItem('projectId')
        if (!projectId) {
            this.showSweetAlert();
        } else if (projectId) {
            this.getSprintData();
        }
    },
    methods: {
        notAllowed() {
            new Noty({
                type: 'error',
                text: "❌ Access denied!! ",
                timeout: 500,
            }).show()
        },
        resetValues() { },
        currentDateTime() {
            const now = new Date();
            const formattedDateTime = now.toISOString().slice(0, 16);
            return formattedDateTime;
        },
        addIssue() {
            router.push("/issues")
        },
        createSprints() { },
        editIssue() { },
        saveContent(e) {
            e.preventDefault()
            if (this.$refs.editor) {
                const quillEditor = this.$refs.editor;
                if (quillEditor.getHTML) {
                    const htmlContent = quillEditor.getHTML();
                    this.updateSprintData.description = htmlContent
                } else {
                    new Noty({
                        type: 'error',
                        text: 'getHTML method is not available',
                        timeout: 1000,
                    }).show();
                }
            } else {
                new Noty({
                    type: 'error',
                    text: 'Quill editor reference not found',
                    timeout: 1000,
                }).show();
            }
        },
        async deleteIssue(id) {
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
                        const response = await axios.delete(`${BASE_URL}api/development/issues?id=${id}`, {
                            headers: {
                                token: this.authToken
                            }
                        })
                        this.getSprintData();
                        Swal.fire('Deleted!', response.data.message, 'success');
                    } catch (error) {
                        this.getSprintData();
                        Swal.fire('Error!', error.response.data.message ? error.response.data.message : error.response.data.detail, 'error');
                    }
                }
            });
        },
        async getSprintData() {
            const projectId = localStorage.getItem("projectId")
            try {
                this.$store.commit('showLoader');
                const response = await axios.get(`${BASE_URL}api/development/sprints?key=active_sprint&id=${projectId}`, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                        token: this.authToken,
                    }
                })
                if (response.status === 200) {
                    this.sprintData = response.data.activeSprintAndIssues
                    if (this.sprintData === undefined) {
                        this.showNoActiveSprintAlert();
                    }
                }
                this.$store.commit('hideLoader');
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show();
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
        showNoActiveSprintAlert() {
            Swal.fire({
                icon: 'info',
                title: 'No Active Sprint',
                text: 'There is no active sprint for the selected project.',
                confirmButtonText: 'OK',
            }).then(() => {
                this.$router.push('/backlogs');
            });
        },
    },
    mounted() {
        this.getSprintData()
    },
    watch: {
        'sprintData.startDate': function (newStartDate) {
            if (this.sprintData.endDate < newStartDate) {
                this.sprintData.endDate = newStartDate;
            }
        },
        '$route.params.key': function (newKey, oldKey) {
            if (newKey !== oldKey) {
                this.projectKey = newKey || null;
            }
        },
    },
}
</script>

<style scoped>
::v-deep .ql-container {
    max-height: 150px;
}

::v-deep .ql-editor img {
    width: 150px;
    height: auto;
    margin: 5px;
    border-radius: 8px;
    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
}

::v-deep .ql-editor {
    height: 250px;
    max-height: 150px;
    overflow-y: auto;
    color: black;
}

::v-deep .ql-tooltip {
    position: fixed;
    left: 50% !important;
    transform: translateX(-50%) !important;
    border: 1px solid red;
    max-height: 500px;
    overflow-y: auto;
    z-index: 99;
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

.issue-div {
    height: 70vh;
    background-color: #f3f3f3;
    border-radius: 5px;
    overflow-y: auto;
    position: relative;
}

.sprint-head {
    color: white;
}

.no-issue {
    /* border: 1px solid red; */
    font-size: 13px;
    font-weight: bold;
    padding-left: 15px;
    position: sticky;
    top: 0;
    background-color: #f3f3f3;
    z-index: 2;
}

.card-head {
    font-size: 12px;
    font-weight: bold;
    padding-left: 15px;
    padding-top: 10px;
    padding-bottom: 10px;
    position: sticky;
    top: 0;
    background-color: #f3f3f3;
    z-index: 2;
}

.issue-card {
    margin: auto;
    height: auto;
    width: 94%;
    background-color: white;
    border-radius: 5px;
    margin-bottom: 8px;
    position: relative;
    box-shadow: rgba(0, 0, 0, 0.09) 0px 2px 1px, rgba(0, 0, 0, 0.09) 0px 2px 2px, rgba(0, 0, 0, 0.09) 0px 2px 2px, rgba(117, 117, 117, 0.09) 0px 2px 2px, rgba(117, 117, 117, 0.09) 0px 2px 2px;
}

.issue-card:hover {
    background-color: rgb(240, 246, 246);
    transform: scale(1.005);
    transition: transform 0.3s;
    z-index: 1;
}

.issue-card-btn {
    position: absolute;
    top: 5px;
    right: 10px;
}

.issue-card-btn:hover {
    cursor: pointer;
    background-color: white;
    color: black !important;
}

.dropdown-menu:hover {
    z-index: 999;
}
</style>