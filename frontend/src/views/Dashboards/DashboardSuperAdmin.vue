<template>
    <div class="wrapper" style="margin-bottom: 80px; padding: 0; ">
        <div class="content-page">
            <!-- <h1>Dashboard Lead</h1> -->
            <div class="container-fluid">
                <div class="row">
                    <div class="col-lg-12">
                        <!-- <h1>Leads</h1> -->
                        <div class="row">
                            <div style="cursor: pointer;" class="col-lg-4 col-md-6 col-12" @click="redirect('lead')">
                                <card :title="stats.money.title" :value="stats.money.value"
                                    :percentage="stats.money.percentage" :iconClass="stats.money.iconClass"
                                    :iconBackground="stats.money.iconBackground" :detail="stats.money.detail"
                                    directionReverse></card>
                            </div>
                            <div style="cursor: pointer;" class="col-lg-4 col-md-6 col-12" @click="redirect('pro')">
                                <card :title="stats.users.title" :value="stats.users.value"
                                    :percentage="stats.users.percentage" :iconClass="stats.users.iconClass"
                                    :iconBackground="stats.users.iconBackground" :detail="stats.users.detail"
                                    directionReverse></card>
                            </div>
                            <div style="cursor: pointer;" class="col-lg-4 col-md-6 col-12" @click="redirect('deve')">
                                <card :title="stats.clients.title" :value="stats.clients.value"
                                    :percentage="stats.clients.percentage" :iconClass="stats.clients.iconClass"
                                    :iconBackground="stats.clients.iconBackground"
                                    :percentageColor="stats.clients.percentageColor" :detail="stats.clients.detail"
                                    directionReverse>
                                </card>
                            </div>
                            <!-- <div class="col-lg-3 col-md-6 col-12">
                                <card :title="stats.sales.title" :value="stats.sales.value"
                                    :percentage="stats.sales.percentage" :iconClass="stats.sales.iconClass"
                                    :iconBackground="stats.sales.iconBackground" :detail="stats.sales.detail"
                                    directionReverse></card>
                            </div> -->
                        </div>

                        <!-- <div class="row mt-4">
                <div class="col-lg-7 mb-lg-0 mb-4">
                    <div class="card">
                        <div class="p-3 pb-0 card-header">
                            <div class="d-flex justify-content-between">
                                <h6 class="mb-2">Sales by Country</h6>
                            </div>
                        </div>
                        <div class="table-responsive">
                            <table class="table align-items-center">
                                <tbody>
                                    <tr v-for="(sale, index) in sales" :key="index">
                                        <td class="w-30">
                                            <div class="px-2 py-1 d-flex align-items-center">
                                                <div>
                                                    <img :src="sale.flag" alt="Country flag" />
                                                </div>
                                                <div class="ms-4">
                                                    <p class="mb-0 text-xs font-weight-bold">Country:</p>
                                                    <h6 class="mb-0 text-sm">{{ sale.country }}</h6>
                                                </div>
                                            </div>
                                        </td>
                                        <td>
                                            <div class="text-center">
                                                <p class="mb-0 text-xs font-weight-bold">Sales:</p>
                                                <h6 class="mb-0 text-sm">{{ sale.sales }}</h6>
                                            </div>
                                        </td>
                                        <td>
                                            <div class="text-center">
                                                <p class="mb-0 text-xs font-weight-bold">Value:</p>
                                                <h6 class="mb-0 text-sm">{{ sale.value }}</h6>
                                            </div>
                                        </td>
                                        <td class="text-sm align-middle">
                                            <div class="text-center col">
                                                <p class="mb-0 text-xs font-weight-bold">Bounce:</p>
                                                <h6 class="mb-0 text-sm">{{ sale.bounce }}</h6>
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
            </div> -->
                    </div>
                </div>
                <div class="card" style="background-color: white; border-radius: 10px; padding: 10px;">
                    <h5>MANAGERS</h5>
                    <div class="row">
                        <div class="col-lg-3 col-md-6 col-sm-12 mb-2" style="width:auto;" v-for="(manager, index) in managers" :key="index">
                            <div class="card p-1"
                                style="height: 140px; display: flex; flex-direction: row; gap: 5px;">
                                <img :src="getProfilePic(manager)" alt="Manager Image"
                                    style="width: 130px; height: 130px; border-radius: 5px;">
                                <div class="card-body" style="padding-bottom: 0; padding-top: 1">
                                    <p class="card-title" style="font-weight: bold; font-size: 15px">{{ manager.name }}
                                    </p>
                                    <p class="card-text" style="font-size: 13px">{{ manager.designation ===
                                'project_manager' ? "Project Manager" : manager.designation === 'sales_manager'
                                ?
                                "Sales Manager" : manager.designation === 'leads_manager'
                                    ?
                                    "Lead Manager" : manager.designation }}</p>
                                </div>
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
// import GradientLineChart from "@/examples/Charts/GradientLineChart.vue";
// import Carousel from "../components/Carousel.vue";
// import CategoriesCard from "../components/CategoriesCard.vue";
import Noty from 'noty';
import US from "@/assets/img/icons/flags/US.png";
import DE from "@/assets/img/icons/flags/DE.png";
import GB from "@/assets/img/icons/flags/GB.png";
import BR from "@/assets/img/icons/flags/BR.png";
import axios from 'axios';
import { BASE_URL } from '../../config/apiConfig';
import { mapState } from 'vuex';
import router from "@/router";

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
                    title: "Total Projects",
                    value: "",
                    percentage: "",
                    iconClass: "ni ni-world",
                    iconBackground: "bg-gradient-danger",
                    detail: "",
                },
                clients: {
                    title: "Total Employees",
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
            managers: [],
        }
    },
    components: {
        Card,
        // GradientLineChart,
        // Carousel,
        // CategoriesCard,
    },
    computed: {
        ...mapState(['authUser', 'authToken']),
    },
    methods: {
        redirect(parameter) {
            parameter === 'deve' ? router.push('/employees/development') : parameter === 'pro' ? router.push('/projects') : parameter === 'lead' ? router.push('/leads') : router.push('/dashboard')
        },
        getProfilePic(manager) {
            return manager.profile_pic ? `data:image/jpeg;base64,${manager.profile_pic}` : "https://www.kindpng.com/picc/m/78-786678_avatar-hd-png-download.png";
        },
        async getLeads() {
            let queryParams = {
                page_no: this.currentPage ? this.currentPage : 1,
            };
            try {
                const response = await axios.get(`${BASE_URL}api/leads/?page_no=${queryParams.page_no}`, {
                    headers: {
                        token: this.authToken,
                    }
                })
                if (response.status === 200) {
                    this.stats.money.value = response?.data?.lead_data?.total_leads
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error,
                    timeout: 500,
                }).show()
            }
        },
        async getProjects() {
            try {

                const response = await axios.get(`${BASE_URL}api/development/projects?key=development`, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                        token: this.authToken,
                    }
                })
                this.$store.commit('showLoader');
                if (response.status === 200) {
                    this.stats.users.value = response?.data?.projects?.length;
                }
                this.$store.commit('hideLoader');
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 500,
                }).show()
                this.$store.commit('hideLoader');
            }
        },
        async getAllManagers() {
            try {
                const response = await axios.get(`${BASE_URL}api/users/getAllManagers`, {
                    headers: {
                        token: this.authToken,
                    }
                })
                if (response.status === 200) {
                    this.managers = response.data.manager_data;
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error,
                    timeout: 500,
                }).show()
            }
        },
        async getEmployees() {
            try {
                const response = await axios.get(`${BASE_URL}api/users/?role=client`, {
                    headers: {
                        token: this.authToken,
                    }
                })
                if (response.status === 200) {
                    this.stats.clients.value = response.data.employee_count;
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error,
                    timeout: 500,
                }).show()
            }
        },
    },
    mounted() {
        this.getLeads();
        this.getProjects();
        this.getAllManagers();
        this.getEmployees();
    }
}
</script>

<style scoped>
.card {
    border: 1px solid #ccc;
    border-radius: 8px;
}

.card-img-top {
    width: 100%;
    height: auto;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
}

.card-title {
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
}

.card-text {
    font-size: 1rem;
}
</style>