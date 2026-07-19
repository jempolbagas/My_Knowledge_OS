---
title: "flow-documentation"
course: Software Engineering
tags: []
aliases: ["flow-documentation"]
created: "2026-05-04"
---
# Loan Application and Payment Flow

This document outlines the standard operating procedure and state transitions for a loan application from initial request to final payment.

## Phase 1: Application & Validation

1. **Submission (Nasabah)**
   - The Nasabah fills out the public loan application form (Personal Info, Bank Details, Guarantor, KTP uploads).
   - Upon submission, the system generates a **Tracking ID**.
   - The Nasabah has the ability to click a "Batalkan Pengajuan" (Cancel Application) button while in this state.
   - **State:** `Baru` (New)

2. **Validation (Karyawan)**
   - The Karyawan reviews the `Baru` applications.
   - If there are minor errors (e.g., blurry KTP), the Karyawan contacts the Nasabah out-of-band (WhatsApp) to get the correct info and **manually edits** the application in the system on their behalf.
   - *Security Rule:* The system creates an immutable audit log of all manual edits (Original Value, New Value, Timestamp, Karyawan ID) visible to the Pengawas.
   - *Security Rule:* The Karyawan must contact the Guarantor out-of-band to confirm consent and manually check the "Guarantor Verified" checkbox in the system.
   - The Karyawan validates the data.
   - **Action:** Mark as `Lolos Validasi` (Passed Validation) OR `Rekomendasi Tolak` (Recommend Reject). Both require an internal note.
   - **State:** `Lolos Validasi` OR `Rekomendasi Tolak`

## Phase 2: Approval & Agreement

3. **Final Decision (Pengawas)**
   - The Pengawas reviews applications that are `Lolos Validasi` or `Rekomendasi Tolak`. They review the edit audit logs.
   - **Action:** `Approve` or `Reject`.
   - If `Reject`, the application is dead. Karyawan notifies Nasabah via WhatsApp.
   - **State:** `Disetujui` (Approved) OR `Ditolak` (Rejected).

4. **Invoice Generation (Kasir)**
   - For `Disetujui` applications, the Kasir reviews the auto-calculated detailed installment schedule.
   - **Action:** Click "Generate Invoice". This creates a standardized PDF.
   - **State:** `Menunggu Persetujuan` (Waiting for Agreement).

5. **Nasabah Agreement (Nasabah)**
   - The Nasabah logs into their tracking dashboard using their Phone Number and Tracking ID.
   - They review the generated Invoice and terms. The Nasabah still has access to the "Batalkan Pengajuan" button if they do not agree with the terms.
   - **Action:** Click the legally binding "Saya Setuju" (I Agree) button.
   - **State:** `Disetujui Nasabah` (Agreed by Customer).
   - *(Note: If the application sits in `Menunggu Persetujuan` for too long, the Pengawas can manually `Cancel` it).*

## Phase 3: Disbursement & Repayment

6. **Disbursement (Kasir)**
   - The Kasir sees applications that are `Disetujui Nasabah`.
   - The Kasir transfers the funds via their bank to the Nasabah's registered bank account.
   - **Action:** Upload the Proof of Transfer document to the system.
   - **State:** `Aktif` (Active / Disbursed).
   - The Karyawan downloads the Proof of Transfer and Invoice and sends them to the Nasabah via WhatsApp.
   - The detailed installment schedule becomes visible on the Nasabah's dashboard.

7. **Payment Upload (Nasabah)**
   - When an installment is due, the Nasabah logs in.
   - If the Nasabah is late, the system natively calculates and adds a Late Fee (Denda) to the unpaid installment, dynamically updating the expected amount shown.
   - **Action:** Select a specific unpaid installment and upload a proof of payment file.
   - **State (Installment Level):** `Menunggu Verifikasi` (Pending Verification).

8. **Payment Verification (Kasir)**
   - The Kasir reviews the uploaded proof of payment.
   - **Rule:** The transferred amount must *exactly match* the expected installment amount (which includes any system-calculated late fees).
   - **Action:**
     - If exact: Mark as `Diterima` (Received/Verified).
     - If incorrect (partial, wrong amount, fake receipt): Mark as `Tidak Valid` (Invalid) and leave a reason.
   - If marked `Tidak Valid`, the Karyawan follows up with the Nasabah via WhatsApp to resolve the discrepancy before they upload a new proof.
   - **Error Handling (Undo Process):** If the Kasir mistakenly marks an installment as `Diterima`, they cannot undo it directly. The Kasir must submit a request to the Pengawas with a mandatory reason. The Pengawas can then undo the status, generating an audit log entry.
   - **State (Installment Level):** `Diterima` OR `Tidak Valid` (reverts to Unpaid status effectively).

## Exception States

* **Ditolak (Rejected):** Triggered by Pengawas during the final decision phase. Terminal state.
* **Dibatalkan (Cancelled):** Triggered manually by the Pengawas, usually if an application is stuck waiting for Nasabah agreement. Terminal state.
* **Dibatalkan Nasabah:** Triggered explicitly by the Nasabah via their dashboard before the loan is disbursed. Terminal state.
* **Lost Tracking ID:** If a Nasabah loses their Tracking ID, they must contact the Karyawan via WhatsApp. **Strict SOP:** The Karyawan must verify the Nasabah's identity by asking for at least 2 pieces of PII (e.g., last 4 digits of KTP, Guarantor's name) before providing the Tracking ID.