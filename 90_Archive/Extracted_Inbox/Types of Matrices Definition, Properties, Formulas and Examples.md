---
title: "Types of Matrices: Definition, Properties, Formulas and Examples"
source: "https://www.geeksforgeeks.org/maths/types-of-matrices/"
author:
  - "[[GeeksforGeeks]]"
published: 2020-11-22
created: 2026-07-28
description: "Your All-in-One Learning Portal: GeeksforGeeks is a comprehensive educational platform that empowers learners across domains-spanning computer science and programming, school education, upskilling, commerce, software tools, competitive exams, and more."
tags:
  - "clippings"
---
A matrix is a rectangular array of numbers arranged in rows and columns. Each element in the matrix is identified by its position, which is denoted as "a <sub>ij</sub> ", where "i" is the row number and "j" is the column number of the element.

In linear algebra, matrices can be classified into various types based on their properties, such as the values of their elements, as well as their order (dimensions).

The different types of matrices are mentioned below,

### Singleton Matrix

A matrix that has only one element is called a singleton matrix. In this type of matrix number of columns and the number of rows is equal to 1. A singleton matrix is represented as \[a\] <sub>1⨯1</sub>.

> $$
> \begin{bmatrix}5\end{bmatrix}_{1 \times 1}
> $$

### Null Matrix

A matrix whose all elements are zero is called a [Null Matrix](https://www.geeksforgeeks.org/maths/zero-matrix/). A null matrix is also called a Zero Matrix because all its elements are zero.

> $$
> \begin{bmatrix}0 & 0 & 0 \\0 & 0 & 0 \\0 & 0 & 0\end{bmatrix}_{3 \times 3}
> $$

### Row Matrix

A matrix that contains only one row and any number of columns is known as a row matrix. A [row matrix](https://www.geeksforgeeks.org/maths/row-matrix/) is represented as \[a\]1⨯n, where 1 is the number of rows and n is the number of columns present in a row matrix.

> $$
> \begin{bmatrix}1 & 3 & 7 \\\end{bmatrix}_{1 \times 3}
> $$

### Column Matrix

A matrix that contains only one column and any number of rows is called a [Column Matrix](https://www.geeksforgeeks.org/maths/column-matrix/). A Column Matrix is represented as \[a\]n⨯1 where n is the number of rows and 1 is the number of columns. An example of a column matrix is given below:

> $$
> \begin{bmatrix}1 \\14 \\4 \\5\end{bmatrix}_{4 \times 1}
> $$

### Horizontal Matrix

A matrix in which the number of rows is lower than the number of columns is called a Horizontal Matrix.

> $$
> \begin{bmatrix}1 & 2 & 3 & 4 \\5 & 6 & 7 & 8\end{bmatrix}_{2 \times 4}
> $$

### Vertical Matrix

The matrix in which the number of rows exceeds the number of columns is called a Vertical Matrix. A Vertical matrix is represented as \[a\] <sub>i⨯j</sub> where i > j.

> $$
> \begin{bmatrix}1 & 2 \\3 & 4 \\5 & 6 \\7 & 8\end{bmatrix}_{4 \times 2}
> $$

### Rectangular Matrix

A matrix that does not have an equal number of rows and columns is known as a [Rectangular Matrix](https://www.geeksforgeeks.org/maths/rectangular-matrix/). A rectangular matrix can be represented as \[A\] <sub>m×n</sub> where m ≠ n. An example of a rectangular matrix is mentioned below:

> $$
> \begin{bmatrix}1 & 3 & 7 & 15 \\3 & 4 & 6 & 11 \\5 & 2 & 9 & 8\end{bmatrix}_{3 \times 4}
> $$

In the above example, we see that the number of rows is 3 while the number of columns is 4, i.e. both are unequal, thus making it a rectangular matrix. We can say that both horizontal and vertical matrices are examples of rectangular matrices.

### Square Matrix

A matrix that has an equal number of rows and an equal number of columns is called a [Square Matrix](https://www.geeksforgeeks.org/maths/square-matrix/). Generally, the representation used for the square matrix is \[A\] <sub>n×n</sub>. An example of a Square Matrix is mentioned below:

> $$
> \begin{bmatrix}8 & 3 & 2 \\6 & 4 & 6 \\5 & 7 & 9\end{bmatrix}_{3 \times 3}
> $$

### Diagonal Matrix

A matrix that has all elements as 0 except diagonal elements is known as a [diagonal matrix](https://www.geeksforgeeks.org/maths/diagonal-matrix/). A Diagonal Matrix is only possible in the case of a Square Matrix. An example of a Diagonal Matrix is mentioned below:

> $$
> \begin{bmatrix}8 & 0 & 0 \\0 & 4 & 0 \\0 & 0 & 9\end{bmatrix}_{3 \times 3}
> $$

### Scalar Matrix

A diagonal matrix whose all diagonal elements are non-zero and the same is called a [Scalar Matrix](https://www.geeksforgeeks.org/maths/scalar-matrix/). Scalar Matrix is a kind of diagonal matrix where all diagonal elements are the same. Identity Matrix is a special case of Scalar Matrix.

> $$
> \begin{bmatrix}4 & 0 & 0 \\0 & 4 & 0 \\0 & 0 & 4\end{bmatrix}_{3 \times 3}
> $$

### Identity Matrix

A diagonal matrix where all the diagonal elements are 1 and all non-diagonal elements are 0 is called an [Identity Matrix](https://www.geeksforgeeks.org/maths/identity-matrix/). The Identity Matrix is called the Unit Matrix. The identity matrix or unit matrix always has an equal number of rows and columns.

> $$
> \begin{bmatrix}1 & 0 & 0 \\0 & 1 & 0 \\0 & 0 & 1\end{bmatrix}_{3 \times 3}
> $$

### Triangular Matrix

A square matrix in which the non-zero elements form a triangular below and above the diagonal is called a [Triangular Matrix](https://www.geeksforgeeks.org/maths/triangular-matrix/). Based on the triangle formed below or above the diagonal, the triangular matrix is classified as:

- ****Upper Triangular Matrix****
- ****Lower Triangular Matrix****

### Upper Triangular Matrix

A square matrix in which all the elements below the diagonal are zero and the elements from the diagonal and above are non-zero elements is called an Upper Triangular Matrix. In an Upper Triangular Matrix, the non-zero elements form a triangular-like shape.

> $$
> \begin{bmatrix}8 & 5 & 6 \\0 & 4 & 7 \\0 & 0 & 9\end{bmatrix}_{3 \times 3}
> $$

### Lower Triangular Matrix

A square matrix in which all the elements above the diagonal are zero and the elements from the diagonal and below are non-zero elements is called a Lower Triangular Matrix. In a Lower Triangular Matrix, the non-zero elements form a triangular-like shape from the diagonal and below.

> $$
> \begin{bmatrix}8 & 0 & 0 \\6 & 4 & 0 \\5 & 7 & 9\end{bmatrix}_{3 \times 3}
> $$

### Singular Matrix

A [singular matrix](https://www.geeksforgeeks.org/maths/singular-matrix/) is referred to as a square matrix whose determinant is zero and is not invertible.  
If det A = 0, a square matrix "A" is said to be singular; otherwise, it is said to be non-singular.

> $$
> A = \begin{bmatrix}3 & 6 & 9 \\6 & 12 & 18 \\2 & 4 & 6\end{bmatrix}
> $$
> 
>   
> ⇒ |A| = 3(12 × 6 - 18 × 4) - 6(6 × 6 - 18 × 2) + 9(6 × 4 - 12 × 2)  
> ⇒ |A| = 3(72 - 72) - 6(36 - 36) + 9(24 - 24)  
> ⇒ |A| = 3 × 0 - 6 × 0 + 9 × 0 = 0

### Non Singular Matrix

A [Non-Singular matrix](https://www.geeksforgeeks.org/maths/non-singular-matrix/) is defined as a square matrix whose determinant is not equal to zero and is invertible.

> $$
> |A| =\begin{bmatrix}1 & 5 \\9 & 8\end{bmatrix}
> $$
> 
> ⇒ |A| = 8 × 1 - 9 × 5 = 8 - 45 = -37

### Symmetric Matrix

A square matrix "A" of any order is defined as a [symmetric matrix](https://www.geeksforgeeks.org/maths/what-is-symmetric-matrix-and-skew-symmetric-matrix/) if the transpose of the matrix is equal to the original matrix itself, i.e., A <sup>T</sup> = A.

> $$
> |A| =\begin{bmatrix}2 & 1 \\1 & 2\end{bmatrix}
> $$

### Skew Symmetric Matrix

A square matrix "A" of any order is defined as a [skew-symmetric matrix](https://www.geeksforgeeks.org/maths/what-is-symmetric-matrix-and-skew-symmetric-matrix/#:~:text=it%20is%20symmetric.-,Skew%20Symmetric%20Matrix,-If%20for%20a) if the transpose of the matrix is equal to the negative of the original matrix itself, i.e., A <sup>T</sup> = -A.

> $$
> \begin{bmatrix}0 & 3 & 5 \\-3 & 0 & -2 \\-5 & 2 & 0\end{bmatrix}
> $$

### Orthogonal Matrix

A square matrix whose transpose is equal to its inverse is called [Orthogonal Matrix](https://www.geeksforgeeks.org/maths/orthogonal-matrix/). In an Orthogonal Matrix if A <sup>T</sup> = A <sup>-1</sup> then AA <sup>T</sup> = I where I is the Identity Matrix.

> $$
> A =\begin{bmatrix}\cos(\theta) & -\sin(\theta) \\\sin(\theta) & \cos(\theta)\end{bmatrix}
> $$
> 
> and
> 
> $$
> A^{T} =\begin{bmatrix}\cos(\theta) & \sin(\theta) \\-\sin(\theta) & \cos(\theta)\end{bmatrix}
> $$
> 
> $$
> A \times A^{T} =\begin{bmatrix}\cos^{2}(\theta) + \sin^{2}(\theta) &\cos(\theta)\sin(\theta) - \cos(\theta)\sin(\theta)\\[6pt]\sin(\theta)\cos(\theta) - \cos(\theta)\sin(\theta) &\cos^{2}(\theta) + \sin^{2}(\theta)\end{bmatrix}
> $$
> 
> $$
> \Rightarrow\ A \times A^{T} =\begin{bmatrix}1 & 0 \\0 & 1\end{bmatrix}= I_{(2 \times 2)}
> $$

### Idempotent Matrix

An [idempotent matrix](https://www.geeksforgeeks.org/maths/idempotent-matrix/) is a special type of square matrix that remains unchanged when multiplied by itself, i.e., A <sup>2</sup> = A.

> $$
> A =\begin{bmatrix}1 & 0 \\0 & 0\end{bmatrix}
> $$
> 
> Hence,
> 
> $$
> A \cdot A =\begin{bmatrix}1 & 0 \\0 & 0\end{bmatrix}\cdot\begin{bmatrix}1 & 0 \\0 & 0\end{bmatrix}=\begin{bmatrix}1 & 0 \\0 & 0\end{bmatrix}= A
> $$

### Nilpotent Matrix

A [Nilpotent](https://www.geeksforgeeks.org/maths/nilpotent-matrix/) is a square matrix that when raised to some positive power results in a zero matrix. The least power let's say 'p' for which the matrix yields zero matrices, then it is called the Nilpotent Matrix of power 'p'.

> $$
> A =\begin{bmatrix}0 & 1 & 2 \\0 & 0 & 3 \\0 & 0 & 0\end{bmatrix}
> $$
> 
> $$
> \Rightarrow A^{2} =\begin{bmatrix}0 & 1 & 2 \\0 & 0 & 3 \\0 & 0 & 0\end{bmatrix}\cdot\begin{bmatrix}0 & 1 & 2 \\0 & 0 & 3 \\0 & 0 & 0\end {bmatrix}
> $$
> 
> $$
> =\begin{bmatrix}0 & 0 & 3 \\0 & 0 & 0 \\0 & 0 & 0\end{bmatrix}
> $$
> 
> $$
> \Rightarrow A^{2} =\begin{bmatrix}0 & 0 & 3 \\0 & 0 & 0 \\0 & 0 & 0\end{bmatrix}
> $$
> 
> and A <sup>3</sup> = A. A <sup>2</sup>
> 
> $$
> \Rightarrow A^{3} =\begin{bmatrix}0 & 1 & 2 \\0 & 0 & 3 \\0 & 0 & 0\end{bmatrix}\cdot\begin{bmatrix}0 & 0 & 3 \\0 & 0 & 0 \\0 & 0 & 0\end{bmatrix}=\begin{bmatrix}0 & 0 & 0 \\0 & 0 & 0 \\0 & 0 & 0\end{bmatrix}
> $$
> 
> Hence, A is a Nilpotent Matrix of index 3.

### Periodic Matrix

A periodic matrix is a square matrix that exhibits periodicity, meaning there exists a positive integer ****p**** such that when the matrix is raised to the power ****p+1****, it equals the original matrix (****A**** **<sup><strong>p+1</strong></sup>** ****\= A)****. If p = 1 then A <sup>2</sup> = A it means A is an Idempotent Matrix. Thus we can say that the Idempotent Matrix is a case of the Periodic Matrix.

> $$
> A = \begin{bmatrix}1 & 0 \\0 & 0\end{bmatrix}
> $$

The above square matrix is a Periodic Matrix of Period 2, where p = 1.

### Involutory Matrix

An [involutory matrix](https://www.geeksforgeeks.org/maths/involutory-matrix/) is a special type of square matrix whose inverse is the original matrix itself, i.e., P = P <sup>-1</sup>, or, in other words, its square is equal to an identity matrix i.e. P <sup>2</sup> = I.

> $$
> A = \begin{bmatrix}2 & 1 \\-3 & -2\end{bmatrix}
> $$

### Hermitian Matrix

A complex square matrix is called a [Hermitian Matrix](https://www.geeksforgeeks.org/maths/hermitian-matrix/) if the conjugate transpose of the matrix is equal to the original matrix. In this type of matrix, the diagonal elements must be a real number.

> $$
> A = \begin{bmatrix}2 & 1 \\-3 & -2\end{bmatrix}
> $$

### Skew Hermitian Matrix

A complex square matrix is called a Skew Hermitian Matrix if the conjugate transpose of the matrix is equal to the negative of the original matrix. In this type of matrix, the diagonal elements can be either 0 or a complex number but can not be real numbers other than 0.

> $$
> A = \begin{bmatrix}2i & 2i & -3i \\-2i & 0 & 4 \\3i & -4 & 0\end{bmatrix}
> $$

### Boolean Matrix

The matrix which represents the binary relationship and takes 0 and 1 as its element is called a Boolean Matrix.

> $$
> \begin{bmatrix}1 & 0 & 1 \\0 & 1 & 0 \\1 & 1 & 0\end{bmatrix}
> $$

### Stochastic Matrix

A square matrix represents probability data, meaning that each element is non-negative, and the sum of the elements in each row is equal to 1. Such a matrix is called a [stochastic matrix](https://www.geeksforgeeks.org/maths/stochastic-matrix/).

> $$
> \begin{bmatrix}0.2 & 0.5 & 0.3 \\0.1 & 0.3 & 0.6 \\0.4 & 0.2 & 0.4\end{bmatrix}
> $$

## Summary

Different types of matrices in linear algebra along with their representation is given below.

| ****Matrix Type**** | ****Example**** |
| --- | --- |
| ****Singleton Matrix**** | $$ \begin{bmatrix} 1 \end{bmatrix} $$ |
| ****Null Matrix**** | $$ \mathbf{O} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} $$ |
| ****Row Matrix**** | $$ {R} = \begin{bmatrix} 1 & 2 & 3 \end{bmatrix} $$ |
| ****Column Matrix**** | $$ \mathbf{C} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} $$ |
| ****Horizontal Matrix**** | $$ \mathbf{H} = \begin{bmatrix} 1 & 2 & 3 \end{bmatrix} $$ |
| ****Vertical Matrix**** | $$ \mathbf{V} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} $$ |
| ****Rectangular Matrix**** | $$ \mathbf{A} = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix} $$ |
| ****Square Matrix**** | $$ \mathbf{S} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} $$ |
| ****Diagonal Matrix**** | $$ {D} = \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix} $$ |
| ****Scalar Matrix**** | $$ {M} = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} $$ |
| ****Identity Matrix**** | $$ \mathbf{I} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} $$ |
| ****Triangular Matrix**** | $$ \mathbf{T} = \begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix} $$ |
| ****Singular Matrix**** | \|A\| = 0; determinant is zero |
| ****Non-Singular Matrix**** | \|A\| ≠ 0; determinant is not equal to zero |
| ****Symmetric Matrix**** | A <sup>T</sup> = A; square matrix that remains same when its transpose is taken |
| ****Skew-Symmetric Matrix**** | A <sup>T</sup> = -A; square matrix with transpose equal to negative |
| ****Orthogonal Matrix**** | Q Q <sup>T</sup> = l <sub>n</sub> = Q <sup>T</sup> Q |
| ****Idempotent Matrix**** | A\*A = A |
| ****Nilpotent Matrix**** | A <sup>k</sup> = 0; where, k ≤ n |
| ****Periodic Matrix**** | A <sup>(k+1)</sup> = A |
| ****Involutory Matrix**** | A\*A = I |
| ****Hermitian Matrix**** | $$ A = \overline{A^{\mathsf{T}}} $$ |
| ****Skew Hermitian Matrix**** | If A is a skew-hermitian matrix, then A <sup>*</sup> = -A |
| ****Boolean Matrix**** | $$ \mathbf{B} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} $$  ; element is either 0 or 1. |
| ****Stochastic Matrix**** | $$ \mathbf{B} = \begin{bmatrix} 1 & 2.2 \\ 0 & 14 \end{bmatrix} $$  ; all elements are non-negative. |

## Practice Problems

****Question 1.**** Given the following matrix, is it a Singular or Non-Singular matrix?

$$
B = \begin{pmatrix} 5 & 2 \\1 & 2 \end{pmatrix}
$$

.

****Question 2.**** Given the matrix

$$
A = \begin{pmatrix} 1 & 3 & 0 \\2 & 4 & 1 \\1 & 1 & 2 \end{pmatrix}
$$

Is matrix A symmetric or skew-symmetric?

****Question 3.**** Given the matrix

$$
A = \begin{pmatrix} 1 & 3 & 0 \\2 & 4 & 1 \\1 & 1 & 2 \end{pmatrix}
$$

Find the determinant of matrix A.

****Question 4.**** What type of matrix has its transpose equal to its inverse?

****Question 5.**** What type of matrix has all its elements as zero?

****Question 6.**** Which matrix has the same elements along the diagonal and zero elsewhere?

$$
\Rightarrow A^{2} =\begin{bmatrix}0 & 0 & 3 \\0 & 0 & 0 \\0 & 0 & 0\end{bmatrix}
$$

10 Questions

Which of the following describes a matrix that contains only one row and any number of columns?

- A
	Column Matrix
- B
	Row Matrix
- C
	Square Matrix
- D
	Diagonal Matrix

What is the characteristic of a diagonal matrix?

- A
	All elements are non-zero.
- B
	All elements are zero except the diagonal.
- C
	The number of rows and columns are unequal.
- D
	It contains only one column.

In which type of matrix are all diagonal elements equal to one, while all other elements are zero?

- A
	Scalar Matrix
- B
	Identity Matrix
- C
	Null Matrix
- D
	Upper Triangular Matrix

Which type of matrix is defined as having a determinant equal to zero?

- A
	Non-Singular Matrix
- B
	Singular Matrix
- C
	Orthogonal Matrix
- D
	Symmetric Matrix

Which of the following matrices has the property that its transpose is equal to its inverse ( A <sup>-1</sup> = A <sup>T</sup>)?

- A
	Skew Symmetric Matrix
- B
	Orthogonal Matrix
- C
	Diagonal Matrix
- D
	Triangular Matrix

Which type of matrix has all its entries equal to zero?

- A
	Null Matrix
- B
	Identity Matrix
- C
	Diagonal Matrix
- D
	Singular Matrix

Which of the following matrices is orthogonal?

- A
	$$
	\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
	$$
- B
	$$
	\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
	$$
- C
	$$
	\begin{pmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{pmatrix}
	$$
- D
	All of the Above

What distinguishes a triangular matrix from other matrices?

- A
	It has non-zero elements only on the diagonal.
- B
	It has all elements below (or above) the diagonal as zero.
- C
	It has an equal number of rows and columns.
- D
	It is always a square matrix.

Let A be a 2 × 2 matrix such that A <sup>T</sup> A = 4I. What type of matrix is (1/2) A?

Which of the following matrices is not invertible?

- A
	$$
	\begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}
	$$
- B
	$$
	\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}
	$$
- C
	$$
	\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
	$$
- D
	$$
	\begin{pmatrix} 5 & 0 \\ 0 & 5 \end{pmatrix}
	$$

![success](https://media.geeksforgeeks.org/auth-dashboard-uploads/sucess-img.png)

Quiz Completed Successfully

Your Score:0/10

Accuracy:0%