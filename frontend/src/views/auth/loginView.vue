<template>
  <head>
    <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <title>Webkit | Responsive Bootstrap 4 Admin Dashboard Template</title>
      
      <!-- Favicon -->
      <link rel="shortcut icon" href="./assets/images/favicon.ico" />
      <link rel="stylesheet" href="./assets/css/backend-plugin.min.css" type="text/css">
      <link rel="stylesheet" href="./assets/css/backend.css" type="text/css">
      <link rel="stylesheet" href="./assets/vendor/line-awesome/dist/line-awesome/css/line-awesome.min.css" type="text/css">
      <link rel="stylesheet" href="./assets/vendor/remixicon/fonts/remixicon.css" type="text/css">
      
      <link rel="stylesheet" href="./assets/vendor/tui-calendar/tui-calendar/dist/tui-calendar.css" type="text/css">
      <link rel="stylesheet" href="./assets/vendor/tui-calendar/tui-date-picker/dist/tui-date-picker.css" type="text/css">
      <link rel="stylesheet" href="./assets/vendor/tui-calendar/tui-time-picker/dist/tui-time-picker.css" type="text/css">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
    </head>
  <body class=" ">
    <!-- loader Start -->
    <!-- <div id="loading">
          <div id="loading-center">
          </div>
    </div> -->
    <!-- loader END -->
    
      <div class="wrapper">
      <section class="login-content">
         <div class="container">
            <div class="row align-items-center justify-content-center height-self-center">
               <div class="col-lg-8">
                  <div class="card auth-card">
                     <div class="card-body p-0">
                        <div class="d-flex align-items-center auth-content">
                           <div class="col-lg-6 bg-primary content-left">
                              <div class="p-3">
                                 <h2 class="mb-2 text-white">Sign In</h2>
                                 <p>Login to stay connected.</p>
                                 <form>
                                    <div class="row">
                                       <div class="col-lg-12">
                                          <div class="floating-label form-group">
                                             <input v-model="email" class="floating-input form-control" type="email" placeholder=" " >
                                             <label>Email</label>
                                          </div>
                                       </div>
                                       <div class="col-lg-12">
                                          <div class="floating-label form-group">
                                             <input v-model="pswd" class="floating-input form-control" type="password" placeholder=" ">
                                             <label>Password</label>
                                          </div>
                                       </div>
                                       <div class="col-lg-6">
                                          <div class="custom-control custom-checkbox mb-3">
                                             <input type="checkbox" class="custom-control-input" id="customCheck1">
                                             <label class="custom-control-label control-label-1 text-white" for="customCheck1">Remember Me</label>
                                          </div>
                                       </div>
                                       <div class="col-lg-6">
                                          <a href="auth-recoverpw.html" class="text-white float-right">Forgot Password?</a>
                                       </div>
                                    </div>
                                    <button class="btn btn-white float-center" @click="doLogin($event)">Sign In</button>

                                 </form>
                              </div>
                           </div>
                           <div class="col-lg-6 content-right">
                              <img src="assets/images/login/01.png" class="img-fluid image-right" alt="">
                           </div>
                           <!-- <PulseLoader v-if="loading" color="#42b983" size="30px" /> -->
                        </div>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </section>
      </div>
  </body>
</template>

<script>
import Noty from "noty"
import axios from "axios"
import { mapMutations } from "vuex";
import { mapState } from "vuex";
import router from "@/router";
// import PulseLoader from 'vue-spinner/src/PulseLoader.vue'
export default {
   components:{
      // PulseLoader
   },
  name: 'loginView',
  data(){
   return{
      email:'',
      pswd:'',
      loading: false,
   }
  },
  computed:{
   ...mapState(['authToken', 'authUser'])
  },
  methods:{
   ...mapMutations(['setAuthToken', 'setAuthUser']),
   doLogin(e){
      e.preventDefault();
      if(!this.email){
         new Noty({
            type: 'warning',
            text: 'Please enter email',
            timeout: 3000
         }).show();
      }
      else if(!this.pswd){
         new Noty({
            type: 'warning',
            text: 'Please enter password',
            timeout: 3000
         }).show();
      }
      else{
         // this.loading = true
         axios.post('http://127.0.0.1:8000/api/login/', {
            "username": this.email,
            "password": this.pswd
         }).then((response)=>{
            if(response.data.status == 'Success'){
               new Noty({
                  type: 'success',
                  text: response.data.message,
                  timeout: 500,
                  // onClose: function () {
                  //    router.push({name: 'dashBoard'});
                  // } 
               }).show()
               this.storeAuthToken(response.headers['token'], response.data.user)
               setTimeout(() => {
                  router.push('/dashboard')
               }, 2000);
            }
            else if(response.data.status == 'Failed'){
               new Noty({
                  type:'error',
                  text: response.data.message,
                  timeout: 3000
               }).show()
            }
         }).catch(()=>{
            // console.log(error)
         })
      }
   },
   storeAuthToken(token,user){
      if(token !== 'undefined' && user){
      this.setAuthToken(token)
      this.setAuthUser(user)
      // console.log(this.authToken, this.authUser, "from state management")
      }
   },
  },
}
</script>