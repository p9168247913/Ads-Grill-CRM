<template>
    <div>
      <h2>Templates</h2>
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
        dataItems: [{ key: '', value: '' }]
      };
    },
    methods: {
      generatePDF() {
        // Create a new jsPDF instance
        const doc = new jsPDF();
  
        // Add header
        const header = 'Header Content';
        doc.setFontSize(16);
        doc.setTextColor(0, 0, 255);
        doc.text(header, 10, 10);

        let yPos = 30; 
        this.dataItems.forEach(item => {
          if (item.key !== '' && item.value !== '') {
            const content = `${item.key}: ${item.value}`;
            doc.setFontSize(12);
            doc.setTextColor(0, 0, 0);
            doc.text(content, 10, yPos);
            yPos += 10; 
          }
        });
  
        // Add footer
        const footer = 'Footer Content';
        const pageSize = doc.internal.pageSize;
        const pageHeight = pageSize.height ? pageSize.height : pageSize.getHeight();
        doc.setFontSize(12);
        doc.setTextColor(0, 0, 0);
        doc.text(footer, 10, pageHeight - 10);
  
        // Save the PDF
        doc.save('document.pdf');
      },
      addInputFields() {
        this.dataItems.push({ key: '', value: '' });
      }
    }
  }
  </script>
  
  <style>
  /* Add your styles here if needed */
  </style>
  