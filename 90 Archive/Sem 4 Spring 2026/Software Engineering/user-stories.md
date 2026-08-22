---
title: "user-stories"
course: Software Engineering
tags: []
aliases: ["user-stories"]
created: "2026-05-04"
---
## **1. Role: Nasabah (Customer)**

### **US-01: Initiate Loan Request**
* **User Story:** As a **Nasabah**, I want to **fill out a form with my personal details, bank account details, guarantor details, loan amount, and installment type**, so that **I can initiate a loan request.**
* **Acceptance Criteria:**
    1. The system must provide a form capturing personal details, loan amount, and installment type.
    2. The system must capture Bank Account Details (Bank Name, Account Number, Account Name).
    3. The system must capture Guarantor Details (Full Name, Phone Number, Relationship to Nasabah).
    4. The system must validate the input before allowing submission.

### **US-02: Secure Identity Verification**
* **User Story:** As a **Nasabah**, I want to **upload my KTP and Guarantor's KTP securely**, so that **my identity can be verified safely.**
* **Acceptance Criteria:**
    1. The system must allow file uploads for KTP and Guarantor's KTP.
    2. The uploaded files must be stored securely.

### **US-03: Tracking ID Generation & Recovery**
* **User Story:** As a **Nasabah**, I want to **receive a unique Tracking ID upon submission**, so that **I can check my application status later.**
* **Acceptance Criteria:**
    1. Upon successful submission, the system generates and displays a unique Tracking ID.
    2. If a Tracking ID is lost, the Nasabah must contact the Karyawan manually to retrieve it. (Note: Karyawan adheres to SOP requiring verification of at least 2 PII data points before sharing).

### **US-04: Stateless Status Tracking, Loan Management & Cancellation**
* **User Story:** As a **Nasabah**, I want to **log in using my Phone Number and Tracking ID**, so that **I can view my application status, review terms, cancel my application if desired, and view my detailed installment schedule.**
* **Acceptance Criteria:**
    1. The system provides a login interface requiring only Phone Number and Tracking ID.
    2. Upon successful login, the system displays the current approval status of the application.
    3. While the application is in "Baru" or "Menunggu Persetujuan" state, the system provides a "Batalkan Pengajuan" (Cancel Application) button.
    4. If the application is in "Menunggu Persetujuan", the system must display the generated invoice/terms and provide a legally binding "Saya Setuju" (I Agree) button.
    5. Once the loan is disbursed, the dashboard displays a detailed installment schedule table showing each installment, its due date, expected amount (including system-calculated late fees if applicable), and current status.
    6. If the application is rejected, the system displays a generic, polite rejection message without exposing internal employee notes.

### **US-05: Upload Proof of Payment for Specific Installment**
* **User Story:** As a **Nasabah**, I want to **upload my proof of payment directly to a specific unpaid installment on my schedule**, so that **the Kasir can verify my payment for that specific month.**
* **Acceptance Criteria:**
    1. The system provides an interface for the Nasabah to upload proof of payment files explicitly linked to a specific unpaid installment.


## **2. Role: Karyawan (Employee)**

### **US-06: View & Manage Loan Applications Queue**
* **User Story:** As a **Karyawan**, I want to **view a queue of new loan applications and search for specific applications**, so that **I can check completeness and assist Nasabah who lost their Tracking IDs.**
* **Acceptance Criteria:**
    1. The dashboard displays a list or queue of all new loan applications.
    2. The dashboard includes a search functionality to find applications by Nasabah Name, Phone Number, or Tracking ID.
    3. The system allows the Karyawan to manually edit Nasabah application data on their behalf to correct minor errors before validation.
    4. **Audit Trail:** Any edits made by the Karyawan trigger the creation of an immutable audit log entry containing the Original Value, New Value, Timestamp, and Karyawan ID.

### **US-07: Validate Application & Guarantor**
* **User Story:** As a **Karyawan**, I want to **mark an application as "Lolos Validasi" (Passed) or "Rekomendasi Tolak" (Recommend Reject) with a note, and verify Guarantor consent**, so that **the Pengawas knows which loans to review and approve/reject.**
* **Acceptance Criteria:**
    1. The system provides a mandatory "Guarantor Verified" checkbox that the Karyawan must tick after successfully contacting the Guarantor out-of-band.
    2. The system allows the Karyawan to change the application status to "Lolos Validasi" or "Rekomendasi Tolak".
    3. The system requires an internal note to be added when changing the status.

### **US-08: Download and Forward Documents**
* **User Story:** As a **Karyawan**, I want to **download the Kasir-generated invoice and proof of transfer from my dashboard**, so that **I can manually send them to the Nasabah via WhatsApp.**
* **Acceptance Criteria:**
    1. The system provides download links/buttons for the invoice and proof of transfer on the application details page.

### **US-09: Send Payment Reminders**
* **User Story:** As a **Karyawan**, I want to **view the due dates for active loans and copy a text template**, so that **I can manually send payment reminders via WhatsApp.**
* **Acceptance Criteria:**
    1. The system displays a list of active loans with their respective upcoming installment due dates.
    2. The system provides a pre-formatted text template that can be copied to the clipboard.

### **US-10: Notify Rejected Applications & Resolve Payment Issues**
* **User Story:** As a **Karyawan**, I want to **view applications that have been rejected or payments marked invalid, and copy a text template**, so that **I can manually notify the Nasabah via WhatsApp to inform them or resolve payment discrepancies.**
* **Acceptance Criteria:**
    1. The system displays a list of rejected applications and invalid payments.
    2. The system provides pre-formatted text templates for rejection and invalid payment follow-up.
    3. The Karyawan handles out-of-band communication for partial or incorrect payments before the Nasabah re-uploads a new proof.


## **3. Role: Pengawas (Supervisor)**

### **US-11: View Validated Applications and Audit Logs**
* **User Story:** As a **Pengawas**, I want to **view a list of applications validated by the Karyawan, along with any edit audit logs**, so that **I can make a fully informed final approval decision.**
* **Acceptance Criteria:**
    1. The dashboard displays a list of applications with the status "Lolos Validasi" or "Rekomendasi Tolak".
    2. The application details page displays the immutable audit log of any edits made by the Karyawan during validation.

### **US-12: Approve, Reject, Cancel Applications, and Override Payments**
* **User Story:** As a **Pengawas**, I want to **approve, reject, or manually cancel applications, and handle payment undo requests**, so that **I have full control over the final credit decision and correction of Kasir errors.**
* **Acceptance Criteria:**
    1. The system provides "Approve", "Reject", and "Cancel" buttons for applications.
    2. Upon approval, the application moves to the Kasir's dashboard for invoice generation.
    3. Upon rejection or cancellation, the system requires an internal note.
    4. The system allows the Pengawas to review requests from the Kasir to undo a verified payment (change "Diterima" back to "Unpaid"), and upon approval, generates an audit log entry.


## **4. Role: Kasir (Cashier)**

### **US-13: View Approved Loans Dashboard**
* **User Story:** As a **Kasir**, I want to **view a dashboard of all loans approved by the Pengawas**, so that **I can generate invoices and prepare for disbursement.**
* **Acceptance Criteria:**
    1. The dashboard displays a list of applications approved by the Pengawas.

### **US-14: Automatic Installment Calculation & Fee Management**
* **User Story:** As a **Kasir**, I want **the system to automatically calculate the detailed installment schedule and natively manage late fees**, so that **the exact expected amount is always accurate.**
* **Acceptance Criteria:**
    1. The system automatically computes and displays the detailed installment schedule based on loan parameters.
    2. The system natively supports adding a Late Fee (Denda) to unpaid installments, adjusting the expected amount dynamically.

### **US-15: Generate Standardized Invoice**
* **User Story:** As a **Kasir**, I want to **click a button to generate a standardized PDF invoice containing the office details, Nasabah details, and calculated detailed payment schedule**, so that **it can be reviewed by the Nasabah.**
* **Acceptance Criteria:**
    1. The system provides a button to generate a PDF invoice.
    2. Generating the invoice changes the application status to "Menunggu Persetujuan".

### **US-16: Upload Proof of Transfer**
* **User Story:** As a **Kasir**, I want to **upload a proof of transfer document ONLY AFTER the Nasabah has agreed to the terms**, so that **the disbursement is legally backed and documented.**
* **Acceptance Criteria:**
    1. The system allows proof of transfer upload *only* for applications in the "Agreed" status.
    2. Uploading the file marks the loan as disbursed ("Aktif").

### **US-17: Strict Review of Proof of Payment & Error Handling**
* **User Story:** As a **Kasir**, I want to **review proof of payment and strictly mark it as received or invalid, with the ability to request a correction from the Pengawas if I make a mistake**, so that **accounting remains accurate.**
* **Acceptance Criteria:**
    1. The system allows the Kasir to view uploaded proof of payment linked to a specific installment.
    2. The system allows the Kasir to mark the payment as verified/received *only* if the payment amount exactly matches the expected amount (including any system-calculated late fees).
    3. The system allows the Kasir to mark a payment as "Invalid/Rejected" (requiring a reason).
    4. If the Kasir mistakenly marks an installment as "Diterima", they cannot undo it directly but can submit an "Undo Request" to the Pengawas with a mandatory reason.