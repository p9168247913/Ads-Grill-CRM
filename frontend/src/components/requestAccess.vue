<!-- Home.vue -->
<template>
    <div class="wrapper">
        <div class="content-page">

            <div class="container-fluid" style="margin-top: 10rem;">
                <div class="col-md-2" data-bs-target="#createRoleModal">
                    <a href="javascript:;" class="btn btn-sm btn-dark float-right" data-bs-toggle="modal"
                        data-bs-target="#createRoleModal">Request Access</a>
                </div>

            </div>




            <!-- Modal for Create Role -->
            <div class="modal fade" id="createRoleModal" tabindex="-1" aria-labelledby="createRoleModalLabel"
                aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="createRoleModalLabel">Request Access</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <!-- Your form to create role -->
                            <form>
                                <!-- Feature Request Select Box -->
                                <div class="mb-3">
                                    <label for="featureRequest" class="form-label">Feature Request</label>
                                    <select class="form-select" id="featureRequest" name="featureRequest">
                                        <option value="select">Select...</option>
                                        <option value="option1">Option 1</option>

                                    </select>
                                </div>

                                <!-- Status Input Box (Disabled) -->
                                <!-- <div class="mb-3">
                                    <label for="status" class="form-label">Status</label>
                                    <input type="text" class="form-control" id="status" name="status" disabled>
                                </div> -->
                            </form>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary">Send</button>
                        </div>
                    </div>
                </div>
            </div>








        </div>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            // showModal: false
        };
    },
    methods: {
        // click() {
        //     alert('123')
        // }
    }

};
</script>
  
<style>/* Add your styles here */</style>
  