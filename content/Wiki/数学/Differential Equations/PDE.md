# 偏微分方程 (Partial Differential Equations, PDE)

## 定义 (Definition)

偏微分方程 (PDE) 是包含未知函数的偏导数的方程。它可以用来描述各种物理现象如热传导、波动、流体动力学等。

A Partial Differential Equation (PDE) is an equation that involves partial derivatives of an unknown function. It can be used to describe various physical phenomena such as heat conduction, waves, fluid dynamics, etc.

## 一阶偏微分方程 (First-Order PDE)

### 一般形式 (General Form)

一阶偏微分方程的一般形式为：

The general form of a first-order PDE is:

$$
F(x, y, u, u_x, u_y) = 0
$$

其中 $\mathbf{u} = u(x, y)$，$\mathbf{u_x} = \frac{\partial u}{\partial x}$，$\mathbf{u_y} = \frac{\partial u}{\partial y}$

where $\mathbf{u} = u(x, y)$, $\mathbf{u_x} = \frac{\partial u}{\partial x}$, $\mathbf{u_y} = \frac{\partial u}{\partial y}$

### 方法 (Methods)

1. **特征线法 (Method of Characteristics)**
   特征线法用于求解一阶线性和准线性偏微分方程。


   The method of characteristics is used to solve first-order linear and quasi-linear PDEs.


   **步骤 (Steps)**
   - 写出特征方程：$\frac{\mathrm{d}x}{a} = \frac{\mathrm{d}y}{b} = \frac{\mathrm{d}u}{c}$
   - 通过解特征方程得到特征线。
   - 将初始条件沿特征线延展，求解出 $\mathbf{u}$。

   Write the characteristic equations: $\frac{\mathrm{d}x}{a} = \frac{\mathrm{d}y}{b} = \frac{\mathrm{d}u}{c}$

   Solve the characteristic equations to get the characteristic curves.

   Extend the initial conditions along the characteristic curves to solve for $\mathbf{u}$.

## 二阶偏微分方程 (Second-Order PDE)

### 一般形式 (General Form)

二阶偏微分方程的一般形式为：

The general form of a second-order PDE is:

$$
A(x, y) \frac{\partial^2 u}{\partial x^2} + B(x, y) \frac{\partial^2 u}{\partial x \partial y} + C(x, y) \frac{\partial^2 u}{\partial y^2} + D(x, y, u, u_x, u_y) = 0
$$

其中 $\mathbf{u} = u(x, y)$

where $\mathbf{u} = u(x, y)$

### 分类 (Classification)

二阶偏微分方程可以根据系数 $A, B, C$ 的判别式进行分类：

Second-order PDEs can be classified based on the discriminant of the coefficients $A, B, C$:

$$
\Delta = B^2 - 4AC
$$

- **椭圆型 (Elliptic)**: $\Delta < 0$
- **双曲型 (Hyperbolic)**: $\Delta > 0$
- **抛物型 (Parabolic)**: $\Delta = 0$

### 经典方程 (Classical Equations)

1. **拉普拉斯方程 (Laplace's Equation)**

   $$

\Delta u = 0

$$
   其中 $\Delta = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}$ 为拉普拉斯算子。
   
   where $\Delta = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}$ is the Laplacian operator.

2. **热传导方程 (Heat Equation)**
   $$

u_t = \alpha \Delta u

$$
   其中 $u_t = \frac{\partial u}{\partial t}$，$\alpha$ 是热扩散系数。
   
   where $u_t = \frac{\partial u}{\partial t}$, $\alpha$ is the thermal diffusivity.

3. **波动方程 (Wave Equation)**
   $$

u_{tt} = c^2 \Delta u

$$
   其中 $u_{tt} = \frac{\partial^2 u}{\partial t^2}$，$c$ 是波速。
   
   where $u_{tt} = \frac{\partial^2 u}{\partial t^2}$, $c$ is the wave speed.

### 分离变量法 (Method of Separation of Variables)

**步骤 (Steps)**

1. 假设解为 $u(x, t) = X(x)T(t)$
2. 将 PDE 分离变量，得到两个 ODE。
3. 解两个 ODE，求得通解。
4. 应用边界条件和初始条件确定特解。

Assume the solution is $u(x, t) = X(x)T(t)$
Separate the variables to obtain two ODEs.
Solve the two ODEs to get the general solution.
Apply boundary conditions and initial conditions to determine the particular solution.

## 边界条件和初始条件 (Boundary and Initial Conditions)

### 边界条件 (Boundary Conditions)

1. **狄利克雷边界条件 (Dirichlet Boundary Condition)**: 给定函数在边界上的值。
2. **诺依曼边界条件 (Neumann Boundary Condition)**: 给定函数在边界上的法向导数值。
3. **罗宾边界条件 (Robin Boundary Condition)**: 给定函数值和法向导数值的线性组合。

Dirichlet Boundary Condition: Given the value of the function on the boundary.
Neumann Boundary Condition: Given the normal derivative of the function on the boundary.
Robin Boundary Condition: Given a linear combination of the function value and its normal derivative on the boundary.

### 初始条件 (Initial Conditions)

初始条件通常用于涉及时间的 PDE，描述初始时刻的函数值。

Initial conditions are usually used in time-involved PDEs to describe the function value at the initial moment.
