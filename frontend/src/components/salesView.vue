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
                            <div class="modal-body modalBody" style="padding-bottom: 0; height:38vh">
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
                        <h6>SALES</h6>
                        <div class="col-md-4 col-lg-5 col-sm-6 mb-3 d-flex">
                            <input class="form-control" v-model="start_date" type="date" placeholder="Start date" />
                            <span class="mt-2">&nbsp;to&nbsp;</span>
                            <input class="form-control" v-model="end_date" :min="start_date" :disabled="!start_date"
                                type="date" placeholder="End date" />
                        </div>
                    </div>
                    <div class="card-body px-0 pt-0">
                        <div class="table-responsive p-0">
                            <table class="table align-items-center mb-0">
                                <thead style="background-color: white; position: sticky; top: 0;">
                                    <tr>
                                        <th style="color: #344767 !important;"
                                            class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold"
                                            v-for="(head) in headers" :key="head">{{ head }}</th>
                                    </tr>
                                </thead>
                                <tbody v-for="(lead, index) in leads" :key="index">
                                    <tr>
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
                                                <h6 class="mb-0 text-sm">{{ formatDate(lead.created_at) }}</h6>
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
            updateLeadData: {
                id: '',
                name: '',
                email: '',
                conact_no: '',
                source: '',
                follow_date: '',
                status: '',
                remark: '',
            },
            headers: ['S.No', 'Contact Name ', 'Email', 'Mobile No.', 'Source', 'Date', 'Actions'],
            modalOpen: false,
            currentPage: 1,
            itemsPerPage: 5,
            totalPages: null,
            totalLeads: null,
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
            let date_range = {};

            if (this.start_date && this.end_date) {
                date_range = {
                    start_date: (this.start_date).toString(),
                    end_date: (this.end_date).toString(),
                }
            }
            try {
                const response = await axios.get(`${BASE_URL}api/sales/?page_no=${queryParams.page_no}&client_name=${queryParams.name ? queryParams.name : ""}&contact_no=${queryParams.contact_no ? queryParams.contact_no : ""}&date_range=${date_range.end_date ? JSON.stringify(date_range) : ''}`, {
                    headers: {
                        token: this.authToken,
                    }
                })
                if (response.status === 200) {
                    this.totalLeads = response?.data?.data?.total_leads
                    this.totalPages = response?.data?.data?.total_pages
                    this.leads = response?.data?.res_data
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message? error.response.data.message: error.response.data.detail,
                    timeout: 1000,
                }).show()
            }
        },
        editModal(lead) {
            this.updateLeadData = { ...lead, id: +(lead.id), follow_date: lead?.follow_date };
            this.isEditModalOpen = true;
        },
        async updateLead(e, id) {
            e.preventDefault()
            this.updateLeadData.id = id
            this.updateLeadData.follow_date = this.updateLeadData.follow_date.toString()
            try {
                const response = await axios.put(`${BASE_URL}api/sales/`, this.updateLeadData, {
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
                    text: error.response.data.message? error.response.data.message: error.response.data.detail,
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
                        Swal.fire('Error', error.response.data.message? error.response.data.message: error.response.data.detail, 'error');
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
        this.getLeads();
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