# Eigenvalue & Eigenvector Cheatsheet

## 1. 定义 (Definitions)

### 特征值 (Eigenvalue)

**特征值** 是方阵 $A$ 的一个标量 $\lambda$，使得存在非零向量 $\mathbf{v}$，满足 $A\mathbf{v} = \lambda\mathbf{v}$。

**Eigenvalue** is a scalar $\lambda$ of a square matrix $A$, such that there exists a non-zero vector $\mathbf{v}$ satisfying $A\mathbf{v} = \lambda\mathbf{v}$.

### 特征向量 (Eigenvector)

**特征向量** 是方阵 $A$ 的一个非零向量 $\mathbf{v}$，使得存在标量 $\lambda$，满足 $A\mathbf{v} = \lambda\mathbf{v}$。

**Eigenvector** is a non-zero vector $\mathbf{v}$ of a square matrix $A$, such that there exists a scalar $\lambda$ satisfying $A\mathbf{v} = \lambda\mathbf{v}$.

## 2. 性质 (Properties)

1. **特征值的数量**:
   方阵 $A$ 的特征值的数量等于矩阵的阶数 $n$。

   The number of eigenvalues of a square matrix $A$ is equal to its order $n$.

2. **特征向量的线性无关性**:
   对于不同的特征值对应的特征向量是线性无关的。

   Eigenvectors corresponding to different eigenvalues are linearly independent.

3. **特征值的迹和行列式**:
   矩阵 $A$ 的特征值之和等于矩阵的迹，特征值的乘积等于矩阵的行列式。

   The sum of the eigenvalues of a matrix $A$ equals the trace of the matrix, and the product of the eigenvalues equals the determinant of the matrix.

4. **幂次方性质**:
   如果 $\lambda$ 是矩阵 $A$ 的特征值，那么 $\lambda^k$ 是 $A^k$ 的特征值。

   If $\lambda$ is an eigenvalue of matrix $A$, then $\lambda^k$ is an eigenvalue of $A^k$.

5. **特征向量的旋转不变性**:
   如果 $\mathbf{v}$ 是 $A$ 的特征向量，那么对任意标量 $c$， $c\mathbf{v}$ 也是 $A$ 的特征向量。

   If $\mathbf{v}$ is an eigenvector of $A$, then for any scalar $c$, $c\mathbf{v}$ is also an eigenvector of $A$.

## 3. 计算方法 (Computation Methods)

### 计算特征值 (Finding Eigenvalues)

1. **特征多项式 (Characteristic Polynomial)**:
   计算 $\text{det}(A - \lambda I) = 0$，其中 $I$ 是单位矩阵。解该多项式方程得到特征值 $\lambda$。

   Calculate $\text{det}(A - \lambda I) = 0$, where $I$ is the identity matrix. Solve the polynomial equation to find the eigenvalues $\lambda$.

### 计算特征向量 (Finding Eigenvectors)

1. **求解线性方程组**:
   对于每个特征值 $\lambda$，求解 $(A - \lambda I)\mathbf{v} = 0$ 的非零解 $\mathbf{v}$。

   For each eigenvalue $\lambda$, solve $(A - \lambda I)\mathbf{v} = 0$ for non-zero vector $\mathbf{v}$.

## 4. 例子 (Examples)

### 例 1：二维矩阵 (2x2 Matrix)

给定矩阵 $A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$:

1. 计算特征多项式:

   $$
   \text{det}(A - \lambda I) = \begin{vmatrix} 4 - \lambda & 1 \\ 2 & 3 - \lambda \end{vmatrix} = (4 - \lambda)(3 - \lambda) - 2 = \lambda^2 - 7\lambda + 10

$$

2. 解方程 $\lambda^2 - 7\lambda + 10 = 0$:
   $$

   \lambda = 2, \ 5

$$
3. 对于 $\lambda = 2$:
   $$

   (A - 2I)\mathbf{v} = 0 \Rightarrow \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = 0 \Rightarrow v_1 = -v_2

$$
   特征向量为 $\mathbf{v} = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$。

4. 对于 $\lambda = 5$:
   $$

   (A - 5I)\mathbf{v} = 0 \Rightarrow \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = 0 \Rightarrow v_1 = v_2

$$
   特征向量为 $\mathbf{v} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$。

## 5. 常见应用 (Common Applications)

1. **系统稳定性分析 (System Stability Analysis)**:
   通过分析系统矩阵的特征值来判断系统的稳定性。

   Analyze the stability of a system by examining the eigenvalues of its system matrix.

2. **图像处理 (Image Processing)**:
   主成分分析（PCA）用于图像降维和特征提取。

   Principal Component Analysis (PCA) is used for image dimensionality reduction and feature extraction.

3. **量子力学 (Quantum Mechanics)**:
   特征值和特征向量在薛定谔方程中用于描述量子态。

   Eigenvalues and eigenvectors are used in the Schrödinger equation to describe quantum states.
