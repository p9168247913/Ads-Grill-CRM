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

                                <button type="button"
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

    <!-- MODAL FOR CREATE PROPOSAL -->
    <div style="min-width: auto; margin-left:-100px" data-bs-backdrop="static" class="modal fade"
        ref="createProposalModal" id="createProposal" tabindex="-1" aria-labelledby="createadminLabel"
        aria-hidden="true">
        <div style="width:auto" class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px; width:auto">
                <div class="modal-header">
                    <h5 class="modal-title" id="createadminLabel">New Proposal</h5>
                    <button ref="createProposalBtn" type="button" class="btn-close bg-dark text-xs"
                        data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body modalBody" style="padding-bottom: 0; height:35rem; width: 900px;">
                    <form @submit="createProposal()">
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
                                    <input disabled type="text" class="form-control" id="project_cost"
                                        style="width: 80%;">
                                    <select class="form-select currency" aria-label="Currency select"
                                        style="width:20%;">
                                        <option selected value="">INR</option>
                                        <option value="USD">USD</option>
                                        <option value="EUR">EUR</option>
                                        <option value="CAD">CAD</option>
                                    </select>
                                </div>
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
                                    <input class="form-control" v-model="data.name" required>
                                </div>
                                <div class="col-md-3 mb-3">
                                    <label style="" for="cost" class="form-label">Cost</label>
                                    <input class="form-control" v-model="data.cost" required>
                                </div>
                                <div class="col-md-3 mb-3">
                                    <label style="" for="date" class="form-label">Delivery Date</label>
                                    <input class="form-control" v-model="data.delivery_date" required>
                                </div>
                                <div v-if="milestoneClonnerData.length>1" class="col-md-3 mb-3">
                                    <label for="" class="form-label"></label>
                                    <button type="button" @click="milestoneRemover(index)"
                                        class="btn btn-danger form-control">Delete</button>
                                </div>
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
import axios from 'axios';
import { mapState } from 'vuex';
// import Noty from 'noty';


export default {
    name: "Proposal",
    data() {
        return {
            quoteStatus: [],
            allSales: [],
            selectedClientID: '',
            selectedClient: null,
            project_type: '',
            milestoneClonnerData: [{ 'name': '', 'cost': '', 'delivery_date': '' }]
        }
    },
    computed: {
        ...mapState(['authUser', 'authToken'])
    },
    methods: {
        milestoneClonner() {
            this.milestoneClonnerData.push({ 'name': '', 'cost': '', 'delivery_date': '' })
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
            } catch (e) {
                console.log(e)
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
                    console.log(this.allSales)
                })
            } catch (e) {
                console.log(e)
            }
        },
        clientHandler(newVal, oldVal) {
            try {
                if (oldVal !== newVal) {
                    this.selectedClient = this.allSales.find((client) => client.id == newVal)
                }
            } catch (e) {
                console.log(e)
            }
        },
        createProposal() {

        },
        resetValues() {
        }
    },
    watch: {
        selectedClientID(newVal, oldVal) {
            this.clientHandler(newVal, oldVal)
        }
    },
    mounted() {
        this.getQuoteStatus()
        this.getALLSales()
    }
}
</script>

<style scoped></style>