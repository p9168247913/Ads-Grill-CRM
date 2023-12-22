<!-- Home.vue -->
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
            <div class="container-fluid">
                <div style="margin-top: 20px;">
                    <div class="row">
                        <div class="col-md-6 col-lg-6 col-sm-12 mb-3">
                            <div class="input-group">
                                <span class="input-group-text text-body">
                                    <i class="fas fa-search" aria-hidden="true"></i>
                                </span>
                                <input type="text" class="form-control" placeholder="Type here..." />
                            </div>
                        </div>
                        <div class="col-md-6 col-lg-6 col-sm-12 d-flex justify-content-lg-end justify-content-md-end">
                            <div class="d-grid gap-2" style="display: flex!important; flex-direction: row;">
                                <button class="btn btn-primary mb-2 h-100" type="button"
                                    style="width: auto; height: 40px !important;" data-bs-toggle="modal"
                                    data-bs-target="#createLead">Create Lead</button>
                                <a class="btn btn-primary mb-2 h-100" type="button"
                                    style="width: auto; height: 40px !important;"
                                    href="http://127.0.0.1:8000/api/leadExcelFormat/" download><i
                                        class="fas fa-download"></i>&nbsp;&nbsp;Lead Format</a>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Modal for Create Lead -->
                <div class="modal fade" ref="createLeadModal" id="createLead" tabindex="-1"
                    aria-labelledby="createadminLabel" aria-hidden="true" @hidden="createLeads">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createadminLabel">Create Lead</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body modalBody">
                                <form @submit="createLeads($event), resetValues()">
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="client_name" class="form-label">Client Name</label>
                                            <input type="text" class="form-control" v-model="leadData.client_name" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="email" class="form-label">Email</label>
                                            <input type="email" class="form-control" v-model="leadData.email" required>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="mobile_no" class="form-label">Mobile No.</label>
                                            <input type="text" class="form-control" v-model="leadData.contact_no" required>
                                        </div>

                                        <div class="col-md-6 mb-3">
                                            <label for="country" class="form-label">Country</label>
                                            <input type="text" class="form-control" v-model="leadData.country" required>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="state" class="form-label">State</label>
                                            <input type="text" class="form-control" v-model="leadData.state" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="city" class="form-label">City</label>
                                            <input type="text" class="form-control" v-model="leadData.city">
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="tag" class="form-label">Tag</label>
                                            <select class="form-select" v-model="leadData.tag" required>
                                                <option value="">Select Tag</option>
                                                <option value="CRM">CRM</option>
                                                <option value="CMS">CMS</option>
                                            </select>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="source" class="form-label">Source</label>
                                            <select class="form-select" v-model="leadData.source">
                                                <option value="">Select Source</option>
                                                <option value="Facebook">Facebook</option>
                                                <option value="Instagram">Instagram</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="status" class="form-label">Status</label>
                                            <select class="form-select" v-model="leadData.status" required>
                                                <option value="">Select Status</option>
                                                <option value="Pending">Pending</option>
                                                <option value="Onboard">Onboard</option>
                                            </select>
                                        </div>
                                        <!-- <div class="col-md-6 mb-3">
                                            <label for="assignee" class="form-label">Assignee</label>
                                            <input type="text" class="form-control" v-model="leadData.userID" required>
                                        </div> -->
                                        <div class="col-md-6 mb-3">
                                            <label for="assignee" class="form-label">Assignee</label>
                                            <select class="form-select" v-model="leadData.userID" required>
                                                <option value="">Select Assignee</option>
                                                <option value="9">9</option>
                                                <option value="10">10</option>
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
                <!-- Modal for Edit Lead -->
                <!-- <div class="modal fade" id="edituser" tabindex="-1" aria-labelledby="edituser" aria-hidden="true">
                    
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
                </div> -->
                <div class="card" style="margin-top: 2rem;">
                    <div class="card-header pb-0">
                        <h6>LEADS</h6>
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
                                <tbody v-for="(lead, index) in leads" :key="index">
                                    <tr>
                                        <td>
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ index + 1 }}</h6>
                                            </div>
                                        </td>
                                        <td>
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.client_name }}</h6>
                                            </div>
                                        </td>
                                        <td>
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.email }}</h6>
                                            </div>
                                        </td>
                                        <td>
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.contact_no }}</h6>
                                            </div>
                                        </td>
                                        <td>
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.country }}</h6>
                                            </div>
                                        </td>
                                        <td>
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.state }}</h6>
                                            </div>
                                        </td>
                                        <td>
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.city }}</h6>
                                            </div>
                                        </td>
                                        <td>
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.tag }}</h6>
                                            </div>
                                        </td>
                                        <td>
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.source }}</h6>
                                            </div>
                                        </td>
                                        <td>
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.status }}</h6>
                                            </div>
                                        </td>
                                        <td>
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.user }}</h6>
                                            </div>
                                        </td>
                                        <td class="align-middle" style="margin-left: 15px !important;">
                                            <i class="fas fa-pencil-alt text-primary fa-xs pr-4"
                                                style="color: dodgerblue !important; margin-left: 20px; cursor: pointer;"></i>
                                            <i class="fas fa-trash text-danger m-3 fa-xs" style="cursor: pointer"></i>
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
</template>
    
<script>
import axios from 'axios';
import Noty from 'noty'
import Swal from 'sweetalert2';

export default {
    data() {
        return {
            leads: [],
            leadData: {
                client_name: '',
                email: '',
                contact_no: '',
                country: '',
                state: '',
                city: '',
                tag: '',
                source: '',
                status: '',
                userID: ''
            },
            headers: ['S.No', 'Client Name ', 'Email', 'Mobile No.', 'Country', 'State', 'City', 'Tag', 'Source', 'Status', 'Assignee', 'Actions'],
            modalOpen: false,
        };
    },
    methods: {
        resetValues() {
            this.leadData = {
                client_name: '',
                email: '',
                mobile_no: '',
                country: '',
                state: '',
                city: '',
                tag: '',
                source: '',
                status: '',
                assignee: ''
            }
        },
        async getLeads() {
            try {
                const response = await axios.get("http://127.0.0.1:8000/api/leads/")
                this.leads = response.data.leads
                console.log(this.leads);
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error,
                    timeout: 500,
                }).show()
            }
        },
        async createLeads(e) {
            e.preventDefault();
            try {
                const response = await axios.post(`http://127.0.0.1:8000/api/leads/`, this.leadData, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                    },
                }
                )
                console.log(response.data);
                if (response.status === 201) {
                    this.getLeads();
                    this.resetValues();
                    this.$refs.createLeadModal.classList.remove('show');
                    this.$refs.createLeadModal.setAttribute('aria-hidden', 'true');
                    this.$refs.createLeadModal.style.display = 'none';
                    this.removeModalBackdrop();
                    Swal.fire({
                        title: `${response.data.message}`,
                        icon: 'success',
                    })
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error,
                    timeout: 500,
                }).show()
            }
        },
        removeModalBackdrop() {
            const modalBackdrop = document.getElementsByClassName('modal-backdrop');
            if (modalBackdrop.length > 0) {
                document.body.classList.remove('modal-open');
                document.body.removeChild(modalBackdrop[0]);
            }
        }
    },
    mounted() {
        this.getLeads()
    },
};
</script>
    
<style>
/* Add your styles here */
.modalBody {
    max-height: calc(100vh - 310px);
    overflow-y: auto;
}
</style>