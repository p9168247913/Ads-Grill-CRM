<template>
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
      <div>
        <label class="form-label">Authentication Types</label>
        <div class="selecBox" v-for="(authType, index) in authenticationTypes" :key="index">
          <input type="checkbox" :id="'authType' + index" :value="authType" v-model="selectedAuthTypes">
          <label :for="'authType' + index">{{ authType }}</label>
        </div>
        <div class="belowTag">
          <input type="text" class="input_form" v-model="customAuthType" placeholder="Enter custom authentication type">
          <button class="btn_form" @click="addCustomAuthType">Add</button>
        </div>
      </div>
      <div>
        <label class="form-label">Roles </label>
        <div class="selecBox" v-for="(role, index) in roles" :key="index">
          <input type="checkbox" :id="'role' + index" :value="role" v-model="selecteRole">
          <label :for="'role' + index">{{ role }}</label>
        </div>
        <div class="belowTag">
          <input type="text" class="input_form" v-model="customRole" placeholder="Enter custom authentication type">
          <button class="btn_form" @click="addCustomRole">Add</button>
        </div>
      </div>
    </div>

    <div class="module">

    </div>
    <div>
      <label for="module" class="form-label">Modules</label>
      <div>
        <label class="module_box" v-for="(module, index) in mainfilled" :key="index">
          <input type="checkbox" v-model="selectedModule" :value="module.value">
          {{ module.key }}
        </label>
        <div class="belowTag2">
          <input class="input_form" type="text" v-model="newCustomModuleLabel">
          <button class="btn_form" @click="addCustomModule">Add Module</button>
        </div>
      </div>
    </div>
    <label>
      Sub Modules
    </label>
    <div class="module">
      <div v-for="(subModuleval, index) in selectedModule" :key="index">
        <label class="form-label">{{ subModuleval }}</label>
        <div>
          <label class="checkbox-label" v-for="(subModule, subIndex) in subModules[subModuleval]"
            :key="'sub_' + subIndex">
            <input type="checkbox" @click="subModuleclick(subModuleval, subModule.value)" v-model="selectedSubModules"
              :value="subModule.value" :checked="shouldShowPopupButton(subModule, subModuleval)">
            {{ subModule.key }}
            <button v-if="shouldShowPopupButton(subModule, subModuleval)" @click="openPopup(subModule)">Open
              Popup</button>
          </label>

          <div class="belowTag2">
            <input class="input_form" type="text" v-model="newSubModuleName[subModuleval]">
            <button class="btn_form" @click="addSubModule(subModuleval)">Add Submodule</button>
          </div>
        </div>

      </div>
    </div>
    <div>
      <div class="module">
        <div>
          <label for="sprint" class="form-label">Select Sidebar</label>
          <select required class="form-select selecBox" v-model="sidebarValue">
            <option value="">Select Sidebar Type</option>
            <option v-for="(sprint, index) in sidbar" :key="index" :value="sprint.value">{{ sprint.key }}</option>
          </select>
        </div>

      </div>
    </div>

    <div class="popup-container" v-if="showPopup">
      <div class="popup">
    <span class="close-btn" @click="closePopup">&times;</span>

    <div class="row">
      <div class="">
        <label for="projectName" class="form-label">Header Description</label>
        <QuillEditor required v-model="popupData.header" :modules="modules" theme="snow" toolbar="full" />
      </div>
    </div>

    <div class="row">
      <div class="">
        <label for="projectName" class="form-label">Body Description</label>
        <QuillEditor required v-model="popupData.body" :modules="modules" theme="snow" toolbar="full" />
      </div>
    </div>

    <div class="row">
      <div class="">
        <label for="projectName" class="form-label">Footer Description</label>
        <QuillEditor required v-model="popupData.footer" :modules="modules" theme="snow" toolbar="full" />
      </div>
    </div>
    <div> <button @click="storeAndClearData">Store Data </button></div>

  </div>
    </div>

    <div>

      <div>
        <label>Select feature modules to be shown with each role</label>
        <div>
          <label>Roles</label>
          <div class="roleBaseAccess" v-for="(role, index) in selecteRole" :key="index">
            {{ role }}

            <label class="" v-for="(module, subIndex) in selectedModule" :key="'sub_' + subIndex">
              <input type="checkbox" v-model="selectedRoleBasedAccess" :value="module.value">
              {{ module }}
            </label>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import jsPDF from 'jspdf';
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';
export default {
  data() {
    return {
      popupData: {
        header: '',
        body: '',
        footer: ''
      },
      showPopup: false,

      dataItems: [{ key: '', value: '' }],
      mainfilled: [{
        key: 'Sales Entery',
        value: 'Sales Entery'
      },
      {
        key: 'Accounts Module',
        value: 'Accounts Module'
      },
      {
        key: 'POS Module',
        value: 'POS Module'
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
        key: "Quatation module",
        value: "Quatation module"
      },
      {
        key: "CRM Module",
        value: "CRM Module"
      }
      ],

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
      selecteRole: [],
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
        "Sales Entery": [{
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
            key: "Purchase Return acc. Ledç",
            value: "Purchase Return acc. Ledç"
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

    }
  },
  components: {
    QuillEditor
  },
  computed: {

  },
  methods: {
    storeAndClearData(popupData ) {
console.log(popupData);
    // this.allData.forEach(category => {
    //   for (const key in category) {
    //     if (Object.prototype.hasOwnProperty.call(category, key)) {
    //       const submodule = category[key];
    //       submodule.forEach(item => {
    //         if (item.key === popupData[0].key) {
              
    //           this.$set(item, 'popupData', popupData[0]);
    //           return;
    //         }
    //       });
    //     }
    //   }
    // });

    // for (const key in formData) {
    //   if (Object.prototype.hasOwnProperty.call(formData, key)) {
    //     this.$set(formData, key, ''); 
    //   }
    // }
  },

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
        // If not present, add it
        this.allData.push({ [subModuleval]: [{ key: value, value: value }] });
      } else {
        // If present, remove it if it exists, otherwise add it
        const existingIndex = this.allData[index][subModuleval].findIndex(item => item.key === value);
        if (existingIndex !== -1) {
          // Value exists, remove it
          this.allData[index][subModuleval].splice(existingIndex, 1);
        } else {
          // Value doesn't exist, add it
          this.allData[index][subModuleval].push({ key: value, value: value });
        }
      }
      console.log("allData:", this.allData);
    }

    ,
    openPopup() {

      this.showPopup = true;
    },
    closePopup() {

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
    generatePDF() {
      const doc = new jsPDF();

      const htmlContent = `
        <h1 style="color: red;">PDF Example</h1>
        <p ref="p1">This is a paragraph inside a PDF generated from HTML content with styling.</p>
      `;

      doc.html(htmlContent, {
        callback: function (doc) {
          doc.save('example.pdf');
        },
        margin: 10,
        x: 10,
        y: 10
      });
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
        this.selecteRole.push(this.customRole.trim());
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

.roleBaseAccess {
  display: flex;
}

.module_box {
  margin-left: 5px;
  padding: 10px;
  align-items: center;
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 6px, rgba(0, 0, 0, 0.23) 0px 3px 6px;
}

.main_body {
  background-color: white;
  padding: 15px;
  margin-left: 5px;
  margin-right: 5px;
  border-radius: 10px;
}

.belowTag2 {
  display: flex;
  gap: 8px;
  width: fit-content;
  border-radius: 5px;
  border: 1px solid gray;
}

.input_form {
  widows: 100%;
  border: none;
  outline: none;
}

.btn_form {
  border: none;
  outline: none;

  padding-left: 3px;
  color: white !important;
  background-color: #6EB4D1;
}

.belowTag {
  display: flex;
  gap: 8px;
  width: 79%;
  border-radius: 5px;
  align-items: center;
  justify-content: center;
  text-align: center;
  border: 1px solid gray;
}

.module {
  display: flex;
  width: "100%";
  gap: 10px;
  flex-direction: row;
  flex-wrap: wrap;
}

.selecBox {
  max-width: 300px;
  min-width: 300px;
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
  font-size: 20px;
  color: #888;
}
</style>