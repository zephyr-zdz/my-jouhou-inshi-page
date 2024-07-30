# Second-Order ODE | 二阶常微分方程

## Definition | 定义

A second-order ordinary differential equation (ODE) is a differential equation of the form:

二阶常微分方程的形式为：

$$
\mathbf{y}''(x) + p(x)\mathbf{y}'(x) + q(x)\mathbf{y}(x) = g(x)
$$

where $\mathbf{y}''(x)$ is the second derivative of $\mathbf{y}(x)$ with respect to $x$, $\mathbf{y}'(x)$ is the first derivative, $p(x)$ and $q(x)$ are given functions, and $g(x)$ is a known function.

其中 $\mathbf{y}''(x)$ 是 $\mathbf{y}(x)$ 对 $x$ 的二阶导数， $\mathbf{y}'(x)$ 是一阶导数， $p(x)$ 和 $q(x)$ 是已知函数， $g(x)$ 是已知函数。

## Types of Second-Order ODEs | 二阶常微分方程的类型

1. **Homogeneous Second-Order ODE | 齐次二阶常微分方程**

   If $g(x) = 0$, the ODE is called homogeneous:

   若 $g(x) = 0$，则该方程称为齐次方程：

   $$
   \mathbf{y}''(x) + p(x)\mathbf{y}'(x) + q(x)\mathbf{y}(x) = 0


$$
2. **Non-Homogeneous Second-Order ODE | 非齐次二阶常微分方程**

   If $g(x) \neq 0$, the ODE is called non-homogeneous:
   若 $g(x) \neq 0$，则该方程称为非齐次方程：
   
	
$$

	   \mathbf{y}''(x) + p(x)\mathbf{y}'(x) + q(x)\mathbf{y}(x) = g(x)
	
	$$

## Solution Methods | 解法

### 1. Homogeneous Equations | 齐次方程

For homogeneous second-order ODEs:

对于齐次二阶常微分方程：

$$
\mathbf{y}'' + p(x)\mathbf{y}' + q(x)\mathbf{y} = 0
$$

#### Characteristic Equation | 特征方程

1. Assume a solution of the form $\mathbf{y} = e^{\mathbf{r}x}$
   设解形式为 $\mathbf{y} = e^{\mathbf{r}x}$

2. Substitute $\mathbf{y}$ into the ODE to get the characteristic equation:
   将 $\mathbf{y}$ 代入方程得到特征方程：

$$
	
	\mathbf{r}^2 + p\mathbf{r} + q = 0
	
	
$$

3. Solve for $\mathbf{r}$:
   解 $\mathbf{r}$：
   - If $\mathbf{r}_1$ and $\mathbf{r}_2$ are real and distinct:
     若 $\mathbf{r}_1$ 和 $\mathbf{r}_2$ 为实且不同：

$$
	
	 \mathbf{y}(x) = C_1 e^{\mathbf{r}_1 x} + C_2 e^{\mathbf{r}_2 x}
	
	 
$$

   - If $\mathbf{r}_1 = \mathbf{r}_2 = \mathbf{r}$
    若 $\mathbf{r}_1 = \mathbf{r}_2 = \mathbf{r}$：

$$
	
	\mathbf{y}(x) = (C_1 + C_2 x)e^{\mathbf{r} x}
	
	
$$

   - If $\mathbf{r}_1$ and $\mathbf{r}_2$ are complex:
    若 $\mathbf{r}_1$ 和 $\mathbf{r}_2$ 为复数：

$$
	
	 \mathbf{r}_1, \mathbf{r}_2 = \alpha \pm \beta i = \alpha e^{\pm i\beta}
	 
	
$$

	$$
	
	 \mathbf{y}(x) = e^{\alpha x}(C_1 \cos(\beta x) + C_2 \sin(\beta x))
	
	$$

### 2. Non-Homogeneous Equations | 非齐次方程

For non-homogeneous second-order ODEs:

对于非齐次二阶常微分方程：

$$
\mathbf{y}'' + p(x)\mathbf{y}' + q(x)\mathbf{y} = g(x)
$$

#### Particular Solutions of Non-Homogeneous Second-Order ODEs | 非齐次二阶常微分方程的特解

When solving a non-homogeneous second-order ODE, the particular solution $\mathbf{y}_p(x)$ can be found using different methods depending on the form of $g(x)$. Here, we discuss some common approaches:

在求解非齐次二阶常微分方程时，特解 $\mathbf{y}_p(x)$ 的求法取决于 $g(x)$ 的形式。以下是一些常见的方法：

##### Method of Undetermined Coefficients | 未定系数法

This method is applicable when $g(x)$ is a polynomial, exponential function, sine or cosine, or a combination of these.

当 $g(x)$ 是多项式、指数函数、正弦或余弦函数，或这些的组合时，可以使用未定系数法。

###### Steps | 步骤

1. **Identify the form of $g(x)$** | 确定 $g(x)$ 的形式

$$
	g(x) = P(x)e^{\alpha x}\cos(\beta x) + Q(x)e^{\alpha x}\sin(\beta x)
	
	
$$

   where $P(x)$ and $Q(x)$ are polynomials.

   其中 $P(x)$ 和 $Q(x)$ 是多项式。

1. **Assume a particular solution $\mathbf{y}_p(x)$ with undetermined coefficients** | 假设具有未定系数的特解 $\mathbf{y}_p(x)$

   - For a polynomial $g(x) = ax^n + bx^{n-1} + \cdots + c$:

$$
	 \mathbf{y}_p(x) = A_n x^n + A_{n-1} x^{n-1} + \cdots + A_0
$$

   - For an exponential function $g(x) = e^{\alpha x}$:

$$
	 \mathbf{y}_p(x) = Ae^{\alpha x}
	
	
$$

   - For a sine or cosine function $g(x) = \cos(\beta x)$ or $g(x) = \sin(\beta x)$:

$$
	 \mathbf{y}_p(x) = A\cos(\beta x) + B\sin(\beta x)

	
$$

   - For a combination like $g(x) = P(x)e^{\alpha x}\cos(\beta x) + Q(x)e^{\alpha x}\sin(\beta x)$:

$$
	\mathbf{y}_p(x) = e^{\alpha x}(A\cos(\beta x) + B\sin(\beta x))

	
$$

1. **Substitute $\mathbf{y}_p(x)$ into the non-homogeneous ODE** | 将 $\mathbf{y}_p(x)$ 代入非齐次方程

2. **Solve for the undetermined coefficients** | 解出未定系数

###### Example | 示例

Given:

$$
\mathbf{y}'' - 3\mathbf{y}' + 2\mathbf{y} = 4e^{2x}
$$

Assume a particular solution:

$$
\mathbf{y}_p(x) = Ae^{2x}
$$

Substitute into the ODE:

$$
(4A - 6A + 2A)e^{2x} = 4e^{2x}
$$

$$
0 = 4e^{2x}
$$

Clearly, the assumption must be modified since it yields a contradiction. Instead, assume:

$$
\mathbf{y}_p(x) = Axe^{2x}
$$

Substitute and solve for $A$:

$$
(4Ax + 2A - 6Ax + 2Ax)e^{2x} = 4e^{2x}
$$

$$
2Ae^{2x} = 4e^{2x}
$$

$$
A = 2
$$

Thus, the particular solution is:

$$
\mathbf{y}_p(x) = 2xe^{2x}
$$

##### Variation of Parameters | 参数变换法

This method is applicable when $g(x)$ is not suitable for the method of undetermined coefficients, or when the form of $g(x)$ is more complicated.

当 $g(x)$ 不适用于未定系数法，或 $g(x)$ 的形式更复杂时，可以使用参数变换法。

###### Steps | 步骤

1. **Solve the corresponding homogeneous equation** | 解对应的齐次方程

$$
	 \mathbf{y}_h(x)'' + p(x)\mathbf{y}_h'(x) + q(x)\mathbf{y}_h(x) = 0
$$

1. **Find the fundamental solutions $\mathbf{y}_1(x)$ and $\mathbf{y}_2(x)$** | 找到基本解 $\mathbf{y}_1(x)$ 和 $\mathbf{y}_2(x)$

2. **Form the particular solution as** | 特解形式为

$$
	 \mathbf{y}_p(x) = \mathbf{y}_1(x)\mathbf{u}_1(x) + \mathbf{y}_2(x)\mathbf{u}_2(x)
	
	
	
$$

1. **Determine $\mathbf{u}_1(x)$ and $\mathbf{u}_2(x)$ by solving** | 通过解以下方程确定 $\mathbf{u}_1(x)$ 和 $\mathbf{u}_2(x)$

$$
	   \begin{cases}
	
	   \mathbf{y}_1(x)\mathbf{u}_1'(x) + \mathbf{y}_2(x)\mathbf{u}_2'(x) = 0 \\
	
	   \mathbf{y}_1'(x)\mathbf{u}_1'(x) + \mathbf{y}_2'(x)\mathbf{u}_2'(x) = g(x)
	
	   \end{cases}
$$

1. **Integrate to find $\mathbf{u}_1(x)$ and $\mathbf{u}_2(x)$** | 积分求 $\mathbf{u}_1(x)$ 和 $\mathbf{u}_2(x)$

$$
	   \mathbf{u}_1(x) = \int -\frac{\mathbf{y}_2(x)g(x)}{\mathbf{W}(\mathbf{y}_1, \mathbf{y}_2)} \, \mathrm{d}x
$$

$$
	   \mathbf{u}_2(x) = \int \frac{\mathbf{y}_1(x)g(x)}{\mathbf{W}(\mathbf{y}_1, \mathbf{y}_2)} \, \mathrm{d}x

、
$$

1. **Combine $\mathbf{u}_1(x)$ and $\mathbf{u}_2(x)$ with $\mathbf{y}_1(x)$ and $\mathbf{y}_2(x)$ to get $\mathbf{y}_p(x)$** | 将 $\mathbf{u}_1(x)$ 和 $\mathbf{u}_2(x)$ 与 $\mathbf{y}_1(x)$ 和 $\mathbf{y}_2(x)$ 结合得到 $\mathbf{y}_p(x)$

###### Example | 示例

Given:

$$
\mathbf{y}'' + \mathbf{y} = \tan(x)
$$

Solve the homogeneous equation:

$$
\mathbf{y}_h'' + \mathbf{y}_h = 0
$$

The fundamental solutions are:

$$
\mathbf{y}_1(x) = \cos(x), \quad \mathbf{y}_2(x) = \sin(x)
$$

Particular solution:

$$
\mathbf{y}_p(x) = \cos(x)\mathbf{u}_1(x) + \sin(x)\mathbf{u}_2(x)
$$

Determine $\mathbf{u}_1(x)$ and $\mathbf{u}_2(x)$:

$$
\begin{cases}

\cos(x)\mathbf{u}_1'(x) + \sin(x)\mathbf{u}_2'(x) = 0 \\

-\sin(x)\mathbf{u}_1'(x) + \cos(x)\mathbf{u}_2'(x) = \tan(x)

\end{cases}
$$

Solve for $\mathbf{u}_1'(x)$ and $\mathbf{u}_2'(x)$:

$$
\mathbf{u}_1'(x) = -\sin(x)\tan(x), \quad \mathbf{u}_2'(x) = \cos(x)\tan(x)
$$

Integrate to find $\mathbf{u}_1(x)$ and $\mathbf{u}_2(x)$:

$$
\mathbf{u}_1(x) = -\int \sin(x)\tan(x) \, \mathrm{d}x = -\int \sin(x)\frac{\sin(x)}{\cos(x)} \, \mathrm{d}x = -\int \frac{\sin^2(x)}{\cos(x)} \, \mathrm{d}x
$$

$$
\mathbf{u}_2(x) = \int \cos(x)\tan(x) \, \mathrm{d}x = \int \sin(x) \, \mathrm{d}x = -\cos(x)
$$

Thus, the particular solution is:

$$
\mathbf{y}_p(x) = \cos(x)(-\frac{1}{2}\ln|\cos(x)|) + \sin(x)(-\cos(x))
$$
