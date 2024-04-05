<template>
  <div>
    <h2>Templates</h2>
    <div class=" module">
      <div>
        <label for="sprint" class="form-label">Project Type</label>
        <select required class="form-select selecBox" v-model="projectTypeValue">
          <option value="">Project Type</option>
          <option v-for="(sprint, index) in projectType" :key="index" :value="sprint.value">{{
          sprint.key }}</option>
        </select>
      </div>
      <div>
        <label for="sprint" class="form-label">Sub Project Type</label>
        <select required class="form-select selecBox" v-model="subProjectTypeValue">
          <option value="">Sub Project Type</option>
          <option v-for="(sprint, index) in mainfilled" :key="index" :value="sprint.value">{{
          sprint.key }}</option>
        </select>
      </div>
      <div>
        <label for="sprint" class="form-label">Modules</label>
        <select required class="form-select selecBox" v-model="modelValue">
          <option value="">Modules</option>
          <option v-for="(sprint, index) in mainfilled" :key="index" :value="sprint.value">{{
          sprint.key }}</option>
        </select>
      </div>
      <div>
        <label for="sprint" class="form-label">Sub Modules</label>
        <select required class="form-select selecBox" v-model="modelValue">
          <option value=""> Sub Modules</option>
          <option v-for="(sprint, index) in mainfilled" :key="index" :value="sprint.value">{{
          sprint.key }}</option>
        </select>
      </div>

    </div>
   
    <div v-for="(item, index) in dataItems" :key="index">

      <input type="text" v-model="item.key" :placeholder="'Enter Key ' + (index + 1)">
      <input type="text" v-model="item.value" :placeholder="'Enter Value for '">
    </div>
    <button @click="addInputFields">Add Key-Value Pair</button>
    <button @click="generatePDF">Generate PDF</button>
  </div>
</template>

<script>
import jsPDF from 'jspdf';

export default {
  data() {
    return {
      dataItems: [{ key: '', value: '' }],
      mainfilled: [{
        key: 'Sales Entery',
        value: 'Sales Entery'
      },
      {
        key: 'POS Entery',
        value: 'POS Entery'
      },
      {
        key: 'Purchase Entery',
        value: 'Purchase Entery'
      },

      {
        key: 'Receipt Entery',
        value: 'Receipt Entery'
      },
      {
        key: 'Payment Entery',
        value: 'Payment Entery'
      },
      {
        key: 'Expense Entery',
        value: 'Expense Entery'
      },
      {
        key: 'Product Entery',
        value: 'Product Entery'
      },
      {
        key: 'Sales Record',
        value: 'Sales Record'
      },
      {
        key: 'Purchase Record',
        value: 'Purchase Record'
      },
      {
        key: "Stock Report",
        value: "Stock Report"
      },
      {
        key: "Customer Due Balance",
        value: "Customer Due Balance"
      },
      {
        key: "Supplier Due Balance",
        value: "Supplier Due Balance"
      }, {
        key: "Customer Ledger",
        value: "Customer Ledger"
      },
      {
        key: "Supplier Ledger",
        value: "Supplier Ledger"
      },
      {
        key: "Cash & Bank Balance",
        value: "Cash & Bank Balance"
      }
      ],
      projectType: [{
        key: 'Retail management System(ERP)',
        value: 'Retail management System (ERP)'
      },
      {
        key: 'Manufacturing Management System(ERP)',
        value: 'Manufacturing Management System(ERP)'
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
      subProjectType: [{
        key: 'Retail management System(ERP)',
        value: 'Retail management System (ERP)'
      },
      {
        key: 'Manufacturing Management System(ERP)',
        value: 'Manufacturing Management System(ERP)'
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
      subModulesSalesEntry:[{
        key: "Sales Module",
        value: "Sales Module"
      },
      {
        key:"Sales Entry",
        value:"Sales Entry"
      },
      {
        key:"POS Entry",
        value:"POS Entry"
      },{
        key:"Customer Entry",
        value:"Customer Entry"
      },
      {
        key:"Sales Return Entry",
        value:"Sales Return Entry"
      },
      {
        key:"Replace Entry",
        value:"Replace Entry"
      },
      {
        key:"View Sales Vouchers",
        value:"View Sales Vouchers"
      },
      {
        key:"Sales Return Vouchers",
        value:"Sales Return Vouchers"
      },
      {
        key:"Sales Record",
        value:"Sales Record"
      },{
        key:" Sales Return Record",
        value:"Sales Return Record"
      },
      {
        key:"Replace Record",
        value:"Replace Record"
      }
      ],
      subModulePOSEntry:[{
        key: "Sales Module",
        value: "Sales Module"
      },
      {
        key:"Sales Entry",
        value:"Sales Entry"
      },
      {
        key:"POS Entry",
        value:"POS Entry"
      },{
        key:"Customer Entry",
        value:"Customer Entry"
      },
      {
        key:"Sales Return Entry",
        value:"Sales Return Entry"
      },
      {
        key:"Replace Entry",
        value:"Replace Entry"
      },
      {
        key:"View Sales Vouchers",
        value:"View Sales Vouchers"
      },
      {
        key:"Sales Return Vouchers",
        value:"Sales Return Vouchers"
      },
      {
        key:"Sales Record",
        value:"Sales Record"
      },{
        key:" Sales Return Record",
        value:"Sales Return Record"
      },
      {
        key:"Replace Record",
        value:"Replace Record"
      }
      ],
      subModulePurchaseEntry:[{
        key: "Purchase Module",
        value: "Purchase Module"
      },
      {
        key:"Purchase Entry",
        value:"Purchase Entry"
      },
      {
        key:"Supplier Entry",
        value:"Supplier Entry"
      },{
        key:"Purchase Return Entry",
        value:"Purchase Return Entry"
      },
      
      {
        key:"Purchase Vouchers",
        value:"Purchase Vouchers"
      },
      {
        key:"Purchase return Vouchers",
        value:"Purchase return Vouchers"
      },
     
      {
        key:"Purchase Record",
        value:"Purchase Record"
      },{
        key:" Purchase Return Record",
        value:"Purchase Return Record"
      }
      
      ],
      subModuleRecepitEntry:[{
        key: "Accounts Module",
        value: "Accounts Module"
      },
      {
        key:"Customer Receipt Entry",
        value:"Customer Receipt Entry"
      },
      {
        key:"Expense Entry",
        value:"Expense Entry"
      },
      {
        key:"Income Entry",
        value:"Income Entry"
      },
      
      {
        key:"Expense Recognition Entry",
        value:"Expense Recognition Entry"
      },
      {
        key:"Branch Transaction Entry",
        value:"Branch Transaction Entry"
      },
     
      {
        key:"Contra / Single Entry",
        value:"Contra / Single Entry"
      },{
        key:"Advance Transaction Entry",
        value:"Advance Transaction Entry"
      },
      {
        key:"Journal / Double Entry",
        value:"Journal / Double Entry"
      },
      {
        key:"Account Entry",
        value:"Account Entry"
      },
      {
        key:"Location Entry",
        value:"Location Entry"
      },
      ],
      subModulePaymentEntry:[{
        key: "Accounts Module",
        value: "Accounts Module"
      },
      {
        key:"Customer Receipt Entry",
        value:"Customer Receipt Entry"
      },
      {
        key:"Expense Entry",
        value:"Expense Entry"
      },
      {
        key:"Income Entry",
        value:"Income Entry"
      },
      
      {
        key:"Expense Recognition Entry",
        value:"Expense Recognition Entry"
      },
      {
        key:"Branch Transaction Entry",
        value:"Branch Transaction Entry"
      },
     
      {
        key:"Contra / Single Entry",
        value:"Contra / Single Entry"
      },{
        key:"Advance Transaction Entry",
        value:"Advance Transaction Entry"
      },
      {
        key:"Journal / Double Entry",
        value:"Journal / Double Entry"
      },
      {
        key:"Account Entry",
        value:"Account Entry"
      },
      {
        key:"Location Entry",
        value:"Location Entry"
      },
      ],
      subModuleExpenseEntry:[{
        key: "Accounts Module",
        value: "Accounts Module"
      },
      {
        key:"Customer Receipt Entry",
        value:"Customer Receipt Entry"
      },
      {
        key:"Supplier Receipt Entry",
        value:"Supplier Receipt Entry"
      },
      {
        key:"Expense Entry",
        value:"Expense Entry"
      },
      {
        key:"Income Entry",
        value:"Income Entry"
      },
      
      {
        key:"Expense Recognition Entry",
        value:"Expense Recognition Entry"
      },
      {
        key:"Branch Transaction Entry",
        value:"Branch Transaction Entry"
      },
     
      {
        key:"Contra / Single Entry",
        value:"Contra / Single Entry"
      },{
        key:"Advance Transaction Entry",
        value:"Advance Transaction Entry"
      },
      {
        key:"Journal / Double Entry",
        value:"Journal / Double Entry"
      },
      {
        key:"Account Entry",
        value:"Account Entry"
      },
      {
        key:"Location Entry",
        value:"Location Entry"
      },
      ],
      subModuleProductEntry:[{
        key: "Settings",
        value: "Settings"
      },
      {
        key:"Product Entry",
        value:"Product Entry"
      },
      {
        key:"Unit Entry & Measurment",
        value:"Unit Entry & Measurment"
      },
      {
        key:"Group Entry",
        value:"Group Entry"
      },
      {
        key:"Category Entry",
        value:"Category Entry"
      },
      
      {
        key:"Model Entry",
        value:"Model Entry"
      },
      {
        key:"Origin Entry",
        value:"Origin Entry"
      },
     
      {
        key:"Warehouse Entry",
        value:"Warehouse Entry"
      },{
        key:"Branch Entry",
        value:"Branch Entry"
      },
      {
        key:"SMS Entry",
        value:"SMS Entry"
      },
      {
        key:"User Entry",
        value:"User Entry"
      },
      {
        key:"Company Profile",
        value:"Company Profile"
      },
      ],
      modelValue: '',
      projectTypeValue: '',
      subProjectTypeValue: ''
    }
  },
  methods: {
    generatePDF() {
      const doc = new jsPDF();
      // Example HTML content
      const htmlContent = `
        <h1 style="color: red;">PDF Example</h1>
        <p ref="p1">This is a paragraph inside a PDF generated from HTML content with styling.</p>
      `;
      // Convert HTML to PDF
      doc.html(htmlContent, {
        callback: function (doc) {
          doc.save('example.pdf');
        },
        margin: 10,
        x: 10,
        y: 10
      });
    },
    addInputFields() {
      this.dataItems.push({ key: '', value: '' });
    }
  },
  mounted() {
    console.log(this.modelValue);
  }
}
</script>

<style>
.module{
  display: flex;
 
  width:"100%";
  gap:10px;
  flex-direction: row;
  flex-wrap: wrap;
 
}
.selecBox{
  max-width: 300px;
  
  min-width:300px;
}
/* Add your styles here if needed */
</style>