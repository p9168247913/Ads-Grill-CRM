<template>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Webkit | Responsive Bootstrap 4 Admin Dashboard Template</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
    </head>
    <div class="wrapper">
        <!-- <h1>hhh</h1> -->
        <div class="content-page">
            <div class="container-fluid">
                <div style="margin-top: 20px;">
                    <div class="row">
                        <div class="col-md-6 col-lg-6 col-sm-12 mb-3">
                            <div class="input-group">
                                <span class="input-group-text text-body">
                                    <i class="fas fa-search" aria-hidden="true"></i>
                                </span>
                                <input type="text" class="form-control" placeholder="Type here..." v-model="searchTerm" />
                            </div>
                        </div>
                        <div class="col-md-6 col-lg-6 col-sm-12 d-flex justify-content-lg-end justify-content-md-end">
                            <div class="d-grid gap-2" style="display: flex!important; flex-direction: row;">
                                <button class="btn btn-primary mb-2 h-100" type="button"
                                    style="width: auto; height: 40px !important;" data-bs-toggle="modal"
                                    data-bs-target="#createRoleModal">Create Role</button>
                                <button class="btn btn-primary mb-2 h-100" type="button"
                                    style="width: auto;height: 40px !important;">Create Admin</button>
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
                                            placeholder="Enter role name...">
                                    </div>
                                </form>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <button type="button" class="btn btn-primary">Add</button>
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
                                <!-- Your form to edit details -->
                                <form>

                                    <!-- First Row -->
                                    <div class="row">
                                        <!-- Name Field -->
                                        <div class="col-md-6 mb-3">
                                            <label for="name" class="form-label">Name</label>
                                            <input type="text" class="form-control" id="name" name="name">
                                        </div>

                                        <!-- Email Field -->
                                        <div class="col-md-6 mb-3">
                                            <label for="email" class="form-label">Email</label>
                                            <input type="email" class="form-control" id="email" name="email">
                                        </div>
                                    </div>

                                    <!-- Second Row -->
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="Role" class="form-label">Role</label>
                                            <select class="form-select" id="role" name="role">
                                                <option value="select">Select...</option>
                                                <option value="option1">Option 1</option>

                                            </select>
                                        </div>

                                        <!-- Contact Number Field -->
                                        <div class="col-md-6 mb-3">
                                            <label for="contactNo" class="form-label">Contact Number</label>
                                            <input type="tel" class="form-control" id="contactNo" name="contactNo">
                                        </div>
                                    </div>
                                    <!-- Second Row -->
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="Pincode" class="form-label">Pincode</label>
                                            <input type="text" class="form-control" id="pincode" name="pincode">
                                        </div>

                                        <!-- Contact Number Field -->
                                        <div class="col-md-6 mb-3">
                                            <label for="Designation" class="form-label">Designation</label>
                                            <input type="text" class="form-control" id="designation" name="designation">
                                        </div>
                                    </div>
                                    <!-- Continue adding rows as needed -->

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
                            <tbody v-for="(user, index) in users" :key="index">
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
                                        <!-- <a href="" class="text-secondary font-weight-bold text-xs"
                                                data-toggle="tooltip" data-original-title="Edit user" @click="showModal = true">Edit
                                            </a> -->


                                        <!-- <a href="" class="text-secondary font-weight-bold text-xs"
                                                data-bs-toggle="modal" data-bs-target="#createRoleModal" style="color: dodgerblue !important">Edit
                                            </a> -->
                                        <i class="fas fa-pencil-alt text-primary fa-xs pr-4" data-bs-toggle="modal"
                                            data-bs-target="#edituser"
                                            style="color: dodgerblue !important; margin-left: 20px"></i>

                                        <!-- <a href="javascript:;" class="text-secondary font-weight-bold text-xs p-2"
                                                @click="confirmDelete" data-toggle="tooltip"
                                                data-original-title="Delete user" style="color: red !important;">
                                                Delete
                                            </a> -->
                                        <i class="fas fa-trash text-danger m-3 fa-xs " @click="confirmDelete"
                                            data-toggle="tooltip" data-original-title="Delete user"></i>
                                    </td>

                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            <!-- Page end  -->
        </div>

    </div>
    <!-- </div>
                </div>
            </div>
        </div>
    </div> -->
</template>

<script>
import axios from 'axios'
import Noty from 'noty'
import { mapState } from 'vuex'
import Swal from 'sweetalert2';
// import { timestamp } from 'public/assets/vendor/tui-calendar/tui-code-snippet/src/js/tricks';
export default {
    data() {
        return {
            // showModal: false,
            searchTerm: '',
            name: '', email: '', role: '', contact_no: '', designation: '', pincode: '', password: '',
            isToggled: false,
            isAreaModal: false,
            displayToggle: 'none',
            users: [],
            headers: ['Profile', 'Name', 'Designation', 'Department', 'Contact No.', 'Pincode', 'Actions']
        }
    },
    computed: {
        ...mapState(['authUser']),
        filteredUsers() {
            return this.users.filter(user => {
                const searchLowerCase = this.searchTerm.toLowerCase();
                return (
                    user.name.toLowerCase().includes(searchLowerCase) ||
                    user.role.toLowerCase().includes(searchLowerCase) ||
                    user.designation.toLowerCase().includes(searchLowerCase)
                );
            });
        }
    },
    methods: {
        confirmDelete() {
            Swal.fire({
                title: 'Are you sure?',
                text: 'You won\'t be able to revert this!',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#d33',
                cancelButtonColor: '#3085d6',
                confirmButtonText: 'Yes, delete it!'
            }).then((result) => {
                if (result.isConfirmed) {
                    // Perform your delete action here
                    // You can use axios or any other method to send a request to delete the user.
                    Swal.fire('Deleted!', 'The user has been deleted.', 'success');
                }
            });

        },
        openModal() {
            this.displayToggle = 'block';
            this.isToggled = !this.isToggled;
        },
        createUser() {
            const requestData = {
                email: this.email,
                name: this.name,
                role: this.role,
                contact_no: this.contact_no,
                designation: this.designation,
                pincode: this.pincode,
                password: this.password
            }
            axios.post('http://127.0.0.1:8000/api/create/user/', requestData).then((r) => {
                // console.log(r.status)
                if (r.status == 201) {
                    new Noty({
                        type: 'success',
                        text: 'user Created Successfully',
                        timeout: 500,
                    }).show()
                }
                this.getUsers
                this.closeModal
            })
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
        }
    },

    watch: {
        '$route.params.val': 'getUsers'
    },
    created() {
        this.getUsers(this.$route.params.val)
    }

}
</script>