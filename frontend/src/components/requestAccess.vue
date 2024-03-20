
<template>
    <div class="wrapper">
        <div class="content-page">

            <div class="container-fluid" style="margin-top: 2rem;">
                <div class="col-md-2" data-bs-target="#createRoleModal">
                    
                    <a href="javascript:;" class="btn btn-sm btn-dark float-right" data-bs-toggle="modal"
                        data-bs-target="#createRoleModal" v-if="authUser.role == 'admin'">Request Access</a>
                   
                </div>



                <!-- Modal for request access -->
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
                                            <option value="select" disabled selected>Select...</option>
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
                                            data-original-title="Delete user"  @click="deleteUser"></i>
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
import Swal from 'sweetalert2';
import axios from 'axios'
// import Noty from 'noty'
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
                        const response = await axios.delete('http://127.0.0.1:8000/api/users/', {
                            params: {
                                userID: ''
                            }
                        });
                        if(response.status === 204){
                            Swal.fire('Deleted!', 'The user has been deleted.', 'success');
                        }
                    } catch (error) {
                        Swal.fire('Error', error.response.data.message ? error.response.data.message : error.response.data.detail, 'error');
                    }
                }
            });
        },
    },
}
</script>
  
<style>
/* Add your styles here */
</style>
  