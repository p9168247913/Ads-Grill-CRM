<template>

    <head>
        <!-- Include necessary CSS files -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
    </head>
    <!-- Modal for post, read and delete Work log -->
    <div data-bs-backdrop="static" class="modal fade" ref="createWorklogModal" id="worklog"
        tabindex="-1" aria-labelledby="createWorklogLabel" aria-hidden="true" role="dialog" @hidden="removeBackdrop">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px;">
                <div class="modal-header">
                    <h5 class="modal-title" id="createWorklogLabel">Work Logs</h5>
                    <button @click="resetValues()" ref="closeModal" type="button" class="btn-close bg-dark text-xs"
                        data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body modalBodyWorklog" style="padding-bottom: 0;">
                    <div v-if="timeTracking" class="row mb-3">
                        <div class="col-md-3">
                            <span class="small text-xs text-dark font-weight-bolder">Time Tracking</span>
                        </div>
                        <div class="col-md-3">
                            <span class="text-xs text-dark">{{ formatDuration(timeTracking.total_logged_time) }}</span>
                            <p class="text-xs text-dark font-weight-bolder">Logged time</p>
                        </div>
                        <div class="col-md-3">
                            <span class="text-xs text-dark">{{ formatDuration(timeTracking.actual_remaining_time)
                                }}</span>
                            <p class="text-xs text-dark font-weight-bolder">Time remaining</p>
                        </div>
                        <div class="col-md-3">
                            <span class="text-xs text-dark">{{ formatDuration(timeTracking.extra_efforts) }}</span>
                            <p class="text-xs text-dark font-weight-bolder">Extra efforts</p>
                        </div>
                    </div>
                    <form @submit="postLogs($event)">
                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label for="expected time" class="form-label">Add Log Time</label>
                                <input placeholder="Format: 4h 20m 45s ('hh mm ss')" required type="text"
                                    class="form-control" v-model="logTime" @change="checkDurationValidity">
                            </div>
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Add Files</label>
                                <input type="file" accept=".xlsx, .xlx, .pdf, .doc, .ppt" class="form-control" multiple
                                    @change="handleFileChange">
                            </div>
                            <div class="col-md-12 mb-3" style="height: auto; overflow: auto; min-height: 100px;">
                                <label for="description" class="form-label">Description</label>
                                <QuillEditor ref="editor" :modules="modules" theme="snow" toolbar="full" />
                            </div>
                            <div></div>

                            <div class="">
                                <div class="row">
                                    <div class="col-md-12">
                                        <h5>Log History</h5>
                                        <hr>
                                    </div>
                                    <div v-if="workLogs.length" class="mt-3 overflow-y-auto pt-2"
                                        style="max-height: 200px;">
                                        <div v-for="(worklog, index) in workLogs" :key="index">
                                            <div class="d-flex flex-row text text-dark">
                                                <span
                                                    style="border-radius: 50%; margin-top:-4px; width:30px; height:30px; text-align: center;  background-color:lightgray;"
                                                    class="small font-weight-bold me-2 pt-1">{{
                                                    worklog.author.charAt(0).toUpperCase()
                                                    }}</span>
                                                <p class="pe-2 small font-weight-bold">{{ worklog.author }}</p>
                                                <p class="small"> logged - {{ formatDuration2(worklog.logged_time) + ' on'
                                                    }} {{
                                                    formatDateTime(worklog.created_at)
                                                    }}
                                                </p>
                                                <a v-if="worklog.attachments.length"
                                                    @click="downloadCommentAttachments($event, worklog.id)">
                                                    <i class="fas fa-download ms-3 cursor-pointer"
                                                        title="download attachments"></i>
                                                </a>
                                            </div>
                                            <div class="d-flex flex-column" style="margin-left: 40px;">
                                                <div class="d-flex flex-column" style="margin-top: -5px;">
                                                    <p class="small" v-html="worklog.description"></p>
                                                </div>
                                                <div v-if="worklog.editMode" class="d-flex flex-row">
                                                    <textarea @keyup.enter="editComment(worklog,)" type="text"
                                                        placeholder="Edit Comment..." v-model="worklog.description"
                                                        class="form-control small w-50 me-3"
                                                        style="height:40px; resize: none;"></textarea>

                                                    <input @change="handleFileChange($event)" id="fileInput2"
                                                        type="file" multiple
                                                        accept=".xlsx, .xls, .doc, .ppt, .pdf, .png, .jpeg, .jpg"
                                                        class="form-control w-auto d-none">
                                                    <label for="fileInput2"
                                                        class="text-xs rounded border border-1 border-dark font-weight-bold me-2"
                                                        title="Add files" style="padding:11px">Add Files</label>
                                                </div>
                                                <div v-if="worklog.editMode" class="d-flex flex-row">
                                                    <p @click="editComment(worklog)"
                                                        class="small me-2 cursor-pointer font-weight-bold">Save</p>
                                                    <p @click="commentToggler(worklog)"
                                                        class="small cursor-pointer font-weight-bold">Cancel</p>
                                                </div>
                                            </div>
                                            <div v-if="!worklog.editMode" class="d-flex flex-row"
                                                style="margin-left:40px; margin-top: -10px;">
                                                <p @click="editedLog(worklog), openEditWorklogModal(worklog)"
                                                    class="text-sm me-2 font-weight-bold cursor-pointer"
                                                    data-bs-dismiss="modal" data-bs-target="#editWorklog"
                                                    data-bs-toggle="modal">Edit</p>
                                                <p @click="deleteWorkLog(worklog.id)"
                                                    class="text-sm font-weight-bold cursor-pointer">Delete</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div v-else>
                                        <h6 class="text-danger">No history found!!</h6>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="modal-footer"
                            style="z-index: 999; margin-top: 30px; position: sticky; bottom: 0; background-color: white; margin-bottom: -500px;">
                            <button @click="resetValues()" type="button" class="btn btn-secondary"
                                data-bs-dismiss="modal">Close</button>
                            <button type="submit" :disabled="buttonToggler" class="btn btn-primary">Save</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!--Modal for edit work log-->
    <div data-bs-backdrop="static" class="modal fade" ref="editWorklogModal" id="editWorklog"
        tabindex="-1" aria-labelledby="editWorklogLable" aria-hidden="true" @hidden="removeBackdrop">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="editWorklogLable">Edit Work Log</h5>
                    <button @click="resetValues()" ref="closeModal" type="button" class="btn-close bg-dark text-xs"
                        data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body modalBody">
                    <form @submit="editLogs($event)">
                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label for="expected time" class="form-label">Add Log Time</label>
                                <input placeholder="Format: 4h 20m 45s ('hh mm ss')" required type="text"
                                    class="form-control" v-model="logTime" @change="checkDurationValidity">
                            </div>
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Add Files</label>
                                <input type="file" accept=".xlsx, .xlx, .pdf, .doc, .ppt" class="form-control" multiple
                                    @change="handleFileChange">
                            </div>
                            <div class="col-md-12 mb-3" style="height: auto; overflow: auto; min-height: 100px;">
                                <label for="description" class="form-label">Description</label>
                                <QuillEditor ref="logEditor" :modules="modules" theme="snow" toolbar="full" />
                            </div>
                            <div></div>
                            <div class="modal-footer">
                                <button @click="resetValues()" type="button" class="btn btn-secondary"
                                    data-bs-dismiss="modal">Close</button>
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
import { BASE_URL } from '../../config/apiConfig';
import axios from 'axios';
import Noty from 'noty';
import Swal from 'sweetalert2';
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
            sprintID: '',
            issueID: '',
            logTime: '',
            logDescription: '',
            selectedFiles: [],
            workLogs: [],
            updatedLog: [],
            timeTracking: '',
            issueStatus:'',
            buttonToggler:false
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
        formatDuration(duration) {
            const regex = /P(\d+D)?T(\d+H)?(\d+M)?(\d+S)?/;
            const matches = duration?.match(regex);

            if (!matches) {
                return '';
            }
            const [, days, hours, minutes, seconds] = matches;

            const formattedParts = [];
            if (days) {
                formattedParts.push(`${parseInt(days, 10)}d`);
            }
            if (hours) {
                formattedParts.push(`${parseInt(hours, 10)}h`);
            }
            if (minutes) {
                formattedParts.push(`${parseInt(minutes, 10)}m`);
            }
            if (seconds) {
                formattedParts.push(`${parseInt(seconds, 10)}s`);
            }
            return formattedParts.join(' ');
        },
        formatDuration2(duration) {
            const regex = /P?T(\d+H)?(\d+M)?(\d+S)?/;
            const matches = duration?.match(regex);

            if (!matches) {
                return '';
            }
            const [, hours, minutes, seconds] = matches;

            const formattedParts = [];
            if (hours) {
                formattedParts.push(`${parseInt(hours, 10)}h`);
            }
            if (minutes) {
                formattedParts.push(`${parseInt(minutes, 10)}m`);
            }
            if (seconds) {
                formattedParts.push(`${parseInt(seconds, 10)}s`);
            }
            return formattedParts.join(' ');
        },
        openEditWorklogModal(worklog) {
            const postWorklogModal = this.$refs.createWorklogModal;
            if (postWorklogModal) {
                postWorklogModal.hide();
            }

            this.editedLog(worklog);
            const editWorklogModal = this.$refs.editWorklogModal;
            if (editWorklogModal) {
                editWorklogModal.show();
            }
        },
        removeBackdrop() {
            const postWorklogBackdrop = document.querySelector('[data-backdrop-ref="postWorklogBackdrop"]');
            if (postWorklogBackdrop) {
                postWorklogBackdrop.remove();
            }
        },
        openEditModal() {
            const editModal = this.$refs.editIssueModal;

            if (editModal) {
                editModal.classList.add('show');
                editModal.addEventListener('click', this.closeEditModal);
                document.addEventListener('keydown', this.closeEditModal);
            }

            const workLogModal = this.$refs.createWorklogModal;
            if (workLogModal) {
                workLogModal.hide();
            }
        },
        closeEditModal(event) {
            const editModal = this.$refs.editIssueModal;

            if (editModal && (event.target === editModal || event.key === 'Escape')) {
                editModal.classList.remove('show');

                editModal.removeEventListener('click', this.closeEditModal);
                document.removeEventListener('keydown', this.closeEditModal);

                const workLogModal = this.$refs.createWorklogModal;
                if (workLogModal) {
                    workLogModal.show();
                }
            }
        },
        getDataFromIssuePage(issueID, sprintID, status) {
            this.sprintID = sprintID
            this.issueID = issueID
            this.issueStatus = status

        },
        checkDurationValidity() {
            if (this.logTime) {
                const durationRegex = /^(?:(\d{1,2})h\s*)?(?:(\d{1,2})m\s*)?(?:(\d{1,2})s\s*)?$/;
                const match = this.logTime.match(durationRegex);

                if (!match) {
                    new Noty({
                        type: 'error',
                        text: "Invalid duration format. Please use the format like '5h 20m 30s'.",
                        timeout: 5000,
                        layout: 'topRight',
                        closeWith: ['click'],
                    }).show();
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
                    new Noty({
                        type: 'error',
                        text: "Invalid time values. Days should be between 0 and 365, hours should be between 0 and 23, and minutes/seconds should be between 0 and 59.",
                        timeout: 5000,
                        layout: 'topRight',
                        closeWith: ['click'],
                    }).show()
                    this.logTime = '';
                    return;
                }
            }
        },
        handleFileChange(e) {
            this.selectedFiles = e.target.files
        },
        removeQuillHTML() {
            let quillHTML = this.$refs.editor
            let logEditorquillHTML = this.$refs.logEditor
            if (quillHTML && logEditorquillHTML) {
                quillHTML.setHTML("")
                logEditorquillHTML.setHTML("")
            }
        },
        resetValues() {
            this.logTime = '';
            this.logDescription = '';
            this.selectedFiles = [];
            this.removeQuillHTML();
            this.workLogs = []
            this.timeTracking = ''
            window.location.reload()
        },
        async postLogs(e) {
            e.preventDefault()
            try {
                this.$store.commit('showLoader');
                const quillHtml = this.$refs.editor
                
                if (quillHtml) {
                    this.logDescription = quillHtml.getHTML();
                }
                const formData = new FormData()
                formData.append('issue_id', this.issueID)
                formData.append('sprint_id', this.sprintID)
                formData.append('description', this.logDescription)
                formData.append('logged_time', this.logTime)
                if (this.selectedFiles.length) {
                    for (let i = 0; i < this.selectedFiles.length; i++) {
                        formData.append('attachments', this.selectedFiles[i])
                    }
                }
                const response = await axios.post(`${BASE_URL}api/development/worklog`, formData, {
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
                    this.getWorkLogs()
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
        async getWorkLogs() {
            try {
                if(this.issueStatus !== 'in_progress'){
                    this.buttonToggler = true
                    new Noty({
                        type: 'error',
                        text: "You can not add logs till status is to do or done",
                        timeout: 2000,
                    }).show();
                    return
                }
                this.$store.commit('showLoader');
                const response = await axios.get(`${BASE_URL}api/development/worklog?issue_id=${this.issueID}`, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                        token: this.authToken,
                    }
                });
                this.workLogs = response.data.worklogs
                this.timeTracking = response.data.time_tracking
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
        editedLog(worklog) {
            this.updatedLog = worklog
            this.logTime = this.formatDuration2(this.updatedLog.logged_time)
            const quillHtml = this.$refs.logEditor
            if (quillHtml) {
                quillHtml.setHTML(this.updatedLog.description)
            }
            this.selectedFiles = []
        },
        async editLogs(e) {
            e.preventDefault()
            try {
                this.$store.commit('showLoader');
                const quillHtml = this.$refs.logEditor
                if (quillHtml) {
                    this.logDescription = quillHtml.getHTML();
                }
                const formData = new FormData()
                formData.append('id', this.updatedLog.id)
                formData.append('description', this.logDescription)
                formData.append('logged_time', this.logTime)
                if (this.selectedFiles.length) {
                    for (let i = 0; i < this.selectedFiles.length; i++) {
                        formData.append('attachments', this.selectedFiles[i])
                    }
                }
                const response = await axios.put(`${BASE_URL}api/development/worklog`, formData, {
                    headers: {
                        'Content-Type': "multipart/form-data",
                        token: this.authToken,
                    }
                });
                if (response.status === 200) {
                    this.resetValues()
                    Swal.fire({
                        text: response.data.message,
                        icon: 'info',
                    })
                    this.getWorkLogs()
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
        async deleteWorkLog(logID) {
            try {
                this.$store.commit('showLoader');
                const response = await axios.delete(`${BASE_URL}api/development/worklog?id=${logID}`, {
                    headers: {
                        token: this.authToken,
                    }
                });
                if (response.status == 200) {
                    Swal.fire({
                        title: response.data.message,
                        icon: 'success',
                    })
                    this.getWorkLogs()
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
        async downloadCommentAttachments(e, logID) {
            e.preventDefault();
            try {
                const response = await axios.get(`${BASE_URL}api/development/worklog/download?id=${logID}`, {
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
    },
}
</script>

<style scoped>
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
}

.modalBody {
    max-height: calc(100vh - 200px);
    overflow: auto;
}

.modalBodyWorklog {
    max-height: calc(100vh - 200px);
    overflow: auto;
    height: 75vh;
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