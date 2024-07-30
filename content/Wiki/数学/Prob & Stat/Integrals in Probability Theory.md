# 概率论常用积分 | Integrals in Probability Theory

## 指数分布 | Exponential Distribution

### 指数分布的概率密度函数 | Probability Density Function of Exponential Distribution

$$
f_X(x) = \lambda e^{-\lambda x} \quad \text{for} \quad x \geq 0
$$

### 指数分布的期望值 | Expectation of Exponential Distribution

$$
\mathbb{E}(X) = \int_{0}^{\infty} x \lambda e^{-\lambda x} \mathrm{d}x
$$

积分过程：

$$
\begin{align*}
\mathbb{E}(X) &= \int_{0}^{\infty} x \lambda e^{-\lambda x} \mathrm{d}x \\
\text{令} \ u &= \lambda x, \ \mathrm{d}u = \lambda \mathrm{d}x \\
&= \int_{0}^{\infty} \frac{u}{\lambda} \lambda e^{-u} \frac{\mathrm{d}u}{\lambda} \\
&= \int_{0}^{\infty} u e^{-u} \mathrm{d}u \\
\text{使用分部积分法} \ \left( \int u \mathrm{d}v = uv - \int v \mathrm{d}u \right) \\
u &= u, \ \mathrm{d}v = e^{-u} \mathrm{d}u \\
v &= -e^{-u}, \ \mathrm{d}u = \mathrm{d}u \\
\int u e^{-u} \mathrm{d}u &= -u e^{-u} \bigg|_{0}^{\infty} + \int e^{-u} \mathrm{d}u \\
&= -u e^{-u} \bigg|_{0}^{\infty} - e^{-u} \bigg|_{0}^{\infty} \\
&= 0 + 1 = 1 \\
\mathbb{E}(X) &= 1 / \lambda
\end{align*}
$$

### 指数分布的方差 | Variance of Exponential Distribution

$$
\mathrm{Var}(X) = \int_{0}^{\infty} x^2 \lambda e^{-\lambda x} \mathrm{d}x - \left(\frac{1}{\lambda}\right)^2 = \frac{1}{\lambda^2}
$$

积分过程：

$$
\begin{align*}
\mathrm{Var}(X) &= \int_{0}^{\infty} x^2 \lambda e^{-\lambda x} \mathrm{d}x - \left(\frac{1}{\lambda}\right)^2 \\
\text{令} \ u &= \lambda x, \ \mathrm{d}u = \lambda \mathrm{d}x \\
&= \int_{0}^{\infty} \left(\frac{u}{\lambda}\right)^2 \lambda e^{-u} \frac{\mathrm{d}u}{\lambda} \\
&= \int_{0}^{\infty} \frac{u^2}{\lambda^2} \lambda e^{-u} \frac{\mathrm{d}u}{\lambda} \\
&= \int_{0}^{\infty} u^2 e^{-u} \mathrm{d}u \\
\text{使用Gamma函数} \ \Gamma(n) = \int_{0}^{\infty} x^{n-1} e^{-x} \mathrm{d}x \\
\text{对于} \ \Gamma(3) &= \int_{0}^{\infty} u^2 e^{-u} \mathrm{d}u = 2! = 2 \\
\mathrm{Var}(X) &= \frac{2}{\lambda^2} - \left(\frac{1}{\lambda}\right)^2 = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2}
\end{align*}
$$

## 正态分布 | Normal Distribution

### 正态分布的概率密度函数 | Probability Density Function of Normal Distribution

$$
f_X(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

### 标准正态分布的积分 | Integral of Standard Normal Distribution

$$
\int_{-\infty}^{\infty} e^{-\frac{x^2}{2}} \mathrm{d}x = \sqrt{2\pi}
$$

高斯积分 (Gaussian Integral) 积分过程：

$$
\begin{align*}
I &= \int_{-\infty}^{\infty} e^{-\frac{x^2}{2}} \mathrm{d}x \\
I^2 &= \left(\int_{-\infty}^{\infty} e^{-\frac{x^2}{2}} \mathrm{d}x\right)\left(\int_{-\infty}^{\infty} e^{-\frac{y^2}{2}} \mathrm{d}y\right) \\
&= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} e^{-\frac{x^2 + y^2}{2}} \mathrm{d}x \mathrm{d}y \\
\text{转换为极坐标} \ x = r\cos\theta, \ y = r\sin\theta, \ \mathrm{d}x \mathrm{d}y = r \mathrm{d}r \mathrm{d}\theta \\
I^2 &= \int_{0}^{2\pi} \int_{0}^{\infty} e^{-\frac{r^2}{2}} r \mathrm{d}r \mathrm{d}\theta \\
&= \int_{0}^{2\pi} \mathrm{d}\theta \int_{0}^{\infty} r e^{-\frac{r^2}{2}} \mathrm{d}r \\
\text{令} \ u &= \frac{r^2}{2}, \ \mathrm{d}u = r \mathrm{d}r \\
I^2 &= \int_{0}^{2\pi} \mathrm{d}\theta \int_{0}^{\infty} e^{-u} \mathrm{d}u \\
&= 2\pi \left[-e^{-u}\right]_{0}^{\infty} \\
&= 2\pi \left[0 - (-1)\right] \\
&= 2\pi \\
I &= \sqrt{2\pi}
\end{align*}
$$

### 正态分布的期望值 | Expectation of Normal Distribution

$$
\mathbb{E}(X) = \int_{-\infty}^{\infty} x \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \mathrm{d}x = \mu
$$

积分过程：

$$
\begin{align*}
\mathbb{E}(X) &= \int_{-\infty}^{\infty} x \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \mathrm{d}x \\
\text{令} \ u &= \frac{x-\mu}{\sigma}, \ x = \sigma u + \mu, \ \mathrm{d}x = \sigma \mathrm{d}u \\
&= \int_{-\infty}^{\infty} (\sigma u + \mu) \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{u^2}{2}} \sigma \mathrm{d}u \\
&= \mu \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-\frac{u^2}{2}} \mathrm{d}u + \sigma \int_{-\infty}^{\infty} u \frac{1}{\sqrt{2\pi}} e^{-\frac{u^2}{2}} \mathrm{d}u \\
&= \mu \left[\int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-\frac{u^2}{2}} \mathrm{d}u \right] + 0 \quad \text{(奇函数在对称区间内积分为零)} \\
&= \mu \cdot 1 \\
&= \mu
\end{align*}
$$

### 正态分布的方差 | Variance of Normal Distribution

$$
\mathrm{Var}(X) = \int_{-\infty}^{\infty} (x - \mu)^2 \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \mathrm{d}x = \sigma^2
$$

积分过程：

$$
\begin{align*}


\mathrm{Var}(X) &= \int_{-\infty}^{\infty} (x - \mu)^2 \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \mathrm{d}x \\
\text{令} \ u &= \frac{x-\mu}{\sigma}, \ x = \sigma u + \mu, \ \mathrm{d}x = \sigma \mathrm{d}u \\
&= \int_{-\infty}^{\infty} (\sigma u)^2 \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{u^2}{2}} \sigma \mathrm{d}u \\
&= \sigma^2 \int_{-\infty}^{\infty} u^2 \frac{1}{\sqrt{2\pi}} e^{-\frac{u^2}{2}} \mathrm{d}u \\
\text{使用分部积分法} \ \left( \int u^2 e^{-\frac{u^2}{2}} \mathrm{d}u = \sqrt{2\pi} \right) \\
\mathrm{Var}(X) &= \sigma^2 \cdot 1 = \sigma^2
\end{align*}
$$

## 均匀分布 | Uniform Distribution

### 均匀分布的概率密度函数 | Probability Density Function of Uniform Distribution

$$
f_X(x) = \begin{cases} 
\frac{1}{b-a} & a \leq x \leq b \\
0 & \text{otherwise}
\end{cases}
$$

### 均匀分布的期望值 | Expectation of Uniform Distribution

$$
\mathbb{E}(X) = \int_{a}^{b} x \frac{1}{b-a} \mathrm{d}x = \frac{a+b}{2}
$$

积分过程：

$$
\begin{align*}
\mathbb{E}(X) &= \int_{a}^{b} x \frac{1}{b-a} \mathrm{d}x \\
&= \frac{1}{b-a} \int_{a}^{b} x \mathrm{d}x \\
&= \frac{1}{b-a} \left[ \frac{x^2}{2} \right]_{a}^{b} \\
&= \frac{1}{b-a} \left( \frac{b^2}{2} - \frac{a^2}{2} \right) \\
&= \frac{b^2 - a^2}{2(b-a)} \\
&= \frac{(b-a)(b+a)}{2(b-a)} \\
&= \frac{a+b}{2}
\end{align*}
$$

### 均匀分布的方差 | Variance of Uniform Distribution

$$
\mathrm{Var}(X) = \int_{a}^{b} x^2 \frac{1}{b-a} \mathrm{d}x - \left(\frac{a+b}{2}\right)^2 = \frac{(b-a)^2}{12}
$$

积分过程：

$$
\begin{align*}
\mathrm{Var}(X) &= \int_{a}^{b} x^2 \frac{1}{b-a} \mathrm{d}x - \left(\frac{a+b}{2}\right)^2 \\
&= \frac{1}{b-a} \int_{a}^{b} x^2 \mathrm{d}x - \left(\frac{a+b}{2}\right)^2 \\
&= \frac{1}{b-a} \left[ \frac{x^3}{3} \right]_{a}^{b} - \frac{(a+b)^2}{4} \\
&= \frac{1}{b-a} \left( \frac{b^3}{3} - \frac{a^3}{3} \right) - \frac{(a^2 + 2ab + b^2)}{4} \\
&= \frac{b^3 - a^3}{3(b-a)} - \frac{a^2 + 2ab + b^2}{4} \\
&= \frac{(b-a)(b^2 + ba + a^2)}{3(b-a)} - \frac{a^2 + 2ab + b^2}{4} \\
&= \frac{b^2 + ba + a^2}{3} - \frac{a^2 + 2ab + b^2}{4} \\
&= \frac{4(b^2 + ba + a^2) - 3(a^2 + 2ab + b^2)}{12} \\
&= \frac{4b^2 + 4ba + 4a^2 - 3a^2 - 6ab - 3b^2}{12} \\
&= \frac{b^2 - 2ab + a^2}{12} \\
&= \frac{(b-a)^2}{12}
\end{align*}
$$

## 伽马分布 | Gamma Distribution

### 伽马分布的概率密度函数 | Probability Density Function of Gamma Distribution

$$
f_X(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x} \quad \text{for} \quad x \geq 0
$$

### 伽马分布的期望值 | Expectation of Gamma Distribution

$$
\mathbb{E}(X) = \int_{0}^{\infty} x \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x} \mathrm{d}x = \frac{\alpha}{\beta}
$$

积分过程：

$$
\begin{align*}
\mathbb{E}(X) &= \int_{0}^{\infty} x \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x} \mathrm{d}x \\
&= \frac{\beta^\alpha}{\Gamma(\alpha)} \int_{0}^{\infty} x^\alpha e^{-\beta x} \mathrm{d}x \\
\text{令} \ u &= \beta x, \ \mathrm{d}u = \beta \mathrm{d}x \\
&= \frac{\beta^\alpha}{\Gamma(\alpha)} \int_{0}^{\infty} \left(\frac{u}{\beta}\right)^\alpha e^{-u} \frac{\mathrm{d}u}{\beta} \\
&= \frac{\beta^\alpha}{\Gamma(\alpha)} \int_{0}^{\infty} \frac{u^\alpha}{\beta^\alpha \beta} e^{-u} \mathrm{d}u \\
&= \frac{\beta^\alpha}{\Gamma(\alpha)} \cdot \frac{1}{\beta^{\alpha+1}} \int_{0}^{\infty} u^\alpha e^{-u} \mathrm{d}u \\
&= \frac{1}{\beta \Gamma(\alpha)} \Gamma(\alpha+1) \\
&= \frac{\Gamma(\alpha+1)}{\beta \Gamma(\alpha)} \\
\text{由于} \ \Gamma(\alpha+1) &= \alpha \Gamma(\alpha) \\
\mathbb{E}(X) &= \frac{\alpha \Gamma(\alpha)}{\beta \Gamma(\alpha)} \\
&= \frac{\alpha}{\beta}
\end{align*}
$$

### 伽马分布的方差 | Variance of Gamma Distribution

$$
\mathrm{Var}(X) = \int_{0}^{\infty} x^2 \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x} \mathrm{d}x - \left(\frac{\alpha}{\beta}\right)^2 = \frac{\alpha}{\beta^2}
$$

积分过程：

$$
\begin{align*}
\mathrm{Var}(X) &= \int_{0}^{\infty} x^2 \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x} \mathrm{d}x - \left(\frac{\alpha}{\beta}\right)^2 \\
&= \frac{\beta^\alpha}{\Gamma(\alpha)} \int_{0}^{\infty} x^{\alpha+1} e^{-\beta x} \mathrm{d}x \\
\text{令} \ u &= \beta x, \ \mathrm{d}u = \beta \mathrm{d}x \\
&= \frac{\beta^\alpha}{\Gamma(\alpha)} \int_{0}^{\infty} \left(\frac{u}{\beta}\right)^{\alpha+1} e^{-u} \frac{\mathrm{d}u}{\beta} \\
&= \frac{\beta^\alpha}{\Gamma(\alpha)} \int_{0}^{\infty} \frac{u^{\alpha+1

}}{\beta^{\alpha+1} \beta} e^{-u} \mathrm{d}u \\
&= \frac{\beta^\alpha}{\Gamma(\alpha)} \cdot \frac{1}{\beta^{\alpha+2}} \int_{0}^{\infty} u^{\alpha+1} e^{-u} \mathrm{d}u \\
&= \frac{1}{\beta^2 \Gamma(\alpha)} \Gamma(\alpha+2) \\
&= \frac{\Gamma(\alpha+2)}{\beta^2 \Gamma(\alpha)} \\
\text{由于} \ \Gamma(\alpha+2) &= (\alpha+1) \alpha \Gamma(\alpha) \\
\mathrm{Var}(X) &= \frac{(\alpha+1) \alpha \Gamma(\alpha)}{\beta^2 \Gamma(\alpha)} - \left(\frac{\alpha}{\beta}\right)^2 \\
&= \frac{(\alpha+1) \alpha}{\beta^2} - \frac{\alpha^2}{\beta^2} \\
&= \frac{\alpha^2 + \alpha - \alpha^2}{\beta^2} \\
&= \frac{\alpha}{\beta^2}
\end{align*}
$$

## 贝塔分布 | Beta Distribution

### 贝塔分布的概率密度函数 | Probability Density Function of Beta Distribution

$$
f_X(x) = \frac{x^{\alpha-1} (1-x)^{\beta-1}}{\mathrm{B}(\alpha, \beta)} \quad \text{for} \quad 0 \leq x \leq 1
$$

其中，$\mathrm{B}(\alpha, \beta)$ 是 Beta 函数

where $\mathrm{B}(\alpha, \beta)$ is the Beta function

### 贝塔分布的期望值 | Expectation of Beta Distribution

$$
\mathbb{E}(X) = \int_{0}^{1} x \frac{x^{\alpha-1} (1-x)^{\beta-1}}{\mathrm{B}(\alpha, \beta)} \mathrm{d}x = \frac{\alpha}{\alpha + \beta}
$$

积分过程：

$$
\begin{align*}
\mathbb{E}(X) &= \int_{0}^{1} x \frac{x^{\alpha-1} (1-x)^{\beta-1}}{\mathrm{B}(\alpha, \beta)} \mathrm{d}x \\
&= \frac{1}{\mathrm{B}(\alpha, \beta)} \int_{0}^{1} x^\alpha (1-x)^{\beta-1} \mathrm{d}x \\
\text{由于} \ \mathrm{B}(\alpha, \beta) &= \int_{0}^{1} x^{\alpha-1} (1-x)^{\beta-1} \mathrm{d}x \\
\mathbb{E}(X) &= \frac{\mathrm{B}(\alpha+1, \beta)}{\mathrm{B}(\alpha, \beta)} \\
\text{使用Beta函数性质} \ \mathrm{B}(\alpha, \beta) &= \frac{\Gamma(\alpha) \Gamma(\beta)}{\Gamma(\alpha + \beta)} \\
\mathrm{B}(\alpha+1, \beta) &= \frac{\Gamma(\alpha+1) \Gamma(\beta)}{\Gamma(\alpha+1 + \beta)} \\
&= \frac{\alpha \Gamma(\alpha) \Gamma(\beta)}{(\alpha + \beta) \Gamma(\alpha + \beta)} \\
\mathbb{E}(X) &= \frac{\alpha \Gamma(\alpha) \Gamma(\beta)}{(\alpha + \beta) \Gamma(\alpha + \beta)} \cdot \frac{\Gamma(\alpha + \beta)}{\Gamma(\alpha) \Gamma(\beta)} \\
&= \frac{\alpha}{\alpha + \beta}
\end{align*}
$$

### 贝塔分布的方差 | Variance of Beta Distribution

$$
\mathrm{Var}(X) = \int_{0}^{1} x^2 \frac{x^{\alpha-1} (1-x)^{\beta-1}}{\mathrm{B}(\alpha, \beta)} \mathrm{d}x - \left(\frac{\alpha}{\alpha + \beta}\right)^2 = \frac{\alpha \beta}{(\alpha + \beta)^2 (\alpha + \beta + 1)}
$$

积分过程：

$$
\begin{align*}
\mathrm{Var}(X) &= \int_{0}^{1} x^2 \frac{x^{\alpha-1} (1-x)^{\beta-1}}{\mathrm{B}(\alpha, \beta)} \mathrm{d}x - \left(\frac{\alpha}{\alpha + \beta}\right)^2 \\
&= \frac{1}{\mathrm{B}(\alpha, \beta)} \int_{0}^{1} x^{\alpha+1} (1-x)^{\beta-1} \mathrm{d}x \\
&= \frac{\mathrm{B}(\alpha+2, \beta)}{\mathrm{B}(\alpha, \beta)} - \left(\frac{\alpha}{\alpha + \beta}\right)^2 \\
&= \frac{\frac{\Gamma(\alpha+2) \Gamma(\beta)}{\Gamma(\alpha + 2 + \beta)}}{\frac{\Gamma(\alpha) \Gamma(\beta)}{\Gamma(\alpha + \beta)}} - \left(\frac{\alpha}{\alpha + \beta}\right)^2 \\
&= \frac{\Gamma(\alpha+2) \Gamma(\beta) \Gamma(\alpha + \beta)}{\Gamma(\alpha + 2 + \beta) \Gamma(\alpha) \Gamma(\beta)} - \left(\frac{\alpha}{\alpha + \beta}\right)^2 \\
&= \frac{(\alpha+1) \alpha \Gamma(\alpha) \Gamma(\beta) \Gamma(\alpha + \beta)}{(\alpha + \beta + 1)(\alpha + \beta) \Gamma(\alpha + \beta) \Gamma(\alpha) \Gamma(\beta)} - \left(\frac{\alpha}{\alpha + \beta}\right)^2 \\
&= \frac{(\alpha+1) \alpha}{(\alpha + \beta + 1)(\alpha + \beta)} - \left(\frac{\alpha}{\alpha + \beta}\right)^2 \\
&= \frac{\alpha (\alpha + 1)}{(\alpha + \beta)^2 (\alpha + \beta + 1)} - \frac{\alpha^2}{(\alpha + \beta)^2} \\
&= \frac{\alpha (\alpha + 1) - \alpha^2}{(\alpha + \beta)^2 (\alpha + \beta + 1)} \\
&= \frac{\alpha (\alpha + 1 - \alpha)}{(\alpha + \beta)^2 (\alpha + \beta + 1)} \\
&= \frac{\alpha \beta}{(\alpha + \beta)^2 (\alpha + \beta + 1)}
\end{align*}
$$
