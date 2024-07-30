# 复矩阵 Complex Matrices

## 定义 Definition

复矩阵是元素为复数的矩阵。复矩阵可以表示为 $\mathbf{A} + i\mathbf{B}$，其中 $\mathbf{A}$ 和 $\mathbf{B}$ 是实矩阵，$i$ 是虚数单位，满足 $i^2 = -1$
A complex matrix is a matrix whose elements are complex numbers. A complex matrix can be represented as $\mathbf{A} + i\mathbf{B}$, where $\mathbf{A}$ and $\mathbf{B}$ are real matrices, and $i$ is the imaginary unit satisfying $i^2 = -1$

## 复矩阵的加法与乘法 Addition and Multiplication of Complex Matrices

复矩阵的加法和乘法类似于实矩阵，但元素之间的运算需要遵循复数的运算法则
Addition and multiplication of complex matrices are similar to those of real matrices, but the operations between elements must follow the rules of complex arithmetic

### 加法 Addition

给定两个复矩阵 $\mathbf{A} = \mathbf{A_1} + i\mathbf{A_2}$ 和 $\mathbf{B} = \mathbf{B_1} + i\mathbf{B_2}$，其和为：
Given two complex matrices $\mathbf{A} = \mathbf{A_1} + i\mathbf{A_2}$ and $\mathbf{B} = \mathbf{B_1} + i\mathbf{B_2}$, their sum is:

$$
\mathbf{A} + \mathbf{B} = (\mathbf{A_1} + \mathbf{B_1}) + i(\mathbf{A_2} + \mathbf{B_2})
$$

### 乘法 Multiplication

给定两个复矩阵 $\mathbf{A} = \mathbf{A_1} + i\mathbf{A_2}$ 和 $\mathbf{B} = \mathbf{B_1} + i\mathbf{B_2}$，其积为：
Given two complex matrices $\mathbf{A} = \mathbf{A_1} + i\mathbf{A_2}$ and $\mathbf{B} = \mathbf{B_1} + i\mathbf{B_2}$, their product is:

$$
\mathbf{A} \mathbf{B} = (\mathbf{A_1} + i\mathbf{A_2})(\mathbf{B_1} + i\mathbf{B_2}) = (\mathbf{A_1}\mathbf{B_1} - \mathbf{A_2}\mathbf{B_2}) + i(\mathbf{A_1}\mathbf{B_2} + \mathbf{A_2}\mathbf{B_1})
$$

## 复共轭 Hermitian Conjugate

复矩阵 $\mathbf{A}$ 的复共轭转置（也称为厄米共轭）记作 $\mathbf{A}^*$，定义为先取复共轭再转置
The Hermitian conjugate (also known as the conjugate transpose) of a complex matrix $\mathbf{A}$ is denoted by $\mathbf{A}^*$ and is defined as taking the complex conjugate of the matrix followed by the transpose

$$
\mathbf{A}^* = \overline{\mathbf{A}}^T
$$

其中，$\overline{\mathbf{A}}$ 表示 $\mathbf{A}$ 的复共轭，$^T$ 表示转置
where $\overline{\mathbf{A}}$ denotes the complex conjugate of $\mathbf{A}$, and $^T$ denotes the transpose

## 厄米矩阵 Hermitian Matrix

厄米矩阵是满足 $\mathbf{A} = \mathbf{A}^*$ 的复矩阵
A Hermitian matrix is a complex matrix that satisfies $\mathbf{A} = \mathbf{A}^*$

### 性质 Properties

- 对角线元素都是实数
  The diagonal elements are real numbers

- 非对角线元素是共轭对称的，即 $a_{ij} = \overline{a_{ji}}$
  The off-diagonal elements are conjugate symmetric, i.e., $a_{ij} = \overline{a_{ji}}$

## 酉矩阵 Unitary Matrix

酉矩阵是满足 $\mathbf{U} \mathbf{U}^* = \mathbf{U}^* \mathbf{U} = \mathbf{I}$ 的复矩阵，其中 $\mathbf{I}$ 是单位矩阵
A unitary matrix is a complex matrix that satisfies $\mathbf{U} \mathbf{U}^* = \mathbf{U}^* \mathbf{U} = \mathbf{I}$, where $\mathbf{I}$ is the identity matrix

### 性质 Properties

- 酉矩阵的行（列）向量构成标准正交基
  The rows (columns) of a unitary matrix form an orthonormal basis

- 酉矩阵的模保持性：$\|\mathbf{U} \mathbf{x}\| = \|\mathbf{x}\|$
  Unitary matrices preserve norms: $\|\mathbf{U} \mathbf{x}\| = \|\mathbf{x}\|$

## 复矩阵的行列式 Determinant of a Complex Matrix

复矩阵 $\mathbf{A}$ 的行列式定义与实矩阵相同，但计算中需要使用复数的运算
The determinant of a complex matrix $\mathbf{A}$ is defined similarly to that of a real matrix, but the computation involves complex arithmetic

### 性质 Properties

- $\mathrm{det}(\mathbf{A}^*) = \overline{\mathrm{det}(\mathbf{A})}$
  $\mathrm{det}(\mathbf{A}^*) = \overline{\mathrm{det}(\mathbf{A})}$

- 对于酉矩阵 $\mathbf{U}$，$\mathrm{det}(\mathbf{U})$ 的模为 1
  For a unitary matrix $\mathbf{U}$, $|\mathrm{det}(\mathbf{U})| = 1$

## 复矩阵的特征值和特征向量 Eigenvalues and Eigenvectors of Complex Matrices

复矩阵 $\mathbf{A}$ 的特征值和特征向量满足 $\mathbf{A} \mathbf{v} = \lambda \mathbf{v}$，其中 $\lambda$ 是特征值，$\mathbf{v}$ 是对应的特征向量
The eigenvalues and eigenvectors of a complex matrix $\mathbf{A}$ satisfy $\mathbf{A} \mathbf{v} = \lambda \mathbf{v}$, where $\lambda$ is an eigenvalue and $\mathbf{v}$ is the corresponding eigenvector

### 性质 Properties

- 复矩阵的特征值可以是复数
  The eigenvalues of a complex matrix can be complex numbers

- 厄米矩阵的特征值是实数
  The eigenvalues of a Hermitian matrix are real

- 酉矩阵的特征值在单位圆上
  The eigenvalues of a unitary matrix lie on the unit circle

### 特殊解法 Special Methods for Finding Eigenvalues of Complex Matrices

- 使用 QR 算法可以高效地计算复矩阵的特征值
  The QR algorithm can efficiently compute the eigenvalues of complex matrices

- 对于厄米矩阵，可以利用其实对称矩阵的性质简化计算
  For Hermitian matrices, their properties as real symmetric matrices can simplify the computation

- 对于酉矩阵，可以使用 Schur 分解将其转化为上三角矩阵，从而直接读取特征值
  For unitary matrices, the Schur decomposition can transform them into upper triangular matrices, from which the eigenvalues can be directly read

## 复矩阵的分解 Decomposition of Complex Matrices

### 极分解 Polar Decomposition

任意复矩阵 $\mathbf{A}$ 都可以分解为一个酉矩阵 $\mathbf{U}$ 和一个正定的厄米矩阵 $\mathbf{P}$ 的乘积，即 $\mathbf{A} = \mathbf{U} \mathbf{P}$
Any complex matrix $\mathbf{A}$ can be decomposed into the product of a unitary matrix $\mathbf{U}$ and a positive definite Hermitian matrix $\mathbf{P}$, i.e., $\mathbf{A} = \mathbf{U} \mathbf{P}$

### 奇异值分解 Singular Value Decomposition (SVD)

任意复矩阵 $\mathbf{A}$ 都可以分解为 $\mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^*$，其中 $\mathbf{U}$ 和 $\mathbf{V}$ 是酉矩阵，$\mathbf{\Sigma}$ 是对角矩阵，对角元素为 $\mathbf{A}$ 的奇异值
Any complex matrix $\mathbf{A}$ can be decomposed as $\mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^*$, where $\mathbf{U}$ and $\mathbf{V}$ are unitary matrices, and $\mathbf{\Sigma}$ is a diagonal matrix with the singular values of $\mathbf{A}$ on its diagonal

### 谱分解

 Spectral Decomposition

对于厄米矩阵 $\mathbf{A}$，可以分解为 $\mathbf{A} = \mathbf{Q} \mathbf{\Lambda} \mathbf{Q}^*$，其中 $\mathbf{Q}$ 是酉矩阵，$\mathbf{\Lambda}$ 是对角矩阵，对角元素为 $\mathbf{A}$ 的特征值
For a Hermitian matrix $\mathbf{A}$, it can be decomposed as $\mathbf{A} = \mathbf{Q} \mathbf{\Lambda} \mathbf{Q}^*$, where $\mathbf{Q}$ is a unitary matrix, and $\mathbf{\Lambda}$ is a diagonal matrix with the eigenvalues of $\mathbf{A}$ on its diagonal

## 厄米矩阵和伴随矩阵的异同 Differences and Similarities between Hermitian and Adjoint Matrices

### 厄米矩阵 Hermitian Matrix

- 厄米矩阵是自身的共轭转置，即 $\mathbf{A} = \mathbf{A}^*$
  A Hermitian matrix is equal to its own conjugate transpose, i.e., $\mathbf{A} = \mathbf{A}^*$

- 厄米矩阵的特征值是实数
  The eigenvalues of a Hermitian matrix are real

- 厄米矩阵的对角元素都是实数，非对角元素是共轭对称的
  The diagonal elements of a Hermitian matrix are real, and the off-diagonal elements are conjugate symmetric

### 伴随矩阵 Adjoint Matrix

- 伴随矩阵是原矩阵的复共轭转置，即 $\mathbf{A}^*$
  The adjoint matrix is the conjugate transpose of the original matrix, i.e., $\mathbf{A}^*$

- 伴随矩阵不一定是厄米矩阵，但对于厄米矩阵，伴随矩阵与原矩阵相同
  An adjoint matrix is not necessarily a Hermitian matrix, but for a Hermitian matrix, the adjoint matrix is the same as the original matrix

- 实矩阵的伴随矩阵就是它的转置矩阵
  For a real matrix, the adjoint matrix is simply its transpose matrix

### 实矩阵与复矩阵之间的差异 Differences between Real and Complex Matrices

- 实矩阵的元素都是实数，而复矩阵的元素可以是复数
  The elements of a real matrix are all real numbers, whereas the elements of a complex matrix can be complex numbers

- 实矩阵的特征值可以是实数或复数，但复矩阵的特征值通常是复数
  The eigenvalues of a real matrix can be real or complex, but the eigenvalues of a complex matrix are typically complex

- 厄米矩阵是复矩阵的一种特殊形式，其特征值是实数
  A Hermitian matrix is a special form of a complex matrix whose eigenvalues are real
