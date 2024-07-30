# 多元微分 Multivariable Differential

## 概念与定义 Concepts and Definitions

### 二元函数 Bivariate Function

一个二元函数是指有两个自变量的函数，形式为 $f(x, y)$。自变量 $x$ 和 $y$ 分别属于实数集 $\mathbb{R}$ 的子集，函数值 $f(x, y)$ 属于实数集 $\mathbb{R}$

A bivariate function refers to a function with two variables, in the form of $f(x, y)$. The variables $x$ and $y$ belong to subsets of the real numbers $\mathbb{R}$, and the function value $f(x, y)$ belongs to the real numbers $\mathbb{R}$

### 极限 Limits

设 $f(x, y)$ 为定义在区域 $D \subset \mathbb{R}^2$ 上的函数。如果存在实数 $L$ 使得当 $(x, y)$ 充分接近点 $(a, b)$ 时，$f(x, y)$ 的值无限接近 $L$，则称 $L$ 为 $f(x, y)$ 在 $(a, b)$ 处的极限，记作：

$$
\lim_{{(x, y) \to (a, b)}} f(x, y) = L
$$

Let $f(x, y)$ be a function defined on a region $D \subset \mathbb{R}^2$. If there exists a real number $L$ such that as $(x, y)$ approaches the point $(a, b)$, the value of $f(x, y)$ approaches $L$, then $L$ is called the limit of $f(x, y)$ at $(a, b)$, denoted as:

$$
\lim_{{(x, y) \to (a, b)}} f(x, y) = L
$$

### 连续性 Continuity

若 $f(x, y)$ 在点 $(a, b)$ 处有定义，且满足以下条件：

$$
\lim_{{(x, y) \to (a, b)}} f(x, y) = f(a, b)
$$

则称 $f(x, y)$ 在点 $(a, b)$ 处连续

If $f(x, y)$ is defined at the point $(a, b)$ and satisfies the following condition:

$$
\lim_{{(x, y) \to (a, b)}} f(x, y) = f(a, b)
$$

then $f(x, y)$ is continuous at the point $(a, b)$

### 偏导数 Partial Derivatives

二元函数 $f(x, y)$ 在点 $(a, b)$ 处对 $x$ 的偏导数定义为：

$$
f_x(a, b) = \lim_{{h \to 0}} \frac{f(a+h, b) - f(a, b)}{h}
$$

对 $y$ 的偏导数定义为：

$$
f_y(a, b) = \lim_{{h \to 0}} \frac{f(a, b+h) - f(a, b)}{h}
$$

The partial derivative of a bivariate function $f(x, y)$ at the point $(a, b)$ with respect to $x$ is defined as:

$$
f_x(a, b) = \lim_{{h \to 0}} \frac{f(a+h, b) - f(a, b)}{h}
$$

The partial derivative with respect to $y$ is defined as:

$$
f_y(a, b) = \lim_{{h \to 0}} \frac{f(a, b+h) - f(a, b)}{h}
$$

## 性质与定理 Properties and Theorems

### 可微性 Differentiability

若 $f(x, y)$ 在点 $(a, b)$ 处连续，并且存在常数 $A$ 和 $B$ 使得：

$$
f(a+h, b+k) - f(a, b) = Ah + Bk + o(\sqrt{h^2 + k^2})
$$

则称 $f(x, y)$ 在点 $(a, b)$ 处可微

If $f(x, y)$ is continuous at the point $(a, b)$, and there exist constants $A$ and $B$ such that:

$$
f(a+h, b+k) - f(a, b) = Ah + Bk + o(\sqrt{h^2 + k^2})
$$

then $f(x, y)$ is differentiable at the point $(a, b)$

### 混合偏导数 Mixed Partial Derivatives

若函数 $f(x, y)$ 的二阶偏导数连续，即 $f_{xy} = f_{yx}$，则称 $f(x, y)$ 的混合偏导数连续

If the second-order partial derivatives of the function $f(x, y)$ are continuous, i.e., $f_{xy} = f_{yx}$, then the mixed partial derivatives of $f(x, y)$ are continuous

### 泰勒展开 Taylor Expansion

若 $f(x, y)$ 在点 $(a, b)$ 处有二阶连续偏导数，则可以展开为泰勒级数形式：

$$
f(x, y) \approx f(a, b) + f_x(a, b)(x - a) + f_y(a, b)(y - b) + \frac{1}{2}[f_{xx}(a, b)(x - a)^2 + 2f_{xy}(a, b)(x - a)(y - b) + f_{yy}(a, b)(y - b)^2]
$$

If $f(x, y)$ has second-order continuous partial derivatives at the point $(a, b)$, it can be expanded in the form of a Taylor series:

$$
f(x, y) \approx f(a, b) + f_x(a, b)(x - a) + f_y(a, b)(y - b) + \frac{1}{2}[f_{xx}(a, b)(x - a)^2 + 2f_{xy}(a, b)(x - a)(y - b) + f_{yy}(a, b)(y - b)^2]
$$

## 计算技巧 Calculation Techniques

### 链式法则 Chain Rule

如果 $z = f(x, y)$，且 $x = g(t), y = h(t)$，则 $z$ 对 $t$ 的导数为：

$$
\frac{dz}{dt} = \frac{\partial f}{\partial x} \frac{dx}{dt} + \frac{\partial f}{\partial y} \frac{dy}{dt}
$$

If $z = f(x, y)$, and $x = g(t), y = h(t)$, then the derivative of $z$ with respect to $t$ is:

$$
\frac{dz}{dt} = \frac{\partial f}{\partial x} \frac{dx}{dt} + \frac{\partial f}{\partial y} \frac{dy}{dt}
$$

### 方向导数 Directional Derivative

在方向 $\mathbf{u} = (u_1, u_2)$ 上，函数 $f(x, y)$ 在点 $(a, b)$ 处的方向导数定义为：

$$
D_{\mathbf{u}} f(a, b) = f_x(a, b)u_1 + f_y(a, b)u_2
$$

In the direction $\mathbf{u} = (u_1, u_2)$, the directional derivative of the function $f(x, y)$ at the point $(a, b)$ is defined as:

$$
D_{\mathbf{u}} f(a, b) = f_x(a, b)u_1 + f_y(a, b)u_2
$$

### 梯度 Gradient

函数 $f(x, y)$ 在点 $(a, b)$ 处的梯度为：

$$
\nabla f(a, b) = \left( f_x(a, b), f_y(a, b) \right)
$$

The gradient of the function $f(x, y)$ at the point $(a, b)$ is:

$$
\nabla f(a, b) = \left( f_x(a, b), f_y(a, b) \right)
$$

### 拉普拉斯算子 Laplacian

拉普拉斯算子用于描述函数的二阶导数和，定义为：

$$
\Delta f = f_{xx} + f_{yy}
$$

The Laplacian operator is used to describe the sum of the second-order derivatives of a function, defined as:

$$
\Delta f = f_{xx} + f_{yy}
$$

### 例题 Examples

#### 例 1 Example 1

求函数 $f(x, y) = x^2 + y^2$ 在点 $(1, 2)$ 处的梯度

Calculate the gradient of the function $f(x, y) = x^2 + y^2$ at the point $(1, 2)$

解：

$$
f_x(x, y) = 2x \\
f_y(x, y) = 2y \\
\nabla f(1, 2) = \left( 2 \cdot 1, 2 \cd

ot 2 \right) = (2, 4)
$$

Solution:

$$
f_x(x, y) = 2x \\
f_y(x, y) = 2y \\
\nabla f(1, 2) = \left( 2 \cdot 1, 2 \cdot 2 \right) = (2, 4)
$$

#### 例 2 Example 2

计算 $z = x^2y + y^3$ 当 $x = \cos(t)$ 且 $y = \sin(t)$ 时的 $\frac{dz}{dt}$

Calculate $\frac{dz}{dt}$ for $z = x^2y + y^3$ when $x = \cos(t)$ and $y = \sin(t)$

解：

$$
\frac{\partial z}{\partial x} = 2xy \\
\frac{\partial z}{\partial y} = x^2 + 3y^2 \\
\frac{dx}{dt} = -\sin(t) \\
\frac{dy}{dt} = \cos(t) \\
\frac{dz}{dt} = \frac{\partial z}{\partial x} \frac{dx}{dt} + \frac{\partial z}{\partial y} \frac{dy}{dt} \\
= (2xy)(-\sin(t)) + (x^2 + 3y^2)(\cos(t)) \\
= (2 \cos(t) \sin(t))(-\sin(t)) + (\cos^2(t) + 3 \sin^2(t))(\cos(t))
$$

Solution:

$$
\frac{\partial z}{\partial x} = 2xy \\
\frac{\partial z}{\partial y} = x^2 + 3y^2 \\
\frac{dx}{dt} = -\sin(t) \\
\frac{dy}{dt} = \cos(t) \\
\frac{dz}{dt} = \frac{\partial z}{\partial x} \frac{dx}{dt} + \frac{\partial z}{\partial y} \frac{dy}{dt} \\
= (2xy)(-\sin(t)) + (x^2 + 3y^2)(\cos(t)) \\
= (2 \cos(t) \sin(t))(-\sin(t)) + (\cos^2(t) + 3 \sin^2(t))(\cos(t))
$$
