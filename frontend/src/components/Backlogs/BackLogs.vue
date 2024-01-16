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
                                    data-bs-target="#createProject">
                                    <i class="fas fa-plus-circle text-success text-sm opacity-10"></i>&nbsp; &nbsp;Create
                                    Sprint
                                </button>
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
                    <!-- <div class="card-body px-0 pt-0 pb-2">
                        <div class="table-responsive p-0">
                            <table class="table align-items-center mb-0">
                                <thead>
                                    <tr>
                                        <th style="color: #344767 !important;"
                                            class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold"
                                            v-for="(head) in headers" :key="head">
                                            {{ head }}
                                        </th>
                                    </tr>
                                </thead>
                                <tbody v-for="(user, index) in allSprints" :key="index">
                                    <tr>
                                        <td>
                                            <div class="dropdown">
                                                <button class="btn btn-secondary dropdown-toggle" type="button"
                                                    id="dropdownMenuButton" data-bs-toggle="dropdown" aria-haspopup="true"
                                                    aria-expanded="false">
                                                    View Issues
                                                </button>
                                                <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                                    <table class="table">
                                                        <thead>
                                                            <tr>
                                                                <th>Issue ID</th>
                                                                <th>Title</th>
                                                                <th>Status</th>
                                                            </tr>
                                                        </thead>
                                                        <tbody>
                                                            <tr v-for="(issue, issueIndex) in user.issues"
                                                                :key="issueIndex">
                                                                <td>{{ issue.id }}</td>
                                                                <td>{{ issue.title }}</td>
                                                                <td>{{ issue.status }}</td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
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
                                            <i class="fas fa-pencil-alt text-primary fa-xs pr-4"
                                                style="color: dodgerblue !important; margin-left: 20px; cursor: not-allowed;"></i>

                                            <i v-if="authUser.role == 'admin'"
                                                class="fas fa-trash text-danger m-3 fa-xs delete-icon"
                                                style="cursor: pointer;" @click="deleteUser" data-toggle="tooltip"
                                                data-original-title="Delete user"></i>
                                            <i class="fas fa-trash text-danger m-3 fa-xs" style="cursor: not-allowed;"></i>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div> -->
                    <div class="card-body px-0 pt-0 pb-2">
                        <div class="table-responsive p-0">
                            <div v-for="(sprint, index) in allSprints" :key="index">
                                <div style="display: flex; gap: 15px; align-items: center; padding: 10px;">
                                    <i @click="toggleDropdown(index)" class="fa fa-chevron-down drop-icon"></i>
                                    <h6>{{ sprint.name }}</h6>
                                    <h6>{{ sprint.name }}</h6>
                                    <h6>{{ sprint.name }}</h6>
                                    <h6>{{ sprint.name }}</h6>
                                    <h6>{{ sprint.name }}</h6>
                                    <h6>{{ sprint.name }}</h6>
                                    <!-- Add more details as needed -->
                                </div>
                                <div>
                                    <div v-show="sprint.showDropdown">
                                        <!-- Issues table -->
                                        <table class="table align-items-center mb-0">
                                            <!-- <thead>
                                                <tr>
                                                    <th>Issue ID</th>
                                                    <th>Title</th>
                                                    <th>Status</th>
                                                </tr>
                                            </thead> -->
                                            <tbody>
                                                <tr v-for="(issue, issueIndex) in sprint.issues" :key="issueIndex">
                                                    <td>
                                                        <div class="d-flex flex-column justify-content-center">
                                                            <h6 class="mb-0 text-sm">{{ issue.id }}</h6>
                                                        </div>
                                                    </td>
                                                    <td>
                                                        <div class="d-flex flex-column justify-content-center">
                                                            <h6 class="mb-0 text-sm">{{
                                                                issue.title }}</h6>
                                                        </div>
                                                    </td>
                                                    <td>
                                                        <div class="d-flex flex-column justify-content-center">
                                                            <h6 class="mb-0 text-sm">{{
                                                                issue.status }}</h6>
                                                        </div>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- <PaginationComponent :currentPage="currentPage" :itemsPerPage="itemsPerPage" :filteredUsers="filteredUsers"
                      :prevPage="prevPage" :nextPage="nextPage" :goToPage="goToPage" /> -->
            </div>
        </div>
    </div>
</template>
      
<script>
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import '@popperjs/core/dist/umd/popper.min.js';
import Popper from 'popper.js';

// Use the global Popper object
window.Popper = Popper;

export default {
    name: "backlogs",
    data() {
        return {
            headers: [" ", 'S.No.', 'Sprint Name', 'Sprint Duration', 'Start Date', 'End Date', 'Goal', 'Actions'],
            allSprints: [{
                id: 1,
                name: "Sprint 1",
                designation: "fbdf",
                // role: "fbyj",
                contact_no: "dfh",
                pincode: "dfb",
                issues: [{
                    id: 1,
                    title: 'ydgf',
                    status: "hsgf"
                }]
            }, {
                id: 2,
                name: "Sprint 2",
                designation: "fbdf",
                // role: "fbyj",
                contact_no: "dfh",
                pincode: "dfb",
                issues: [{
                    id: 1,
                    title: 'gfjhfgjfgjfh',
                    status: "fgjfhjfhj"
                }]
            }],
            sprintData: {
                sprint_name: '',
                sprintDuration: '',
                startDate: '',
                endDate: '',
                goal: '',
            },
        };
    },
    components: {
    },
    methods: {
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
        createSprints() { },
        toggleDropdown(index) {
            this.allSprints[index].showDropdown = !this.allSprints[index].showDropdown;
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
}

.sprint-head {
    color: white;
}
</style>
      