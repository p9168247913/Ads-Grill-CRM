<template>

    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Webkit | Responsive Bootstrap 4 Admin Dashboard Template</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
    </head>
    <!-- <LoaderComponent v-if="isLoading" /> -->
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
                                    placeholder="Search by name, role, designation or number..." />
                            </div>
                        </div>
                        <div class="col-md-6 col-lg-6 col-sm-12 d-flex justify-content-lg-end justify-content-md-end">
                            <div class="d-grid gap-2" style="display: flex!important; flex-direction: row;">
                                <button v-if="authUser.role == 'super-admin'" type="button"
                                    style="width: auto; height: 40px !important;"
                                    class="btn btn-sm btn-dark mb-0 px-2 py-1 mb-0 nav-link active"
                                    data-bs-toggle="modal" data-bs-target="#createRoleModal">
                                    <i class="fas fa-plus-circle text-success text-sm opacity-10"></i>&nbsp;
                                    &nbsp;Create
                                    Role
                                </button>
                                <button v-if="authUser.role == 'super-admin'" type="button"
                                    style="width: auto; height: 40px !important;"
                                    class="btn btn-sm btn-dark mb-0 px-2 py-1 mb-0 nav-link active"
                                    data-bs-toggle="modal" data-bs-target="#createAdmin">
                                    <i class="fas fa-plus-circle text-success text-sm opacity-10"></i>&nbsp;
                                    &nbsp;Create
                                    Admin
                                </button>
                                <button v-if="authUser.role == 'admin'" type="button"
                                    style="width: auto; height: 40px !important;"
                                    class="btn btn-sm btn-dark mb-0 px-2 py-1 mb-0 nav-link active"
                                    data-bs-toggle="modal" data-bs-target="#createUser" @click="getUserRole">
                                    <i class="fas fa-plus-circle text-success text-sm opacity-10"></i>&nbsp;
                                    &nbsp;Create
                                    User
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Modal for Create Role -->
                <div data-bs-backdrop="static" class="modal fade" id="createRoleModal" tabindex="-1"
                    aria-labelledby="createRoleModalLabel" aria-hidden="true" @hidden="createRole">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px;">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createRoleModalLabel">Create Role</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal"
                                    aria-label="Close"></button>
                            </div>
                            <div class="modal-body modalBody"
                                style="padding-bottom: 0; height:52vh; border: 1px solid red;">
                                <form @submit="createRole($event)">
                                    <div class="mb-3">
                                        <label for="roleName" class="form-label">Role Name</label>
                                        <input type="text" class="form-control" id="roleName"
                                            placeholder="Enter role name..." v-model="roleName">
                                    </div>
                                    <div class="modal-footer"
                                        style="z-index: 999; margin-top: 15px; position: sticky; bottom: 0; background-color: white; margin-bottom: -500px;">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                                            @click="roleName = ''">Close</button>
                                        <button type="button" class="btn btn-primary">Add</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Modal for Create admin -->
                <div data-bs-backdrop="static" class="modal fade" id="createAdmin" tabindex="-1"
                    aria-labelledby="createadminLabel" aria-hidden="true" @hidden="createUser">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px;">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createadminLabel">Create Admin</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal"
                                    aria-label="Close"></button>
                            </div>
                            <div class="modal-body modalBody"
                                style="padding-bottom: 0; height:52vh; border: 1px solid red;">
                                <form @submit="createUser($event), resetValues()">
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="name" class="form-label">Name</label>
                                            <input type="text" class="form-control" v-model="name" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="email" class="form-label">Designation</label>
                                            <input type="text" class="form-control" v-model="designation" required>
                                        </div>
                                    </div>
                                    <!-- Second Row -->
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="email" class="form-label">Email</label>
                                            <input type="text" class="form-control" v-model="email" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="password" class="form-label">Password</label>
                                            <input type="password" class="form-control" v-model="password" required>
                                        </div>
                                    </div>
                                    <!-- Second Row -->
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="Pincode" class="form-label">Pincode</label>
                                            <input type="text" class="form-control" v-model="pincode" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="role" class="form-label">Role</label>
                                            <input type="text" class="form-control" disabled value="admin">
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="contact_no" class="form-label">Contact No</label>
                                            <input type="text" class="form-control" v-model="contact_no" required>
                                        </div>
                                    </div>
                                    <div class="modal-footer"
                                        style="z-index: 999; margin-top: 15px; position: sticky; bottom: 0; background-color: white; margin-bottom: -500px;">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                                            @click="resetValues">Close</button>
                                        <button type="submit" class="btn btn-primary">Send</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- end -->

                <!-- Modal for Create user -->
                <div data-bs-backdrop="static" class="modal fade" id="createUser" tabindex="-1"
                    aria-labelledby="createadminLabel" aria-hidden="true" @hidden="createUser">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px;">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createadminLabel">Create User</h5>
                                <button ref="modalAddCloseBtn" class="btn-close bg-dark text-xs" type="button"
                                    data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body modalBody" style="padding-bottom: 0; height:52vh">
                                <form @submit="createUser($event), resetValues()">
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="name" class="form-label">Name</label>
                                            <input type="text" class="form-control" v-model="name" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="email" class="form-label">Email</label>
                                            <input type="text" class="form-control" v-model="email" required>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="Role" class="form-label">Role</label>
                                            <select @change="handleDesignation" class="form-select" id="role"
                                                name="role" v-model="selectedRole" required>
                                                <option value="" disabled selected>Select Role</option>
                                                <option v-for="(item, index) in userRole" :key="index"
                                                    :value="`${item.id},${item.name}`"> {{
                                    item.name }}</option>
                                            </select>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="Designation" class="form-label">Designation</label>
                                            <select class="form-select" id="Designation" name="Designation"
                                                v-model="selectedDesgination" required>
                                                <option value="" disabled selected>Select Designation</option>
                                                <option v-for="(item, index) in filteredDesignations" :key="index"
                                                    :value="item"> {{
                                    item }}</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="contactno" class="form-label">Contact No</label>
                                            <input type="text" class="form-control" v-model="contact_no" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="Pincode" class="form-label">Pincode</label>
                                            <input type="text" class="form-control" v-model="pincode" required>
                                        </div>

                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="password" class="form-label">Password</label>
                                            <input type="password" class="form-control" v-model="password" required>
                                        </div>
                                    </div>
                                    <div class="modal-footer"
                                        style="z-index: 999; margin-top: 15px; position: sticky; bottom: 0; background-color: white; margin-bottom: -500px;">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                                            @click="resetValues()">Close</button>
                                        <button type="submit" class="btn btn-primary">Create</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Modal for Edit Details -->
                <div data-bs-backdrop="static" class="modal fade" id="edituser" tabindex="-1" aria-labelledby="edituser"
                    aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px;">
                            <div class="modal-header">
                                <h5 class="modal-title" id="editdetails">Edit Details</h5>
                                <button ref="modalCloseBtn" class="btn-close bg-dark text-xs" type="button"
                                    data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body modalBody" style="padding-bottom: 0; height:44vh">
                                <form @submit="editUser($event)">
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="name" class="form-label">Name</label>
                                            <input type="text" v-model="editData.name" class="form-control" id="name"
                                                name="name">
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="email" class="form-label">Email</label>
                                            <input type="email" v-model="editData.email" class="form-control" id="email"
                                                name="email" disabled>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="editRole" class="form-label">Role</label>
                                            <input v-model="editData.role" type="text" class="form-control"
                                                id="designation" name="designation" disabled>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="contactNo" class="form-label">Contact Number</label>
                                            <input v-model="editData.contact_no" type="tel" class="form-control"
                                                id="contactNo" name="contactNo">
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="Pincode" class="form-label">Pincode</label>
                                            <input v-model="editData.pincode" type="text" class="form-control"
                                                id="pincode" name="pincode">
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="Designation" class="form-label">Designation</label>
                                            <input v-model="editData.designation" type="text" class="form-control"
                                                id="designation" name="designation" disabled>
                                        </div>
                                    </div>
                                    <div class="modal-footer"
                                        style="z-index: 999; margin-top: 25px; position: sticky; bottom: 0; background-color: white; margin-bottom: -500px;">
                                        <button type="button" class="btn btn-secondary"
                                            data-bs-dismiss="modal">Close</button>
                                        <button type="submit" class="btn btn-primary">Save</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>

                <!--Table-->
                <div v-if="users?.length" class="card" style="margin-top: 2rem;">
                    <div class="card-header pb-0 heads" style="overflow: auto; gap:20px;">

                        <h6>{{ $route.params.val.toUpperCase() }}</h6>

                        <div class="col-md-3 col-lg-4 col-sm-6 mb-3 d-flex">
                            <input class="form-control" v-model="start_date" type="date" placeholder="Start date" />
                            <span class="mt-2">&nbsp;to&nbsp;</span>
                            <input class="form-control" v-model="end_date" :min="start_date" :disabled="!start_date"
                                type="date" placeholder="End date" />
                        </div>
                        <div class="col-md-3 col-lg-3 col-sm-6 mb-3 d-flex gap-2">
                            <select
                                v-if="this.authUser.designation === 'project_manager' || this.authUser.designation === 'admin' || this.authUser.designation === 'super-admin'"
                                v-model="selectedEmployee" class="form-select">
                                <option value="" selected>Select Employee</option>
                                <option v-for="(item, index) in users" :key="index" :value="item.id"> {{
                                    item.name }}</option>
                            </select>
                            <select v-else v-model="selectedEmployee" class="form-select">
                                <option :value="this.authUser.id" selected>{{ this.authUser.name }}</option>
                                <!-- <option v-for="(item, index) in users" :key="index" :value="item.id"> {{
                                    item.name }}</option> -->
                            </select>
                            <button @click="downloadReport($event)" type="button"
                                v-if="this.selectedEmployee && this.start_date && this.end_date"
                                style="width: auto; height: 40px !important;"
                                class="btn btn-sm btn-dark mb-0 px-2 py-1 mb-0 nav-link active ">
                                <i class="bi bi-download"></i>
                                <span class="d-none d-md-inline">&nbsp; &nbsp;Report</span>
                            </button>
                        </div>
                    </div>
                    <div class="card-body px-0 pt-0 pb-2">
                        <div class="table-responsive p-0">
                            <table class="table align-items-center mb-0">
                                <thead style="position: sticky;  top: 0; background-color: whitesmoke; z-index: 1">
                                    <tr>
                                        <th style="color: #344767 !important;"
                                            class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold action-head"
                                            v-for="(header) in headers" :key="header">{{ header }}</th>
                                    </tr>
                                </thead>
                                <tbody v-for="(user, index) in paginatedUsers" :key="index">
                                    <tr>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex">
                                                <div>
                                                    <img :src="'data:image/jpeg;base64,' + user.profile_pic"
                                                        class="avatar avatar-sm me-3 rounded-circle" />
                                                </div>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ user.name }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ formatText(user.designation) }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ formatText(user.role) }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ user.email }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ user.contact_no }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ user.pincode }}</h6>
                                            </div>
                                        </td>
                                        <td class="align-middle actions">
                                            <i v-if="authUser.role == 'admin'"
                                                class="fas fa-pencil-alt text-primary mx-3 icon" data-bs-toggle="modal"
                                                data-bs-target="#edituser" style="margin-left: 20px; cursor: pointer;"
                                                @click="handleEditClick(user)"></i>
                                            <i v-else class="fas fa-pencil-alt text-primary mx-3 icon"
                                                style="color: dodgerblue !important; margin-left: 20px; cursor: not-allowed;"></i>

                                            <!-- Delete Icon -->
                                            <i v-if="authUser.role == 'admin'"
                                                class="fas fa-trash text-danger m-3 mx-3  icon" style="cursor: pointer;"
                                                @click="deleteUser(user.id)" data-toggle="tooltip"
                                                data-original-title="Delete user"></i>
                                            <i v-else class="fas fa-trash text-danger m-3 mx-3 icon"
                                                style="cursor: not-allowed;"></i>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <PaginationComponent v-if="users.length > 10" :currentPage="currentPage"
                        :itemsPerPage="itemsPerPage" :filteredUsers="filteredUsers" :prevPage="prevPage"
                        :nextPage="nextPage" :goToPage="goToPage" />
                </div>
                <div v-else>
                    No users found!!
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Noty from 'noty';
import { mapState } from 'vuex';
import Swal from 'sweetalert2';
import PaginationComponent from './Paginator/PaginatorComponent.vue';
import { BASE_URL } from '../config/apiConfig';

export default {
    components: {
        PaginationComponent,
    },
    data() {
        return {
            start_date: '',
            end_date: '',
            selectedEmployee: '',
            isLoading: false,
            searchTerm: '',
            name: '', email: '', role: '', contact_no: '', designation: '', pincode: '', password: '',
            editData: {
                userID: '', name: '', email: '', role: '', contact_no: '', designation: '', pincode: '',
            },
            isToggled: false,
            isAreaModal: false,
            displayToggle: 'none',
            users: [],
            headers: ['Profile', 'Name', 'Designation', 'Department', 'Email', 'Contact No.', 'Pincode', 'Actions'],
            roleName: '',
            createadminRole: 'admin',
            userRole: [],
            selectedRole: '',
            selectedRoleName: '',
            selectedDesgination: '',
            currentPage: 1,
            itemsPerPage: 10,
            designations: {
                "development": ['FE_Developer', 'BE_Developer', 'Full_Stack_Developer', 'Team_Lead', 'Project_Manager', 'Tester', 'Dev_Ops_Engineer', 'Product_Manager', 'QA_Engineer', 'UI_Designer', 'Junior_Web_Developer', 'Web_Developer', 'App_Developer', 'Software_Architecture'],
                "sales": ["Sales_Manager", "Sales_Associate"],
                "leads": ["Leads_Manager", "Leads_Associate", "Marketing_Manager"],
                "client": ["Client"],
                'admin': ['Admin'],
                "super_admin": ["super_admin"],
                "hr": ["hr"]
            }
        }
    },
    computed: {
        ...mapState(['authToken', 'authUser']),
        filteredUsers() {
            const searchLowerCase = this.searchTerm.toLowerCase() || ''
            return this.users.filter(user => {
                return (
                    user.name.toLowerCase().includes(searchLowerCase) ||
                    user.role.toLowerCase().includes(searchLowerCase) ||
                    user.designation.toLowerCase().includes(searchLowerCase) ||
                    user.contact_no.toLowerCase().includes(searchLowerCase)
                );
            });
        },
        paginatedUsers() {
            const startIndex = (this.currentPage - 1) * this.itemsPerPage;
            return this.filteredUsers.slice(startIndex, startIndex + this.itemsPerPage);
        },
        filteredDesignations() {
            const designationsForRole = this.designations[this.selectedRoleName] || [];
            return designationsForRole.map(item => this.removeUnderScores(item));
        }
    },
    methods: {
        extractFilename(response) {
            const contentDisposition = response.headers['content-disposition'];
            if (contentDisposition) {
                const filenameMatch = contentDisposition.match(/filename=([^;]+)/);
                console.log("nmae", filenameMatch);
                return filenameMatch ? filenameMatch[1] : 'download.zip';
            } else {
                return 'download.zip';
            }
        },
        async downloadReport(e) {
            e.preventDefault()
            const date_range = {
                start_date: this.start_date,
                end_date: this.end_date
            }
            try {
                this.$store.commit('showLoader')
                const response = await axios.get(`${BASE_URL}api/development/downloadUserWorkReport?id=${this.selectedEmployee}&date_range=${JSON.stringify(date_range)}`, {
                    headers: {
                        "Content-Type": "'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'",
                        token: this.authToken
                    },
                    responseType: 'blob'
                })
                if (response?.status === 200 && response?.data) {
                    const filename = this.extractFilename(response);
                    const blob = new Blob([response.data], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });

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
                    this.start_date = "";
                    this.end_date = "";
                    this.$store.commit('hideLoader');
                    this.selectedEmployee = "";
                }
                this.$store.commit('hideLoader')
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 500,
                }).show()
                this.$store.commit('hideLoader')
            }
        },
        formatText(inputText) {
            if (!inputText) {
                return '';
            }
            const words = inputText.split('_');

            const formattedWords = words.map(word => word.charAt(0).toUpperCase() + word.slice(1));

            const formattedText = formattedWords.join(' ');

            return formattedText;
        },
        nextPage() {
            if (this.currentPage * this.itemsPerPage < this.filteredUsers.length) {
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
            this.displayedUsers = this.filteredUsers.slice(startIndex, endIndex);
        },
        resetValues() {
            this.closeModal
            this.email = ''
            this.name = ''
            this.contact_no = ''
            this.designation = ''
            this.password = ''
            this.pincode = ''
            this.role = ''
            this.selectedRole = ''
            this.selectedDesgination = ''
        },
        async getUserRole() {
            try {
                this.$store.commit('showLoader')
                const response = await axios.get(`${BASE_URL}api/roles/`);
                if (response.status === 200) {
                    this.userRole = response.data.roles
                }
                this.$store.commit('hideLoader')
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 500,
                }).show()
                this.$store.commit('hideLoader')
            }
        },
        handleDesignation() {
            this.selectedRoleName = this.selectedRole.split(',')[1]
            this.selectedDesgination = ''
        },
        removeUnderScores(value) {
            // return value.replace(/_/g, ' ')
            let result = ''
            for (let i = 0; i < value.length; i++) {
                if (value[i] == '_') {
                    result += ' '
                }
                else {
                    result += value[i]
                }
            }
            return result
        },
        formatDesignationToLowerCaseAndUnderScores() {
            let designation = this.selectedDesgination.toLowerCase()
            let result = ''
            for (let i = 0; i < designation.length; i++) {
                if (designation[i] == ' ') {
                    result += '_'
                }
                else {
                    result += designation[i]
                }
            }
            return result
        },
        async createRole(e) {
            e.preventDefault()
            if (!this.roleName) {
                Swal.fire({
                    title: 'Please enter role name',
                    icon: 'warning',
                })
            }
            else {
                try {
                    this.$store.commit('showLoader')
                    const response = await axios.post(`${BASE_URL}api/roles/?role=${this.roleName}`)
                    if (response.status == 201) {
                        Swal.fire({
                            title: response.data.message,
                            icon: 'success',
                        })
                        this.roleName = ''
                    }
                    this.$store.commit('hideLoader')
                } catch (error) {
                    new Noty({
                        type: 'error',
                        text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                        timeout: 500,
                    }).show()
                    this.$store.commit('hideLoader')
                }
            }
        },
        handleEditClick(user) {
            this.editData.userID = user.id
            this.editData.name = user.name
            this.editData.email = user.email
            this.editData.role = user.role
            this.editData.contact_no = user.contact_no
            this.editData.designation = user.designation
            this.editData.pincode = user.pincode
        },
        async editUser(e) {
            e.preventDefault();
            try {
                this.$store.commit('showLoader')
                const response = await axios.put(`${BASE_URL}api/users/`, this.editData, {
                    headers: { token: this.authToken },
                },
                )
                if (response.status == 200) {
                    this.users = response.data.users
                    Swal.fire({
                        title: response.data.message,
                        icon: 'success',
                    })
                    this.getUsers(this.$route.params.val);
                    this.$refs.modalCloseBtn.click()
                    this.resetValues();
                }
                this.$store.commit('hideLoader')
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 500,
                }).show()
                this.$store.commit('hideLoader')
            }
        },
        async deleteUser(id) {
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
                        this.$store.commit('showLoader')
                        const response = await axios.delete(`${BASE_URL}api/users/`, {
                            params: {
                                userID: id
                            },
                            headers: { token: this.authToken },
                        });
                        if (response.status === 204) {
                            Swal.fire('Deleted!', 'The user has been deleted.', 'success');
                            this.getUsers()
                        }
                        this.$store.commit('hideLoader')
                    } catch (error) {
                        Swal.fire('Error!', error.response.data.message ? error.response.data.message : error.response.data.detail, 'error');
                        this.$store.commit('hideLoader')
                    }
                }
            });
        },
        openModal() {
            this.displayToggle = 'block';
            this.isToggled = !this.isToggled;
        },
        async createUser(e) {
            e.preventDefault()
            let requestData = {
                email: this.email,
                name: this.name,
                role: '',
                contact_no: this.contact_no,
                designation: '',
                pincode: this.pincode,
                password: this.password
            }
            requestData.designation = this.formatDesignationToLowerCaseAndUnderScores()
            if (this.authUser.role == 'admin') {
                requestData.role = this.selectedRole.split(',')[0]
            }
            else if (this.authUser.role == 'super-admin') {
                let admin = this.userRole.find((item) => {
                    return item.name == 'admin'
                })
                requestData.role = admin.id
            }

            try {
                this.$store.commit('showLoader')
                const response = await axios.post(`${BASE_URL}api/create/user/`, requestData, {
                    headers: {
                        token: this.authToken,
                        'Content-Type': "multipart/form-data",
                    }
                })
                if (response.status == 201) {
                    Swal.fire({
                        title: 'User created successfully!',
                        icon: 'success',
                    })
                    this.getUsers(this.$route.params.val);
                    this.$refs.modalAddCloseBtn.click()
                    this.resetValues()
                }
                this.$store.commit('hideLoader')
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail ? error.response.data.detail : error.response.data.email,
                    timeout: 500,
                }).show()
                this.$store.commit('hideLoader')
            }
        },
        closeModal() {
            this.displayToggle = 'none';
            this.isToggled = !this.isToggled;
        },
        async getUsers(role) {
            try {
                this.$store.commit('showLoader')
                const response = await axios.get(`${BASE_URL}api/users/`, {
                    params: { role: role },
                    headers: { token: this.authToken },
                },
                )
                console.log(response);
                if (response.status == 200) {
                    this.users = response.data.users
                }
                this.$store.commit('hideLoader')
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 500,
                }).show()
                this.$store.commit('hideLoader')
            }
        },
    },
    watch: {
        '$route.params.val': 'getUsers',
        start_date: {
            handler() {
                this.end_date = '';
            }
        },
    },
    created() {
        this.getUsers(this.$route.params.val)
    },

}
</script>

<style>
.heads {
    display: flex;
    justify-content: space-between
}

@media (max-width: 576px) {
    .heads {
        display: flex;
        flex-direction: column
    }
}

.modalBody {
    max-height: calc(100vh - 200px);
    overflow: auto;
    height: auto
}

.icon:hover {
    transform: scale(1.1);
}

.actions {
    margin-left: 15px !important;
    position: sticky;
    right: 0;
    z-index: 0;
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

.avatar:hover {
    transform: scale(2.15);
    transition: transform 0.3s ease;
}

.table-responsive {
    overflow-x: auto;
    max-height: 60vh;
}

.scrollable-body {
    display: block;
    max-height: inherit;
    overflow-y: auto;
}

.delete-icon {
    transition: background-color 0.3s, color 0.3s;
    padding: 8px;
    border-radius: 50%;
}

.delete-icon:hover {
    background-color: #ff0000;
    color: white !important;
}

.edit-icon {
    transition: background-color 0.3s, color 0.3s;
    padding: 8px;
    border-radius: 50%;
}

.edit-icon:hover {
    background-color: dodgerblue;
    color: rgb(251, 251, 251) !important;
}
</style>
