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
                                <input type="text" v-model="searchTerm" @change="filterLeads" class="form-control"
                                    placeholder="Search by name, role, designation or number..." />
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
                                            <label for="contact_no" class="form-label">Mobile No.</label>
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
                                                <option v-for="(tag, index) in tags" :key="index" :value="tag.name">{{
                                                    tag.name }}</option>
                                            </select>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="source" class="form-label">Source</label>
                                            <select class="form-select" v-model="leadData.source">
                                                <option value="">Select Source</option>
                                                <option v-for="(source, index) in sources" :key="index"
                                                    :value="source.name">
                                                    {{ source.name }}</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="status" class="form-label">Status</label>
                                            <select class="form-select" v-model="leadData.status" required>
                                                <option value="">Select Status</option>
                                                <option v-for="(status, index) in statuses" :key="index"
                                                    :value="status.name">{{ status.name }}</option>
                                            </select>
                                        </div>
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
                <div class="modal fade" ref="editLeadModal" id="edituser" tabindex="-1" @hidden="updateLead" aria-labelledby="edituser" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content" style="padding: 30px;">
                            <div class="modal-header">
                                <h5 class="modal-title" id="editdetails">Edit Details</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <form @submit="updateLead($event, updateLeadData.id), resetValues()">
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="client_name" class="form-label">Client Name</label>
                                            <input type="text" class="form-control" v-model="updateLeadData.client_name"
                                                required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="email" class="form-label">Email</label>
                                            <input type="email" class="form-control" v-model="updateLeadData.email"
                                                required>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="contact_no" class="form-label">Mobile No.</label>
                                            <input type="text" class="form-control" v-model="updateLeadData.contact_no"
                                                required>
                                        </div>

                                        <div class="col-md-6 mb-3">
                                            <label for="country" class="form-label">Country</label>
                                            <input type="text" class="form-control" v-model="updateLeadData.country"
                                                required>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="state" class="form-label">State</label>
                                            <input type="text" class="form-control" v-model="updateLeadData.state" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="city" class="form-label">City</label>
                                            <input type="text" class="form-control" v-model="updateLeadData.city">
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="tag" class="form-label">Tag</label>
                                            <select class="form-select" v-model="updateLeadData.tag" required>
                                                <option value="">Select Tag</option>
                                                <option v-for="(tag, index) in tags" :key="index" :value="tag.name">{{
                                                    tag.name }}</option>
                                            </select>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="source" class="form-label">Source</label>
                                            <select class="form-select" v-model="updateLeadData.source">
                                                <option value="">Select Source</option>
                                                <option v-for="(source, index) in sources" :key="index"
                                                    :value="source.name">
                                                    {{ source.name }}</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="status" class="form-label">Status</label>
                                            <select class="form-select" v-model="updateLeadData.status" required>
                                                <option value="">Select Status</option>
                                                <option v-for="(status, index) in statuses" :key="index"
                                                    :value="status.name">{{ status.name }}</option>
                                            </select>
                                        </div>
                                        <!-- <div class="col-md-6 mb-3">
                                            <label for="assignee" class="form-label">Assignee</label>
                                            <input type="text" class="form-control" v-model="leadData.userID" required>
                                        </div> -->
                                        <div class="col-md-6 mb-3">
                                            <label for="assignee" class="form-label">Assignee</label>
                                            <select class="form-select" v-model="updateLeadData.userID" required>
                                                <option value="">Select Assignee</option>
                                                <option value="9">9</option>
                                                <option value="10">10</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                                            @click="resetValues()">Close</button>
                                        <button type="submit" class="btn btn-primary">Save
                                            Changes</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                <!--Leads Table-->
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
                                <tbody v-for="(lead, index) in paginatedLeads" :key="index">
                                    <tr>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ index + 1 }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.client_name }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.email }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.contact_no }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.country }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.state }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.city }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.tag }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.source }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.status }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.user }}</h6>
                                            </div>
                                        </td>
                                        <td class="align-middle" style="margin-left: 15px !important;">
                                            <i v-if="authUser.role === 'super-admin'"
                                                class="fas fa-pencil-alt text-primary fa-xs pr-4 "
                                                style=" cursor: not-allowed;"></i>
                                            <i v-else class="fas fa-pencil-alt text-primary fa-xs pr-4 edit-icon"
                                                data-bs-toggle="modal" data-bs-target="#edituser" @click="editModal(lead)"
                                                style=" cursor: pointer;"></i>
                                            <i v-if="authUser.role === 'super-admin'" class="fas fa-trash text-danger m-3 fa-xs"
                                                style="cursor: not-allowed"></i>
                                            <i v-else class="fas fa-trash text-danger m-3 fa-xs delete-icon"
                                                @click="deleteLead(lead.id)" style="cursor: pointer"></i>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <PaginationComponent :currentPage="currentPage" :itemsPerPage="itemsPerPage"
                        :filteredUsers="filteredLeads" :prevPage="prevPage" :nextPage="nextPage" :goToPage="goToPage" />
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import axios from 'axios';
import Noty from 'noty'
import { mapState } from 'vuex'
import Swal from 'sweetalert2';
import PaginationComponent from './Paginator/PaginatorComponent.vue';
import { BASE_URL } from '../config/apiConfig';

export default {
    components: {
        PaginationComponent,
    },
    data() {
        return {
            searchTerm: '',
            leads: [],
            leadData: {
                key: "post",
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
            updateLeadData: {
                id: '',
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
            currentPage: 1,
            itemsPerPage: 10,
            tags: [],
            sources: [],
            statuses: [],
        };
    },
    computed: {
        ...mapState(['authUser']),
        filteredLeads() {
            return this.leads.filter(lead => {
                const searchLowerCase = this.searchTerm.toLowerCase() || ''
                return (
                    lead.client_name.toLowerCase().includes(searchLowerCase) ||
                    lead.email.toLowerCase().includes(searchLowerCase) ||
                    lead.contact_no.toLowerCase().includes(searchLowerCase) ||
                    lead.country.toLowerCase().includes(searchLowerCase) ||
                    lead.state.toLowerCase().includes(searchLowerCase) ||
                    lead.city.toLowerCase().includes(searchLowerCase)
                );
            });
        },
        paginatedLeads() {
            const startIndex = (this.currentPage - 1) * this.itemsPerPage;
            return this.filteredLeads.slice(startIndex, startIndex + this.itemsPerPage);
        }
    },
    methods: {
        nextPage() {
            if (this.currentPage * this.itemsPerPage < this.filteredLeads.length) {
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
            this.displayedLaads = this.filteredLeads.slice(startIndex, endIndex);
        },
        filterUsers() { },
        resetValues() {
            this.leadData = {
                client_name: '',
                email: '',
                contact_no: '',
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
                const response = await axios.get(`${BASE_URL}api/leads/`)
                this.leads = response.data.leads
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
                const response = await axios.post(`${BASE_URL}api/leads/`, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                    },
                }
                )
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
                    text: error.response.data.message,
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
        },
        editModal(lead) {
            this.updateLeadData = { ...lead };
            this.isEditModalOpen = true;
        },
        async updateLead(e, id) {
            e.preventDefault()
            this.updateLeadData.id = id
            try {
                const response = await axios.put(`${BASE_URL}api/leads/`, this.updateLeadData, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                    },
                })
                this.resetValues()
                if(response.status===200){
                    this.getLeads();
                    this.resetValues();
                    this.$refs.editLeadModal.classList.remove('show');
                    this.$refs.editLeadModal.setAttribute('aria-hidden', 'true');
                    this.$refs.editLeadModal.style.display = 'none';
                    this.removeModalBackdrop();
                    Swal.fire({
                        title: `${response.data.message}`,
                        icon: 'success',
                    })
                }
                this.getLeads()
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message,
                    timeout: 500,
                }).show()
            }
        },
        async getLeadsInfo() {
            try {
                const response = await axios.get(`${BASE_URL}api/leadinfo/`)
                this.tags = response.data.leadInfoData['leadTag']
                this.sources = response.data.leadInfoData['leadSource']
                this.statuses = response.data.leadInfoData['leadStatus']
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message,
                    timeout: 500,
                }).show()
            }
        },
        async deleteLead(id) {
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
                        const response = await axios.delete(`${BASE_URL}api/leads/?id=${id}`)
                        this.getLeads();
                        Swal.fire('Deleted!', response.data.message, 'success');
                    } catch (error) {
                        Swal.fire('Error', 'An error occurred while deleting the user.', 'error');
                    }
                }
            });
        },
    },
    mounted() {
        this.getLeads()
        this.getLeadsInfo()
    },
};
</script>
    
<style>
.modalBody {
    max-height: calc(100vh - 310px);
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