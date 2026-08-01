---
type: concept
title: Hypervisor
subject: Computer_Science
date_created: 2026-08-01
tags:
  - hypervisor
  - kvm
  - xen
  - virtualization
  - computer-science
source: "[[Virtual_Private_Server_Architecture_and_Mechanics]]"
source_hash: "494ebf3890811af0be27577d3fb7b600"
---

## The idea (one clear statement)
**Hypervisor** (atau *Virtual Machine Monitor / VMM*) adalah lapisan abstraksi perangkat lunak atau *firmware* yang memultipleks dan mengontrol sumber daya perangkat keras fisik (CPU, memori, I/O) untuk menjalankan beberapa sistem operasi *guest* secara bersamaan dalam mode eksekusi terisolasi.

## Why it matters / how it connects
* **Klasifikasi Arsitektural:** Beroperasi sebagai **Type-1 Bare-Metal** (berjalan langsung di atas *hardware* dalam Ring -1 / VMX Root, seperti KVM, Xen, ESXi) untuk performa komputasi maksimum, atau **Type-2 Hosted** (berjalan sebagai aplikasi di atas host OS) untuk fleksibilitas pengujian.
* **Dukungan Ekstensi Hardware:** Memanfaat sistem ekstensi CPU (*Intel VT-x / AMD-V*) dan translasi memori dua tingkat (*Intel EPT / AMD NPT*) untuk mengeksekusi instruksi *guest* pada kecepatan hardware asli tanpa teknik *binary translation* manual.
* **Batas Keamanan Multi-Tenant:** Mengisolasi penyewa multi-tenant dan mencegah serangan inter-VM. Modifikasi instruksi sensitif oleh guest memicu intersepsi *VM Exit*, sementara pertahanan modern mengintegrasikan *confidential computing* (SEV-SNP, TDX) untuk menyembunyikan data memori guest dari administrator host.

## Related concepts
- [[Virtual_Private_Server_Architecture_and_Mechanics]]
- [[Virtual Private Server]]
- [[WebAssembly_vs_Docker]]
