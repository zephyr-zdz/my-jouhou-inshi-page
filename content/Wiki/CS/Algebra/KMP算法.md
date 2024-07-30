# KMP 算法 | KMP Algorithm

## 定义 | Definition

KMP (Knuth-Morris-Pratt) 算法是一种高效的字符串匹配算法，用于在一个文本字符串中查找一个模式字符串。与朴素的字符串匹配算法相比，KMP 算法通过部分匹配表（或称为失败函数）避免了不必要的比较，从而提高了匹配效率。

The KMP (Knuth-Morris-Pratt) algorithm is an efficient string matching algorithm used to find occurrences of a pattern string within a text string. Compared to the naive string matching algorithm, the KMP algorithm uses a partial match table (also known as the failure function) to avoid unnecessary comparisons, thus improving matching efficiency.

## 算法思想 | Algorithm Idea

KMP 算法的核心思想是利用已经匹配的信息，在模式字符串中预处理一个部分匹配表，从而在匹配过程中避免重复比较。

The core idea of the KMP algorithm is to use already matched information to preprocess a partial match table in the pattern string, thereby avoiding repeated comparisons during the matching process.

## 部分匹配表 | Partial Match Table

部分匹配表记录了模式字符串的前缀和后缀的最长公共元素的长度。

The partial match table records the length of the longest common prefix and suffix for the pattern string.

### 计算部分匹配表 | Computing the Partial Match Table

1. 初始化部分匹配表。
2. 逐步计算每个位置的部分匹配值。
3. 使用部分匹配值来跳过不必要的比较。

4. Initialize the partial match table.
5. Compute the partial match values for each position step by step.
6. Use the partial match values to skip unnecessary comparisons.

#### 伪代码 | Pseudocode

```python
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m  # 初始化部分匹配表
    length = 0  # 记录最长公共前缀和后缀的长度
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps
```

## KMP 匹配过程 | KMP Matching Process

1. 预处理模式字符串，计算部分匹配表。
2. 使用部分匹配表，在文本字符串中进行匹配。
3. 遇到不匹配时，根据部分匹配表调整模式字符串的位置。

4. Preprocess the pattern string to compute the partial match table.
5. Use the partial match table to perform the matching in the text string.
6. Adjust the position of the pattern string according to the partial match table when a mismatch occurs.

### 伪代码 | Pseudocode

```python
def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)  # 计算部分匹配表

    i = 0  # text的索引
    j = 0  # pattern的索引

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp_search(text, pattern)  # Output: Pattern found at index 10
```

## 优化版本的 KMP | Optimized KMP

在部分匹配表计算过程中，可以进一步优化，当模式字符串和前缀部分不匹配时，避免一些不必要的比较。

During the computation of the partial match table, further optimizations can be made to avoid some unnecessary comparisons when the pattern string and the prefix part do not match.

### 优化的部分匹配表计算 | Optimized LPS Computation

#### 伪代码 | Pseudocode

```python
def compute_lps_optimized(pattern):
    m = len(pattern)
    lps = [0] * m  # 初始化部分匹配表
    length = 0  # 记录最长公共前缀和后缀的长度
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # 优化部分：调整 lps 值
    for i in range(1, m):
        if lps[i] > 0 and pattern[lps[i]] != pattern[i]:
            lps[i] = lps[lps[i] - 1]

    return lps
```

### 优化版本的 KMP 搜索 | Optimized KMP Search

#### 伪代码 | Pseudocode

```python
def kmp_search_optimized(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps_optimized(pattern)  # 计算优化后的部分匹配表

    i = 0  # text的索引
    j = 0  # pattern的索引

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp_search_optimized(text, pattern)  # Output: Pattern found at index 10
```

## 示例 | Example

假设我们有以下文本和模式：

Suppose we have the following text and pattern:

```plaintext
文本 | Text:    "ABABDABACDABABCABAB"
模式 | Pattern: "ABABCABAB"
```

1. 计算优化后的部分匹配表：
   For the pattern "ABABCABAB", the optimized partial match table (lps) is:
      $[0, 0, 1, 2, 0, 1, 2, 3, 4]$.
2. 使用优化后的部分匹配表进行匹配，最终输出匹配的起始索引为 10。
   Using the optimized partial match table to match, the final output is the starting index of the match, which is 10.

## 时间复杂度 | Time Complexity

KMP 算法的时间复杂度为 $O(n + m)$，其中 $n$ 是文本的长度，$m$ 是模式的长度。预处理部分匹配表需要 $O(m)$ 时间，而匹配过程需要 $O(n)$ 时间。

The time complexity of the KMP algorithm is $O(n + m)$, where $n$ is the length of the text and $m$ is the length of the pattern. Preprocessing the partial match table takes $O(m)$ time, and the matching process takes $O(n)$ time.

## 总结 | Summary

KMP 算法通过部分匹配表有效地提高了字符串匹配的效率，避免了在匹配过程中不必要的重复比较。优化版本的 KMP 算法进一步减少了计算部分匹配表时的冗余比较，从而提升了算法的性能。理解和实现这一算法，对于处理复杂字符串匹配问题具有重要意义。

The KMP algorithm improves the efficiency of string matching by effectively using the partial match table to avoid unnecessary repeated comparisons during the matching process. The optimized version of the KMP algorithm further reduces redundant comparisons during the computation of the partial match table, thus enhancing the algorithm's performance. Understanding and implementing this algorithm is crucial for solving complex string matching problems.
