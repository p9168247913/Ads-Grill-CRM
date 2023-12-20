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
                <div style="margin-top: 20px;">
                    <div class="row">
                        <div class="col-md-6 col-lg-6 col-sm-12 mb-3">
                            <div class="input-group">
                                <span class="input-group-text text-body">
                                    <i class="fas fa-search" aria-hidden="true"></i>
                                </span>
                                <input type="text" v-model="searchTerm" @change="filterUsers" class="form-control"
                                    placeholder="Search by name, role, designation or number..." />
                            </div>
                        </div>
                        <div class="col-md-6 col-lg-6 col-sm-12 d-flex justify-content-lg-end justify-content-md-end">
                            <div class="d-grid gap-2" style="display: flex!important; flex-direction: row;">
                                <button v-if="authUser.role == 'super-admin'" class="btn btn-primary mb-2 h-100"
                                    type="button" style="width: auto; height: 40px !important;" data-bs-toggle="modal"
                                    data-bs-target="#createRoleModal">Create Role</button>
                                <button v-if="authUser.role == 'super-admin'" class="btn btn-primary mb-2 h-100"
                                    type="button" style="width: auto;height: 40px !important;" data-bs-toggle="modal"
                                    data-bs-target="#createAdmin">Create Admin</button>
                                <button v-if="authUser.role == 'admin'" class="btn btn-primary mb-2 h-100" type="button"
                                    style="width: auto;height: 40px !important;" data-bs-toggle="modal"
                                    data-bs-target="#createUser" @click="getUserRole">Create User</button>
                            </div>    
                        </div>
                    </div>
                </div>
                <!-- Modal for Create Role -->
                <div class="modal fade" id="createRoleModal" tabindex="-1" aria-labelledby="createRoleModalLabel"
                    aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createRoleModalLabel">Create Role</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <form>
                                    <div class="mb-3">
                                        <label for="roleName" class="form-label">Role Name</label>
                                        <input type="text" class="form-control" id="roleName"
                                            placeholder="Enter role name..." v-model="roleName">
                                    </div>
                                </form>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                                    @click="roleName = ''">Close</button>
                                <button @click="createRole" type="button" class="btn btn-primary">Add</button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Modal for Create admin -->
                <div class="modal fade" id="createAdmin" tabindex="-1" aria-labelledby="createadminLabel"
                    aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createadminLabel">Create Admin</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <form>
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
                                </form>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                                    @click="resetValues">Close</button>
                                <button type="button" class="btn btn-primary" @click="createUser">Send</button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- end -->

                <!-- Modal for Create user -->
                <div class="modal fade" id="createUser" tabindex="-1" aria-labelledby="createadminLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createadminLabel">Create User</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <form>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="name" class="form-label">Name</label>
                                            <input type="text" class="form-control" v-model="name" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="desgination" class="form-label">Designation</label>
                                            <input type="text" class="form-control" v-model="designation" required>
                                        </div>
                                    </div>
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
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="Pincode" class="form-label">Pincode</label>
                                            <input type="text" class="form-control" v-model="pincode" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="Role" class="form-label">Role</label>
                                            <select class="form-select" id="role" name="role" v-model="selectedRole"
                                                required>
                                                <option value="" disabled selected>Select Role</option>
                                                <option v-for="(item, index) in userRole" :key="index" :value="item.id"> {{
                                                    item.name }}</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="contactno" class="form-label">Contact No</label>
                                            <input type="text" class="form-control" v-model="contact_no" required>
                                        </div>
                                    </div>
                                </form>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                                    @click="resetValues()">Close</button>
                                <button type="button" class="btn btn-primary" @click="createUser"
                                    data-bs-dismiss="modal">Send</button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Modal for Edit Details -->
                <div class="modal fade" id="edituser" tabindex="-1" aria-labelledby="edituser" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content" style="padding: 30px;">
                            <div class="modal-header">
                                <h5 class="modal-title" id="editdetails">Edit Details</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <form>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="name" class="form-label">Name</label>
                                            <input type="text" class="form-control" id="name" name="name">
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="email" class="form-label">Email</label>
                                            <input type="email" class="form-control" id="email" name="email">
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="Role" class="form-label">Role</label>
                                            <select class="form-select" id="role" name="role">
                                                <option value="select">Select...</option>
                                                <option value="option1">Option 1</option>
                                            </select>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="contactNo" class="form-label">Contact Number</label>
                                            <input type="tel" class="form-control" id="contactNo" name="contactNo">
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="Pincode" class="form-label">Pincode</label>
                                            <input type="text" class="form-control" id="pincode" name="pincode">
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="Designation" class="form-label">Designation</label>
                                            <input type="text" class="form-control" id="designation" name="designation">
                                        </div>
                                    </div>
                                </form>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <button type="button" class="btn btn-primary">Save Changes</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="card" style="margin-top: 2rem;">
                <!-- <h1>hello</h1> -->
                <div class="card-header pb-0">
                    <h6>{{ $route.params.val.toUpperCase() }}</h6>
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
                            <tbody v-for="(user, index) in paginatedUsers" :key="index">
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
                                        <i v-if="authUser.role == 'admin'" class="fas fa-pencil-alt text-primary fa-xs pr-4"
                                            data-bs-toggle="modal" data-bs-target="#edituser"
                                            style="color: dodgerblue !important; margin-left: 20px; cursor: pointer;"
                                            @click="handleEditClick"></i>
                                        <i v-else class="fas fa-pencil-alt text-primary fa-xs pr-4"
                                            style="color: dodgerblue !important; margin-left: 20px; cursor: not-allowed;"></i>

                                        <!-- Delete Icon -->
                                        <i v-if="authUser.role == 'admin'" class="fas fa-trash text-danger m-3 fa-xs"
                                            style="cursor: pointer;" @click="deleteUser" data-toggle="tooltip"
                                            data-original-title="Delete user"></i>
                                        <i v-else class="fas fa-trash text-danger m-3 fa-xs"
                                            style="cursor: not-allowed;"></i>
                                    </td>

                                </tr>
                            </tbody>
                        </table>
                        <PaginationComponent :currentPage="currentPage" :itemsPerPage="itemsPerPage"
                            :filteredUsers="filteredUsers" :prevPage="prevPage" :nextPage="nextPage" :goToPage="goToPage" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Noty from 'noty'
import { mapState } from 'vuex'
import Swal from 'sweetalert2';
import PaginationComponent from './Paginator/PaginatorComponent.vue';
export default {
    components: {
        PaginationComponent,
    },
    data() {
        return {
            searchTerm: '',
            name: '', email: '', role: '', contact_no: '', designation: '', pincode: '', password: '',
            isToggled: false,
            isAreaModal: false,
            displayToggle: 'none',
            users: [],
            headers: ['Profile', 'Name', 'Designation', 'Department', 'Contact No.', 'Pincode', 'Actions'],
            roleName: '',
            createadminRole: 'admin',
            userRole: [],
            selectedRole: '',
            currentPage: 1,
            itemsPerPage: 5,
        }
    },
    computed: {
        ...mapState(['authUser']),
        filteredUsers() {
            console.log(this.searchTerm);
            return this.users.filter(user => {
                const searchLowerCase = this.searchTerm.toLowerCase() || ''
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
        }
    },
    methods: {
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
        filterUsers() { },
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
        },
        getUserRole() {
            axios.get('http://127.0.0.1:8000/api/roles/').then((res => {
                this.userRole = res.data.roles
            }))
        },
        createRole() {
            if (!this.roleName) {
                Swal.fire({
                    title: 'Please enter role name',
                    icon: 'warning',
                })
            }
            else {
                axios.post(`http://127.0.0.1:8000/api/roles/?role=${this.roleName}`
                ).then((r => {
                    // console.log(r)
                    if (r.status == 201) {
                        new Noty({
                            type: 'success',
                            text: 'Role Created Successfully',
                            timeout: 500,
                        }).show()
                        this.roleName = ''
                    }
                }))
            }

        },
        async deleteUser() {
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
                        // Make an HTTP DELETE request to delete the user
                        await axios.delete('http://127.0.0.1:8000/api/users/', {
                            params: {
                                userID: ''
                            }
                        });
                        Swal.fire('Deleted!', 'The user has been deleted.', 'success');
                    } catch (error) {
                        Swal.fire('Error', 'An error occurred while deleting the user.', 'error');
                    }
                }
            });
        },
        openModal() {
            this.displayToggle = 'block';
            this.isToggled = !this.isToggled;
        },
        createUser() {
            if (!this.email || !this.name || !this.contact_no || !this.designation || !this.pincode || !this.password || !this.selectedRole) {
                Swal.fire({
                    title: 'Please fill all Fields',
                    icon: 'warning',
                })
            }
            else {
                let requestData = {
                    email: this.email,
                    name: this.name,
                    role: '',
                    contact_no: this.contact_no,
                    designation: this.designation,
                    pincode: this.pincode,
                    password: this.password
                }
                if (this.authUser.role == 'admin') {
                    requestData.role = this.selectedRole
                }
                else if (this.authUser.role == 'super-admin') {
                    requestData.role = 'admin'
                }

                axios.post('http://127.0.0.1:8000/api/create/user/', requestData).then((r) => {
                    //  .log(r.status)
                    if (r.status == 201) {

                        new Noty({
                            type: 'success',
                            text: 'user Created Successfully',
                            timeout: 500,
                        }).show()
                        this.getUsers(this.$route.params.val);
                        this.resetValues

                    }
                })
            }
        },
        closeModal() {
            this.displayToggle = 'none';
            this.isToggled = !this.isToggled;
        },
        getUsers(role) {
            // console.log(role)
            axios.get('http://127.0.0.1:8000/api/users/', {
                params: { role: role }
            }).then((r) => {
                this.users = r.data.users
                // console.log(this.users, 'userData')
            })
        },
    },
    watch: {
        '$route.params.val': 'getUsers'
    },
    created() {
        this.getUsers(this.$route.params.val)
    }

}
</script>

<style>
.table-responsive {
    overflow-x: auto;
    max-height: 350px;
}

.scrollable-body {
    display: block;
    max-height: inherit;
    overflow-y: auto;
}
</style>