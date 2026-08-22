---
title: "Matrix Operations: Addition, Subtraction, Multiplication, Inverse"
source: "https://www.geeksforgeeks.org/maths/matrix-operations/"
author:
  - "[[GeeksforGeeks]]"
published: 2020-11-23
created: 2026-07-28
description: "Your All-in-One Learning Portal: GeeksforGeeks is a comprehensive educational platform that empowers learners across domains-spanning computer science and programming, school education, upskilling, commerce, software tools, competitive exams, and more."
tags:
  - "clippings"
---
****Matrix Operations**** are basic calculations performed on matrices to solve problems or manipulate their structure. Common operations include:

- ****Addition****: Add two matrices of the same size.
- ****Subtraction****: Subtract two matrices of the same size.
- ****Scalar Multiplication****: Multiply each element of a matrix by a constant.
- ****Matrix Multiplication****: Multiply two matrices to create a new matrix.
- ****Transpose****: Flip the rows and columns of a matrix.
- ****Inverse****: Find the inverse of a Matrix.

## Addition of Matrices

[Adding matrices](https://www.geeksforgeeks.org/maths/matrix-addition/) is as simple as adding numbers, but there’s one important rule: the matrices must have the same order (i.e., the same number of rows and columns). Once this condition is met, the addition is performed by adding corresponding elements of both matrices to form a new matrix.

![[addition of matrices.webp|addition_of_matrices]]

Matrix Addition

****Example:**** Take three matrices A, B, and C of order (2×2), (2×2), and (3×3), respectively. Find the sum of (A + B) and (A + C).

****Solution:****

> The addition of matrix A and matrix B is found as,
> 
> A + B =
> 
> $$
> \begin{bmatrix}2+1 & 9+7\\ 5+2 & 6+3\end{bmatrix}
> $$
> 
> A + B =
> 
> $$
> \begin{bmatrix}3 & 16\\ 7 & 9\end{bmatrix}
> $$
> 
> Matrix A and matrix C can not be added as their order is not the same.

### Properties of Matrix Addition

There are various properties associated with matrix addition that are, for matrices A, B, and C of the same order, then,

- ****Commutative Law:**** A + B = B + A
- ****Associative Law:**** (A + B) + C = A + (B + C)
- ****Identity of Matrix:**** A + O = O + A = A, where O is a zero matrix, which is the Additive Identity of the Matrix
- ****Additive Inverse:**** A + (-A) = O = (-A) + A, where (-A) is obtained by changing the sign of every element of A, which is the additive inverse of the matrix.

## Subtraction of Matrices

To [subtract two matrices](https://www.geeksforgeeks.org/maths/subtraction-of-matrices/), the matrices ****must have the same order**** (i.e., the same number of rows and columns). Subtraction is performed by subtracting the corresponding elements of the second matrix from the first matrix to form a new matrix. This completes the subtraction operation.

![[Subtraction-of-Matrices.webp|Subtraction-of-Matrices]]

Matrix Subtraction

****Example:**** For matrices A and B, subtract matrix B from matrix A

$$
A = \begin{bmatrix}2 & 9\\ 5 & 6\end{bmatrix}\\B = \begin{bmatrix}1 & 7\\ 2 & 3\end{bmatrix}
$$

****Solution:****

> Matrix A and Matrix B can be easily subtracted as their order is the same. The subtraction of matrix A and matrix B is found as,
> 
> A - B =
> 
> $$
> \begin{bmatrix}2-1 & 9-7\\ 5-2 & 6-3\end{bmatrix}
> $$
> 
> A - B =
> 
> $$
> \begin{bmatrix}1 & 2\\ 3 & 3\end{bmatrix}
> $$

## Scalar Multiplication of Matrices

For any matrix A = \[a <sub>ij</sub>\] <sub>m×n,</sub> if we multiply the matrix A by any scalar (say k), then the scalar ismultiplied by each elementof the matrix, and this is called the scalar multiplication of matrices.

![[scalar multiplication.webp|scalar_multiplication]]

Scalar Multiplication of Matrix

****Example:**** Multiply the matrix A by the scalar value k = 3.

$$
A = \begin{bmatrix}1 & 2\\ 3 & 4\end{bmatrix}
$$

> The scalar multiplication ****kA**** is computed by multiplying each element of ****A**** by 3:
> 
> $$
> kA = 3\times \begin{bmatrix}1 & 2\\ 3 & 4\end{bmatrix} = \begin{bmatrix}3\times1 & 3\times2\\ 3\times3 & 3\times4\end{bmatrix}
> $$
> 
> So,
> 
> $$
> kA = \begin{bmatrix}3 & 6\\ 9 & 12\end{bmatrix}\\
> $$

### Properties of Scalar Multiplication

For any matrices A and B of the same order, and λ and μ are any two scalars, then,

> - λ(A + B) = λA + λB
> - (λ + μ)A = λA + μA
> - λ(μA) = (λμA) = μ(λA)
> - (-λA) = -(λA) = λ(-A)

## Multiplication of Matrices

[Matrix multiplication](https://www.geeksforgeeks.org/maths/matrix-multiplication/) is the operation that helps us multiply two matrices. This is different from algebraic multiplication, and not all matrices can be multiplied. Only those matrices can be multiplied where ****the number of columns in the first is equal to the number of rows in the second****, i.e, for matrix A <sub>m×n</sub> and matrix B <sub>n×p,</sub> the multiplication is possible for any other matrices where the column of the first matrix is not equal to the row in the second matrix, the multiplication is not possible.

![[Matrix-Multiplication.png|Matrix-Multiplication]]

Matrix Multiplication

Also, the multiplication of the matrices is not commutative; if matrix A and matrix B are taken, then A×B ≠ B×A.

### Properties of Matrix Multiplication

> - Matrix Multiplication is not commutative in general i.e AB ≠ BA.
> - Matrix Multiplication is associative i.e (AB)C = A(BC).
> - Matrix Multiplication is distributive over matrix addition i.e A(B + C) = A.B + A.C.
> - The product of two matrices can be null matrix while neither of them is null i.e If AB = 0 it is not necessary that A = 0 or B =0.
> - If AB = AC then B ≠ C ( Cancellation law is not applicable).
> - There exists a multiplicative identity for every square matrix, such as AI = IA = A.

## Transpose Operation of a Matrix

The [transpose operation](https://www.geeksforgeeks.org/maths/transpose-of-a-matrix/) of a matrix rearranges its rows into columns and its columns into rows. For a matrix A of order m×n, denoted as A = \[aij\] <sub>m×n</sub>, its transpose is represented by A <sup>T</sup> and is defined as:

> ****(A)**** **<sup><strong>T</strong></sup>** ****\= \[a**** **<sub><strong>ji</strong></sub>******\]**** **<sub><strong>n×m</strong></sub>**

![[transpose.webp|transpose]]

Transpose of a Matrix

****Example:**** Find the Transpose of the Matrix A:

$$
A = \begin{bmatrix}1 & 2 & 3\\ 4 & 5 & 6 \\7 & 8 & 9\end{bmatrix}
$$

****Solution:****

> $$
> A^T = \begin{bmatrix}1 & 4 & 7\\ 2 & 5 & 8 \\3 & 6 & 9\end{bmatrix}
> $$

## Inverse Operation of a Matrix

The inverse of a matrix A exists only if A is a square matrix (i.e., has the same number of rows and columns) and its determinant is non-zero.

> ****A = \[ij\]**** **<sub><strong>n×n</strong></sub>** and ****|A| ≠ 0****

![[inverse-of-a-matrix.webp|inverse-of-a-matrix]]

Inverse of a Matrix

Specifically, if ∣A∣ = 1, the matrix A is invertible. The inverse of A, denoted as A <sup>−1</sup>, is a matrix that satisfies:

> ****A × A**** **<sup><strong>−1</strong></sup>** ****\= I****

Where ****I**** is the identity matrix of the same order as A. The inverse operation finds this A <sup>−1</sup>.

****Example:**** Find the inverse of the given matrix.

$$
A=\begin{bmatrix}2 & 1 & 3\\ 1 & 0 & 2\\ 4 & 1 & 8\end{bmatrix}
$$

****Solution:****

> ****Step 1:**** **Caclulate the determinant of the matrix**
> 
> $$
> \det(A)=2\begin{vmatrix}0&2\\1&8\end{vmatrix}-1\begin{vmatrix}1&2\\4&8\end{vmatrix}+3\begin{vmatrix}1&0\\4&1\end{vmatrix}
> $$
> 
> $$
> =2(0\cdot8-2\cdot1)-1(8-8)+3(1-0)
> $$
> 
> $$
> =-4+0+3=-1
> $$
> 
> ****Step 2:**** **Calculate Adjoint of the matrix**
> 
> $$
> \operatorname{adj}(A)=\begin{bmatrix}-2&5&2\\0&4&-2\\1&-2&-1\end{bmatrix}
> $$
> 
> ****Step 3:**** **The Inverse is calculated by dividing the adjoint by the determinant**
> 
> $$
> A^{-1}=\frac{1}{-1}\operatorname{adj}(A)
> $$
> 
> $$
> =\begin{bmatrix}2&-5&-2\\0&-4&2\\-1&2&1\end{bmatrix}
> $$

### Related Articles:

> - [Gaussian Elimination Method](https://www.geeksforgeeks.org/dsa/gaussian-elimination/).
> - [Elementary Operations on Matrices](https://www.geeksforgeeks.org/maths/elementary-operations-on-matrices/)
> - [Covariance Matrix](https://www.geeksforgeeks.org/maths/covariance-matrix/)
> - [Eigen Decomposition of a Matrix](https://www.geeksforgeeks.org/engineering-mathematics/eigen-decomposition-of-a-matrix/)
> - [Eigenvalues and Eigenvectors](https://www.geeksforgeeks.org/engineering-mathematics/eigen-values/)

## Solved Examples of Matrix Operations

****Example 1:**** Find the sum of matrix A and B when,

$$
A = \begin{bmatrix}1 & 3\\ 5 & 7\end{bmatrix}\\B = \begin{bmatrix}2 & 4\\ 6 & 8\end{bmatrix}
$$

****Solution:****

> Matrix A and Matrix B can be easily added as their order is the same. The addition of matrix A and matrix B is found as,
> 
> A + B = P =
> 
> $$
> \begin{bmatrix}1+2 & 3+4\\ 5+6 & 7+8\end{bmatrix}
> $$
> 
> P =
> 
> $$
> \begin{bmatrix}3 & 7\\ 11 & 15\end{bmatrix}
> $$

****Example 2:**** Find (A - B) when,

$$
A = \begin{bmatrix}2 & 4\\ 6 & 8\end{bmatrix}\\B = \begin{bmatrix}1 & 3\\ 5 & 7\end{bmatrix}
$$

****Solution:****

> Matrix A and Matrix B can be easily subtracted as their order is the same. The value of (A-B) is found as,
> 
> (A - B) = P =
> 
> $$
> \begin{bmatrix}2-1 & 4-3\\ 6-5 & 8-7\end{bmatrix}
> $$
> 
> P =
> 
> $$
> \begin{bmatrix}1 & 1\\ 1 & 1\end{bmatrix}
> $$

****Example 3:**** Find the transpose of matrix A

$$
A = \begin{bmatrix}2 & 4\\ 6 & 8\\10 & 12\end{bmatrix}
$$

****Solution:****

> Transpose of matrix A is the matrix in which the rows of matrix A are its column and the column are its rows.
> 
> Transpose of matrix A is represented as, (A) <sup>T</sup>
> 
> (A) <sup>T</sup> =
> 
> $$
> \begin{bmatrix}2 & 6  & 10\\ 4 & 8 & 12\end{bmatrix}
> $$

## Unsolved Practice Questions on Matrix Operations

****Question 1:**** Given the matrices:

$$
A = \begin{bmatrix} 2 & 3 \\ -1 & 4 \end{bmatrix} \quad \text{and} \quad B = \begin{bmatrix} 1 & 0 \\ 5 & -2 \end{bmatrix}
$$

.

- Find A + B.
- Find A - B.

****Question 2:**** Given the matrix:

$$
A = \begin{bmatrix}1 & 4 & -2 \\3 & 0 & 5\end{bmatrix}
$$

. Find 3A (scalar multiplication by 3).

****Question 3:**** Given the matrices:

$$
A = \begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix} \quad \text{and} \quad B = \begin{bmatrix} 4 & 0 \\ 1 & 5 \end{bmatrix}
$$

. Find A ⨉ B.

****Question 4:**** Given the Matrix:

$$
A = \begin{bmatrix}1 & 3 & 4 \\2 & 5 & 6\end{bmatrix}
$$

. Find A <sup>T</sup><sub>.</sub>

****Question 5:**** Given the Matrix:

$$
A = \begin{bmatrix}4 & 7 \\2 & 6\end{bmatrix}
$$

. Find the inverse of the matrix A if it exists.