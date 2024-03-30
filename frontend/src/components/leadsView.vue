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
                        <div class="col-md-6 col-lg-3 col-sm-6 mb-3">
                            <div class="input-group">
                                <span class="input-group-text text-body">
                                    <i class="fas fa-search" aria-hidden="true"></i>
                                </span>
                                <input type="text" v-model="clientNameFilter" class="form-control"
                                    placeholder="Search by contact name..." />
                            </div>
                        </div>
                        <div class="col-md-6 col-lg-3 col-sm-6 mb-3">
                            <div class="input-group">
                                <span class="input-group-text text-body">
                                    <i class="fas fa-search" aria-hidden="true"></i>
                                </span>
                                <input type="text" v-model="contactNoFilter" class="form-control"
                                    placeholder="Search by contact number..." />
                            </div>
                        </div>
                        <div class="col-md-6 col-lg-6 col-sm-10 d-flex justify-content-lg-end justify-content-md-end">
                            <div class="d-grid gap-2" style="display: flex!important; flex-direction: row;">
                                <button type="button" style="width: auto; height: 40px !important;"
                                    class="btn btn-sm btn-dark mb-0 px-2 py-1 mb-0 nav-link active"
                                    data-bs-toggle="modal" data-bs-target="#createLead">
                                    <i class="fas fa-plus-circle text-success text-sm opacity-10"></i>
                                    <span class="d-none d-md-inline">&nbsp; &nbsp;Create Lead</span>
                                </button>
                                <a class="btn btn-sm btn-dark px-3 py-2 h-100" type="button"
                                    style="width: auto; height: 40px !important; padding: none !important; "
                                    href="http://127.0.0.1:8000/api/leadExcelFormat/" download>
                                    <i class="fas fa-download text-success text-sm opacity-10"></i>
                                    <span class="d-none d-md-inline">&nbsp;&nbsp;Lead Format</span>
                                </a>
                                <input @change="leadsBulkUpload" type="file" class="btn btn-sm btn-dark px-3 py-2 h-100"
                                    style="width: auto; height: 40px !important; display: none; " id="fileInput"
                                    accept=".xlsx, .xls">
                                <label for="fileInput" class="btn btn-sm btn-dark px-3 py-2 h-100"
                                    style="width: auto; height: 40px !important;">
                                    <i class="fas fa-upload text-success text-sm opacity-10"></i>
                                    <span class="d-none d-md-inline">&nbsp;&nbsp;Bulk Upload</span>
                                </label>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Modal for Create Lead -->
                <div data-bs-backdrop="static" class="modal fade" ref="createLeadModal" id="createLead" tabindex="-1"
                    aria-labelledby="createadminLabel" aria-hidden="true" @hidden="createLeads">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px;">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createadminLabel">Create Lead</h5>
                                <button ref="createLeadBtn" type="button" class="btn-close bg-dark text-xs"
                                    data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body modalBody" style="padding-bottom: 0; height:45vh">
                                <form @submit="createLeads($event)">
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="client_name" class="form-label">Name</label>
                                            <input type="text" class="form-control" v-model="leadData.client_name"
                                                required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="email" class="form-label">Email</label>
                                            <input type="email" class="form-control" v-model="leadData.email" required>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="contact_no" class="form-label">Mobile No.</label>
                                            <input type="text" class="form-control" v-model="leadData.contact_no"
                                                required>
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
                                        <div class="col-md-12 mb-3">
                                            <label for="email" class="form-label">Requirement</label>
                                            <textarea class="form-control" v-model="leadData.requirement"
                                                required></textarea>
                                        </div>
                                    </div>
                                    <div class="modal-footer"
                                        style="z-index: 999; margin-top: 15px; position: sticky; bottom: 0; background-color: white; margin-bottom: -500px;">
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
                <div data-bs-backdrop="static" class="modal fade" ref="editLeadModal" id="edituser" tabindex="-1"
                    @hidden="updateLead" aria-labelledby="edituser" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px;">
                            <div class="modal-header">
                                <h5 class="modal-title" id="editdetails">Edit Details</h5>
                                <button ref="editModalBtn" type="button" class="btn-close bg-dark text-xs"
                                    data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body modalBody" style="padding-bottom: 0; height:45vh">
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
                                        <div class="col-md-12 mb-3">
                                            <label for="email" class="form-label">Requirement</label>
                                            <textarea class="form-control" v-model="updateLeadData.requirement"
                                                required></textarea>
                                        </div>
                                    </div>
                                    <div class="modal-footer"
                                        style="z-index: 999; margin-top: 15px; position: sticky; bottom: 0; background-color: white; margin-bottom: -500px;">
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
                <div class="card" style="margin-top: 2rem; margin-bottom:4rem;">
                    <div class="card-header pb-0 heads" style="overflow: auto; gap:20px;">
                        <h6>LEADS</h6>
                        <div class="col-md-4 col-lg-5 col-sm-6 mb-3 d-flex">
                            <input class="form-control" v-model="start_date" type="date" placeholder="Start date" />
                            <span class="mt-2">&nbsp;to&nbsp;</span>
                            <input class="form-control" v-model="end_date" :min="start_date" :disabled="!start_date"
                                type="date" placeholder="End date" />
                        </div>
                        <div class="col-md-4 col-lg-3 col-sm-6 mb-3 d-flex gap-2">
                            <select v-model="selectedAssignee" class="form-select">
                                <option value="">Sales Assignee</option>
                                <option v-for="(item, index) in allAssignee" :key="index" :value="item.id"> {{
                                    item.name }}</option>
                            </select>
                            <button @click="assignLeads($event)"
                                v-if="this.selectedData.length > 0 && this.selectedAssignee" type="button"
                                style="width: auto; height: 40px !important;"
                                class="btn btn-sm btn-dark mb-0 px-2 py-1 mb-0 nav-link active ">
                                <i class="bi bi-person-plus"></i>
                                <span class="d-none d-md-inline">&nbsp; &nbsp;Assign</span>
                            </button>
                        </div>
                    </div>
                    <div class="card-body px-0 pt-0">
                        <div class="table-responsive p-0">
                            <table class="table align-items-center mb-0">
                                <thead style="background-color: white; position: sticky; top: 0;">
                                    <tr>
                                        <th style="color: #344767 !important;">
                                            <input style="width: 15px; height: 15px;" type="checkbox"
                                                v-model="selectAll" @change="selectAllRows">
                                        </th>
                                        <th style="color: #344767 !important;"
                                            class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold"
                                            v-for="(head) in headers" :key="head">{{ head }}</th>
                                    </tr>
                                </thead>
                                <tbody v-for="(lead, index) in leads" :key="index">
                                    <tr>
                                        <td style="padding-left: 24px;">
                                            <input :disabled="lead.is_assigned" style="width: 15px; height: 15px;"
                                                type="checkbox" v-model="selectedData" :value="lead.id"
                                                @change="updateSelectedData">
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ index + 1
                                                    }}</h6>
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
                                                <h6 class="mb-0 text-sm">{{ lead.source }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ formatDate(lead.date) }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.is_assigned ? "Assigned" : "Not Assigned"
                                                    }}</h6>
                                            </div>
                                        </td>
                                        <td class="align-middle" style="margin-left: 15px !important;">
                                            <i v-if="authUser.role === 'super-admin'"
                                                class="fas fa-pencil-alt text-primary fa-xs pr-4 "
                                                style=" cursor: not-allowed;"></i>
                                            <i v-else class="fas fa-pencil-alt text-primary mx-3 icon"
                                                data-bs-toggle="modal" data-bs-target="#edituser"
                                                @click="editModal(lead)" style=" cursor: pointer;"></i>
                                            <i v-if="authUser.role === 'super-admin'"
                                                class="fas fa-trash text-danger m-3 fa-xs"
                                                style="cursor: not-allowed"></i>
                                            <i v-else class="fas fa-trash text-danger mx-3 icon"
                                                @click="deleteLead(lead.id)" style="cursor: pointer"></i>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <PaginationComponent v-if="this.totalPages > 1" :currentPage="currentPage" :totalPages="totalPages"
                        :itemsPerPage="itemsPerPage" :prevPage="prevPage" :getLeads="getLeads" :nextPage="nextPage"
                        :goToPage="goToPage" />
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
            clientNameFilter: '',
            contactNoFilter: '',
            leads: [],
            leadData: {
                key: "post",
                client_name: '',
                email: '',
                contact_no: '',
                source: '',
            },
            updateLeadData: {
                id: '',
                client_name: '',
                email: '',
                contact_no: '',
                source: '',
            },
            headers: ['S.No', 'Contact Name ', 'Email', 'Mobile No.', 'Source', 'Date', 'Assigned', 'Actions'],
            modalOpen: false,
            currentPage: 1,
            itemsPerPage: 5,
            tags: [],
            sources: [],
            statuses: [],
            totalPages: null,
            totalLeads: null,
            selectedData: [],
            selectAll: false,
            allAssignee: [],
            selectedAssignee: '',
        };
    },
    computed: {
        ...mapState(['authUser', 'authToken']),
    },
    methods: {
        selectAllRows() {
            if (this.selectAll) {
                this.selectedData = this.leads.filter(lead => !lead.is_assigned).map(lead => lead.id);
            } else {
                this.selectedData = [];
            }
            const checkboxes = document.querySelectorAll('input[type="checkbox"]');
            checkboxes.forEach(checkbox => {
                checkbox.checked = this.selectAll;
            });
            console.log([...this.selectedData]);
        },
        updateSelectedData() {
            console.log([...this.selectedData]);
        },
        formatDate(inputDate) {
            const date = new Date(inputDate);
            const options = { day: 'numeric', month: 'long', year: 'numeric' };
            const formattedDate = date.toLocaleDateString('en-GB', options);
            return formattedDate;
        },
        nextPage() {
            this.currentPage++;
        },
        prevPage() {
            if (this.currentPage > 1) {
                this.currentPage--;
            }
        },
        goToPage(page) {
            this.currentPage = page;
        },
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
        async getSalesEmployee() {
            try {
                const response = await axios.get(`${BASE_URL}api/sales/getAllEmployees`, {
                    headers: {
                        token: this.authToken
                    }
                })
                if (response.status === 200) {
                    this.allAssignee = response.data.employee_data;
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.message,
                    timeout: 1000,
                }).show()
            }
        },
        async assignLeads(e) {
            e.preventDefault();
            let data = {}
            if (this.selectedData.length > 0 && this.selectedAssignee) {
                data = {
                    lead_ids: [...this.selectedData],
                    assignee_id: this.selectedAssignee
                }
            }
            try {
                const response = await axios.post(`${BASE_URL}api/sales/`, data, {
                    headers: {
                        token: this.authToken
                    }
                })
                if (response.status === 201) {
                    this.selectedData = [];
                    this.selectedAssignee = '';
                    this.getLeads();
                    Swal.fire({
                        title: `${response.data.message}`,
                        icon: 'success',
                    })
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.message,
                    timeout: 500,
                }).show()
            }
        },
        getQueryString(params) {
            return Object.keys(params)
                .filter((key) => params[key] !== undefined && params[key] !== "")
                .map((key) => `${key}=${encodeURIComponent(params[key])}`)
                .join("&");
        },
        async getLeads() {
            let queryParams = {
                page_no: this.currentPage ? this.currentPage : 1,
            };

            if (this.clientNameFilter) {
                queryParams = { ...queryParams, client_name: this.clientNameFilter };
            }
            if (this.contactNoFilter) {
                queryParams = { ...queryParams, contact_no: this.contactNoFilter };
            }
            let date_range = {};

            if (this.start_date && this.end_date) {
                date_range = {
                    start_date: (this.start_date).toString(),
                    end_date: (this.end_date).toString(),
                }
            }
            try {
                const response = await axios.get(`${BASE_URL}api/leads/?page_no=${queryParams.page_no}&client_name=${queryParams.client_name ? queryParams.client_name : ""}&contact_no=${queryParams.contact_no ? queryParams.contact_no : ""}&date_range=${date_range.end_date ? JSON.stringify(date_range) : ''}`, {
                    headers: {
                        token: this.authToken,
                    }
                })
                if (response.status === 200) {
                    this.totalLeads = response?.data?.lead_data?.total_leads
                    this.totalPages = response?.data?.lead_data?.total_pages
                    this.leads = response?.data?.lead_data?.leads
                }
                // console.log(this.leads);
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
                const response = await axios.post(`${BASE_URL}api/leads/`, this.leadData, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                        token: this.authToken
                    },
                }
                )
                if (response.status === 201) {
                    this.getLeads();
                    this.resetValues();
                    this.$refs.createLeadBtn.click()
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
                        token: this.authToken
                    },
                })
                this.resetValues()
                if (response.status === 200) {
                    this.getLeads();
                    this.$refs.editModalBtn.click()
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
                const response = await axios.get(`${BASE_URL}api/leadinfo/`, {
                    headers: {
                        token: this.authToken
                    }
                })
                this.tags = response?.data?.leadInfoData['leadTag']
                this.sources = response?.data?.leadInfoData['leadSource']
                this.statuses = response?.data?.leadInfoData['leadStatus']
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message,
                    timeout: 500,
                }).show()
            }
        },
        async leadsBulkUpload(event) {
            let file = event.target.files[0]
            if (!file) {
                new Noty({
                    type: 'error',
                    text: 'Please select a file',
                    timeout: 500
                }).show()
            }
            else {
                const formData = new FormData();
                formData.append('key', 'bulkUpload');
                formData.append('file', file);
                await axios.post(`${BASE_URL}api/leads/`, formData, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                        token: this.authToken
                    },
                }).then((r => {
                    if(r?.status ===200){
                        new Noty({
                        type: 'info',
                        text: r?.data?.database_res.message,
                        timeout: 3000
                    }).show()
                    }
                    if (r?.data.database_res?.status == 201) {
                        Swal.fire({
                            title: `${r.data.database_res.message}`,
                            icon: 'success',
                        })
                        this.getLeads()
                    }
                    if(r?.data?.excel_res){
                        new Noty({
                        type: 'info',
                        text: r?.data?.excel_res.message,
                        timeout: 3000
                    }).show()
                    }
                })).catch(e => {
                    new Noty({
                        type: 'error',
                        text: e,
                        timeout: 1000
                    }).show()
                })
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
                        const response = await axios.delete(`${BASE_URL}api/leads/?id=${id}`, {
                            headers: {
                                token: this.authToken
                            }
                        })
                        this.getLeads();
                        Swal.fire('Deleted!', response.data.message, 'success');
                    } catch (error) {
                        Swal.fire('Error', 'An error occurred while deleting the user.', 'error');
                    }
                }
            });
        },
    },
    watch: {
        clientNameFilter(newValue, oldValue) {
            if (newValue !== oldValue) {
                this.getLeads();
            }
        },
        contactNoFilter(newValue, oldValue) {
            if (newValue !== oldValue) {
                this.getLeads();
            }
        },
        start_date: {
            handler() {
                this.getLeads();
                this.end_date = '';
            }
        },
        end_date: {
            handler() {
                this.getLeads();
            }
        }
    },
    mounted() {
        this.getLeads()
        this.getLeadsInfo()
        this.getSalesEmployee()
    },
};
</script>

<style scoped>
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
    max-height: calc(100vh - 150px);
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