<template>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Webkit | Responsive Bootstrap 4 Admin Dashboard Template</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
    </head>
    <div class="wrapper">
        <div class="content-page">
            <div class="container-fluid" style="margin-top: 7rem;">
                <div class="card">
                    <div class="card-header pb-0">
                        <h6>{{$route.params.val.toUpperCase() }}</h6>
                    </div>
                    <div class="card-body px-0 pt-0 pb-2">
                        <div class="table-responsive p-0">
                            <table class="table align-items-center mb-0">
                                <thead>
                                    <tr>
                                        <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 font-weight-bold"
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
                                        <td class="align-middle">
                                            <a href="javascript:;" class="text-secondary font-weight-bold text-xs"
                                                data-toggle="tooltip" data-original-title="Edit user">Edit</a>
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
            name: '', email: '', role: '3', contact_no: '', designation: 'Full stack developer', pincode: '', password: '',
            isToggled: false,
            isAreaModal: false,
            displayToggle: 'none',
            users: [],
            headers: ['Profile', 'Name', 'Designation', 'Department', 'Contact No.', 'Pincode', 'Actions']
        }
    },
    computed: {
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
                name: this.name,
                role: this.role,
                contact_no: this.contact_no,
                designation: this.designation,
                pincode: this.pincode,
                password: this.password
            }
            axios.post('http://127.0.0.1:8000/api/create/user/', requestData).then((r) => {
                console.log(r.status)
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