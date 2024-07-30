# 经典二阶偏微分方程的解法 (Solutions to Classical Second-Order PDEs)

## 拉普拉斯方程 (Laplace's Equation)

### 定义 (Definition)

拉普拉斯方程的形式为：

The form of Laplace's Equation is:

$$
\Delta u = 0
$$

其中 $\Delta = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}$ 是拉普拉斯算子。

where $\Delta = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}$ is the Laplacian operator.

### 解法 (Solution Method)

**分离变量法 (Method of Separation of Variables)**

1. **假设解 (Assume the Solution)**

   假设解为 $u(x, y) = X(x)Y(y)$

   Assume the solution is $u(x, y) = X(x)Y(y)$

2. **分离变量 (Separate Variables)**

   将拉普拉斯方程代入假设解并分离变量：

   Substitute the assumed solution into Laplace's equation and separate variables:

   $$
   X''(x)Y(y) + X(x)Y''(y) = 0

$$

   除以 $X(x)Y(y)$ 并重排：

   Divide by $X(x)Y(y)$ and rearrange:

   $$

   \frac{X''(x)}{X(x)} = -\frac{Y''(y)}{Y(y)} = \lambda

$$

   这里 $\lambda$ 是分离常数。

   Here $\lambda$ is the separation constant.

3. **求解 ODE (Solve the ODEs)**

   得到两个常微分方程：

   Obtain two ordinary differential equations:

   $$

   X''(x) - \lambda X(x) = 0

$$

   $$

   Y''(y) + \lambda Y(y) = 0

$$

   根据 $\lambda$ 的值，解这些方程得到 $X(x)$ 和 $Y(y)$ 的通解。

   Solve these equations for $X(x)$ and $Y(y)$ depending on the value of $\lambda$ to get the general solutions.

4. **构造通解 (Construct the General Solution)**

   将 $X(x)$ 和 $Y(y)$ 的解结合起来，构造 $u(x, y)$ 的通解。

   Combine the solutions of $X(x)$ and $Y(y)$ to construct the general solution of $u(x, y)$.

5. **应用边界条件 (Apply Boundary Conditions)**

   使用边界条件确定特解。

   Use boundary conditions to determine the particular solution.

## 热传导方程 (Heat Equation)

### 定义 (Definition)
热传导方程的形式为：

The form of the Heat Equation is:

$$

u_t = \alpha \Delta u

$$

其中 $u_t = \frac{\partial u}{\partial t}$，$\alpha$ 是热扩散系数。

where $u_t = \frac{\partial u}{\partial t}$, $\alpha$ is the thermal diffusivity.

### 解法 (Solution Method)

**分离变量法 (Method of Separation of Variables)**

1. **假设解 (Assume the Solution)**

   假设解为 $u(x, t) = X(x)T(t)$

   Assume the solution is $u(x, t) = X(x)T(t)$

2. **分离变量 (Separate Variables)**

   将热传导方程代入假设解并分离变量：

   Substitute the assumed solution into the heat equation and separate variables:

   $$

   X(x)T'(t) = \alpha X''(x)T(t)

$$

   除以 $\alpha X(x)T(t)$ 并重排：

   Divide by $\alpha X(x)T(t)$ and rearrange:

   $$

   \frac{T'(t)}{\alpha T(t)} = \frac{X''(x)}{X(x)} = -\lambda

$$

   这里 $\lambda$ 是分离常数。

   Here $\lambda$ is the separation constant.

3. **求解 ODE (Solve the ODEs)**

   得到两个常微分方程：

   Obtain two ordinary differential equations:

   $$

   T'(t) + \alpha \lambda T(t) = 0

$$

   $$

   X''(x) + \lambda X(x) = 0

$$

   解这些方程得到 $X(x)$ 和 $T(t)$ 的通解。

   Solve these equations for $X(x)$ and $T(t)$ to get the general solutions.

4. **构造通解 (Construct the General Solution)**

   将 $X(x)$ 和 $T(t)$ 的解结合起来，构造 $u(x, t)$ 的通解。

   Combine the solutions of $X(x)$ and $T(t)$ to construct the general solution of $u(x, t)$.

5. **应用初始条件和边界条件 (Apply Initial and Boundary Conditions)**

   使用初始条件和边界条件确定特解。

   Use initial and boundary conditions to determine the particular solution.

## 波动方程 (Wave Equation)

### 定义 (Definition)
波动方程的形式为：

The form of the Wave Equation is:

$$

u_{tt} = c^2 \Delta u

$$

其中 $u_{tt} = \frac{\partial^2 u}{\partial t^2}$，$c$ 是波速。

where $u_{tt} = \frac{\partial^2 u}{\partial t^2}$, $c$ is the wave speed.

### 解法 (Solution Method)

**分离变量法 (Method of Separation of Variables)**

1. **假设解 (Assume the Solution)**

   假设解为 $u(x, t) = X(x)T(t)$

   Assume the solution is $u(x, t) = X(x)T(t)$

2. **分离变量 (Separate Variables)**

   将波动方程代入假设解并分离变量：

   Substitute the assumed solution into the wave equation and separate variables:

   $$

   X(x)T''(t) = c^2 X''(x)T(t)

$$

   除以 $c^2 X(x)T(t)$ 并重排：

   Divide by $c^2 X(x)T(t)$ and rearrange:

   $$

   \frac{T''(t)}{c^2 T(t)} = \frac{X''(x)}{X(x)} = -\lambda

$$

   这里 $\lambda$ 是分离常数。

   Here $\lambda$ is the separation constant.

3. **求解 ODE (Solve the ODEs)**

   得到两个常微分方程：

   Obtain two ordinary differential equations:

   $$

   T''(t) + c^2 \lambda T(t) = 0

$$

   $$

   X''(x) + \lambda X(x) = 0

$$

   解这些方程得到 $X(x)$ 和 $T(t)$ 的通解。

   Solve these equations for $X(x)$ and $T(t)$ to get the general solutions.

4. **构造通解 (Construct the General Solution)**

   将 $X(x)$ 和 $T(t)$ 的解结合起来，构造 $u(x, t)$ 的通解。

   Combine the solutions of $X(x)$ and $T(t)$ to construct the general solution of $u(x, t)$.

5. **应用初始条件和边界条件 (Apply Initial and Boundary Conditions)**

   使用初始条件和边界条件确定特解。

   Use initial and boundary conditions to determine the particular solution.

## 解法示例 (Example Solutions)

### 拉普拉斯方程示例 (Laplace's Equation Example)

#### 方程 (Equation)
求解以下拉普拉斯方程：

Solve the following Laplace's equation:

$$

\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0

$$

在矩形区域 $0 \leq x \leq a$ 和 $0 \leq y \leq b$，边界条件为：

In a rectangular region $0 \leq x \leq a$ and $0 \leq y \leq b$, with boundary conditions:

$$

u(0, y) = u(a, y) = 0, \quad u(x, 0) = 0, \quad u(x, b) = f(x)

$$

#### 解法 (Solution Method)

1. **假设解 (Assume the Solution)**

   假设解为 $u(x, y) = X(x)Y(y)$

   Assume the solution is $u(x, y) = X(x)Y(y)$

2. **分离变量 (Separate Variables)**

   将假设解代入拉普拉斯方程：

   Substitute the assumed solution into Laplace's equation:

   $$

   X''(x)Y(y) + X(x)Y''(y) = 0

$$

   除以 $X(x)Y(y)$ 并重排：

   Divide by $X(x)Y(y)$ and rearrange:

   $$

   \frac{X''(x)}{X(x)} = -\frac{Y''(y)}{Y(y)} = \lambda

$$

3. **求解 ODE (Solve the ODEs)**

   得到两个常微分方程：

   Obtain two ordinary differential equations:

   $$

   X''(x) + \lambda X(x) = 0

$$

   $$

   Y''(y) - \lambda Y(y) = 0

$$

   设 $\lambda = \left(\frac{n\pi}{a}\right)^2$，得到解：

   Assume $\lambda = \left(\frac{n\pi}{a}\right)^2$, obtain solutions:

   $$

   X_n(x) = \sin\left(\frac{n\pi x}{a}\right)

$$

   $$

   Y_n(y) = A_n \sinh\left(\frac{n\pi y}{a}\right)

$$

4. **构造通解 (Construct the General Solution)**

   结合边界条件 $u(x, 0) = 0$ 和 $u(x, b) = f(x)$，构造解：

   Combine with boundary conditions $u(x, 0) = 0$ and $u(x, b) = f(x)$, construct the solution:

   $$

   u(x, y) = \sum_{n=1}^{\infty} B_n \sin\left(\frac{n\pi x}{a}\right) \sinh\left(\frac{n\pi y}{a}\right)

$$

   利用傅里叶级数展开 $f(x)$ 来确定 $B_n$：

   Determine $B_n$ using Fourier series expansion of $f(x)$:

   $$

   f(x) = \sum_{n=1}^{\infty} B_n \sin\left(\frac{n\pi x}{a}\right)

$$

### 热传导方程示例 (Heat Equation Example)

#### 方程 (Equation)
求解以下热传导方程：

Solve the following heat equation:

$$

u_t = \alpha \frac{\partial^2 u}{\partial x^2}

$$

在区间 $0 \leq x \leq L$，初始条件和边界条件为：

In the interval $0 \leq x \leq L$, with initial and boundary conditions:

$$

u(x, 0) = f(x), \quad u(0, t) = u(L, t) = 0

$$

#### 解法 (Solution Method)

1. **假设解 (Assume the Solution)**

   假设解为 $u(x, t) = X(x)T(t)$

   Assume the solution is $u(x, t) = X(x)T(t)$

2. **分离变量 (Separate Variables)**

   将假设解代入热传导方程：

   Substitute the assumed solution into the heat equation:

   $$

   X(x)T'(t) = \alpha X''(x)T(t)

$$

   除以 $X(x)T(t)$ 并重排：

   Divide by $X(x)T(t)$ and rearrange:

   $$

   \frac{T'(t)}{\alpha T(t)} = \frac{X''(x)}{X(x)} = -\lambda

$$

3. **求解 ODE (Solve the ODEs)**

   得到两个常微分方程：

   Obtain two ordinary differential equations:

   $$

   T'(t) + \alpha \lambda T(t) = 0

$$

   $$

   X''(x) + \lambda X(x) = 0

$$

   设 $\lambda = \left(\frac{n\pi}{L}\right)^2$，得到解：

   Assume $\lambda = \left(\frac{n\pi}{L}\right)^2$, obtain solutions:

   $$

   X_n(x) = \sin\left(\frac{n\pi x}{L}\right)

$$

   $$

   T_n(t) = e^{-\alpha \left(\frac{n\pi}{L}\right)^2 t}

$$

4. **构造通解 (Construct the General Solution)**

   结合初始条件 $u(x, 0) = f(x)$，构造解：

   Combine with initial condition $u(x, 0) = f(x)$, construct the solution:

   $$

   u(x, t) = \sum_{n=1}^{\infty} B_n \sin\left(\frac{n\pi x}{L}\right) e^{-\alpha \left(\frac{n\pi}{L}\right)^2 t}

$$

   利用傅里叶级数展开 $f(x)$ 来确定 $B_n$：

   Determine $B_n$ using Fourier series expansion of $f(x)$:

   $$

   f(x) = \sum_{n=1}^{\infty} B_n \sin\left(\frac{n\pi x}{L}\right)

$$

### 波动方程示例 (Wave Equation Example)

#### 方程 (Equation)
求解以下波动方程：

Solve the following wave equation:

$$

u_{tt} = c^2 \frac{\partial^2 u}{\partial x^2}

$$

在区间 $0 \leq x \leq L$，初始条件和边界条件为：

In the interval $0 \leq x \leq L$, with initial and boundary conditions:

$$

u(x, 0) = f(x), \quad u_t(x, 0) = g(x), \quad u(0, t) = u(L, t) = 0

$$

#### 解法 (Solution Method)

1. **假设解 (Assume the Solution)**

   假设解为 $u(x, t) = X(x)T(t)$

   Assume the solution is $u(x, t) = X(x)T(t)$

2. **分离变量 (Separate Variables)**

   将假设解代入波动方程：

   Substitute the assumed solution into the wave equation:

   $$

   X(x)T''(t) = c^2 X''(x)T(t)

$$

   除以 $c^2 X(x)T(t)$ 并重排：

   Divide by $c^2 X(x)T(t)$ and rearrange:

   $$

   \frac{T''(t)}{c^2 T(t)} = \frac{X''(x)}{X(x)} = -\lambda

$$

3. **求解 ODE (Solve the ODEs)**

   得到两个常微分方程：

   Obtain two ordinary differential equations:

   $$

   T''(t) + c^2 \lambda T(t) = 0

$$

   $$

   X''(x) + \lambda X(x) = 0

$$

   设 $\lambda = \left(\frac{n\pi}{L}\right)^2$，得到解：

   Assume $\lambda = \left(\frac{n\pi}{L}\right)^2$, obtain solutions:

   $$

   X_n(x) = \sin\left(\frac{n\pi x}{L}\right)

$$

   $$

   T_n(t) = A_n \cos\left(\frac{n\pi c t}{L}\right) + B_n \sin\left(\frac{n\pi c t}{L}\right)

$$

4. **构造通解 (Construct the General Solution)**

   结合初始条件 $u(x, 0) = f(x)$ 和 $u_t(x, 0) = g(x)$，构造解：

   Combine with initial conditions $u(x, 0) = f(x)$ and $u_t(x, 0) = g(x)$, construct the solution:

   $$

   u(x, t) = \sum_{n=1}^{\infty} \left[ A_n \cos\left(\frac{n\pi c t}{L}\right) + B_n \sin\left(\frac{n\pi c t}{L}\right) \right] \sin\left(\frac{n\pi x}{L}\right)

$$

   利用傅里叶级数展开 $f(x)$ 和 $g(x)$ 来确定 $A_n$ 和 $B_n$：

   Determine $A_n$ and $B_n$ using Fourier series expansion of $f(x)$ and $g(x)$:

   $$

   f(x) = \sum_{n=1}^{\infty} A_n \sin\left(\frac{n\pi x}{L}\right)

$$

   $$

   g(x) = \sum_{n=1}^{\infty} \frac{n\pi c}{L} B_n \sin\left(\frac{n\pi x}{L}\right)

$$
