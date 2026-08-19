---
source: "[[Transformasi_Laplace]]"
source_hash: "d651b9654030aa28867238dff430f1c3"
---

# Region of Convergence (ROC)

Dalam Transformasi Laplace, **Region of Convergence (ROC)** adalah himpunan semua titik pada bidang-s (s-plane) di mana integral Transformasi Laplace bernilai terhingga (konvergen).

ROC sangat penting karena:
1. **Identifikasi Sinyal Unik:** Rumus aljabar hasil transformasi (seperti $\frac{1}{s+a}$) tidak memiliki makna fisik yang unik tanpa menyertakan ROC-nya. Fungsi yang sama bisa merepresentasikan sinyal kausal (berjalan ke kanan/masa depan) atau anti-kausal (berjalan ke kiri/masa lalu) tergantung dari ROC-nya.
2. **Kestabilan:** Sebuah sistem LTI (Linear Time-Invariant) dikatakan stabil jika dan hanya jika ROC dari fungsi alih (transfer function) sistem tersebut mencakup sumbu imajiner ($j\omega$) pada bidang-s.
3. **Batas:** ROC tidak boleh memuat kutub (poles), karena pada kutub nilai fungsi menuju tak hingga, sehingga integralnya pasti divergen.
