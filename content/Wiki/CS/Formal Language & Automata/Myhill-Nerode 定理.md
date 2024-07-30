# Myhill-Nerode 定理 | Myhill-Nerode Theorem

## 定义 | Definition

Myhill-Nerode 定理是自动机理论中的一个重要结果，它给出了一个语言是否是正规语言（即是否可以被确定有限自动机 DFA 识别）的判定标准。该定理通过等价类的概念描述了正规语言的结构特征。

The Myhill-Nerode theorem is a fundamental result in automata theory that provides a criterion for determining whether a language is a regular language (i.e., whether it can be recognized by a deterministic finite automaton, DFA). The theorem describes the structural characteristics of regular languages through the concept of equivalence classes.

## 定理陈述 | Theorem Statement

设 $L$ 是一个定义在字母表 $\Sigma$ 上的语言。以下三个条件是等价的：

Let $L$ be a language defined over an alphabet $\Sigma$. The following three conditions are equivalent:

1. $L$ 是正规语言。
   $L$ is a regular language.
2. $L$ 的等价类集合是有限的。具体来说，存在有限个等价类，将 $\Sigma^*$ 中的所有字符串分类，使得对于任意两个字符串 $x, y \in \Sigma^*$，如果它们属于同一等价类，则对所有的 $z \in \Sigma^*$，有 $xz \in L \iff yz \in L$。
   The set of equivalence classes of $L$ is finite. Specifically, there are a finite number of equivalence classes that partition all strings in $\Sigma^*$ such that for any two strings $x, y \in \Sigma^*$, if they belong to the same equivalence class, then for all $z \in \Sigma^*$, $xz \in L \iff yz \in L$.
3. 存在一个有限状态自动机（DFA），它识别语言 $L$。
   There exists a finite state automaton (DFA) that recognizes the language $L$.

## 等价类 | Equivalence Classes

对于语言 $L \subseteq \Sigma^*$，定义一个等价关系 $\sim_L$：

For a language $L \subseteq \Sigma^*$, define an equivalence relation $\sim_L$:

对于任意 $x, y \in \Sigma^*$，

For any $x, y \in \Sigma^*$,

$$
x \sim_L y \iff \forall z \in \Sigma^* (xz \in L \iff yz \in L)
$$

这意味着 $x$ 和 $y$ 在等价类 $\sim_L$ 下是等价的，当且仅当对于所有可能的字符串 $z$，$xz$ 和 $yz$ 要么都属于 $L$，要么都不属于 $L$。

This means that $x$ and $y$ are equivalent under the equivalence relation $\sim_L$ if and only if for all possible strings $z$, either both $xz$ and $yz$ belong to $L$ or neither of them does.

## 定理证明思路 | Proof Outline

### 从 DFA 到 等价类有限性 | From DFA to Finite Equivalence Classes

1. 假设 $L$ 是由 DFA 识别的正规语言。
   Suppose $L$ is a regular language recognized by a DFA.
2. DFA 的状态数是有限的。
   The number of states in a DFA is finite.
3. 每个状态代表一个等价类，这些等价类的数量也是有限的。
   Each state represents an equivalence class, and the number of such equivalence classes is finite.

### 从 等价类有限性 到 DFA | From Finite Equivalence Classes to DFA

1. 假设语言 $L$ 的等价类数量有限。
   Suppose the number of equivalence classes of the language $L$ is finite.
2. 可以构造一个状态数等于等价类数量的 DFA。
   A DFA can be constructed with the number of states equal to the number of equivalence classes.
3. 这个 DFA 通过状态转移来区分不同的等价类，从而识别语言 $L$。
   This DFA transitions between states to distinguish different equivalence classes, thus recognizing the language $L$.

## 示例 | Example

考虑语言 $L = \{ w \in \{a, b\}^* \mid w \text{ 以 } a \text{ 结尾} \}$。

Consider the language $L = \{ w \in \{a, b\}^* \mid w \text{ ends with } a \}$.

### 构造 DFA | Constructing a DFA

1. 状态集合 $Q = \{ q_0, q_1 \}$。
   The set of states $Q = \{ q_0, q_1 \}$.
2. 初始状态 $q_0$。
   The initial state $q_0$.
3. 接受状态 $F = \{ q_1 \}$。
   The set of accepting states $F = \{ q_1 \}$.
4. 状态转移函数 $\delta$ 定义如下：
   The state transition function $\delta$ is defined as follows:

   - $\delta(q_0, a) = q_1$
   - $\delta(q_0, b) = q_0$
   - $\delta(q_1, a) = q_1$
   - $\delta(q_1, b) = q_0$

### 等价类分析 | Equivalence Class Analysis

- $x \sim_L y \iff \forall z \in \{a, b\}^* (xz \in L \iff yz \in L)$
- 对于 $w \in \{a, b\}^*$，如果 $w$ 以 $a$ 结尾，则 $w \in L$；否则，$w \notin L$。
- 分析后发现存在两个等价类：
  - $[q_0] = \{ w \in \{a, b\}^* \mid w \text{ 以 } b \text{ 结尾或为空字符串} \}$
  - $[q_1] = \{ w \in \{a, b\}^* \mid w \text{ 以 } a \text{ 结尾} \}$

## 总结 | Summary

Myhill-Nerode 定理提供了一个判定语言是否为正规语言的强大工具。通过分析语言的等价类结构，可以构造出相应的 DFA，从而验证语言的正则性。理解这一定理有助于深入理解自动机理论和正规语言的性质。

The Myhill-Nerode theorem provides a powerful tool for determining whether a language is regular. By analyzing the equivalence class structure of a language, one can construct the corresponding DFA, thereby verifying the regularity of the language. Understanding this theorem helps in gaining deeper insights into automata theory and the properties of regular languages.
