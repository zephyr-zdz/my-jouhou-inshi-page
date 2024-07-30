# 微分方程 Differential Equations, DE

## 基本概念和分类 Basic Concepts and Classification

### 微分方程的定义 Definition of Differential Equations

微分方程是一个包含未知函数及其导数的方程。

A differential equation is an equation that contains an unknown function and its derivatives.

数学表示：

Mathematical representation:

$f(x, y, y', y'', …, y^{(n)}) = 0$

其中 $y = y(x)$ 是未知函数，$y', y'', …, y^{(n)}$ 是 $y$ 的各阶导数。

Where $y = y(x)$ is the unknown function, and $y', y'', …, y^{(n)}$ are the derivatives of $y$ of various orders.

重要性：

Importance:

1. 在数学中建立函数关系
   Establish functional relationships in mathematics
2. 描述物理、工程、经济等领域的动态系统
   Describe dynamic systems in physics, engineering, economics, etc.
3. 预测和模拟复杂系统的行为
   Predict and simulate the behavior of complex systems

### 微分方程的分类 Classification of Differential Equations

1. 按未知函数的自变量数目分类：
   Classification based on the number of independent variables of the unknown function:

   a) 常微分方程 (Ordinary Differential Equations, ODE)：

      只包含一个自变量的导数

      Contains derivatives with respect to only one independent variable

      例如 (Example): $\frac{dy}{dx} + 2y = x$

   b) 偏微分方程 (Partial Differential Equations, PDE)：

      包含多个自变量的偏导数

      Contains partial derivatives with respect to multiple independent variables

      例如 (Example): $\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$

2. 按最高阶导数分类：
   Classification based on the highest order of derivatives:

   a) 一阶微分方程 (First-order Differential Equations)：

      最高阶导数为一阶

      The highest order derivative is first-order

      例如 (Example): $\frac{dy}{dx} = x^2 + y$

   b) 二阶微分方程 (Second-order Differential Equations)：

      最高阶导数为二阶

      The highest order derivative is second-order

      例如 (Example): $\frac{d^2y}{dx^2} + 3\frac{dy}{dx} + 2y = 0$

   c) 高阶微分方程 (Higher-order Differential Equations)：

      最高阶导数大于二阶

      The highest order derivative is higher than second-order

      例如 (Example): $\frac{d^3y}{dx^3} + 2\frac{d^2y}{dx^2} - \frac{dy}{dx} + y = \sin x$

3. 按方程的形式分类：
   Classification based on the form of the equation:

   a) 线性微分方程 (Linear Differential Equations)：

      未知函数及其导数均以一次方出现，且系数为自变量的函数或常数

      The unknown function and its derivatives appear only to the first power, and their coefficients are functions of the independent variable or constants

      例如 (Example): $\frac{d^2y}{dx^2} + p(x)\frac{dy}{dx} + q(x)y = r(x)$

   b) 非线性微分方程 (Nonlinear Differential Equations)：

      不满足线性方程条件的方程

      Equations that do not satisfy the conditions for linear equations

      例如 (Example): $\frac{dy}{dx} = y^2 + \sin x$
