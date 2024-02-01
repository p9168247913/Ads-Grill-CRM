<template>
    <div class="wrapper" style="margin-bottom: 80px;">
        <div v-if="projectKey !== ''" class="content-page">
            <div class="container-fluid" style="margin-top: 30px;">
                <h5 class="sprint-head">{{ sprintData.activeSprint ? sprintData.activeSprint.name : "" }}</h5>
                <div class="row">
                    <div class="col-md-6 col-lg-6 col-sm-12 mb-3">
                        <div class="input-group">
                            <span class="input-group-text text-body">
                                <i class="fas fa-search" aria-hidden="true"></i>
                            </span>
                            <input type="text" v-model="searchTerm" @change="filterUsers" class="form-control"
                                placeholder="Search Issue..." />
                        </div>
                    </div>
                </div>
                <div class="row">
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
                                            <ul class="dropdown-menu dropdown-menu-end"
                                                aria-labelledby="dropdownMenuButton">
                                                <li data-bs-toggle="modal" data-bs-target="#editIssue"><a
                                                        class="dropdown-item" href="#"><i
                                                            class="fas fa-edit text-success"></i>&nbsp;&nbsp;Edit</a>
                                                </li>
                                                <li><a class="dropdown-item" href="#"><i
                                                            class="fas fa-trash-alt text-danger"></i>&nbsp;&nbsp;Delete</a>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="row align-items-center "
                                        style="margin-left: 2px;width: 95%; margin-top: -20px;">
                                        <img style="width: 40px;" class="sc-1j9o0vm-0 dMMVlq" alt="Story"
                                            src="https://adsgrilltech.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium"
                                            aria-describedby="5673val-tooltip">
                                        <p class="story-name col-10 ps-0"
                                            style="margin-top: 15px; font-size: 12px; font-weight: bold;">PROJECT NAME</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-4 mb-3">
                        <div class="border issue-div" style="">
                            <p class="card-head">IN PROGRESS</p>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-4 mb-3">
                        <div class="border issue-div">
                            <p class="card-head">DONE</p>
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
                                        <QuillEditor required ref="editor" :modules="modules" theme="snow" toolbar="full" />
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
        <div v-else>
            <!-- <p>No project selected. Please select a project.</p> -->
        </div>
    </div>
</template>
  
<script>
import { BASE_URL } from '../../config/apiConfig';
import axios from 'axios';
import { mapState } from 'vuex';
import Swal from 'sweetalert2';
import { QuillEditor } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';

export default {
    name: "active-sprint",
    data() {
        return {
            projectKey: localStorage.getItem("projectId"),
            editorInstance: null,
            sprintData: {},
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
        resetValues() { },
        currentDateTime() {
            const now = new Date();
            const formattedDateTime = now.toISOString().slice(0, 16);
            return formattedDateTime;
        },
        createSprints() { },
        editIssue() { },
        saveContent(e) {
            e.preventDefault()
            if (this.$refs.editor) {
                const quillEditor = this.$refs.editor;
                // console.log('checkhtml', quillEditor)
                console.log(quillEditor['editor'])
                // for(let data in quillEditor){
                //     console.log(quillEditor['editor'])
                // }
                if (quillEditor.getHTML) {
                    const htmlContent = quillEditor.getHTML();
                    console.log("html",htmlContent);
                } else {
                    console.error('getHTML method is not available');
                }
            } else {
                console.error('Quill editor reference not found');
            }
        },
        async getSprintData() {
            const projectId = localStorage.getItem("projectId")
            try {
                const response = await axios.get(`${BASE_URL}api/development/sprints?key=active_sprint&id=${projectId}`, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                        token: this.authToken,
                    }
                })
                this.sprintData = response.data.activeSprintAndIssues
                if (this.sprintData === undefined) {
                    this.showNoActiveSprintAlert();
                }
            } catch (error) {
                console.log(error);
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
    padding-top: 20px;
    overflow-y: auto;
}

.sprint-head {
    color: white;
}

.card-head {
    font-size: 12px;
    font-weight: bold;
    margin-left: 15px;
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