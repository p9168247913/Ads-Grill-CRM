<template>
    <div class="container">
        <div class="row" style="margin-top: 20px;">
            <div class="col-md-12 col-lg-12 block">
                <h6 class="text-uppercase">Add Tag</h6>
                <div class="col-md-5 mb-3">
                    <form @submit="addLeadInfo($event, 'tag')" style="display: flex; gap: 10px;">
                        <input required type="text" class="form-control" v-model="newLeadInfoTag"
                            placeholder="Enter Tag" />
                        <button type="submit" class="btn btn-sm btn-dark px-3 py-2 h-100 d-flex"
                            style="width: auto !important;"> <i
                                class="fas fa-plus-circle text-success text-sm opacity-10"></i>
                            &nbsp;&nbsp;<span>Add</span></button>
                    </form>
                </div>
                <table class="table">
                    <thead>
                        <tr>
                            <th style="color: #344767 !important;width: 25%;"
                                class="text-start align-middle text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold"
                                scope="col">S.NO.</th>
                            <th style="color: #344767 !important;width: 50%;"
                                class="text-start align-middle text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold"
                                scope="col">Tag</th>
                            <th style="color: #344767 !important;width: 35%;"
                                class="text-start align-middle text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold"
                                scope="col">ACTIONS</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(tag, index) in tags" :key="index">
                            <td style="padding-left: 25px;" class="text-start align-middle" scope="row">
                                <h6 class="mb-0 text-sm">{{ index + 1 }}</h6>
                            </td>
                            <td style="padding-left: 25px;" class="text-start align-middle">
                                <h6 class="mb-0 text-sm">{{ tag.name }}</h6>
                            </td>
                            <td style="padding-left: 25px;" class="text-start align-middle">
                                <i class="fas fa-trash text-danger m-3 fa-xs delete-icon"
                                    @click="deleteLeadInfo('tag', tag.id)" style="cursor: pointer"></i>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="row" style="margin-top: 20px;">
            <div class="col-md-12 col-lg-12 block">
                <h6 class="text-uppercase">Add Source</h6>
                <div class="col-md-5 mb-3">
                    <form @submit="addLeadInfo($event, 'source')" style="display: flex; gap: 10px;">
                        <input required type="text" class="form-control" v-model="newLeadInfoSource"
                            placeholder="Enter Source" />
                        <button type="submit" class="btn btn-dark d-flex" style="width: auto !important;"> <i
                                class="fas fa-plus-circle text-success text-sm opacity-10"></i>
                            &nbsp;&nbsp;<span>Add</span></button>
                    </form>
                </div>
                <table class="table">
                    <thead>
                        <tr>
                            <th style="color: #344767 !important;width: 25%;"
                                class="text-start align-middle text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold"
                                scope="col">S.NO.</th>
                            <th style="color: #344767 !important;width: 50%;"
                                class="text-start align-middle text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold"
                                scope="col">Source</th>
                            <th style="color: #344767 !important;width: 35%;"
                                class="text-start align-middle text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold"
                                scope="col">ACTIONS</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(source, index) in sources" :key="index">
                            <td style="padding-left: 25px;" class="text-start align-middle" scope="row">
                                <h6 class="mb-0 text-sm">{{ index + 1 }}</h6>
                            </td>
                            <td style="padding-left: 25px;" class="text-start align-middle">
                                <h6 class="mb-0 text-sm">{{ source.name }}</h6>
                            </td>
                            <td style="padding-left: 25px;" class="text-start align-middle">
                                <i class="fas fa-trash text-danger m-3 fa-xs delete-icon"
                                    @click="deleteLeadInfo('source', source.id)" style="cursor: pointer"></i>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="row" style="margin-top: 20px;">
            <div class="col-md-12 col-lg-12 block">
                <h6 class="text-uppercase">Add Status</h6>
                <div class="col-md-5 mb-3">
                    <form @submit="addLeadInfo($event, 'status')" style="display: flex; gap: 10px;">
                        <input required type="text" class="form-control" v-model="newLeadInfoStatus"
                            placeholder="Enter Status" />
                        <button type="submit" class="btn btn-dark d-flex" style="width: auto !important;"> <i
                                class="fas fa-plus-circle text-success text-sm opacity-10"></i>
                            &nbsp;&nbsp;<span>Add</span></button>
                    </form>
                </div>
                <table class="table">
                    <thead>
                        <tr>
                            <th style="color: #344767 !important;width: 25%;"
                                class="text-start align-middle text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold"
                                scope="col">S.NO.</th>
                            <th style="color: #344767 !important;width: 50%;"
                                class="text-start align-middle text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold"
                                scope="col">STATUS</th>
                            <th style="color: #344767 !important;width: 35%;"
                                class="text-start align-middle text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold"
                                scope="col">ACTIONS</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(status, index) in statuses" :key="index">
                            <td style="padding-left: 25px;" class="text-start align-middle" scope="row">
                                <h6 class="mb-0 text-sm">{{ index + 1 }}</h6>
                            </td>
                            <td style="padding-left: 25px;" class="text-start align-middle">
                                <h6 class="mb-0 text-sm">{{ status.name }}</h6>
                            </td>
                            <td style="padding-left: 25px;" class="text-start align-middle">
                                <i class="fas fa-trash text-danger m-3 fa-xs delete-icon"
                                    @click="deleteLeadInfo('status', status.id)" style="cursor: pointer"></i>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Noty from 'noty';
import Swal from 'sweetalert2';
import { BASE_URL } from '../config/apiConfig';

export default {
    data() {
        return {
            isLoading: false,
            newLeadInfoTag: '',
            newLeadInfoSource: '',
            newLeadInfoStatus: '',
            newLeadInfo: '',
            tags: [],
            sources: [],
            statuses: [],
        };
    },
    methods: {
        async getLeadsInfo() {
            try {
                this.$store.commit('showLoader')
                const response = await axios.get(`${BASE_URL}api/leadinfo/`)
                this.tags = response.data.leadInfoData['leadTag']
                this.sources = response.data.leadInfoData['leadSource']
                this.statuses = response.data.leadInfoData['leadStatus']
                this.$store.commit('hideLoader')
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show()
                this.$store.commit('hideLoader')
            }
        },
        async addLeadInfo(e, infoName) {
            e.preventDefault()
            if (infoName === 'tag') {
                this.newLeadInfo = this.newLeadInfoTag
            }
            else if (infoName === 'source') {
                this.newLeadInfo = this.newLeadInfoSource
            }
            else if (infoName === 'status') {
                this.newLeadInfo = this.newLeadInfoStatus
            }
            try {
                this.$store.commit('showLoader')
                const response = await axios.post(`${BASE_URL}api/leadinfo/?key=${infoName}&name=${this.newLeadInfo}`)
                if (response.status === 201) {
                    Swal.fire({
                        title: `${response.data.message}`,
                        icon: 'success',
                    })
                    this.getLeadsInfo();
                    this.newLeadInfoTag = ''
                    this.newLeadInfoSource = ''
                    this.newLeadInfoStatus = ''
                }
                this.$store.commit('hideLoader')
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show()
                this.$store.commit('hideLoader')
            }
        },
        async deleteLeadInfo(infoName, newLeadInfoId) {
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
                        this.$store.commit('showLoader')
                        const response = await axios.delete(`${BASE_URL}api/leadinfo/?key=${infoName}&id=${newLeadInfoId}`)
                        if (response.status === 204) {
                            this.getLeadsInfo();
                            Swal.fire('Deleted!', response.data.message, 'success');
                        }
                        this.$store.commit('hideLoader')
                    } catch (error) {
                        Swal.fire('Error', error.response.data.message ? error.response.data.message : error.response.data.detail, 'error');
                        this.$store.commit('hideLoader')
                    }
                }
            });
        },
    },
    mounted() {
        this.getLeadsInfo();
    }
};
</script>

<style scoped>
.container {
    margin-top: 30px;
    padding-bottom: 80px !important;
}

.block {
    background-color: white;
    border-radius: 10px;
    box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
    padding: 10px;
}

.input-group {
    display: flex;
    gap: 10px;
}

.form-control,
.btn-primary {
    height: 38px;
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
</style>