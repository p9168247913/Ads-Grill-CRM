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
                        <div class="col-md-6 col-lg-3 col-sm-6 mb-3">
                                <select v-model="searchColor" name="" id="" class="form-select">
                                    <option value="" selected>Find by color</option>
                                    <option :value="color" v-for="(color) in colors" :key="color" :style="{ backgroundColor: `#${color.split(':')[0]}` }">{{`#${color}` }}</option>
                                </select>
                        </div>
                    </div>
                </div>

                <!-- Modal for Edit Lead -->
                <div data-bs-backdrop="static" class="modal fade" ref="editLeadModal" id="edituser" tabindex="-1"
                    @hidden="updateLead" aria-labelledby="edituser" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px;">
                            <div class="modal-header">
                                <h5 class="modal-title" id="editdetails">Edit</h5>
                                <button ref="editModalBtn" type="button" class="btn-close bg-dark text-xs"
                                    data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body modalBody" style="padding-bottom: 0; height:20rem">
                                <form @submit="updateLead($event, updateLeadData.id), resetValues()">
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="follow_date" class="form-label">Follow-up date</label>
                                            <input type="datetime-local" class="form-control"
                                                v-model="updateLeadData.follow_date" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="status" class="form-label">Status</label>
                                            <input type="text" class="form-control" v-model="updateLeadData.status"
                                                required>
                                        </div>
                                    </div>

                                    <div class="row">
                                        <div class="col-md-12 mb-3">
                                            <label for="remark" class="form-label">Remark</label>
                                            <textarea class="form-control" v-model="updateLeadData.remark"
                                                required></textarea>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-12 mb-3">
                                            <label for="choose color" class="form-label">Choose color</label>
                                            <select v-model="updateLeadData.row_color" class="form-select" required>
                                                <option value="" selected>Choose a color</option>
                                                <option v-for="(color) in colors" :key="color" :value="color"
                                                    :style="{ backgroundColor: `#${color.split(':')[0]}` }">{{ `#${color}` }}</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="modal-footer"
                                        style="z-index: 999; margin-top: 15px; position: sticky; bottom: 0; background-color: white; margin-bottom: -500px;">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                                            @click="resetValues(), updateLeadData.row_color = ''">Close</button>
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
                        <h6>SALES</h6>
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
                            <button @click="assignSales" v-if="this.selectedSales.length > 0 && this.selectedAssignee"
                                type="button" style="width: auto; height: 40px !important;"
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
                                                v-model="selectAll" @change="selectAllSales">
                                        </th>
                                        <th style="color: #344767 !important;"
                                            class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold"
                                            v-for="(head) in headers" :key="head">{{ head }}</th>
                                    </tr>
                                </thead>
                                <tbody v-for="(lead, index) in leads" :key="index">
                                    <tr :style="{backgroundColor: `#${lead.row_color ? lead.row_color : ''}`}">
                                        <td style="padding-left: 24px;">
                                            <input :disabled="lead.is_assigned" style="width: 15px; height: 15px;"
                                                type="checkbox" v-model="selectedSales" :value="lead.id">
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ index + 1
                                                    }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.name }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.email }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.conact_no }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ lead.source.name }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
					        <h6 class="mb-0 text-sm">{{ lead.requirement }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 25px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">{{ formatDate(lead.created_at) }}</h6>
                                            </div>
                                        </td>
                                        <td class="align-middle" style="margin-left: 15px !important;">
                                            <div class="d-flex flex-row justify-content-center gap-4">
                                                <i v-if="!lead?.related_users" title="Create Contact"
                                                    @click="createContact(lead)" class="fas fa-user-plus mt-2"></i>
                                                <i v-if="lead?.related_users?.designation !== 'client'"
                                                    title="Create Client" @click="createClient(lead.related_users)"
                                                    class="fas fa-users mt-2"></i>
                                                <i @click="downloadReq(lead.temp_data)" v-if="lead.temp_data"
                                                    title="Download requirement" class="fas fa-download mt-2"></i>
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
import html2pdf from 'html2pdf.js'
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
            updateLeadData: {
                id: '',
                name: '',
                email: '',
                conact_no: '',
                source: '',
                follow_date: '',
                status: '',
                remark: '',
                row_color:''
            },
            contact_role: {
                id: '',
                name: ""
            },
            client_role: {
                id: '',
                name: ""
            },
            headers: ['S.No', 'Contact Name ', 'Email', 'Mobile No.', 'Source', 'Requirements', 'Date', 'QUOT & REQS', 'Actions'],
            modalOpen: false,
            currentPage: 1,
            itemsPerPage: 5,
            totalPages: null,
            totalLeads: null,
            selectAll: false,
            selectedSales: [],
            selectedAssignee: '',
            allAssignee: [],
            colors: ['00FF00:Onboarded', 'FFFF00:Follow Up', 'FFA500:Pending', 'FF0000:Decline'],
            searchColor: ''
        };
    },
    computed: {
        ...mapState(['authUser', 'authToken']),
    },
    methods: {
        parseDateTime(dateTimeString) {
            if (dateTimeString) {
                this.updateLeadData.follow_date = new Date(dateTimeString);
            }
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
        async getLeads() {
            let queryParams = {
                page_no: this.currentPage ? this.currentPage : 1,
            };
            if (this.clientNameFilter) {
                queryParams = { ...queryParams, name: this.clientNameFilter };
            }
            if (this.contactNoFilter) {
                queryParams = { ...queryParams, contact_no: this.contactNoFilter };
            }
            if(this.searchColor){
                this.searchColor = this.searchColor.split(":")[0]
                queryParams = { ...queryParams, searchColor: this.searchColor}
            }
            let date_range = {};

            if (this.start_date && this.end_date) {
                date_range = {
                    start_date: (this.start_date).toString(),
                    end_date: (this.end_date).toString(),
                }
            }
            try {
                const response = await axios.get(`${BASE_URL}api/sales/?page_no=${queryParams.page_no}&client_name=${queryParams.name ? queryParams.name : ""}&contact_no=${queryParams.contact_no ? queryParams.contact_no : ""}&date_range=${date_range.end_date ? JSON.stringify(date_range) : ''}&searchColor=${queryParams.searchColor?queryParams.searchColor:""}`, {
                    headers: {
                        token: this.authToken,
                    }
                })
                if (response.status === 200) {
                    this.totalLeads = response?.data?.data?.total_leads
                    this.totalPages = response?.data?.data?.total_pages
                    this.leads = []
                    this.leads = response?.data?.res_data
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show()
            }
        },
        editModal(lead) {
            console.log(lead, 'leadData')
            this.updateLeadData = { ...lead, id: +(lead.id), follow_date: lead?.follow_date, row_color:lead.row_color};
            console.log(this.updateLeadData, 'updatedLeaddata')
            this.isEditModalOpen = true;
        },
        async updateLead(e, id) {
            e.preventDefault()
            this.updateLeadData.id = id
            this.updateLeadData.follow_date = this.updateLeadData.follow_date.toString()
            this.updateLeadData.row_color = this.updateLeadData.row_color.split(":")[0]
            try {
                const response = await axios.put(`${BASE_URL}api/sales/`, this.updateLeadData, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                        token: this.authToken
                    },
                })
                this.resetValues()
                if (response.status === 200) {
                    this.updateLeadData.row_color = ''
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
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
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
                        const response = await axios.delete(`${BASE_URL}api/sales/?id=${id}`, {
                            headers: {
                                token: this.authToken
                            }
                        })
                        this.getLeads();
                        Swal.fire('Deleted!', response.data.message, 'success');
                    } catch (error) {
                        Swal.fire('Error', error.response.data.message ? error.response.data.message : error.response.data.detail, 'error');
                    }
                }
            });
        },
        async getUserRole() {
            try {
                this.$store.commit('showLoader')
                const response = await axios.get(`${BASE_URL}api/roles/`, {
                    headers: {
                        token: this.authToken
                    }
                });
                if (response.status === 200) {
                    this.userRole = response.data.roles;
                    let admin = this.userRole.find((item) => item.name === 'contact');
                    let clients = this.userRole.find((item) => item.name === 'client');

                    this.contact_role = {
                        id: admin.id,
                        name: admin.name
                    };

                    this.client_role = {
                        id: clients.id,
                        name: clients.name
                    };
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
        generatePassword(length = 12) {
            const charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,./<>?';
            let password = '';
            for (let i = 0; i < length; i++) {
                const randomIndex = Math.floor(Math.random() * charset.length);
                password += charset[randomIndex];
            }
            return password;
        },
        async createContact(data) {
            Swal.fire({
                title: 'Are you sure?',
                text: 'You want to create contact for this lead!',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#d33',
                cancelButtonColor: '#3085d6',
                confirmButtonText: 'Yes, create!'
            }).then(async (result) => {
                if (result.isConfirmed) {
                    const requestData = {
                        name: data.name,
                        email: data.email,
                        password: this.generatePassword(),
                        contact_no: data.conact_no,
                        role: this.contact_role.id,
                        designation: this.contact_role.name
                    }
                    try {
                        const response = await axios.post(`${BASE_URL}api/create/user/`, requestData, {
                            headers: {
                                token: this.authToken,
                                'Content-Type': "multipart/form-data",
                            }
                        })
                        this.getLeads();
                        Swal.fire('Contact created!', response.data.message, 'success');
                    } catch (error) {
                        Swal.fire('Error', error.response.data.message ? error.response.data.message : error.response.data.detail, 'error');
                    }
                }
            });
        },
        async createClient(data) {
            Swal.fire({
                title: 'Are you sure?',
                text: 'You want to create client for this lead!',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#d33',
                cancelButtonColor: '#3085d6',
                confirmButtonText: 'Yes, create!'
            }).then(async (result) => {
                if (result.isConfirmed) {
                    const requestData = {
                        userID: data.id,
                        name: data.name,
                        email: data.email,
                        contact_no: data.contact_no,
                        role: this.client_role.id,
                        designation: this.client_role.name
                    }
                    try {
                        const response = await axios.put(`${BASE_URL}api/users/`, requestData, {
                            headers: { token: this.authToken },
                        },)
                        this.getLeads();
                        Swal.fire('Contact created!', response.data.message, 'success');
                    } catch (error) {
                        Swal.fire('Error', error.response.data.message ? error.response.data.message : error.response.data.detail, 'error');
                    }
                }
            });
        },
        downloadReq(data) {
            const parser = new DOMParser();
            let doc = parser.parseFromString(data, "text/html");

            let firstDiv = doc.querySelector('div')
            if (firstDiv) {
                firstDiv.style.display = 'flex';
            }

            var opt = {
                margin: 0.1,
                fileName: 'new.pdf',
                image: {
                    type: 'jpeg',
                    quality: 0.99
                },
                html2canvas: { scale: 2 },
                jsPDF: {
                    unit: 'in',
                    format: 'a4',
                    orientation: 'portrait'
                }
            };
            html2pdf().from(doc.body).set(opt).save();
        },
        selectAllSales() {
            if (this.selectAll) {
                this.selectedSales = this.leads.map(lead => lead.id);
            } else {
                this.selectedSales = [];
            }
            const checkboxes = document.querySelectorAll('input[type="checkbox"]');
            checkboxes.forEach(checkbox => {
                checkbox.checked = this.selectAll;
            });
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
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show()
            }
        },
        async assignSales(e) {
            e.preventDefault();
            let data = {}
            if (this.selectedSales.length > 0 && this.selectedAssignee) {
                data = {
                    salesIds: [...this.selectedSales],
                    saleAssignee: this.selectedAssignee
                }
            }
            try {
                const response = await axios.patch(`${BASE_URL}api/sales/`, data, {
                    headers: {
                        token: this.authToken
                    }
                })
                if (response.status === 200) {
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
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show()
            }
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
        searchColor(newValue, oldValue) {
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
        this.getLeads();
        this.getUserRole();
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
