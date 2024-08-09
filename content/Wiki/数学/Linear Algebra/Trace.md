# 矩阵的迹 / Matrix Trace

## 定义 / Definition

**迹（trace）**: 一个方阵 $\mathbf{A}$ 的迹是其对角线元素之和，用 $\mathrm{tr}(\mathbf{A})$ 表示
**Trace**: The trace of a square matrix $\mathbf{A}$ is the sum of its diagonal elements, denoted as $\mathrm{tr}(\mathbf{A})$

$$
\mathrm{tr}(\mathbf{A}) = \sum_{i=1}^{n} a_{ii}
$$

其中，$a_{ii}$ 表示矩阵 $\mathbf{A}$ 的第 $i$ 个对角线元素

where $a_{ii}$ represents the $i$-th diagonal element of matrix $\mathbf{A}$

## 迹的性质 / Properties of Trace

1. **线性性 / Linearity**

若 $\mathbf{A}$ 和 $\mathbf{B}$ 是两个 $n \times n$ 矩阵，且 $c$ 是一个标量，则

If $\mathbf{A}$ and $\mathbf{B}$ are two $n \times n$ matrices, and $c$ is a scalar, then

$$
\mathrm{tr}(\mathbf{A} + \mathbf{B}) = \mathrm{tr}(\mathbf{A}) + \mathrm{tr}(\mathbf{B})
$$

$$
\mathrm{tr}(c\mathbf{A}) = c \cdot \mathrm{tr}(\mathbf{A})
$$

2. **迹的相似不变性 / Invariance under Similarity**

如果 $\mathbf{A}$ 和 $\mathbf{B}$ 是相似矩阵，即存在可逆矩阵 $\mathbf{P}$ 使得 $\mathbf{B} = \mathbf{P}^{-1} \mathbf{A} \mathbf{P}$，则

If $\mathbf{A}$ and $\mathbf{B}$ are similar matrices, i.e., there exists an invertible matrix $\mathbf{P}$ such that $\mathbf{B} = \mathbf{P}^{-1} \mathbf{A} \mathbf{P}$, then

$$
\mathrm{tr}(\mathbf{A}) = \mathrm{tr}(\mathbf{B})
$$

3. **迹与转置矩阵 / Trace and Transpose Matrix**

对于任意矩阵 $\mathbf{A}$，其转置矩阵 $\mathbf{A}^\mathrm{T}$ 的迹与其本身相等，即

For any matrix $\mathbf{A}$, the trace of its transpose $\mathbf{A}^\mathrm{T}$ is equal to its own trace, i.e.,

$$
\mathrm{tr}(\mathbf{A}) = \mathrm{tr}(\mathbf{A}^\mathrm{T})
$$

4. **迹与矩阵乘积 / Trace and Matrix Product**

对于任意 $n \times n$ 矩阵 $\mathbf{A}$ 和 $\mathbf{B}$，有

For any $n \times n$ matrices $\mathbf{A}$ and $\mathbf{B}$, we have

$$
\mathrm{tr}(\mathbf{A} \mathbf{B}) = \mathrm{tr}(\mathbf{B} \mathbf{A})
$$

这个性质可以推广到多个矩阵的乘积，即

This property can be generalized to the product of multiple matrices, i.e.,

$$
\mathrm{tr}(\mathbf{A} \mathbf{B} \mathbf{C}) = \mathrm{tr}(\mathbf{C} \mathbf{A} \mathbf{B}) = \mathrm{tr}(\mathbf{B} \mathbf{C} \mathbf{A})
$$

5. **迹与特征值 / Trace and Eigenvalues**

对于一个 $n \times n$ 矩阵 $\mathbf{A}$，其特征值 $\lambda_1, \lambda_2, \ldots, \lambda_n$ 的和等于其迹

For an $n \times n$ matrix $\mathbf{A}$, the sum of its eigenvalues $\lambda_1, \lambda_2, \ldots, \lambda_n$ equals its trace

$$
\mathrm{tr}(\mathbf{A}) = \sum_{i=1}^{n} \lambda_i
$$

6. **迹的迹（trace of the trace）/ Trace of the Trace**

若 $\mathbf{A}$ 是一个 $n \times n$ 方阵，则

If $\mathbf{A}$ is an $n \times n$ square matrix, then

$$
\mathrm{tr}(\mathrm{tr}(\mathbf{A})) = \mathrm{tr}(\mathbf{A})
$$

## 证明 / Proofs

### 迹的相似不变性 / Invariance under Similarity

如果 $\mathbf{A}$ 和 $\mathbf{B}$ 是相似矩阵，即存在可逆矩阵 $\mathbf{P}$ 使得 $\mathbf{B} = \mathbf{P}^{-1} \mathbf{A} \mathbf{P}$，则

If $\mathbf{A}$ and $\mathbf{B}$ are similar matrices, i.e., there exists an invertible matrix $\mathbf{P}$ such that $\mathbf{B} = \mathbf{P}^{-1} \mathbf{A} \mathbf{P}$, then

计算 $\mathbf{B}$ 的迹

Compute the trace of $\mathbf{B}$

$$
\mathrm{tr}(\mathbf{B}) = \mathrm{tr}(\mathbf{P}^{-1} \mathbf{A} \mathbf{P})
$$

利用迹的性质 $\mathrm{tr}(\mathbf{X} \mathbf{Y}) = \mathrm{tr}(\mathbf{Y} \mathbf{X})$

Using the property of trace $\mathrm{tr}(\mathbf{X} \mathbf{Y}) = \mathrm{tr}(\mathbf{Y} \mathbf{X})$

$$
\mathrm{tr}(\mathbf{P}^{-1} \mathbf{A} \mathbf{P}) = \mathrm{tr}(\mathbf{A} \mathbf{P} \mathbf{P}^{-1}) = \mathrm{tr}(\mathbf{A})
$$

因此，相似矩阵的迹相等

Therefore, the trace of similar matrices is equal

### 迹与特征值的和 / Trace and Sum of Eigenvalues

设 $\mathbf{A}$ 是一个 $n \times n$ 方阵，$\lambda_1, \lambda_2, \ldots, \lambda_n$ 是 $\mathbf{A}$ 的特征值

Let $\mathbf{A}$ be an $n \times n$ square matrix, and $\lambda_1, \lambda_2, \ldots, \lambda_n$ be the eigenvalues of $\mathbf{A}$

根据特征多项式 $\mathrm{det}(\mathbf{A} - \lambda \mathbf{I}) = 0$，我们知道 $\mathbf{A}$ 的特征值是 $\mathbf{A}$ 的特征多项式的根

According to the characteristic polynomial $\mathrm{det}(\mathbf{A} - \lambda \mathbf{I}) = 0$, we know that the eigenvalues of $\mathbf{A}$ are the roots of the characteristic polynomial of $\mathbf{A}$

特征多项式可以表示为

The characteristic polynomial can be written as

$$
\mathrm{det}(\mathbf{A} - \lambda \mathbf{I}) = (-1)^n (\lambda^n - (\mathrm{tr}(\mathbf{A})) \lambda^{n-1} + \cdots + \mathrm{det}(\mathbf{A}))
$$

其中，$\mathrm{tr}(\mathbf{A})$ 是 $\mathbf{A}$ 的迹，表示 $\mathbf{A}$ 的特征值之和

where $\mathrm{tr}(\mathbf{A})$ is the trace of $\mathbf{A}$, representing the sum of the eigenvalues of $\mathbf{A}$

### 结论 / Conclusion

$$
\mathrm{tr}(\mathbf{A}) = \sum_{i=1}^{n} a_{ii} = \sum_{i=1}^{n} \lambda_i
$$

迹是矩阵的重要性质之一，等于对角线元素的和，也等于特征值的和

Trace is one of the important properties of a matrix, equal to the sum of the diagonal elements and the sum of the eigenvalues

## Derivatives Involving Trace / 迹相关的导数

1. **$\frac{\partial}{\partial \mathbf{A}} \mathrm{tr}(\mathbf{A}\mathbf{X}) = \mathbf{X}^T$**

   When differentiating the trace of the product of matrices $\mathbf{A}$ and $\mathbf{X}$, with respect to $\mathbf{A}$, the result is the transpose of $\mathbf{X}$.

   对 $\mathrm{tr}(\mathbf{A}\mathbf{X})$ 关于 $\mathbf{A}$ 求导时，结果为 $\mathbf{X}$ 的转置。

2. **$\frac{\partial}{\partial \mathbf{A}} \mathrm{tr}(\mathbf{X}\mathbf{A}^T) = \mathbf{X}$**

   Differentiating the trace of the product of $\mathbf{X}$ and $\mathbf{A}^T$ with respect to $\mathbf{A}$ results in $\mathbf{X}$.

   对 $\mathrm{tr}(\mathbf{X}\mathbf{A}^T)$ 关于 $\mathbf{A}$ 求导时，结果为 $\mathbf{X}$。

3. **$\frac{\partial}{\partial \mathbf{A}} \mathrm{tr}(\mathbf{A}\mathbf{X}\mathbf{A}^T) = \mathbf{A}(\mathbf{X} + \mathbf{X}^T)$**

   When differentiating the trace of $\mathbf{A}\mathbf{X}\mathbf{A}^T$ with respect to $\mathbf{A}$, the result is $\mathbf{A}$ multiplied by the sum of $\mathbf{X}$ and its transpose.

   对 $\mathrm{tr}(\mathbf{A}\mathbf{X}\mathbf{A}^T)$ 关于 $\mathbf{A}$ 求导时，结果为 $\mathbf{A}$ 乘以 $\mathbf{X}$ 和其转置之和。

## Additional Notes / 额外说明

- The trace of a matrix is invariant under cyclic permutations, which can often simplify expressions and calculations. For example, in certain optimization problems, the cyclic property can be used to manipulate the objective function.
- 矩阵的迹在循环置换下不变，这通常可以简化表达式和计算。例如，在某些优化问题中，循环性质可用于操作目标函数。

This overview covers the basic concepts and properties of matrix trace and its derivatives, which are essential tools in various fields such as machine learning, statistics, and applied mathematics. 这份概述涵盖了矩阵迹及其导数的基本概念和性质，这些是机器学习、统计学和应用数学等领域的重要工具。
