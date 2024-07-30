# Cumulative Distribution Function (CDF)

## Definition

### English

The Cumulative Distribution Function (CDF) of a random variable $X$ is a function $F_X(x)$ that gives the probability that $X$ will take a value less than or equal to $x$. Mathematically, it is defined as:

$$
F_X(x) = P(X \leq x)
$$

### 中文

累积分布函数（CDF）是随机变量 $X$ 的一个函数 $F_X(x)$，它给出 $X$ 取值小于或等于 $x$ 的概率。数学上，它定义为：

$$
F_X(x) = P(X \leq x)
$$

## Properties

### English

1. **Non-decreasing**: $F_X(x)$ is a non-decreasing function.
2. **Limits**:
   - $\lim_{x \to -\infty} F_X(x) = 0$
   - $\lim_{x \to \infty} F_X(x) = 1$
3. **Right-continuous**: $F_X(x)$ is right-continuous, meaning $\lim_{x \to x_0^+} F_X(x) = F_X(x_0)$.
4. **Probability Mass Function (PMF) Relation** (for discrete random variables):

   $$

 F_X(x) = \sum_{t \leq x} P(X = t)

$$
5. **Probability Density Function (PDF) Relation** (for continuous random variables):
   $$

 F_X(x) = \int_{-\infty}^{x} f_X(t) \, dt

$$

### 中文
1. **非减性**：$F_X(x)$ 是一个非减函数。
2. **极限**：
   - $\lim_{x \to -\infty} F_X(x) = 0$
   - $\lim_{x \to \infty} F_X(x) = 1$
3. **右连续**：$F_X(x)$ 是右连续的，意味着 $\lim_{x \to x_0^+} F_X(x) = F_X(x_0)$。
4. **概率质量函数 ([[PMF&PDF#概率密度函数 (PDF)|PMF]]) 关系**（对于离散随机变量）：
   $$

 F_X(x) = \sum_{t \leq x} P(X = t)

$$
5. **概率密度函数 ([[PMF&PDF#概率密度函数 (PDF)|PDF]]) 关系**（对于连续随机变量）：
   $$

 F_X(x) = \int_{-\infty}^{x} f_X(t) \, dt

$$

## Calculation Techniques
### English
- **Discrete Random Variable**: To find the CDF of a discrete random variable, sum the probabilities of all outcomes less than or equal to $x$.
  $$

 F_X(x) = \sum_{t \leq x} P(X = t)

$$
  
- **Continuous Random Variable**: To find the CDF of a continuous random variable, integrate the PDF from $-\infty$ to $x$.
  $$

 F_X(x) = \int_{-\infty}^{x} f_X(t) \, dt

$$

### 中文
- **离散随机变量**：为了找到离散随机变量的CDF，求所有小于或等于 $x$ 的结果的概率之和。
  ==
$$

 F_X(x) = \sum_{t \leq x} P(X = t)

$$==

- **连续随机变量**：为了找到连续随机变量的CDF，积分从 $-\infty$ 到 $x$ 的PDF。
  ==
$$

 F_X(x) = \int_{-\infty}^{x} f_X(t) \, dt

$$==

## Important Points to Remember
### English
- The CDF provides a complete description of the probability distribution of a random variable.
- For continuous random variables, the derivative of the CDF with respect to $x$ gives the PDF:
  $$

 f_X(x) = \frac{d}{dx} F_X(x)

$$ ^bfcb0c
- For discrete random variables, the difference of the CDF at adjacent points gives the PMF:
  $$

 P(X = x) = F_X(x) - F_X(x-)

$$
- The CDF can be used to find probabilities for ranges of values:
  $$

 P(a < X \leq b) = F_X(b) - F_X(a)

$$

### 中文
- CDF提供了随机变量的概率分布的完整描述。
- 对于连续随机变量，CDF关于 $x$ 的导数给出了PDF：
  $$

 f_X(x) = \frac{d}{dx} F_X(x)

$$
- 对于离散随机变量，相邻点处CDF的差异给出了PMF：
  $$

 P(X = x) = F_X(x) - F_X(x-)

$$
- CDF可以用来找到值范围的概率：
  $$

 P(a < X \leq b) = F_X(b) - F_X(a)

$$

## Common Mistakes
### English
- Confusing the CDF with the PDF. Remember, the CDF is the integral of the PDF for continuous variables and the sum of the PMF for discrete variables.
- Forgetting that the CDF is right-continuous.
- Misinterpreting the limits: Ensure you correctly understand that $F_X(x)$ approaches 0 as $x$ approaches $-\infty$ and 1 as $x$ approaches $\infty$.

### 中文
- 将CDF与PDF混淆。记住，对于连续变量，CDF是PDF的积分；对于离散变量，CDF是PMF的和。
- 忘记CDF是右连续的。
- 误解极限：确保你正确理解 $F_X(x)$ 当 $x$ 趋近 $-\infty$ 时趋近于0，当 $x$ 趋近 $\infty$ 时趋近于1。

## Example
### English
Given a discrete random variable $X$ with the following PMF:

$$

P(X = x) =

\begin{cases}

0.2 & \text{if } x = 1 \\

0.5 & \text{if } x = 2 \\

0.3 & \text{if } x = 3 \\

0 & \text{otherwise}

\end{cases}

$$

The CDF $F_X(x)$ is calculated as:

$$

F_X(x) =

\begin{cases}

0 & \text{if } x < 1 \\

0.2 & \text{if } 1 \leq x < 2 \\

0.7 & \text{if } 2 \leq x < 3 \\

1 & \text{if } x \geq 3

\end{cases}

$$

### 中文
给定一个离散随机变量 $X$，其PMF如下：

$$

P(X = x) =

\begin{cases}

0.2 & \text{如果 } x = 1 \\

0.5 & \text{如果 } x = 2 \\

0.3 & \text{如果 } x = 3 \\

0 & 其他情况

\end{cases}

$$

CDF $F_X(x)$ 计算如下：

$$

F_X(x) =

\begin{cases}

0 & \text{如果 } x < 1 \\

0.2 & \text{如果 } 1 \leq x < 2 \\

0.7 & \text{如果 } 2 \leq x < 3 \\

1 & \text{如果 } x \geq 3

\end{cases}

$$
