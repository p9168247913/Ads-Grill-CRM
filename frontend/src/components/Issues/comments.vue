<template>
    <head>
        <!-- Include necessary CSS files -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
    </head>
    <!-- Modal for Create Issue -->
    <div class="modal fade" ref="createProjectModal" id="comments" tabindex="-1" aria-labelledby="createProjectLabel"
        aria-hidden="true" role="dialog" data-backdrop="false">
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
                                    data-bs-toggle="tab" data-bs-target="#filteredCommentsClient" type="button" role="tab"
                                    aria-controls="list1" aria-selected="true" title="click me">Client</button>
                            </li>
                            <li class="nav-item" role="presentation">
                                <button @click="getComments('developers'), resetValues()" class="nav-link" id="list2-tab"
                                    data-bs-toggle="tab" data-bs-target="#filteredCommentsClient" type="button" role="tab"
                                    aria-controls="list2" aria-selected="false" title="click me">Development</button>
                            </li>
                        </ul>
                    </div>
                    <div class="tab-content" id="myTabContent">
                        <div class="tab-pane fade" id="filteredCommentsClient" role="tabpanel" aria-labelledby="list2-tab">
                            <!-- Content for List 1 -->
                            <div v-if="filterKey" class="row mt-3">
                                <div class="col-md-10 mb-3">
                                    <textarea v-model="commentDesc" ref="doComment" @focus="isCommentFocused = true"
                                        style="height: 40px; resize: none; max-height: auto;" placeholder=" Add Comments..."
                                        type="text" class="form-control" required></textarea>
                                </div>
                                <div v-if="isCommentFocused" class="col-md-2 mb-3">
                                    <input @change="handleFileChange($event)" id="fileInput1" type="file" multiple
                                        accept=".xlsx, .xls, .doc, .ppt, .pdf, .png, .jpeg, .jpg"
                                        class="form-control w-auto d-none">
                                    <label for="fileInput1"
                                        class="text-xs rounded border border-1 border-dark font-weight-bold cursor-pointer"
                                        title="Attach" style="padding:11px;">Attach</label>
                                </div>
                                <div v-if="!isCommentFocused" style="margin-top: -8px;">
                                    <p class="text-xs"><span class="font-weight-bold text-dark">Pro tip:</span> Press <span
                                            class="font-weight-bold text-dark">C</span> to comment</p>
                                </div>
                            </div>
                            <div v-if="isCommentFocused && filterKey" class="row" style="margin-top: -15px;">
                                <div style="margin-right: -12px;" class="col-sm-1 col-lg-1 col-md-1">
                                    <p @click="postComment()" class="cursor-pointer ms-1 text-sm font-weight-bold">save</p>
                                </div>
                                <div class="col-sm-1 col-lg-1 col-md-1">
                                    <p @click="isCommentFocused = false, resetValues()"
                                        class="cursor-pointer ms-1 text-sm font-weight-bold">
                                        cancel</p>
                                </div>
                            </div>
                            <div v-if="comments.length" class="mt-3 overflow-y-auto pt-2" style="max-height: 200px;">
                                <div v-for="(comment, index) in comments" :key="index">
                                    <div class="d-flex flex-row text text-dark">
                                        <span
                                            style="border-radius: 50%; margin-top:-4px; width:30px; height:30px; text-align: center;  background-color:lightgray;"
                                            class="small font-weight-bold me-2 pt-1">{{
                                                comment.author.name.charAt(0).toUpperCase()
                                            }}</span>
                                        <p class="pe-2 small font-weight-bold">{{ comment.author.name }}</p>
                                        <p class="small">Posted {{ comment.created_at }}</p>
                                        <a v-if="comment.attachments.length"
                                            @click="downloadCommentAttachments($event, comment.commentID)">
                                            <i class="fas fa-download ms-3 cursor-pointer" title="download attachments"></i>
                                        </a>
                                    </div>
                                    <div class="d-flex flex-column" style="margin-left: 40px;">
                                        <div v-if="!comment.editMode" class="d-flex flex-column" style="margin-top: -5px;">
                                            <p class="small">{{ comment.description }}</p>
                                        </div>
                                        <div v-if="comment.editMode" class="d-flex flex-row">
                                            <textarea @keyup.enter="editComment(comment,)" type="text"
                                                placeholder="Edit Comment..." v-model="comment.description"
                                                class="form-control small w-50 me-3"
                                                style="height:40px; resize: none;"></textarea>

                                            <input @change="handleFileChange($event)" id="fileInput2" type="file" multiple
                                                accept=".xlsx, .xls, .doc, .ppt, .pdf, .png, .jpeg, .jpg"
                                                class="form-control w-auto d-none">
                                            <label for="fileInput2"
                                                class="text-xs rounded border border-1 border-dark font-weight-bold me-2"
                                                title="Add files" style="padding:11px">Add Files</label>
                                        </div>
                                        <div v-if="comment.editMode" class="d-flex flex-row">
                                            <p @click="editComment(comment)"
                                                class="small me-2 cursor-pointer font-weight-bold">save</p>
                                            <p @click="commentToggler(comment)"
                                                class="small cursor-pointer font-weight-bold">cancel</p>
                                        </div>
                                    </div>
                                    <div v-if="!comment.editMode" class="d-flex flex-row"
                                        style="margin-left:40px; margin-top: -10px;">
                                        <p @click="commentToggler(comment)"
                                            class="text-sm me-2 font-weight-bold cursor-pointer">Edit</p>
                                        <p @click="deleteComment(comment.commentID)"
                                            class="text-sm font-weight-bold cursor-pointer">Delete</p>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- <div class="tab-pane fade" id="filteredCommentsDevelopers" role="tabpanel" aria-labelledby="list2-tab">
                            Content for List 2
                            <div v-if="filterKey" class="row mt-3">
                                <div class="col-md-10 mb-3">
                                    <input v-model="commentDesc" ref="doComment" @focus="isCommentFocused = true"
                                        style="height: 35px;" placeholder=" Add Comments..." type="text"
                                        class="form-control" required>
                                </div>
                                <div v-if="isCommentFocused" class="col-md-2 mb-3">
                                    <input @change="handleFileChange($event)" id="fileInput1" type="file" multiple
                                        accept=".xlsx, .xls, .doc, .ppt, .pdf, .png, .jpeg, .jpg"
                                        class="form-control w-auto d-none">
                                    <label for="fileInput1"
                                        class="p-2 text-xs rounded border border-1 border-dark font-weight-bold cursor-pointer"
                                        title="Attach">Attach</label>
                                </div>
                                <div v-if="!isCommentFocused" style="margin-top: -8px;">
                                    <p class="text-xs"><span class="font-weight-bold text-dark">Pro tip:</span> Press <span
                                            class="font-weight-bold text-dark">C</span> to comment</p>
                                </div>
                            </div>
                            <div v-if="isCommentFocused && filterKey" class="row" style="margin-top: -15px;">
                                <div style="margin-right: -12px;" class="col-sm-1 col-lg-1 col-md-1">
                                    <p @click="postComment()" class="cursor-pointer ms-1 text-sm font-weight-bold">save</p>
                                </div>
                                <div class="col-sm-1 col-lg-1 col-md-1">
                                    <p @click="isCommentFocused = false, resetValues()"
                                        class="cursor-pointer ms-1 text-sm font-weight-bold">
                                        cancel</p>
                                </div>
                            </div>
                            <div v-if="comments.length" class="mt-3 overflow-y-auto pt-2" style="max-height: 200px;">
                                <div v-for="(comment, index) in comments" :key="index">
                                    <div class="d-flex flex-row text text-dark">
                                        <span
                                            style="border-radius: 50%; margin-top:-4px; width:30px; height:30px; text-align: center;  background-color:lightgray;"
                                            class="small font-weight-bold me-2 pt-1">{{
                                                comment.author.name.charAt(0).toUpperCase()
                                            }}</span>
                                        <p class="pe-2 small font-weight-bold">{{ comment.author.name }}</p>
                                        <p class="small">Posted {{ comment.created_at }}</p>
                                        <a v-if="comment.attachments.length"
                                            @click="downloadCommentAttachments($event, comment.commentID)">
                                            <i class="fas fa-download ms-3 cursor-pointer" title="download attachments"></i>
                                        </a>
                                    </div>
                                    <div class="d-flex flex-column" style="margin-left: 40px;">
                                        <div v-if="!comment.editMode" class="d-flex flex-column" style="margin-top: -5px;">
                                            <p class="small">{{ comment.description }}</p>
                                        </div>
                                        <div v-if="comment.editMode" class="d-flex flex-row">
                                            <input @keyup.enter="editComment(comment,)" type="text"
                                                v-model="comment.description"
                                                class="small w-50 me-2 rounded border border-dark"
                                                style="height:33px; background-color: rgb(247, 249, 250);">
                                            <input @change="handleFileChange($event)" id="fileInput2" type="file" multiple
                                                accept=".xlsx, .xls, .doc, .ppt, .pdf, .png, .jpeg, .jpg"
                                                class="form-control w-auto me-2 d-none">
                                            <label for="fileInput2"
                                                class="p-2 text-xs rounded border border-1 border-dark font-weight-bold me-2"
                                                title="Add files">Add Files</label>
                                        </div>
                                        <div v-if="comment.editMode" class="d-flex flex-row">
                                            <p @click="editComment(comment)"
                                                class="small me-2 cursor-pointer font-weight-bold">save</p>
                                            <p @click="commentToggler(comment)"
                                                class="small cursor-pointer font-weight-bold">cancel</p>
                                        </div>
                                    </div>
                                    <div v-if="!comment.editMode" class="d-flex flex-row"
                                        style="margin-left:40px; margin-top: -10px;">
                                        <p @click="commentToggler(comment)"
                                            class="text-sm me-2 font-weight-bold cursor-pointer">Edit</p>
                                        <p @click="deleteComment(comment.commentID)"
                                            class="text-sm font-weight-bold cursor-pointer">Delete</p>
                                    </div>
                                </div>
                            </div>
                        </div> -->
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
            selectedFiles: []
        }
    },
    computed: {
        ...mapState(['authToken', 'authUser'])
    },
    methods: {
        getDataFromIssuePage(issueID, sprintID) {
            this.sprintID = sprintID
            this.issueID = issueID
        },
        handleKeyDown(e) {
            if (e.key === 'C' && !this.isCommentFocused) {
                e.preventDefault()
                this.$refs.doComment.focus()
            }
        },
        handleFileChange(e) {
            this.selectedFiles = e.target.files
        },
        async postComment() {
            if (!this.commentDesc) {
                new Noty({
                    type: 'error',
                    text: "Comment input field is required!!",
                    timeout: 500,
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
                if (this.selectedFiles.length) {
                    for (let i = 0; i < this.selectedFiles.length; i++) {
                        formData.append('attachments', this.selectedFiles[i])
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
                    // this.$refs.closeModal.click()
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
                    text: error.response.data.detail,
                    timeout: 500,
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
                console.log('comments', this.comments)
                if (!this.comments.length) {
                    new Noty({
                        type: 'warning',
                        text: "No comments found!!",
                        timeout: 500,
                    }).show()
                    this.$store.commit('hideLoader');
                }
                this.$store.commit('hideLoader');
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.detail,
                    timeout: 500,
                }).show()
                this.$store.commit('hideLoader');
            }
        },
        async editComment(comment) {
            try {
                this.$store.commit('showLoader');
                const formData = new FormData();
                if (this.selectedFiles.length) {
                    for (let i = 0; i < this.selectedFiles.length; i++) {
                        formData.append('attachments', this.selectedFiles[i])
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
                    text: error.response.data.detail,
                    timeout: 500,
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
                    text: error.response.data.detail,
                    timeout: 500,
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
                    console.log(response, '-----------downlaod Response--------------')
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
                    text: 'An error occurred',
                    timeout: 500,
                }).show();
            }
        },
        commentToggler(comment) {
            comment.editMode = !comment.editMode
        },
        resetValues() {
            this.isCommentFocused = false
            this.selectedFiles = []
            this.commentDesc = ''
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