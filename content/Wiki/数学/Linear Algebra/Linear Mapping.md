# Linear Mapping / 线性映射

## Linear Mapping / 线性映射

A linear mapping $T: \mathbb{R}^m \to \mathbb{R}^n$ is a function that satisfies $T(a\mathbf{x} + b\mathbf{y}) = aT(\mathbf{x}) + bT(\mathbf{y})$ for all $\mathbf{x}, \mathbf{y} \in \mathbb{R}^m$ and all scalars $a, b \in \mathbb{R}$.

线性映射 $T: \mathbb{R}^m \to \mathbb{R}^n$ 是一个满足 $T(a\mathbf{x} + b\mathbf{y}) = aT(\mathbf{x}) + bT(\mathbf{y})$ 的函数，其中 $\mathbf{x}, \mathbf{y} \in \mathbb{R}^m$，$a, b \in \mathbb{R}$。

## Surjectivity / 满射

A function $T$ is surjective (onto) if for every $\mathbf{y} \in \mathbb{R}^n$, there exists at least one $\mathbf{x} \in \mathbb{R}^m$ such that $T(\mathbf{x}) = \mathbf{y}$.

如果对每个 $\mathbf{y} \in \mathbb{R}^n$，至少存在一个 $\mathbf{x} \in \mathbb{R}^m$ 使得 $T(\mathbf{x}) = \mathbf{y}$，则函数 $T$ 是满射（到射）的。

## Injectivity / 单射

A function $T$ is injective (one-to-one) if for every $\mathbf{x}_1, \mathbf{x}_2 \in \mathbb{R}^m$, $T(\mathbf{x}_1) = T(\mathbf{x}_2)$ implies $\mathbf{x}_1 = \mathbf{x}_2$.

如果对每个 $\mathbf{x}_1, \mathbf{x}_2 \in \mathbb{R}^m$，$T(\mathbf{x}_1) = T(\mathbf{x}_2)$ 蕴含 $\mathbf{x}_1 = \mathbf{x}_2$，则函数 $T$ 是单射的。

## Bijectivity / 双射

A function $T$ is bijective if it is both injective and surjective, meaning that for every $\mathbf{y} \in \mathbb{R}^n$, there exists a unique $\mathbf{x} \in \mathbb{R}^m$ such that $T(\mathbf{x}) = \mathbf{y}$.

如果函数 $T$ 既是单射又是满射，则称其为双射，这意味着对每个 $\mathbf{y} \in \mathbb{R}^n$，存在唯一的 $\mathbf{x} \in \mathbb{R}^m$ 使得 $T(\mathbf{x}) = \mathbf{y}$。
