<template>

    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Webkit | Responsive Bootstrap 4 Admin Dashboard Template</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
    </head>

    <div class="wrapper">
        <div class="content-page">
            <div class="container-fluid">
                <div style="margin-top: 20px;">
                    <div class="row">
                        <div class="col-md-6 col-lg-2 col-sm-6 mb-3">
                            <div class="input-group">
                                <span class="input-group-text text-body">
                                    <i class="fas fa-search" aria-hidden="true"></i>
                                </span>
                                <input type="text" v-model="clientNameFilter" class="form-control"
                                    placeholder="contact name..." />
                            </div>
                        </div>
                        <div class="col-md-6 col-lg-2 col-sm-6 mb-3">
                            <div class="input-group">
                                <span class="input-group-text text-body">
                                    <i class="fas fa-search" aria-hidden="true"></i>
                                </span>
                                <input type="text" v-model="contactNoFilter" class="form-control"
                                    placeholder="contact number..." />
                            </div>
                        </div>
                        <div class="col-md-6 col-lg-3 col-sm-6 mb-3">
                            <select class="form-control text-muted" v-model="project_type_filter">
                                <option value="">Select Project Type</option>
                                <option value="ERPS">Enterprise Resource Planning System (ERPS)</option>
                                <option value="CRM">Customer Engagement Platform (CRM)</option>
                                <option value="E-Com">Online Retail Platform (E-Com)</option>
                                <option value="Game_Dev">Interactive Entertainment Solutions (Game_Dev)</option>
                                <option value="WordPress">Dynamic Web Content Management (WordPress)</option>
                                <option value="Magento">E-Commerce Powerhouse (Magento)</option>
                                <option value="Shopify">E-Commerce Simplified (Shopify)</option>
                                <option value="Mobile Application">Mobile Application Solutions</option>
                                <option value="Web Presence">Web Presence Solutions</option>
                            </select>
                        </div>
                        <div class="col-md-6 col-lg-2 col-sm-6 mb-3">
                            <select class="form-select text-muted" v-model="statusFilter">
                                <option value="">Search by status</option>
                                <option v-for="status in quoteStatus" :key="status" :value="status.name">{{ status.name
                                    }}
                                </option>
                            </select>
                        </div>
                        <div class="col-md-6 col-lg-3 col-sm-10">
                            <div class="d-grid gap-2" style="display: flex!important; flex-direction: row;">
                                <!-- <button type="button"
                                    style=" display:flex; width:5px;height:40px !important; outline: none; justify-content: center; align-items: center;"
                                    class="btn btn-sm btn-dark nav-link"><i
                                        class="fas fa-search text-success text-sm opacity-10"></i><span
                                        class="d-none d-md-inline">&nbsp;
                                        &nbsp;</span></button> -->
                                <button type="button" @click="resestFilter"
                                    style=" display:flex; width:100px;height:40px !important; outline: none; justify-content: center; align-items: center;"
                                    class="btn btn-sm btn-dark nav-link"><i
                                        class="fas fa-trash text-success text-sm opacity-10"></i> &nbsp;Reset<span
                                        class="d-none d-md-inline">&nbsp;
                                        &nbsp;</span></button>

                                <button ref="newProposalModal" type="button" v-if="authUser.role!=='super-admin'"
                                    style=" display:flex; width:7em;height:40px !important; outline: none; justify-content: center; align-items: center;"
                                    class="btn btn-sm btn-dark" data-bs-toggle="modal" data-bs-target="#createProposal"
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

    <!--Add Open and Close Status Model Start-->
    <div data-bs-backdrop="static" class="modal fade" ref="addStatus" id="addStatusModal" tabindex="-1"
        aria-labelledby="createadminLabel" aria-hidden="true">
        <div style="width:auto" class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px; width:auto">
                <div class="modal-header">
                    <h5 class="modal-title" id="createadminLabel">Add New Status</h5>
                    <button @click="resetValues" type="button" class="btn-close bg-dark text-xs"
                        data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body modalBody" style="padding-bottom: 0; height:10rem; width: 26rem;">
                    <form @submit="addStatus($event)">
                        <div class="row">
                            <div class="col-md-12 col-lg-12">
                                <label class="form-label" for="statusInput">Enter Status</label>
                                <input id="statusInput" type="text" class="form-control" v-model="newStatus" required>
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
    <!--Add Open and Close Status Model Start-->

    <!--Desclaimer Template Start -->
    <div data-bs-backdrop="static" class="modal fade" ref="addDesclaimer" id="addDesclaimerModal" tabindex="-1"
        aria-labelledby="createadminLabel" aria-hidden="true" style="margin-left: -160px;">
        <div style="width:auto" class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px; width:auto">
                <div class="modal-header">
                    <h5 class="modal-title" id="createadminLabel">Add Desclaimer Templates</h5>
                    <button @click="resetValues" type="button" class="btn-close bg-dark text-xs"
                        data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body modalBody" style="padding-bottom: 0; height:35rem; width: 890px;">
                    <form @submit="addDesclaimer($event)">
                        <div class="row">
                            <div class="col-md-12 col-lg-12">
                                <label class="form-label" for="desclaimerTitle">Enter Desclaimer Title</label>
                                <input id="desclaimerTitle" type="text" class="form-control" v-model="newDesclaimerTitle" required>
                            </div>
                            <div class="col-md-12 col-lg-12 mb-8">
                                <label class="form-label" for="desclaimerDesc">Enter Desclaimer Description</label>
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
    <!--Desclaimer Template End -->

    <!-- About Template Start -->
    <div data-bs-backdrop="static" class="modal fade" ref="addAbout" id="addAboutModal" tabindex="-1"
        aria-labelledby="createadminLabel" aria-hidden="true" style="margin-left: -160px;">
        <div style="width:auto" class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px; width:auto">
                <div class="modal-header">
                    <h5 class="modal-title" id="createadminLabel">Add About Templates</h5>
                    <button @click="resetValues" type="button" class="btn-close bg-dark text-xs"
                        data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body modalBody" style="padding-bottom: 0; height:35rem; width: 890px;">
                    <form @submit="addAbout($event)">
                        <div class="row">
                            <div class="col-md-12 col-lg-12">
                                <label class="form-label" for="aboutTitle">Enter About Template Title</label>
                                <input id="aboutTitle" type="text" class="form-control" v-model="newAboutTitle" required>
                            </div>
                            <div class="col-md-12 col-lg-12 mb-8">
                                <label class="form-label" for="aboutDesc">Enter Desclaimer Description</label>
                                <QuillEditor required ref="editor" theme="snow" toolbar="full" v-model:content="newAboutDesc" contentType="html" id="aboutDesc"/>
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
    <!-- About Template End -->

    <!-- NDA Template Start -->
    <div data-bs-backdrop="static" class="modal fade" ref="addNDA" id="addNdaModal" tabindex="-1"
        aria-labelledby="createadminLabel" aria-hidden="true" style="margin-left: -160px;">
        <div style="width:auto" class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px; width:auto">
                <div class="modal-header">
                    <h5 class="modal-title" id="createadminLabel">Add NDA Templates</h5>
                    <button @click="resetValues" type="button" class="btn-close bg-dark text-xs"
                        data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body modalBody" style="padding-bottom: 0; height:35rem; width: 890px;">
                    <form @submit="addNDA($event)">
                        <div class="row">
                            <div class="col-md-12 col-lg-12">
                                <label class="form-label" for="ndaTitle">Enter NDA Template Title</label>
                                <input id="ndaTitle" type="text" class="form-control" v-model="newNdaTitle" required>
                            </div>
                            <div class="col-md-12 col-lg-12 mb-8">
                                <label class="form-label" for="ndaDesc">Enter NDA Description</label>
                                <QuillEditor required ref="editor" theme="snow" toolbar="full" v-model:content="newNdaDesc" contentType="html" id="ndaDesc"/>
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
    <!-- NDA Template Start -->

    <!-- MODAL FOR CREATE PROPOSAL START -->
    <div style="margin-left:-100px;" data-bs-backdrop="static" class="modal fade" ref="createProposalModal"
        id="createProposal" tabindex="-1" aria-labelledby="createadminLabel" aria-hidden="true">
        <div style="width:auto" class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px; width:auto">
                <div class="modal-header">
                    <h5 class="modal-title" id="createadminLabel">New Proposal</h5>
                    <button ref="createProposalBtn" type="button" class="btn-close bg-dark text-xs"
                        data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body modalBody" style="padding-bottom: 0; height:35rem; width: 890px;">
                    <form @submit="createProposal($event)">
                        <div class="row">
                            <div class="col-md-4 mb-3">
                                <label for="Client" class="form-label">Client</label>
                                <select class="form-select" v-model="selectedClientID">
                                    <option value="">Select Client</option>
                                    <option v-for="client in allSales" :key="client" :value="client.id">{{ client.name
                                        }}</option>
                                </select>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="email" class="form-label">Email</label>
                                <div v-if="selectedClient">
                                    <input disabled type="email" class="form-control" :value="selectedClient.email"
                                        required>
                                </div>
                                <div v-else>
                                    <input type="email" class="form-control" value="" required>
                                </div>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="contact_no" class="form-label">Mobile No.</label>
                                <div v-if="selectedClient">
                                    <input disabled type="text" class="form-control" :value="selectedClient.contact_no"
                                        required>
                                </div>
                                <div v-else>
                                    <input type="text" class="form-control" value="" required>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-4 mb-3">
                                <label for="project_types" class="form-label">Project Type</label>
                                <select class="form-control" v-model="project_type">
                                    <option value="">Select Type</option>
                                    <option value="ERPS">Enterprise Resource Planning System (ERPS)</option>
                                    <option value="CRM">Customer Engagement Platform (CRM)</option>
                                    <option value="E-Com">Online Retail Platform (E-Com)</option>
                                    <option value="Game_Dev">Interactive Entertainment Solutions (Game_Dev)</option>
                                    <option value="WordPress">Dynamic Web Content Management (WordPress)</option>
                                    <option value="Magento">E-Commerce Powerhouse (Magento)</option>
                                    <option value="Shopify">E-Commerce Simplified (Shopify)</option>
                                    <option value="Mobile Application">Mobile Application Solutions</option>
                                    <option value="Web Presence">Web Presence Solutions</option>
                                </select>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="project_name" class="form-label">Project Name</label>
                                <input type="text" class="form-control" v-model="projectName">
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="project_cost" class="form-label">Project Cost</label>
                                <div class="input-group">
                                    <input v-model="projectCost" type="text" class="form-control" id="project_cost"
                                        style="width: 78%;">
                                    <select class="form-select currency" v-model="selectedCurr"
                                        aria-label="Currency select" style="width:22%;">
                                        <option value="INR">INR</option>
                                        <option value="USD">USD</option>
                                        <option value="EUR">EUR</option>
                                        <option value="CAD">CAD</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-4">
                                <label for="status" class="form-label">Status</label>
                                <div class="input-group">
                                    <select v-model="selectedStatus" class="form-select" name="" id="">
                                        <option selected value="">Select Status</option>
                                        <option v-for="status in quoteStatus" :key="status.id" :value="status.id">{{ status.name }}
                                        </option>
                                    </select>
                                    <button data-bs-toggle="modal" data-bs-target="#addStatusModal" v-if="authUser.designation == 'sales_manager' || authUser.role=='admin'"
                                        style="border: none; border-radius: 0px 8px 8px 0px; outline: none; background-color: cornflowerblue; color: white; font-weight: 600;">Add</button>
                                </div>
                            </div>
                            <div class="col-md-4">
                                <label for="api_integration" class="form-label">APIs Integration</label>
                                <input class="form-control" type="text" name="" id="api_integration" v-model="apiInfo">
                            </div>
                            <div class="col-md-4">
                                <label for="project_refrence" class="form-label">Project Refrence</label>
                                <input class="form-control" type="text" name="" id="project_refrence" v-model="projectRefrence">
                            </div>
                        </div>
                        <div class="row mb-8 mt-3">
                            <div class="col-lg-12 col-md-12">
                                <label for="type" class="form-label">Project Objective</label>
                                <QuillEditor required ref="editor" theme="snow" toolbar="full" v-model:content="projectObjective" contentType="html" />
                            </div>
                        </div>
                        <div class="row mb-8 mt-2">
                            <div class="col-lg-12 col-md-12">
                                <label for="type" class="form-label">Project Functional Requirements</label>
                                <QuillEditor required ref="editor" theme="snow" toolbar="full" v-model:content="projectFuncRequire" contentType="html"/>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <h5>Time Frame</h5>
                            <div class="col-md-4">
                                <label class="form-label" for="start-date">Start Date</label>
                                <input @change="calculateWorkingDays" v-model="timeFrame.startDate" class="form-control"
                                    type="date" name="start-date" required>
                            </div>
                            <div class="col-md-4">
                                <label class="form-label" for="end-date">End Date</label>
                                <input @change="calculateWorkingDays" v-model="timeFrame.endDate" class="form-control"
                                    type="date" name="end-date" required>
                            </div>
                            <div class="col-md-4">
                                <label class="form-label" for="workingDays">Working Days</label>
                                <input disabled v-model="timeFrame.workingDays" class="form-control" type="text"
                                    name="workingDays" required>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <h5>Tech Specification</h5>
                            <div class="col-md-4 mb-3">
                                <label style="" for="email" class="form-label">Frontend</label>
                                <input class="form-control" v-model="techSpecs.frontEnd" required>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label style="" for="email" class="form-label">Backend</label>
                                <input class="form-control" v-model="techSpecs.backEnd" required>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label style="" for="email" class="form-label">Databases</label>
                                <input class="form-control" v-model="techSpecs.dataBase" required>
                            </div>
                        </div>
                        <div>
                            <div class="row" style="margin: 13px 0px -20px -10px">
                                <div class="col-md-3">
                                    <h5>Milestones</h5>
                                </div>
                                <div class="col-md-3">
                                    <button @click="milestoneClonner" type="button"
                                        class="btn btn-primary px-2 py-1 text-sm"
                                        style="margin-left: -100px; outline: none;">Add</button>
                                </div>
                            </div>
                            <div v-for="(data, index) in milestoneClonnerData" :key="index" class="row mt-3">
                                <div class="col-md-3 mb-3">
                                    <label style="" for="name" class="form-label">Name</label>
                                    <input :disabled="!projectCost" class="form-control" v-model="data.name" required>
                                </div>
                                <div class="col-md-3 mb-3">
                                    <label style="" for="cost" class="form-label">Cost</label>
                                    <input :disabled="!projectCost" class="form-control" v-model="data.cost" required>
                                </div>
                                <div class="col-md-3 mb-3">
                                    <label style="" for="date" class="form-label">Delivery Date</label>
                                    <input :disabled="!projectCost" class="form-control" v-model="data.delivery_date"
                                        required>
                                </div>
                                <div v-if="milestoneClonnerData.length > 1" class="col-md-3 mb-3">
                                    <label for="" class="form-label"></label>
                                    <button type="button" @click="milestoneRemover(index)"
                                        class="btn btn-danger form-control">Delete</button>
                                </div>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <div class="col">
                                <label for="desclaimer_status" class="form-label"><h5>Desclaimer Templates</h5></label>
                                <div class="input-group">
                                    <select v-model="selectedDesclaimer" class="form-select" name="" id="">
                                        <option selected value="">Select Status</option>
                                        <option v-for="status in desclaimerStatus" :key="status.id" :value="status.id">{{ status.title }}
                                        </option>
                                    </select>
                                    <button data-bs-toggle="modal" data-bs-target="#addDesclaimerModal" v-if="authUser.designation == 'sales_manager' || authUser.role=='admin'"
                                        style="border: none; border-radius: 0px 8px 8px 0px; outline: none; background-color: cornflowerblue; color: white; font-weight: 600;">Add</button>
                                </div>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <div class="col">
                                <label for="about_status" class="form-label"><h5>About Templates</h5></label>
                                <div class="input-group">
                                    <select v-model="selectedAboutTemplate" class="form-select" name="" id="">
                                        <option selected value="">Select Status</option>
                                        <option v-for="status in aboutStatus" :key="status.id" :value="status.id">{{ status.title }}
                                        </option>
                                    </select>
                                    <button data-bs-toggle="modal" data-bs-target="#addAboutModal" v-if="authUser.designation == 'sales_manager' || authUser.role=='admin'"
                                        style="border: none; border-radius: 0px 8px 8px 0px; outline: none; background-color: cornflowerblue; color: white; font-weight: 600;">Add</button>
                                </div>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <div class="col">
                                <label for="nda_status" class="form-label"><h5>NDA Templates</h5></label>
                                <div class="input-group">
                                    <select v-model="selectedNdaTemplate" class="form-select" name="" id="">
                                        <option selected value="">Select Status</option>
                                        <option v-for="status in ndaStatus" :key="status.id" :value="status.id">{{ status.title }}
                                        </option>
                                    </select>
                                    <button data-bs-toggle="modal" data-bs-target="#addNdaModal" v-if="authUser.designation == 'sales_manager' || authUser.role=='admin'"
                                        style="border: none; border-radius: 0px 8px 8px 0px; outline: none; background-color: cornflowerblue; color: white; font-weight: 600;">Add</button>
                                </div>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <div class="col col-md-3">
                                <input type="radio" name="GST" id="" v-model="selectedGST" value="GST"> IGST@18%
                            </div>
                            <div class="col col-md-3">
                                <input type="radio" name="GST" id="" v-model="selectedGST" value="CGST_SGST"> CGST,SGST@9%
                            </div>
                        </div>
                        <div class="modal-footer"
                            style="z-index: 999; margin-top: 15px; position: sticky; bottom: 0; background-color: white; margin-bottom: -500px;">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                                @click="resetValues">Close</button>
                            <button type="submit" class="btn btn-primary">Create</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <!-- MODAL FOR CREATE PROPOSAL END -->

    <!-- MODAL FOR EDIT PROPOSAL START -->
    <div style="margin-left:-100px;" data-bs-backdrop="static" class="modal fade" ref="createProposalModal"
        id="editProposalModal" tabindex="-1" aria-labelledby="createadminLabel" aria-hidden="true">
        <div style="width:auto" class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="padding-bottom: 0;padding-left: 7px; padding-right: 7px; width:auto">
                <div class="modal-header">
                    <h5 class="modal-title" id="createadminLabel">Edit Proposal</h5>
                    <button ref="createProposalBtn" type="button" class="btn-close bg-dark text-xs"
                        data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body modalBody" style="padding-bottom: 0; height:35rem; width: 890px;">
                    <form @submit.prevent="updateProposalData">
                        <div class="row">
                            <div class="col-md-4 mb-3">
                                <label for="Client" class="form-label">Client</label>
                                <input type="text" class="form-control" v-model="editProposalData.sale_data.client" disabled>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="email" class="form-label">Email</label>
                                <input type="text" class="form-control" v-model="editProposalData.sale_data.email" disabled>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="contact_no" class="form-label">Mobile No.</label>
                                <input type="text" class="form-control" v-model="editProposalData.sale_data.contact_no" disabled>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-4 mb-3">
                                <label for="project_types" class="form-label">Project Type</label>
                                <select class="form-control" v-model="editProposalData.project_type">
                                    <option value="">Select Type</option>
                                    <option value="ERPS">Enterprise Resource Planning System (ERPS)</option>
                                    <option value="CRM">Customer Engagement Platform (CRM)</option>
                                    <option value="E-Com">Online Retail Platform (E-Com)</option>
                                    <option value="Game_Dev">Interactive Entertainment Solutions (Game_Dev)</option>
                                    <option value="WordPress">Dynamic Web Content Management (WordPress)</option>
                                    <option value="Magento">E-Commerce Powerhouse (Magento)</option>
                                    <option value="Shopify">E-Commerce Simplified (Shopify)</option>
                                    <option value="Mobile Application">Mobile Application Solutions</option>
                                    <option value="Web Presence">Web Presence Solutions</option>
                                </select>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="project_name" class="form-label">Project Name</label>
                                <input type="text" class="form-control" v-model="editProposalData.project_name">
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="project_cost" class="form-label">Project Cost</label>
                                <div class="input-group">
                                    <input v-model="editProposalData.project_cost" type="text" class="form-control" id="project_cost"
                                        style="width: 78%;">
                                    <select class="form-select currency" v-model="selectedCurr"
                                        aria-label="Currency select" style="width:22%;">
                                        <option value="INR">INR</option>
                                        <option value="USD">USD</option>
                                        <option value="EUR">EUR</option>
                                        <option value="CAD">CAD</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-4">
                                <label for="status" class="form-label">Status</label>
                                <div class="input-group">
                                    <select v-model="editProposalData.status.pk" class="form-select" name="" id="">
                                        <option selected value="">Select Status</option>
                                        <option v-for="status in quoteStatus" :key="status.id" :value="status.id">{{ status.name }}
                                        </option>
                                    </select>
                                    <button data-bs-toggle="modal" data-bs-target="#addStatusModal" v-if="authUser.designation == 'sales_manager'"
                                        style="border: none; border-radius: 0px 8px 8px 0px; outline: none; background-color: cornflowerblue; color: white; font-weight: 600;">Add</button>
                                </div>
                            </div>
                            <div class="col-md-4">
                                <label for="api_integration" class="form-label">APIs Integration</label>
                                <input class="form-control" type="text" name="" id="api_integration" v-model="editProposalData.api_info">
                            </div>
                            <div class="col-md-4">
                                <label for="project_refrence" class="form-label">Project Refrence</label>
                                <input class="form-control" type="text" name="" id="project_refrence" v-model="editProposalData.project_ref">
                            </div>
                        </div>
                        <div class="row mb-8 mt-3">
                            <div class="col-lg-12 col-md-12">
                                <label for="type" class="form-label">Project Objective</label>
                                <QuillEditor required ref="editor" theme="snow" toolbar="full" v-model:content="editProposalData.objectives" contentType="html" />
                            </div>
                        </div>
                        <div class="row mb-8 mt-2">
                            <div class="col-lg-12 col-md-12">
                                <label for="type" class="form-label">Project Functional Requirements</label>
                                <QuillEditor required ref="editor" theme="snow" toolbar="full" v-model:content="editProposalData.project_desc" contentType="html"/>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <h5>Time Frame</h5>
                            <div class="col-md-4">
                                <label class="form-label" for="start-date">Start Date</label>
                                <input @change="updatecalculateWorkingDays" v-model="editProposalData.time_frame.startDate" class="form-control"
                                    type="date" name="start-date" required>
                            </div>
                            <div class="col-md-4">
                                <label class="form-label" for="end-date">End Date</label>
                                <input @change="updatecalculateWorkingDays" v-model="editProposalData.time_frame.endDate" class="form-control"
                                    type="date" name="end-date" required>
                            </div>
                            <div class="col-md-4">
                                <label class="form-label" for="workingDays">Working Days</label>
                                <input disabled v-model="editProposalData.time_frame.workingDays" class="form-control" type="text"
                                    name="workingDays" required>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <h5>Tech Specification</h5>
                            <div class="col-md-4 mb-3">
                                <label style="" for="email" class="form-label">Frontend</label>
                                <input class="form-control" v-model="editProposalData.tech_specs.frontEnd" required>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label style="" for="email" class="form-label">Backend</label>
                                <input class="form-control" v-model="editProposalData.tech_specs.backEnd" required>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label style="" for="email" class="form-label">Databases</label>
                                <input class="form-control" v-model="editProposalData.tech_specs.dataBase" required>
                            </div>
                        </div>
                        <div>
                            <div class="row" style="margin: 13px 0px -20px -10px">
                                <div class="col-md-3">
                                    <h5>Milestones</h5>
                                </div>
                                <div class="col-md-3">
                                    <button @click="editmilestoneClonner" type="button"
                                        class="btn btn-primary px-2 py-1 text-sm"
                                        style="margin-left: -100px; outline: none;">Add</button>
                                </div>
                            </div>
                            <div v-for="(data, index) in editProposalData.milestones" :key="index" class="row mt-3">
                                <div class="col-md-3 mb-3">
                                    <label style="" for="name" class="form-label">Name</label>
                                    <input :disabled="!editProposalData.project_cost" class="form-control" v-model="data.name" required>
                                </div>
                                <div class="col-md-3 mb-3">
                                    <label style="" for="cost" class="form-label">Cost</label>
                                    <input :disabled="!editProposalData.project_cost" class="form-control" v-model="data.cost" required>
                                </div>
                                <div class="col-md-3 mb-3">
                                    <label style="" for="date" class="form-label">Delivery Date</label>
                                    <input :disabled="!editProposalData.project_cost" class="form-control" v-model="data.delivery_date"
                                        required>
                                </div>
                                <div v-if="editProposalData.milestones.length > 1" class="col-md-3 mb-3">
                                    <label for="" class="form-label"></label>
                                    <button type="button" @click="editmilestoneRemover(index)"
                                        class="btn btn-danger form-control">Delete</button>
                                </div>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <div class="col">
                                <label for="desclaimer_status" class="form-label"><h5>Desclaimer Templates</h5></label>
                                <div class="input-group">
                                    <select v-model="this.editProposalData.disclaimer.pk" class="form-select" name="" id="">
                                        <option selected value="">Select Status</option>
                                        <option v-for="status in desclaimerStatus" :key="status.id" :value="status.id">{{ status.title }}
                                        </option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <div class="col">
                                <label for="about_status" class="form-label"><h5>About Templates</h5></label>
                                <div class="input-group">
                                    <select v-model="this.editProposalData.about_us.pk" class="form-select" name="" id="">
                                        <option selected value="">Select Status</option>
                                        <option v-for="status in aboutStatus" :key="status.id" :value="status.id">{{ status.title }}
                                        </option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <div class="col">
                                <label for="nda_status" class="form-label"><h5>NDA Templates</h5></label>
                                <div class="input-group">
                                    <select v-model="this.editProposalData.nda.pk" class="form-select" name="" id="">
                                        <option selected value="">Select Status</option>
                                        <option v-for="status in ndaStatus" :key="status.id" :value="status.id">{{ status.title }}
                                        </option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <div class="col col-md-3">
                                <input type="radio" name="GST" id="" v-model="editProposalData.gst_details" value="GST"> IGST@18%
                            </div>
                            <div class="col col-md-3">
                                <input type="radio" name="GST" id="" v-model="editProposalData.gst_details" value="CGST_SGST"> CGST,SGST@9%
                            </div>
                        </div>
                        <div class="modal-footer"
                            style="z-index: 999; margin-top: 15px; position: sticky; bottom: 0; background-color: white; margin-bottom: -500px;">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                                @click="resetValues">Close</button>
                            <button type="submit" class="btn btn-primary">Save changes</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <!-- MODEL FOR EDIT PROPOSAL END -->


    <!--Table Start-->
    <div class="card" style="margin-top: 2rem; padding: 5px;">
          <div class="card-header pb-0">
            <h6>Proposal Table</h6>
          </div>
          <div class="card-body px-0 pt-0 pb-2">
            <div class="table-responsive p-0">
              <table class="table align-items-center mb-0">
                <thead style="position: sticky; top: 0; background-color: white; z-index: 2;">
                  <tr>
                    <th style="color: #344767 !important;"
                    class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold">S.NO.</th>
                      <th style="color: #344767 !important;"
                      class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold">CLIENT NAME</th>
                      <th style="color: #344767 !important;"
                      class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold">MOBILE</th>
                      <th style="color: #344767 !important;"
                      class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold">REQUIREMENT</th>
                      <th style="color: #344767 !important;"
                      class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold">STATUS</th>
                    <th style="color: #344767 !important;"
                      class="text-uppercase text-secondary text-xs font-weight-bolder font-weight-bold action-head">
                      Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="tableRow" v-for="(status,index) in paginatedProjects" :key="status.id">
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-left">
                        <h6 class="mb-0 text-sm">{{ (currentPage - 1) * itemsPerPage + index + 1 }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-left">
                        <h6 class="mb-0 text-sm">{{ status.sale_data.client }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-left">
                        <h6 class="mb-0 text-sm">{{ status.sale_data.contact_no }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-left">
                        <h6 class="mb-0 text-sm">{{ truncatedDesc(status.project_desc) }}</h6>
                      </div>
                    </td>
                    <td style="padding-left: 25px;">
                      <div class="d-flex flex-column justify-content-left">
                        <h6 class="mb-0 text-sm">{{ status.status.name}}</h6>
                      </div>
                    </td>
                    <td class="align-middle d-md-table-cell actions">
                      <i title="Download Propsal pdf" class="fas fa-eye text-info mx-3 icon"
                        style="cursor: pointer;"
                        data-bs-toggle="modal" data-bs-target="#viewProposalModal"
                        @click="generatePDF(status)"></i>
                      <i title="Duplicate Proposal" class="fas fa-copy text-secondary mx-3 icon"
                        style="cursor: pointer;"
                        data-bs-toggle="modal"
                        @click="duplicateProposal(status)"></i>
                      <i title="Edit Proposal" class="fas fa-pencil-alt text-primary mx-3 icon"
                        style="margin-left: 20px; cursor: pointer;" data-bs-toggle="modal" data-bs-target="#editProposalModal" @click="editProposal(status)"></i>
                      <i title="Delete Propsal" data-bs-toggle="modal" data-bs-target="#" @click="deleteProposal(status.id)"
                        class="fas fa-trash text-danger m-3 mx-3 icon" style="cursor: pointer;"></i>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <PaginationComponent v-if="allProposal.length > itemsPerPage" :currentPage="currentPage"
            :itemsPerPage="itemsPerPage" :prevPage="prevPage" :nextPage="nextPage" :filteredUsers="filteredProjects"
            :goToPage="goToPage" />
        </div>
        <ProposalPdfData :dynamicDesclaimer="pdfproject_desclaimer" :dynamicNda="pdfproject_nda" :dynamicAbout="pdfproject_about" :dynamicClientName="pdfClientName" :dynamicClientEmail="pdfClientEmail" :dynamicClientPhone="pdfClientPhone" :dynamicProjectType="pdfProjectType" :dynamicProjectName="pdfProjectName" :dynamicProjectCost="pdfProjectCost" :dynamicProjectGST="pdfProjectGST" :dynamicApiIntegration="pdfApiIntegration" :dynamicProjectRefrence="pdfProjectRefrence" :dynamicProjectObjective="pdfProjectObjective" :dynamicProjectRequirement="pdfProjectRequirement" :dynamicTimeFrameStart="pdfTimeFrameStart" :dynamicTimeFrameEnd="pdfTimeFrameEnd" :dynamicTimeFrameWorking="pdfTimeFrameWorking" :dynamicMilestoneName="pdfMilestoneName" :dynamicMilestoneCost="pdfMilestoneCost" :dynamicMilestoneDeliveryDate="pdfMilestoneDeliveryDate" :dynamicTechSpecsFrontend="pdfTechSpecsFrontend" :dynamicTechSpecsBackend="pdfTechSpecsBackend" :dynamicTechSpecsDatabase="pdfTechSpecsDatabase" :dynamicMilestone="pdfMilestone"/>
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
import html2pdf from 'html2pdf.js';
import ProposalPdfData from './PropsalTemplate/ProposalTemplate1.vue';

export default {
    name: "Proposal",
    components: {
        QuillEditor,
        PaginationComponent,
        ProposalPdfData
    },
    data() {
        return {
            pdfClientName: '',
            pdfClientEmail: '',
            pdfClientPhone: '',
            pdfProjectType: '',
            pdfProjectName: '',
            pdfProjectCost: '',
            pdfProjectGST: '',
            pdfApiIntegration: '',
            pdfProjectRefrence:'',
            pdfProjectObjective:'',
            pdfProjectRequirement: '',
            pdfTimeFrameStart: '',
            pdfTimeFrameEnd: '',
            pdfTimeFrameWorking: '',
            pdfMilestoneName: '',
            pdfMilestoneCost: '',
            pdfMilestoneDeliveryDate: '',
            pdfMilestone: '',
            pdfTechSpecsFrontend: '',
            pdfTechSpecsBackend: '',
            pdfTechSpecsDatabases: '',
            pdfproject_desclaimer:'',
            pdfproject_nda:'',
            pdfproject_about:'',
            currentPage: 1,
            itemsPerPage: 10,
            allProposal: [],
            clientNameFilter: '',
            contactNoFilter: '',
            statusFilter:'',
            quoteStatus: [],
            desclaimerStatus: [],
            aboutStatus: [],
            ndaStatus:[],
            allSales: [],
            selectedClientID: '',
            selectedClient: null,
            project_type: '',
            project_type_filter: '',
            projectCost: null,
            selectedCurr: 'INR',
            milestoneClonnerData: [{ 'name': '', 'cost': '', 'delivery_date': '' }],
            timeFrame: {
                startDate: '',
                endDate: '',
                workingDays: ''
            },
            selectedStatus: '',
            selectedDesclaimer: '',
            selectedAboutTemplate:'',
            selectedNdaTemplate: '',
            AddStatusModalToggler: false,
            newStatus: '',
            newDesclaimerTitle: '',
            newDesclaimerDesc: '',
            newAboutTitle:'',
            newAboutDesc:'',
            newNdaTitle:'',
            newNdaDesc:'',
            projectName: '',
            apiInfo:'',
            techSpecs:{
                frontEnd:'',
                backEnd: '',
                dataBase:''
            },
            selectedGST: '',
            projectFuncRequire: '',
            projectObjective: '',
            projectRefrence:'',
            getProposal: [],
            editProposalData:{
                id:'',
                sale_data:{
                    id: '',
                    client: '',
                    contact_no: '',
                    email: '',
                    requirement: '',
                    temp_data: '',
                    is_assigned: '',
                    created_date: ''
                },
            project_type: '',
            project_name: '',
            project_desc: '',
            project_cost: '',
            project_ref: '',
            gst_details: '',
            milestones: [{ 'name': '', 'cost': '', 'delivery_date': '' }],
            time_frame: {
                endDate: '',
                startDate: '',
                workingDays: ''
            },
            objectives: '',
            tech_specs: {
                backEnd: '',
                dataBase: '',
                frontEnd: ''
            },
            api_info:'',
            status: {
                pk: '',
                name: ''
            },
            about_us: {
                pk: '',
                title: '',
                desc: ''
            },
            disclaimer: {
                pk: '',
                title: '',
                desc: ''
            },
            nda: {
                pk: '',
                title: '',
                desc: ''
            },
            }
        }
    },
    computed: {
        ...mapState(['authUser', 'authToken']),
        filteredProjects() {
        return this.allProposal.filter(proposal => {
            const searchLowerCase = this.clientNameFilter.toLowerCase() || this.contactNoFilter.toLowerCase() || this.project_type_filter.toLowerCase() || this.statusFilter.toLowerCase()
            return (
                proposal.sale_data.client.toLowerCase().includes(searchLowerCase) ||
                proposal.sale_data.contact_no.toLowerCase().includes(searchLowerCase) ||
                proposal.project_type.toLowerCase().includes(searchLowerCase) ||
                proposal.status.name.toLowerCase().includes(searchLowerCase)
            );
        });
        },
        paginatedProjects() {
            const startIndex = (this.currentPage - 1) * this.itemsPerPage;
            return this.filteredProjects.slice(startIndex, startIndex + this.itemsPerPage);
        },
        truncatedDesc() {
            return (desc) => desc.length > 15 ? desc.substring(0, 15) + '...' : desc;
        }
    },
    methods: {
        async generatePDF(status) {
            this.pdfproject_desclaimer = status.disclaimer.desc
            this.pdfproject_nda = status.nda.desc
            this.pdfproject_about = status.about_us.desc
            this.pdfClientName = status.sale_data.client
            this.pdfClientEmail = status.sale_data.email
            this.pdfClientPhone = status.sale_data.contact_no
            this.pdfProjectType = status.project_type
            this.pdfProjectName = status.project_name
            this.pdfProjectCost = status.project_cost
            this.pdfProjectGST = status.gst_details
            this.pdfApiIntegration = status.api_info
            this.pdfProjectRefrence = status.project_ref
            this.pdfProjectObjective = status.objectives
            this.pdfProjectRequirement = status.project_desc
            this.pdfTimeFrameStart = status.time_frame.startDate
            this.pdfTimeFrameEnd = status.time_frame.endDate
            this.pdfTimeFrameWorking = status.time_frame.workingDays
            this.pdfTechSpecsFrontend = status.tech_specs.frontEnd
            this.pdfTechSpecsBackend = status.tech_specs.backEnd
            this.pdfTechSpecsDatabase = status.tech_specs.dataBase
            this.pdfMilestone = status.milestones
            await this.$nextTick();
            let html = document.getElementById('pdf').innerHTML;
            const opt = {
                margin: 0,
                filename: 'proposal.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 2 },
                jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' }
            };

            try {
            const pdf = await html2pdf().from(html).set(opt).outputPdf('blob');
            const url = URL.createObjectURL(pdf);
            window.open(url, '_blank');
            new Noty({
                type: 'success',
                text: 'PDF opened successfully',
                timeout: 2000,
            }).show();
            } catch(error) {
            new Noty({
                type: 'error',
                text: 'Failed to generate PDF: ' + error.message,
                timeout: 2000,
            }).show();
        };
        },
        nextPage() {
        if (this.currentPage * this.itemsPerPage < this.filteredProjects.length) {
            this.currentPage++;
            this.updateDisplayedProposal();
        }
        },
        prevPage() {
        if (this.currentPage > 1) {
            this.currentPage--;
            this.updateDisplayedProposal();
        }
        },
        goToPage(page) {
            this.currentPage = page;
            this.updateDisplayedProposal();
        },
        updateDisplayedProposal() {
            const startIndex = (this.currentPage - 1) * this.itemsPerPage;
            this.getProposal = this.allProposal.slice(startIndex, startIndex + this.itemsPerPage);
        },
        async getSalesEmployee() {
            try {
                const response = await axios.get(`${BASE_URL}api/sales/getAllEmployees`, {
                    headers: {
                        token: this.authToken
                    }
                })
                if (response.status === 200) {
                    this.allAssignee = response.data.employee_data;
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message? error.response.data.message: error.response.data.detail,
                    timeout: 1000,
                }).show()
            }
        },
        milestoneClonner() {
            if (!this.projectCost) {
                new Noty({
                    type: 'info',
                    text: 'Please enter project Cost',
                    timeout: 500,
                }).show()
            }
            else {
                let milestonesCost = 0
                this.milestoneClonnerData.forEach((item) => {
                    milestonesCost += Number(item.cost)
                })
                if (milestonesCost >= Number(this.projectCost)) {
                    new Noty({
                        type: 'error',
                        text: 'Total sum of milestones cost should not exceeds the project cost',
                        timeout: 1000,
                    }).show()
                    return
                }
                else {
                    this.milestoneClonnerData.push({ name: '', cost: '', delivery_date: '' })
                }
            }
        },
        milestoneRemover(ind) {
            this.milestoneClonnerData.splice(ind, 1)
        },
        editmilestoneClonner() {
            if (!this.editProposalData.project_cost) {
                new Noty({
                    type: 'info',
                    text: 'Please enter project Cost',
                    timeout: 500,
                }).show()
            }
            else {
                let milestonesCost = 0
                this.editProposalData.milestones.forEach((item) => {
                    milestonesCost += Number(item.cost)
                })
                if (milestonesCost >= Number(this.editProposalData.project_cost)) {
                    new Noty({
                        type: 'error',
                        text: 'Total sum of milestones cost should not exceeds the project cost',
                        timeout: 1000,
                    }).show()
                    return
                }
                else {
                    this.editProposalData.milestones.push({ name: '', cost: '', delivery_date: '' })
                }
            }
        },
        editmilestoneRemover(ind) {
            this.editProposalData.milestones.splice(ind, 1)
        },
        getQuoteStatus() {
            try {
                axios.get(`${BASE_URL}/api/development/proposal/status`, {
                    headers: {
                        "token": this.authToken
                    }
                }).then((res) => {
                    this.quoteStatus = res.data.data

                })
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 500,
                }).show()
            }
        },
        getDesclaimerStatus() {
            try {
                axios.get(`${BASE_URL}/api/development/proposal/disclaimer`, {
                    headers: {
                        "token": this.authToken
                    }
                }).then((res) => {
                    this.desclaimerStatus = res.data.data

                })
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 500,
                }).show()
            }
        },
        getAboutStatus() {
            try {
                axios.get(`${BASE_URL}/api/development/proposal/aboutUs`, {
                    headers: {
                        "token": this.authToken
                    }
                }).then((res) => {
                    this.aboutStatus = res.data.data

                })
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 500,
                }).show()
            }
        },
        getNdaStatus() {
            try {
                axios.get(`${BASE_URL}/api/development/proposal/nda`, {
                    headers: {
                        "token": this.authToken
                    }
                }).then((res) => {
                    this.ndaStatus = res.data.data
                })
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 500,
                }).show()
            }
        },
        getALLSales() {
            try {
                axios.get(`${BASE_URL}/api/sales/`, {
                    headers: {
                        "token": this.authToken
                    }
                }).then((res) => {
                    this.allSales = res.data.res_data
                })
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 500,
                }).show()
            }
        },
        clientHandler(newVal, oldVal) {
            try {
                if (oldVal !== newVal && newVal !== "") {
                    this.selectedClient = this.allSales.find((client) => client.id == newVal)
                    if (!this.selectedClient) {
                        throw new Error("No lead found for the given ID")
                    }
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.message,
                    timeout: 500,
                }).show()
            }
        },
        calculateWorkingDays() {
            let d1 = new Date(this.timeFrame.startDate);
            let d2 = new Date(this.timeFrame.endDate);

            if (!this.timeFrame.startDate || !this.timeFrame.endDate) {
                new Noty({
                    type: "error",
                    text: "Please select both start and end dates",
                    timeout: 1000
                }).show();
                return;
            }

            if (d2 <= d1) {
                new Noty({
                    type: "error",
                    text: "Please select a valid date range",
                    timeout: 1000
                }).show();
                return;
            }

            if (d2.getDate() - d1.getDate() > 3650) {
                new Noty({
                    type: "info",
                    text: "Don't try to be oversmart",
                    timout: 1000
                }).show();
                return;
            }

            function getWorkingDays(startDate, endDate) {
                let totalDays = 0;
                let currentDate = startDate;

                while (currentDate <= endDate) {
                    let dayOfWeek = currentDate.getDay();
                    if (dayOfWeek !== 0 && dayOfWeek !== 6) {
                        totalDays++;
                    }
                    currentDate.setDate(currentDate.getDate() + 1);
                }
                return totalDays;
            }

            this.timeFrame.workingDays = getWorkingDays(d1, d2);
        },
        updatecalculateWorkingDays() {
            let d1 = new Date(this.editProposalData.time_frame.startDate);
            let d2 = new Date(this.editProposalData.time_frame.endDate);

            if (!this.editProposalData.time_frame.startDate || !this.editProposalData.time_frame.endDate) {
                new Noty({
                    type: "error",
                    text: "Please select both start and end dates",
                    timeout: 1000
                }).show();
                return;
            }

            if (d2 <= d1) {
                new Noty({
                    type: "error",
                    text: "Please select a valid date range",
                    timeout: 1000
                }).show();
                return;
            }

            if (d2.getDate() - d1.getDate() > 3650) {
                new Noty({
                    type: "info",
                    text: "Don't try to be oversmart",
                    timout: 1000
                }).show();
                return;
            }

            function updategetWorkingDays(startDate, endDate) {
                let totalDays = 0;
                let currentDate = startDate;

                while (currentDate <= endDate) {
                    let dayOfWeek = currentDate.getDay();
                    if (dayOfWeek !== 0 && dayOfWeek !== 6) {
                        totalDays++;
                    }
                    currentDate.setDate(currentDate.getDate() + 1);
                }
                return totalDays;
            }

            this.editProposalData.time_frame.workingDays = updategetWorkingDays(d1, d2);
        },
        addStatus(e) {
            e.preventDefault()
            try {
                this.$store.commit("showLoader")
                axios.post(`${BASE_URL}/api/development/proposal/status`, {
                    statusName: this.newStatus
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
                        this.newStatus=''
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
        addAbout(e) {
            e.preventDefault()
            try {
                this.$store.commit("showLoader")
                axios.post(`${BASE_URL}/api/development/proposal/aboutUs`, {
                    title: this.newAboutTitle,
                    desc: this.newAboutDesc
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
                        this.newAboutTitle=''
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
        addNDA(e) {
            e.preventDefault()
            try {
                this.$store.commit("showLoader")
                axios.post(`${BASE_URL}/api/development/proposal/nda`, {
                    title: this.newNdaTitle,
                    desc: this.newNdaDesc
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
                        this.newNdaTitle=''
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
        createProposal(e) {
            e.preventDefault();
            try {
                this.$store.commit("showLoader")
                axios.post(`${BASE_URL}/api/development/proposal`, {
                    statusID: this.selectedStatus,
                    saleID: this.selectedClientID,
                    disclaimerID:this.selectedDesclaimer,
                    aboutID:this.selectedAboutTemplate,
                    nda_id:this.selectedNdaTemplate,
                    project_type: this.project_type,
                    project_name: this.projectName,
                    project_cost: this.projectCost,
                    gst_details: this.selectedGST,
                    milestones:this.milestoneClonnerData,
                    time_frame: this.timeFrame,
                    project_ref: this.projectRefrence,
                    desc: this.projectFuncRequire,
                    objectives: this.projectObjective,
                    tech_specs: this.techSpecs,
                    api_specs: this.apiInfo
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
                        this.selectedStatus=''
                        this.selectedClientID=''
                        this.selectedDesclaimer=''
                        this.selectedAboutTemplate=''
                        this.selectedNdaTemplate=''
                        this.project_type=''
                        this.projectName=''
                        this.projectCost=''
                        this.projectRefrence=''
                        this.timeFrame=''
                        this.projectFuncRequire=''
                        this.projectObjective=''
                        this.techSpecs=''
                        this.apiInfo=''
                        this.milestoneClonnerData=''
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
        async getProposalData() {
            try {
                const res = await axios.get(`${BASE_URL}/api/development/proposal`, {
                    headers: {
                        "token": this.authToken
                    }
                });
                if (res.status === 200) {
                    this.getProposal = res.data.message;
                    this.allProposal = res.data.message;
                    this.updateDisplayedProposal();
                } else {
                    throw new Error('Unexpected response status');
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 500,
                }).show()
            }
        },
        async deleteProposal(id) {
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
                        const response = await axios.delete(`${BASE_URL}api/development/proposal?id=${id}`, {
                            headers: {
                                token: this.authToken
                            }
                        })
                        if (response.status === 204) {
                            Swal.fire('Deleted!', response.data.message, 'success');
                            window.location.reload()
                        }
                        this.getProposalData();
                    } catch (error) {
                        this.getProposalData();
                        Swal.fire('Error!', error.response.data.message ? error.response.data.message : error.response.data.detail, 'error');
                    }
                }
            });
        },
        editProposal(status) {
            this.editProposalData={
                id:status.id,
                sale_data: status.sale_data,
                project_type: status.project_type,
                project_name: status.project_name,
                project_desc: status.project_desc,
                project_cost: status.project_cost,
                project_ref: status.project_ref,
                gst_details: status.gst_details,
                milestones: status.milestones,
                time_frame: status.time_frame,
                objectives: status.objectives,
                tech_specs: status.tech_specs,
                api_info:status.api_info,
                status: status.status,
                about_us: status.about_us,
                disclaimer: status.disclaimer,
                nda: status.nda,
                };
        },
        async updateProposalData(e) {
            e.preventDefault();
            try {
                console.log(this.editProposalData.sale_data.id)
                const response = await axios.put(`${BASE_URL}/api/development/proposal`, {
                                    id:this.editProposalData.id,
                                    saleID: this.editProposalData.sale_data.id,
                                    statusID: this.editProposalData.status.pk,
                                    disclaimerID:this.editProposalData.disclaimer.pk,
                                    aboutID:this.editProposalData.about_us.pk,
                                    nda_id:this.editProposalData.nda.pk,
                                    project_type: this.editProposalData.project_type,
                                    project_name: this.editProposalData.project_name,
                                    project_cost: this.editProposalData.project_cost,
                                    gst_details: this.editProposalData.gst_details,
                                    milestones:this.editProposalData.milestones,
                                    time_frame: this.editProposalData.time_frame,
                                    project_ref: this.editProposalData.project_ref,
                                    desc: this.editProposalData.project_desc,
                                    objectives: this.editProposalData.objectives,
                                    tech_specs: this.editProposalData.tech_specs,
                                    api_specs: this.editProposalData.api_info
                }, {
                    headers: {
                        'Content-Type': "application/json",
                        token: this.authToken
                    },
                });

                if (response.status === 200) {
                    new Noty({
                        "type": "success",
                        "text": "Propsal updated successfully",
                        "timeout": 2000
                    }).show();
                    setTimeout(()=>{
                    window.location.reload()
                    },1100)
                    this.$store.commit("hideLoader")
                    this.getProposalData();
                }
            } catch (error) {
                new Noty({
                    type: 'error',
                    text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                    timeout: 1000,
                }).show();
            }
        },
        async duplicateProposal(proposal) {
            try {
                const newProposal = JSON.parse(JSON.stringify(proposal));

                this.$store.commit("showLoader");
                await axios.post(`${BASE_URL}/api/development/proposal`, {
                                            statusID: newProposal.status.pk,
                                            saleID: newProposal.sale_data.id,
                                            disclaimerID:newProposal.disclaimer.pk,
                                            aboutID:newProposal.about_us.pk,
                                            nda_id:newProposal.nda.pk,
                                            project_type: newProposal.project_type,
                                            project_name: newProposal.project_name,
                                            project_cost: newProposal.project_cost,
                                            gst_details: newProposal.gst_details,
                                            milestones:newProposal.milestones,
                                            time_frame: newProposal.time_frame,
                                            project_ref: newProposal.project_ref,
                                            desc: newProposal.project_desc,
                                            objectives: newProposal.objectives,
                                            tech_specs: newProposal.tech_specs,
                                            api_specs: newProposal.api_info
                }, {
                    headers: {
                    'Content-Type': "application/json",
                    token: this.authToken
                },
                }).then((res) => {
                    if(res.status===201){
                        new Noty({
                            "type":"success",
                            "text": "Propsal Duplicate Successfully",
                            "timeout":2000
                        }).show()
                    }
                    setTimeout(()=>{
                    window.location.reload()
                    },1100)
                    this.$store.commit("hideLoader")
                })
                } catch (error) {
                    new Noty({
                        type: 'error',
                        text: error.response.data.message ? error.response.data.message : error.response.data.detail,
                        timeout: 1000,
                    }).show();
                }
                finally {
                    this.$store.commit("hideLoader");
                }
        },
        resetValues() {
            window.location.reload()
        },
        resestFilter(){
            this.clientNameFilter = '',
            this.contactNoFilter = '',
            this.project_type_filter = '',
            this.statusFilter = ''
        }
    },
    watch: {
        selectedClientID(newVal, oldVal) {
            this.clientHandler(newVal, oldVal)
        },
        projectCost(newVal) {
            if (!newVal) {
                this.milestoneClonnerData = [{ 'name': '', 'cost': '', 'delivery_date': '' }]
            }
        }
    },
    mounted() {
        this.getQuoteStatus()
        this.getALLSales()
        this.getDesclaimerStatus()
        this.getAboutStatus()
        this.getNdaStatus()
        this.getProposalData()
    }
}
</script>

<style scoped>
.form-select {
    background-image: none;
    outline: none;
}
</style>