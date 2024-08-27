<template>
    <div id="pdf" style="display:none;">
      <!--Quotation page1 start-->
      <div class="container">
        <img :src="imagePath1">
      </div>
      <!--Quotation page1 end-->

      <!--Quotation page2 start-->
      <div class="container">
        <img :src="imagePath2">
      </div>
      <!--Quotation page2 end-->

      <!--Quotation page3 start-->
      <div class="container">
        <img :src="imageHeader">
        <div style="width: 90%; border: 1px solid gray; margin: 35px auto;"></div>
        <br>
        <h6 style="padding-left: 50px; color: #000000;"><b>Client name :-</b> <span v-html="dynamicClientName" style="background-color: #E9E9F3; width: 78%; display: inline-block; padding-left: 10px;"> </span></h6>
        <div style="display: grid; grid-template-columns: 1fr 1fr; margin-top: 35px;">
          <h6 style="padding-left: 50px; color: #000000;"><b>Email :-</b> <span v-html="dynamicClientEmail" style="background-color: #E9E9F3; width: 75%; display: inline-block; padding-left: 10px;"> </span></h6>
          <h6 style="padding-left: 80px; color: #000000;"><b>Mobile No :-</b> <span v-html="dynamicClientPhone" style="background-color: #E9E9F3; width: 50%; display: inline-block; padding-left: 10px;"> </span></h6>
        </div>
      </div>
      <div style="width: 90%; border: 1px solid gray; margin: 35px auto;"></div>
      <h5 style="padding-left: 50px; color: #000000; text-align: center;"><b><u>Project Details</u></b></h5>
      <h6 style="padding-left: 50px; color: #000000; margin-top: 35px;"><b>Project Type :-</b> <span v-html="dynamicProjectType" style="background-color: #E9E9F3; width: 68%; display: inline-block; padding-left: 10px; margin-left: 53px;"> </span></h6>
      <h6 style="padding-left: 50px; color: #000000; margin-top: 35px;"><b>Project Name :-</b> <span v-html="dynamicProjectName" style="background-color: #E9E9F3; width: 68%; display: inline-block; padding-left: 10px; margin-left: 45px;"> </span></h6>
      <h6 style="padding-left: 50px; color: #000000; margin-top: 35px;"><b>Project Cost :-</b> <span v-html="dynamicProjectCost" style="background-color: #E9E9F3; width: 68%; display: inline-block; padding-left: 10px; margin-left: 57px;"> </span></h6>
      <h6 style="padding-left: 50px; color: #000000; margin-top: 35px;"><b>Project GST :-</b> <span style="background-color: #E9E9F3; width: 68%; display: inline-block; padding-left: 10px; margin-left: 65px;"> {{this.dynamicProjectCost * 18 / 100}} </span></h6>
      <h6 style="padding-left: 50px; color: #000000; margin-top: 35px;"><b>GST Name :-</b> <span v-html="dynamicProjectGST" style="background-color: #E9E9F3; width: 68%; display: inline-block; padding-left: 10px; margin-left: 73px;"> </span></h6>
      <h6 style="padding-left: 50px; color: #000000; margin-top: 35px;"><b>Project Total Cost :-</b> <span style="background-color: #E9E9F3; width: 68%; display: inline-block; padding-left: 10px; margin-left: 15px;"> {{Number(this.dynamicProjectCost) + Number(this.dynamicProjectCost) * 18 / 100}} </span></h6>
      <div style="width: 90%; border: 1px solid gray; margin: 35px auto;"></div>
      <h6 style="padding-left: 50px; color: #000000; margin-top: 35px;"><b>Apis Integration :-</b> <span v-html="dynamicApiIntegration" style="background-color: #E9E9F3; width: 68%; display: inline-block; padding-left: 10px; margin-left: 25px;"> </span></h6>
      <h6 style="padding-left: 50px; color: #000000; margin-top: 35px;"><b>Project Refrence :-</b> <span v-html="dynamicProjectRefrence" style="background-color: #E9E9F3; width: 68%; display: inline-block; padding-left: 10px; margin-left: 20px;"> </span></h6>
      <img :src="imageFooter" style="margin-top: 72px;">
      <!--Quotation page3 end-->

      <!--Quotation page4 start-->
      <div class="container">
        <img :src="commonHeader">
        <div style="padding: 5px 5px 5px 15px; width: 90%; margin: 35px auto; background-color: #2E3192;">
          <h5 style="color:#ffffff"><b>Project Objective :- </b></h5>
        </div>
        <div style="width: 90%; border: 1px solid gray; margin: 35px auto;"></div>
        <div style="width:90%; margin: 20px auto; height: 300px; background-color: #E9E9F3; border: 1px solid #E9E9F3; padding: 20px;">
            <h6 v-html="dynamicProjectObjective"></h6>
        </div>
        <div style="width: 90%; border: 1px solid gray; margin: 35px auto;"></div>
        <div style="padding: 5px 5px 5px 15px; width: 90%; margin: 35px auto; background-color: #2E3192;">
          <h5 style="color:#ffffff"><b>Project Functional Requirements :- </b></h5>
        </div>
        <div style="width:90%; margin: 20px auto; height: 300px; background-color: #E9E9F3; border: 1px solid #E9E9F3; padding: 20px;">
            <h6 v-html="dynamicProjectRequirement"></h6>
        </div>
        <img :src="imageFooter" style="margin-top: 65px;">
      </div>
      <!--Quotation page4 end-->

      <!--Quotation page5 start-->
      <div class="container">
        <img :src="commonHeader">
        <div style="padding: 5px 5px 5px 15px; width: 90%; margin: 35px auto; background-color: #2E3192;">
          <h5 style="color:#ffffff"><b>Time Frame :- </b></h5>
        </div>
        <div style="width: 90%; border: 1px solid gray; margin: 35px auto;"></div>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; grid-template-rows: 40px 30px; margin-top: 35px;">
          <h6 style="padding-left: 50px; color: #000000; text-align:center;"><b><u>Start Date :</u></b></h6>
          <h6 style="padding-left: 50px; color: #000000; text-align:center;"><b><u>End Date :</u></b></h6>
          <h6 style="padding-left: 50px; color: #000000; text-align:center;"><b><u>Working Days :</u></b></h6>
          <h6 style="margin-left: 80px; color: #000000; background-color: #ECF8FD; width:150px; text-align:center;">{{dynamicTimeFrameStart}}</h6>
          <h6 style="margin-left: 80px; color: #000000; background-color: #ECF8FD; width:150px; text-align:center">{{dynamicTimeFrameEnd}}</h6>
          <h6 style="margin-left: 80px; color: #000000; background-color: #ECF8FD; width:150px; text-align:center">{{dynamicTimeFrameWorking}}</h6>
        </div>
        <div style="width: 90%; border: 1px solid gray; margin: 35px auto;"></div>
        <h5 style="padding-left: 50px; color: #000000;"><b>Tech Specification</b></h5>
        <h6 style="padding-left: 50px; color: #000000; margin-top: 35px;"><b>Frontend :-</b> <span v-html="dynamicTechSpecsFrontend" style="background-color: #E9E9F3; width: 80%; display: inline-block; padding-left: 10px; margin-left: 28px;"> </span></h6>
        <h6 style="padding-left: 50px; color: #000000; margin-top: 35px;"><b>Backend :-</b> <span v-html="dynamicTechSpecsBackend" style="background-color: #E9E9F3; width: 80%; display: inline-block; padding-left: 10px; margin-left: 33px;"> </span></h6>
        <h6 style="padding-left: 50px; color: #000000; margin-top: 35px;"><b>Databases :-</b> <span v-html="dynamicTechSpecsDatabase" style="background-color: #E9E9F3; width: 80%; display: inline-block; padding-left: 10px; margin-left: 20px;"> </span></h6>
        <div style="width: 90%; border: 1px solid gray; margin: 35px auto;"></div>
        <div style="height: 263px; background-color: #ECF8FD;">
            <h5 style="padding-left: 50px; color: #000000; text-align:center;"><b><u>MILESTONE FOR PAYMENT</u></b></h5>
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; grid-template-rows: auto; margin-top: 35px;">
              <h6 style="padding-left: 80px; color: #000000;"><b><u>Name</u></b></h6>
              <h6 style="padding-left: 50px; color: #000000;"><b><u>Cost</u></b></h6>
              <h6 style="padding-left: 50px; color: #000000;"><b><u>Delivery Date</u></b></h6>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; grid-template-rows: auto; margin-top: 16px; margin-left: 80px;" v-for="item in dynamicMilestone" :key="item.name">
                <p style="color: #000000; margin-top:-25px; font-size: 12px;">{{item.name}}</p>
                <p style="color: #000000; margin-top:-25px; font-size: 12px;">{{item.cost}}</p>
                <p style="color: #000000; margin-top:-25px; margin-left: 30px; font-size: 12px;">{{item.delivery_date}}</p>
            </div>
        </div>
        <h6 style="color: #000000; text-align:center; margin-top:65px;"><b>Project Time Potential {{dynamicTimeFrameWorking}} days excluding Saturdays, Sundays and Public holidays.</b></h6>
        <h6 style="color: #000000; text-align:center;"><b>Terms & Conditions :- <span style="color: #1B75BC;">https://adsgrill.com/</span></b></h6>
        <img :src="imageFooter" style="margin-top: 21px;">
      </div>
      <!--Quotation page5 end-->

      <!--Quotation page6 start-->
      <img :src="imagePath3">
      <!--Quotation page6 end-->

      <!--Quotation page7 start-->
      <img :src="disclaimerPage">
      <div v-html="dynamicDesclaimer" style="width: 100%; height: 970px; padding: 15px; background-color: #ECF8FD;"></div>
      <img :src="imageFooter" style="margin-top: 20px;">
      <!--Quotation page7 end-->

      <!--Quotation page8 start-->
      <img :src="aboutPage">
      <div v-html="dynamicAbout" style="width: 100%; height: 970px; padding: 15px; background-color: #ECF8FD;"></div>
      <img :src="imageFooter" style="margin-top: 21px;">
      <!--Quotation page8 end-->

      <!--Quotation page9 start-->
      <img :src="ndaPage">
      <div v-html="dynamicNda" style="width: 100%; height: 970px; padding: 15px; background-color: #ECF8FD;"></div>
      <img :src="imageFooter" style="margin-top: 21px;">
      <!--Quotation page9 end-->
    </div>
  </template>
  
  <script>
  
  export default {
    props: {
        dynamicDesclaimer:{
            type: String,
        },
        dynamicNda:{
            type: String,
        },
        dynamicAbout:{
            type: String,
        },
        dynamicClientName:{
          type: String
        },
        dynamicClientEmail:{
          type: String
        },
        dynamicClientPhone:{
          type: String
        },
        dynamicProjectType:{
          type: String
        },
        dynamicProjectName:{
          type: String
        },
        dynamicProjectCost:{
          type: String
        },
        dynamicProjectGST:{
          type: String
        },
        dynamicApiIntegration:{
          type: String
        },
        dynamicProjectRefrence:{
          type: String
        },
        dynamicProjectObjective:{
          type: String
        },
        dynamicProjectRequirement:{
          type: String
        },
        dynamicTimeFrameStart:{
          type: String
        },
        dynamicTimeFrameEnd:{
          type: String
        },
        dynamicTimeFrameWorking:{
          type: String
        },
        dynamicTechSpecsFrontend:{
          type: String
        },
        dynamicTechSpecsBackend:{
          type: String
        },
        dynamicTechSpecsDatabase:{
          type: String
        },
        dynamicMilestone:{
          type: Array
        }
    },
    data() {
      return{
        imagePath1 : require(`@/assets/img/Proposal/quotation1.png`),
        imagePath2 : require(`@/assets/img/Proposal/quotation2.png`),
        imagePath3 : require(`@/assets/img/Proposal/quotation3.png`),
        imageFooter : require(`@/assets/img/Proposal/quotation_footer.png`),
        imageHeader : require(`@/assets/img/Proposal/quotation3_header.png`),
        commonHeader : require(`@/assets/img/Proposal/common_header.png`),
        disclaimerPage : require(`@/assets/img/Proposal/disclaimer_page.png`),
        aboutPage : require(`@/assets/img/Proposal/about_page.png`),
        ndaPage : require(`@/assets/img/Proposal/nda_page.png`),
      }
    },
    computed:
    {
      computedImagePath()
      {
        return {
        imagePath1: this.imagePath1,
        imagePath2: this.imagePath2,
        imagePath3: this.imagePath3,
        imageFooter: this.imageFooter,
        imageHeader: this.imageHeader,
        commonHeader: this.commonHeader,
        disclaimerPage: this.disclaimerPage,
        aboutPage: this.aboutPage,
        ndaPage: this.ndaPage,
      };
      }
    }
  };
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Bona+Nova+SC:ital,wght@0,400;0,700;1,400&display=swap');
  .container{
    width: 100%;
    margin: 0;
    padding: 0;
  }
  img{
    width: 100%;
    height: auto;
  }
  </style>
  