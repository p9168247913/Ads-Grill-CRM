<!-- Home.vue -->
<template>
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
    </head>
    <div class="wrapper" style="margin-bottom: 80px; ">
        <div class="content-page">
            <div class="container-fluid">
                <div style="margin-top: 20px;">
                    <div class="row">
                        <div class="col-md-6 col-lg-6 col-sm-12 mb-3">
                            <div class="input-group">
                                <span class="input-group-text text-body">
                                    <i class="fas fa-search" aria-hidden="true"></i>
                                </span>
                                <input type="text" v-model="searchTerm" class="form-control"
                                    placeholder="Search Issue..." />
                            </div>
                        </div>
                        <div class="col-md-6 col-lg-6 col-sm-12 d-flex justify-content-lg-end justify-content-md-end">
                            <div class="d-grid gap-2" style="display: flex!important; flex-direction: row;">
                                <button type="button" style="width: auto; height: 40px !important;"
                                    class="btn btn-sm btn-dark mb-0 px-2 py-1 mb-0 nav-link active" data-bs-toggle="modal"
                                    data-bs-target="#createIssue">
                                    <i class="fas fa-plus-circle text-success text-sm opacity-10"></i>&nbsp; &nbsp;Create
                                    Issue
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Modal for Create Issue -->
                <div class="modal fade" ref="createProjectModal" id="createIssue" tabindex="-1"
                    aria-labelledby="createProjectLabel" aria-hidden="true" @hidden="createSprints">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="createProjectLabel">Create Issue</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body modalBody">
                                <form @submit="createIssues($event)">
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="title" class="form-label">Title</label>
                                            <input type="text" class="form-control" v-model="issueData.title"
                                                @input="generateKey" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="key" class="form-label">Key</label>
                                            <input type="text" class="form-control" v-model="issueData.key"
                                                readonly="readonly" required>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="sprint" class="form-label">Sprint</label>
                                            <select required class="form-select" v-model="issueData.sprint_id">
                                                <option value="">Select sprint</option>
                                                <option v-for="(sprint, index) in allSprints" :key="index"
                                                    :value="sprint.id">{{
                                                        sprint.name }}</option>
                                            </select>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="reporter" class="form-label">Reporter</label>
                                            <select required class="form-select" v-model="issueData.reporter_id">
                                                <option value="">Select Reporter</option>
                                                <option v-for="(manager, index) in projectManagers" :key="index"
                                                    :value="manager.id">{{
                                                        manager.name }}</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">Type</label>
                                            <select required class="form-select" v-model="issueData.type">
                                                <option value="">Select Type</option>
                                                <option value="epic">Epic</option>
                                                <option value="story">Story</option>
                                                <option value="task">Task</option>
                                                <option value="subtask">Subtask</option>
                                                <option value="bug">Bug</option>
                                            </select>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="parent" class="form-label">Parent</label>
                                            <v-select v-model="selected_parent_issues" :options="validParentIssues"
                                                label="title" :multiple="true" placeholder="Select parent(s)"
                                                :disabled="isParentDropdownDisabled"></v-select>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="team lead" class="form-label">Team Lead</label>
                                            <select class="form-select" v-model="issueData.team_lead_id">
                                                <option value="">Select Team Lead</option>
                                                <option v-for="(lead, index) in teamLead" :key="index" :value="lead.id">{{
                                                    lead.name }}</option>
                                            </select>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="expected time" class="form-label">Expected Time</label>
                                            <input required type="text" class="form-control"
                                                v-model="issueData.exp_duration" @change="checkDurationValidity">
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="Assignee" class="form-label">Assignee</label>
                                            <select required class="form-select" v-model="issueData.assignee_id">
                                                <option value="">Select Assignee</option>
                                                <option v-for="(assignee, index) in assignees" :key="index"
                                                    :value="assignee.id">{{
                                                        assignee.name }}</option>
                                            </select>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="priority" class="form-label">Priority</label>
                                            <select required class="form-select" v-model="issueData.priority">
                                                <option value="">Select Priority</option>
                                                <option value="lowest">Lowest</option>
                                                <option value="low">Low</option>
                                                <option value="medium">Medium</option>
                                                <option value="high">High</option>
                                                <option value="highest">Highest</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-12 mb-3">
                                            <label for="issueName" class="form-label">Add Files</label>
                                            <input type="file" accept=".xlsx, .xlx, .pdf, .doc, .ppt" class="form-control"
                                                multiple @change="handleFileChange">
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-12 mb-3" style="height: 400px; overflow: auto;">
                                            <label for="description" class="form-label">Description</label>
                                            <QuillEditor ref="editor" :modules="modules" theme="snow" toolbar="full" />
                                        </div>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                                            @click="resetValues">Close</button>
                                        <button type="submit" data-bs-dismiss="modal"
                                            class="btn btn-primary">Create</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Modal for edit Issue -->
                <div class="modal fade" ref="createProjectModal" id="editIssue" tabindex="-1"
                    aria-labelledby="createProjectLabel" aria-hidden="true" @hiddln="createSprints">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">

                            <div class="modal-body modalBody">
                                <form @submit="editIssue($event), resetValues()">
                                    <div class="row">
                                        <!-- <h5 class="modal-title" id="createProjectLabel">Edit Issue</h5> -->
                                        <div class="col-md-6 mb-3">
                                            <input type="text" class="form-control modal-title-input"
                                                v-model="editIssueData.title" @input="generateKey" required>
                                        </div>
                                        <!-- <div class="col-md-6 mb-3">
                                            <a href="#child">Child</a>
                                        </div> -->
                                    </div>
                                    <div class="row" style="margin-top: -20px;">
                                        <div class="col-md-6 mb-3">
                                            <!-- <label for="key" class="form-label">Key</label> -->
                                            <input type="text" class="form-control modal-key-input"
                                                v-model="editIssueData.key" readonly="readonly" required>
                                        </div>

                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="sprint" class="form-label">Sprint</label>
                                            <select class="form-select" v-model="editIssueData.sprint_id" required>
                                                <option value="">Select sprint</option>
                                                <option v-for="(sprint, index) in allSprints" :key="index"
                                                    :value="sprint.id">{{
                                                        sprint.name }}</option>
                                            </select>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="reporter" class="form-label">Reporter</label>
                                            <select class="form-select" v-model="editIssueData.reporter_id" required>
                                                <option value="">Select Reporter</option>
                                                <option v-for="(manager, index) in projectManagers" :key="index"
                                                    :value="manager.id">{{
                                                        manager.name }}</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="type" class="form-label">Type</label>
                                            <select class="form-select" v-model="editIssueData.type" required>
                                                <option value="">Select Type</option>
                                                <option value="epic">Epic</option>
                                                <option value="story">Story</option>
                                                <option value="task">Task</option>
                                                <option value="subtask">Subtask</option>
                                                <option value="bug">Bug</option>
                                            </select>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="team lead" class="form-label">Team Lead</label>
                                            <select class="form-select" v-model="editIssueData.team_lead_id">
                                                <option value="">Select Team Lead</option>
                                                <option v-for="(lead, index) in teamLead" :key="index" :value="lead.id">{{
                                                    lead.name }}</option>
                                            </select>
                                        </div>

                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="expected time" class="form-label">Expected Time</label>
                                            <input type="text" class="form-control" v-model="editIssueData.exp_duration"
                                                @change="checkDurationValidity" required>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="Assignee" class="form-label">Assignee</label>
                                            <select class="form-select" v-model="editIssueData.assignee_id" required>
                                                <option value="">Select Assignee</option>
                                                <option v-for="(assignee, index) in assignees" :key="index"
                                                    :value="assignee.id">{{
                                                        assignee.name }}</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 mb-3">
                                            <label for="priority" class="form-label">Priority</label>
                                            <select class="form-select" v-model="editIssueData.priority" required>
                                                <option value="">Select Priority</option>
                                                <option value="lowest">Lowest</option>
                                                <option value="low">Low</option>
                                                <option value="medium">Medium</option>
                                                <option value="high">High</option>
                                                <option value="highest">Highest</option>
                                            </select>
                                        </div>
                                        <div class="col-md-6 mb-3">
                                            <label for="parent" class="form-label">Parent</label>
                                            <v-select v-model="selected_parent_issues" :options="validEditParentIssues"
                                                label="title" :multiple="true" placeholder="Select parent(s)"
                                                :disabled="isEditParentDropdownDisabled"></v-select>
                                            <!-- <select class="form-select" v-model="editIssueData.parent_id"
                                                :disabled="isEditParentDropdownDisabled" required>
                                                <option value="">Select Parent</option>
                                                <option v-for="(parent, index) in validEditParentIssues" :key="index"
                                                    :value="parent.id">{{ parent.title }}</option>
                                            </select> -->
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-12 mb-3">
                                            <label for="issueName" class="form-label">Files</label>
                                            <input type="file" accept=".xlsx, .xlx, .pdf, .doc, .ppt" class="form-control"
                                                multiple @change="handleUpdateFileChange">
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-12 mb-3" style="height: 400px; overflow: auto;">
                                            <label for="description" class="form-label">Description</label>
                                            <QuillEditor required ref="editEditor" :modules="modules" theme="snow"
                                                toolbar="full" />
                                        </div>
                                    </div>
                                    <div class="row" v-if="this.parent_issues.length > 0">
                                        <label for="description" class="form-label">Parent issue</label>
                                        <div class="col-md-12 mb-3" style="overflow: auto;">
                                            <table class="table align-items-center mb-0">
                                                <thead>
                                                    <tr>
                                                        <th style="color: #344767 !important;"
                                                            class="text-uppercase text-secondary text-xxs font-weight-bolder font-weight-bold">
                                                            Sr No.</th>
                                                        <th style="color: #344767!important;"
                                                            class="text-uppercase text-secondary text-xxs font-weight-bolder font-weight-bold">
                                                            Title</th>
                                                        <th style="color: #344767!important;"
                                                            class="text-uppercase text-secondary text-xxs font-weight-bolder font-weight-bold">
                                                            Status</th>
                                                        <th style="color: #344767!important;"
                                                            class="text-uppercase text-secondary text-xxs font-weight-bolder font-weight-bold">
                                                            Priority</th>
                                                        <th style="color: #344767!important;"
                                                            class="text-uppercase text-secondary text-xxs font-weight-bolder font-weight-bold">
                                                            Assignee</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr v-for="(issue, issueIndex) in parent_issues" :key="issueIndex">
                                                        <td style="padding-left: 25px;">
                                                            <div class="d-flex flex-column justify-content-center">
                                                                <h6 class="mb-0 text-xs">{{ issueIndex + 1 }}</h6>
                                                            </div>
                                                        </td>
                                                        <td style="padding-left: 25px;">
                                                            <div @click="dataChanger(issue), openEditModal()"
                                                                class="d-flex flex-column justify-content-center parent-title">
                                                                <h6 class="mb-0 text-xs">{{
                                                                    issue.title }}</h6>

                                                            </div>
                                                        </td>
                                                        <td style="padding-left: 25px;">
                                                            <div class="d-flex flex-column justify-content-center">
                                                                <h6 class="mb-0 text-xs">{{
                                                                    issue.status }}</h6>
                                                            </div>
                                                        </td>
                                                        <td style="padding-left: 25px;">
                                                            <div class="d-flex flex-column justify-content-center">
                                                                <h6 class="mb-0 text-xs">{{
                                                                    issue.priority }}</h6>
                                                            </div>
                                                        </td>
                                                        <td style="padding-left: 25px;">
                                                            <div class="d-flex flex-column justify-content-center">
                                                                <h6 class="mb-0 text-xs">{{
                                                                    issue.assignee }}</h6>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                </tbody>

                                            </table>
                                        </div>
                                    </div>
                                    <div id="child" class="row" v-if="this.child_issues.length > 0">
                                        <label for="description" class="form-label">Child issue</label>
                                        <div class="col-md-12 mb-3" style="overflow: auto;">
                                            <table class="table align-items-center mb-0">
                                                <thead>
                                                    <tr>
                                                        <th style="color: #344767 !important;"
                                                            class="text-uppercase text-secondary text-xxs font-weight-bolder font-weight-bold">
                                                            Sr No.</th>
                                                        <th style="color: #344767!important;"
                                                            class="text-uppercase text-secondary text-xxs font-weight-bolder font-weight-bold">
                                                            Title</th>
                                                        <th style="color: #344767!important;"
                                                            class="text-uppercase text-secondary text-xxs font-weight-bolder font-weight-bold">
                                                            Status</th>
                                                        <th style="color: #344767!important;"
                                                            class="text-uppercase text-secondary text-xxs font-weight-bolder font-weight-bold">
                                                            Priority</th>
                                                        <th style="color: #344767!important;"
                                                            class="text-uppercase text-secondary text-xxs font-weight-bolder font-weight-bold">
                                                            Assignee</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr v-for="(issue, issueIndex) in child_issues" :key="issueIndex">
                                                        <td style="padding-left: 25px;">
                                                            <div class="d-flex flex-column justify-content-center">
                                                                <h6 class="mb-0 text-xs">{{ issueIndex + 1 }}</h6>
                                                            </div>
                                                        </td>
                                                        <td style="padding-left: 25px;">
                                                            <div @click="dataChanger(issue), openEditModal()"
                                                                class="d-flex flex-column justify-content-center parent-title">
                                                                <h6 class="mb-0 text-xs">{{
                                                                    issue.title }}</h6>

                                                            </div>
                                                        </td>
                                                        <td style="padding-left: 25px;">
                                                            <div class="d-flex flex-column justify-content-center">
                                                                <h6 class="mb-0 text-xs">{{
                                                                    issue.status }}</h6>
                                                            </div>
                                                        </td>
                                                        <td style="padding-left: 25px;">
                                                            <div class="d-flex flex-column justify-content-center">
                                                                <h6 class="mb-0 text-xs">{{
                                                                    issue.priority }}</h6>
                                                            </div>
                                                        </td>
                                                        <td style="padding-left: 25px;">
                                                            <div class="d-flex flex-column justify-content-center">
                                                                <h6 class="mb-0 text-xs">{{
                                                                    issue.assignee }}</h6>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                </tbody>

                                            </table>
                                        </div>
                                    </div>
                                    <div id="child" class="row" v-if="this.linked_issues.length > 0">
                                        <label for="description" class="form-label">Linked issue</label>
                                        <div class="col-md-12 mb-3" style="overflow: auto;">
                                            <table class="table align-items-center mb-0">
                                                <thead>
                                                    <tr>
                                                        <th style="color: #344767 !important;"
                                                            class="text-uppercase text-secondary text-xxs font-weight-bolder font-weight-bold">
                                                            Sr No.</th>
                                                        <th style="color: #344767!important;"
                                                            class="text-uppercase text-secondary text-xxs font-weight-bolder font-weight-bold">
                                                            Title</th>
                                                        <th style="color: #344767!important;"
                                                            class="text-uppercase text-secondary text-xxs font-weight-bolder font-weight-bold">
                                                            Status</th>
                                                        <th style="color: #344767!important;"
                                                            class="text-uppercase text-secondary text-xxs font-weight-bolder font-weight-bold">
                                                            Priority</th>
                                                        <th style="color: #344767!important;"
                                                            class="text-uppercase text-secondary text-xxs font-weight-bolder font-weight-bold">
                                                            Assignee</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr v-for="(issue, issueIndex) in linked_issues" :key="issueIndex">
                                                        <td style="padding-left: 25px;">
                                                            <div class="d-flex flex-column justify-content-center">
                                                                <h6 class="mb-0 text-xs">{{ issueIndex + 1 }}</h6>
                                                            </div>
                                                        </td>
                                                        <td style="padding-left: 25px;">
                                                            <div @click="dataChanger(issue), openEditModal()"
                                                                class="d-flex flex-column justify-content-center parent-title">
                                                                <h6 class="mb-0 text-xs">{{
                                                                    issue.title }}</h6>
                                                            </div>
                                                        </td>
                                                        <td style="padding-left: 25px;">
                                                            <div class="d-flex flex-column justify-content-center">
                                                                <h6 class="mb-0 text-xs">{{
                                                                    issue.status }}</h6>
                                                            </div>
                                                        </td>
                                                        <td style="padding-left: 25px;">
                                                            <div class="d-flex flex-column justify-content-center">
                                                                <h6 class="mb-0 text-xs">{{
                                                                    issue.priority }}</h6>
                                                            </div>
                                                        </td>
                                                        <td style="padding-left: 25px;">
                                                            <div class="d-flex flex-column justify-content-center">
                                                                <h6 class="mb-0 text-xs">{{
                                                                    issue.assignee }}</h6>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                </tbody>

                                            </table>
                                        </div>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                                            @click="resetValues">Close</button>
                                        <button type="submit" data-bs-dismiss="modal" class="btn btn-primary">Save</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>

                <comments ref="commentsView" />
                <worklog />
                

                <!--Table-->
                <div class="card" style="margin-top: 2rem;">
                    <div class="card-header pb-0">
                        <h6>ISSUES</h6>
                    </div>
                    <div class="card-body px-0 pt-0 pb-2">
                        <div class="table-responsive p-0">
                            <table class="table align-items-center mb-0">
                                <thead>
                                    <tr>
                                        <th style="color: #344767 !important;"
                                            class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold"
                                            v-for="(head) in headers" :key="head">{{ head }}</th>
                                        <th style="color: #344767 !important;"
                                            class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold action-head">
                                            Action</th>
                                    </tr>
                                </thead>
                                <tbody v-for="(issue, index) in allIssues" :key="index">
                                    <tr>
                                        <td style="padding: 25px;">
                                            <div class="d-flex flex-column justify-content-left">
                                                <h6 class="mb-0 text-sm">{{ index + 1 }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding: 25px;">
                                            <div class="d-flex flex-column justify-content-left">
                                                <h6 class="mb-0 text-sm">{{ issue.title }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding: 25px;">
                                            <div class="d-flex flex-column justify-content-left">
                                                <h6 class="mb-0 text-sm">{{ issue.type }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding: 25px;">
                                            <div class="d-flex flex-column justify-content-left">
                                                <h6 class="mb-0 text-sm">{{ issue.status }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding: 25px;">
                                            <div class="d-flex flex-column justify-content-left">
                                                <h6 class="mb-0 text-sm">{{ issue.exp_duration }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding: 25px;">
                                            <div class="d-flex flex-column justify-content-left">
                                                <h6 class="mb-0 text-sm">{{ issue.org_duration }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding: 25px;">
                                            <div class="d-flex flex-column justify-content-left">
                                                <h6 class="mb-0 text-sm">{{ issue.reporter.name }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding: 25px;">
                                            <div class="d-flex flex-column justify-content-left">
                                                <h6 class="mb-0 text-sm">{{ issue.assignee.name }}</h6>
                                            </div>
                                        </td>
                                        <td style="padding-left: 30px;">
                                            <div class="d-flex flex-column justify-content-center">
                                                <a v-if="issue.attachments.length"
                                                    @click="getAttachmentUrl($event, issue.id)">
                                                    <i class="fas fa-download"></i>
                                                </a>
                                                <span v-else>No Files</span>
                                            </div>
                                        </td>
                                        <td class="align-middle d-md-table-cell actions">
                                            <!-- <i v-if="authUser.role == 'admin'"
                                              class="fas fa-pencil-alt text-primary fa-xs pr-4 edit-icon"
                                              data-bs-toggle="modal" data-bs-target="#edituser"
                                              style="margin-left: 20px; cursor: pointer;" ></i> -->
                                            <i class="fas fa-pencil-alt text-primary fa-xs pr-4" data-bs-toggle="modal"
                                                data-bs-target="#editIssue" @click="editData(issue)"
                                                style="color: dodgerblue !important; margin-left: 20px; cursor: pointer"></i>

                                            <!-- <i v-if="authUser.role == 'admin'"
                                              class="fas fa-trash text-danger m-3 fa-xs delete-icon" style="cursor: pointer;"
                                              @click="deleteUser" data-toggle="tooltip" data-original-title="Delete user"></i> -->
                                            <i @click="deleteIssue(issue.id)" class="fas fa-trash text-danger m-3 fa-xs"
                                                style="cursor: pointer;"></i>

                                                <!-- Comment Section Button-->
                                            <i @click="sendDataToComments(issue.id, issue.sprint.id)"
                                                class="fas fa-trash text-danger m-1 fa-xs" data-bs-toggle="modal"
                                                data-bs-target="#comments" style="cursor: pointer;"></i>

                                                    <!-- Worklog Section Button-->
                                                <i @click="sendDataToComments(issue.id, issue.sprint.id)"
                                                class="fas fa-trash text-danger m-1 fa-xs" data-bs-toggle="modal"
                                                data-bs-target="#worklog" style="cursor: pointer;"></i>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <!-- <PaginationComponent :currentPage="currentPage" :itemsPerPage="itemsPerPage" :filteredUsers="filteredUsers"
                      :prevPage="prevPage" :nextPage="nextPage" :goToPage="goToPage" /> -->
                </div>
            </div>
        </div>
    </div>
</template>
      
<script>
import comments from './comments.vue';
import worklog from './worklog.vue';
import { BASE_URL } from '../../config/apiConfig';
import axios from 'axios';
import Noty from 'noty';
import Swal from 'sweetalert2';
import { mapState } from 'vuex';
import { QuillEditor } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";
export default {
    name: "IssuePage",
    data() {
        return {
            isEditIssueModalVisible: false,
            headers: ['S.No.', 'Title', 'Type', 'Status', 'Task duration', 'Actual duration', 'Reporting Manager', 'Assignee', 'Files'],
            allIssues: [],
            selectedSprintId: '',
            selectedEditSprintId: '',
            searchTerm: '',
            allSprints: [],
            teamLead: [],
            assignees: [],
            projectManagers: [],
            selectedFiles: [],
            selectedUpdateFiles: [],
            team_lead: [{
                id: 7,
                name: "Shyam",
            }],
            selected_parent_issues: [],
            issueData: {
                project_id: '',
                sprint_id: '',
                parent_issues: [],
                reporter_id: '',
                team_lead_id: '',
                attachments: [],
                title: '',
                key: '',
                description: '',
                type: '',
                priority: '',
                exp_duration: '',
                assignee_id: '',
            },
            filteredIssues: [],
            editIssueData: {
                id: '',
                project_id: '',
                sprint_id: '',
                reporter_id: '',
                team_lead_id: '',
                attachments: [],
                title: '',
                key: '',
                description: '',
                type: '',
                priority: '',
                exp_duration: '',
                assignee_id: '',
            },
            parent_issues: [],
            child_issues: [],
            linked_issues: [],
        };
    },
    components: {
        QuillEditor,
        vSelect,
        comments,
        worklog
    },
    computed: {
        ...mapState(['authUser', 'authToken']),
        validParentIssues: function () {
            if (!this.issueData.sprint_id) {
                return [];
            }

            const validTypes = this.getValidParentTypes(this.issueData.type);
            return this.allIssues.filter(issue =>
                validTypes.includes(issue.type) && issue.sprint.id === this.issueData.sprint_id
            );
        },
        isParentDropdownDisabled: function () {
            return this.issueData.type === 'epic';
        },
        validEditParentIssues: function () {
            if (!this.editIssueData.sprint_id) {
                return [];
            }
            const validTypes = this.getValidParentTypes(this.editIssueData.type);
            const currentParentIssueIds = this.parent_issues.map(parent => parent.id);

            return this.allIssues.filter(issue =>
                validTypes.includes(issue.type) &&
                issue.sprint.id === this.editIssueData.sprint_id &&
                !currentParentIssueIds.includes(issue.id)
            );
        },

        isEditParentDropdownDisabled: function () {
            return this.editIssueData.type === 'epic';
        },
    },
    methods: {
        async getAttachmentUrl(e, id) {
            e.preventDefault();
            try {
                const response = await axios.get(`${BASE_URL}api/development/issues/download?id=${id}`, {
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
                // console.log(error);
                new Noty({
                    text: 'An error occurred',
                    timeout: 500,
                }).show();
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
        async dataChanger(issue) {
            var id = '';
            var selectedIssue = []
            this.allIssues.find((Allissue) => {
                if (Allissue.id == issue.id) {
                    selectedIssue = Allissue
                    id = Allissue.id
                }
            });
            // console.log("issue", issue);
            if (id !== '') {
                try {
                    this.$store.commit('showLoader')
                    const response = await axios.get(`${BASE_URL}api/development/issueMetaData?id=${id}`, {
                        headers: {
                            token: this.authToken,
                        },
                    })
                    //111
                    if (response.data.Data.parentIssues.length > 0 && response.data.Data.childIssues.length > 0 && response.data.Data.linked_issues.length > 0) {
                        this.parent_issues = response.data.Data.parentIssues;
                        this.child_issues = response.data.Data.childIssues;
                        this.linked_issues = response.data.Data.linked_issues;
                    }
                    //100
                    else if (response.data.Data.parentIssues.length > 0 && response.data.Data.childIssues.length === 0 && response.data.Data.linked_issues.length === 0) {
                        this.parent_issues = response.data.Data.parentIssues;
                        this.child_issues = [];
                        this.linked_issues = [];
                    }
                    //110
                    else if (response.data.Data.parentIssues.length > 0 && response.data.Data.childIssues.length > 0 && response.data.Data.linked_issues.length === 0) {
                        this.parent_issues = response.data.Data.parentIssues;
                        this.child_issues = response.data.Data.childIssues;
                        this.linked_issues = [];
                    }
                    //101
                    else if (response.data.Data.parentIssues.length > 0 && response.data.Data.childIssues.length === 0 && response.data.Data.linked_issues.length > 0) {
                        this.parent_issues = response.data.Data.parentIssues;
                        this.child_issues = [];
                        this.linked_issues = response.data.Data.linked_issues;
                    }
                    //011
                    else if (response.data.Data.childIssues.length > 0 && response.data.Data.parentIssues.length === 0 && response.data.Data.linked_issues.length > 0) {
                        this.child_issues = response.data.Data.childIssues;
                        this.parent_issues = [];
                        this.linked_issues = response.data.Data.linked_issues;
                    }
                    //010
                    else if (response.data.Data.childIssues.length > 0 && response.data.Data.parentIssues.length === 0 && response.data.Data.linked_issues.length === 0) {
                        this.parent_issues = [];
                        this.child_issues = response.data.Data.childIssues;
                        this.linked_issues = [];
                    }
                    //001
                    else if (response.data.Data.childIssues.length === 0 && response.data.Data.parentIssues.length === 0 && response.data.Data.linked_issues.length > 0) {
                        this.child_issues = [];
                        this.parent_issues = [];
                        this.linked_issues = response.data.Data.linked_issues;
                    }
                    //000
                    else {
                        this.parent_issues = [];
                        this.child_issues = [];
                        this.linked_issues = []
                    }
                    this.$store.commit('hideLoader');
                } catch (error) {
                    // console.log(error);
                    new Noty({
                        type: 'error',
                        text: error.message,
                        timeout: 1000,
                    }).show();
                    this.$store.commit('hideLoader');
                }
            }
            this.editIssueData = {
                type: selectedIssue.type,
                title: selectedIssue.title,
                key: selectedIssue.key,
                priority: selectedIssue.priority,
                exp_duration: selectedIssue.exp_duration,
                assignee_id: selectedIssue.assignee.id,
                reporter_id: selectedIssue.reporter.id,
                sprint_id: selectedIssue.sprint.id,
                team_lead_id: selectedIssue.team_lead.id,
            }
            const quillEditor = this.$refs.editEditor;
            if (quillEditor) {
                quillEditor.setHTML(selectedIssue.description);
            }
        },
        openEditModal() {
            const modal = this.$refs.editIssueModal;
            if (modal) {
                modal.classList.add('show');
                modal.addEventListener('click', this.closeEditModal);
                document.addEventListener('keydown', this.closeEditModal);
            }
        },
        closeEditModal(event) {
            const modal = this.$refs.editIssueModal;

            if (modal && (event.target === modal || event.key === 'Escape')) {
                modal.classList.remove('show');

                modal.removeEventListener('click', this.closeEditModal);
                document.removeEventListener('keydown', this.closeEditModal);
            }
        },
        getValidParentTypes: function (childType) {
            const hierarchy = ['epic', 'story', 'task', 'subtask', 'bug'];
            const childIndex = hierarchy.indexOf(childType);
            return hierarchy.slice(0, childIndex);
        },
        checkDurationValidity() {
            const durationRegex = /^(?:(\d{1,2})h\s*)?(?:(\d{1,2})m\s*)?(?:(\d{1,2})s\s*)?$/;
            const match = this.issueData.exp_duration.match(durationRegex);

            if (!match) {
                alert("Invalid duration format. Please use the format like '7h 20m 30s'.");
                this.issueData.exp_duration = '';
                return;
            }
            const hours = parseInt(match[1]) || 0;
            const minutes = parseInt(match[2]) || 0;
            const seconds = parseInt(match[3]) || 0;

            const formattedMinutes = minutes > 0 ? `${minutes}m` : "0m";
            const formattedSeconds = seconds > 0 ? `${seconds}s` : "0s";
            const formattedDuration = `${hours}h ${formattedMinutes} ${formattedSeconds}`;
            this.issueData.exp_duration = formattedDuration;

            if (hours > 23 || minutes > 59 || seconds > 59) {
                alert("Invalid time values. Hours should be between 0 and 23, and minutes/seconds should be between 0 and 59.");
                this.issueData.exp_duration = '';
                return;
            }
            // console.log(match);
        },
        onParentIssuesChange(selectedParents) {
            const parentIds = selectedParents.map(parent => parent.id);
            this.issueData.parent_issues = parentIds;
        },
        resetValues() {
            this.issueData = {
                sprint: '',
                reporter: '',
                team_lead_id: '',
                title: '',
                key: '',
                description: '',
                type: '',
                priority: '',
                exp_duration: '',
                assignee_id: '',
                attachments: null,
            }
            this.parent_issues = []
            this.selected_parent_issues = []
        },
        saveContent(e) {
            e.preventDefault()
            if (this.$refs.editor) {
                const quillEditor = this.$refs.editor;
                if (quillEditor) {
                    const htmlContent = quillEditor.getHTML();
                    return htmlContent
                } else {
                    console.error('rootHTML method is not available');
                }
            } else {
                console.error('Quill editor reference not found');
            }
        },
        async getIssue() {
            let id = localStorage.getItem('projectId')
            try {
                this.$store.commit('showLoader');
                const response = await axios.get(`${BASE_URL}api/development/issues?project_id=${id}`, {
                    headers: {
                        token: this.authToken,
                    }
                })
                if (response.status === 200) {
                    this.allIssues = response.data.issues
                }
                this.$store.commit('hideLoader');
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.message,
                    timeout: 500,
                }).show()
                this.$store.commit('hideLoader');
            }
        },
        async createIssues(e) {
            console.log('heelo')
            e.preventDefault()
            try {
                let project_id = localStorage.getItem('projectId')
                this.issueData.project_id = project_id
                this.issueData.description = this.saveContent(e);

                let formData = new FormData();
                formData.append('project_id', this.issueData.project_id);
                formData.append('sprint_id', this.issueData.sprint_id);
                formData.append('reporter_id', this.issueData.reporter_id);
                formData.append('team_lead_id', this.issueData.team_lead_id);
                formData.append('title', this.issueData.title);
                formData.append('key', this.issueData.key);
                formData.append('description', this.issueData.description);
                formData.append('type', this.issueData.type);
                formData.append('priority', this.issueData.priority);
                formData.append('exp_duration', this.issueData.exp_duration);
                formData.append('assignee_id', this.issueData.assignee_id);

                for (let i = 0; i < this.selected_parent_issues.length; i++) {
                    formData.append('parent_issues', this.selected_parent_issues[i].id);
                }
                for (let i = 0; i < this.selectedFiles.length; i++) {
                    formData.append('attachments', this.selectedFiles[i]);
                }

                this.$store.commit('showLoader');
                const response = await axios.post(`${BASE_URL}api/development/issues`, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                        token: this.authToken,
                    },
                    onUploadProgress: progressEvent => {
                        const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
                        this.uploadProgress = percentCompleted;
                    },
                });
                if (response.status === 201) {
                    Swal.fire({
                        title: response.data.message,
                        icon: 'success',
                    });
                    this.resetValues();
                } else {
                    new Noty({
                        type: 'error',
                        text: response.data.message,
                        timeout: 1000,
                    }).show();
                }
                this.$store.commit('hideLoader');
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message,
                    timeout: 1000,
                }).show();
                this.$store.commit('hideLoader');
            }
        },
        async editData(issue) {
            let project_id = localStorage.getItem('projectId')
            try {
                this.$store.commit('showLoader');
                const response = await axios.get(`${BASE_URL}api/development/issueMetaData?id=${issue.id}`, {
                    headers: {
                        token: this.authToken,
                    },
                })
                if (response.data.Data.parentIssues.length > 0 && response.data.Data.childIssues.length > 0 && response.data.Data.linked_issues.length > 0) {
                    this.parent_issues = response.data.Data.parentIssues;
                    this.child_issues = response.data.Data.childIssues;
                    this.linked_issues = response.data.Data.linked_issues;
                }
                else if (response.data.Data.parentIssues.length > 0 && response.data.Data.childIssues.length === 0 && response.data.Data.linked_issues.length === 0) {
                    this.parent_issues = response.data.Data.parentIssues;
                    this.child_issues = [];
                    this.linked_issues = [];
                }
                else if (response.data.Data.parentIssues.length > 0 && response.data.Data.childIssues.length > 0 && response.data.Data.linked_issues.length === 0) {
                    this.parent_issues = response.data.Data.parentIssues;
                    this.child_issues = response.data.Data.childIssues;
                    this.linked_issues = [];
                }
                else if (response.data.Data.parentIssues.length > 0 && response.data.Data.childIssues.length === 0 && response.data.Data.linked_issues.length > 0) {
                    this.parent_issues = response.data.Data.parentIssues;
                    this.child_issues = [];
                    this.linked_issues = response.data.Data.linked_issues;
                }
                else if (response.data.Data.childIssues.length > 0 && response.data.Data.parentIssues.length === 0 && response.data.Data.linked_issues.length > 0) {
                    this.child_issues = response.data.Data.childIssues;
                    this.parent_issues = [];
                    this.linked_issues = response.data.Data.linked_issues;
                }
                else if (response.data.Data.childIssues.length > 0 && response.data.Data.parentIssues.length === 0 && response.data.Data.linked_issues.length === 0) {
                    this.parent_issues = [];
                    this.child_issues = response.data.Data.childIssues;
                    this.linked_issues = [];
                }
                else if (response.data.Data.childIssues.length === 0 && response.data.Data.parentIssues.length === 0 && response.data.Data.linked_issues.length > 0) {
                    this.child_issues = [];
                    this.parent_issues = [];
                    this.linked_issues = response.data.Data.linked_issues;
                }
                else {
                    this.parent_issues = [];
                    this.child_issues = [];
                    this.linked_issues = []
                }
                this.$store.commit('hideLoader')
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.message,
                    timeout: 500,
                }).show()
                this.$store.commit('hideLoader');
            }
            this.selected_parent_issues = this.parent_issues
            this.selectedUpdateFiles = []
            this.editIssueData = {
                id: issue.id,
                title: issue.title,
                project_id: project_id,
                key: issue.key,
                type: issue.type,
                priority: issue.priority,
                exp_duration: issue.exp_duration,
                assignee_id: issue.assignee.id,
                reporter_id: issue.reporter.id,
                sprint_id: issue.sprint.id,
                team_lead_id: issue.team_lead.id,
                status: issue.status
            };
            this.selectedEditSprintId = issue.sprint.id;
            const quillEditor = this.$refs.editEditor;
            if (quillEditor) {
                quillEditor.setHTML(issue.description);
            }
            // console.log("selectedData", this.editIssueData);
        },
        async editIssue(e) {
            e.preventDefault()
            let project_id = localStorage.getItem('projectId')
            const quillEditor = this.$refs.editEditor;
            this.editIssueData.project_id = project_id
            if (quillEditor) {
                const htmlContent = quillEditor.getHTML();
                this.editIssueData.description = htmlContent
            }
            try {
                let formData = new FormData();
                formData.append('id', this.editIssueData.id);
                formData.append('project_id', this.editIssueData.project_id);
                formData.append('sprint_id', this.editIssueData.sprint_id);
                formData.append('reporter_id', this.editIssueData.reporter_id);
                formData.append('team_lead_id', this.editIssueData.team_lead_id);
                formData.append('title', this.editIssueData.title);
                formData.append('key', this.editIssueData.key);
                formData.append('status', this.editIssueData.status);
                formData.append('description', this.editIssueData.description);
                formData.append('type', this.editIssueData.type);
                formData.append('priority', this.editIssueData.priority);
                formData.append('exp_duration', this.editIssueData.exp_duration);
                formData.append('assignee_id', this.editIssueData.assignee_id);
                if (this.selected_parent_issues.length) {
                    for (let i = 0; i < this.selected_parent_issues.length; i++) {
                        formData.append('parent_issues', this.selected_parent_issues[i].id);
                    }
                }

                if (this.selectedUpdateFiles.length) {
                    for (let i = 0; i < this.selectedUpdateFiles.length; i++) {
                        formData.append('attachments', this.selectedUpdateFiles[i]);
                    }
                }
                // console.log("finalData", this.editIssueData);

                this.$store.commit('showLoader');
                const response = await axios.put(`${BASE_URL}api/development/issues`, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                        token: this.authToken,
                    },
                    onUploadProgress: progressEvent => {
                        const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
                        this.uploadProgress = percentCompleted;
                    },
                });
                if (response.status === 200) {
                    Swal.fire({
                        title: response.data.message,
                        icon: 'success',
                    });
                    this.resetValues();
                    this.getIssue()
                } else {
                    new Noty({
                        type: 'error',
                        text: response.data.message,
                        timeout: 1000,
                    }).show();
                }
                this.$store.commit('hideLoader');
            } catch (error) {
                // console.log(error);
                new Noty({
                    type: 'error',
                    text: error.message,
                    timeout: 1000,
                }).show();
                this.$store.commit('hideLoader');
            }
        },
        async deleteIssue(id) {
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
                        const response = await axios.delete(`${BASE_URL}api/development/issues?id=${id}`, {
                            headers: {
                                token: this.authToken
                            }
                        })
                        this.getIssue();
                        Swal.fire('Deleted!', response.data.message, 'success');
                    } catch (error) {
                        this.getIssue();
                        Swal.fire('Error!', error.response.data.message, 'error');
                    }
                }
            });
        },
        async getProjectManagers() {
            try {
                this.$store.commit('showLoader');
                const response = await axios.get(`${BASE_URL}api/development/getProjectManagers`, {
                    headers: {
                        token: this.authToken,
                    }
                })
                this.projectManagers = response.data.project_managers;
                this.$store.commit('hideLoader');
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.message,
                    timeout: 500,
                }).show()
                this.$store.commit('hideLoader');
            }
        },
        async getTeamLead() {
            try {
                this.$store.commit('showLoader');
                const response = await axios.get(`${BASE_URL}api/development/getTeamLeaders`, {
                    headers: {
                        token: this.authToken,
                    }
                })
                this.teamLead = response.data.team_leaders
                this.$store.commit('hideLoader');
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.message,
                    timeout: 500,
                }).show()
                this.$store.commit('hideLoader');
            }
        },
        async getSprint() {
            let id = localStorage.getItem('projectId')
            try {
                this.$store.commit('showLoader');
                const response = await axios.get(`${BASE_URL}api/development/sprints?key=backlog&id=${id}`, {
                    headers: {
                        token: this.authToken,
                    }
                })
                if (response.status === 200) {
                    this.allSprints = response.data.sprintAndIssues
                }
                this.$store.commit('hideLoader');
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.message,
                    timeout: 500,
                }).show()
                this.$store.commit('hideLoader');
            }
        },
        async getAssignees() {
            try {
                this.$store.commit('showLoader');
                const response = await axios.get(`${BASE_URL}api/development/getAssignees`, {
                    headers: {
                        token: this.authToken,
                    }
                })
                if (response.status === 200) {
                    this.assignees = response.data.assignees
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.message,
                    timeout: 500,
                }).show()
                this.$store.commit('hideLoader');
            }
        },
        handleFileChange(e) {
            this.selectedFiles = e.target.files
        },
        handleUpdateFileChange(e) {
            this.selectedUpdateFiles = e.target.files
        },
        generateKey() {
            var issueTitle = this.issueData.title ? this.issueData.title.toUpperCase().split(' ') : [];
            var editIssueTitle = this.editIssueData.title ? this.editIssueData.title.toUpperCase().split(' ') : [];
            let key = '';
            let key2 = '';

            if (issueTitle.length === 1 || editIssueTitle.length === 1) {
                key = issueTitle[0];
                key2 = editIssueTitle[0];
            } else if (issueTitle.length === 2 || editIssueTitle.length === 2) {
                key = `${issueTitle[0].charAt(0)}${issueTitle[1].charAt(0)}`;
                key2 = `${editIssueTitle[0].charAt(0)}${editIssueTitle[1].charAt(0)}`;
            } else if (issueTitle.length > 2 || editIssueTitle.length > 2) {
                key = issueTitle.reduce((acc, curr) => acc + curr.charAt(0), '');
                key2 = editIssueTitle.reduce((acc, curr) => acc + curr.charAt(0), '');
            }
            const randomNumber = Math.floor(1000 + Math.random() * 9000);
            let uniqueKey = key ? `${key}_${randomNumber}` : '';
            let uniqueKey2 = key2 ? `${key2}_${randomNumber}` : '';
            this.issueData.key = uniqueKey;
            this.editIssueData.key = uniqueKey2;
        },

        // comments component methods
        sendDataToComments(issueID, sprintID) {
            this.$refs.commentsView.getDataFromIssuePage(issueID, sprintID);
        }
    },
    mounted() {
        this.getSprint();
        this.getAssignees();
        this.getProjectManagers();
        this.getTeamLead();
        this.getIssue();
    },
};

</script>

<style scoped>
::v-deep .ql-container {
    max-height: 500px;
    display: block;
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

.modal-title-input {
    border: none;
    outline: none;
    font-size: 1.5rem;
    font-weight: bold;
    background-color: transparent;
}


.modal-key-input {
    border: none;
    outline: none;
    font-size: .8rem;
    font-weight: bold;
    background-color: white !important;
}

.modalBody {
    max-height: calc(100vh - 200px);
    overflow: auto;
}

.actions {
    margin-left: 15px !important;
    position: sticky;
    right: 0;
    z-index: 1;
    background-color: white !important;
}

.action-head {
    position: sticky;
    right: 0;
    z-index: 1;
    background-color: white !important;
}

@media (max-width: 576px) {
    .modal-dialog {
        max-width: 99%;
        margin: auto;
    }

    .sprint-card {
        gap: 40px;
    }

    .actions {
        margin-left: 15px !important;
        z-index: 1;
        position: relative;
    }

    .action-head {
        position: relative;

        z-index: 1;
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

.issue-head {
    color: white;
}

.parent-title:hover {
    cursor: pointer;
    color: blue !important;
    text-decoration: underline;
    transform: scale(1.1);
}</style>
      