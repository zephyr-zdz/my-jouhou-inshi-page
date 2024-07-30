# SVD 分解 | SVD Decomposition

## 定义 | Definition

- 奇异值分解（SVD）是一种矩阵分解方法，它将一个矩阵分解为三个矩阵的乘积：
  - The Singular Value Decomposition (SVD) is a matrix factorization method that decomposes a matrix into the product of three matrices:

$$
  \mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T
$$

  - 其中 $\mathbf{A}$ 是 $m \times n$ 矩阵，$\mathbf{U}$ 是 $m \times m$ 正交矩阵，$\mathbf{\Sigma}$ 是 $m \times n$ 对角矩阵，$\mathbf{V}$ 是 $n \times n$ 正交矩阵
  - Where $\mathbf{A}$ is an $m \times n$ matrix, $\mathbf{U}$ is an $m \times m$ orthogonal matrix, $\mathbf{\Sigma}$ is an $m \times n$ diagonal matrix, and $\mathbf{V}$ is an $n \times n$ orthogonal matrix

## 正交矩阵 | Orthogonal Matrix

- 正交矩阵 $\mathbf{Q}$ 满足 $\mathbf{Q}^T \mathbf{Q} = \mathbf{I}$
  - An orthogonal matrix $\mathbf{Q}$ satisfies $\mathbf{Q}^T \mathbf{Q} = \mathbf{I}$
- 正交矩阵的列向量互相正交且单位化
  - The column vectors of an orthogonal matrix are orthogonal to each other and have unit length

## 奇异值 | Singular Values

- 奇异值是对角矩阵 $\mathbf{\Sigma}$ 中的非负元素，按降序排列
  - Singular values are the non-negative elements on the diagonal of the matrix $\mathbf{\Sigma}$, arranged in descending order
- 奇异值的数量等于矩阵 $\mathbf{A}$ 的秩
  - The number of singular values equals the rank of the matrix $\mathbf{A}$

## SVD 分解的具体操作 | Steps for SVD Decomposition

1. 计算 $\mathbf{A} \mathbf{A}^T$ 和 $\mathbf{A}^T \mathbf{A}$
   - Compute $\mathbf{A} \mathbf{A}^T$ and $\mathbf{A}^T \mathbf{A}$
2. 找到 $\mathbf{A} \mathbf{A}^T$ 的特征值和特征向量，特征向量组成矩阵 $\mathbf{U}$
   - Find the eigenvalues and eigenvectors of $\mathbf{A} \mathbf{A}^T$, with the eigenvectors forming the matrix $\mathbf{U}$
3. 找到 $\mathbf{A}^T \mathbf{A}$ 的特征值和特征向量，特征向量组成矩阵 $\mathbf{V}$
   - Find the eigenvalues and eigenvectors of $\mathbf{A}^T \mathbf{A}$, with the eigenvectors forming the matrix $\mathbf{V}$
4. 对角矩阵 $\mathbf{\Sigma}$ 的对角元素是 $\mathbf{A} \mathbf{A}^T$ 或 $\mathbf{A}^T \mathbf{A}$ 的非零特征值的平方根
   - The diagonal elements of the diagonal matrix $\mathbf{\Sigma}$ are the square roots of the non-zero eigenvalues of $\mathbf{A} \mathbf{A}^T$ or $\mathbf{A}^T \mathbf{A}$

## 举例 | Example

设 $\mathbf{A}$ 为以下 $2 \times 2$ 矩阵

- Given $\mathbf{A}$ is the following $2 \times 2$ matrix

$$
\mathbf{A} = \begin{pmatrix}
3 & 1 \\
1 & 3
\end{pmatrix}
$$

### 计算 $\mathbf{A} \mathbf{A}^T$ 和 $\mathbf{A}^T \mathbf{A}$ | Compute $\mathbf{A} \mathbf{A}^T$ and $\mathbf{A}^T \mathbf{A}$

$$
\mathbf{A} \mathbf{A}^T = \begin{pmatrix}
10 & 6 \\
6 & 10
\end{pmatrix}, \quad
\mathbf{A}^T \mathbf{A} = \begin{pmatrix}
10 & 6 \\
6 & 10
\end{pmatrix}
$$

### 计算特征值和特征向量 | Compute Eigenvalues and Eigenvectors

- $\mathbf{A} \mathbf{A}^T$ 和 $\mathbf{A}^T \mathbf{A}$ 的特征值为 16 和 4，对应的特征向量为 $\begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}$ 和 $\begin{pmatrix} -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}$
  - The eigenvalues of $\mathbf{A} \mathbf{A}^T$ and $\mathbf{A}^T \mathbf{A}$ are 16 and 4, with corresponding eigenvectors $\begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}$ and $\begin{pmatrix} -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}$

### 构造 $\mathbf{U}$、$\mathbf{\Sigma}$ 和 $\mathbf{V}$ | Construct $\mathbf{U}$, $\mathbf{\Sigma}$, and $\mathbf{V}$

$$
\mathbf{U} = \begin{pmatrix}
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \\
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}}
\end{pmatrix}, \quad
\mathbf{\Sigma} = \begin{pmatrix}
4 & 0 \\
0 & 2
\end{pmatrix}, \quad
\mathbf{V} = \begin{pmatrix}
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \\
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}}
\end{pmatrix}
$$

### 验证 SVD 分解 | Verify SVD Decomposition

$$
\mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T = \begin{pmatrix}
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \\
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}}
\end{pmatrix}
\begin{pmatrix}
4 & 0 \\
0 & 2
\end{pmatrix}
\begin{pmatrix}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
-\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}}
\end{pmatrix}
$$

## SVD 分解与伪逆矩阵 | SVD and Pseudoinverse

- 在机器学习中，SVD 分解与伪逆矩阵有着紧密的联系
  - In machine learning, SVD decomposition is closely related to the pseudoinverse matrix
- 伪逆矩阵（也称为摩尔-彭若斯逆矩阵）用于解决线性系统，特别是当系统没有唯一解或者没有解时
  - The pseudoinverse matrix, also known as the Moore-Penrose inverse, is used to solve linear systems, especially when the system does not have a unique solution or has no solution at all
- 伪逆矩阵 $\mathbf{A}^+$ 的定义可以通过 SVD 分解来表示
  - The pseudoinverse matrix $\mathbf{A}^+$ can be defined in terms of the SVD decomposition
  - 若 $\mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$，则 $\mathbf{A}^+$ 为
   If $\mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$, then $\mathbf{A}^+$ is given by

$$
  \mathbf{A}^+ = \mathbf{V} \mathbf{\Sigma}^+ \mathbf{U}^T
$$

  - 其中 $\mathbf{\Sigma}^+$ 是 $\mathbf{\Sigma}$ 中所有非零奇异值的倒数构成的对角矩阵，并在剩余位置填充 0
  - Where $\mathbf{\Sigma}^+$ is a diagonal matrix that contains the reciprocals of the non-zero singular values of $\mathbf{\Sigma}$, with zeros filling the remaining positions

## SVD 分解在机器学习中的应用 | Applications of SVD in Machine Learning

1. **降维 | Dimensionality Reduction**
   - 在主成分分析（PCA）中，SVD 用于将数据从高维空间映射到低维空间，以减少计算复杂度并消除噪声
   - In Principal Component Analysis (PCA), SVD is used to map data from a high-dimensional space to a lower-dimensional space to reduce computational complexity and eliminate noise

2. **回归分析 | Regression Analysis**
   - 在多重线性回归中，当设计矩阵 $\mathbf{X}$ 列不独立时，可以使用伪逆矩阵来找到回归系数
   - In multiple linear regression, when the columns of the design matrix $\mathbf{X}$ are not independent, the pseudoinverse matrix can be used to find the regression coefficients

$$
   \mathbf{\beta} = \mathbf{X}^+ \mathbf{y}
$$

   - 其中 $\mathbf{y}$ 是响应变量，$\mathbf{\beta}$ 是回归系数
   - Where $\mathbf{y}$ is the response variable and $\mathbf{\beta}$ is the regression coefficient

3. **推荐系统 | Recommender Systems**
   - SVD 用于矩阵分解技术，分解用户-物品评分矩阵，预测用户可能喜欢的物品
   - SVD is used in matrix factorization techniques to decompose the user-item rating matrix to predict items that a user might like

4. **自然语言处理 | Natural Language Processing**
   - 在词嵌入中，SVD 用于将高维的词频矩阵降维，从而提取词之间的语义关系
   - In word embeddings, SVD is used to reduce the dimensionality of high-dimensional word frequency matrices to extract semantic relationships between words

通过理解 SVD 分解和伪逆矩阵的关系，可以更好地理解和应用许多机器学习算法。

Understanding the relationship between SVD decomposition and the pseudoinverse matrix can enhance the comprehension and application of many machine learning algorithms.
