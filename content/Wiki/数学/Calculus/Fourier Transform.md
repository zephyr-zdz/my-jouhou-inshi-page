# 傅里叶变换 | Fourier Transform

## 1. Introduction 简介

The Fourier Transform is a fundamental tool in signal processing, physics, and mathematics, used to decompose functions into their constituent frequencies.

傅里叶变换是信号处理、物理学和数学中的基本工具,用于将函数分解为其构成频率。

## 2. Definitions 定义

### 2.1 Continuous Fourier Transform 连续傅里叶变换

**Forward Transform 正变换**:

$$
F(\omega) = \int_{-\infty}^{\infty} f(t)e^{-i\omega t}dt
$$

**Inverse Transform 逆变换**:

$$
f(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} F(\omega)e^{i\omega t}d\omega
$$

Where 其中:

- $f(t)$ is the original function in the time domain
  $f(t)$ 是时域中的原始函数
- $F(\omega)$ is the Fourier transform in the frequency domain
  $F(\omega)$ 是频域中的傅里叶变换
- $\omega$ is the angular frequency (radians per second)
  $\omega$ 是角频率 (弧度/秒)

### 2.2 Discrete Fourier Transform (DFT) 离散傅里叶变换

For a sequence of N complex numbers $\{x_n\}$, $n = 0, \ldots, N-1$:

对于 N 个复数的序列 $\{x_n\}$, $n = 0, \ldots, N-1$:

**Forward Transform 正变换**:

$$
X_k = \sum_{n=0}^{N-1} x_n e^{-i2\pi kn/N}, \quad k = 0, \ldots, N-1
$$

**Inverse Transform 逆变换**:

$$
x_n = \frac{1}{N}\sum_{k=0}^{N-1} X_k e^{i2\pi kn/N}, \quad n = 0, \ldots, N-1
$$

## 3. Properties 性质

1. **Linearity 线性**:

   $$

\mathcal{F}\{af(t) + bg(t)\} = aF(\omega) + bG(\omega)

$$

2. **Time Shift 时移**:
   $$

\mathcal{F}\{f(t-t_0)\} = e^{-i\omega t_0}F(\omega)

$$

3. **Frequency Shift 频移**:
   $$

\mathcal{F}\{e^{i\omega_0 t}f(t)\} = F(\omega-\omega_0)

$$

4. **Scaling 尺度变换**:
   $$

\mathcal{F}\{f(at)\} = \frac{1}{|a|}F(\frac{\omega}{a})

$$

5. **Convolution 卷积**:
   $$

\mathcal{F}\{f(t) * g(t)\} = F(\omega)G(\omega)

$$

6. **Multiplication 相乘**:
   $$

\mathcal{F}\{f(t)g(t)\} = \frac{1}{2\pi}F(\omega) * G(\omega)

$$

7. **Parseval's Theorem 帕塞瓦尔定理**:
   $$

\int_{-\infty}^{\infty} |f(t)|^2 dt = \frac{1}{2\pi}\int_{-\infty}^{\infty} |F(\omega)|^2 d\omega

$$

## 4. Common Transform Pairs 常见变换对

1. **Delta Function δ函数**:
   $$

\delta(t) \leftrightarrow 1

$$
   其中 $\delta(t)$ 是Dirac Delta function
   where $\delta(t)$ is the Dirac Delta function
   $$

   \delta(t) = \begin{cases}

   \infty, & t = 0 \\

   0, & t \neq 0

   \end{cases}

$$
   且 $\int_{-\infty}^{\infty} \delta(t)dt = 1$

2. **Constant 常数**:
   $$1 \leftrightarrow 2\pi\delta(\omega)$$

3. **Sine and Cosine 正弦和余弦**:
   $$\sin(\omega_0 t) \leftrightarrow \pi i[\delta(\omega+\omega_0) - \delta(\omega-\omega_0)]$$
   $$\cos(\omega_0 t) \leftrightarrow \pi[\delta(\omega+\omega_0) + \delta(\omega-\omega_0)]$$

4. **Exponential 指数函数**:
   $$e^{-a|t|} \leftrightarrow \frac{2a}{a^2 + \omega^2}$$

5. **Gaussian 高斯函数**:
   $$e^{-at^2} \leftrightarrow \sqrt{\frac{\pi}{a}}e^{-\omega^2/(4a)}$$

6. **Rectangle Function 矩形函数**:
   $$\text{rect}(t) = \begin{cases} 1, & |t| < \frac{1}{2} \\ 0, & \text{otherwise} \end{cases} \leftrightarrow \text{sinc}(\omega) = \frac{\sin(\omega/2)}{\omega/2}$$

## 5. Applications 应用

1. **Signal Processing 信号处理**:
   - Filtering 滤波
   - Compression 压缩
   - Modulation 调制

2. **Image Processing 图像处理**:
   - Edge detection 边缘检测
   - Image compression 图像压缩

3. **Differential Equations 微分方程**:
   - Solving PDEs 求解偏微分方程

4. **Quantum Mechanics 量子力学**:
   - Wave function analysis 波函数分析

5. **Acoustics 声学**:
   - Sound wave analysis 声波分析

## 6. Computation Techniques 计算技巧

1. **Fast Fourier Transform (FFT) 快速傅里叶变换**:
   - Efficient algorithm for computing DFT
   - 计算DFT的高效算法
   - Reduces complexity from $O(N^2)$ to $O(N\log N)$
   - 将复杂度从 $O(N^2)$ 降低到 $O(N\log N)$

2. **Windowing 窗函数**:
   - Reduce spectral leakage in DFT
   - 减少DFT中的频谱泄漏
   - Common windows: Hamming, Hann, Blackman
   - 常见窗函数: 汉明窗、汉宁窗、布莱克曼窗

3. **Zero-padding 零填充**:
   - Increase frequency resolution in DFT
   - 增加DFT的频率分辨率

## 7. Common Pitfalls 常见陷阱

1. Aliasing due to undersampling
   欠采样导致的混叠

2. Spectral leakage in finite-length signals
   有限长信号中的频谱泄漏

3. Neglecting the scaling factor in inverse DFT
   忽略逆DFT中的缩放因子

4. Misinterpreting phase information
   错误解释相位信息

## 8. Derivations and Proofs 推导与证明

### 8.1 Derivation of the Fourier Transform 傅里叶变换的推导

Starting from the Fourier series for a periodic function with period $T$:
从周期为 $T$ 的周期函数的傅里叶级数开始：

$$f(t) = \sum_{n=-\infty}^{\infty} c_n e^{in\omega_0 t}$$

Where $\omega_0 = \frac{2\pi}{T}$ and $c_n = \frac{1}{T}\int_{-T/2}^{T/2} f(t)e^{-in\omega_0 t}dt$

As $T \to \infty$, $\omega_0 \to d\omega$ and $\frac{1}{T} \to \frac{d\omega}{2\pi}$, we get:
当 $T \to \infty$ 时，$\omega_0 \to d\omega$ 且 $\frac{1}{T} \to \frac{d\omega}{2\pi}$，我们得到：

$$f(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} (\int_{-\infty}^{\infty} f(\tau)e^{-i\omega \tau}d\tau) e^{i\omega t}d\omega$$

This gives us the Fourier transform pair:
这给出了傅里叶变换对：

$$F(\omega) = \int_{-\infty}^{\infty} f(t)e^{-i\omega t}dt$$
$$f(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} F(\omega)e^{i\omega t}d\omega$$

### 8.2 Proof of Convolution Theorem 卷积定理的证明

To prove: $\mathcal{F}\{f(t) * g(t)\} = F(\omega)G(\omega)$

Let $h(t) = f(t) * g(t) = \int_{-\infty}^{\infty} f(\tau)g(t-\tau)d\tau$

Taking the Fourier transform of $h(t)$:
对 $h(t)$ 进行傅里叶变换：

$$

\begin{align*}

H(\omega) &= \int_{-\infty}^{\infty} h(t)e^{-i\omega t}dt \\

&= \int_{-\infty}^{\infty} (\int_{-\infty}^{\infty} f(\tau)g(t-\tau)d\tau) e^{-i\omega t}dt \\

&= \int_{-\infty}^{\infty} f(\tau) (\int_{-\infty}^{\infty} g(t-\tau)e^{-i\omega t}dt) d\tau

\end{align*}

$$

Let $u = t-\tau$, then $dt = du$:
令 $u = t-\tau$，则 $dt = du$：
$$\begin{align*}
H(\omega) &= \int_{-\infty}^{\infty} f(\tau) (\int_{-\infty}^{\infty} g(u)e^{-i\omega (u+\tau)}du) d\tau \\
&= \int_{-\infty}^{\infty} f(\tau)e^{-i\omega \tau} (\int_{-\infty}^{\infty} g(u)e^{-i\omega u}du) d\tau \\
&= (\int_{-\infty}^{\infty} f(\tau)e^{-i\omega \tau}d\tau) (\int_{-\infty}^{\infty} g(u)e^{-i\omega u}du) \\
&= F(\omega)G(\omega)
\end{align*}
$$

Thus, the convolution theorem is proved.

因此，卷积定理得证。

### 8.3 Derivation of the Uncertainty Principle 不确定性原理的推导

The uncertainty principle states that a function and its Fourier transform cannot both be highly concentrated.

不确定性原理指出，一个函数及其傅里叶变换不能同时高度集中。

Define the "spread" of $f(t)$ and $F(\omega)$ as:

定义 $f(t)$ 和 $F(\omega)$ 的 " 展宽 " 为：

$$(\Delta t)^2 = \frac{\int_{-\infty}^{\infty} t^2 |f(t)|^2 dt}{\int_{-\infty}^{\infty} |f(t)|^2 dt}
$$

$$(\Delta \omega)^2 = \frac{\int_{-\infty}^{\infty} \omega^2 |F(\omega)|^2 d\omega}{\int_{-\infty}^{\infty} |F(\omega)|^2 d\omega}
$$

Using Parseval's theorem and the properties of Fourier transforms, we can show:

使用帕塞瓦尔定理和傅里叶变换的性质，我们可以证明：

$$\Delta t \cdot \Delta \omega \geq \frac{1}{2}
$$

This is the mathematical expression of the uncertainty principle.

这是不确定性原理的数学表达。

### 8.4 Proof of Parseval's Theorem 帕塞瓦尔定理的证明

To prove: $\int_{-\infty}^{\infty} |f(t)|^2 dt = \frac{1}{2\pi}\int_{-\infty}^{\infty} |F(\omega)|^2 d\omega$

Start with the inverse Fourier transform:

从逆傅里叶变换开始：

$$
f(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} F(\omega)e^{i\omega t}d\omega$$

Multiply both sides by $f^*(t)$ (complex conjugate of $f(t)$):
两边乘以 $f^*(t)$ ($f(t)$ 的复共轭)：

$$|f(t)|^2 = f(t)f^*(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} F(\omega)f^*(t)e^{i\omega t}d\omega$$

Integrate both sides with respect to $t$:
对两边关于 $t$ 积分：

$$\int_{-\infty}^{\infty} |f(t)|^2 dt = \frac{1}{2\pi}\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} F(\omega)f^*(t)e^{i\omega t}d\omega dt$$

Change the order of integration (Fubini's theorem):
改变积分顺序（Fubini定理）：

$$\int_{-\infty}^{\infty} |f(t)|^2 dt = \frac{1}{2\pi}\int_{-\infty}^{\infty} F(\omega) (\int_{-\infty}^{\infty} f^*(t)e^{i\omega t}dt) d\omega$$

The inner integral is the complex conjugate of $F(\omega)$:
内部积分是 $F(\omega)$ 的复共轭：

$$\int_{-\infty}^{\infty} |f(t)|^2 dt = \frac{1}{2\pi}\int_{-\infty}^{\infty} F(\omega)F^*(\omega)d\omega = \frac{1}{2\pi}\int_{-\infty}^{\infty} |F(\omega)|^2 d\omega
$$

Thus, Parseval's theorem is proved.

因此，帕塞瓦尔定理得证。
