# Akra-Bazzi Theorem | Akra-Bazzi 定理

## Introduction | 介绍

The **Akra-Bazzi Theorem** is a general method used to solve divide-and-conquer recurrences that arise in the analysis of many algorithms, particularly those that do not fit neatly into the Master Theorem. It is often used for recurrences where the subproblem size is a non-linear function of the original problem size. This theorem generalizes the Master Theorem to handle more complex cases.

**Akra-Bazzi 定理**是一种用于解决分治法递推关系的通用方法，特别适用于那些不能直接套用主定理的情况。该定理常用于子问题规模是原问题规模的非线性函数的递推关系分析。这一理论是主定理的推广，能够处理更复杂的情况。

## Theorem Statement | 定理陈述

Given a recurrence of the form:

$$
T(x) = g(x) + \sum_{i=1}^{k} a_i \cdot T(b_i \cdot x + h_i(x))
$$

where:

- $g(x)$, $h_i(x)$ are continuous functions,
- $a_i$ and $b_i$ are constants with $0 < b_i < 1$ and $a_i > 0$,
- $T(x)$ is the function to be solved,

the solution can be expressed as:

$$
T(x) = \Theta \left( x^p \left(1 + \int_{1}^{x} \frac{g(u)}{u^{p+1}} \mathrm{d}u \right) \right)
$$

where $p$ is a constant satisfying the equation:

$$
\sum_{i=1}^{k} a_i \cdot b_i^p = 1
$$

This equation determines the critical exponent $p$.

给定一个如下形式的递推关系:

$$
T(x) = g(x) + \sum_{i=1}^{k} a_i \cdot T(b_i \cdot x + h_i(x))
$$

其中:

- $g(x)$, $h_i(x)$ 是连续函数,
- $a_i$ 和 $b_i$ 是常数，且 $0 < b_i < 1$ 且 $a_i > 0$,
- $T(x)$ 是需要求解的函数,

其解可以表示为:

$$
T(x) = \Theta \left( x^p \left(1 + \int_{1}^{x} \frac{g(u)}{u^{p+1}} \mathrm{d}u \right) \right)
$$

其中 $p$ 是满足下列方程的常数:

$$
\sum_{i=1}^{k} a_i \cdot b_i^p = 1
$$

这个方程确定了临界指数 $p$。

## Applications | 应用

The Akra-Bazzi theorem is particularly useful when dealing with algorithms where the input size is reduced by a non-constant factor, such as in cases where each recursive call works on a different fraction of the input size. Examples include:

- Quicksort with median of medians
- Various dynamic programming algorithms where subproblem sizes vary non-uniformly

**Akra-Bazzi 定理**特别适用于处理输入规模按非固定比例缩减的算法，如每个递归调用处理输入规模的不同分数的情况。例子包括:

- 使用中位数选择的快速排序
- 各种子问题规模不均匀变化的动态规划算法

## Example | 示例

Consider the recurrence:

$$
T(x) = 2T\left(\frac{x}{2}\right) + \sqrt{x}
$$

Here, we have:

- $a_1 = 2$, $b_1 = \frac{1}{2}$, $g(x) = \sqrt{x}$

First, solve for $p$:

$$
2 \cdot \left(\frac{1}{2}\right)^p = 1
$$

This simplifies to $p = 1$.

The solution is then given by:

$$
T(x) = \Theta \left( x \left(1 + \int_{1}^{x} \frac{\sqrt{u}}{u^{2}} \mathrm{d}u \right) \right)
$$

Evaluating the integral:

$$
\int_{1}^{x} \frac{\sqrt{u}}{u^{2}} \mathrm{d}u = \int_{1}^{x} u^{-\frac{3}{2}} \mathrm{d}u
$$

This gives us:

$$
T(x) = \Theta(x)
$$

考虑以下递推关系:

$$
T(x) = 2T\left(\frac{x}{2}\right) + \sqrt{x}
$$

这里，我们有:

- $a_1 = 2$, $b_1 = \frac{1}{2}$, $g(x) = \sqrt{x}$

首先求解 $p$:

$$
2 \cdot \left(\frac{1}{2}\right)^p = 1
$$

简化得 $p = 1$。

那么解为:

$$
T(x) = \Theta \left( x \left(1 + \int_{1}^{x} \frac{\sqrt{u}}{u^{2}} \mathrm{d}u \right) \right)
$$

计算积分:

$$
\int_{1}^{x} \frac{\sqrt{u}}{u^{2}} \mathrm{d}u = \int_{1}^{x} u^{-\frac{3}{2}} \mathrm{d}u
$$

因此:

$$
T(x) = \Theta(x)
$$

This result shows that $T(x)$ grows linearly with $x$.

这个结果表明 $T(x)$ 随着 $x$ 线性增长。
