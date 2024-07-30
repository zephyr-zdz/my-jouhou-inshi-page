# Matrix Decompositions 矩阵分解

## Why Decompose a Matrix? 为什么要对矩阵做分解？

Matrix decomposition is essential in various mathematical and computational applications. It simplifies matrix operations, aids in solving linear systems, eigenvalue problems, and facilitates numerical stability and efficiency. By decomposing a matrix, complex problems become more manageable, enabling efficient computations and deeper insights into the linear transformations represented by the matrix.

矩阵分解在各种数学和计算应用中至关重要。它简化了矩阵运算，有助于解决线性方程组、特征值问题，并提高数值稳定性和效率。通过对矩阵进行分解，复杂问题变得更加易于处理，从而实现高效计算并深入理解矩阵所代表的线性变换。

## Types of Matrix Decompositions 矩阵分解的种类

### 1. LU Decomposition LU 分解

LU decomposition factorizes a matrix $\mathbf{A}$ into a product of a lower triangular matrix $\mathbf{L}$ and an upper triangular matrix $\mathbf{U}$.

$$
\mathbf{A} = \mathbf{L} \mathbf{U}
$$

- **Usage:** Solving linear systems $\mathbf{A}\mathbf{x} = \mathbf{b}$.
- **Requirements:** $\mathbf{A}$ must be a square matrix.
- **Procedure:**
  1. **Gaussian Elimination 高斯消元法:**
     - Convert $\mathbf{A}$ to an upper triangular matrix $\mathbf{U}$ using row operations.
     - Keep track of the multipliers used to eliminate elements below the pivot, forming $\mathbf{L}$.
  2. **Forming Matrices 形成矩阵:**
     - $\mathbf{L}$: Lower triangular matrix with ones on the diagonal and the multipliers below the diagonal.
     - $\mathbf{U}$: Upper triangular matrix obtained after Gaussian elimination.

LU 分解将矩阵 $\mathbf{A}$ 分解为下三角矩阵 $\mathbf{L}$ 和上三角矩阵 $\mathbf{U}$ 的乘积。

$$
\mathbf{A} = \mathbf{L} \mathbf{U}
$$

- **用途:** 解决线性方程组 $\mathbf{A}\mathbf{x} = \mathbf{b}$。
- **要求:** $\mathbf{A}$ 必须是方阵。
- **过程:**
  1. **高斯消元法:**
     - 使用行运算将 $\mathbf{A}$ 转换为上三角矩阵 $\mathbf{U}$。
     - 记录用来消去主元下方元素的乘数，形成 $\mathbf{L}$。
  2. **形成矩阵:**
     - $\mathbf{L}$: 对角线为 1 且对角线下方为消去乘数的下三角矩阵。
     - $\mathbf{U}$: 经过高斯消元法得到的上三角矩阵。

### 2. QR Decomposition QR 分解

QR decomposition expresses a matrix $\mathbf{A}$ as a product of an orthogonal matrix $\mathbf{Q}$ and an upper triangular matrix $\mathbf{R}$.

QR 分解将矩阵 $\mathbf{A}$ 表示为正交矩阵 $\mathbf{Q}$ 和上三角矩阵 $\mathbf{R}$ 的乘积。

$$
\mathbf{A} = \mathbf{Q} \mathbf{R}
$$

#### Usage 用途

- Solving linear least squares problems.
- 解决线性最小二乘问题。

#### Requirements 要求

- $\mathbf{A}$ can be any $m \times n$ matrix.
- $\mathbf{A}$ 可以是任意 $m \times n$ 矩阵。

#### Procedure 过程

1. **Gram-Schmidt Orthogonalization 格拉姆-施密特正交化**
   - **Step 1:** Start with the columns of $\mathbf{A}$, denoted as $\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_n$.
     从 $\mathbf{A}$ 的列 $\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_n$ 开始。

   - **Step 2:** Form orthogonal vectors $\mathbf{u}_i$ using:
     使用公式形成正交向量 $\mathbf{u}_i$：

$$
     \mathbf{u}_i = \mathbf{a}_i - \sum_{j=1}^{i-1} \frac{\mathbf{a}_i^\top \mathbf{u}_j}{\mathbf{u}_j^\top \mathbf{u}_j} \mathbf{u}_j
$$

   - **Step 3:** Normalize $\mathbf{u}_i$ to get $\mathbf{q}_i$:
     将 $\mathbf{u}_i$ 归一化得到 $\mathbf{q}_i$：

$$
\mathbf{q}_i = \frac{\mathbf{u}_i}{\|\mathbf{u}_i\|}
$$

   - **Step 4:** Construct $\mathbf{Q}$ with $\mathbf{q}_i$ as columns and $\mathbf{R}$ using the inner products $\mathbf{R}_{ij} = \mathbf{q}_i^\top \mathbf{a}_j$.
     用 $\mathbf{q}_i$ 构造 $\mathbf{Q}$，并使用内积 $\mathbf{R}_{ij} = \mathbf{q}_i^\top \mathbf{a}_j$ 构造 $\mathbf{R}$。

1. **Householder Transformations Householder 变换**
   - **Step 1:** Use reflections to zero out below-diagonal entries.
     使用反射将对角线下方元素归零。

   - **Step 2:** Form $\mathbf{Q}$ as a product of Householder matrices.
     将 $\mathbf{Q}$ 表示为 Householder 矩阵的乘积。

### 3. Singular Value Decomposition (SVD) 奇异值分解 (SVD)

SVD decomposes a matrix $\mathbf{A}$ into three matrices: an orthogonal matrix $\mathbf{U}$, a diagonal matrix $\mathbf{\Sigma}$, and the transpose of an orthogonal matrix $\mathbf{V}$.

$$
\mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^\top
$$

- **Usage:** Principal Component Analysis (PCA), solving linear systems, and pseudoinverse computation.
- **Requirements:** $\mathbf{A}$ can be any $m \times n$ matrix.
- **Procedure:**
  1. **Compute Eigenvalues and Eigenvectors 计算特征值和特征向量:**
     - Compute $\mathbf{A} \mathbf{A}^\top$ and $\mathbf{A}^\top \mathbf{A}$.
     - Find the eigenvalues and eigenvectors of these matrices.
  2. **Forming Matrices 形成矩阵:**
     - $\mathbf{U}$: Columns are eigenvectors of $\mathbf{A} \mathbf{A}^\top$.
     - $\mathbf{\Sigma}$: Diagonal matrix with singular values (square roots of eigenvalues).
     - $\mathbf{V}$: Columns are eigenvectors of $\mathbf{A}^\top \mathbf{A}$.

奇异值分解将矩阵 $\mathbf{A}$ 分解为三个矩阵：正交矩阵 $\mathbf{U}$、对角矩阵 $\mathbf{\Sigma}$ 和正交矩阵 $\mathbf{V}$ 的转置。

$$
\mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^\top
$$

- **用途:** 主成分分析 (PCA)，解决线性方程组和计算广义逆矩阵。
- **要求:** $\mathbf{A}$ 可以是任意 $m \times n$ 矩阵。
- **过程:**
  1. **计算特征值和特征向量:**
     - 计算 $\mathbf{A} \mathbf{A}^\top$ 和 $\mathbf{A}^\top \mathbf{A}$。
     - 找到这些矩阵的特征值和特征向量。
  2. **形成矩阵:**
     - $\mathbf{U}$：列向量是 $\mathbf{A} \mathbf{A}^\top$ 的特征向量。
     - $\mathbf{\Sigma}$：对角矩阵，其对角线元素为奇异值（特征值的平方根）。
     - $\mathbf{V}$：列向量是 $\mathbf{A}^\top \mathbf{A}$ 的特征向量。

### 4. Cholesky Decomposition Cholesky 分解

Cholesky decomposition factorizes a positive definite matrix $\mathbf{A}$ into the product of a lower triangular matrix $\mathbf{L}$ and its transpose.

$$
\mathbf{A} = \mathbf{L} \mathbf{L}^\top
$$

- **Usage:** Solving linear systems, especially in optimization problems.
- **Requirements:** $\mathbf{A}$ must be symmetric and positive definite.
- **Procedure:**
  1. **Forming $\mathbf{L}$ 形成 $\mathbf{L}$:**
     - For each diagonal element $\mathbf{A}_{ii}$, compute:

$$
       \mathbf{L}_{ii} = \sqrt{\mathbf{A}_{ii} - \sum_{k=1}^{i-1} \mathbf{L}_{ik}^2}
$$

  - For each off-diagonal element $\mathbf{A}_{ij}$, compute:

$$
       \mathbf{L}_{ij} = \frac{1}{\mathbf{L}_{jj}} \left(\mathbf{A}_{ij} - \sum_{k=1}^{j-1} \mathbf{L}_{ik} \mathbf{L}_{jk}\right) \quad \text{for} \; i > j
       
$$

Cholesky 分解将正定矩阵 $\mathbf{A}$ 分解为下三角矩阵 $\mathbf{L}$ 和其转置的乘积。

$$
\mathbf{A} = \mathbf{L} \mathbf{L}^\top
$$

- **用途:** 解决线性方程组，特别是在优化问题中。
- **要求:** $\mathbf{A}$ 必须是对称且正定的。
- **过程:**
  1. **形成 $\mathbf{L}$:**
     - 对于每个对角元素 $\mathbf{A}_{ii}$，计算：

       $$
       \mathbf{L}_{ii} = \sqrt{\mathbf{A}_{ii} - \sum_{k=1}^{i-1} \mathbf{L}_{ik}^2}


$$
  - 对于每个非对角元素 $\mathbf{A}_{ij}$，计算：
$$

       \mathbf{L}_{ij} = \frac{1}{\mathbf{L}_{jj}} \left(\mathbf{A}_{ij} - \sum_{k=1}^{j-1} \mathbf{L}_{ik} \mathbf{L}_{jk}\right) \quad \text{当} \; i > j
       

$$
### 5. Eigenvalue Decomposition 特征值分解

Eigenvalue decomposition expresses a matrix $\mathbf{A}$ in terms of its eigenvalues and eigenvectors.
$$

\mathbf{A} = \mathbf{V} \mathbf{\Lambda} \mathbf{V}^{-1}

$$
- **Usage:** Analyzing linear transformations, stability analysis.
- **Requirements:** $\mathbf{A}$ must be a square matrix with linearly independent eigenvectors.
- **Procedure:**
  1. **Find Eigenvalues and Eigenvectors 找到特征值和特征向量:**
     - Solve the characteristic equation $\det(\mathbf{A} - \lambda \mathbf{I}) = 0$ to find eigenvalues $\lambda_i$.
     - Solve $(\mathbf{A} - \lambda_i \mathbf{I}) \mathbf{v}_i = 0$ to find eigenvectors $\mathbf{v}_i$.
  2. **Forming Matrices 形成矩阵:**
     - $\mathbf{\Lambda}$: Diagonal matrix with eigenvalues $\lambda_i$.
     - $\mathbf{V}$: Matrix with eigenvectors $\mathbf{v}_i$ as columns.

特征值分解将矩阵 $\mathbf{A}$ 表示为其特征值和特征向量的形式。
$$

\mathbf{A} = \mathbf{V} \mathbf{\Lambda} \mathbf{V}^{-1}

$$

- **用途:** 分析线性变换、稳定性分析。
- **要求:** $\mathbf{A}$ 必须是具有线性无关特征向量的方阵。
- **过程:**
  1. **找到特征值和特征向量:**
     - 通过求解特征方程 $\det(\mathbf{A} - \lambda \mathbf{I}) = 0$ 找到特征值 $\lambda_i$。
     - 通过求解 $(\mathbf{A} - \lambda_i \mathbf{I}) \mathbf{v}_i = 0$ 找到特征向量 $\mathbf{v}_i$。
  2. **形成矩阵:**
     - $\mathbf{\Lambda}$: 对角矩阵，其对角线元素为特征值 $\lambda_i$。
     - $\mathbf{V}$: 列向量是特征向量 $\mathbf{v}_i$ 的矩阵。
