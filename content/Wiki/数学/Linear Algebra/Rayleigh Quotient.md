# Rayleigh 商 (Rayleigh Quotient)

## 定义 Definition

Rayleigh 商用于描述一个向量 $\mathbf{x}$ 和矩阵 $\mathbf{A}$ 之间的关系。对于给定的向量 $\mathbf{x}$ 和对称矩阵 $\mathbf{A}$，Rayleigh 商定义如下：

The Rayleigh quotient describes the relationship between a vector $\mathbf{x}$ and a matrix $\mathbf{A}$. For a given vector $\mathbf{x}$ and symmetric matrix $\mathbf{A}$, the Rayleigh quotient is defined as:

$$
R(\mathbf{x}) = \frac{\mathbf{x}^\top \mathbf{A} \mathbf{x}}{\mathbf{x}^\top \mathbf{x}}
$$

其中，$\mathbf{x} \neq \mathbf{0}$。

where $\mathbf{x} \neq \mathbf{0}$.

## 性质 Properties

1. **范围 Range**:
    对于对称矩阵 $\mathbf{A}$，Rayleigh 商 $R(\mathbf{x})$ 的值在 $\mathbf{A}$ 的最小特征值 $\lambda_{\min}$ 和最大特征值 $\lambda_{\max}$ 之间。

    For a symmetric matrix $\mathbf{A}$, the value of the Rayleigh quotient $R(\mathbf{x})$ lies between the minimum eigenvalue $\lambda_{\min}$ and the maximum eigenvalue $\lambda_{\max}$ of $\mathbf{A}$.

2. **特征值与特征向量 Eigenvalues and Eigenvectors**:
    如果 $\mathbf{x}$ 是 $\mathbf{A}$ 的特征向量，则 Rayleigh 商 $R(\mathbf{x})$ 等于 $\mathbf{x}$ 对应的特征值。

    If $\mathbf{x}$ is an eigenvector of $\mathbf{A}$, then the Rayleigh quotient $R(\mathbf{x})$ equals the eigenvalue corresponding to $\mathbf{x}$.

3. **正定矩阵 Positive Definite Matrix**:
    如果 $\mathbf{A}$ 是正定矩阵，则 Rayleigh 商 $R(\mathbf{x})$ 始终为正。

    If $\mathbf{A}$ is a positive definite matrix, then the Rayleigh quotient $R(\mathbf{x})$ is always positive.

## 求解最值过程 Solving for Extremum

Rayleigh 商在求解特征值问题中非常重要，尤其是求最大和最小特征值。Rayleigh quotient is crucial in solving eigenvalue problems, especially for finding the maximum and minimum eigenvalues.

### 利用二次型、线性变换和矩阵特征值计算 Rayleigh 商的最值 Using Quadratic Forms, Linear Transformations, and Matrix Eigenvalues to Calculate the Extremum of the Rayleigh Quotient

1. **二次型 Quadratic Form**:
    [[Quadratic Forms and Positive Definite Matrices]]

    二次型 $\mathbf{x}^\top \mathbf{A} \mathbf{x}$ 表示向量 $\mathbf{x}$ 在矩阵 $\mathbf{A}$ 作用下的二次变换。Rayleigh 商可以视为二次型与向量模长平方的比值。

    The quadratic form $\mathbf{x}^\top \mathbf{A} \mathbf{x}$ represents the quadratic transformation of the vector $\mathbf{x}$ under the matrix $\mathbf{A}$. The Rayleigh quotient can be seen as the ratio of the quadratic form to the squared norm of the vector.

2. **线性变换 Linear Transformation**:
	 [[Linear Transformation]]
    考虑 $\mathbf{A}$ 的特征值分解 $\mathbf{A} = \mathbf{Q} \mathbf{\Lambda} \mathbf{Q}^\top$，其中 $\mathbf{Q}$ 是正交矩阵，$\mathbf{\Lambda}$ 是对角矩阵，包含 $\mathbf{A}$ 的特征值。令 $\mathbf{y} = \mathbf{Q}^\top \mathbf{x}$，则有

    Consider the eigenvalue decomposition of $\mathbf{A}$, $\mathbf{A} = \mathbf{Q} \mathbf{\Lambda} \mathbf{Q}^\top$, where $\mathbf{Q}$ is an orthogonal matrix and $\mathbf{\Lambda}$ is a diagonal matrix containing the eigenvalues of $\mathbf{A}$. Let $\mathbf{y} = \mathbf{Q}^\top \mathbf{x}$, then

$$
R(\mathbf{x}) = \frac{\mathbf{y}^\top \mathbf{\Lambda} \mathbf{y}}{\mathbf{y}^\top \mathbf{y}}
$$

1. **分解过程 Decomposition Process**:

    - **特征值分解 Eigenvalue Decomposition**:
	    [[Eigenvalue & Eigen vector]]
        首先，我们需要找到对称矩阵 $\mathbf{A}$ 的特征值和特征向量。特征值分解 $\mathbf{A} = \mathbf{Q} \mathbf{\Lambda} \mathbf{Q}^\top$ 其中 $\mathbf{Q}$ 是由 $\mathbf{A}$ 的特征向量构成的正交矩阵，$\mathbf{\Lambda}$ 是对角矩阵，包含 $\mathbf{A}$ 的特征值 $\lambda_i$。

        First, we need to find the eigenvalues and eigenvectors of the symmetric matrix $\mathbf{A}$. The eigenvalue decomposition $\mathbf{A} = \mathbf{Q} \mathbf{\Lambda} \mathbf{Q}^\top$ where $\mathbf{Q}$ is an orthogonal matrix composed of the eigenvectors of $\mathbf{A}$, and $\mathbf{\Lambda}$ is a diagonal matrix containing the eigenvalues $\lambda_i$ of $\mathbf{A}$.

$$
 \mathbf{A} \mathbf{q}_i = \lambda_i \mathbf{q}_i 
$$

        其中 $\mathbf{q}_i$ 是 $\mathbf{A}$ 的特征向量，$\lambda_i$ 是对应的特征值。

        where $\mathbf{q}_i$ is the eigenvector of $\mathbf{A}$ and $\lambda_i$ is the corresponding eigenvalue.

    - **变换到特征空间 Transformation to Eigenvector Space**:
        将向量 $\mathbf{x}$ 表示为特征向量的线性组合，即 $\mathbf{x} = \mathbf{Q} \mathbf{y}$，其中 $\mathbf{y}$ 是新坐标系中的向量。

        Represent the vector $\mathbf{x}$ as a linear combination of eigenvectors, i.e., $\mathbf{x} = \mathbf{Q} \mathbf{y}$, where $\mathbf{y}$ is the vector in the new coordinate system.
        

$$
 \mathbf{x}^\top \mathbf{A} \mathbf{x} = (\mathbf{Q} \mathbf{y})^\top \mathbf{A} (\mathbf{Q} \mathbf{y}) = \mathbf{y}^\top (\mathbf{Q}^\top \mathbf{A} \mathbf{Q}) \mathbf{y} = \mathbf{y}^\top \mathbf{\Lambda} \mathbf{y} 
$$

        由于 $\mathbf{Q}$ 是正交矩阵，所以 $\mathbf{Q}^\top \mathbf{Q} = \mathbf{I}$。

        Since $\mathbf{Q}$ is an orthogonal matrix, $\mathbf{Q}^\top \mathbf{Q} = \mathbf{I}$.
        $$

 \mathbf{x}^\top \mathbf{x} = (\mathbf{Q} \mathbf{y})^\top (\mathbf{Q} \mathbf{y}) = \mathbf{y}^\top \mathbf{Q}^\top \mathbf{Q} \mathbf{y} = \mathbf{y}^\top \mathbf{y} $$

    - **Rayleigh 商的表示 Representation of Rayleigh Quotient**:
        将以上结果代入 Rayleigh 商的定义中，得到：

        Substituting the above results into the definition of the Rayleigh quotient, we get:
        $$ R(\mathbf{x}) = \frac{\mathbf{x}^\top \mathbf{A} \mathbf{x}}{\mathbf{x}^\top \mathbf{x}} = \frac{\mathbf{y}^\top \mathbf{\Lambda} \mathbf{y}}{\mathbf{y}^\top \mathbf{y}} $$

1. **最大特征值与最小特征值 Maximum and Minimum Eigenvalues**:
    对于矩阵 $\mathbf{A}$ 的最大特征值 $\lambda_{\max}$ 和最小特征值 $\lambda_{\min}$，可以通过如下方式计算 Rayleigh 商的最值：

    For the maximum eigenvalue $\lambda_{\max}$ and minimum eigenvalue $\lambda_{\min}$ of the matrix $\mathbf{A}$, the extrema of the Rayleigh quotient can be calculated as follows:

    - **最大值 Maximum**: 当 $\mathbf{x}$ 为对应于 $\lambda_{\max}$ 的特征向量时，Rayleigh 商达到最大值 $\lambda_{\max}$。即

      When $\mathbf{x}$ is the eigenvector corresponding to $\lambda_{\max}$, the Rayleigh quotient reaches its maximum value $\lambda_{\max}$. That is,

      $$
      R(\mathbf{x}) = \lambda_{\max} \text{ 当 } \mathbf{x} = \mathbf{q}_{\max}


$$
 
    - **最小值 Minimum**: 当 $\mathbf{x}$ 为对应于 $\lambda_{\min}$ 的特征向量时，Rayleigh 商达到最小值 $\lambda_{\min}$。即

      When $\mathbf{x}$ is the eigenvector corresponding to $\lambda_{\min}$, the Rayleigh quotient reaches its minimum value $\lambda_{\min}$. That is,

      
$$

      R(\mathbf

{x}) = \lambda_{\min} \text{ 当 } \mathbf{x} = \mathbf{q}_{\min}

      $$

### 详细示例 Detailed Example

假设 $\mathbf{A}$ 是一个 $2 \times 2$ 的对称矩阵：

Suppose $\mathbf{A}$ is a $2 \times 2$ symmetric matrix:

$$

\mathbf{A} = \begin{pmatrix}

4 & 1 \\

1 & 3

\end{pmatrix}

$$

1. **求特征值和特征向量 Finding Eigenvalues and Eigenvectors**:
    解特征方程 $\det(\mathbf{A} - \lambda \mathbf{I}) = 0$，得到特征值 $\lambda_1 = 5, \lambda_2 = 2$。

    Solve the characteristic equation $\det(\mathbf{A} - \lambda \mathbf{I}) = 0$ to get eigenvalues $\lambda_1 = 5, \lambda_2 = 2$.

    对应的特征向量分别为：

    The corresponding eigenvectors are:

$$
    \mathbf{q}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \quad \mathbf{q}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}
$$

1. **特征值分解 Eigenvalue Decomposition**:
    构造 $\mathbf{Q}$ 和 $\mathbf{\Lambda}$：

    Construct $\mathbf{Q}$ and $\mathbf{\Lambda}$:

$$
    \mathbf{Q} = \begin{pmatrix}
    \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
    \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
    \end{pmatrix}, \quad \mathbf{\Lambda} = \begin{pmatrix}
    5 & 0 \\
    0 & 2
    \end{pmatrix}
    
$$

1. **计算 Rayleigh 商 Calculating Rayleigh Quotient**:
    对于任意向量 $\mathbf{x}$，可以将其表示为 $\mathbf{x} = \mathbf{Q} \mathbf{y}$。

    For any vector $\mathbf{x}$, it can be represented as $\mathbf{x} = \mathbf{Q} \mathbf{y}$.

    $$
    R(\mathbf{x}) = \frac{\mathbf{y}^\top \mathbf{\Lambda} \mathbf{y}}{\mathbf{y}^\top \mathbf{y}}


$$
    例如，当 $\mathbf{x} = \mathbf{q}_1$ 时，

    For example, when $\mathbf{x} = \mathbf{q}_1$,

    
$$

    R(\mathbf{x}) = \lambda_1 = 5
    

$$
    当 $\mathbf{x} = \mathbf{q}_2$ 时，

    When $\mathbf{x} = \mathbf{q}_2$,

    
$$

    R(\mathbf{x}) = \lambda_2 = 2
    

$$

通过特征值分解，可以将 Rayleigh 商的极值问题转化为寻找特征向量对应的特征值的问题。利用二次型和线性变换，可以更直观地理解 Rayleigh 商的计算过程。

By using eigenvalue decomposition, the problem of finding the extremum of the Rayleigh quotient can be transformed into finding the eigenvalues corresponding to the eigenvectors. Using quadratic forms and linear transformations provides a more intuitive understanding of the calculation process of the Rayleigh quotient.
