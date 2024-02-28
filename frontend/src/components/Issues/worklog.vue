<template>
    <head>
        <!-- Include necessary CSS files -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
    </head>
    <!-- Modal for Work log -->
    <div class="modal fade" ref="createProjectModal" id="worklog" tabindex="-1" aria-labelledby="createProjectLabel"
        aria-hidden="true" role="dialog" data-backdrop="false">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="createProjectLabel">Work Logs</h5>
                    <button ref="closeModal" type="button" class="btn-close bg-dark text-xs" data-bs-dismiss="modal"
                        aria-label="Close"></button>
                </div>
                <div class="modal-body modalBody">
                    <form @submit="postLogs($event)">
                        <div class="row">
                            <div class="col-md-12 mb-3">
                                <label for="expected time" class="form-label">Add Log Time</label>
                                <input placeholder="Please use format: 4h 20m 45s ('hh mm ss')" required type="text" class="form-control" v-model="logTime"
                                    @change="checkDurationValidity">
                            </div>
                            <div class="col-md-12 mb-3">
                                <label class="form-label">Add Files</label>
                                <input type="file" accept=".xlsx, .xlx, .pdf, .doc, .ppt" class="form-control" multiple
                                    @change="handleFileChange">
                            </div>
                            <div class="col-md-12 mb-3" style="height: auto; overflow: auto;">
                                <label for="description" class="form-label">Description</label>
                                <QuillEditor ref="editor" :modules="modules" theme="snow" toolbar="full" />
                            </div>
                            <div></div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <button type="submit" class="btn btn-primary">Save</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// import { BASE_URL } from '../../config/apiConfig';
// import axios from 'axios';
// import Noty from 'noty';
// import Swal from 'sweetalert2';
import { mapState } from 'vuex';
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import { QuillEditor } from '@vueup/vue-quill';
export default {
    name: 'Worklog',
    components: {
        QuillEditor,
    },
    data() {
        return {
            isCommentFocused: false,
            sprintID: '',
            issueID: '',
            logTime: '',
            selectedFiles: []
        }
    },
    computed: {
        ...mapState(['authToken', 'authUser'])
    },
    methods: {
        checkDurationValidity() {
            if (this.logTime) {
                const durationRegex = /^(?:(\d{1,2})h\s*)?(?:(\d{1,2})m\s*)?(?:(\d{1,2})s\s*)?$/;
                const match = this.logTime.match(durationRegex);

                if (!match) {
                    alert("Invalid duration format. Please use the format like '7h 20m 30s'.");
                    this.logTime = '';
                    return;
                }
                const hours = parseInt(match[1]) || 0;
                const minutes = parseInt(match[2]) || 0;
                const seconds = parseInt(match[3]) || 0;

                const formattedMinutes = minutes > 0 ? `${minutes}m` : "0m";
                const formattedSeconds = seconds > 0 ? `${seconds}s` : "0s";
                const formattedDuration = `${hours}h ${formattedMinutes} ${formattedSeconds}`;
                this.logTime = formattedDuration;

                if (hours > 23 || minutes > 59 || seconds > 59) {
                    alert("Invalid time values. Hours should be between 0 and 23, and minutes/seconds should be between 0 and 59.");
                    this.logTime = '';
                    return;
                }
            }
        },
        handleFileChange(e) {
            this.selectedFiles = e.target.files
        },
        postLogs(e){
            e.preventDefault()
        }
        // getDataFromIssuePage(issueID, sprintID) {
        //     this.sprintID = sprintID
        //     this.issueID = issueID
        // },
        // handleKeyDown(e) {
        //     if (e.key === 'C' && !this.isCommentFocused) {
        //         e.preventDefault()
        //         this.$refs.doComment.focus()
        //     }
        // },
        // handleFileChange(e) {
        //     this.selectedFiles = e.target.files
        // },
        // async postComment() {
        //     if (!this.commentDesc) {
        //         new Noty({
        //             type: 'error',
        //             text: "Comment input field is required!!",
        //             timeout: 500,
        //         }).show()
        //         return
        //     }
        //     try {
        //         this.$store.commit('showLoader');
        //         const formData = new FormData()
        //         formData.append('desc', this.commentDesc)
        //         formData.append('key', this.filterKey)
        //         if (this.filterKey == 'client') {
        //             formData.append('sprintID', this.sprintID)
        //         }
        //         if (this.filterKey == 'developers') {
        //             formData.append('issueID', this.issueID)
        //         }
        //         if (this.selectedFiles.length) {
        //             for (let i = 0; i < this.selectedFiles.length; i++) {
        //                 formData.append('attachments', this.selectedFiles[i])
        //             }
        //         }
        //         const response = await axios.post(`${BASE_URL}api/development/comments`, formData, {
        //             headers: {
        //                 'Content-Type': "multipart/form-data",
        //                 token: this.authToken,
        //             }
        //         });
        //         if (response.status === 201) {
        //             this.resetValues()
        //             // this.$refs.closeModal.click()
        //             Swal.fire({
        //                 title: response.data.message,
        //                 icon: 'success',
        //             })
        //             this.getComments(this.filterKey)
        //         }
        //         this.$store.commit('hideLoader');
        //     } catch (error) {
        //         new Noty({
        //             type: 'error',
        //             text: error.response.data.detail,
        //             timeout: 500,
        //         }).show()
        //         this.$store.commit('hideLoader');
        //     }
        // },
        // async getComments(filterKey) {
        //     this.filterKey = filterKey
        //     try {
        //         if (this.filterKey == 'client') {
        //             this.$store.commit('showLoader');
        //             const response = await axios.get(`${BASE_URL}api/development/comments?sprintID=${this.sprintID}&key=${this.filterKey}`, {
        //                 headers: {
        //                     'Content-Type': "multipart/form-data",
        //                     token: this.authToken,
        //                 }
        //             });
        //             this.comments = response.data.comments
        //         }
        //         if (this.filterKey == 'developers') {
        //             this.$store.commit('showLoader');
        //             const response = await axios.get(`${BASE_URL}api/development/comments?issueID=${this.issueID}&key=${this.filterKey}`, {
        //                 headers: {
        //                     'Content-Type': "multipart/form-data",
        //                     token: this.authToken,
        //                 }
        //             });
        //             this.comments = response.data.comments
        //         }
        //         console.log('comments', this.comments)
        //         if (!this.comments.length) {
        //             new Noty({
        //                 type: 'warning',
        //                 text: "No comments found!!",
        //                 timeout: 500,
        //             }).show()
        //             this.$store.commit('hideLoader');
        //         }
        //         this.$store.commit('hideLoader');
        //     } catch (error) {
        //         new Noty({
        //             type: 'error',
        //             text: error.response.data.detail,
        //             timeout: 500,
        //         }).show()
        //         this.$store.commit('hideLoader');
        //     }
        // },
        // async editComment(comment) {
        //     try {
        //         this.$store.commit('showLoader');
        //         const formData = new FormData();
        //         if (this.selectedFiles.length) {
        //             for (let i = 0; i < this.selectedFiles.length; i++) {
        //                 formData.append('attachments', this.selectedFiles[i])
        //             }
        //         }
        //         formData.append('desc', comment.description)
        //         formData.append('commentID', comment.commentID)
        //         const response = await axios.put(`${BASE_URL}api/development/comments`, formData, {
        //             headers: {
        //                 'Content-Type': "multipart/form-data",
        //                 token: this.authToken,
        //             }
        //         });
        //         if (response.status == 200) {
        //             comment.editMode = !comment.editMode
        //             Swal.fire({
        //                 title: response.data.message,
        //                 icon: 'success',
        //             })
        //             this.getComments(this.filterKey)
        //         }
        //         this.$store.commit('hideLoader');
        //     }
        //     catch (error) {
        //         new Noty({
        //             type: 'error',
        //             text: error.response.data.detail,
        //             timeout: 500,
        //         }).show()
        //         this.$store.commit('hideLoader');
        //     }
        // },
        // async deleteComment(commentID) {
        //     try {
        //         this.$store.commit('showLoader');
        //         const response = await axios.delete(`${BASE_URL}api/development/comments?commentID=${commentID}`, {
        //             headers: {
        //                 token: this.authToken,
        //             }
        //         });
        //         if (response.status == 200) {
        //             Swal.fire({
        //                 title: response.data.message,
        //                 icon: 'success',
        //             })
        //             this.getComments(this.filterKey)
        //         }
        //         this.$store.commit('hideLoader');
        //     } catch (error) {
        //         new Noty({
        //             type: 'error',
        //             text: error.response.data.detail,
        //             timeout: 500,
        //         }).show()
        //         this.$store.commit('hideLoader');
        //     }
        // },
        // extractFilename(response) {
        //     const contentDisposition = response.headers['content-disposition'];
        //     if (contentDisposition) {
        //         const filenameMatch = contentDisposition.match(/filename=([^;]+)/);
        //         return filenameMatch ? filenameMatch[1] : 'download.zip';
        //     } else {
        //         return 'download.zip';
        //     }
        // },
        // async downloadCommentAttachments(e, commentID){
        //     e.preventDefault();
        //     try {
        //         const response = await axios.get(`${BASE_URL}api/development/comments/download?commentID=${commentID}`, {
        //             headers: {
        //                 token: this.authToken
        //             },
        //             responseType: 'arraybuffer',
        //         });
        //         if (response && response.status === 200 && response.data) {
        //             console.log(response, '-----------downlaod Response--------------')
        //             const filename = this.extractFilename(response);
        //             const blob = new Blob([response.data], { type: 'application/zip' });

        //             const link = document.createElement('a');
        //             link.href = window.URL.createObjectURL(blob);
        //             link.download = filename;

        //             document.body.appendChild(link);
        //             link.click();
        //             document.body.removeChild(link);

        //             Swal.fire({
        //                 title: `Downloaded successfully!`,
        //                 icon: 'success',
        //             });
        //         }
        //     } catch (error) {
        //         new Noty({
        //             text: 'An error occurred',
        //             timeout: 500,
        //         }).show();
        //     }
        // },
        // commentToggler(comment) {
        //     comment.editMode = !comment.editMode
        // },
        // resetValues() {
        //     this.isCommentFocused = false
        //     this.selectedFiles = []
        //     this.commentDesc = ''
        // }
    },
    // mounted() {
    //     document.addEventListener('keydown', this.handleKeyDown)
    // }
}
</script>

<style scoped>
/* ::v-deep .ql-container {
    max-height: 500px;
} */

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