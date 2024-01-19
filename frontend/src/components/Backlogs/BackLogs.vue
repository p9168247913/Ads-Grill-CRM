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
                <div class="modal fade" ref="createProjectModal" id="createSprint" tabindex="-1"
                    aria-labelledby="createProjectLabel" aria-hidden="true" @hidden="createProjects">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createProjectLabel">Create Sprint</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body modalBody">
                                <form @submit="createSprints($event), resetValues()">
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">Sprint Name</label>
                                            <select class="form-control" v-model="sprintData.project_id" required>
                                                <option value="">Select Type</option>
                                                <option value="31">CRM_1234</option>
                                                <!-- <option v-for="(tag, index) in tags" :key="index" :value="tag.name">{{
                                                    tag.name }}</option> -->
                                            </select>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="projectName" class="form-label">Duration</label>
                                            <select class="form-control" v-model="sprintData.reporter_id" required>
                                                <option value="">Select Type</option>
                                                <option value="18">Abhishek</option>
                                                <!-- <option v-for="(tag, index) in tags" :key="index" :value="tag.name">{{
                                                    tag.name }}</option> -->
                                            </select>
                                        </div>
                                    </div>

                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">Key</label>
                                            <input type="text" class="form-control" v-model="sprintData.key" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="projectName" class="form-label">Description</label>
                                            <input type="text" class="form-control" v-model="sprintData.description"
                                                required>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="key" class="form-label">Start Date</label>
                                            <input type="datetime-local" class="form-control"
                                                v-model="sprintData.start_date" :min="currentDateTime()" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">End Date</label>
                                            <input type="datetime-local" class="form-control" v-model="sprintData.end_date"
                                                :min="sprintData.start_date" :disabled="sprintData.start_date.length === 0"
                                                required>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">Sprint Name</label>
                                            <input type="text" class="form-control" v-model="sprintData.name" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="projectName" class="form-label">Duration</label>
                                            <input type="text" class="form-control" :disabled="true"
                                                :value="calculateDuration()" required>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">Goal</label>
                                            <input type="text" class="form-control" v-model="sprintData.goal" required>
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
                <div class="modal fade" ref="createProjectModal" id="editSprint" tabindex="-1"
                    aria-labelledby="createProjectLabel" aria-hidden="true" @hidden="createProjects">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createProjectLabel">Edit Sprint</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body modalBody">
                                <form @submit="createSprints($event), resetValues()">
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">Sprint Name</label>
                                            <input type="text" class="form-control" v-model="sprintData.sprint_name"
                                                required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="projectName" class="form-label">Duration</label>
                                            <input type="text" class="form-control" v-model="sprintData.sprintDuration"
                                                required>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="key" class="form-label">Start Date</label>
                                            <input type="datetime-local" class="form-control" v-model="sprintData.startDate"
                                                :min="currentDateTime()" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">End Date</label>
                                            <input type="datetime-local" class="form-control" v-model="sprintData.endDate"
                                                required>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">Goal</label>
                                            <input type="text" class="form-control" v-model="sprintData.goal" required>
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
                        <h6>SPRINTS</h6>
                    </div>
                    <div class="card-body px-0 pt-0 pb-1">
                        <div class="table-responsive p-1">
                            <div class="align-items-center mb-0 sprint-card" v-for="(sprint, index) in filteredSprints"
                                :key="index">
                                <div style="display: flex; gap: 20px; align-items: center;">
                                    <div class="d-flex flex-row justify-content-center">
                                        <span class="mb-0 text-sm"><i @click="toggleDropdown(index)"
                                                class="fa fa-chevron-down drop-icon"></i></span>
                                    </div>
                                    <div class="d-flex flex-row justify-content-center">
                                        <h6 class="mb-0 text-sm">{{ sprint.project.key }}</h6>
                                    </div>
                                    <div class="d-flex flex-row justify-content-center">
                                        <h6 class="mb-0 text-sm">{{ sprint.name }}</h6>
                                    </div>
                                    <div class="d-flex flex-row justify-content-center ">
                                        <p class="mb-0 text-sm" style="font-size: smaller;">{{ formatDate(sprint.start_date)
                                        }} - {{ formatDate(sprint.end_date) }}</p>
                                    </div>
                                    <div class="d-flex flex-row justify-content-center">
                                        <p class="mb-0 text-sm" style="font-size: smaller;">({{ sprint.issues.length }}
                                            issues)</p>
                                    </div>
                                    <!-- <div class="d-flex flex-column justify-content-center">
                                        <h6 class="mb-0 text-sm">{{ sprint.name }}</h6>
                                    </div><div class="d-flex flex-column justify-content-center">
                                        <h6 class="mb-0 text-sm">{{ sprint.name }}</h6>
                                    </div><div class="d-flex flex-column justify-content-center">
                                        <h6 class="mb-0 text-sm">{{ sprint.name }}</h6>
                                    </div> -->
                                    <div class="col text-end">
                                        <button class="btn btn-link dropdown-open" type="button" id="dropdownMenuButton2"
                                            data-bs-toggle="dropdown" aria-expanded="false">
                                            <i class="fas fa-ellipsis-h"></i>
                                        </button>
                                        <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownMenuButton2">
                                            <li data-bs-toggle="modal" data-bs-target="#editSprint"><a class="dropdown-item"
                                                    href="#"><i class="fas fa-edit text-success"></i>&nbsp;&nbsp;Edit</a>
                                            </li>
                                            <li><a class="dropdown-item" href="#"><i
                                                        class="fas fa-trash-alt text-danger"></i>&nbsp;&nbsp;Delete</a></li>
                                        </ul>
                                    </div>
                                </div>
                                <div class="issue-card">
                                    <div v-show="sprint.showDropdown">
                                        <table class="table align-items-center mb-0">
                                            <tbody v-if="sprint.issues.length > 1">
                                                <tr v-for="(issue, issueIndex) in sprint.issues" :key="issueIndex">
                                                    <td>
                                                        <div class="d-flex flex-row justify-content-center">
                                                            <h6 class="mb-0 text-sm">{{ issue.id }}</h6>
                                                        </div>
                                                    </td>
                                                    <td>
                                                        <div class="d-flex flex-row justify-content-center">
                                                            <h6 class="mb-0 text-sm">{{
                                                                issue.title }}</h6>
                                                        </div>
                                                    </td>
                                                    <td>
                                                        <div class="d-flex flex-row justify-content-center">
                                                            <h6 class="mb-0 text-sm">{{
                                                                issue.status }}</h6>
                                                        </div>
                                                    </td>
                                                </tr>
                                            </tbody>
                                            <tbody v-else>
                                                <tr style="margin: auto;">
                                                    <span style="color: rgb(253, 97, 97);">No issues found!</span>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
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
import Noty from 'noty';
// import Swal from 'sweetalert2';
import { mapState } from 'vuex'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import '@popperjs/core/dist/umd/popper.min.js';
import Popper from 'popper.js';
window.Popper = Popper;

export default {
    name: "backlogs",
    data() {
        return {
            searchTerm: '',
            headers: [" ", 'S.No.', 'Sprint Name', 'Sprint Duration', 'Start Date', 'End Date', 'Goal', 'Actions'],
            allSprints: [],
            sprintData: {
                project_id: '',
                reporter_id: '',
                name: '',
                key: '',
                description: '',
                exp_duration: '',
                start_date: '',
                end_date: '',
                goal: '',
            },
            projectId: 31
        };
    },
    components: {
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
    methods: {
        formatDate(dateString) {
            const options = { day: 'numeric', month: 'short' };
            const date = new Date(dateString);
            return date.toLocaleDateString('en-US', options);
        },
        resetValues() {
            this.sprintData = {
                sprint_name: '',
                sprintDuration: '',
                startDate: '',
                endDate: '',
                goal: '',
            }
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

        createSprints(e) {
            e.preventDefault()
            console.log("sprintData", this.sprintData);
        },
        toggleDropdown(index) {
            this.allSprints[index].showDropdown = !this.allSprints[index].showDropdown;
        },
        async getAllSprints() {
            try {
                this.$store.commit('showLoader');
                const response = await axios.get(`${BASE_URL}api/development/sprints?key=backlog&id=${this.projectId}`, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                        token: this.authToken,
                    }
                });
                this.allSprints = response.data.sprintAndIssues
                this.$store.commit('hideLoader');
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error,
                    timeout: 500,
                }).show()
                this.$store.commit('hideLoader');
            }
        }
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
    }
};
</script>

<style scoped>
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
    width: 98%;
    padding-left: 10px;
    overflow: auto;
    margin: auto;
    margin-bottom: 15px !important;
    border-radius: 8px;
    box-shadow: rgba(0, 0, 0, 0.09) 0px 2px 1px, rgba(0, 0, 0, 0.09) 0px 2px 2px, rgba(0, 0, 0, 0.09) 0px 2px 2px, rgba(117, 117, 117, 0.09) 0px 2px 2px, rgba(117, 117, 117, 0.09) 0px 2px 2px;
}

.issue-card {
    margin: auto;
    width: 95%;
    border-radius: 8px;
    background-color: rgb(232, 230, 230);
}
</style>
      