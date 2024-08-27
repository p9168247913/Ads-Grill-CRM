<template>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Webkit | Responsive Bootstrap 4 Admin Dashboard Template</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
    </head>

    <!--Create Disclaimer Template Button Start-->
    <div class="wrapper">
        <div class="content-page">
            <div class="container-fluid">
                <div style="margin-top: 20px;">
                    <div class="row">
                        <div  class="col">
                            <h5>Create Template</h5>
                            <div>
                                <button ref="newDisclaimerModel" type="button" style=" display:flex; width:10em;height:40px !important; outline: none; justify-content: center; align-items: center;" 
                                class="btn btn-sm btn-dark" data-bs-toggle="modal" data-bs-target="#createDisclaimer"
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
       <!--Create Disclaimer Template Button End-->

        <!--Create Disclaimer Template Modal Start-->
        <div data-bs-backdrop="static" class="modal fade" ref="addDesclaimer" id="createDisclaimer" tabindex="-1"
        aria-labelledby="createadminLabel" aria-hidden="true" style="margin-left: -160px;">
        <div style="width:auto" class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px; width:auto">
                <div class="modal-header">
                    <h5 class="modal-title" id="createadminLabel">Add Disclaimer Templates</h5>
                    <button @click="resetValues" type="button" class="btn-close bg-dark text-xs"
                        data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body modalBody" style="padding-bottom: 0; height:35rem; width: 890px;">
                    <form @submit="addDesclaimer($event)">
                        <div class="row">
                            <div class="col-md-12 col-lg-12">
                                <label class="form-label" for="desclaimerTitle">Enter Disclaimer Title</label>
                                <input id="desclaimerTitle" type="text" class="form-control" v-model="newDesclaimerTitle" required>
                            </div>
                            <div class="col-md-12 col-lg-12 mb-8">
                                <label class="form-label" for="desclaimerDesc">Enter Disclaimer Description</label>
                                <QuillEditor required ref="editor" theme="snow" toolbar="full" v-model:content="newDesclaimerDesc" contentType="html" id="desclaimerDesc"/>
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
    <!--Create Disclaimer Template Modal End-->

    <!--Modal for Editing Disclaimer Start-->
    <div data-bs-backdrop="static" class="modal fade" ref="editDesclaimer" id="editDisclaimerModal" tabindex="-1"
        aria-labelledby="createadminLabel" aria-hidden="true" style="margin-left: -160px;">
        <div style="width:auto" class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px; width:auto">
                <div class="modal-header">
                    <h5 class="modal-title" id="createadminLabel">Edit Disclaimer Templates</h5>
                    <button @click="resetValues" type="button" class="btn-close bg-dark text-xs"
                        data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body modalBody" style="padding-bottom: 0; height:35rem; width: 890px;">
                    <form @submit.prevent="updateDisclaimer">
                        <div class="row">
                            <div class="col-md-12 col-lg-12">
                                <label for="editDesclaimerTitle" class="form-label">Title</label>
                                <input type="text" class="form-control" id="editDesclaimerTitle" v-model="editDesclaimerData.title" required>
                            </div>
                            <div class="col-md-12 col-lg-12 mb-8">
                                <label for="editDesclaimerDesc" class="form-label">Description</label>
                            <QuillEditor required ref="editor" theme="snow" toolbar="full" v-model:content="editDesclaimerData.desc" contentType="html" id="editDesclaimerDesc"/>
                            </div>
                        </div>

                        <div class="mt-3" style="z-index: 999; position: sticky; bottom: 0; background-color: white">
                            <button style="margin-right: 5px;" type="button" class="btn btn-secondary btn-xs"
                                data-bs-dismiss="modal" @click="resetValues">Close</button>
                            <button type="submit" class="btn btn-primary btn-xs">Save Changes</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <!--Modal for Editing Disclaimer End-->

    <!--Table Start-->
    <div class="card" style="margin-top: 2rem; padding: 5px;">
          <div class="card-header pb-0">
            <h6>Disclaimer Templates</h6>
          </div>
          <div class="card-body px-0 pt-0 pb-2">
            <div class="table-responsive p-0">
              <table class="table align-items-center mb-0">
                <thead style="position: sticky; top: 0; background-color: white; z-index: 2;">
                  <tr>
                    <th style="color: #344767 !important;"
                      class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold">S.NO.</th>
                      <th style="color: #344767 !important;"
                      class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold">TItle</th>
                      <th style="color: #344767 !important;"
                      class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold">DESCRIPTION</th>
                    <th style="color: #344767 !important;"
                      class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold action-head">
                      Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="tableRow" v-for="(status,index) in desclaimerStatus" :key="status.id">
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-left">
                        <h6 class="mb-0 text-sm">{{ (currentPage - 1) * itemsPerPage + index + 1 }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-left">
                        <h6 class="mb-0 text-sm">{{ status.title }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-left">
                        <h6 class="mb-0 text-sm">{{ truncatedDesc(status.desc) }}</h6>
                      </div>
                    </td>
                    <td class="align-middle d-md-table-cell actions">
                      <i title="Edit Disclaimer" class="fas fa-pencil-alt text-primary mx-3 icon"
                        style="margin-left: 20px; cursor: pointer;" data-bs-toggle="modal" data-bs-target="#editDisclaimerModal" @click="editDesclaimer(status)"></i>
                      <i title="Delete Disclaimer" data-bs-toggle="modal" data-bs-target="#" @click="deleteDisclaimer(status.id)"
                        class="fas fa-trash text-danger m-3 mx-3 icon" style="cursor: pointer;"></i>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <PaginationComponent v-if="allDisclaimer.length > itemsPerPage" :currentPage="currentPage"
            :itemsPerPage="itemsPerPage" :prevPage="prevPage" :nextPage="nextPage"
            :goToPage="goToPage" />
        </div>
    <!--Table End-->
</template>

<script>
import { BASE_URL } from '../config/apiConfig';
import { QuillEditor } from '@vueup/vue-quill';
import axios from 'axios';
import { mapState } from 'vuex';
import Noty from 'noty';
import Swal from 'sweetalert2';
import PaginationComponent from './Paginator/PaginatorComponent.vue';

    export default{
        name: "Disclaimer",
        components: {
        QuillEditor,
        PaginationComponent
    },
    data(){
        return{
            currentPage: 1,
            itemsPerPage: 10,
            allDisclaimer: [],
            newDesclaimerTitle:'',
            newDesclaimerDesc:'',
            desclaimerStatus: [],
            selectedDesclaimer: '',
            editDesclaimerData: {
                id: '',
                title: '',
                desc: '',
            },
        }
    },
    computed: {
        ...mapState(['authUser', 'authToken']),
        paginatedProjects() {
            const startIndex = (this.currentPage - 1) * this.itemsPerPage;
            return this.filteredProjects.slice(startIndex, startIndex + this.itemsPerPage);
        },
        truncatedDesc() {
            return (desc) => desc.length > 15 ? desc.substring(0, 15) + '...' : desc;
        }
    },
    methods:{
        nextPage() {
        if (this.currentPage * this.itemsPerPage < this.allDisclaimer.length) {
            this.currentPage++;
            this.updateDisplayedDisclaimers();
        }
        },
        prevPage() {
        if (this.currentPage > 1) {
            this.currentPage--;
            this.updateDisplayedDisclaimers();
        }
        },
        goToPage(page) {
            this.currentPage = page;
            this.updateDisplayedDisclaimers();
        },
        updateDisplayedDisclaimers() {
            const startIndex = (this.currentPage - 1) * this.itemsPerPage;
            this.desclaimerStatus = this.allDisclaimer.slice(startIndex, startIndex + this.itemsPerPage);
        },
        addDesclaimer(e) {
            e.preventDefault()
            try {
                this.$store.commit("showLoader")
                axios.post(`${BASE_URL}/api/development/proposal/disclaimer`, {
                    title: this.newDesclaimerTitle,
                    desc: this.newDesclaimerDesc
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
                        this.newDesclaimerTitle=''
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
        getDesclaimerStatus() {
            try {
                axios.get(`${BASE_URL}/api/development/proposal/disclaimer`, {
                    headers: {
                        "token": this.authToken
                    }
                }).then((res) => {
                    this.desclaimerStatus = res.data.data;
                    console.log(this.desclaimerStatus);
                    this.allDisclaimer = res.data.data;
                    this.updateDisplayedDisclaimers();

                })
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 500,
                }).show()
            }
        },
        async deleteDisclaimer(id) {
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
                        const response = await axios.delete(`${BASE_URL}api/development/proposal/disclaimer?id=${id}`, {
                            headers: {
                                token: this.authToken
                            }
                        })
                        if (response.status === 204) {
                            Swal.fire('Deleted!', response.data.message, 'success');
                            window.location.reload()
                        }
                        this.getDesclaimerStatus();
                    } catch (error) {
                        this.getDesclaimerStatus();
                        Swal.fire('Error!', error.response.data.message ? error.response.data.message : error.response.data.detail, 'error');
                    }
                }
            });
        },
        editDesclaimer(status) {
            this.editDesclaimerData = {
                id: status.id,
                title: status.title,
                desc: status.desc
            };
        },
        async updateDisclaimer(e) {
            e.preventDefault();
            try {
                const response = await axios.put(`${BASE_URL}/api/development/proposal/disclaimer`, this.editDesclaimerData, {
                    headers: {
                        'Content-Type': "application/json",
                        token: this.authToken
                    },
                });

                if (response.status === 200) {
                    new Noty({
                        "type": "success",
                        "text": response.data.message,
                        "timeout": 2000
                    }).show();
                    this.getDesclaimerStatus();
                    this.resetValues();
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show();
            }
        },
        resetValues() {
            window.location.reload()
        },
    },
    mounted() {
        this.getDesclaimerStatus()
    }
    };
</script>
