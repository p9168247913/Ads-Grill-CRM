<template>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Webkit | Responsive Bootstrap 4 Admin Dashboard Template</title>

        <!-- Favicon -->
        <link rel="shortcut icon" href="./assets/images/favicon.ico" />
        <link rel="stylesheet" href="./assets/css/backend-plugin.min.css">
        <link rel="stylesheet" href="./assets/css/backend.css?v=1.0.0">
        <link rel="stylesheet" href="./assets/vendor/line-awesome/dist/line-awesome/css/line-awesome.min.css">
        <link rel="stylesheet" href="./assets/vendor/remixicon/fonts/remixicon.css">

        <link rel="stylesheet" href="./assets/vendor/tui-calendar/tui-calendar/dist/tui-calendar.css">
        <link rel="stylesheet" href="./assets/vendor/tui-calendar/tui-date-picker/dist/tui-date-picker.css">
        <link rel="stylesheet" href="./assets/vendor/tui-calendar/tui-time-picker/dist/tui-time-picker.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
    </head>
    <div class="wrapper">
        <div class="content-page">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-lg-12">
                        <div class="card">
                            <div class="card-body">
                                <div class="d-flex flex-wrap align-items-center justify-content-between breadcrumb-content">
                                    <h5>Employees</h5>
                                    <div class="d-flex align-items-center">
                                        <div class="list-grid-toggle d-flex align-items-center mr-3">
                                            <div data-toggle-extra="tab" data-target-extra="#list" class="active">
                                                <!-- <div class="grid-icon">
                                            <svg  width="20" height="20" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                                <line x1="21" y1="10" x2="3" y2="10"></line><line x1="21" y1="6" x2="3" y2="6"></line><line x1="21" y1="14" x2="3" y2="14"></line><line x1="21" y1="18" x2="3" y2="18"></line>
                                            </svg>
                                        </div> -->
                                            </div>
                                        </div>
                                        <div class="pl-3 border-left btn-new">
                                            <a href="#" class="btn btn-primary" data-target="#new-user-modal"
                                                data-toggle="modal">Create Role</a>
                                        </div>
                                        <div class="pl-3 btn-new">
                                            <a href="#" class="btn btn-primary" data-target="#new-user-modal"
                                                data-toggle="modal" @click="openModal">Create User</a>
                                        </div>
                                    </div>


                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="modal fade bd-example-modal-lg" :class="{ 'show': isToggled }" role="dialog" aria-modal="true"
                    id="new-user-modal" :style="{ 'display': displayToggle }">
                    <div class="modal-dialog  modal-dialog-centered modal-lg" role="document">
                        <div class="modal-content">
                            <div class="modal-header d-block text-center pb-3 border-bttom">
                                <h3 class="modal-title" id="exampleModalCenterTitle02">New User</h3>
                            </div>
                            <div class="modal-body">
                                <div class="row">
                                    <div class="col-lg-6">
                                        <div class="form-group mb-3 custom-file-small">
                                            <label for="exampleInputText01" class="h5">Upload Profile Picture</label>
                                            <div class="custom-file">
                                                <input type="file" class="custom-file-input" id="inputGroupFile02">
                                                <label class="custom-file-label" for="inputGroupFile02">Choose file</label>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-lg-6">
                                        <div class="form-group mb-3">
                                            <label for="exampleInputText2" class="h5">Full Name</label>
                                            <input v-model="name" type="text" class="form-control" id="exampleInputText2"
                                                placeholder="Enter your full name">
                                        </div>
                                    </div>
                                    <div class="col-lg-6">
                                        <div class="form-group mb-3">
                                            <label for="exampleInputText04" class="h5">Phone Number</label>
                                            <input v-model="contact_no" type="text" class="form-control" id="exampleInputText04"
                                                placeholder="Enter phone number">
                                        </div>
                                    </div>
                                    <div class="col-lg-6">
                                        <div class="form-group mb-3">
                                            <label for="exampleInputText006" class="h5">Email</label>
                                            <input v-model="email" type="text" class="form-control" id="exampleInputText006"
                                                placeholder="Enter your Email">
                                        </div>
                                    </div>
                                    <div class="col-lg-6">
                                        <div class="form-group mb-3">
                                            <label for="exampleInputText2" class="h5">Designation</label>
                                            <select name="type" class="form-control" data-style="py-0">
                                                <option>Type</option>
                                                <option>Trainee</option>
                                                <option>Employee</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="col-lg-6">
                                        <div class="form-group mb-3">
                                            <label for="exampleInputText2" class="h5">Role</label>
                                            <select name="type" class="form-control" data-style="py-0">
                                                <option>Role</option>
                                                <option>Designer</option>
                                                <option>Developer</option>
                                                <option>Manager</option>
                                                <option>BDE</option>
                                                <option>SEO</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="col-lg-6">
                                        <div class="form-group mb-3">
                                            <label for="exampleInputText006" class="h5">Pincode</label>
                                            <input v-model="pincode" type="text" class="form-control" id="exampleInputText006"
                                                placeholder="Enter your Pincode">
                                        </div>
                                    </div>
                                    <div class="col-lg-6">
                                        <div class="form-group mb-3">
                                            <label for="exampleInputText006" class="h5">Password</label>
                                            <input v-model="password" type="text" class="form-control" id="exampleInputText006"
                                                placeholder="Enter your Password">
                                        </div>
                                    </div>
                                    <div class="col-lg-12">
                                        <div class="d-flex flex-wrap align-items-ceter justify-content-center mt-2">
                                            <div @click="createUser" class="btn btn-primary mr-3" data-dismiss="modal">Save
                                            </div>
                                            <div class="btn btn-primary" data-dismiss="modal" @click="closeModal">Cancel
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div id="list" class="item-content animate__animated animate__fadeIn active"
                    data-toggle-extra="tab-content">
                    <div class="table-responsive rounded bg-white mb-4">
                        <table class="table mb-0 table-borderless tbl-server-info">
                            <thead>
                                <tr>
                                    <td v-for="(head) in headers" :key="head" class="font-weight-bold">{{ head }}</td>
                                </tr>
                            </thead>
                            <tbody v-for="(user, index) in users" :key="index">
                                <tr>
                                    <td>
                                        <div class="media align-items-center">
                                            <img src="" class="img-fluid rounded-circle avatar-40" alt="image">
                                        </div>
                                    </td>
                                    <td>
                                        {{ user.name }}
                                    </td>
                                    <td>{{ user.designation }}</td>
                                    <td>{{ user.role }}</td>
                                    <td>{{ user.contact_no }}</td>
                                    <td>{{ user.pincode }}</td>
                                    <td>
                                        <div class="d-flex align-items-center">
                                            <a href="#" class="text-body"><i class="las la-pen mr-3"></i></a>
                                            <a href="#" class="text-body"><i class="las la-trash-alt mr-0"></i></a>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <!-- Page end  -->
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import Noty from 'noty'
import { mapState } from 'vuex'
// import { timestamp } from 'public/assets/vendor/tui-calendar/tui-code-snippet/src/js/tricks';
export default {
    data() {
        return {
            name:'', email:'',role:'3', contact_no:'', designation:'Full stack developer', pincode:'', password:'',
            isToggled: false,
            isAreaModal: false,
            displayToggle: 'none',
            users: [],
            headers: ['Profile', 'Name', 'Designation', 'Department', 'Contact No.', 'Pincode', 'Actions']
        }
    },
    computed:{
        ...mapState(['authUser'])
    },
    methods: {
        openModal() {
            this.displayToggle = 'block';
            this.isToggled = !this.isToggled;
        },
        createUser() {
            const requestData = {
                email: this.email,
                name:this.name,
                role:this.role,
                contact_no:this.contact_no,
                designation: this.designation,
                pincode: this.pincode,
                password:this.password
            }
            axios.post('http://127.0.0.1:8000/api/create/user/',requestData).then((r)=>{
                console.log(r.status)
                if(r.status == 201){
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
            console.log(role)
            axios.get('http://127.0.0.1:8000/api/users/', {
                params: { role: role }
            }).then((r) => {
                this.users = r.data.users
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