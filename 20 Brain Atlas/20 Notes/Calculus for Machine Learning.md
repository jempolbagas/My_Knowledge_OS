---
type: note
title: "Calculus for Machine Learning"
subject: "Mathematics"
created: 2026-09-03
prerequisites: []
tags:
  - calculus
  - mathematics
  - machine-learning
  - optimization
---

Kalkulus untuk Machine Learning pada hakikatnya berfokus pada satu tujuan utama: **mengukur sensitivitas perubahan output terhadap perubahan input untuk memandu optimasi**. Anda tidak memerlukan pembuktian teoretis $\epsilon$-$\delta$ atau teknik integrasi simbolik yang rumit; fondasi kalkulus yang menggerakkan hampir seluruh algoritma modern (termasuk [[Backpropagation]]) hanya bertumpu pada tiga pilar: **laju perubahan (turunan biasa)**, **isolasi variabel (turunan parsial)**, dan **perambatan komposisi (aturan rantai / chain rule)**.

## 1. Turunan Biasa: Mengukur "Senggolan"

Turunan $\frac{df}{dx}$ pada dasarnya menjawab pertanyaan sederhana:
> *"Jika nilai $x$ disenggol sedikit ke kanan sebesar $\Delta x$, apakah nilai $f(x)$ akan naik atau turun, dan seberapa cepat respon perubahannya?"*

Secara formal:
$$ \frac{df}{dx} = \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x} $$

- **Tanda Positif ($+$):** $x$ naik $\implies f(x)$ ikut naik.
- **Tanda Negatif ($-$):** $x$ naik $\implies f(x)$ malah turun.
- **Besar Angka (Magnitudo):** Sensitivitas atau kecuraman lereng.
- **Nol ($0$):** Titik datar / stasioner (kandidat lembah minimum atau puncak maksimum).

## 2. Turunan Parsial ($\partial$): Isolasi Satu Variabel

Dalam Machine Learning, fungsi rugi (*Loss*) tidak hanya bergantung pada 1 angka, melainkan pada jutaan bobot sekaligus: $\mathcal{L}(w_1, w_2, w_3, \dots, b)$.

Turunan parsial $\frac{\partial \mathcal{L}}{\partial w_1}$ memiliki satu aturan emas yang sangat mekanis:
> **Anggap semua variabel lain ($w_2, w_3, b$) sebagai ANGKA KONSTAN (batu mati), lalu turunkan fungsi tersebut HANYA terhadap variabel yang ditargetkan.**

### Worked Example: Turunan Parsial
Misalkan fungsi nilai error dua bobot:
$$ f(x, y) = 3x^2 y + 5y^3 + 7x $$

1. **Hitung $\frac{\partial f}{\partial x}$ (Turunkan terhadap $x$, anggap $y$ angka konstan):**
   - Suku $3x^2 y$: karena $y$ adalah konstanta, anggap seperti $3(c) x^2 \implies 2 \cdot 3y \cdot x = 6xy$.
   - Suku $5y^3$: karena tidak mengandung $x$ sama sekali, maka turunannya adalah $0$.
   - Suku $7x$: turunannya adalah $7$.
   $$ \frac{\partial f}{\partial x} = 6xy + 7 $$

2. **Hitung $\frac{\partial f}{\partial y}$ (Turunkan terhadap $y$, anggap $x$ angka konstan):**
   - Suku $3x^2 y$: $x$ adalah konstanta, sehingga turunannya terhadap $y$ adalah $3x^2(1) = 3x^2$.
   - Suku $5y^3$: turunannya terhadap $y$ adalah $15y^2$.
   - Suku $7x$: tidak mengandung $y$, maka turunannya adalah $0$.
   $$ \frac{\partial f}{\partial y} = 3x^2 + 15y^2 $$

Vektor yang menggabungkan seluruh turunan parsial ini disebut **Gradien ($\nabla f$)**:
$$ \nabla f(x, y) = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix} = \begin{bmatrix} 6xy + 7 \\ 3x^2 + 15y^2 \end{bmatrix} $$

## 3. Aturan Rantai (*Chain Rule*): Rasio Roda Gigi

Ketika fungsi saling bersarang (komposisi fungsi), aturan rantai menghitung laju perubahan total dengan mengalikan laju perubahan di setiap persinggahan.

**Analogi Roda Gigi Sepeda:**
- Jika mengayuh pedal $x$ sebanyak 1 putaran membuat gir tengah $u$ berputar 3 kali ($\frac{du}{dx} = 3$).
- Dan setiap 1 putaran gir tengah $u$ membuat roda belakang $y$ berputar 2 kali ($\frac{dy}{du} = 2$).
- Maka setiap 1 kali kayuhan pedal $x$, roda belakang $y$ berputar:
  $$ \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = 2 \times 3 = 6 \text{ kali} $$

### Worked Example: Chain Rule Komposisi
Misalkan:
$$ y = (3x + 2)^4 $$
Definisikan variabel perantara $u = 3x + 2$, sehingga $y = u^4$.
1. $\frac{dy}{du} = 4u^3$
2. $\frac{du}{dx} = 3$
3. Gabungkan:
   $$ \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = 4u^3 \cdot 3 = 12(3x + 2)^3 $$

Inilah mekanisme persis yang digunakan di [[Backpropagation]] untuk merambatkan turunan dari layer output ke layer input melewati fungsi aktivasi.

> [!abstract]- Quick Reference
> | Aturan Turunan | Rumus $f(x)$ | Turunan $f'(x)$ | Catatan untuk ML |
> | :--- | :--- | :--- | :--- |
> | **Pangkat** | $x^n$ | $n x^{n-1}$ | Dipakai pada fungsi MSE $\frac{1}{2}(\hat{y}-y)^2$ |
> | **Konstanta Pengali** | $c \cdot g(x)$ | $c \cdot g'(x)$ | Konstanta tetap menempel |
> | **Konstanta Murni** | $c$ | $0$ | Lenyap saat diturunkan |
> | **Sigmoid** | $\sigma(z) = \frac{1}{1+e^{-z}}$ | $\sigma(z)(1 - \sigma(z))$ | Turunannya bisa dihitung dari outputnya sendiri |
> | **ReLU** | $\max(0, z)$ | $1$ jika $z > 0$, $0$ jika $z < 0$ | Menghindari vanishing gradient |
> | **Chain Rule** | $f(g(x))$ | $f'(g(x)) \cdot g'(x)$ | Mesin utama backward pass |

> [!question]- Practice
> **Soal 1:** Diberikan fungsi error $\mathcal{L}(w) = \frac{1}{2}(w \cdot x - y)^2$. Turunkan fungsi tersebut terhadap $w$ dengan menganggap $x$ dan $y$ konstan.
> 
> > [!check]- Answer
> > Gunakan chain rule.
> > Misalkan $u = w \cdot x - y \implies \mathcal{L} = \frac{1}{2}u^2$.
> > 1. $\frac{\partial \mathcal{L}}{\partial u} = \frac{1}{2} \cdot 2u = u = (w \cdot x - y)$
> > 2. $\frac{\partial u}{\partial w} = x$ (karena $y$ konstan jadi $0$, dan turunan $w \cdot x$ terhadap $w$ adalah $x$).
> > 3. $\frac{\partial \mathcal{L}}{\partial w} = \frac{\partial \mathcal{L}}{\partial u} \cdot \frac{\partial u}{\partial w} = \mathbf{(w \cdot x - y) \cdot x}$.
> 
> **Soal 2:** Diberikan fungsi $f(x, y) = 4x^3 + 2xy^2 - 9$. Berapakah nilai dari turunan parsial $\frac{\partial f}{\partial y}$ pada titik $(x = 2, y = 3)$?
> 
> > [!check]- Answer
> > 1. Turunkan terhadap $y$ (anggap $x$ konstan):
> >    - Suku $4x^3 \implies 0$
> >    - Suku $2xy^2 \implies 2x(2y) = 4xy$
> >    - Suku $-9 \implies 0$
> >    Maka $\frac{\partial f}{\partial y} = 4xy$.
> > 2. Substitusikan titik $(2, 3)$:
> >    $\frac{\partial f}{\partial y}(2, 3) = 4(2)(3) = \mathbf{24}$.

> [!info]- Going Deeper
> - **Jacobian Matrix:** Matriks yang memuat seluruh turunan parsial orde-1 dari fungsi bervariabel banyak ke output bervariabel banyak ($\mathbb{R}^n \to \mathbb{R}^m$). Dalam backpropagation, perambatan layer-ke-layer pada dasarnya adalah perkalian matriks Jacobian.
> - **Hessian Matrix:** Matriks turunan parsial orde-2 ($\nabla^2 f$) yang mengukur kelengkungan permukaan error.
