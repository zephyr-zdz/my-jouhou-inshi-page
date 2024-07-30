# 行列式 Determinant

## 定义 Definition

**行列式**: 行列式是方阵的一个标量值，用来描述方阵的某些性质，如可逆性。对于一个 $n \times n$ 矩阵 $A$，其行列式记作 $|A|$ 或 $\det(A)$
**Determinant**: The determinant is a scalar value that describes certain properties of a square matrix, such as invertibility. For an $n \times n$ matrix $A$, its determinant is denoted as $|A|$ or $\det(A)$

### 计算 Calculation

1. **$2 \times 2$ 矩阵的行列式 Determinant of a $2 \times 2$ Matrix**:

   $$
   A = \begin{pmatrix}
   a & b \\
   c & d
   \end{pmatrix}, \quad |A| = ad - bc

$$

2. **$3 \times 3$ 矩阵的行列式 Determinant of a $3 \times 3$ Matrix**:
   $$

   A = \begin{pmatrix}

   a_{11} & a_{12} & a_{13} \\

   a_{21} & a_{22} & a_{23} \\

   a_{31} & a_{32} & a_{33}

   \end{pmatrix}

$$
   $$

   |A| = a_{11} \begin{vmatrix}

   a_{22} & a_{23} \\

   a_{32} & a_{33}

   \end{vmatrix} - a_{12} \begin{vmatrix}

   a_{21} & a_{23} \\

   a_{31} & a_{33}

   \end{vmatrix} + a_{13} \begin{vmatrix}

   a_{21} & a_{22} \\

   a_{31} & a_{32}

   \end{vmatrix}

$$

3. **高阶行列式 Higher-Order Determinants**: 可以通过递归使用 $2 \times 2$ 和 $3 \times 3$ 矩阵的行列式公式来计算更高阶的行列式
   Higher-order determinants can be computed recursively using the $2 \times 2$ and $3 \times 3$ determinant formulas

## 拉普拉斯展开 Laplace Expansion

### 定义 Definition

**拉普拉斯展开**: 行列式可以通过任意一行或一列的元素及其余子式来展开
**Laplace Expansion**: A determinant can be expanded along any row or column using its elements and their minors

### 计算 Calculation

对于一个 $n \times n$ 矩阵 $A$，其行列式 $|A|$ 可以沿第 $i$ 行展开为:
For an $n \times n$ matrix $A$, its determinant $|A|$ can be expanded along the $i$-th row as:
$$

|A| = \sum_{j=1}^{n} (-1)^{i+j} a_{ij} M_{ij}

$$

也可以沿第 $j$ 列展开:
It can also be expanded along the $j$-th column:
$$

|A| = \sum_{i=1}^{n} (-1)^{i+j} a_{ij} M_{ij}

$$

## 余子式 Minor

### 定义 Definition

**余子式**: 对于一个 $n \times n$ 矩阵 $A$，其余子式 $M_{ij}$ 是通过删除 $A$ 的第 $i$ 行和第 $j$ 列得到的 $(n-1) \times (n-1)$ 子矩阵的行列式
**Minor**: For an $n \times n$ matrix $A$, the minor $M_{ij}$ is the determinant of the $(n-1) \times (n-1)$ submatrix obtained by deleting the $i$-th row and $j$-th column from $A$

### 计算 Calculation

设 $A$ 为一个 $3 \times 3$ 矩阵:
Let $A$ be a $3 \times 3 matrix:
$$

A = \begin{pmatrix}

a_{11} & a_{12} & a_{13} \\

a_{21} & a_{22} & a_{23} \\

a_{31} & a_{32} & a_{33}

\end{pmatrix}

$$

余子式 $M_{11}$ 通过删除第 $1$ 行和第 $1$ 列得到:
The minor $M_{11}$ is obtained by deleting the 1st row and 1st column:
$$

M_{11} = \begin{vmatrix}

a_{22} & a_{23} \\

a_{32} & a_{33}

\end{vmatrix} = a_{22}a_{33} - a_{23}a_{32}

$$

同理，其他余子式可以类似计算
Similarly, other minors can be calculated similarly

## 代数余子式 Cofactor

### 定义 Definition

**代数余子式**: 对于一个 $n \times n$ 矩阵 $A$，其代数余子式 $C_{ij}$ 是余子式 $M_{ij}$ 乘以 $(-1)^{i+j}$
**Cofactor**: For an $n \times n$ matrix $A$, its cofactor $C_{ij}$ is the minor $M_{ij}$ multiplied by $(-1)^{i+j}$

### 计算 Calculation

代数余子式 $C_{ij}$ 计算如下:
The cofactor $C_{ij}$ is calculated as follows:
$$

C_{ij} = (-1)^{i+j} M_{ij}

$$

## 伴随矩阵 Adjugated Matrix

### 定义 Definition

**伴随矩阵**: 对于一个 $n \times n$ 矩阵 $A$，其伴随矩阵 $\text{adj}(A)$ 是由 $A$ 的余子式组成的转置矩阵，即
**Adjugated Matrix**: For an $n \times n$ matrix $A$, its adjugated matrix $\text{adj}(A)$ is the transpose of the matrix of its cofactors:
$$

\text{adj}(A) = C^T

$$

### 计算 Calculation

对于一个 $3 \times 3$ 矩阵 $A$，其伴随矩阵 $\text{adj}(A)$ 为:
For a $3 \times 3$ matrix $A$, its adjugate matrix $\text{adj}(A)$ is:
$$

\text{adj}(A) = \begin{pmatrix}

C_{11} & C_{21} & C_{31} \\

C_{12} & C_{22} & C_{32} \\

C_{13} & C_{23} & C_{33}

\end{pmatrix}

$$

其中 $C_{ij} = (-1)^{i+j} M_{ij}$ 是 $A$ 的余子式 $M_{ij}$ 的代数余子式
where $C_{ij} = (-1)^{i+j} M_{ij}$ is the cofactor of the minor $M_{ij}$ of $A$

## 矩阵的逆 Inverse of a Matrix

### 计算 Calculation

若矩阵 $A$ 是可逆的，则其逆矩阵 $A^{-1}$ 为:
If a matrix $A$ is invertible, its inverse $A^{-1}$ is given by:
$$

A^{-1} = \frac{1}{|A|} \text{adj}(A)

$$

## 示例 Example

### 计算 $3 \times 3$ 矩阵的行列式和伴随矩阵 Calculate the Determinant and Adjugated Matrix of a $3 \times 3$ Matrix

设 $A$ 为一个 $3 \times 3$ 矩阵:
Let $A$ be a $3 \times 3$ matrix:
$$

A = \begin{pmatrix}

1 & 2 & 3 \\

0 & 4 & 5 \\

1 & 0 & 6

\end{pmatrix}

$$

1. 计算行列式 Calculate the determinant:
$$

|A| = 1 \begin{vmatrix}

4 & 5 \\

0 & 6

\end{vmatrix} - 2 \begin{vmatrix}

0 & 5 \\

1 & 6

\end{vmatrix} + 3 \begin{vmatrix}

0 & 4 \\

1 & 0

\end{vmatrix}

$$
$$

= 1(24) - 2(-5) + 3(-4) = 24 + 10 - 12 = 22

$$

2. 计算余子式 Calculate the minors:
$$

M_{11} = \begin{vmatrix}

4 & 5 \\

0 & 6

\end{vmatrix} = 24, \quad M_{12} = \begin{vmatrix}

0 & 5 \\

1 & 6

\end{vmatrix} = -5, \quad M_{13} = \begin{vmatrix}

0 & 4 \\

1 & 0

\end{vmatrix} = -4

$$
$$

M_{21} = \begin{vmatrix}

2 & 3 \\

0 & 6

\end{vmatrix} = 12, \quad M_{22} = \begin{vmatrix}

1 & 3 \\

1 & 6

\end{vmatrix} = 3, \quad M_{23} = \begin{vmatrix}

1 & 2 \\

1 & 0

\end{vmatrix} = -2

$$
$$

M_{31} = \begin{vmatrix}

2 & 3 \\

4 & 5

\end{vmatrix} = -2, \quad M_{32} = \begin{vmatrix}

1 & 3 \\

0 & 5

\end{vmatrix} = 5, \quad M_{33} = \begin{vmatrix}

1 & 2 \\

0 & 4

\end{vmatrix} = 4

$$

3. 计算代数余子式 Calculate the cofactors:
$$

C_{11} = 24, \quad C_{12} = 5, \quad C_{13} = -4

$$
$$

C_{21} = -12, \quad C_{22} = 3, \quad C_{23} = 2

$$
$$

C_{31} = -2, \quad C_{32} = -5, \quad C_{33} = 4

$$

4. 构造伴随矩阵 Form the adjugated matrix:
$$

\text{adj}(A) = \begin{pmatrix}

24 & -12 & -2 \\

5 & 3 & -5 \\

-4 & 2 & 4

\end{pmatrix}^T = \begin{pmatrix}

24 & 5 & -4 \\

-12 & 3 & 2 \\

-2 & -5 & 4

\end{pmatrix}

$$

5. 计算逆矩阵 Calculate the inverse matrix:
$$

A^{-1} = \frac{1}{|A|} \text{adj}(A) = \frac{1}{22} \begin{pmatrix}

24 & 5 & -4 \\

-12 & 3 & 2 \\

-2 & -5 & 4

\end{pmatrix}

$$
