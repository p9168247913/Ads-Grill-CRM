<!-- Home.vue -->
<template>
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
                    aria-labelledby="createProjectLabel" aria-hidden="true" @hidden="createProjects">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createProjectLabel">Create Issue</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body modalBody">
                                <form @submit="createSprints($event), resetValues()">
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="task_name" class="form-label">Title</label>
                                            <input type="text" class="form-control" v-model="sprintData.task_name" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="sprint_name" class="form-label">Sprint Name</label>
                                            <!-- <input type="text" class="form-control" v-model="sprintData.sprint_name"
                                                required> -->
                                            <select class="form-select" v-model="sprintData.sprint_name" required>
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
                                            <input type="text" class="form-control" v-model="sprintData.expectedDuration"
                                                required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="actualDuration" class="form-label">Actual duration</label>
                                            <input type="text" class="form-control" v-model="sprintData.actualDuration"
                                                required>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="reportingManager" class="form-label">Reporting Manager</label>
                                            <select class="form-select" v-model="sprintData.reportingManager" required>
                                                <option value="">Select Sprint Name</option>
                                                <option value="Abhishek">Abhishek</option>
                                                <option value="Pawan">Pawan</option>
                                                <!-- <option v-for="(tag, index) in tags" :key="index" :value="tag.name">{{
                                                    tag.name }}</option> -->
                                            </select>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="assignee" class="form-label">Assignee</label>
                                            <select class="form-select" v-model="sprintData.assignee" required>
                                                <option value="">Assignee</option>
                                                <option value="Shantanu">Shantanu</option>
                                                <option value="Pushkaraj">Pushkaraj</option>
                                                <!-- <option v-for="(tag, index) in tags" :key="index" :value="tag.name">{{
                                                    tag.name }}</option> -->
                                            </select>
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

export default {
    name: "backlogs",
    data() {
        return {
            headers: ['S.No.', 'Task Name', 'Sprint', 'Status', 'Task duration', 'Actual duration', 'Reporting Manager', 'Assignee', 'Actions'],
            allSprints: [],
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
        createSprints() { },
    }
};
</script>

<style>
.sprint-head {
    color: white;
}
</style>
      