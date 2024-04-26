<template>
  <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/noty.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/noty@3.2.0-beta-deprecated/lib/themes/mint.css">
  </head>
  <div class="main_body">
    <h2>Templates</h2>
    <div class="module">
      <div>
        <label for="sprint" class="form-label">Project Type</label>
        <select required class="form-select selecBox" v-model="projectTypeValue">
          <option value="">Project Type</option>
          <option v-for="(sprint, index) in projectType" :key="index" :value="sprint.value">{{ sprint.key }}</option>
        </select>
      </div>
    </div>
    <hr />
    <div>
      <label class="form-label">Authentication Types</label>
      <div class="flexContainer">
        <div class="selecBox" v-for="(authType, index) in authenticationTypes" :key="index">
          <div class="module_box">
            <input type="checkbox" :id="'authType' + index" :value="authType" v-model="selectedAuthTypes">
            <div :for="'authType' + index">{{ authType }}</div>
          </div>

        </div>
      </div>
      <div class="belowTag module_box2">
        <input type="text" class="input_form" v-model="customAuthType" placeholder="Enter custom auth type">
        <button class="btn_form" @click="addCustomAuthType">Add</button>
      </div>
    </div>
    <hr />
    <div>
      <label class="form-label">Roles </label>
      <div class="flexContainer">
        <div class="selecBox" v-for="(role, index) in roles" :key="index">
          <div class="module_box">
            <input type="checkbox" :id="'role' + index" :value="role" v-model="selectedRole">
            <div :for="'role' + index">{{ role }}</div>
          </div>
        </div>
      </div>
      <div class="belowTag module_box2">
        <input type="text" class="input_form" v-model="customRole" placeholder="Enter custom role">
        <button class="btn_form" @click="addCustomRole">Add</button>
      </div>

    </div>
    <hr />
    <div>
      <label for="module" class="form-label">Modules</label>
      <div>
        <div class="flexContainer">
          <div class="module_box" v-for="(module, index) in mainfilled" :key="index">
            <input type="checkbox" v-model="selectedModule" :value="module?.value">
            {{ module.key }}
          </div>
        </div>
        <div class="belowTag module_box2">
          <input class="input_form" type="text" placeholder="Add Module" v-model="newCustomModuleLabel">
          <button class="btn_form" @click="addCustomModule">Add </button>
        </div>
      </div>
    </div>
    <hr />
    <label>
      Sub Modules
    </label>
    <div class="module">
      <div v-for="(subModuleval, index) in selectedModule" :key="index">
        <label class="form-label">{{ subModuleval }}</label>
        <div>
          <div class="flexContainer">
            <div class="checkbox-label" v-for="(subModule, subIndex) in subModules[subModuleval]"
              :key="'sub_' + subIndex">
              <div class="module_box3">
                <input type="checkbox" @click="subModuleclick(subModuleval, subModule.value)"
                  v-model="selectedSubModules" :value="subModule.value"
                  :checked="shouldShowPopupButton(subModule, subModuleval)">
                {{ subModule.key }}
                <button class="btn_form2" v-if="shouldShowPopupButton(subModule, subModuleval)"
                  @click="openPopup(subModuleval, subModule)">Add Details</button>
              </div>
            </div>
          </div>
          <div class="belowTag module_box2">
            <input class="input_form" placeholder="Add Custom" type="text" v-model="newSubModuleName[subModuleval]">
            <button class="btn_form" @click="addSubModule(subModuleval)">Add </button>
          </div>

        </div>

      </div>
    </div>

    <hr />
    <div>
      <div class="module">
        <div class="selectSidebar">
          <label for="sprint" class="form-label">Select Sidebar</label>
          <select required class="form-select selecBox" v-model="sidebarValue">
            <option value="">Select Sidebar Type</option>
            <option v-for="(sprint, index) in sidbar" :key="index" :value="sprint.value">{{ sprint.key }}</option>
          </select>
        </div>

      </div>
    </div>
    <hr />
    <div class="popup-container" v-if="showPopup">
      <div class="popup">
        <span class="close-btn" @click="closePopup">&times;</span>

        <div class="row">
          <div class="">
            <label for="projectName" class="form-label"> Header Description </label>
            <QuillEditor required ref="headerDesc"  theme="snow" toolbar="full" />
          </div>
        </div>

        <div class="row">
          <div class="">
            <label for="projectName" class="form-label"> Body Description </label>
            <QuillEditor required ref="bodyDesc" theme="snow" toolbar="full" />
          </div>
        </div>

        <div class="row">
          <div class="">
            <label for="projectName" class="form-label">Footer Description</label>
            <QuillEditor required ref="footerDesc" theme="snow" toolbar="full" />
          </div>
        </div>
        <div> <button class="form-btn" @click="storeAndClearData()">Submit</button></div>

      </div>
    </div>

    <div>
      <div>
        <label>Roles</label>

        <div class="" v-for="(role, index) in selectedRole" :key="index">
          {{ role }}
          <br />

          <div class="flexContainer">
            <div class="module_box" v-for="(module, subIndex) in selectedModule" :key="'sub_' + subIndex">
              <input type="checkbox" :checked="isChecked(role, module)"
                @change="updateRoleBasedAccess(role, module)">
              {{ module }}
            </div>
          </div>
        </div>
      </div>

    <div>
      <button @click="sendHTMLToDB">Save</button>
    </div>

  </div>

  <div style="display: flex; flex-direction: column; min-width: 500px; max-width: 500px;" ref="temp1">
    <div>
      <p style="font-weight: bold; font-size: small;">Project Type</p>
      <p style="font-size: smaller;">{{ projectTypeValue }}</p>
    </div>
    <div v-if="selectedAuthTypes.length">
      <p style="font-weight: bold; font-size: small;">Authentication Types</p>
      <ul>
        <li style="font-size:smaller" v-for="item in selectedAuthTypes" :key="item">{{ item }}</li>
      </ul>
    </div>
    <div v-if="selectedRole.length">
      <p style="font-weight: bold; font-size: small;">Roles & Departments</p>
      <ul>
        <li style="font-size:smaller" v-for="item in selectedRole" :key="item">{{ item }}</li>
      </ul>
    </div>
    <div v-if="allData.length">
      <p style="font-weight: bold; font-size: small;">Modules & SubModules</p>
      <ol>
      <li style="font-size:smaller" v-for="item, ind in allData" :key="ind">{{Object.keys(item)[0] }}
        <ul>
          <li v-for="(subModule, ind) in Object.values(item)[0]" :key="ind">{{ subModule.key }}
          <p style="font-size: 13px; margin-top:5px">-- Header Description: {{ subModule.otherData? subModule.otherData.header : "No description found" }}</p>
          <p style="font-size: 13px;">-- Body Description: {{ subModule.otherData? subModule.otherData.body : "No description found" }}</p>
          <p style="font-size: 13px;">-- Footer Description: {{ subModule.otherData? subModule.otherData.footer : "No description found" }}</p>
          </li>
        </ul>
      </li>
    </ol>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Noty from 'noty';
import { BASE_URL } from '../../config/apiConfig';
import { mapState } from 'vuex';
// import Swal from 'sweetalert2';
import html2pdf from 'html2pdf.js'
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';
export default {
 
  data() {
    return {
      selectedRoleBasedAccess: {},
      popupData: {
        header: '',
        body: '',
        footer: ''
      },
      showPopup: false,

      dataItems: [{ key: '', value: '' }],
      mainfilled: [{
        key: 'Sales Entery & POS Module ',
        value: 'Sales Entery & POS Module'
      },
      {
        key: 'Accounts Module',
        value: 'Accounts Module'
      },

      {
        key: 'Purchases Module',
        value: 'Purchases Module'
      },
      {
        key: 'Inventory Module',
        value: 'Inventory Module'
      },
      {
        key: 'Manufacturing Module',
        value: 'Manufacturing Module'
      },
      {
        key: 'Service Module',
        value: 'Service Module'
      },
      {
        key: 'Reports Module',
        value: 'Reports Module'
      },
      {
        key: 'Hr & Payroll Module',
        value: 'Hr & Payroll Module'
      },
      {
        key: "Order Module",
        value: "Order Module"
      },
      {
        key: "Quatation Module",
        value: "Quatation Module"
      },
      {
        key: "CRM Module",
        value: "CRM Module"
      }
      ],

      footer: "",
      sidbar: [{
        key: "Top Sidebar",
        value: "Top Sidebar"
      },
      {
        key: "Left Sidebar",
        value: "Left Sidebar"
      },
      {
        key: "Both Sidebar",
        value: "Both Sidebar"
      }
      ],
      authenticationTypes: ['Username/Password', 'OAuth', 'Two-Factor Authentication', 'Social Login authentication', 'Biometric authentication', "Client Certification"],
      roles: ["Super Admin", "Admin", "Manager", "Employee", "Customer", "Viewer"],
      selectedRole: [],
      customModules: '',
      selectedAuthTypes: [],
      modelValue: '',
      projectTypeValue: '',
      customAuthType: '',
      selectedModule: [],
      sidebarValue: '',
      selectedSubModules: [],
      customRole: '',
      newSubModuleName: {},
      subModulesArray: [],
      newCustomModuleLabel: '',
      allData: [],
      subModules: {
        "Sales Entery & POS Module": [{
          key: "Sales Module",
          value: "Sales Module"
        },
        {
          key: "Sales Entry",
          value: "Sales Entry"
        },
        {
          key: "POS Entry",
          value: "POS Entry"
        }, {
          key: "Customer Entry",
          value: "Customer Entry"
        },
        {
          key: "Sales Return Entry",
          value: "Sales Return Entry"
        },
        {
          key: "Replace Entry",
          value: "Replace Entry"
        },
        {
          key: "View Sales Vouchers",
          value: "View Sales Vouchers"
        },
        {
          key: "Sales Return Vouchers",
          value: "Sales Return Vouchers"
        },
        {
          key: "Sales Record",
          value: "Sales Record"
        }, {
          key: " Sales Return Record",
          value: "Sales Return Record"
        },
        {
          key: "Replace Record",
          value: "Replace Record"
        }
        ],

        "Accounts Module": [{
          key: "Accounts Module",
          value: "Accounts Module"
        },
        {
          key: "Customer Receipt Entry",
          value: "Customer Receipt Entry"
        },
        {
          key: "Supplier Receipt Entry",
          value: "Supplier Receipt Entry"
        },
        {
          key: "Expense Entry",
          value: "Expense Entry"
        },
        {
          key: "Income Entry",
          value: "Income Entry"
        },

        {
          key: "Expense Recognition Entry",
          value: "Expense Recognition Entry"
        },
        {
          key: "Branch Transaction Entry",
          value: "Branch Transaction Entry"
        },

        {
          key: "Contra / Single Entry",
          value: "Contra / Single Entry"
        }, {
          key: "Advance Transaction Entry",
          value: "Advance Transaction Entry"
        },
        {
          key: "Journal / Double Entry",
          value: "Journal / Double Entry"
        },
        {
          key: "Account Entry",
          value: "Account Entry"
        },
        {
          key: "Location Entry",
          value: "Location Entry"
        },
        ],
        "POS Module": [{
          key: "Sales Module",
          value: "Sales Module"
        },
        {
          key: "Sales Entry",
          value: "Sales Entry"
        },
        {
          key: "POS Entry",
          value: "POS Entry"
        }, {
          key: "Customer Entry",
          value: "Customer Entry"
        },
        {
          key: "Sales Return Entry",
          value: "Sales Return Entry"
        },
        {
          key: "Replace Entry",
          value: "Replace Entry"
        },
        {
          key: "View Sales Vouchers",
          value: "View Sales Vouchers"
        },
        {
          key: "Sales Return Vouchers",
          value: "Sales Return Vouchers"
        },
        {
          key: "Sales Record",
          value: "Sales Record"
        }, {
          key: " Sales Return Record",
          value: "Sales Return Record"
        },
        {
          key: "Replace Record",
          value: "Replace Record"
        }
        ],
        "Purchases Module": [{
          key: "Inventory Modules",
          value: "Inventory Modules"
        },
        {
          key: "Item Stock Report",
          value: "Item Stock Report"
        },
        {
          key: "Item Ledger",
          value: "Item Ledger"
        },
        {
          key: "Transfer Entry",
          value: "Transfer Entry"
        },
        {
          key: "Item Adjustment Enty",
          value: "Item Adjustment Enty"
        },
        {
          key: "Adjustment Record",
          value: "Adjustment Record"
        },
        {
          key: "Transfer Record",
          value: "Transfer Record"
        },
        {
          key: "Transfer Pending Record",
          value: "Transfer Pending Record"
        },
        {
          key: "Transfer Receive Record",
          value: "Transfer Receive Record"
        }
        ],
        "Inventory Module": [{
          key: "Purchase Module",
          value: "Purchase Module"
        },
        {
          key: "Purchase Entry",
          value: "Purchase Entry"
        },
        {
          key: "Supplier Entry",
          value: "Supplier Entry"
        }, {
          key: "Purchase Return Entry",
          value: "Purchase Return Entry"
        },

        {
          key: "Purchase Vouchers",
          value: "Purchase Vouchers"
        },
        {
          key: "Purchase return Vouchers",
          value: "Purchase return Vouchers"
        },

        {
          key: "Purchase Record",
          value: "Purchase Record"
        }, {
          key: " Purchase Return Record",
          value: "Purchase Return Record"
        }

        ],
        "Manufacturing Module": [
          {
            key: "Manufacturing Module",
            value: "Manufacturing Module"
          },
          {
            key: "Manufacturing Journal Entry",
            value: "Manufacturing Journal Entry"
          },
          {
            key: "Manufacturing Vouchers",
            value: "Manufacturing Vouchers"
          },
          {
            key: "Manufacturing Record",
            value: "Manufacturing Record"
          }

        ],
        "Service Module": [
          {
            key: "Service Module",
            value: "Service Module"
          },
          {
            key: "Service Entry",
            value: "Service Entry"
          }, {
            key: "Service Expense Entry",
            value: "Service Expense Entry"
          },
          {
            key: "View Service Vouchers",
            value: "View Service Vouchers"
          },
          {
            key: "Service Expense Record",
            value: "Service Expense Record"
          },
          {
            key: "Service Record",
            value: "Service Record"
          },
          {
            key: "Service Expense Record",
            value: "Service Expense Record"
          }


        ],

        "Reports Module": [
          {
            key: "Customer Due Balance",
            value: "Customer Due Balance"
          },
          {
            key: "Supplier Due Balance",
            value: "Supplier Due Balance"
          },
          {
            key: "Customer Ledger",
            value: "Customer Ledger"
          },
          {
            key: "Supplier Ledger",
            value: "Supplier Ledger"
          },
          {
            key: "Sales & Collection Record",
            value: "Sales & Collection Record"
          },
          {
            key: "Customer Receipt Record",
            value: "Customer Receipt Record"
          },
          {
            key: "Cash & Bank Balance",
            value: "Cash & Bank Balance"
          },
          {
            key: "Cash & Bank Ledger",
            value: "Cash & Bank Ledger"
          },
          {
            key: "Expense Balance Report",
            value: "Expense Balance Report"
          },
          {
            key: "Expense Record",
            value: "Expense Record"
          },
          {
            key: "Daily Ledger",
            value: "Daily Ledger"
          },
          {
            key: "Item Stock Report",
            value: "Item Stock Report"
          },
          {
            key: "Profit Loss",
            value: "Profit Loss"
          },
          {
            key: "Item Wise Profit/ Loss",
            value: "Item Wise Profit/ Loss"
          },
          {
            key: "Balance Sheet",
            value: "Balance Sheet"
          },
          {
            key: "Trial Balance",
            value: "Trial Balance"
          },
          {
            key: "Capitals Balance",
            value: "Capitals Balance"
          },
          {
            key: "Loan Accounts Balance",
            value: "Loan Accounts Balance"
          },
          {
            key: "Branch Tran Pending List",
            value: "Branch Tran Pending List"
          },
          {
            key: "Branch Tran Received List",
            value: "Branch Tran Received List"
          },
          {
            key: "Branch Tran Transfer List",
            value: "Branch Tran Transfer List"
          },
          {
            key: "Advance Customer Balance",
            value: "Advance Customer Balance"
          },
          {
            key: "Advance Supplier Balance",
            value: "Advance Supplier Balance"
          },
          {
            key: "Indirect Income Balance",
            value: "Indirect Income Balance"
          },
          {
            key: "Fixed Asset Balance",
            value: "Fixed Asset Balance"
          },
          {
            key: "Branch Balance Report",
            value: "Branch Balance Report"
          },
          {
            key: "Fixed Asset Ledger",
            value: "Fixed Asset Ledger"
          },
          {
            key: "Loan Account Ledger",
            value: "Loan Account Ledger"
          },
          {
            key: "Indirect Expense Ledger",
            value: "Indirect Expense Ledger"
          },
          {
            key: "Indirect Income Ledger",
            value: "Indirect Income Ledger"
          },
          {
            key: "Capital Ledger",
            value: "Capital Ledger"
          },
          {
            key: "Branch Ledger",
            value: "Branch Ledger"
          },
          {
            key: "Sales Account Ledger",
            value: "Sales Account Ledger"
          },
          {
            key: "Purchase Account Ledger",
            value: "Purchase Account Ledger"
          },
          {
            key: "Service Expense Ledger",
            value: "Service Expense Ledger"
          },
          {
            key: "Services Account Ledger",
            value: "Services Account Ledger"
          },
          {
            key: "Sales Return Acc. Ledger",
            value: "Sales Return Acc. Ledger"
          },
          {
            key: "Purchase Return acc. Ledger",
            value: "Purchase Return acc. Ledger"
          },
          {
            key: "Dutie & Tax Acc. Ledger",
            value: "Dutie & Tax Acc. Ledger"
          },
          {
            key: "Direct Expense Balance",
            value: "Direct Expense Balance"
          },
          {
            key: "Direct Expense Ledger",
            value: "Direct Expense Ledger"
          },
          {
            key: "Supplier Payment Record",
            value: "Supplier Payment Record"
          },
          {
            key: "Advance Tran Record",
            value: "Advance Tran Record"
          },
          {
            key: "Expense Recognition Reco",
            value: "Expense Recognition Reco"
          },
          {
            key: "Income Record",
            value: "Income Record"
          },
          {
            key: "Journal Record",
            value: "Journal Record"
          },
          {
            key: "Contra Record",
            value: "Contra Record"
          },
          {
            key: "Sales Record",
            value: "Sales Record"
          },
          {
            key: "Sales Return Record",
            value: "Sales Return Record"
          },
          {
            key: "Purchase Record",
            value: "Purchase Record"
          },
          {
            key: "Purchase Return Record",
            value: "Purchase Return Record"
          },
          {
            key: "Manufacturing Record",
            value: "Manufacturing Record"
          },
          {
            key: "Salary Payment Report",
            value: "Salary Payment Report"
          },
          {
            key: "Direct Income Balance",
            value: "Direct Income Balance"
          },
          {
            key: "Direct Income Ledger",
            value: "Direct Income Ledger"
          },
          {
            key: "Salary Payment Report",
            value: "Salary Payment Report"
          }
        ],

        "Hr & Payroll Module": [
          {
            key: "HrAndPayroll",
            value: "HrAndPayroll"
          },
          {
            key: "Attendance Entry",
            value: "Attendance Entry"
          },
          {
            key: "Salary Payment Entry",
            value: "Salary Payment Entry"
          },
          {
            key: "Employee Entry",
            value: "Employee Entry"
          },
          {
            key: "Department Entry",
            value: "Department Entry"
          },
          {
            key: "Designation Entry",
            value: "Designation Entry"
          },
          {
            key: "Salary Payment Report",
            value: "Salary Payment Report"
          },
          {
            key: "Monthly Salary Report",
            value: "Monthly Salary Report"
          }
        ],

        "Order Module": [
          {
            key: "Order Module",
            value: "Order Module"
          },
          {
            key: "Sales order Entry",
            value: "Sales order Entry"
          },
          {
            key: "Purchases order Entry",
            value: "Purchases order Entry"
          },
          {
            key: "Sales order Vouchers",
            value: "Sales order Vouchers"
          },
          {
            key: "Purchases order Vouchers",
            value: "Purchases order Vouchers"
          },

          {
            key: "Purchases order Record",
            value: "Purchases order Record"
          },
          {
            key: "Sales order Record",
            value: "Sales order Record"
          },
        ],

        "Quatation module": [
          {
            key: "Quotion Module",
            value: "Quotion Module"
          },
          {
            key: "Quotion Entry",
            value: "Quotion Entry"
          },
          {
            key: "Quotion Record",
            value: "Quotion Record"
          }
        ],
        "CRM Module": [
          {
            key: "CRM Module",
            value: "CRM Module"
          },
          {
            key: "Customer Entry",
            value: "Customer Entry"
          },
          {
            key: "Pending Customer Entry",
            value: "Pending Customer Entry"
          },
          {
            key: "Approved Customer Entry",
            value: "Approved Customer Entry"
          },
          {
            key: "Rejected Customer Entry",
            value: "Rejected Customer Entry"
          },
          {
            key: "Employee Wise Customer Report",
            value: "Employee Wise Customer Report"
          }
        ],
      },
      projectType: [
        {
          key: 'Enterprise Resource Planning System (ERPS)',
          value: 'Enterprise Resource Planning System (ERPS)'
        },
        {
          key: 'Customer Enagement Platform(CRM)',
          value: 'Customer Enagement Platform(CRM)'
        },

        {
          key: 'Online Retail Platform (E-Com)',
          value: 'Online Retail Platform (E-Com)'
        },
        {
          key: 'Interactive Entertainment Solutions(Game_Dev)',
          value: 'Interactive Entertainment Solutions(Game_Dev)'
        },
        {
          key: 'Dynamic Web Content Management(WordPress)',
          value: 'Dynamic Web Content Management(WordPress)'
        },
        {
          key: 'E-commerce Powerhouse (magento)',
          value: 'E-commerce Powerhouse (magento)'
        },
        {
          key: 'E-commerce Simplified (Shopify)',
          value: 'E-commerce Simplified (Shopify)'
        },
        {
          key: 'Mobile Application Solution',
          value: 'Mobile Application Solution'
        },
        {
          key: "Web Presence Solution",
          value: "Web Presence Solution"
        },

      ],
      currentModule: "",
      currentSubModule: ""
    }
  },
  components: {
    QuillEditor
  },
  computed: {
    ...mapState(['authToken', 'authUser']),
  },

  methods: {
    abcdCall(){
      console.log("abcdCall", this.selectedRoleBasedAccess)
    },
    isChecked(role, value) {
      console.log("isChecked",role,value)
    return this.abcdCall[role] && this.selectedRoleBasedAccess[role].includes(value);
  },
  updateRoleBasedAccess(role, value) {
    if (!this.selectedRoleBasedAccess[role]) {
      this.selectedRoleBasedAccess[role] = []; // Initialize if the role doesn't exist
    }
    const index = this.selectedRoleBasedAccess[role].indexOf(value);
    if (index === -1) {
      this.selectedRoleBasedAccess[role].push(value); // Add value if it's not already in the array
    } else {
      this.selectedRoleBasedAccess[role].splice(index, 1); // Remove value if it already exists
    }
  }
,
    storeAndClearData() {
      const footerData = this.$refs.footerDesc;
      if (footerData) {
        const htmlContent = footerData.getHTML();
        this.popupData.footer = htmlContent;
      }
      const bodyData = this.$refs.bodyDesc;
      if (bodyData) {
        const htmlContent = bodyData.getHTML();
        this.popupData.body = htmlContent;
      }
      const headerData = this.$refs.headerDesc;
      if (headerData) {
        const htmlContent = headerData.getHTML();
        this.popupData.header = htmlContent;
      }
    

      const mainModuleIndex = this.allData.findIndex(item => Object.keys(item)[0] === this.currentModule);
      let currentModuleData = null;

      if (mainModuleIndex !== -1) {
        currentModuleData = this.allData[mainModuleIndex][this.currentModule];
      }

      if (currentModuleData) {

        const existingSubmoduleIndex = currentModuleData.findIndex(item => item.key === this.currentSubModule);
        if (existingSubmoduleIndex !== -1) {

          currentModuleData[existingSubmoduleIndex].otherData = this.popupData;
        } else {
          currentModuleData.push({
            "key": this.currentSubModule,
            "value": this.currentSubModule,
            "otherData": this.popupData
          });
        }
      } else {

        this.allData.push({
          [this.currentModule]: [
            {
              "key": this.currentSubModule,
              "value": this.currentSubModule,
              "otherData": this.popupData
            }
          ]
        });
      }

      this.closePopup();
    }
    ,
    shouldShowPopupButton(subModule, subModuleval) {
      subModule = subModule?.key


      return this.allData.some(data =>
        Object.keys(data).includes(subModuleval) &&
        data[subModuleval].some(sub => sub.value === subModule)
      );
    }
    ,
    subModuleclick(subModuleval, value) {
      const index = this.allData.findIndex(item => Object.keys(item)[0] === subModuleval);
      if (index === -1) {

        this.allData.push({ [subModuleval]: [{ key: value, value: value }] });
      } else {

        const existingIndex = this.allData[index][subModuleval].findIndex(item => item.key === value);
        if (existingIndex !== -1) {

          this.allData[index][subModuleval].splice(existingIndex, 1);
        } else {

          this.allData[index][subModuleval].push({ key: value, value: value });
        }
      }
      console.log("allData:", this.allData);
    }

    ,
    openPopup(subModuleval, subModule) {
      this.currentModule = subModuleval;
      this.currentSubModule = subModule.key;
    
      const moduleIndex = this.allData.findIndex(item => Object.keys(item)[0] === subModule.key);
  
  if (moduleIndex !== -1) {
    // Module exists, check if subModule exists
    const submoduleIndex = this.allData[moduleIndex][subModule.key].findIndex(item => item.key === subModuleval);
    
    if (submoduleIndex !== -1) {
      // Submodule exists, populate popup with existing data
      const existingData = this.allData[moduleIndex][subModule.key][submoduleIndex].otherData;
      this.popupData = { ...existingData };
    } else {
      // Submodule doesn't exist, open popup with empty fields
      this.popupData = {
        header: "",
        body: "",
        footer: ""
      };
    }
  } else {
    // Module doesn't exist, open popup with empty fields
    this.popupData = {
      header: "",
      body: "",
      footer: ""
    };

    this.showPopup = true;
  }
    },
    closePopup() {
      this.currentModule = "";
      this.currentSubModule = "";
      this.showPopup = false;
    },
    updateSubModules() {
      this.selectedSubModule = '';
    },
    addSubModule(moduleName) {
      if (this.newSubModuleName[moduleName].trim() !== '') {
        const newSubModule = {
          key: this.newSubModuleName[moduleName],
          value: this.newSubModuleName[moduleName]
        };
        if (this.subModules[moduleName] === undefined) {
          this.subModules[moduleName] = [newSubModule];
        } else {
          this.subModules[moduleName].push(newSubModule);
        }
        this.newSubModuleName[moduleName] = '';

        if (!this.mainfilled.some(module => module.key === moduleName)) {
          this.selectedModule.push(moduleName);
        }
      }
    },

    addCustomModule() {
      if (this.newCustomModuleLabel.trim() !== '') {
        const newCustomModule = {
          key: this.newCustomModuleLabel,
          value: this.newCustomModuleLabel
        };
        this.mainfilled.push(newCustomModule);
        this.selectedModule.push(this.newCustomModuleLabel);
        this.newCustomModuleLabel = '';
      }
    },
    async sendHTMLToDB(){
      this.$store.commit('showLoader')
      try{
        const response = await axios.put(`${BASE_URL}api/templateView/`,
        {
        data:this.$refs.temp1.outerHTML
      }, {
        headers:{
            token:this.authToken
          },
      })
      if (response.data.message === "Requirements Submitted"){
        new Noty({
          type:'success',
          text:response.data.message,
          timeout: 1000,
        }).show()
        this.$store.commit('hideLoader')
      }
      } catch(error){
        new Noty({
          type:'error',
          text:error.response.data.message ? error.response.data.message : error.response.data.detail,
          timeout: 1000,
        }).show()
      }
      this.$store.commit('hideLoader')

    },
    generatePDF() {
      //console.log(html2pdf)
      console.log("----------", this.allData, "------------")
      var opt = {
        margin: 0.1,
        fileName: 'new.pdf',
        image: {
          type: 'jpeg',
          quality: 0.99
        },
        html2canvas: { scale: 2 },
        jsPDF: {
          unit: 'in',
          format: 'a4',
          orientation: 'portrait'
        }
      };
      html2pdf().from(this.$refs.temp1).set(opt).save();
    },
    addCustomAuthType() {
      if (this.customAuthType.trim() !== '') {
        this.authenticationTypes.push(this.customAuthType.trim());
        this.selectedAuthTypes.push(this.customAuthType.trim());
        this.customAuthType = '';
      }
    },
    addCustomRole() {
      if (this.customRole.trim() !== '') {
        this.roles.push(this.customRole.trim());
        this.selectedRole.push(this.customRole.trim());
        this.customRole = '';
      }
    },
    addInputFields() {
      this.dataItems.push({ key: '', value: '' });
    },
    addSubModuleData() {


    },

  },
  mounted() {
   //console.log(this.selectedSubModules)
    //console.log(this.modelValue);
  },
  watch: {
    selectedSubModule: {
      handler() {
      }
    }
  },
}
</script>

<style scoped>
::v-deep .ql-container {
  max-height: 135px;
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
  max-height: 135px;
  overflow-y: auto;
  color: black;
  height: 135px;
}

.checkbox-label {
  display: block;
  margin-bottom: 5px;

}

.lastBody {
  margin-bottom: 10px;
  margin-top: 10px;
  align-items: center;


}
.form-btn{
  margin: auto;
  margin-top: 10px;
  margin-left: 10px;
}
.lastBody>div {
  width: 300px;
  color: white;
  margin: auto;
}

.lastBody>div>button {
  width: 100%;
  border: none;
  color: white;
  padding: 5px;
  background-color: #6EB4D1;
  border-radius: 5px;
  margin: auto;
}

.flexContainer {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 10px;
  font-size: 14px;
  align-items: center;
}

.selectSidebar {
  width: 375px;
}

.roleBaseAccess {
  display: flex;
}

.module_box {
  margin-left: 5px;
  height: 40px;
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 5px 15px 5px 15px;
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.02) 0px 1px 3px 0px, rgba(27, 31, 35, 0.15) 0px 0px 0px 1px;
}

.module_box3 {
  margin-left: 5px;
  height: 40px;
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 5px 5px 5px 15px;
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.02) 0px 1px 3px 0px, rgba(27, 31, 35, 0.15) 0px 0px 0px 1px;
}

.module_box2 {

  align-items: center;

  box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 6px, rgba(0, 0, 0, 0.23) 0px 3px 6px;
}

.module_box2>div {
  margin: 25px;
}

.main_body {
  background-color: white;
  padding: 15px;
  margin-left: 5px;
  margin-right: 5px;
  color: black;
  border-radius: 10px;
}

.belowTag2 {
  display: flex;
  gap: 8px;
  width: fit-content;
  border-radius: 5px;

}

.input_form {
  widows: 100%;
  border: none;
  outline: none;
}

.btn_form {
  border: none;
  outline: none;
  border-radius: 0px 5px 5px 0px;
  padding-left: 3px;
  height: 35px;
  color: white !important;
  padding: 0px 6px 0px 6px;
  background-color: #6EB4D1;
}

.btn_form2 {
  border: none;
  outline: none;
  margin-left: 10px;
  height: 35px;
  color: white !important;
  padding: 0px 6px 0px 6px;
  background-color: #6EB4D1;
}

.belowTag {
  display: flex;
  gap: 8px;
  max-width: fit-content;
  border-radius: 5px;
  margin-top: 15px;
  height: 35px;
  align-items: center;
  justify-content: center;
  text-align: center;

}

.belowTag>input {
  padding: 0px 5px 0px 5px;
  font-size: 15px;
}

.module {
  display: flex;
  width: "100%";
  gap: 10px;
  flex-direction: row;
  flex-wrap: wrap;
}

.selecBox {
  display: flex;
  align-items: center;


}

.popup-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  margin: 5px;
  z-index: 100;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.popup {
  background-color: #fff;
  height: 85vh;
  width: 90%;
  padding: 10px;
  overflow: auto;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  position: relative;
}


.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
  font-size: 12px;
  font-size: 20px;
  color: #888;
}
</style>