<template>

    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Webkit | Responsive Bootstrap 4 Admin Dashboard Template</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
    </head>
    <!-- <h1>Dashboard Lead</h1> -->
    <div class="row">
        <div class="col-lg-12">
            <!-- <h1>Leads</h1> -->
            <div class="row">
                <div style="cursor: pointer;" class="col-lg-4 col-md-6 col-12" @click="showAllLeads">
                    <card :title="stats.money.title" :value="stats.money.value" :percentage="stats.money.percentage"
                        :iconClass="stats.money.iconClass" :iconBackground="stats.money.iconBackground"
                        :detail="stats.money.detail" directionReverse></card>
                </div>
                <div style="cursor: pointer;" class="col-lg-4 col-md-6 col-12" @click="showFollowUpLeads">
                    <card :title="stats.users.title" :value="stats.users.value" :percentage="stats.users.percentage"
                        :iconClass="stats.users.iconClass" :iconBackground="stats.users.iconBackground"
                        :detail="stats.users.detail" directionReverse></card>
                </div>
                <div class="col-lg-4 col-md-6 col-12">
                    <card :title="stats.clients.title" :value="stats.clients.value" :percentage="stats.clients.percentage"
                        :iconClass="stats.clients.iconClass" :iconBackground="stats.clients.iconBackground"
                        :percentageColor="stats.clients.percentageColor" :detail="stats.clients.detail" directionReverse>
                    </card>
                </div>
                <div class="col-lg-4 col-md-6 col-12">
                    <card :title="stats.sales.title" :value="stats.sales.value" :percentage="stats.clients.percentage"
                        :iconClass="stats.clients.iconClass" :iconBackground="stats.clients.iconBackground"
                        :percentageColor="stats.clients.percentageColor" :detail="stats.clients.detail" directionReverse>
                    </card>
                </div>
                <div style="cursor: pointer;" class="col-lg-4 col-md-6 col-12" @click="showFollowUpLeads">
                    <card :title="stats.proposal.title" :value="stats.proposal.value" :percentage="stats.users.percentage"
                        :iconClass="stats.users.iconClass" :iconBackground="stats.users.iconBackground"
                        :detail="stats.users.detail" directionReverse></card>
                </div>
                <div class="col-lg-4 col-md-6 col-12">
                    <card :title="stats.invoice.title" :value="stats.invoice.value" :percentage="stats.clients.percentage"
                        :iconClass="stats.clients.iconClass" :iconBackground="stats.clients.iconBackground"
                        :percentageColor="stats.clients.percentageColor" :detail="stats.clients.detail" directionReverse>
                    </card>
                </div>
                <!-- <div class="col-lg-3 col-md-6 col-12">
                    <card :title="stats.sales.title" :value="stats.sales.value" :percentage="stats.sales.percentage"
                        :iconClass="stats.sales.iconClass" :iconBackground="stats.sales.iconBackground"
                        :detail="stats.sales.detail" directionReverse></card>
                </div> -->
            </div>

            <div class="row mt-4">
                <div class="col-lg-7 mb-lg-0 mb-4">
                    <div class="card">
                        <div class="p-3 pb-0 card-header">
                            <div class="d-flex justify-content-between">
                                <h6 class="mb-2">All Leads</h6>
                            </div>
                        </div>
                        <div class="table-responsive">
                            <table class="table align-items-center">
                                <tbody>
                                    <tr v-for="(lead, index) in allLeads" :key="index" :style="{backgroundColor: `#${lead.row_color ? lead.row_color : ''}`}">
                                        <td>
                                            <div class="text-center">
                                                <!-- <div>
                                                    <img :src="sale.flag" alt="Country flag" />
                                                </div> -->
                                                <!-- <div class="ms-4"> -->
                                                <p class="mb-0 text-xs font-weight-bold">Contact name:</p>
                                                <h6 class="mb-0 text-sm">{{ lead.name }}</h6>
                                                <!-- </div> -->
                                            </div>
                                        </td>
                                        <td>
                                            <div class="text-center">
                                                <p class="mb-0 text-xs font-weight-bold">Contact number:</p>
                                                <h6 class="mb-0 text-sm">{{ lead.conact_no }}</h6>
                                            </div>
                                        </td>
                                        <td>
                                            <div class="text-center">
                                                <p class="mb-0 text-xs font-weight-bold">Source:</p>
                                                <h6 class="mb-0 text-sm">{{ lead.source.name }}</h6>
                                            </div>
                                        </td>
                                        <td class="text-sm align-middle">
                                            <div class="text-center col">
                                                <p class="mb-0 text-xs font-weight-bold">Date:</p>
                                                <h6 class="mb-0 text-sm">{{ formatDate(lead.created_at) }}</h6>
                                            </div>
                                        </td>
                                        <td class="text-sm align-middle">
                                            <div class="text-center col">
                                                <p v-if="lead?.follow_date" class="mb-0 text-xs font-weight-bold">Follow
                                                    up's date:</p>
                                                <h6 class="mb-0 text-sm">{{ lead?.follow_date ?
                                                    formatDate(lead?.follow_date) : "No follow up's" }}</h6>
                                            </div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <PaginationComponent v-if="this.totalPages > 1" :currentPage="currentPage" :totalPages="totalPages"
                        :itemsPerPage="itemsPerPage" :prevPage="prevPage" :getLeads="getLeads" :nextPage="nextPage"
                        :goToPage="goToPage" />
                    </div>
                    
                </div>
                <div class="col-lg-5">
                    <div class="card">
                        <div class="p-3 pb-0 card-header">
                            <div class="d-flex justify-content-between">
                                <h6 class="mb-2">My Todos</h6>
                                <div class="dropdown">
                                    <button class="btn btn-secondary dropdown-toggle" type="button" id="filterDropdown"
                                        data-bs-toggle="dropdown" aria-expanded="false">
                                        Filter
                                    </button>
                                    <ul class="dropdown-menu" aria-labelledby="filterDropdown">
                                        <li><a class="dropdown-item" href="#" @click="filterTodos('All')">All</a></li>
                                        <li><a class="dropdown-item" href="#" @click="filterTodos('todo')">Todo</a></li>
                                        <li><a class="dropdown-item" href="#" @click="filterTodos('done')">Done</a></li>
                                    </ul>
                                </div>
                                <button data-bs-toggle="modal" data-bs-target="#createTodo" class="btn btn-primary">Add
                                    Todo</button>
                            </div>
                        </div>
                        <div class="table-responsive">
                            <table class="table align-items-center">
                                <tbody>
                                    <tr v-for="(todo, index) in filteredTodos" :key="index">
                                        <td>
                                            <div class="card mb-1">
                                                <div class="card-body d-flex justify-content-between">
                                                    <p class="mb-0">{{ todo.desc }}</p>
                                                    <div data-bs-toggle="modal" data-bs-target="#editTodo">
                                                        <i class="far fa-edit mr-2" @click="editData(todo)"></i>
                                                    </div>
                                                </div>
                                            </div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    
                </div>
                <div data-bs-backdrop="static" class="modal fade" ref="createProject" id="createTodo" tabindex="-1"
                    aria-labelledby="createProjectLabel" aria-hidden="true" @hidden="createSprints">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px;">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createProjectLabel">Create Todo</h5>
                                <button @click="resetValues" ref="createTodo" type="button"
                                    class="btn-close bg-dark text-xs" data-bs-dismiss="modal"
                                    aria-label="Close"></button>
                            </div>
                            <div class="modal-body modalBodyCreate" style="padding-bottom: 0; height: 14rem; overflow: auto;">
                                <form @submit="createTodo($event)">
                                    <div class="row">
                                        <div class="col-md-12 mb-3">
                                            <label for="title" class="form-label">Description</label>
                                            <textarea type="text" class="form-control" v-model="todo.desc"
                                                required></textarea>
                                        </div>
                                    </div>
                                    <div class="modal-footer"
                                        style="z-index: 999; margin-top: 10px; position: sticky; bottom: 0; background-color: white; ">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                                            @click="resetValues">Close</button>
                                        <button type="submit" class="btn btn-primary">Create</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                <div data-bs-backdrop="static" class="modal fade" ref="createProject" id="editTodo" tabindex="-1"
                    aria-labelledby="createProjectLabel" aria-hidden="true" @hidden="createSprints">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px;">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createProjectLabel">Edit Todo</h5>
                                <button @click="resetValues" ref="editTodo" type="button"
                                    class="btn-close bg-dark text-xs" data-bs-dismiss="modal"
                                    aria-label="Close"></button>
                            </div>
                            <div class="modal-body modalBodyCreate" style="padding-bottom: 0; height: 20rem; overflow: auto;">
                                <form @submit="editTodos($event)">
                                    <div class="row">
                                        <div class="col-md-12 mb-3">
                                            <label for="title" class="form-label">Description</label>
                                            <textarea type="text" class="form-control" v-model="editTodo.desc"
                                                required></textarea>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-12 mb-3">
                                            <label for="title" class="form-label">Status</label>
                                            <select class="form-select" v-model="editTodo.status" required>
                                                <option value="todo">To do</option>
                                                <option value="done">Done</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="modal-footer"
                                        style="z-index: 999; margin-top: 10px; position: sticky; bottom: 0; background-color: white; ">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                                            @click="resetValues">Close</button>
                                        <button type="submit" class="btn btn-primary">Update</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import Card from "@/examples/Cards/Card.vue";
import Noty from 'noty';
import US from "@/assets/img/icons/flags/US.png";
import DE from "@/assets/img/icons/flags/DE.png";
import GB from "@/assets/img/icons/flags/GB.png";
import BR from "@/assets/img/icons/flags/BR.png";
import axios from 'axios';
import { BASE_URL } from '../../config/apiConfig';
import { mapState } from 'vuex';
import PaginationComponent from '../../components/Paginator/PaginatorComponent.vue';


export default {
    data() {
        return {
            stats: {
                money: {
                    title: "Total Leads",
                    value: "",
                    percentage: "",
                    iconClass: "ni ni-money-coins",
                    detail: "",
                    iconBackground: "bg-gradient-primary",
                },
                users: {
                    title: "Follow-up's",
                    value: "",
                    percentage: "",
                    iconClass: "ni ni-world",
                    iconBackground: "bg-gradient-danger",
                    detail: "",
                },
                clients: {
                    title: "Quotation",
                    value: "200",
                    percentage: "",
                    iconClass: "ni ni-paper-diploma",
                    percentageColor: "text-danger",
                    iconBackground: "bg-gradient-success",
                    detail: "",
                },
                sales: {
                    title: "Onboarded Leads",
                    value: "10",
                    percentage: "+5%",
                    iconClass: "ni ni-cart",
                    iconBackground: "bg-gradient-warning",
                    detail: "than last month",
                },
                proposal: {
                    title: "Proposals",
                    value: "30",
                    percentage: "+5%",
                    iconClass: "ni ni-cart",
                    iconBackground: "bg-gradient-warning",
                    detail: "than last month",
                },
                invoice: {
                    title: "Invoice",
                    value: "40",
                    percentage: "+5%",
                    iconClass: "ni ni-cart",
                    iconBackground: "bg-gradient-warning",
                    detail: "than last month",
                },
            },
            sales: {
                us: {
                    country: "United States",
                    sales: 2500,
                    value: "$230,900",
                    bounce: "29.9%",
                    flag: US,
                },
                germany: {
                    country: "Germany",
                    sales: "3.900",
                    value: "$440,000",
                    bounce: "40.22%",
                    flag: DE,
                },
                britain: {
                    country: "Great Britain",
                    sales: "1.400",
                    value: "$190,700",
                    bounce: "23.44%",
                    flag: GB,
                },
                brasil: {
                    country: "Brasil",
                    sales: "562",
                    value: "$143,960",
                    bounce: "32.14%",
                    flag: BR,
                },
            },
            currentPage: 1,
            allLeads: [],
            todo: {
                desc: ""
            },
            editTodo: {
                id: '',
                desc: "",
                status: ''
            },
            allTodos: [],
            selectedStatus: "All",
            itemsPerPage: 5,
            totalPages: null,
        }
    },
    components: {
        Card,
        PaginationComponent,
    },
    computed: {
        ...mapState(['authUser', 'authToken']),
        filteredTodos() {
            if (this.selectedStatus === "All") {
                return this.allTodos;
            } else {
                return this.allTodos.filter(todo => todo.status === this.selectedStatus);
            }
        }
    },
    methods: {
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
        formatDate(inputDate) {
            const date = new Date(inputDate);
            const options = { day: 'numeric', month: 'long', year: 'numeric' };
            const formattedDate = date.toLocaleDateString('en-GB', options);
            return formattedDate;
        },
        showFollowUpLeads() {
            this.allLeads = this.allLeads.filter(lead => lead.follow_date);
        },
        showAllLeads() {
            this.getLeads()
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
                    this.allLeads = response?.data?.res_data
                    this.stats.money.value = response?.data?.data?.total_sales
                    this.stats.users.value = response?.data?.data?.follow_count
                    // this.stats.clients.value = response?.data?.lead_data?.unassigned_leads
                    this.totalPages = response?.data?.data?.total_pages
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show()
            }
        },
        async getTodos() {
            try {
                const response = await axios.get(`${BASE_URL}api/todo/`, {
                    headers: {
                        token: this.authToken,
                    }
                })
                if (response.status === 200) {
                    this.allTodos = response?.data?.todo
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show()
            }
        },
        async createTodo(e) {
            e.preventDefault();
            try {
                const response = await axios.post(`${BASE_URL}api/todo/`, this.todo, {
                    headers: {
                        token: this.authToken,
                    }
                })
                if (response.status === 201) {
                    new Noty({
                        type: 'success',
                        text: '✔ Added!',
                        timeout: 1000,
                        layout: 'topCenter'
                    }).show()
                    this.todo.desc="";
                    this.getTodos();
                    this.$refs.createTodo.click()
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show()
            }
        },
        editData(todo) {
            this.editTodo.id = todo.id;
            this.editTodo.desc = todo.desc;
            this.editTodo.status = todo.status;
        },
        async editTodos(e) {
            e.preventDefault();
            try {
                const response = await axios.patch(`${BASE_URL}api/todo/`, this.editTodo, {
                    headers: {
                        token: this.authToken,
                    }
                })
                if (response.status === 200) {
                    new Noty({
                        type: 'success',
                        text: '✔ Updated!',
                        timeout: 1000,
                        layout: 'topCenter'
                    }).show()
                    this.getTodos();
                    this.$refs.editTodo.click()
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show()
            }
        },
        filterTodos(status) {
            this.selectedStatus = status;
        },
    },
    mounted() {
        this.getLeads();
        this.getTodos();
    }
}
</script>