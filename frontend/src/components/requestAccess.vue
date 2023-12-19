<!-- Home.vue -->
<template>
    <div class="wrapper">
        <div class="content-page">

            <div class="container-fluid" style="margin-top: 2rem;">
                <div class="col-md-2" data-bs-target="#createRoleModal">
                    <!-- <a href="javascript:;" class="btn btn-sm btn-dark float-right" data-bs-toggle="modal"
                        data-bs-target="#createRoleModal"  v-if="!issuperAdmin">Request Access</a> -->
                    <a href="javascript:;" class="btn btn-sm btn-dark float-right" data-bs-toggle="modal"
                        data-bs-target="#createRoleModal" v-if="authUser.role == 'admin'">Request Access</a>
                   
                </div>



                <!-- Modal for Create Role -->
                <div class="modal fade" id="createRoleModal" tabindex="-1" aria-labelledby="createRoleModalLabel"
                    aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createRoleModalLabel">Request Access</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <!-- Your form to create role -->
                                <form>
                                    <!-- Feature Request Select Box -->
                                    <div class="mb-3">
                                        <label for="featureRequest" class="form-label">Feature Request</label>
                                        <select class="form-select" id="featureRequest" name="featureRequest">
                                            <option value="select">Select...</option>
                                            <option value="option1">Option 1</option>

                                        </select>
                                    </div>


                                </form>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <button type="button" class="btn btn-primary">Send</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="card" style="margin-top: 2rem;">
                <!-- <h1>hello</h1> -->
                <div class="card-header pb-0">

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
                            <tbody>
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
                                            <h6 class="mb-0 text-sm">ww</h6>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="d-flex flex-column justify-content-center">
                                            <h6 class="mb-0 text-sm">ww</h6>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="d-flex flex-column justify-content-center">
                                            <h6 class="mb-0 text-sm">yy</h6>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="d-flex flex-column justify-content-center">
                                            <h6 class="mb-0 text-sm">jj</h6>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="d-flex flex-column justify-content-center">
                                            <h6 class="mb-0 text-sm">uiui</h6>
                                        </div>
                                    </td>
                                    <td class="align-middle" style="margin-left: 15px !important;">
                                        <i class="fas fa-trash text-danger m-3 fa-xs " data-toggle="tooltip"
                                            data-original-title="Delete user"></i>
                                    </td>

                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>
  
<script>
import { mapState } from 'vuex'
export default {
    data() {
        return {
            headers: ['Profile', 'Name', 'Designation', 'Department', 'Contact No.', 'Pincode', 'Actions'],
        };
    },
    computed: {
        ...mapState(['authUser']),
    },
    methods: {


    },
    // computed: {
    // issuperAdmin() {
    //   const role = localStorage.getItem('role');
    //   return role === 'super-admin';
    // },
    // }
}
</script>
  
<style>
/* Add your styles here */
</style>
  