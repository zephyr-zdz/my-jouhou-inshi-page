# 矩阵理论 Matrix Theory

## Cayley-Hamilton 定理 Cayley-Hamilton Theorem

### 定义 Definition

**Cayley-Hamilton 定理**: 一个 $n \times n$ 的矩阵 $A$ 满足其特征多项式 $p(\lambda)$，即 $A$ 代入其特征多项式得到的矩阵多项式等于零矩阵
Cayley-Hamilton Theorem: An $n \times n$ matrix $A$ satisfies its characteristic polynomial $p(\lambda)$, meaning that the matrix polynomial obtained by substituting $A$ into its characteristic polynomial equals the zero matrix

用数学语言表达:

Expressed mathematically:

$$
p(\lambda) = \det(\lambda I - A)
$$

$$
p(A) = 0
$$

### 特征多项式 Characteristic Polynomial

一个矩阵 $A$ 的特征多项式定义为:

The characteristic polynomial of a matrix $A$ is defined as:

$$
p(\lambda) = \det(\lambda I - A)
$$

其中 $\det$ 表示行列式，$I$ 是单位矩阵，$\lambda$ 是一个标量

where $\det$ denotes the determinant, $I$ is the identity matrix, and $\lambda$ is a scalar

### 证明 Proof

Cayley-Hamilton 定理的证明通常包括以下步骤:

The proof of the Cayley-Hamilton Theorem typically includes the following steps:

1. 计算 $A$ 的特征多项式 $p(\lambda)$
   Calculate the characteristic polynomial $p(\lambda)$ of $A$
2. 通过代入 $\lambda = A$ 验证 $p(A) = 0$
   Verify that $p(A) = 0$ by substituting $\lambda = A$

### 性质 Properties

1. **适用于任何方阵**: Cayley-Hamilton 定理对任何 $n \times n$ 矩阵都适用，无论是实矩阵还是复矩阵
   **Applicable to any square matrix**: The Cayley-Hamilton Theorem applies to any $n \times n$ matrix, whether real or complex
2. **特征值和特征向量的关系**: Cayley-Hamilton 定理表明矩阵的特征值是其特征多项式的根
   **Relationship between eigenvalues and eigenvectors**: The Cayley-Hamilton Theorem indicates that the eigenvalues of a matrix are the roots of its characteristic polynomial

### 应用 Applications

1. **求幂矩阵**: 利用 Cayley-Hamilton 定理可以简化高次幂矩阵的计算
   **Computing matrix powers**: The Cayley-Hamilton Theorem can simplify the computation of high powers of a matrix
2. **求矩阵函数**: 如矩阵的指数函数、对数函数等
   **Finding matrix functions**: Such as the exponential function and logarithm function of a matrix
3. **系统理论**: 在控制系统的稳定性分析中
   **Systems theory**: In the stability analysis of control systems

### 计算技巧 Calculation Techniques

- **利用幂简化**: 通过 Cayley-Hamilton 定理，可以将高次幂矩阵 $A^k$ 表示为较低次幂矩阵的线性组合，从而简化计算
  **Simplifying powers**: By using the Cayley-Hamilton Theorem, a high power of a matrix $A^k$ can be expressed as a linear combination of lower powers of the matrix, thus simplifying the calculation
- **求解线性微分方程组**: 在求解常系数线性微分方程组时，可以利用 Cayley-Hamilton 定理将问题转化为代数问题
  **Solving linear differential equations**: When solving constant coefficient linear differential equations, the Cayley-Hamilton Theorem can be used to transform the problem into an algebraic one

### 易混淆点 Easily Confused Points

- **特征多项式与最小多项式的区别**: 特征多项式是矩阵的特征值的多项式，最小多项式是满足矩阵等式 $p(A) = 0$ 的最低次多项式
  **Difference between characteristic polynomial and minimal polynomial**: The characteristic polynomial is the polynomial of the eigenvalues of the matrix, while the minimal polynomial is the lowest-degree polynomial that satisfies the matrix equation $p(A) = 0$
- **矩阵与其特征值**: Cayley-Hamilton 定理表明矩阵的特征多项式应用于矩阵本身等于零矩阵，但不意味着矩阵本身为零
  **Matrix and its eigenvalues**: The Cayley-Hamilton Theorem indicates that the characteristic polynomial of a matrix, when applied to the matrix itself, equals the zero matrix, but this does not mean the matrix itself is zero

## 示例 Examples

### 示例 1: 计算矩阵的特征多项式并验证 Cayley-Hamilton 定理

Example 1: Calculate the characteristic polynomial of a matrix and verify the Cayley-Hamilton Theorem

设 $A$ 为一个 $2 \times 2$ 矩阵:

Let $A$ be a $2 \times 2$ matrix:

$$
A = \begin{pmatrix}
4 & 1 \\
2 & 3
\end{pmatrix}
$$

1. 计算特征多项式:
   Calculate the characteristic polynomial:

$$
p(\lambda) = \det(\lambda I - A) = \det\begin{pmatrix}
\lambda - 4 & -1 \\
-2 & \lambda - 3
\end{pmatrix} = (\lambda - 4)(\lambda - 3) - (-2)(-1) = \lambda^2 - 7\lambda + 10
$$

1. 验证 $p(A) = 0$:
   Verify $p(A) = 0$:

$$
p(A) = A^2 - 7A + 10I
$$

计算 $A^2$:

Calculate $A^2$:

$$
A^2 = \begin{pmatrix}
4 & 1 \\
2 & 3
\end{pmatrix} \begin{pmatrix}
4 & 1 \\
2 & 3
\end{pmatrix} = \begin{pmatrix}
18 & 7 \\
14 & 11
\end{pmatrix}
$$

然后:

Then:

$$
p(A) = \begin{pmatrix}
18 & 7 \\
14 & 11
\end{pmatrix} - 7\begin{pmatrix}
4 & 1 \\
2 & 3
\end{pmatrix} + 10\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix} = \begin{pmatrix}
0 & 0 \\
0 & 0
\end{pmatrix}
$$

这验证了 Cayley-Hamilton 定理

This verifies the Cayley-Hamilton Theorem

### 示例 2: 利用 Cayley-Hamilton 定理计算高次幂矩阵

Example 2: Using the Cayley-Hamilton Theorem to compute higher powers of a matrix

对于矩阵 $A$:

For the matrix $A$:

$$
A = \begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

特征多项式为:

The characteristic polynomial is:

$$
p(\lambda) = \lambda^2 - 5\lambda - 2
$$

根据 Cayley-Hamilton 定理:

According to the Cayley-Hamilton Theorem:

$$
A^2 - 5A + 2I = 0 \implies A^2 = 5A - 2I
$$

因此可以简化 $A^3$ 的计算:

Thus, the computation of $A^3$ can be simplified:

$$
A^3 = A \cdot A^2 = A(5A - 2I) = 5A^2 - 2A = 5(5A - 2I) - 2A = 25A - 10I - 2A = 23A - 10I
$$

## 3x3 矩阵的 Cayley-Hamilton 定理 Cayley-Hamilton Theorem for a 3x3 Matrix

对于一个 $3 \times 3$ 矩阵 $A$:

For a $3 \times 3$ matrix $A$:

$$
A = \begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}
$$

其特征多项式可以表示为:

Its characteristic polynomial can be expressed as:

$$
p(\lambda) = \det(\lambda I - A) = \lambda^3 - \text{tr}(A)\lambda^2 + \text{sum of principal minors of } A \cdot \lambda - \det(A)
$$

其中:

Where:

- $\text{tr}(A)$ 表示矩阵 $A$ 的迹，即对角线上元素的和:

  $\text{tr}(A)$ denotes the trace of the matrix $A$, which is the sum of the diagonal elements:

  $$
  \text{tr}(A) = a_{11} + a_{22} + a_{33}

$

$

- 矩阵 $A$ 的所有主子式之和
  The sum of the principal minors of matrix $A$

例如，对于矩阵 $A$:

For example, for the matrix $A$:

$$
A = \begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{pmatrix}
$$

其所有主子式的行列式之和为:

The sum of the determinants of all its principal minors is:

$$
\text{sum of principal minors} = \det\begin{pmatrix}
a & b \\
d & e
\end{pmatrix} + \det\begin{pmatrix}
a & c \\
g & i
\end{pmatrix} + \det\begin{pmatrix}
e & f \\
h & i
\end{pmatrix}
$$

应用 Cayley-Hamilton 定理，将特征多项式 $p(\lambda)$ 应用于矩阵 $A$，得到:

Applying the Cayley-Hamilton Theorem, the characteristic polynomial $p(\lambda)$ is applied to the matrix $A$ to obtain:

$$
p(A) = A^3 - \text{tr}(A)A^2 + \text{sum of principal minors of } A \cdot A - \det(A)I = 0
$$
