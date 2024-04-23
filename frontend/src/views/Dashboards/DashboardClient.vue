<template>

    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Webkit | Responsive Bootstrap 4 Admin Dashboard Template</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
    </head>
    <div class="wrapper" style="margin-bottom: 80px; ">
        <div class="content-page">
            <div class="container-fluid p-0">
                <!--Table-->
                <div class="card"
                    style="margin-top: 2rem; padding: 3px; padding-bottom: 8px; box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset;">
                    <div class="card-header pb-0">
                        <h6>PROJECTS</h6>
                    </div>
                    <div class="card-body px-0 pt-0 pb-1" style="border-top: 1px solid gray;">
                        <div class="table-responsive p-1">
                            <div class="align-items-center p-1 project-card" v-for="(project, index) in allProjects"
                                :key="index">
                                <div class="align-items-center mb-0 sprintRow" @click="toggleDropdown(index)">
                                    <div style="display: flex; gap: 50px; align-items: center; ">
                                        <div class="d-flex flex-row justify-content-center">
                                            <span class="mb-0 text-sm"><i
                                                    class="fa fa-chevron-down drop-icon"></i></span>
                                        </div>
                                        <div class="d-flex flex-row justify-content-center">
                                            <h6 class="mb-0 text-sm">{{ project.name }}</h6>
                                        </div>
                                        <div class="d-flex flex-row justify-content-center">
                                            <h6 class="mb-0 text-sm" style="white-space: nowrap;">{{ project.type }}
                                            </h6>
                                        </div>
                                        <div class="d-flex flex-row justify-content-center ">
                                            <p class="mb-0 text-sm" style="font-size: smaller; white-space: nowrap;">{{
                                                formatDate(project.created_at) }}</p>
                                        </div>
                                        <div class="d-flex flex-row justify-content-center">
                                            <p class="mb-0 text-sm" style="font-size: smaller;white-space: nowrap;">{{
                                                project.status === 'to_do' ? "To Do" : project.status === 'in_progress'
                                                    ?
                                                    'In Progress' : project.status === 'done' ? "Done" : '' }}</p>
                                        </div>
                                        <div class="d-flex flex-row justify-content-center">
                                            <p class="mb-0 text-sm" style="font-size: smaller;white-space: nowrap;">{{
                                                project.reporter.name }}</p>
                                        </div>
                                        <div class="d-flex flex-row justify-content-center">
                                            <p class="mb-0 text-sm" style="font-size: smaller;white-space: nowrap;">{{
                                                project.tech_stacks }}</p>
                                        </div>
                                        <div class="d-flex flex-row justify-content-center">
                                            <p class="mb-0 text-sm" style="font-size: smaller;white-space: nowrap;">{{
                                                project.host_address }}</p>
                                        </div>
                                        <div class="d-flex flex-column justify-content-left" style="padding: 0px 10px;">
                                            <h6 class="mb-0 text-sm">
                                                <argon-progress :percentage="project.progress" color="success"
                                                    style="width: 100px;" />
                                            </h6>
                                        </div>
                                    </div>
                                </div>
                                <div class="sprint-card pt-2">
                                    <div v-show="project.showDropdown">
                                        <table v-if="project.sprints.length" class="table align-items-center mb-0">
                                            <thead>
                                                <div class="mt-1" style="margin-left: 8px;">
                                                    <h6>Sprints</h6>
                                                </div>
                                            </thead>

                                            <tbody>
                                                <tr title="click me to see comments" class="issueRow"
                                                    @click="getComments(sprint.id)"
                                                    v-for="(sprint, sprintIndex) in project.sprints" :key="sprintIndex">
                                                    <td style="padding-left: 25px;">
                                                        <div class="d-flex flex-column justify-content-center">
                                                            <h6 class="mb-0 text-sm">{{ sprintIndex + 1 }}</h6>
                                                        </div>
                                                    </td>

                                                    <td style="padding-left: 25px;">
                                                        <div class="d-flex flex-column justify-content-center">
                                                            <h6 class="mb-0 text-sm">{{
                                                                sprint.name }}</h6>
                                                        </div>
                                                    </td>
                                                    <td style="padding-left: 25px;">
                                                        <div class="d-flex flex-column justify-content-center">
                                                            <h6 class="mb-0 text-sm">{{
                                                                sprint.key }}</h6>
                                                        </div>
                                                    </td>
                                                    <td style="padding-left: 25px;">
                                                        <div class="d-flex flex-column justify-content-center">
                                                            <h6 class="mb-0 text-sm">{{ sprint.status === 'done' ?
                                                                "Done"
                                                                :
                                                                sprint.status === 'in_progress' ? 'In Progress' :
                                                                    sprint.status === 'to_do' ? "To Do" : '' }}</h6>
                                                        </div>
                                                    </td>
                                                    <td style="padding-left: 25px;">
                                                        <div class="d-flex flex-column justify-content-center">
                                                            <h6 class="mb-0 text-sm">{{
                                                                formatDate(sprint.start_date) }}</h6>
                                                        </div>
                                                    </td>
                                                </tr>
                                            </tbody>

                                        </table>
                                        <table v-else>
                                            <tr style="margin: auto;">
                                                <span style="color: rgb(253, 97, 97);">No sprints found!</span>
                                            </tr>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- <div v-else>
                    <p>No sprints found</p>
                </div> -->
            </div>
        </div>

        <!--COMMENT SECTION-->
        <div class="d-flex flex-column justify-content-center mt-4">
            <h5 class="mb-2">Comments</h5>

            <div v-if="sprintId != null" class="d-flex flex-column mb-4">
                <div class="d-flex flex-row">
                    <input ref="doComment" @focus="isCommentFocused = true" v-model="commentDesc"
                        class="small w-50 me-2 rounded border border-dark" type="text" placeholder="Add Comments..."
                        style="height:33px; background-color: rgb(247, 249, 250);">
                    <div v-if="isCommentFocused">
                        <input @change="handleFileChange($event)" id="fileInput1" type="file" multiple
                            accept=".xlsx, .xls, .doc, .ppt, .pdf, .png, .jpeg, .jpg"
                            class="form-control w-auto me-2 d-none">
                        <label for="fileInput1"
                            class="p-2 text-xs rounded border border-1 border-dark font-weight-bold me-2 cursor-pointer"
                            title="Attach">Attach</label>
                    </div>
                </div>
                <p v-if="!isCommentFocused" class="text-xs mt-1"><span class="font-weight-bold text-dark">Pro tip:
                    </span>Press <span class="font-weight-bold text-dark">C</span> to comment</p>
                <div v-if="isCommentFocused" class="d-flex flex-row">
                    <p v-if="commentDesc" @click="postComment()" class="small me-2 cursor-pointer font-weight-bold">Save
                    </p>
                    <p v-else style="cursor:not-allowed" title="Please enter comment"
                        class="small me-2 cursor-pointer font-weight-bold">save</p>
                    <p @click="isCommentFocused = false" class="small cursor-pointer font-weight-bold">Cancel</p>
                </div>
            </div>
            <div v-else class="small text-danger">Please click on a particular sprint to see and post comments!!</div>
            <div v-if="comments.length">
                <div v-for="(comment, index) in comments" :key="index">
                    <div class="d-flex flex-row text text-dark">
                        <span
                            style="border-radius: 50%; margin-top:-4px; width:30px; height:30px; text-align: center;  background-color:lightgray;"
                            class="small font-weight-bold me-2 pt-1">{{ comment.author.name.charAt(0).toUpperCase()
                            }}</span>
                        <p class="pe-2 small font-weight-bold">{{ comment.author.name }}</p>
                        <p class="small">Posted {{ formatDateTime(comment.created_at) }}</p>
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
                            <input @keyup.enter="editComment(comment, comment.sprintID)" type="text"
                                v-model="comment.description" class="small w-50 me-2 rounded border border-dark"
                                style="height:33px; background-color: rgb(247, 249, 250);">
                            <input @change="handleFileChange($event)" id="fileInput2" type="file" multiple
                                accept=".xlsx, .xls, .doc, .ppt, .pdf, .png, .jpeg, .jpg"
                                class="form-control w-auto me-2 d-none">
                            <label for="fileInput2"
                                class="p-2 text-xs rounded border border-1 border-dark font-weight-bold me-2"
                                title="Add files">Add Files</label>
                        </div>
                        <div v-if="comment.editMode" class="d-flex flex-row">
                            <p @click="editComment(comment, comment.sprintID)"
                                class="small me-2 cursor-pointer font-weight-bold">Save</p>
                            <p @click="commentToggler(comment)" class="small cursor-pointer font-weight-bold">Cancel</p>
                        </div>
                    </div>
                    <div v-if="!comment.editMode" class="d-flex flex-row mb-4"
                        style="margin-left:40px; margin-top: -10px;">
                        <p @click="commentToggler(comment)" class="text-sm me-2 font-weight-bold cursor-pointer">Edit
                        </p>
                        <p @click="deleteComment(comment.commentID, comment.sprintID)"
                            class="text-sm font-weight-bold cursor-pointer">Delete</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import ArgonProgress from '../../components/ArgonProgress.vue'
import { BASE_URL } from '../../config/apiConfig';
import axios from 'axios';
import Noty from 'noty';
import Swal from 'sweetalert2';
import { mapState } from 'vuex'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import '@popperjs/core/dist/umd/popper.min.js';
import Popper from 'popper.js';
window.Popper = Popper;
export default {
    name: "dashboardClient",
    data() {
        return {
            allProjects: [],
            comments: [],
            selectedFiles: [],
            isCommentFocused: false,
            sprintId: null,
            commentDesc: ''
        };
    },
    components: {
        ArgonProgress
    },
    computed: {
        ...mapState(['authUser', 'authToken']),
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
        formatDate(dateString) {
            const options = { day: 'numeric', month: 'short', year: 'numeric' };
            const date = new Date(dateString);
            return date.toLocaleDateString('en-US', options);
        },
        removeModalBackdrop() {
            const modalBackdrop = document.getElementsByClassName('modal-backdrop');
            if (modalBackdrop.length > 0) {
                document.body.classList.remove('modal-open');
                document.body.removeChild(modalBackdrop[0]);
            }
        },
        toggleDropdown(index) {
            this.allProjects[index].showDropdown = !this.allProjects[index].showDropdown;
        },
        async getAllProjects() {
            try {
                this.$store.commit('showLoader');
                const response = await axios.get(`${BASE_URL}api/development/projects?key=client&clientID=${this.authUser.id}`, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                        token: this.authToken,
                    }
                });
                if (response.status === 200) {
                    this.allProjects = response.data.projects
                }
                this.$store.commit('hideLoader');
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.detail ? error.response.data.detail : error.response.data.message,
                    timeout: 1000,
                }).show()
                this.$store.commit('hideLoader');
            }
        },
        async getComments(sprintID) {
            this.sprintId = sprintID
            try {
                this.$store.commit('showLoader');
                const response = await axios.get(`${BASE_URL}api/development/comments?sprintID=${sprintID}`, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                        token: this.authToken,
                    }
                });
                this.comments = response.data.comments
                if (!this.comments.length) {
                    new Noty({
                        type: 'warning',
                        text: "No comments found for selected sprint",
                        timeout: 500,
                    }).show()
                    this.$store.commit('hideLoader');
                }
                this.$store.commit('hideLoader');
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.detail ? error.response.data.detail : error.response.data.message,
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
        async downloadCommentAttachments(event, commentID) {
            event.preventDefault();
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
                    type: 'error',
                    text: error.response.data.detail ? error.response.data.detail : error.response.data.message,
                    timeout: 1000,
                }).show();
            }
        },
        commentToggler(comment) {
            comment.editMode = !comment.editMode
        },
        handleFileChange(e) {
            this.selectedFiles = e.target.files
        },
        handleKeyDown(event) {
            if (event.key === 'C' && !this.isCommentFocused) {
                event.preventDefault()
                this.$refs.doComment.focus()
            }
        },
        async postComment() {
            try {
                this.$store.commit('showLoader');
                const formData = new FormData()
                if (this.selectedFiles.length) {
                    for (let i = 0; i < this.selectedFiles.length; i++) {
                        formData.append('attachments', this.selectedFiles[i])
                    }
                }
                formData.append('desc', this.commentDesc)
                formData.append('sprintID', this.sprintId)
                const response = await axios.post(`${BASE_URL}api/development/comments`, formData, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                        token: this.authToken,
                    }
                });
                if (response.status === 201) {
                    this.isCommentFocused = false
                    this.selectedFiles = []
                    this.commentDesc = ''
                    Swal.fire({
                        title: response.data.message,
                        icon: 'success',
                    })
                    this.getComments(this.sprintId)
                }
                this.$store.commit('hideLoader');
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.detail ? error.response.data.detail : error.response.data.message,
                    timeout: 1000,
                }).show()
                this.$store.commit('hideLoader');
            }
        },
        async editComment(comment, sprintID) {
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
                    this.getComments(sprintID)
                }
                this.$store.commit('hideLoader');
            }
            catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.detail ? error.response.data.detail : error.response.data.message,
                    timeout: 1000,
                }).show()
                this.$store.commit('hideLoader');
            }
        },
        async deleteComment(commentID, sprintID) {
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
                    this.getComments(sprintID)
                }
                this.$store.commit('hideLoader');
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.detail ? error.response.data.detail : error.response.data.message,
                    timeout: 1000,
                }).show()
                this.$store.commit('hideLoader');
            }
        }
    },
    mounted() {
        this.getAllProjects();
        document.addEventListener('keydown', this.handleKeyDown)
    },
    beforeUnmount() {
        document.removeEventListener('keydown', this.handleKeyDown)
    },
};
</script>

<style scoped>
::v-deep .ql-container {
    max-height: 300px;
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
    max-height: 300px;
    overflow-y: auto;
    color: black;
}

::v-deep .ql-tooltip {
    position: fixed;
    left: 50% !important;
    transform: translateX(-50%) !important;
    border: 1px solid red;
    max-height: 500px;
    overflow-y: auto;
    z-index: 99;
}

.sprintRow {
    display: flex;
    justify-content: space-between;
    border-radius: 5px;
    padding: 8px;
}

.sprintRow:hover {
    background-color: rgb(244, 243, 243);
    cursor: pointer;
}

/* .issueRow{
    
} */

.issueRow:hover {
    background-color: rgb(244, 243, 243);
    cursor: pointer;
}

.priority-icon {
    width: 20px;
    height: 20px;
}

.modalBody {
    max-height: calc(100vh - 150px);
    overflow: auto;
}

@media (max-width: 576px) {
    .modal-dialog {
        max-width: 99%;
        margin: auto;
    }

    .project-card {
        gap: 40px;
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

.close :hover {
    cursor: pointer;
    border: 1px solid red;
    z-index: 999999999999999999999;

}

.drop-icon {
    padding: 5px;
    border-radius: 10px;
}

.drop-icon:hover {
    background-color: lightgray;
    cursor: pointer;
}

.sprint-head {
    color: white;
}

.project-card {
    width: auto;
    padding-left: 10px;
    overflow: auto;
    margin: auto;
    margin-bottom: 15px !important;
    border-radius: 8px;
    box-shadow: rgba(0, 0, 0, 0.09) 0px 2px 1px, rgba(0, 0, 0, 0.09) 0px 2px 2px, rgba(0, 0, 0, 0.09) 0px 2px 2px, rgba(117, 117, 117, 0.09) 0px 2px 2px, rgba(117, 117, 117, 0.09) 0px 2px 2px;
}

.sprint-card {
    margin: auto;
    width: auto;
    border-radius: 8px;
}
</style>