# 线性方程组 Linear Equations

## 简介 Introduction

在线性代数中，两个重要的方程组形式是 $Ax = 0$ 和 $Ax = b$。这两个方程组涉及到矩阵 $A$ 和向量 $x$、$b$，它们的解集有着不同的性质和几何意义。理解这些解集对于线性代数的学习和应用至关重要。

In linear algebra, two important forms of systems of equations are $Ax = 0$ and $Ax = b$. These systems involve a matrix $A$ and vectors $x$ and $b$, and their solution sets have different properties and geometric meanings. Understanding these solution sets is crucial for learning and applying linear algebra.

## 齐次线性方程组 $Ax = 0$ Homogeneous System $Ax = 0$

### 定义与性质 Definition and Properties

1. **定义 Definition**：

   $$
   Ax = 0

$$

   这里，$A$ 是一个 $m \times n$ 的矩阵，$x$ 是一个 $n$ 维列向量，零向量 $0$ 是一个 $m$ 维列向量。

   Here, $A$ is an $m \times n$ matrix, $x$ is an $n$-dimensional column vector, and the zero vector $0$ is an $m$-dimensional column vector.

2. **解集 Solution Set**：
   $Ax = 0$ 的解集被称为矩阵 $A$ 的 **零空间（null space）** 或 **核（kernel）**，记作 $N(A)$。
   这个解集是一个向量空间。

   The solution set of $Ax = 0$ is called the **null space** or **kernel** of the matrix $A$, denoted as $N(A)$. This solution set is a vector space.

### 求解方法 Solution Methods

1. **行简化 Row Reduction**：
   将矩阵 $A$ 进行 **简化行阶梯形矩阵（reduced row echelon form, RREF）** 变换。

   Reduce the matrix $A$ to its **reduced row echelon form (RREF)**.

   例 Example：
   $$

   A = \begin{pmatrix}

   1 & 2 & 1 \\

   2 & 4 & 2 \\

   3 & 6 & 3

   \end{pmatrix} \rightarrow \text{RREF} \rightarrow \begin{pmatrix}

   1 & 2 & 1 \\

   0 & 0 & 0 \\

   0 & 0 & 0

   \end{pmatrix}

$$
   通过 RREF，可以发现 $x_1 + 2x_2 + x_3 = 0$，即 $$x = t_1 \begin{pmatrix}
   -2 \\
   1 \\
   0
   \end{pmatrix} + t_2 \begin{pmatrix}
   -1 \\
   0 \\
   1
   \end{pmatrix}$，其中 $t_1, t_2 \in \mathbb{R}$$。
   
   By RREF, we find that $x_1 + 2x_2 + x_3 = 0$, hence $$x = t_1 \begin{pmatrix}
   -2 \\
   1 \\
   0
   \end{pmatrix} + t_2 \begin{pmatrix}
   -1 \\
   0 \\
   1
   \end{pmatrix}$, where $t_1, t_2 \in \mathbb{R}$$.

2. **使用分块矩阵和转置矩阵 Constructing Solution with Block Matrix and Transpose Matrix**：
   假设矩阵 $A$ 的 RREF 可以表示为分块矩阵：
   $$

   \text{RREF}(A) = \begin{pmatrix}

   I & B \\

   O & O

   \end{pmatrix}

$$
   其中 $I$ 是单位矩阵，$B$ 是适当大小的矩阵，$O$ 是零矩阵。用 $B$ 的转置 $B^T$ 和单位矩阵来构造零空间的基础解系。

   Suppose the RREF of matrix $A$ can be represented as a block matrix:
   $$

   \text{RREF}(A) = \begin{pmatrix}

   I & B \\

   O & O

   \end{pmatrix}

$$
   where $I$ is the identity matrix, $B$ is an appropriately sized matrix, and $O`$ is the zero matrix. Use the transpose of $B$, $B^T$, and the identity matrix to construct the basis for the null space.

   例 Example：
   $$

   A = \begin{pmatrix}

   1 & 2 & 1 & 3 \\

   2 & 4 & 2 & 6 \\

   3 & 6 & 3 & 9

   \end{pmatrix} \rightarrow \text{RREF} \rightarrow \begin{pmatrix}

   1 & 2 & 1 & 3 \\

   0 & 0 & 0 & 0 \\

   0 & 0 & 0 & 0

   \end{pmatrix}

$$
   从 RREF 可以看到 $x_2, x_3, x_4$ 是自由变量。构造 $B^T$：
   $$

   B = \begin{pmatrix}

   2 & 1 & 3

   \end{pmatrix}, \quad B^T = \begin{pmatrix}

   2 \\

   1 \\

   3

   \end{pmatrix}

$$
   解空间为：
   $$

   x = t_1 \begin{pmatrix}

   -2 \\

   1 \\

   0 \\

   0

   \end{pmatrix} + t_2 \begin{pmatrix}

   -1 \\

   0 \\

   1 \\

   0

   \end{pmatrix} + t_3 \begin{pmatrix}

   -3 \\

   0 \\

   0 \\

   1

   \end{pmatrix}

$$
   其中 $t_1, t_2, t_3 \in \mathbb{R}$。

   From the RREF, we see that $x_2, x_3, x_4$ are free variables. Construct $B^T$:
   $$

   B = \begin{pmatrix}

   2 & 1 & 3

   \end{pmatrix}, \quad B^T = \begin{pmatrix}

   2 \\

   1 \\

   3

   \end{pmatrix}

$$
   The solution space is:
   $$

   x = t_1 \begin{pmatrix}

   -2 \\

   1 \\

   0 \\

   0

   \end{pmatrix} + t_2 \begin{pmatrix}

   -1 \\

   0 \\

   1 \\

   0

   \end{pmatrix} + t_3 \begin{pmatrix}

   -3 \\

   0 \\

   0 \\

   1

   \end{pmatrix}

$$
   where $t_1, t_2, t_3 \in \mathbb{R}$.

## 非齐次线性方程组 $Ax = b$ Non-Homogeneous System $Ax = b$

### 定义与性质 Definition and Properties

1. **定义 Definition**：
   $$

   Ax = b

$$
   这里，$b$ 是一个 $m$ 维列向量。

   Here, $b$ is an $m$-dimensional column vector.

2. **解集 Solution Set**：
   如果 $Ax = b$ 有解，那么解集可以表示为一个特解 $x_p$ 加上齐次方程组 $Ax = 0$ 的解空间，即
   $$

   x = x_p + N(A)

$$

   If $Ax = b$ has a solution, the solution set can be expressed as a particular solution $x_p$ plus the solution space of the homogeneous system $Ax = 0$, i.e.,
   $$

   x = x_p + N(A)

$$

### 求解方法 Solution Methods

1. **行简化 Row Reduction**：
   将增广矩阵 $[A | b]$ 进行行简化，直到得到简化行阶梯形矩阵。

   Perform row reduction on the augmented matrix $[A | b]$ until you obtain the reduced row echelon form (RREF).

   例 Example：
   $$

   A = \begin{pmatrix}

   1 & 2 & 1 \\

   2 & 4 & 2 \\

   3 & 6 & 3

   \end{pmatrix}, \quad b = \begin{pmatrix}

   1 \\

   2 \\

   3

   \end{pmatrix} \rightarrow [A | b] = \begin{pmatrix}

   1 & 2 & 1 & 1 \\

   2 & 4 & 2 & 2 \\

   3 & 6 & 3 & 3

   \end{pmatrix} \rightarrow \text{RREF} \rightarrow \begin{pmatrix}

   1 & 2 & 1 & 1 \\

   0 & 0 & 0 & 0 \\

   0 & 0 & 0 & 0

   \end{pmatrix}

$$
   通过 RREF，可以发现 $x_1 + 2x_2 + x_3 = 1$，解集为 $$x = \begin{pmatrix}
   1 \\
   0 \\
   0
   \end{pmatrix} + t_1 \begin{pmatrix}
   -2 \\
   1 \\
   0
   \end{pmatrix} + t_2 \begin{pmatrix}
   -1 \\
   0 \\
   1
   \end{pmatrix}$$，其中 $t_1, t_2 \in \mathbb{R}$。

   By RREF, we find that $x_1 + 2x_2 + x_3 = 1$, hence the solution set is $$x = \begin{pmatrix}
   1 \\
   0 \\
   0
   \end{pmatrix} + t_1 \begin{pmatrix}
   -2 \\
   1 \\
   0
   \end{pmatrix} + t_2 \begin{pmatrix}
   -1 \\
   0 \\
   1
   \end{pmatrix}$$, where $t_1, t_2 \in \mathbb{R}$。

## Rouché-Capelli Theorem
### Definition / 定义

**Rouché-Capelli Theorem**: This theorem states that a system of linear equations $\mathbf{A}\mathbf{x} = \mathbf{b}$ has at least one solution if and only if the rank of the coefficient matrix $\mathbf{A}$ is equal to the rank of the augmented matrix $[\mathbf{A} | \mathbf{b}]$.
$$

\text{rank}(\mathbf{A}) = \text{rank}([\mathbf{A} | \mathbf{b}])

$$

**Rouché-Capelli 定理**：该定理指出，对于线性方程组 $\mathbf{A}\mathbf{x} = \mathbf{b}$，当且仅当系数矩阵 $\mathbf{A}$ 的秩等于增广矩阵 $[\mathbf{A} | \mathbf{b}]$ 的秩时，方程组至少有一个解。
$$

\text{rank}(\mathbf{A}) = \text{rank}([\mathbf{A} | \mathbf{b}])

$$

### Properties / 性质

1. **Consistent System**: If $\text{rank}(\mathbf{A}) = \text{rank}([\mathbf{A} | \mathbf{b}])$, the system is consistent (i.e., it has at least one solution).
   - **一致性系统**：如果 $\text{rank}(\mathbf{A}) = \text{rank}([\mathbf{A} | \mathbf{b}])$，则该系统是一致的（即，它至少有一个解）。

2. **Inconsistent System**: If $\text{rank}(\mathbf{A}) \neq \text{rank}([\mathbf{A} | \mathbf{b}])$, the system is inconsistent (i.e., it has no solutions).
   - **不一致性系统**：如果 $\text{rank}(\mathbf{A}) \neq \text{rank}([\mathbf{A} | \mathbf{b}])$，则该系统是不一致的（即，它没有解）。

3. **Unique Solution**: If $\text{rank}(\mathbf{A}) = \text{rank}([\mathbf{A} | \mathbf{b}]) = n$ (where $n$ is the number of unknowns), the system has a unique solution.
   - **唯一解**：如果 $\text{rank}(\mathbf{A}) = \text{rank}([\mathbf{A} | \mathbf{b}]) = n$（其中 $n$ 是未知数的数量），则该系统有唯一解。

4. **Infinite Solutions**: If $\text{rank}(\mathbf{A}) = \text{rank}([\mathbf{A} | \mathbf{b}]) < n$, the system has infinitely many solutions.
   - **无限多解**：如果 $\text{rank}(\mathbf{A}) = \text{rank}([\mathbf{A} | \mathbf{b}]) < n$，则该系统有无限多个解。
