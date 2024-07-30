# Lagrange Multiplier 拉格朗日乘数法

## Introduction 简介

Lagrange Multiplier is a method for finding the local maxima and minima of a function subject to equality constraints. 拉格朗日乘数法是一种在等式约束条件下寻找函数局部极值的方法。

---

## Lagrange Multiplier for Functions | 函数的拉格朗日乘数法

To find the extrema of a function $f(\mathbf{x})$ subject to constraints $g_i(\mathbf{x}) = 0$, we form the Lagrange function:

要在约束条件 $g_i(\mathbf{x}) = 0$ 下找到函数 $f(\mathbf{x})$ 的极值，我们构建拉格朗日函数：

$$
\mathcal{L}(\mathbf{x}, \mathbf{\lambda}) = f(\mathbf{x}) + \sum_{i} \lambda_i g_i(\mathbf{x})
$$

Where $\mathbf{\lambda} = (\lambda_1, \lambda_2, \ldots, \lambda_m)$ are the Lagrange multipliers. 其中 $\mathbf{\lambda} = (\lambda_1, \lambda_2, \ldots, \lambda_m)$ 是拉格朗日乘数。

### Steps 步骤

1. Compute the partial derivatives and set them to zero:

    计算偏导数并将其设为零：

    $$
    \frac{\partial \mathcal{L}}{\partial \mathbf{x}} = \nabla f(\mathbf{x}) + \sum_{i} \lambda_i \nabla g_i(\mathbf{x}) = \mathbf{0}


$$
    
    
$$

    \frac{\partial \mathcal{L}}{\partial \lambda_i} = g_i(\mathbf{x}) = 0
    

$$
2. Solve the resulting system of equations for $\mathbf{x}$ and $\mathbf{\lambda}$.

    解出 $\mathbf{x}$ 和 $\mathbf{\lambda}$ 的方程组。

---

## Lagrange Multiplier for Matrices | 矩阵的拉格朗日乘数法

Consider a matrix optimization problem where we need to optimize $f(\mathbf{X})$ subject to matrix constraints $\mathbf{G}(\mathbf{X}) = \mathbf{0}$.

考虑一个矩阵优化问题，需要在矩阵约束 $\mathbf{G}(\mathbf{X}) = \mathbf{0}$ 下优化 $f(\mathbf{X})$。

### Steps 步骤

1. Formulate the Lagrangian:

    构建拉格朗日函数：

    
$$

    \mathcal{L}(\mathbf{X}, \mathbf{\Lambda}) = f(\mathbf{X}) + \mathrm{tr}(\mathbf{\Lambda}^\top \mathbf{G}(\mathbf{X}))

$$

2. Compute the partial derivatives and set them to zero:

    计算偏导数并将其设为零：

$$

    \frac{\partial \mathcal{L}}{\partial \mathbf{X}} = \nabla f(\mathbf{X}) + \mathbf{\Lambda} \nabla \mathbf{G}(\mathbf{X}) = \mathbf{0}
    

$$

    $$
    \frac{\partial \mathcal{L}}{\partial \mathbf{\Lambda}} = \mathbf{G}(\mathbf{X}) = \mathbf{0}
    

$$

3. Solve for $\mathbf{X}$ and $\mathbf{\Lambda}$.

    解出 $\mathbf{X}$ 和 $\mathbf{\Lambda}$。

---

## Solving Linear Systems with Infinite Solutions | 拉格朗日乘数法解决线性方程组无穷解的问题

When a linear system $\mathbf{A}\mathbf{x} = \mathbf{b}$ has infinitely many solutions, the Lagrange multiplier can be used to find specific solutions that optimize a secondary criterion.

当线性方程组 $\mathbf{A}\mathbf{x} = \mathbf{b}$ 有无穷多解时，可以使用拉格朗日乘数法找到优化次要准则的特定解。

### Example 例子

Minimize $f(\mathbf{x}) = \|\mathbf{x}\|^2$ subject to $\mathbf{A}\mathbf{x} = \mathbf{b}$:

在约束条件 $\mathbf{A}\mathbf{x} = \mathbf{b}$ 下最小化 $f(\mathbf{x}) = \|\mathbf{x}\|^2$：

1. Form the Lagrangian:

    构建拉格朗日函数：

$$

    \mathcal{L}(\mathbf{x}, \mathbf{\lambda}) = \|\mathbf{x}\|^2 + \mathbf{\lambda}^\top (\mathbf{A}\mathbf{x} - \mathbf{b})
    

$$

1. Compute the partial derivatives and set them to zero:

    计算偏导数并将其设为零：

$$
    \frac{\partial \mathcal{L}}{\partial \mathbf{x}} = 2\mathbf{x} + \mathbf{A}^\top \mathbf{\lambda} = \mathbf{0}
$$

$$
    \frac{\partial \mathcal{L}}{\partial \mathbf{\lambda}} = \mathbf{A}\mathbf{x} - \mathbf{b} = \mathbf{0}
    
$$

1. Solve the system to find $\mathbf{x}$ and $\mathbf{\lambda}$.

    解出 $\mathbf{x}$ 和 $\mathbf{\lambda}$ 的方程组。

---

## Applications in Machine Learning | 拉格朗日乘数法在机器学习的应用

Lagrange multipliers are used in various machine learning algorithms, particularly for optimization problems involving constraints. 拉格朗日乘数法在各种机器学习算法中都有应用，特别是在涉及约束的优化问题中。

### Support Vector Machines (SVM) 支持向量机

In SVM, we maximize the margin between different classes by solving a constrained optimization problem using Lagrange multipliers.

在支持向量机中，通过使用拉格朗日乘数法求解约束优化问题来最大化不同类别之间的间隔。

1. Formulate the primal problem:

    构建原始问题：

    $$
    \min_{\mathbf{w}, b} \frac{1}{2} \|\mathbf{w}\|^2 \quad \text{s.t.} \quad y_i(\mathbf{w}^\top \mathbf{x}_i + b) \geq 1, \forall i


$$
2. Form the Lagrangian:

    构建拉格朗日函数：
    
    
$$

    \mathcal{L}(\mathbf{w}, b, \mathbf{\alpha}) = \frac{1}{2} \|\mathbf{w}\|^2 - \sum_i \alpha_i [y_i (\mathbf{w}^\top \mathbf{x}_i + b) - 1]
    

$$
2. Compute the partial derivatives and set them to zero:

    计算偏导数并将其设为零：

    
$$

    \frac{\partial \mathcal{L}}{\partial \mathbf{w}} = \mathbf{w} - \sum_i \alpha_i y_i \mathbf{x}_i = \mathbf{0}

$$

$$

    \frac{\partial \mathcal{L}}{\partial b} = \sum_i \alpha_i y_i = 0
    

$$

1. Solve the dual problem for $\alpha_i$:

    解出 $\alpha_i$ 的对偶问题：

    $$
    \max_{\mathbf{\alpha}} \sum_i \alpha_i - \frac{1}{2} \sum_i \sum_j \alpha_i \alpha_j y_i y_j \mathbf{x}_i^\top \mathbf{x}_j \quad \text{s.t.} \quad \sum_i \alpha_i y_i = 0, \alpha_i \geq 0


$$

### Generalized Linear Models (GLM) 广义线性模型

In GLM, Lagrange multipliers can be used to handle constraints during the estimation of model parameters. This is particularly useful when fitting models that must adhere to certain conditions.

在广义线性模型（GLM）中，拉格朗日乘数法可以用来处理参数估计中的约束。这在拟合必须遵循特定条件的模型时特别有用。

#### Constrained Maximum Likelihood Estimation 约束最大似然估计

Consider a GLM where we want to maximize the likelihood function subject to linear constraints on the parameters $\boldsymbol{\beta}$.

考虑一个广义线性模型，我们希望在参数 $\boldsymbol{\beta}$ 上的线性约束下最大化似然函数。

1. Formulate the likelihood function $L(\boldsymbol{\beta})$ and the constraints $\mathbf{A}\boldsymbol{\beta} = \mathbf{b}$.

    构建似然函数 $L(\boldsymbol{\beta})$ 和约束条件 $\mathbf{A}\boldsymbol{\beta} = \mathbf{b}$。

2. Form the Lagrangian:

    构建拉格朗日函数：

$$

    \mathcal{L}(\boldsymbol{\beta}, \mathbf{\lambda}) = \log L(\boldsymbol{\beta}) + \mathbf{\lambda}^\top (\mathbf{A}\boldsymbol{\beta} - \mathbf{b})
    

$$

4. Compute the partial derivatives and set them to zero:

    计算偏导数并将其设为零：

$$
    \frac{\partial \mathcal{L}}{\partial \boldsymbol{\beta}} = \frac{\partial \log L(\boldsymbol{\beta})}{\partial \boldsymbol{\beta}} + \mathbf{A}^\top \mathbf{\lambda} = \mathbf{0}
$$

$$
    \frac{\partial \mathcal{L}}{\partial \mathbf{\lambda}} = \mathbf{A}\boldsymbol{\beta} - \mathbf{b} = \mathbf{0}
    
$$

1. Solve the resulting system of equations for $\boldsymbol{\beta}$ and $\mathbf{\lambda}$.

    解出 $\boldsymbol{\beta}$ 和 $\mathbf{\lambda}$ 的方程组。

#### Example 例子

Suppose we are fitting a logistic regression model with a constraint that the sum of coefficients equals a constant $c$. The likelihood function for logistic regression is given by:

假设我们拟合一个逻辑回归模型，并且有一个约束条件是系数的和等于一个常数 $c$。逻辑回归的似然函数为：

$$
L(\boldsymbol{\beta}) = \prod_{i=1}^n \left( \frac{e^{\mathbf{x}_i^\top \boldsymbol{\beta}}}{1 + e^{\mathbf{x}_i^\top \boldsymbol{\beta}}} \right)^{y_i} \left( \frac{1}{1 + e^{\mathbf{x}_i^\top \boldsymbol{\beta}}} \right)^{1 - y_i}
$$

To incorporate the constraint $\mathbf{1}^\top \boldsymbol{\beta} = c$, we form the Lagrangian:

为了包含约束条件 $\mathbf{1}^\top \boldsymbol{\beta} = c$，我们构建拉格朗日函数：

$$
\mathcal{L}(\boldsymbol{\beta}, \lambda) = \log L(\boldsymbol{\beta}) + \lambda (\mathbf{1}^\top \boldsymbol{\beta} - c)
$$

Taking the partial derivatives and setting them to zero:

计算偏导数并将其设为零：

$$
\frac{\partial \mathcal{L}}{\partial \boldsymbol{\beta}} = \frac{\partial \log L(\boldsymbol{\beta})}{\partial \boldsymbol{\beta}} + \lambda \mathbf{1} = \mathbf{0}
$$

$$
\frac{\partial \mathcal{L}}{\partial \lambda} = \mathbf{1}^\top \boldsymbol{\beta} - c = \mathbf{0}
$$

Solving these equations will give the estimates of $\boldsymbol{\beta}$ and $\lambda$ that satisfy the constraint.

解出这些方程将得到满足约束条件的 $\boldsymbol{\beta}$ 和 $\lambda$ 的估计值。
