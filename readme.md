# **Expense Tracker**

This repository contains the source code for building an **Expense Tracker** that helps users monitor monthly expenses across various categories. The project is modular, with the codebase organized into distinct directories based on functionality.

---

## **Project Structure**

### **1. Data Processing**
This directory includes scripts for processing monthly transaction data downloaded in CSV format. It ensures the data is cleaned and formatted for further analysis and categorization.

### **2. Data Categorization**
This directory contains scripts that leverage ChatGPT to categorize transactions into pre-defined categories. The categorization logic can be expanded and fine-tuned based on user feedback.

### **3. Database**
This directory contains scripts to:
- Establish connections to a database.
- Create necessary tables.
- Perform CRUD (Create, Read, Update, Delete) operations to manage expense data.

---

## **Planned Improvements**

### **1. Configuration Improvements**
- **Dynamic Category Management:**
  - Add a configuration file (e.g., `categories.yml`) to define categories dynamically, eliminating the need for hardcoded category lists.

### **2. Enhanced Categorization**
- **Training ChatGPT:**
  - Add functionality to fine-tune ChatGPT categorization in the following scenarios:
    - When ChatGPT assigns a transaction to an incorrect category.
    - When transactions need to be categorized under a "Miscellaneous" category.

- **Sub-Categories:**
  - Introduce sub-category functionality:
    - Create a configuration file for sub-categories.
    - Add logic to identify and assign sub-categories to all transactions.
    - Update the database schema to include a `sub_category` column.
    - Backfill sub-categories for historical transaction data.
    - Modify existing functions (e.g., `insert_transactions`) to accommodate the schema changes.

---

## **Future Enhancements**
- **Analytics Dashboards:** Integrate visualization tools to track expenses by categories, sub-categories, or over time.
- **Mobile/Cloud Integration:** Extend the tracker for mobile or cloud-based access.
- Error Handling for gpt

---


