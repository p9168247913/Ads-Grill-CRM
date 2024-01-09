<template>
    <div class="wrapper" style="margin-bottom: 80px;">
        <div class="content-page">
            <div class="container-fluid" style="margin-top: 30px;">
                <h5 class="sprint-head">SPRINT 1</h5>
                <div class="row">
                    <div class="col-md-6 col-lg-6 col-sm-12 mb-3">
                        <div class="input-group">
                            <span class="input-group-text text-body">
                                <i class="fas fa-search" aria-hidden="true"></i>
                            </span>
                            <input type="text" v-model="searchTerm" @change="filterUsers" class="form-control"
                                placeholder="Search Issue..." />
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-6 col-sm-12 d-flex justify-content-lg-end justify-content-md-end">
                        <div class="d-grid gap-2" style="display: flex!important; flex-direction: row;">
                            <button type="button" style="width: auto; height: 40px !important;"
                                class="btn btn-sm btn-dark mb-0 px-2 py-1 mb-0 nav-link active" data-bs-toggle="modal"
                                data-bs-target="#createProject">
                                <i class="fas fa-plus-circle text-success text-sm opacity-10"></i>&nbsp; &nbsp;Create
                                Sprint
                            </button>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6 col-lg-4 mb-3">
                        <div class="border issue-div">
                            <p class="card-head">TO DO</p>
                            <div class="issue-card">
                                <div class="row p-2 align-items-center">
                                    <p style="font-size: 12px; font-weight: bold;" class="col">Backend</p>
                                    <div class="col text-end">
                                        <button class="btn btn-link issue-card-btn dropdown-open" type="button"
                                            id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
                                            <i class="fas fa-ellipsis-h"></i>
                                        </button>
                                        <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownMenuButton">
                                            <li><a class="dropdown-item" href="#"><i
                                                        class="fas fa-edit text-success"></i>&nbsp;&nbsp;Edit</a></li>
                                            <li><a class="dropdown-item" href="#"><i
                                                        class="fas fa-trash-alt text-danger"></i>&nbsp;&nbsp;Delete</a></li>
                                        </ul>
                                    </div>
                                </div>
                                <div class="row align-items-center "
                                    style="margin-left: 2px;width: 95%; margin-top: -20px;">
                                    <img style="width: 40px;" class="sc-1j9o0vm-0 dMMVlq" alt="Story"
                                        src="https://adsgrilltech.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium"
                                        aria-describedby="5673val-tooltip">
                                    <p class="story-name col-10 ps-0"
                                        style="margin-top: 15px; font-size: 12px; font-weight: bold;">PROJECT NAME</p>
                                </div>
                            </div>
                            <div class="issue-card" data-bs-toggle="modal"
                                data-bs-target="#issueModal">
                                <div class="row p-2 align-items-center">
                                    <p style="font-size: 12px; font-weight: bold;" class="col">Frontend</p>
                                    <div class="col text-end">
                                        <button class="btn btn-link issue-card-btn dropdown-open" type="button"
                                            id="dropdownMenuButton2" data-bs-toggle="dropdown" aria-expanded="false">
                                            <i class="fas fa-ellipsis-h"></i>
                                        </button>
                                        <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownMenuButton2">
                                            <li><a class="dropdown-item" href="#"><i
                                                        class="fas fa-edit text-success"></i>&nbsp;&nbsp;Edit</a></li>
                                            <li><a class="dropdown-item" href="#"><i
                                                        class="fas fa-trash-alt text-danger"></i>&nbsp;&nbsp;Delete</a></li>
                                        </ul>
                                    </div>
                                </div>
                                <div class="row align-items-center "
                                    style="margin-left: 2px;width: 95%; margin-top: -20px;">
                                    <img style="width: 40px;" class="sc-1j9o0vm-0 dMMVlq" alt="Story"
                                        src="https://adsgrilltech.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium"
                                        aria-describedby="5673val-tooltip">
                                    <p class="story-name col-10 ps-0"
                                        style="margin-top: 15px; font-size: 12px; font-weight: bold;">PROJECT NAME</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-6 col-lg-4 mb-3">
                        <div class="border issue-div" style="">
                            <p class="card-head">IN PROGRESS</p>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-4 mb-3">
                        <div class="border issue-div">
                            <p class="card-head">DONE</p>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Modal for Create Sprint -->
            <div class="modal fade" ref="createProjectModal" id="createProject" tabindex="-1"
                aria-labelledby="createProjectLabel" aria-hidden="true" @hidden="createProjects">
                <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="createProjectLabel">Create Sprint</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body modalBody">
                            <form @submit="createProjects($event), resetValues()">
                                <div class="row">
                                    <div class="col-md-6 mb-3">
                                        <label for="type" class="form-label">Sprint Name</label>
                                        <input type="text" class="form-control" v-model="sprintData.sprint_name" required>
                                    </div>
                                    <div class="col-md-6 mb-3">
                                        <label for="projectName" class="form-label">Duration</label>
                                        <input type="text" class="form-control" v-model="sprintData.sprintDuration"
                                            required>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-md-6 mb-3">
                                        <label for="key" class="form-label">Start Date</label>
                                        <input type="date" class="form-control" v-model="sprintData.startDate" required>
                                    </div>
                                    <div class="col-md-6 mb-3">
                                        <label for="type" class="form-label">End Date</label>
                                        <input type="date" class="form-control" v-model="sprintData.endDate" required>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-md-6 mb-3">
                                        <label for="type" class="form-label">Goal</label>
                                        <input type="text" class="form-control" v-model="sprintData.goal" required>
                                    </div>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                                        @click="resetValues">Close</button>
                                    <button type="submit" class="btn btn-primary">Create</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>

            <!--Editor's Work in progress-->
            <div style="z-index: 9999999999;" class="modal fade" ref="createProjectModal" id="issueModal" tabindex="-1"
                aria-labelledby="createProjectLabel" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered modal-lg">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="createProjectLabel">Create Task</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body modalBody">
                            <QuillEditor ref="editor" :modules="modules" theme="snow" toolbar="full" />
                        </div>
                        <div class="modal-footer">
                            <button @click="saveContent">Save</button>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>
  
<script>
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';
// import ImageUploader from 'quill-image-uploader';
// import axios from 'axios';

export default {
    name: "active-sprint",
    data() {
        return {
            editorInstance: null,
            sprintData: {
                sprint_name: '',
                sprintDuration: '',
                startDate: '',
                endDate: '',
                goal: '',
            },
        };
    },
    components: {
        QuillEditor,
    },
    methods: {
        resetValues() {
            this.sprintData = {
                sprint_name: '',
                sprintDuration: '',
                startDate: '',
                endDate: '',
                goal: '',
            }
        },
        createSprints() { },
        saveContent() {
            if (this.$refs.editor) {
                const quillEditor = this.$refs.editor;
                if (quillEditor.getHTML) {
                    const htmlContent = quillEditor.getHTML();
                    console.log(htmlContent);
                } else {
                    console.error('getHTML method is not available');
                }
            } else {
                console.error('Quill editor reference not found');
            }
        },
    },
    // setup: () => {
    //     const modules = {
    //         name: 'imageUploader',
    //         module: ImageUploader,
    //         options: {
    //             upload: file => {
    //                 return new Promise((resolve, reject) => {
    //                     const formData = new FormData();
    //                     formData.append("image", file);

    //                     axios.post('/upload-image', formData)
    //                         .then(res => {
    //                             console.log(res)
    //                             resolve(res.data.url);
    //                         })
    //                         .catch(err => {
    //                             reject("Upload failed");
    //                             console.error("Error:", err)
    //                         })
    //                 })
    //             }

    //         }
    //     }
    //     return { modules }
    // }
}
</script>
    
<style scoped>
.issue-div {
    height: 70vh;
    background-color: #f3f3f3;
    border-radius: 5px;
    padding-top: 20px;
    overflow-y: auto;
}

.sprint-head {
    color: white;
}

.card-head {
    font-size: 12px;
    font-weight: bold;
    margin-left: 15px;
}

.issue-card {
    margin: auto;
    height: auto;
    width: 94%;
    background-color: white;
    border-radius: 5px;
    margin-bottom: 8px;
    position: relative;
    box-shadow: rgba(0, 0, 0, 0.09) 0px 2px 1px, rgba(0, 0, 0, 0.09) 0px 2px 2px, rgba(0, 0, 0, 0.09) 0px 2px 2px, rgba(117, 117, 117, 0.09) 0px 2px 2px, rgba(117, 117, 117, 0.09) 0px 2px 2px;
}

.issue-card:hover {
    background-color: rgb(240, 246, 246);
    transform: scale(1.005);
    transition: transform 0.3s;
    z-index: 1;
}

.issue-card-btn {
    position: absolute;
    top: 5px;
    right: 10px;
}

.issue-card-btn:hover {
    cursor: pointer;
    background-color: white;
    color: black !important;
}

.dropdown-menu:hover {
    z-index: 999;
}
</style>
  