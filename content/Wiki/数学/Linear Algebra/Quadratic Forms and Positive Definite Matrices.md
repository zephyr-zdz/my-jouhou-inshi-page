# 二次型与正定矩阵 | Quadratic Forms and Positive Definite Matrices

## 定义 | Definitions

### 二次型 | Quadratic Form

二次型是指形式为 $Q(\mathbf{x}) = \mathbf{x}^\mathrm{T} \mathbf{A} \mathbf{x}$ 的表达式，其中 $\mathbf{x}$ 是 $n$ 维列向量，$\mathbf{A}$ 是 $n \times n$ 的对称矩阵

A quadratic form is an expression of the form $Q(\mathbf{x}) = \mathbf{x}^\mathrm{T} \mathbf{A} \mathbf{x}$, where $\mathbf{x}$ is an $n$-dimensional column vector and $\mathbf{A}$ is an $n \times n$ symmetric matrix

### 正定矩阵 | Positive Definite Matrix

正定矩阵是指对于任何非零向量 $\mathbf{x}$，都有 $\mathbf{x}^\mathrm{T} \mathbf{A} \mathbf{x} > 0$ 的对称矩阵

A positive definite matrix is a symmetric matrix $\mathbf{A}$ such that $\mathbf{x}^\mathrm{T} \mathbf{A} \mathbf{x} > 0$ for any non-zero vector $\mathbf{x}$

## 性质 | Properties

### 二次型的性质 | Properties of Quadratic Forms

1. 对称性: $Q(\mathbf{x}) = Q(-\mathbf{x})$
2. 如果 $\mathbf{A}$ 是正定矩阵，则 $Q(\mathbf{x})$ 为正定二次型
3. $Q(\mathbf{x})$ 可以通过特征值分解写成 $Q(\mathbf{x}) = \sum_{i=1}^n \lambda_i z_i^2$，其中 $\lambda_i$ 是 $\mathbf{A}$ 的特征值，$z_i$ 是线性变换后的变量

4. Symmetry: $Q(\mathbf{x}) = Q(-\mathbf{x})$
5. If $\mathbf{A}$ is a positive definite matrix, then $Q(\mathbf{x})$ is a positive definite quadratic form
6. $Q(\mathbf{x})$ can be expressed using eigenvalue decomposition as $Q(\mathbf{x}) = \sum_{i=1}^n \lambda_i z_i^2$, where $\lambda_i$ are the eigenvalues of $\mathbf{A}$ and $z_i$ are the transformed variables

### 正定矩阵的性质 | Properties of Positive Definite Matrices

1. 所有特征值均为正
2. 所有主子矩阵的行列式均为正
3. $\mathbf{A}$ 可被分解为 $\mathbf{A} = \mathbf{L} \mathbf{L}^\mathrm{T}$，其中 $\mathbf{L}$ 为下三角矩阵

4. All eigenvalues are positive
5. Determinants of all leading principal minors are positive
6. $\mathbf{A}$ can be decomposed as $\mathbf{A} = \mathbf{L} \mathbf{L}^\mathrm{T}$, where $\mathbf{L}$ is a lower triangular matrix

## 计算技巧 | Calculation Techniques

### 二次型化简 | Simplifying Quadratic Forms

通过正交变换 $\mathbf{P}$ 将 $\mathbf{A}$ 对角化，可以将二次型化简为 $Q(\mathbf{y}) = \sum_{i=1}^n \lambda_i y_i^2$

By orthogonal transformation $\mathbf{P}$ that diagonalizes $\mathbf{A}$, the quadratic form can be simplified to $Q(\mathbf{y}) = \sum_{i=1}^n \lambda_i y_i^2$

### 判定正定矩阵的方法 | Methods to Determine Positive Definite Matrices

1. 确认所有特征值是否均为正
2. 使用主子矩阵行列式进行测试
3. 计算 $\mathbf{A}$ 是否可以进行 Cholesky 分解

[[Matrix Decompositions#4. Cholesky Decomposition Cholesky 分解]]

1. Check if all eigenvalues are positive
2. Use leading principal minors to test
3. Determine if $\mathbf{A}$ can be decomposed using Cholesky decomposition

## 坐标变换 | Coordinate Transformations

### 正交变换 | Orthogonal Transformation

正交变换保持二次型的形式不变，即 $Q(\mathbf{y}) = \mathbf{y}^\mathrm{T} (\mathbf{P}^\mathrm{T} \mathbf{A} \mathbf{P}) \mathbf{y}$，其中 $\mathbf{P}$ 是正交矩阵

An orthogonal transformation preserves the form of the quadratic form, i.e., $Q(\mathbf{y}) = \mathbf{y}^\mathrm{T} (\mathbf{P}^\mathrm{T} \mathbf{A} \mathbf{P}) \mathbf{y}$, where $\mathbf{P}$ is an orthogonal matrix

### 仿射变换 | Affine Transformation

仿射变换包括旋转、平移等操作，可以用于化简或标准化二次型

Affine transformations include operations such as rotation and translation, and can be used to simplify or standardize quadratic forms

## 例子 | Examples

### 二次型的例子 | Example of a Quadratic Form

设 $\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$，$\mathbf{A} = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$，则二次型为

$$
Q(\mathbf{x}) = \mathbf{x}^\mathrm{T} \mathbf{A} \mathbf{x} = \begin{pmatrix} x_1 & x_2 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = 2x_1^2 + 2x_1x_2 + 3x_2^2
$$

Let $\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$ and $\mathbf{A} = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$, then the quadratic form is

$$
Q(\mathbf{x}) = \mathbf{x}^\mathrm{T} \mathbf{A} \mathbf{x} = \begin{pmatrix} x_1 & x_2 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = 2x_1^2 + 2x_1x_2 + 3x_2^2
$$

### 正定矩阵的例子 | Example of a Positive Definite Matrix

考虑矩阵 $\mathbf{A} = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$，计算特征值

$$
\det(\mathbf{A} - \lambda \mathbf{I}) = \det \begin{pmatrix} 2 - \lambda & -1 \\ -1 & 2 - \lambda \end{pmatrix} = (2 - \lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = 0
$$

特征值为 $\lambda_1 = 1, \lambda_2 = 3$，均为正值，因此 $\mathbf{A}$ 为正定矩阵

Consider the matrix $\mathbf{A} = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$ and compute the eigenvalues

$$
\det(\mathbf{A} - \lambda \mathbf{I}) = \det \begin{pmatrix} 2 - \lambda & -1 \\ -1 & 2 - \lambda \end{pmatrix} = (2 - \lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = 0
$$

The eigenvalues are $\lambda_1 = 1, \lambda_2 = 3$, both positive, hence $\mathbf{A}$ is a positive definite matrix

## 坐标变换中的应用 | Applications in Coordinate Transformations

### 对角化二次型 | Diagonalizing Quadratic Forms

为了将二次型 $Q(\mathbf{x}) = \mathbf{x}^\mathrm{T} \mathbf{A} \mathbf{x}$ 对角化，我们寻找正交矩阵 $\mathbf{P}$ 使得 $\mathbf{P}^\mathrm{T} \mathbf{A} \mathbf{P}$ 为对角矩阵 $\mathbf{D}$，于是 $Q(\mathbf{y}) = \mathbf{y}^\mathrm{T} \mathbf{D} \mathbf{y}$

To diagonalize the quadratic form $Q(\mathbf{x}) = \mathbf{x}^\mathrm{T} \mathbf{A} \mathbf{x}$, we find an orthogonal matrix $\mathbf{P}$ such that $\mathbf{P}^\mathrm{T} \mathbf{A} \mathbf{P}$ is a diagonal matrix $\mathbf{D}$, thus $Q(\mathbf{y}) = \mathbf{y}^\mathrm{T} \mathbf{D} \mathbf{y}$

### 坐标变换举例 | Example of Coordinate Transformation

假设 $\mathbf{A} = \begin{pmatrix} 4 & 2 \\ 2 & 3 \end{pmatrix}$，则特征值为 $\lambda_1 = 5, \lambda_2 = 2$，对应的特征向量为 $\mathbf{v}_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$，$\mathbf{v}_2 = \begin{pmatrix} -1 \\ 2 \end{pmatrix}$。构造正交矩阵 $\mathbf{P}$ 并进行对角化

$$
\mathbf{P} = \begin{pmatrix} \frac{2}{\sqrt{5}} & \frac{-1}{\sqrt{5}} \\ \frac{1}{\sqrt{5}} & \frac{2}{\sqrt{5}} \end{pmatrix}, \quad \mathbf{P}^\mathrm{T} \mathbf{A} \mathbf{P} = \begin{pmatrix} 5 & 0 \\ 0 & 2 \end{pmatrix}
$$

新的二次型为 $Q(\mathbf{y}) = 5y_1^2 + 2y_2^2$

Suppose $\mathbf{A} = \begin{pmatrix} 4 & 2 \\ 2 & 3 \end{pmatrix}$, the eigenvalues are $\lambda_1 = 5, \lambda_2 = 2$, with corresponding eigenvectors $\mathbf{v}_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$ and $\mathbf{v}_2 = \begin{pmatrix} -1 \\ 2 \end{pmatrix}$. Construct the orthogonal matrix $\mathbf{P}$ and diagonalize

$$
\mathbf{P} = \begin{pmatrix} \frac{2}{\sqrt{5}} & \frac{-1}{\sqrt{5}} \\ \frac{1}{\sqrt{5}} & \frac{2}{\sqrt{5}} \end{pmatrix}, \quad \mathbf{P}^\mathrm{T} \mathbf{A} \mathbf{P} = \begin{pmatrix} 5 & 0 \\ 0 & 2 \end{pmatrix}
$$

The new quadratic form is $Q(\mathbf{y}) = 5y_1^2 + 2y_2^2$
