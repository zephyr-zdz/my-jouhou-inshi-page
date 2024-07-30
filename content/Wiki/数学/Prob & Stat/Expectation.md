# Expectation Values

## Definition

**Expectation** of a random variable $X$, denoted by $\mathbb{E}[X]$ or $E(X)$, is the long-run average value of repetitions of the experiment it represents. It's also known as the **mean**.

## Important Properties

1. **Linearity of Expectation**:
   - $\mathbb{E}[aX + bY] = a\mathbb{E}[X] + b\mathbb{E}[Y]$
   - This holds for any real numbers $a$ and $b$, and random variables $X$ and $Y$.

2. **Expectation of a Constant**:
   - $\mathbb{E}[c] = c$ where $c$ is a constant.

3. **Non-negativity**:
   - If $X \geq 0$ almost surely, then $\mathbb{E}[X] \geq 0$.

4. **Law of the Unconscious Statistician**:
   - If $X$ is a random variable and $g$ is a function, then $\mathbb{E}[g(X)]$ is not necessarily $g(\mathbb{E}[X])$. However, $\mathbb{E}[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x) dx$, where $f_X(x)$ is the probability density function of $X$.

## Common Formulas

1. **Discrete Random Variables**:
   - For a discrete random variable $X$ with possible values $x_1, x_2, \ldots$ and corresponding probabilities $p_1, p_2, \ldots$:

     $$
     \mathbb{E}[X] = \sum_{i} x_i p_i

$$


2. **Continuous Random Variables**:
   - For a continuous random variable $X$ with probability density function $f_X(x)$:
     $$
     \mathbb{E}[X] = \int_{-\infty}^{\infty} x f_X(x) dx
     
$$

3. **Expectation of the Sum**:
   - For any two random variables $X$ and $Y$:

     $$
     \mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]

$$


## Calculation Techniques

1. **Using Symmetry**:
   - If the distribution of $X$ is symmetric about $a$, then $\mathbb{E}[X] = a$.

2. **Indicator Variables**:
   - If $I_A$ is an indicator variable for event $A$, then $\mathbb{E}[I_A] = P(A)$.

3. **Transformation**:
   - For $Y = aX + b$, use linearity:
     $$
     \mathbb{E}[Y] = a\mathbb{E}[X] + b
     
$$

4. **Expected Value of Geometric Distribution**:
   - If $X \sim \text{Geom}(p)$:

     $$
     \mathbb{E}[X] = \frac{1}{p}

$$
