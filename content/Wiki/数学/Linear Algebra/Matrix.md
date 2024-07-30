# 矩阵基本概念 (Basic Concepts of Matrices)

## 矩阵定义 (Matrix Definition)

一个矩阵是一个矩形数组，包含 $m$ 行和 $n$ 列的元素，记作 $\mathbf{A}$：

A matrix is a rectangular array of elements with $m$ rows and $n$ columns, denoted as $\mathbf{A}$:

$$
\mathbf{A} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}
$$

## 矩阵类型 (Types of Matrices)

1. **零矩阵 (Zero Matrix)**: 所有元素均为零的矩阵，记作 $\mathbf{0}$。
   A matrix with all elements being zero, denoted as $\mathbf{0}$.

2. **单位矩阵 (Identity Matrix)**: 对角线元素为 1，非对角线元素为 0 的方阵，记作 $\mathbf{I}$。
   A square matrix with ones on the diagonal and zeros elsewhere, denoted as $\mathbf{I}$.

3. **对角矩阵 (Diagonal Matrix)**: 仅对角线元素可能为非零的方阵。
   A square matrix where only the diagonal elements may be non-zero.

4. **对称矩阵 (Symmetric Matrix)**: 转置后等于自身的矩阵，即 $\mathbf{A} = \mathbf{A}^T$。
   A matrix that is equal to its transpose, i.e., $\mathbf{A} = \mathbf{A}^T$.

5. **反对称矩阵 (Skew-Symmetric Matrix)**: 转置后等于其负的矩阵，即 $\mathbf{A} = -\mathbf{A}^T$。
   A matrix that is equal to the negative of its transpose, i.e., $\mathbf{A} = -\mathbf{A}^T$.

6. **矩形矩阵 (Rectangular Matrix)**: 行数和列数不相等的矩阵。
   A matrix with unequal number of rows and columns.

7. **方阵 (Square Matrix)**: 行数和列数相等的矩阵。
   A matrix with an equal number of rows and columns.

## 矩阵运算 (Matrix Operations)

1. **矩阵加法 (Matrix Addition)**

   两个同维数矩阵的对应元素相加：

   Adding corresponding elements of two matrices of the same dimension:

   $$
   \mathbf{A} + \mathbf{B} = \begin{pmatrix}
   a_{11} & a_{12} & \cdots & a_{1n} \\
   a_{21} & a_{22} & \cdots & a_{2n} \\
   \vdots & \vdots & \ddots & \vdots \\
   a_{m1} & a_{m2} & \cdots & a_{mn}
   \end{pmatrix}
   +
   \begin{pmatrix}
   b_{11} & b_{12} & \cdots & b_{1n} \\
   b_{21} & b_{22} & \cdots & b_{2n} \\
   \vdots & \vdots & \ddots & \vdots \\
   b_{m1} & b_{m2} & \cdots & b_{mn}
   \end{pmatrix}
   =
   \begin{pmatrix}
   a_{11} + b_{11} & a_{12} + b_{12} & \cdots & a_{1n} + b_{1n} \\
   a_{21} + b_{21} & a_{22} + b_{22} & \cdots & a_{2n} + b_{2n} \\
   \vdots & \vdots & \ddots & \vdots \\
   a_{m1} + b_{m1} & a_{m2} + b_{m2} & \cdots & a_{mn} + b_{mn}
   \end{pmatrix}

$$

2. **矩阵减法 (Matrix Subtraction)**

   两个同维数矩阵的对应元素相减：
   Subtracting corresponding elements of two matrices of the same dimension:

   $$

   \mathbf{A} - \mathbf{B} = \begin{pmatrix}
   a_{11} & a_{12} & \cdots & a_{1n} \\
   a_{21} & a_{22} & \cdots & a_{2n} \\
   \vdots & \vdots & \ddots & \vdots \\
   a_{m1} & a_{m2} & \cdots & a_{mn}
   \end{pmatrix}
   -
   \begin{pmatrix}
   b_{11} & b_{12} & \cdots & b_{1n} \\
   b_{21} & b_{22} & \cdots & b_{2n} \\
   \vdots & \vdots & \ddots & \vdots \\
   b_{m1} & b_{m2} & \cdots & b_{mn}
   \end{pmatrix}
   =

   \begin{pmatrix}

   a_{11} - b_{11} & a_{12} - b_{12} & \cdots & a_{1n} - b_{1n} \\

   a_{21} - b_{21} & a_{22} - b_{22} & \cdots & a_{2n} - b_{2n} \\

   \vdots & \vdots & \ddots & \vdots \\

   a_{m1} - b_{m1} & a_{m2} - b_{m2} & \cdots & a_{mn} - b_{mn}

   \end{pmatrix}

$$

3. **数乘矩阵 (Scalar Multiplication)**

   矩阵的每个元素乘以一个标量$c$：
   Multiplying each element of a matrix by a scalar $c$:

   $$

   c\mathbf{A} = c \begin{pmatrix}
   a_{11} & a_{12} & \cdots & a_{1n} \\
   a_{21} & a_{22} & \cdots & a_{2n} \\
   \vdots & \vdots & \ddots & \vdots \\
   a_{m1} & a_{m2} & \cdots & a_{mn}
   \end{pmatrix}
   =

   \begin{pmatrix}

   ca_{11} & ca_{12} & \cdots & ca_{1n} \\

   ca_{21} & ca_{22} & \cdots & ca_{2n} \\

   \vdots & \vdots & \ddots & \vdots \\

   ca_{m1} & ca_{m2} & \cdots & ca_{mn}

   \end{pmatrix}

$$

4. **矩阵乘法 (Matrix Multiplication)**

   矩阵$\mathbf{A}$与矩阵$\mathbf{B}$的乘积定义为：
   The product of matrix $\mathbf{A}$ and matrix $\mathbf{B}$ is defined as:

   $$

   \mathbf{C} = \mathbf{A} \mathbf{B}, \quad \text{其中} \ \mathbf{C} = \begin{pmatrix}

   c_{11} & c_{12} & \cdots & c_{1p} \\

   c_{21} & c_{22} & \cdots & c_{2p} \\

   \vdots & \vdots & \ddots & \vdots \\

   c_{m1} & c_{m2} & \cdots & c_{mp}

   \end{pmatrix}

$$

   其中 $c_{ij}$ 为第 $i$ 行与第 $j$ 列的元素的乘积和：
   where $c_{ij}$ is the sum of the products of the elements from the $i$-th row and the $j$-th column:

   $$

   c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}

$$

## 矩阵的性质 (Properties of Matrices)

1. **交换律 (Commutative Property)**: 矩阵加法满足交换律，即$\mathbf{A} + \mathbf{B} = \mathbf{B} + \mathbf{A}$。
   Matrix addition is commutative, i.e., $\mathbf{A} + \mathbf{B} = \mathbf{B} + \mathbf{A}$.

2. **结合律 (Associative Property)**: 矩阵加法和数乘满足结合律，即$(\mathbf{A} + \mathbf{B}) + \mathbf{C} = \mathbf{A} + (\mathbf{B} + \mathbf{C})$和$c(\mathbf{A} \mathbf{B}) = (c\mathbf{A}) \mathbf{B}$。
   Matrix addition and scalar multiplication are associative, i.e., $(\mathbf{A} + \mathbf{B}) + \mathbf{C} = \mathbf{A} + (\mathbf{B} + \mathbf{C})$ and $c(\mathbf{A} \mathbf{B}) = (c\mathbf{A}) \mathbf{B}$.

3. **分配律 (Distributive Property)**: 矩阵乘法对矩阵加法满足分配律，即$\mathbf{A}(\mathbf{B} + \mathbf{C}) = \mathbf{A}\mathbf{B} + \mathbf{A}\mathbf{C}$和$(\mathbf{A} + \mathbf{B})\mathbf{C} = \mathbf{A}\mathbf{C} + \mathbf{B}\mathbf{C}$。
   Matrix multiplication is distributive over matrix addition, i.e., $\mathbf{A}(\mathbf{B} + \mathbf{C}) = \mathbf{A}\mathbf{B} + \mathbf{A}\mathbf{C}$ and $(\mathbf{A} + \mathbf{B})\mathbf{C} = \mathbf{A}\mathbf{C} + \mathbf{B}\mathbf{C}$.

## 逆矩阵 (Inverse Matrix)

一个方阵$\mathbf{A}$的逆矩阵$\mathbf{A}^{-1}$满足以下条件：
The inverse of a square matrix $\mathbf{A}$, denoted as $\mathbf{A}^{-1}$, satisfies:

$$

\mathbf{A} \mathbf{A}^{-1} = \mathbf{A}^{-1} \mathbf{A} = \mathbf{I}

$$

- 只有当$\mathbf{A}$是非奇异矩阵（即$\det(\mathbf{A}) \neq 0$）时，$\mathbf{A}$才存在逆矩阵。
- The inverse matrix $\mathbf{A}^{-1}$ exists if and only if $\mathbf{A}$ is a non-singular matrix (i.e., $\det(\mathbf{A}) \neq 0$).

## 伪逆矩阵 (Pseudo-Inverse Matrix)

矩阵$\mathbf{A}$的伪逆矩阵$\mathbf{A}^+$是最小二乘解的一种扩展，常用于求解无法求逆的矩阵。
The pseudo-inverse matrix $\mathbf{A}^+$ of a matrix $\mathbf{A}$ is an extension for finding least-squares solutions, often used when $\mathbf{A}$ is not invertible.

- $\mathbf{A}^+$ 是唯一的，满足以下四个条件：
  - $\mathbf{A} \mathbf{A}^+ \mathbf{A} = \mathbf{A}$
  - $\mathbf{A}^+ \mathbf{A} \mathbf{A}^+ = \mathbf{A}^+$
  - $(\mathbf{A} \mathbf{A}^+)^T = \mathbf{A} \mathbf{A}^+$
  - $(\mathbf{A}^+ \mathbf{A})^T = \mathbf{A}^+ \mathbf{A}$
- $\mathbf{A}^+$ is unique and satisfies the following four conditions:
  - $\mathbf{A} \mathbf{A}^+ \mathbf{A} = \mathbf{A}$
  - $\mathbf{A}^+ \mathbf{A} \mathbf{A}^+ = \mathbf{A}^+$
  - $(\mathbf{A} \mathbf{A}^+)^T = \mathbf{A} \mathbf{A}^+$
  - $(\mathbf{A}^+ \mathbf{A})^T = \mathbf{A}^+ \mathbf{A}$

## 矩阵的迹 (Trace of a Matrix)

矩阵$\mathbf{A}$的迹是其对角线元素之和，记作$\mathrm{tr}(\mathbf{A})$：
The trace of a matrix $\mathbf{A}$, denoted as $\mathrm{tr}(\mathbf{A})$, is the sum of its diagonal elements:

$$

\mathrm{tr}(\mathbf{A}) = \sum_{i=1}^{n} a_{ii}

$$

- 迹的性质：
  - $\mathrm{tr}(\mathbf{A} + \mathbf{B}) = \mathrm{tr}(\mathbf{A}) + \mathrm{tr}(\mathbf{B})$
  - $\mathrm{tr}(c\mathbf{A}) = c \cdot \mathrm{tr}(\mathbf{A})$
  - $\mathrm{tr}(\mathbf{A} \mathbf{B}) = \mathrm{tr}(\mathbf{B} \mathbf{A})$
- Properties of the trace:
  - $\mathrm{tr}(\mathbf{A} + \mathbf{B}) = \mathrm{tr}(\mathbf{A}) + \mathrm{tr}(\mathbf{B})$
  - $\mathrm{tr}(c\mathbf{A}) = c \cdot \mathrm{tr}(\mathbf{A})$
  - $\mathrm{tr}(\mathbf{A} \mathbf{B}) = \mathrm{tr}(\mathbf{B} \mathbf{A})$

## 矩阵的秩 (Rank of a Matrix)

矩阵$\mathbf{A}$的秩是其行向量（或列向量）线性无关的最大数目：
The rank of a matrix $\mathbf{A}$ is the maximum number of linearly independent row vectors (or column vectors):

- 秩的性质：
  - $\mathrm{rank}(\mathbf{A}) = \mathrm{rank}(\mathbf{A}^T)$
  - 若$\mathbf{A}$是$m \times n$矩阵，则$\mathrm{rank}(\mathbf{A}) \leq \min(m, n)$
  - $\mathrm{rank}(\mathbf{A} \mathbf{B}) \leq \min(\mathrm{rank}(\mathbf{A}), \mathrm{rank}(\mathbf{B}))$
- Properties of the rank:
  - $\mathrm{rank}(\mathbf{A}) = \mathrm{rank}(\mathbf{A}^T)$
  - If $\mathbf{A}$ is an $m \times n$ matrix, then $\mathrm{rank}(\mathbf{A}) \leq \min(m, n)$
  - $\mathrm{rank}(\mathbf{A} \mathbf{B}) \leq \min(\mathrm{rank}(\mathbf{A}), \mathrm{rank}(\mathbf{B}))$

## 矩阵的行列式 (Determinant of a Matrix)

一个方阵$\mathbf{A}$的行列式，记作$\det(\mathbf{A})$，是一个标量，反映了矩阵是否可逆：
The determinant of a square matrix $\mathbf{A}$, denoted as $\det(\mathbf{A})$, is a scalar that indicates whether the matrix is invertible:

- $\det(\mathbf{A}) = 0$表示矩阵$\mathbf{A}$是奇异矩阵，不可逆。
- $\det(\mathbf{A}) \neq 0$表示矩阵$\mathbf{A}$是非奇异矩阵，可逆。
- $\det(\mathbf{A}) = 0$ indicates that the matrix $\mathbf{A}$ is singular and not invertible.
- $\det(\mathbf{A}) \neq 0$ indicates that the matrix $\mathbf{A}$ is non-singular and invertible.

- 行列式的性质：
  - $\det(\mathbf{A} \mathbf{B}) = \det(\mathbf{A}) \det(\mathbf{B})$
  - $\det(\mathbf{A}^T) = \det(\mathbf{A})$
  - $\det(c\mathbf{A}) = c^n \det(\mathbf{A})$，其中$c$是一个标量，$\mathbf{A}$是$n \times n$矩阵
- Properties of the determinant:
  - $\det(\mathbf{A} \mathbf{B}) = \det(\mathbf{A}) \det(\mathbf{B})$
  - $\det(\mathbf{A}^T) = \det(\mathbf{A})$
  - $\det(c\mathbf{A}) = c^n \det(\mathbf{A})$, where $c$ is a scalar and $\mathbf{A}$ is an $n \times n$ matrix
