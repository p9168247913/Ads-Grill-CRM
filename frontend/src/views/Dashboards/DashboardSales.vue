<template>
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
                <!-- <div class="col-lg-4 col-md-6 col-12">
                    <card :title="stats.clients.title" :value="stats.clients.value" :percentage="stats.clients.percentage"
                        :iconClass="stats.clients.iconClass" :iconBackground="stats.clients.iconBackground"
                        :percentageColor="stats.clients.percentageColor" :detail="stats.clients.detail" directionReverse>
                    </card>
                </div> -->
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
                                    <tr v-for="(lead, index) in allLeads" :key="index">
                                        <td >
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
                                                <p v-if="lead?.follow_date" class="mb-0 text-xs font-weight-bold">Follow up's date:</p>
                                                <h6 class="mb-0 text-sm">{{ lead?.follow_date? formatDate(lead?.follow_date) :"No follow up's" }}</h6>
                                            </div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
                <div class="col-lg-5">
                    <categories-card />
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
                    title: "Unassigned Leads",
                    value: "",
                    percentage: "",
                    iconClass: "ni ni-paper-diploma",
                    percentageColor: "text-danger",
                    iconBackground: "bg-gradient-success",
                    detail: "",
                },
                sales: {
                    title: "Sales",
                    value: "$103,430",
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
        }
    },
    components: {
        Card,
    },
    computed: {
        ...mapState(['authUser', 'authToken']),
    },
    methods: {
        formatDate(inputDate) {
            const date = new Date(inputDate);
            const options = { day: 'numeric', month: 'long', year: 'numeric' };
            const formattedDate = date.toLocaleDateString('en-GB', options);
            return formattedDate;
        },
        showFollowUpLeads() {
            this.allLeads = this.allLeads.filter(lead => lead.follow_date);
        },
        showAllLeads(){
            this.getLeads()
        },
        async getLeads() {
            let queryParams = {
                page_no: this.currentPage ? this.currentPage : 1,
            };
            try {
                const response = await axios.get(`${BASE_URL}api/sales/?page_no=${queryParams.page_no}`, {
                    headers: {
                        token: this.authToken,
                    }
                })
                if (response.status === 200) {
                    this.allLeads = response?.data?.res_data
                    this.stats.money.value = response?.data?.data?.total_sales
                    this.stats.users.value = response?.data?.data?.follow_count
                    this.stats.clients.value = response?.data?.lead_data?.unassigned_leads
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
    mounted() {
        this.getLeads()
    }  
}
</script>