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

                            <select class="form-select text-muted">
                                <option value="Search by status">Search by status</option>
                                <option v-for="status in quoteStatus" :key="status" :value="status.name">{{ status.name
                                    }}
                                </option>
                            </select>

                        </div>
                        <div class="col-md-6 col-lg-3 col-sm-10">
                            <div class="d-grid gap-2" style="display: flex!important; flex-direction: row;">
                                <button type="button"
                                    style=" display:flex; width:5px;height:40px !important; outline: none; justify-content: center; align-items: center;"
                                    class="btn btn-sm btn-dark nav-link"><i
                                        class="fas fa-search text-success text-sm opacity-10"></i><span
                                        class="d-none d-md-inline">&nbsp;
                                        &nbsp;</span></button>
                                <button type="button"
                                    style=" display:flex; width:5px;height:40px !important; outline: none; justify-content: center; align-items: center;"
                                    class="btn btn-sm btn-dark nav-link"><i
                                        class="fas fa-trash text-success text-sm opacity-10"></i><span
                                        class="d-none d-md-inline">&nbsp;
                                        &nbsp;</span></button>

                                <button ref="newProposalModal" type="button"
                                    style=" display:flex; width:7em;height:40px !important; outline: none; justify-content: center; align-items: center;"
                                    class="btn btn-sm btn-dark" data-bs-toggle="modal" data-bs-target="#createProposal"
                                    data-v-0a3051fc=""><i class="fas fa-plus-circle text-success text-sm opacity-10"
                                        data-v-0a3051fc="" aria-hidden="true"></i><span class="d-none d-md-inline"
                                        data-v-0a3051fc="">&nbsp;
                                        &nbsp;</span>Create</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>


    <div data-bs-backdrop="static" class="modal fade" ref="addStatus" id="addStatusModal" tabindex="-1"
        aria-labelledby="createadminLabel" aria-hidden="true">
        <div style="width:auto" class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px; width:auto">
                <div class="modal-header">
                    <h5 class="modal-title" id="createadminLabel">Add New Status</h5>
                    <button @click="resetValues" type="button" class="btn-close bg-dark text-xs"
                        data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body modalBody" style="padding-bottom: 0; height:10rem; width: 26rem;">
                    <form @submit="addStatus($event)">
                        <div class="row">
                            <div class="col-md-12 col-lg-12">
                                <label class="form-label" for="statusInput">Enter Status</label>
                                <input id="statusInput" type="text" class="form-control" v-model="newStatus" required>
                            </div>
                        </div>

                        <div class="mt-3" style="z-index: 999; position: sticky; bottom: 0; background-color: white">
                            <button style="margin-right: 5px;" type="button" class="btn btn-secondary btn-xs"
                                data-bs-dismiss="modal" @click="resetValues">Close</button>
                            <button type="submit" class="btn btn-primary btn-xs">Create</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <!-- MODAL FOR CREATE PROPOSAL -->
    <div style="margin-left:-100px;" data-bs-backdrop="static" class="modal fade" ref="createProposalModal"
        id="createProposal" tabindex="-1" aria-labelledby="createadminLabel" aria-hidden="true">
        <div style="width:auto" class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px; width:auto">
                <div class="modal-header">
                    <h5 class="modal-title" id="createadminLabel">New Proposal</h5>
                    <button ref="createProposalBtn" type="button" class="btn-close bg-dark text-xs"
                        data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body modalBody" style="padding-bottom: 0; height:35rem; width: 890px;">
                    <form @submit="createProposal($event)">
                        <div class="row">
                            <div class="col-md-4 mb-3">
                                <label for="Client" class="form-label">Client</label>
                                <select class="form-select" v-model="selectedClientID">
                                    <option value="">Select Client</option>
                                    <option v-for="client in allSales" :key="client" :value="client.id">{{ client.name
                                        }}</option>
                                </select>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="email" class="form-label">Email</label>
                                <div v-if="selectedClient">
                                    <input disabled type="email" class="form-control" :value="selectedClient.email"
                                        required>
                                </div>
                                <div v-else>
                                    <input type="email" class="form-control" value="" required>
                                </div>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="contact_no" class="form-label">Mobile No.</label>
                                <div v-if="selectedClient">
                                    <input disabled type="text" class="form-control" :value="selectedClient.contact_no"
                                        required>
                                </div>
                                <div v-else>
                                    <input type="text" class="form-control" value="" required>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-4 mb-3">
                                <label for="project_types" class="form-label">Project Type</label>
                                <select class="form-control" v-model="project_type">
                                    <option value="">Select Type</option>
                                    <option value="ERPS">Enterprise Resource Planning System (ERPS)</option>
                                    <option value="CRM">Customer Engagement Platform (CRM)</option>
                                    <option value="E-Com">Online Retail Platform (E-Com)</option>
                                    <option value="Game_Dev">Interactive Entertainment Solutions (Game_Dev)</option>
                                    <option value="WordPress">Dynamic Web Content Management (WordPress)</option>
                                    <option value="Magento">E-Commerce Powerhouse (Magento)</option>
                                    <option value="Shopify">E-Commerce Simplified (Shopify)</option>
                                    <option value="Mobile Application">Mobile Application Solutions</option>
                                    <option value="Web Presence">Web Presence Solutions</option>
                                </select>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="project_name" class="form-label">Project Name</label>
                                <input type="text" class="form-control">
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="project_cost" class="form-label">Project Cost</label>
                                <div class="input-group">
                                    <input v-model="projectCost" type="text" class="form-control" id="project_cost"
                                        style="width: 78%;">
                                    <select class="form-select currency" v-model="selectedCurr"
                                        aria-label="Currency select" style="width:22%;">
                                        <option value="INR">INR</option>
                                        <option value="USD">USD</option>
                                        <option value="EUR">EUR</option>
                                        <option value="CAD">CAD</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-4">
                                <label for="status" class="form-label">Status</label>
                                <div class="input-group">
                                    <select v-model="selectedStatus" class="form-select" name="" id="">
                                        <option selected value="">Select Status</option>
                                        <option v-for="status in quoteStatus" :key="status.id">{{ status.name }}
                                        </option>
                                    </select>
                                    <button data-bs-toggle="modal" data-bs-target="#addStatusModal"
                                        style="border: none; border-radius: 0px 8px 8px 0px; outline: none; background-color: cornflowerblue; color: white; font-weight: 600;">Add</button>
                                </div>
                            </div>
                            <div class="col-md-4">
                                <label for="ref_link" class="form-label">Reference Link</label>
                                <input class="form-control" type="text" name="" id="ref_link">
                            </div>
                            <div class="col-md-4">
                                <label for="api_integration" class="form-label">APIs Integration</label>
                                <input class="form-control" type="text" name="" id="api_integration">
                            </div>
                        </div>
                        <div class="row mb-8">
                            <div class="col-lg-12 col-md-12">
                                <label for="type" class="form-label">Description</label>
                                <QuillEditor required ref="editor" theme="snow" toolbar="full" />
                            </div>
                        </div>
                        <div class="row mt-3">
                            <h5>Time Frame</h5>
                            <div class="col-md-4">
                                <label class="form-label" for="start-date">Start Date</label>
                                <input @change="calculateWorkingDays" v-model="timeFrame.startDate" class="form-control"
                                    type="date" name="start-date" required>
                            </div>
                            <div class="col-md-4">
                                <label class="form-label" for="end-date">End Date</label>
                                <input @change="calculateWorkingDays" v-model="timeFrame.endDate" class="form-control"
                                    type="date" name="end-date" required>
                            </div>
                            <div class="col-md-4">
                                <label class="form-label" for="workingDays">Working Days</label>
                                <input disabled v-model="timeFrame.workingDays" class="form-control" type="text"
                                    name="workingDays" required>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <h5>Tech Specification</h5>
                            <div class="col-md-4 mb-3">
                                <label style="" for="email" class="form-label">Frontend</label>
                                <input class="form-control" required>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label style="" for="email" class="form-label">Backend</label>
                                <input class="form-control" required>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label style="" for="email" class="form-label">Databases</label>
                                <input class="form-control" required>
                            </div>
                        </div>
                        <div>
                            <div class="row" style="margin: 13px 0px -20px -10px">
                                <div class="col-md-3">
                                    <h5>Milestones</h5>
                                </div>
                                <div class="col-md-3">
                                    <button @click="milestoneClonner" type="button"
                                        class="btn btn-primary px-2 py-1 text-sm"
                                        style="margin-left: -100px; outline: none;">Add</button>
                                </div>
                            </div>
                            <div v-for="(data, index) in milestoneClonnerData" :key="index" class="row mt-3">
                                <div class="col-md-3 mb-3">
                                    <label style="" for="name" class="form-label">Name</label>
                                    <input :disabled="!projectCost" class="form-control" v-model="data.name" required>
                                </div>
                                <div class="col-md-3 mb-3">
                                    <label style="" for="cost" class="form-label">Cost</label>
                                    <input :disabled="!projectCost" class="form-control" v-model="data.cost" required>
                                </div>
                                <div class="col-md-3 mb-3">
                                    <label style="" for="date" class="form-label">Delivery Date</label>
                                    <input :disabled="!projectCost" class="form-control" v-model="data.delivery_date"
                                        required>
                                </div>
                                <div v-if="milestoneClonnerData.length > 1" class="col-md-3 mb-3">
                                    <label for="" class="form-label"></label>
                                    <button type="button" @click="milestoneRemover(index)"
                                        class="btn btn-danger form-control">Delete</button>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col col-md-3">
                                <input type="radio" name="GST" id=""> IGST@18%
                            </div>
                            <div class="col col-md-3">
                                <input type="radio" name="GST" id=""> CGST,SGST@9%
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
</template>

<script>
import { BASE_URL } from '../config/apiConfig';
import { QuillEditor } from '@vueup/vue-quill';
import axios from 'axios';
import { mapState } from 'vuex';
import Noty from 'noty';


export default {
    name: "Proposal",
    components: {
        QuillEditor
    },
    data() {
        return {
            clientNameFilter: '',
            contactNoFilter: '',
            quoteStatus: [],
            allSales: [],
            selectedClientID: '',
            selectedClient: null,
            project_type: '',
            projectCost: null,
            selectedCurr: 'INR',
            milestoneClonnerData: [{ 'name': '', 'cost': '', 'delivery_date': '' }],
            timeFrame: {
                startDate: '',
                endDate: '',
                workingDays: ''
            },
            selectedStatus: '',
            AddStatusModalToggler: false,
            newStatus: ''
        }
    },
    computed: {
        ...mapState(['authUser', 'authToken'])
    },
    methods: {
        milestoneClonner() {
            if (!this.projectCost) {
                new Noty({
                    type: 'info',
                    text: 'Please enter project Cost',
                    timeout: 500,
                }).show()
            }
            else {
                let milestonesCost = 0
                this.milestoneClonnerData.forEach((item) => {
                    milestonesCost += Number(item.cost)
                })
                if (milestonesCost >= Number(this.projectCost)) {
                    new Noty({
                        type: 'error',
                        text: 'Total sum of milestones cost should not exceeds the project cost',
                        timeout: 1000,
                    }).show()
                    return
                }
                else {
                    this.milestoneClonnerData.push({ name: '', cost: '', delivery_date: '' })
                }
            }
        },
        milestoneRemover(ind) {
            this.milestoneClonnerData.splice(ind, 1)
        },
        getQuoteStatus() {
            try {
                axios.get(`${BASE_URL}/api/development/proposal/status`, {
                    headers: {
                        "token": this.authToken
                    }
                }).then((res) => {
                    this.quoteStatus = res.data.data

                })
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 500,
                }).show()
            }
        },
        getALLSales() {
            try {
                axios.get(`${BASE_URL}/api/sales/`, {
                    headers: {
                        "token": this.authToken
                    }
                }).then((res) => {
                    this.allSales = res.data.res_data
                })
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 500,
                }).show()
            }
        },
        clientHandler(newVal, oldVal) {
            try {
                if (oldVal !== newVal && newVal !== "") {
                    this.selectedClient = this.allSales.find((client) => client.id == newVal)
                    if (!this.selectedClient) {
                        throw new Error("No lead found for the given ID")
                    }
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.message,
                    timeout: 500,
                }).show()
            }
        },
        calculateWorkingDays() {
            let d1 = new Date(this.timeFrame.startDate);
            let d2 = new Date(this.timeFrame.endDate);

            if (!this.timeFrame.startDate || !this.timeFrame.endDate) {
                new Noty({
                    type: "error",
                    text: "Please select both start and end dates",
                    timeout: 1000
                }).show();
                return;
            }

            if (d2 <= d1) {
                new Noty({
                    type: "error",
                    text: "Please select a valid date range",
                    timeout: 1000
                }).show();
                return;
            }

            if (d2.getDate() - d1.getDate() > 3650) {
                new Noty({
                    type: "info",
                    text: "Don't try to be oversmart",
                    timout: 1000
                }).show();
                return;
            }

            function getWorkingDays(startDate, endDate) {
                let totalDays = 0;
                let currentDate = startDate;

                while (currentDate <= endDate) {
                    let dayOfWeek = currentDate.getDay();
                    if (dayOfWeek !== 0 && dayOfWeek !== 6) {
                        totalDays++;
                    }
                    currentDate.setDate(currentDate.getDate() + 1);
                }
                return totalDays;
            }

            this.timeFrame.workingDays = getWorkingDays(d1, d2);
        },
        addStatus(e) {
            e.preventDefault()
            try {
                this.$store.commit("showLoader")
                axios.post(`${BASE_URL}/api/development/proposal/status`, {
                    statusName: this.newStatus
                }, {
                    headers: {
                        token: this.authToken
                    },
                }).then((res) => {
                    if(res.status===201){
                        new Noty({
                            "type":"success",
                            "text":res.data.message,
                            "timeout":1000
                        }).show()
                        this.newStatus=''
                    }
                    setTimeout(()=>{
                    window.location.reload()
                    },1100)
                    setTimeout(()=>{
                    this.$refs.newProposalModal.click()
                    }, 500)
                    this.$store.commit("hideLoader")
                })
            } catch (error) {
                console.error(error.response.data.message ? error.response.data.message : error.response.data.detail)
                this.$store.commit("hideLoader")
            } finally {
                this.$store.commit("hideLoader")
            }

        },

        createProposal(e) {
            e.preventDefault();
        },
        resetValues() {
            window.location.reload()
        }
    },
    watch: {
        selectedClientID(newVal, oldVal) {
            this.clientHandler(newVal, oldVal)
        },
        projectCost(newVal) {
            if (!newVal) {
                this.milestoneClonnerData = [{ 'name': '', 'cost': '', 'delivery_date': '' }]
            }
        }
    },
    mounted() {
        this.getQuoteStatus()
        this.getALLSales()
    }
}
</script>

<style scoped>
.form-select {
    background-image: none;
    outline: none;
}
</style>