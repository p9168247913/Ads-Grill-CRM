<template>
    <div id="preloader" class="d-flex justify-content-center align-items-center">
        <div class="spinner-border text-primary" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
    </div>
</template>

<script>
export default {}
</script>

<style>
#preloader {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(255, 255, 255, 0.8); /* Add a semi-transparent background for better visibility */
    z-index: 9999999;
}

@media (min-width: 576px) {}

@media (min-width: 750px) {}

@media (min-width: 992px) {}

@media (min-width: 1200px) {}
</style>