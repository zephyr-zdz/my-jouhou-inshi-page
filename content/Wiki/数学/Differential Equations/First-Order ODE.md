# 一阶常微分方程 (First-Order Ordinary Differential Equations)

## 定义 (Definition)

一阶常微分方程是只包含一个自变量及其一阶导数的方程。

A first-order ordinary differential equation is an equation that contains only one independent variable and its first derivative.

一般形式 (General form):

$F(x, y, \frac{dy}{dx}) = 0$ 或 (or) $\frac{dy}{dx} = f(x, y)$

其中 $y = y(x)$ 是未知函数，$x$ 是自变量。

Where $y = y(x)$ is the unknown function and $x$ is the independent variable.

## 主要类型 (Main Types)

### 1. 可分离变量方程 (Separable Equations)

定义 (Definition):

可以将方程改写成 $g(y)dy = h(x)dx$ 形式的方程。

Equations that can be rewritten in the form $g(y)dy = h(x)dx$.

解法 (Solution method):

1. 分离变量
   Separate the variables
2. 两边积分
   Integrate both sides
3. 解出 $y$
   Solve for $y$

例子 (Example):

$\frac{dy}{dx} = xy$

解 (Solution):

$$
\frac{dy}{y} = xdx
$$

$$
\int \frac{dy}{y} = \int xdx
$$

$$
\ln |y| = \frac{1}{2}x^2 + C
$$

$$
y = \pm e^{\frac{1}{2}x^2 + C} = Ce^{\frac{1}{2}x^2}
$$

### 2. 线性方程 (Linear Equations)

定义 (Definition):

形如 $\frac{dy}{dx} + P(x)y = Q(x)$ 的方程。

Equations of the form $\frac{dy}{dx} + P(x)y = Q(x)$.

解法 (Solution method):

1. 求积分因子 $\mu(x) = e^{\int P(x)dx}$
   Find the integrating factor $\mu(x) = e^{\int P(x)dx}$
2. 两边乘以积分因子
   Multiply both sides by the integrating factor
3. 整理并积分
   Simplify and integrate

详细步骤 (Detailed steps):

1. 将方程改写成 Rewrite the equation as

$$
\mu(x)\frac{dy}{dx} + \mu(x)P(x)y = y'e^{\int P(x)dx} + P(x)y = \mu(x)Q(x)
$$

1. 左边为 The left side becomes

$$
y'(e^{\int P(x)dx}) + (e^{\int P(x)dx})'y = (ye^{\int P(x)dx})'
$$

1. 解出 $\mu(x)y = \int \mu(x)Q(x)dx$
   Solve for $\mu(x)y = \int \mu(x)Q(x)dx$

例子 (Example):

$\frac{dy}{dx} + 2xy = x$

解 (Solution):

积分因子 (Integrating factor): $\mu(x) = e^{\int 2xdx} = e^{x^2}$

$$
e^{x^2}\frac{dy}{dx} + 2xe^{x^2}y = xe^{x^2}
$$

$$
\frac{d}{dx}(e^{x^2}y) = xe^{x^2}
$$

$$
e^{x^2}y = \int xe^{x^2}dx = \frac{1}{2}e^{x^2} + C
$$

$$
y = \frac{1}{2} + Ce^{-x^2}
$$

### 3. 伯努利方程 (Bernoulli Equations)

定义 (Definition):

形如 $\frac{dy}{dx} + P(x)y = Q(x)y^n$ 的方程，其中 $n \neq 0, 1$。

Equations of the form $\frac{dy}{dx} + P(x)y = Q(x)y^n$, where $n \neq 0, 1$.

解法 (Solution method):

1. 令 $v = y^{1-n}$，将方程转化为线性方程
   Let $v = y^{1-n}$, transform the equation into a linear equation
2. 解转化后的线性方程
   Solve the resulting linear equation
3. 代回 $y = v^{\frac{1}{1-n}}$ 得到原方程的解
   Substitute back $y = v^{\frac{1}{1-n}}$ to get the solution of the original equation

例子 (Example):

$\frac{dy}{dx} - 2xy = x^3y^3$

解 (Solution):

令 (Let) $v = y^{-2}$, $\frac{dv}{dx} = -2y^{-3}\frac{dy}{dx}$, 则 (Then) $y = v^{-\frac{1}{2}}$, $\frac{dy}{dx} = -\frac{1}{2}v^{-\frac{3}{2}}\frac{dv}{dx}$

$$
-\frac{1}{2}v^{-\frac{3}{2}}\frac{dv}{dx} - 2xv^{-\frac{1}{2}} = x^3v^3
$$

$$
\frac{dv}{dx} + 4xv = -2x^3
$$

这是一个线性方程，可以用上面的方法解决。

This is a linear equation that can be solved using the method above.

### 4. 精确方程 (Exact Equations)

定义 (Definition):

形如 $M(x,y)dx + N(x,y)dy = 0$ 的方程，其中 $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$。

Equations of the form $M(x,y)dx + N(x,y)dy = 0$, where $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$.

解法 (Solution method):

1. 验证方程是否为精确方程
   Verify if the equation is exact
2. 找到函数 $\phi(x,y)$ 使得 $\frac{\partial \phi}{\partial x} = M$ 和 $\frac{\partial \phi}{\partial y} = N$
   Find a function $\phi(x,y)$ such that $\frac{\partial \phi}{\partial x} = M$ and $\frac{\partial \phi}{\partial y} = N$
3. 解方程 $\phi(x,y) = C$
   Solve the equation $\phi(x,y) = C$

例子 (Example):

$(2xy + y^2)dx + (x^2 + 2xy)dy = 0$

解 (Solution):

验证 (Verify): $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} = 2x + 2y$

$$
\phi(x,y) = \int (2xy + y^2)dx = x^2y + xy^2 + f(y)
$$

$$
\frac{\partial \phi}{\partial y} = x^2 + 2xy + f'(y) = x^2 + 2xy
$$

因此 (Therefore), $f'(y) = 0$, $f(y) = C$

最终解 (Final solution): $x^2y + xy^2 = C$

注意事项 (Important notes):

- 识别方程类型是解题的关键第一步
  Identifying the equation type is the crucial first step in solving
- 有些方程可能需要先进行变量替换或其他转化才能归类
  Some equations may require variable substitution or other transformations before classification
- 在考试中，熟练应用这些方法可以大大提高解题效率
  In exams, proficiency in applying these methods can greatly improve solving efficiency
- 解的验证很重要，可以通过将解代入原方程来检查
  Solution verification is important, which can be done by substituting the solution back into the original equation
