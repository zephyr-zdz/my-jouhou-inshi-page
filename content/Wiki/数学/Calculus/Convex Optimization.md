# 凸函数优化 Convex Optimization

## 凸函数 (Convex Function)

### 定义 (Definition)

一个函数 $f: \mathbb{R}^n \to \mathbb{R}$ 是凸的，如果对于所有 $x, y \in \mathbb{R}^n$ 和 $\lambda \in [0, 1]$，满足

A function $f: \mathbb{R}^n \to \mathbb{R}$ is convex if for all $x, y \in \mathbb{R}^n$ and $\lambda \in [0, 1]$, the following holds:

$$
f(\lambda x + (1 - \lambda) y) \leq \lambda f(x) + (1 - \lambda) f(y)
$$

### 一阶条件 (First-order Condition)

一个可微函数 $f$ 是凸的，当且仅当对所有 $x, y \in \mathbb{R}^n$，满足

A differentiable function $f$ is convex if and only if for all $x, y \in \mathbb{R}^n$, the following holds:

$$
f(y) \geq f(x) + \nabla f(x)^T (y - x)
$$

其中 $\nabla f(x)$ 是 $f$ 在 $x$ 处的梯度向量

where $\nabla f(x)$ is the gradient vector of $f$ at $x$

### 二阶条件 (Second-order Condition)

一个两次可微函数 $f$ 是凸的，当且仅当对于所有 $x \in \mathbb{R}^n$，Hessian 矩阵 $\nabla^2 f(x)$ 半正定

A twice-differentiable function $f$ is convex if and only if for all $x \in \mathbb{R}^n$, the Hessian matrix $\nabla^2 f(x)$ is positive semidefinite

## Hessian 矩阵 (Hessian Matrix)

### 定义 (Definition)

Hessian 矩阵是由函数 $f$ 的所有二阶偏导数组成的方阵，记作 $\nabla^2 f(x)$

The Hessian matrix is a square matrix of second-order partial derivatives of a function $f$, denoted as $\nabla^2 f(x)$

$$
\begin{equation}
\nabla^2 f(x) = \begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}
\end{equation}
$$

### 性质 (Properties)

1. 对称性：如果 $f$ 二次可微，则 Hessian 矩阵 $\nabla^2 f(x)$ 是对称的
Symmetry: If $f$ is twice differentiable, then the Hessian matrix $\nabla^2 f(x)$ is symmetric
2. 半正定性：如果 $f$ 是凸函数，则 $\nabla^2 f(x)$ 是半正定的
Positive semidefiniteness: If $f$ is a convex function, then $\nabla^2 f(x)$ is positive semidefinite

## 矩阵求导 (Matrix Calculus)

### 梯度 (Gradient)

向量 $x \in \mathbb{R}^n$ 的函数 $f(x)$ 的梯度是一个包含所有偏导数的列向量

The gradient of a function $f(x)$ with respect to a vector $x \in \mathbb{R}^n$ is a column vector containing all partial derivatives

$$
\nabla f(x) = \begin{bmatrix}
\frac{\partial f}{\partial x_1} \\
\frac{\partial f}{\partial x_2} \\
\vdots \\
\frac{\partial f}{\partial x_n}
\end{bmatrix}
$$

### 雅可比矩阵 (Jacobian Matrix)

向量值函数 $\mathbf{f}: \mathbb{R}^n \to \mathbb{R}^m$ 的雅可比矩阵是一个 $m \times n$ 的矩阵，包含所有一阶偏导数

The Jacobian matrix of a vector-valued function $\mathbf{f}: \mathbb{R}^n \to \mathbb{R}^m$ is an $m \times n$ matrix containing all first-order partial derivatives

$$
J_{\mathbf{f}} = \begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \cdots & \frac{\partial f_1}{\partial x_n} \\
\frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \cdots & \frac{\partial f_2}{\partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial f_m}{\partial x_1} & \frac{\partial f_m}{\partial x_2} & \cdots & \frac{\partial f_m}{\partial x_n}
\end{bmatrix}
$$

### 矩阵的导数 (Derivatives of Matrices)

如果 $A$ 是一个 $m \times n$ 的常数矩阵，$x \in \mathbb{R}^n$ 是一个变量向量，则 $Ax$ 对 $x$ 的导数是 $A$

If $A$ is an $m \times n$ constant matrix and $x \in \mathbb{R}^n$ is a variable vector, then the derivative of $Ax$ with respect to $x$ is $A$

$$
\frac{\partial (Ax)}{\partial x} = A
$$

## 矩阵和向量求导法则 (Rules for Matrix and Vector Derivatives)

### 矩阵求导法则 (Matrix Derivative Rules)

1. 对于标量函数 $f(x)$，$x \in \mathbb{R}^n$，梯度 $\nabla f(x)$ 是一个列向量
For a scalar function $f(x)$, $x \in \mathbb{R}^n$, the gradient $\nabla f(x)$ is a column vector

$$
\nabla f(x) = \begin{bmatrix}
\frac{\partial f}{\partial x_1} \\
\frac{\partial f}{\partial x_2} \\
\vdots \\
\frac{\partial f}{\partial x_n}
\end{bmatrix}
$$

2. 对于矩阵 $A \in \mathbb{R}^{m \times n}$ 和向量 $x \in \mathbb{R}^n$，$Ax$ 对 $x$ 的导数是 $A$
For a matrix $A \in \mathbb{R}^{m \times n}$ and a vector $x \in \mathbb{R}^n$, the derivative of $Ax$ with respect to $x$ is $A$

$$
\frac{\partial (Ax)}{\partial x} = A
$$

3. 对于矩阵 $A \in \mathbb{R}^{n \times n}$ 和向量 $x \in \mathbb{R}^n$，$x^T A x$ 对 $x$ 的导数是 $2Ax$
For a matrix $A \in \mathbb{R}^{n \times n}$ and a vector $x \in \mathbb{R}^n$, the derivative of $x^T A x$ with respect to $x$ is $2Ax$

$$
\frac{\partial (x^T A x)}{\partial x} = 2Ax
$$

4. 对于标量函数 $f(Ax)$，其中 $f: \mathbb{R}^m \to \mathbb{R}$ 和 $A \in \mathbb{R}^{m \times n}$，导数是 $A^T \nabla f(Ax)$
For a scalar function $f(Ax)$, where $f: \mathbb{R}^m \to \mathbb{R}$ and $A \in \mathbb{R}^{m \times n}$, the derivative is $A^T \nabla f(Ax)$

$$
\frac{\partial f(Ax)}{\partial x} = A^T \nabla f(Ax)
$$
