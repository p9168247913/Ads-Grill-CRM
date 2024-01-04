<!-- Home.vue -->
<template>
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
                                            <input type="date" class="form-control" v-model="sprintData.startDate" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">End Date</label>
                                            <input type="date" class="form-control" v-model="sprintData.endDate" required>
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
            headers: ['S.No.', 'Sprint Name', 'Sprint Duration', 'Start Date', 'End Date', 'Goal', 'Actions'],
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
            this.sprintData= {
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
      