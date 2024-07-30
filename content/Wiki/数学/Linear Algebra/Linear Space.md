# 线性空间 Linear Spaces

## 零空间 Null Space

### 定义与性质 Definition and Properties

1. **零空间 Null Space**：
   矩阵 $A$ 的零空间是解齐次线性方程组 $Ax = 0$ 的所有向量 $x$ 的集合，记作 $N(A)$。

   The null space of a matrix $A$ is the set of all vectors $x$ that satisfy the homogeneous system $Ax = 0$, denoted as $N(A)$.

2. **维数 Dimension**：
   零空间的维数被称为 **零空间的维数（nullity）**。如果 $A$ 是一个 $m \times n$ 矩阵，零空间的维数为 $n - \text{rank}(A)$。

   The dimension of the null space is called the **nullity**. If $A$ is an $m \times n$ matrix, the dimension of the null space is $n - \text{rank}(A)$.

### 计算方法 Calculation Methods

1. **行简化 Row Reduction**：
   对 $A$ 进行行简化，找出自由变量，并用这些变量表示出解空间。

   Perform row reduction on $A$, identify the free variables, and express the solution space in terms of these variables.

2. **参数表示 Parametric Form**：
   零空间的向量可以表示为参数向量的线性组合。

   The vectors in the null space can be expressed as a linear combination of parametric vectors.

   例 Example：

   $$
   A = \begin{pmatrix}
   1 & 2 & 1 \\
   0 & 0 & 1 \\
   1 & 2 & 0
   \end{pmatrix} \rightarrow \text{RREF} \rightarrow \begin{pmatrix}
   1 & 2 & 0 \\
   0 & 0 & 1 \\
   0 & 0 & 0
   \end{pmatrix}

$$

   $$

N(A) = \left\{ t \begin{pmatrix}

   -2 \\

   1 \\

   0

   \end{pmatrix} \mid t \in \mathbb{R} \right\}

$$

## 列空间 Column Space

### 定义与性质 Definition and Properties

1. **定义 Definition**：
   矩阵 $A$ 的列空间是由 $A$ 的所有列向量张成的空间，记作 $\text{Col}(A)$。
   
   The column space of a matrix $A$ is the space spanned by all the column vectors of $A$, denoted as $\text{Col}(A)$.

2. **维数 Dimension**：
   列空间的维数被称为 **秩（rank）**。如果 $A$ 是一个 $m \times n$ 矩阵，列空间的维数等于矩阵 $A$ 的秩 $\text{rank}(A)$。

   The dimension of the column space is called the **rank**. If $A$ is an $m \times n$ matrix, the dimension of the column space is the rank of the matrix $\text{rank}(A)$.

3. **几何意义 Geometric Interpretation**：
   列空间是线性方程组 $Ax = b$ 右侧向量 $b$ 的所有可能值的集合。

   The column space represents all possible values of the right-hand side vector $b$ in the linear system $Ax = b$.

### 计算方法 Calculation Methods

1. **行简化 Row Reduction**：
   对 $A$ 进行行简化，保留列阶梯形矩阵（column echelon form）中的主列向量，它们张成列空间。

   Perform row reduction on $A$ and retain the pivot columns in the column echelon form, which span the column space.

   例 Example：
   $$

   A = \begin{pmatrix}

   1 & 2 & 3 \\

   4 & 5 & 6 \\

   7 & 8 & 9

   \end{pmatrix} \rightarrow \text{RREF} \rightarrow \begin{pmatrix}

   1 & 0 & -1 \\

   0 & 1 & 2 \\

   0 & 0 & 0

   \end{pmatrix}

$$
   列空间由原矩阵 $A$ 的第一列和第二列张成，即 $\text{Col}(A) = \text{Span}\left\{ \begin{pmatrix} 1 \\ 4 \\ 7 \end{pmatrix}, \begin{pmatrix} 2 \\ 5 \\ 8 \end{pmatrix} \right\}$。

   The column space is spanned by the first and second columns of the original matrix $A$, i.e., $\text{Col}(A) = \text{Span}\left\{ \begin{pmatrix} 1 \\ 4 \\ 7 \end{pmatrix}, \begin{pmatrix} 2 \\ 5 \\ 8 \end{pmatrix} \right\}$.

## 行空间 Row Space

### 定义与性质 Definition and Properties

1. **定义 Definition**：
   矩阵 $A$ 的行空间是由 $A$ 的所有行向量张成的空间，记作 $\text{Row}(A)$。

   The row space of a matrix $A$ is the space spanned by all the row vectors of $A$, denoted as $\text{Row}(A)$.

2. **维数 Dimension**：
   行空间的维数等于矩阵 $A$ 的秩 $\text{rank}(A)$。

   The dimension of the row space is equal to the rank of the matrix $\text{rank}(A)$.

### 计算方法 Calculation Methods

1. **行简化 Row Reduction**：
   对 $A$ 进行行简化，保留简化行阶梯形矩阵（reduced row echelon form, RREF）中的非零行，它们张成行空间。

   Perform row reduction on $A$ and retain the non-zero rows in the reduced row echelon form (RREF), which span the row space.

   例 Example：
   $$

   A = \begin{pmatrix}

   1 & 2 & 3 \\

   4 & 5 & 6 \\

   7 & 8 & 9

   \end{pmatrix} \rightarrow \text{RREF} \rightarrow \begin{pmatrix}

   1 & 0 & -1 \\

   0 & 1 & 2 \\

   0 & 0 & 0

   \end{pmatrix}

$$
   行空间由非零行向量张成，即 $\text{Row}(A) = \text{Span}\left\{ \begin{pmatrix} 1 & 0 & -1 \end{pmatrix}, \begin{pmatrix} 0 & 1 & 2 \end{pmatrix} \right\}$。

   The row space is spanned by the non-zero row vectors, i.e., $\text{Row}(A) = \text{Span}\left\{ \begin{pmatrix} 1 & 0 & -1 \end{pmatrix}, \begin{pmatrix} 0 & 1 & 2 \end{pmatrix} \right\}$.

## 零空间与列空间的关系 Relationship between Null Space and Column Space

### 正交补 Orthogonal Complement

1. **定义 Definition**：
   矩阵 $A$ 的列空间 $\text{Col}(A)$ 和零空间 $N(A^T)$（$A$ 的转置的零空间）互为正交补，即
   $$

   \text{Col}(A) \perp N(A^T)

$$
   所有在 $\text{Col}(A)$ 中的向量都与在 $N(A^T)$ 中的向量正交。

   The column space $\text{Col}(A)$ and the null space of the transpose $N(A^T)$ of a matrix $A$ are orthogonal complements of each other, i.e.,
   $$

   \text{Col}(A) \perp N(A^T)

$$
   All vectors in $\text{Col}(A)$ are orthogonal to all vectors in $N(A^T)$.

2. **几何意义 Geometric Interpretation**：
   如果 $y \in \text{Col}(A)$，则 $y \cdot x = 0$ 对于任意 $x \in N(A^T)$ 成立。

   If $y \in \text{Col}(A)$, then $y \cdot x = 0$ for any $x \in N(A^T)$.

### 基础定理 Fundamental Theorem

线性代数的基本定理之一表明，对于任意矩阵 $A$，
$$

\text{rank}(A) + \text{nullity}(A) = n

$$
其中 $n$ 是矩阵 $A$ 的列数。

One of the fundamental theorems of linear algebra states that for any matrix $A$,
$$

\text{rank}(A)

 + \text{nullity}(A) = n

$$
where $n$ is the number of columns of the matrix $A$.

### 零空间和列空间的关系总结 Summary of the Relationship between Null Space and Column Space

1. 矩阵 $A$ 的零空间 $N(A)$ 是 $A$ 的列空间 $\text{Col}(A)$ 的正交补。

   The null space $N(A)$ of a matrix $A$ is the orthogonal complement of the column space $\text{Col}(A)$ of $A$.

2. 矩阵 $A^T$ 的零空间 $N(A^T)$ 是 $A$ 的行空间 $\text{Row}(A)$ 的正交补。

   The null space $N(A^T)$ of the transpose matrix $A^T$ is the orthogonal complement of the row space $\text{Row}(A)$ of $A$.

3. 矩阵 $A$ 的秩和零空间的维数之和等于 $A$ 的列数。

   The sum of the rank of matrix $A$ and the dimension of its null space equals the number of columns of $A$.
