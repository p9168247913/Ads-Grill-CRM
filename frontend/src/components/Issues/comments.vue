<template>

    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
    </head>
    <!-- Modal for Create Comments -->
    <div data-bs-backdrop="static" class="modal fade" ref="createProjectModal" id="comments" tabindex="-1"
        aria-labelledby="createProjectLabel" aria-hidden="true" role="dialog" data-backdrop="false">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="createProjectLabel">Comments</h5>
                    <button @click="comments = [], resetValues(), filterKey = ''" ref="closeModal" type="button"
                        class="btn-close bg-dark text-xs" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body modalBody">
                    <div>
                        <ul class="nav nav-tabs" id="myTab" role="tablist">
                            <li class="nav-item" role="presentation">
                                <button
                                    v-if="authUser.role == 'development' && authUser.designation == 'project_manager' | authUser.role == 'client'"
                                    @click="getComments('client'), resetValues()" class="nav-link" id="list1-tab"
                                    data-bs-toggle="tab" data-bs-target="#filteredCommentsClient" type="button"
                                    role="tab" aria-controls="list1" aria-selected="true"
                                    title="click me">Client</button>
                            </li>
                            <li class="nav-item" role="presentation">
                                <button @click="getComments('developers'), resetValues()" class="nav-link"
                                    id="list2-tab" data-bs-toggle="tab" data-bs-target="#filteredCommentsClient"
                                    type="button" role="tab" aria-controls="list2" aria-selected="false"
                                    title="click me">Development</button>
                            </li>
                        </ul>
                    </div>
                    <div class="tab-content" id="myTabContent">
                        <div class="tab-pane fade" id="filteredCommentsClient" role="tabpanel"
                            aria-labelledby="list2-tab">
                            <!-- Content for List 1 -->
                            <div v-if="filterKey" class="row mt-3">
                                <!-- <button>open</button> -->
                                <div class="col-md-10 mb-3">
                                    <textarea v-model="commentDesc" ref="doComment" @input="checkMail()"
                                        style="height: 40px; resize: none; max-height: auto;"
                                        placeholder=" Add Comments..." type="text" class="form-control"
                                        required></textarea>
                                    <div class="col-md-4">
                                        <ul v-if="showEmailSelector" name="emailSelector" id="emailSelector">
                                            <li @click="selectEmail(item.email)" v-for="item in devUsers" :key="item.id"
                                                :value="item.email">{{ item.email }}</li>
                                        </ul>
                                    </div>
                                </div>

                                <div class="col-md-2 mb-1">
                                    <input @change="handlePostFileChange($event)" id="fileInput1" type="file" multiple
                                        accept=".xlsx, .xls, .doc, .ppt, .pdf, .png, .jpeg, .jpg"
                                        class="form-control w-auto d-none">
                                    <label for="fileInput1"
                                        class="text-xs rounded border border-1 border-dark font-weight-bold cursor-pointer"
                                        title="Attach" style="padding:11px;">Attach</label>
                                    <p v-if="this.postselectedFiles.length > 0" class="text-xs" style="margin-left: 5px;">
                                        {{ `${this.postselectedFiles.length} file selected` }}</p>
                                </div>
                                <!-- <div v-if="!isCommentFocused" style="margin-top: -8px;">
                                    <p class="text-xs"><span class="font-weight-bold text-dark">Pro tip:</span> Press
                                        <span class="font-weight-bold text-dark">C</span> to comment
                                    </p>
                                </div> -->
                            </div>
                            <div v-if="filterKey" class="row" style="margin-top: -15px;">
                                <div style="margin-right: -12px;" class="col-sm-1 col-lg-1 col-md-1">
                                    <p @click="postComment()" class="cursor-pointer ms-1 text-sm font-weight-bold icon">
                                        Save
                                    </p>
                                </div>
                                <div class="col-sm-1 col-lg-1 col-md-1" style="margin-left: 10px;">
                                    <p @click="isCommentFocused = false, resetValues()"
                                        class="cursor-pointer ms-1 text-sm font-weight-bold icon">
                                        Cancel</p>
                                </div>
                            </div>
                            <div v-if="comments.length" class="mt-3 overflow-y-auto pt-2" style="max-height: 200px;">
                                <div v-for="(comment, index) in comments" :key="index">
                                    <div class="d-flex flex-row text text-dark">
                                        <span
                                            style="border-radius: 50%; margin-top:-4px; width:30px; height:30px; text-align: center;  background-color:lightgray;"
                                            class="small font-weight-bold me-2 pt-1">
                                            {{ comment.author.name.charAt(0).toUpperCase() }}
                                        </span>
                                        <p class="pe-2 small font-weight-bold">{{ comment.author.name }}</p>
                                        <p class="small">Posted {{ formatDateTime(comment.created_at) }}</p>
                                        <a v-if="comment.attachments.length"
                                            @click="downloadCommentAttachments($event, comment.commentID)">
                                            <i class="fas fa-download ms-3 cursor-pointer"
                                                title="download attachments"></i>
                                        </a>
                                    </div>
                                    <div class="d-flex flex-column" style="margin-left: 40px;">
                                        <div v-if="!comment.editMode" class="d-flex flex-column"
                                            style="margin-top: -5px;">
                                            <p class="small">{{ comment.description }}</p>
                                        </div>
                                        <div v-if="comment.editMode" class="d-flex flex-row">
                                            <textarea @keyup.enter="editComment(comment,)" type="text"
                                                placeholder="Edit Comment..." v-model="comment.description"
                                                class="form-control small w-50 me-3"
                                                style="height:40px; resize: none;"></textarea>

                                            <input @change="handleEditFileChange($event)" id="fileInput2" type="file"
                                                multiple accept=".xlsx, .xls, .doc, .ppt, .pdf, .png, .jpeg, .jpg"
                                                class="form-control w-auto d-none">
                                            <label for="fileInput2"
                                                class="text-xs rounded border border-1 border-dark font-weight-bold me-2"
                                                title="Add files" style="padding:11px">Add Files</label>
                                            <p v-if="this.editselectedFiles.length > 0" class="text-xs">{{
                                                `${this.editselectedFiles.length} file selected` }}</p>
                                        </div>
                                        <div v-if="comment.editMode" class="d-flex flex-row gap-4">
                                            <p @click="editComment(comment)"
                                                class="small me-2 cursor-pointer font-weight-bold icon">Save</p>
                                            <p @click="commentToggler(comment)"
                                                class="small cursor-pointer font-weight-bold icon">Cancel</p>
                                        </div>
                                    </div>
                                    <div v-if="!comment.editMode" class="d-flex flex-row gap-4"
                                        style="margin-left:40px; margin-top: -10px;">
                                        <p @click="commentToggler(comment)"
                                            class="text-sm me-2 font-weight-bold cursor-pointer icon">Edit</p>
                                        <p @click="deleteComment(comment.commentID)"
                                            class="text-sm font-weight-bold cursor-pointer icon">Delete</p>
                                    </div>
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
import { BASE_URL } from '../../config/apiConfig';
import axios from 'axios';
import Noty from 'noty';
import Swal from 'sweetalert2';
import { mapState } from 'vuex';
import '@vueup/vue-quill/dist/vue-quill.snow.css';
export default {
    name: 'Comments',
    data() {
        return {
            isCommentFocused: false,
            sprintID: '',
            issueID: '',
            commentDesc: '',
            comments: [],
            filterKey: '',
            postselectedFiles: [],
            editselectedFiles: [],
            showModal: false,
            devUsers: [],
            showEmailSelector: false
        }
    },
    computed: {
        ...mapState(['authToken', 'authUser'])
    },
    methods: {
        formatDateTime(dateTimeString) {
            const date = new Date(dateTimeString);

            const options = {
                year: 'numeric',
                month: 'long',
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit',
                hour12: false,
                timeZone: 'Asia/Kolkata'
            };

            return new Intl.DateTimeFormat('en-US', options).format(date);
        },
        getDataFromIssuePage(issueID, sprintID) {
            this.sprintID = sprintID
            this.issueID = issueID
        },
        getDevUsersFromIssuePage(devUsers) {
            this.devUsers = devUsers
        },
        // handleKeyDown(e) {
        //     if (e.key === 'C' && !this.isCommentFocused) {
        //         e.preventDefault()
        //         this.$refs.doComment.focus()
        //     }
        // },
        handlePostFileChange(e) {
            this.postselectedFiles = e.target.files
        },
        handleEditFileChange(e) {
            this.editselectedFiles = e.target.files
        },
        async postComment() {
            if (!this.commentDesc) {
                new Noty({
                    type: 'error',
                    text: "Comment input field is required!!",
                    timeout: 1000,
                }).show()
                return
            }
            try {
                this.$store.commit('showLoader');
                const formData = new FormData()
                formData.append('desc', this.commentDesc)
                formData.append('key', this.filterKey)
                if (this.filterKey == 'client') {
                    formData.append('sprintID', this.sprintID)
                }
                if (this.filterKey == 'developers') {
                    formData.append('issueID', this.issueID)
                }
                if (this.postselectedFiles.length) {
                    for (let i = 0; i < this.postselectedFiles.length; i++) {
                        formData.append('attachments', this.postselectedFiles[i])
                    }
                }
                const response = await axios.post(`${BASE_URL}api/development/comments`, formData, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                        token: this.authToken,
                    }
                });
                if (response.status === 201) {
                    this.resetValues()
                    Swal.fire({
                        title: response.data.message,
                        icon: 'success',
                    })
                    this.getComments(this.filterKey)
                }
                this.$store.commit('hideLoader');
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show()
                this.$store.commit('hideLoader');
            }
        },
        async getComments(filterKey) {
            this.filterKey = filterKey
            try {
                if (this.filterKey == 'client') {
                    this.$store.commit('showLoader');
                    const response = await axios.get(`${BASE_URL}api/development/comments?sprintID=${this.sprintID}&key=${this.filterKey}`, {
                        headers: {
                            'Content-Type': "multipart/form-data",
                            token: this.authToken,
                        }
                    });
                    this.comments = response.data.comments
                }
                if (this.filterKey == 'developers') {
                    this.$store.commit('showLoader');
                    const response = await axios.get(`${BASE_URL}api/development/comments?issueID=${this.issueID}&key=${this.filterKey}`, {
                        headers: {
                            'Content-Type': "multipart/form-data",
                            token: this.authToken,
                        }
                    });
                    this.comments = response.data.comments
                }
                if (!this.comments.length) {
                    new Noty({
                        type: 'warning',
                        text: "No comments found!!",
                        timeout: 1000,
                    }).show()
                    this.$store.commit('hideLoader');
                }
                this.$store.commit('hideLoader');
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show()
                this.$store.commit('hideLoader');
            }
        },
        async editComment(comment) {
            try {
                this.$store.commit('showLoader');
                const formData = new FormData();
                if (this.editselectedFiles.length) {
                    for (let i = 0; i < this.editselectedFiles.length; i++) {
                        formData.append('attachments', this.editselectedFiles[i])
                    }
                }
                formData.append('desc', comment.description)
                formData.append('commentID', comment.commentID)
                const response = await axios.put(`${BASE_URL}api/development/comments`, formData, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                        token: this.authToken,
                    }
                });
                if (response.status == 200) {
                    comment.editMode = !comment.editMode
                    Swal.fire({
                        title: response.data.message,
                        icon: 'success',
                    })
                    this.getComments(this.filterKey)
                }
                this.$store.commit('hideLoader');
            }
            catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show()
                this.$store.commit('hideLoader');
            }
        },
        async deleteComment(commentID) {
            try {
                this.$store.commit('showLoader');
                const response = await axios.delete(`${BASE_URL}api/development/comments?commentID=${commentID}`, {
                    headers: {
                        token: this.authToken,
                    }
                });
                if (response.status == 200) {
                    Swal.fire({
                        title: response.data.message,
                        icon: 'success',
                    })
                    this.getComments(this.filterKey)
                }
                this.$store.commit('hideLoader');
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show()
                this.$store.commit('hideLoader');
            }
        },
        extractFilename(response) {
            const contentDisposition = response.headers['content-disposition'];
            if (contentDisposition) {
                const filenameMatch = contentDisposition.match(/filename=([^;]+)/);
                return filenameMatch ? filenameMatch[1] : 'download.zip';
            } else {
                return 'download.zip';
            }
        },
        async downloadCommentAttachments(e, commentID) {
            e.preventDefault();
            try {
                const response = await axios.get(`${BASE_URL}api/development/comments/download?commentID=${commentID}`, {
                    headers: {
                        token: this.authToken
                    },
                    responseType: 'arraybuffer',
                });
                if (response && response.status === 200 && response.data) {
                    const filename = this.extractFilename(response);
                    const blob = new Blob([response.data], { type: 'application/zip' });

                    const link = document.createElement('a');
                    link.href = window.URL.createObjectURL(blob);
                    link.download = filename;

                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);

                    Swal.fire({
                        title: `Downloaded successfully!`,
                        icon: 'success',
                    });
                }
            } catch (error) {
                new Noty({
                    type: "error",
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show();
            }
        },
        commentToggler(comment) {
            comment.editMode = !comment.editMode
        },
        resetValues() {
            this.isCommentFocused = false
            this.postselectedFiles = []
            this.editselectedFiles = []
            this.commentDesc = ''
            this.showEmailSelector = false
        },
        async getDevUsers() {
            try {
                const response = await axios.get(`${BASE_URL}api/users/?role=development`, {
                    headers: {
                        token: this.authToken
                    },
                });
                if (response && response.status === 200 && response.data) {
                    this.devUsers = response.data.users
                }
            } catch (error) {
                new Noty({
                    type: "error",
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show();
            }
        },
        checkMail() {
            let value = this.commentDesc;
            if (value.slice(-1) == '@') {
                this.showEmailSelector = true;
            }
            else {
                this.showEmailSelector = false;
            }
        },
        selectEmail(email) {
            let content = this.commentDesc
            content = content.slice(0, -1) + ' ' + email + " "
            this.commentDesc = content
            this.showEmailSelector = false
            this.$refs.doComment.focus()
        }
    },
    mounted() {
        document.addEventListener('keydown', this.handleKeyDown)
    }
}
</script>

<style scoped>
::v-deep .ql-container {
    max-height: 500px;
}

::v-deep .ql-editor img {
    width: 150px;
    height: auto;
    margin: 5px;
    border-radius: 8px;
    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
}

::v-deep .ql-editor {
    height: auto;
    max-height: 500px;
    overflow-y: auto;
    color: black;
}

::v-deep .ql-tooltip {
    position: fixed;
    left: 50% !important;
    transform: translateX(-50%) !important;
    max-height: 500px;
    overflow-y: auto;
    z-index: 99;
}

::v-deep .ql-editor img {
    width: 200px;
    height: auto;
    margin: 5px;
    border-radius: 8px;
    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
    transition: transform 0.3s ease-in-out;
}

::v-deep .ql-editor img:hover {
    transform: scale(2.5);
    /* Adjust the scale factor as needed */
}

.icon:hover {
    transform: scale(1.1);
}

.modalBody {
    max-height: calc(100vh - 200px);
    overflow: auto;
}

@media (max-width: 576px) {
    .modal-dialog {
        max-width: 99%;
        margin: auto;
    }
}

@media (min-width: 577px) and (max-width: 992px) {
    .modal-dialog {
        max-width: 80%;
        margin: auto;
    }
}

@media (min-width: 993px) {
    .modal-dialog {
        max-width: 50%;
        margin: auto;
    }
}
</style>