<template>
    <div class="container">
        <div class="row" style="margin-top: 20px;">
            <div class="col-md-12 col-lg-12 block">
                <h6 class="text-uppercase">Add Tag</h6>
                <div class="col-md-4 mb-3" style="display: flex; gap: 10px;">
                    <input type="text" class="form-control" v-model="newTag" placeholder="Enter Tag" />
                    <button class="btn btn-primary" @click="addTag">Add</button>
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
                            <td style="padding-left: 25px;" class="text-start align-middle" scope="row">{{ index + 1 }}</td>
                            <td style="padding-left: 25px;" class="text-start align-middle">{{ tag }}</td>
                            <td style="padding-left: 25px;" class="text-start align-middle">
                                <i class="fas fa-trash text-danger m-3 fa-xs" @click="deleteTag(index)"
                                    style="cursor: pointer"></i>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="row" style="margin-top: 20px;">
            <div class="col-md-12 col-lg-12 block">
                <h6 class="text-uppercase">Add Source</h6>
                <div class="col-md-4 mb-3" style="display: flex; gap: 10px;">
                    <input type="text" class="form-control" v-model="newSource" placeholder="Enter Source" />
                    <button class="btn btn-primary" @click="addSource">Add</button>
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
                            <td style="padding-left: 25px;" class="text-start align-middle" scope="row">{{ index + 1 }}</td>
                            <td style="padding-left: 25px;" class="text-start align-middle">{{ source }}</td>
                            <td style="padding-left: 25px;" class="text-start align-middle">
                                <i class="fas fa-trash text-danger m-3 fa-xs" @click="deleteSource(index)"
                                    style="cursor: pointer"></i>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="row" style="margin-top: 20px;">
            <div class="col-md-12 col-lg-12 block">
                <h6 class="text-uppercase">Add Status</h6>
                <div class="col-md-4 mb-3" style="display: flex; gap: 10px;">
                    <input type="text" class="form-control" v-model="newStatus" placeholder="Enter Status" />
                    <button class="btn btn-primary" @click="addStatus">Add</button>
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
                            <td style="padding-left: 25px;" class="text-start align-middle" scope="row">{{ index + 1 }}</td>
                            <td style="padding-left: 25px;" class="text-start align-middle">{{ status }}</td>
                            <td style="padding-left: 25px;" class="text-start align-middle">
                                <i class="fas fa-trash text-danger m-3 fa-xs" @click="deleteStatus(index)"
                                    style="cursor: pointer"></i>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            newTag: '',
            newSource: '',
            newStatus: '',
            tags: [],
            sources: [],
            statuses: [],
        };
    },
    methods: {
        addTag() {
            if (this.newTag.trim() !== '') {
                this.tags.push(this.newTag.trim());
                this.newTag = '';
            }
        },
        deleteTag(index) {
            this.tags.splice(index, 1);
        },
        addStatus() {
            if (this.newStatus.trim() !== '') {
                this.statuses.push(this.newStatus.trim());
                this.newStatus = '';
            }
        },
        addSource() {
            if (this.newSource.trim() !== '') {
                this.sources.push(this.newSource.trim());
                this.newSource = '';
            }
        },
        deleteSource(index) {
            this.sources.splice(index, 1);
        },
        deleteStatus(index) {
            this.statuses.splice(index, 1);
        },
    },
};
</script>
  
<style scoped>
.container {
    margin-top: 30px;
}

.block {
    /* border: 1px solid red; */
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
    /* Adjust as needed */
}
</style>
  