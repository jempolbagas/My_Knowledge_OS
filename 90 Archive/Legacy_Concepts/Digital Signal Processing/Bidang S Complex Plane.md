---
source: "[[Transformasi Laplace]]"
source_hash: "d651b9654030aa28867238dff430f1c3"
---

# Bidang S (Complex Plane)

Bidang S (S-plane) adalah representasi grafis dari variabel frekuensi kompleks $s = \sigma + j\omega$ yang digunakan dalam Transformasi Laplace.

- **Sumbu Horizontal (Real Axis, $\sigma$):** Merepresentasikan tingkat redaman (damping). Nilai negatif berarti sinyal meluruh (decaying), nilai positif berarti sinyal membesar (growing) menuju tak hingga.
- **Sumbu Vertikal (Imaginary Axis, $j\omega$):** Merepresentasikan frekuensi osilasi (frekuensi sinusoidal murni). Jika $\sigma = 0$, kita berada tepat di sumbu imajiner, yang ekuivalen dengan domain pada Transformasi Fourier.

Dalam DSP, lokasi kutub (poles) pada Bidang S menentukan kestabilan sistem. Agar sistem stabil dan kausal, semua poles harus berada di sebelah kiri sumbu imajiner ($\sigma < 0$).
