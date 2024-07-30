# Jordan 标准型 Jordan Canonical Form

## 定义 Definition

**Jordan 标准型** 是一种矩阵分解形式，每个方阵都可以表示为一个对角矩阵被若干 Jordan 块取代后的形式。这种形式使得处理矩阵的幂和矩阵函数更加简单。

A **Jordan canonical form** is a type of matrix decomposition where any square matrix can be represented in a form that replaces the diagonal matrix with several Jordan blocks. This form simplifies the handling of matrix powers and matrix functions.

### Jordan 块 Jordan Block

一个 $n \times n$ 的 Jordan 块 $\mathbf{J}_n(\lambda)$ 是一个以下形式的矩阵：

An $n \times n$ Jordan block $\mathbf{J}_n(\lambda)$ is a matrix of the following form:

$$
\mathbf{J}_n(\lambda) = \begin{pmatrix}
\lambda & 1 & 0 & \cdots & 0 \\
0 & \lambda & 1 & \cdots & 0 \\
0 & 0 & \lambda & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & 1 \\
0 & 0 & 0 & \cdots & \lambda
\end{pmatrix}
$$

其中，$\lambda$ 是特征值。

where $\lambda$ is an eigenvalue.

## 性质 Properties

1. **特征值 Eigenvalues**：Jordan 标准型的对角线元素都是原矩阵的特征值。

   The diagonal elements of the Jordan canonical form are the eigenvalues of the original matrix.

2. **相似矩阵 Similarity**：每个矩阵 $\mathbf{A}$ 都与它的 Jordan 标准型 $\mathbf{J}$ 相似，即存在可逆矩阵 $\mathbf{P}$ 使得 $\mathbf{A} = \mathbf{PJP}^{-1}$。

   Every matrix $\mathbf{A}$ is similar to its Jordan canonical form $\mathbf{J}$, meaning there exists an invertible matrix $\mathbf{P}$ such that $\mathbf{A} = \mathbf{PJP}^{-1}$.

3. **唯一性 Uniqueness**：Jordan 标准型在相似矩阵的意义上是唯一的。

   The Jordan canonical form is unique up to similarity transformations.

4. **块对角形式 Block Diagonal Form**：Jordan 标准型由若干 Jordan 块构成，其大小和数量由矩阵 $\mathbf{A}$ 的特征值和特征向量决定。

   The Jordan canonical form is composed of several Jordan blocks, the size and number of which are determined by the eigenvalues and eigenvectors of the matrix $\mathbf{A}$.

## 证明 Proof

1. **特征值分解 Eigenvalue Decomposition**：首先，对矩阵 $\mathbf{A}$ 进行特征值分解，找出所有特征值和对应的特征向量。

   First, perform eigenvalue decomposition on the matrix $\mathbf{A}$ to find all eigenvalues and their corresponding eigenvectors.

2. **构建 Jordan 块 Construct Jordan Blocks**：根据特征值和特征向量，构建对应的 Jordan 块。对于每个特征值 $\lambda_i$，若其代数重数为 $m$，几何重数为 $g$，则需要构造 $m - g$ 个大小大于 $1$ 的 Jordan 块。

   Construct the corresponding Jordan blocks based on the eigenvalues and eigenvectors. For each eigenvalue $\lambda_i$, if its algebraic multiplicity is $m$ and its geometric multiplicity is $g$, construct $m - g$ Jordan blocks of size greater than 1.

3. **构造变换矩阵 Construct the Transformation Matrix**：构造变换矩阵 $\mathbf{P}$，其列向量由特征向量和广义特征向量组成。

   Construct the transformation matrix $\mathbf{P}$, whose column vectors consist of the eigenvectors and generalized eigenvectors.

4. **验证 Verification**：验证 $\mathbf{P}^{-1} \mathbf{A} \mathbf{P}$ 是否为 Jordan 标准型。若是，则 $\mathbf{J} = \mathbf{P}^{-1} \mathbf{A} \mathbf{P}$。

   Verify that $\mathbf{P}^{-1} \mathbf{A} \mathbf{P}$ is in Jordan canonical form. If so, then $\mathbf{J} = \mathbf{P}^{-1} \mathbf{A} \mathbf{P}$.

## 例子 Example

设 $\mathbf{A}$ 为以下矩阵：

Let $\mathbf{A}$ be the following matrix:

$$
\mathbf{A} = \begin{pmatrix}
5 & 4 & 2 & 1 \\
0 & 1 & -1 & -1 \\
0 & 0 & 2 & 1 \\
0 & 0 & 0 & 3
\end{pmatrix}
$$

其 Jordan 标准型为：

Its Jordan canonical form is:

$$
\mathbf{J} = \begin{pmatrix}
5 & 1 & 0 & 0 \\
0 & 5 & 0 & 0 \\
0 & 0 & 2 & 1 \\
0 & 0 & 0 & 3
\end{pmatrix}
$$
