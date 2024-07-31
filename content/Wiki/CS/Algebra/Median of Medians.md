# Median of Medians | 中位数中的中位数算法

## Definition | 定义

The **Median of Medians** algorithm is a selection algorithm used to find the median of an unsorted list. It can also be used as a pivot selection strategy for the Quickselect algorithm, guaranteeing worst-case linear time complexity. This algorithm divides the input array into smaller groups of size $m$, finds the median of each group, and then recursively finds the median of these medians.

**中位数中的中位数**算法是一种用于在无序列表中找到中位数的选择算法。它还可以用作快速选择（Quickselect）算法的主元选择策略，保证最坏情况下的线性时间复杂度。该算法将输入数组分成大小为 $m$ 的小组，找到每组的中位数，然后递归地找到这些中位数的中位数。

## Algorithm Steps | 算法步骤

1. **Divide the array into groups of size $m$**: If the number of elements in the array is not divisible by $m$, the last group may have fewer than $m$ elements.

   **将数组分成 $m$ 个一组**：如果数组中的元素数量不能被 $m$ 整除，最后一组可能少于 $m$ 个元素。

2. **Sort each group and find the median**: Sort each group and identify the median. For a group of $m$, the median is the $\left\lfloor \frac{m}{2} \right\rfloor$-th element after sorting.

   **对每组进行排序并找到中位数**：对每组进行排序，并确定中位数。对于 $m$ 个一组的情况，中位数是排序后的第 $\left\lfloor \frac{m}{2} \right\rfloor$ 个元素。

3. **Collect the medians**: Create a new array that contains all the medians from the previous step.

   **收集中位数**：创建一个包含上一步中所有中位数的新数组。

4. **Find the median of medians**: Recursively apply the Median of Medians algorithm to the new array to find its median.

   **找到中位数中的中位数**：递归地对新数组应用中位数中的中位数算法，以找到其中位数。

5. **Partition the original array**: Use the median of medians as the pivot to partition the original array into elements less than, equal to, and greater than the pivot.

   **分区原始数组**：使用中位数中的中位数作为主元，将原始数组分区为小于、等于和大于主元的元素。

6. **Recursively select**: Depending on the desired order statistic (e.g., the k-th smallest element), recursively select from the appropriate partition.

   **递归选择**：根据所需的顺序统计量（例如，第 k 小的元素），从适当的分区递归选择。

## Time Complexity Analysis | 时间复杂度分析

### Analysis | 分析

To understand why the worst-case partition size is $\frac{m+1}{2m}n$, consider the following process:

理解为什么最坏情况下的分区大小是 $\frac{m+1}{2m}n$，可以考虑以下过程：

- **Grouping and Medians**: The algorithm divides the array into groups of size $m$ and sorts each group. The median of each group, which is the $\left\lfloor \frac{m}{2} \right\rfloor$-th element in the sorted order, is collected into a new array. The median of medians is then chosen as the pivot for partitioning the original array.

  **分组与中位数**：算法将数组分成大小为 $m$ 的组并对每组进行排序。每组的中位数，即排序后的第 $\left\lfloor \frac{m}{2} \right\rfloor$ 个元素，被收集到一个新的数组中。然后选择中位数中的中位数作为原始数组的主元进行分区。

- **Partitioning Based on the Pivot**: In the worst case, the algorithm aims to achieve a balanced partitioning of the array into elements smaller than, equal to, and greater than the pivot. Specifically, the goal is to ensure that the number of elements in the larger subset after partitioning is minimized.

  **基于主元的分区**：在最坏情况下，算法旨在实现数组的平衡分区，即将数组分成小于、等于和大于主元的元素。具体来说，目标是确保分区后较大子集中的元素数量最小化。

Now, let's delve into the contribution of each group towards the elements smaller and larger than the pivot:

现在，让我们详细讨论每组对小于和大于主元的元素集的贡献：

1. **Groups with Median Less than Pivot**: For any group whose median is less than **the median of medians**, there must be at least half of its elements (i.e., $\left\lfloor \frac{m}{2} \right\rfloor$) that are also less than the pivot. This is because the median of the group is a middle element, ensuring that at least half the group is on either side. Therefore, these groups collectively contribute a significant number of elements to the subset of elements smaller than the pivot.

   **中位数小于主元的组**：对于中位数小于**中位数中位数**的组，至少有一半的元素（即 $\left\lfloor \frac{m}{2} \right\rfloor$）也小于主元。这是因为组的中位数是中间元素，确保至少有一半的组元素位于任一侧。因此，这些组总共为小于主元的元素集贡献了大量元素。

2. **Groups with Median Greater than Pivot**: Similarly, for groups whose median is greater than **the median of medians**, at least $\left\lfloor \frac{m}{2} \right\rfloor$ elements are greater than the pivot. This is due to the symmetric property of the median within each sorted group.

   **中位数大于主元的组**：同样地，对于中位数大于**中位数中位数**的组，至少有 $\left\lfloor \frac{m}{2} \right\rfloor$ 个元素大于主元。这是由于每个排序组中的中位数的对称性质。

By these principles, **for each half of the groups**, there will be at least $\left\lfloor \frac{m}{2} \right\rfloor$ elements that are guaranteed to be on the correct side of the partition relative to the pivot (median of medians). Thus, the worst-case size of one partition (say, the larger partition) will contain at most $\frac{m+1}{2m}n$ elements. This is derived from the fact that each group with a median less than the pivot contributes at least half of its elements to the set of elements less than the pivot, and vice versa for those greater than the pivot.

基于这些原则，对于每一半的组，将有至少 $\left\lfloor \frac{m}{2} \right\rfloor$ 个元素保证在相对于主元的正确分区一侧。因此，最坏情况下一个分区（假设是较大的分区）的大小最多包含 $\frac{m+1}{2} \frac{n}{m}$ 个元素。这源于以下事实：对于中位数小于主元的组，每组至少有一半的元素会被分配到小于主元的元素集中，反之亦然。

### Recurrence Relation | 递推关系

The time complexity of the Median of Medians algorithm can be analyzed using a recurrence relation that captures the cost of each step:

中位数中的中位数算法的时间复杂度可以使用递推关系进行分析，该递推关系捕获每一步的成本：

$$
T(n) \leq T\left(\frac{n}{m}\right) + T\left(\frac{m+1}{2m}n\right) + O(n)
$$

- **$T\left(\frac{n}{m}\right)$**: Time complexity to find the median of the medians. This involves finding the median of a list of medians, which is derived from dividing the array into groups of $m$, finding their medians, and then finding the median of those medians recursively.

  **$T\left(\frac{n}{m}\right)$**：找到中位数的中位数的时间复杂度。这包括从将数组分成 $m$ 个一组、找到它们的中位数，然后递归地找到这些中位数中的中位数。

- **$T\left(\frac{m+1}{2m}n\right)$**: The term $T\left(\frac{m+1}{2m}n\right)$ arises from the worst-case scenario of the partitioning step. After selecting the pivot (the median of medians), the array is divided into elements smaller and larger than the pivot. The worst-case occurs when the pivot divides the array such that one partition contains at most $\frac{m+1}{2m}n$ elements, while the other contains the rest. This is based on the observation that the median of medians is at least better than $\frac{m-1}{2m}$ of the elements, thus guaranteeing that at least $\frac{m-1}{2}$ of elements are greater and at least $\frac{m-1}{2}$ are smaller.

  **$T\left(\frac{m+1}{2m}n\right)$**：这个项来源于分区步骤的最坏情况。在选择主元（中位数中的中位数）后，数组被分成小于和大于主元的元素。最坏情况下，主元将数组分为最多 $\frac{m+1}{2m}n$ 个元素的一个部分，其余的在另一部分。这是基于观察到的中位数中的中位数至少比 $\frac{m-1}{2m}$ 的元素更好，从而保证至少 $\frac{m-1}{2}$ 的元素比它大，至少 $\frac{m-1}{2}$ 的元素比它小。

- **$O(n)$**: Time complexity for dividing the array into groups and partitioning around the pivot. This step involves linear operations, such as splitting the array into smaller parts and rearranging elements based on the pivot.

  **$O(n)$**：将数组分组并围绕主元分区的时间复杂度。此步骤涉及线性操作，例如将数组分成较小的部分和根据主元重新排列元素。

The recurrence relation can be analyzed using the Master Theorem for divide-and-conquer recurrences. In this case, $a = 1$, $b = \frac{m}{m+1}$, and $f(n) = O(n)$. According to the Master Theorem, we compare $f(n)$ with $n^{\log_b a}$.

该递推关系可以使用分治递归的主定理进行分析。在本例中，$a = 1$，$b = \frac{m}{m+1}$，$f(n) = O(n)$。根据主定理，我们将 $f(n)$ 与 $n^{\log_b a}$ 进行比较。

Here, $n^{\log_b a} = n^{\log_{m/(m+1)} 1} = n^0 = 1$. Since $f(n) = O(n)$ grows faster than $n^{\log_b a}$, we conclude that $f(n)$ dominates the recurrence relation. Therefore, by the Master Theorem, the time complexity $T(n)$ is given by $f(n)$.

这里，$n^{\log_b a} = n^{\log_{m/(m+1)} 1} = n^0 = 1$。由于 $f(n) = O(n)$ 增长速度快于 $n^{\log_b a}$，因此我们得出 $f(n)$ 在递推关系中占主导地位。因此，根据主定理，时间复杂度 $T(n)$ 由 $f(n)$ 决定。

Thus, the final time complexity of the Median of Medians algorithm is $T(n) = O(n)$, indicating that the algorithm runs in linear time.

因此，中位数中的中位数算法的最终时间复杂度为 $T(n) = O(n)$，这表明该算法以线性时间运行。

### Determining the Value of $m$ | 确定 $m$ 的值

The choice of $m$ affects both the practical performance and theoretical guarantees of the algorithm. Typically, $m = 5$ is chosen because it provides a good balance between the simplicity of implementation and the efficiency of the algorithm. However, the value of $m$ can be adjusted based on the specific requirements and constraints of the application:

1. **For Smaller $m$**: The algorithm performs more recursive calls but with a smaller number of elements. This can be useful when the cost of dividing and conquering is high, and fewer elements can be handled in each group.

   **较小的 $m$**：算法进行更多的递归调用，但元素数量较少。这在分治成本高且每组能处理的元素较少时很有用。

2. **For Larger $m$**: The groups are larger, and thus the number of recursive calls is reduced. However, sorting larger groups and finding the median may become computationally expensive.

   **较大的 $m$**：组更大，因此递归调用的次数减少。然而，排序较大的组和找到中位数可能会变得计算昂贵。

In practical applications, $m = 5$ is often a good default choice. For specific datasets or hardware, experimentation may determine that a different $m$ is more optimal.

在实际应用中，$m = 5$ 通常是一个不错的默认选择。对于特定的数据集或硬件，实验可能会确定不同的 $m$ 更为优化。

## Code Implementation | 代码实现

```python
def median_of_medians(arr, k, m=5):
    if len(arr) <= m:
        return sorted(arr)[k]

    # Step 1: Divide array into groups of m
    sublists = [arr[j:j + m] for j in range(0, len(arr), m)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    median_of_medians = median_of_medians(medians, len(medians) // 2, m)

    # Step 2: Partition the array around the median of medians
    low = [el for el in arr if el < median_of_medians]
    high = [el for el in arr if el > median_of_medians]
    pivot_count = len(arr) - len(low) - len(high)

    if k < len(low):
        return median_of_medians(low, k, m)
    elif k < len(low) + pivot_count:
        return median_of_medians
    else:
        return median_of_medians(high, k - len(low) - pivot_count, m)
```

This implementation includes the crucial steps: dividing the array into groups of size $m$, finding the medians, selecting the median of medians, and partitioning around it. The recursive selection process ensures the desired element is found efficiently even in the worst case.

该实现包括关键步骤：将数组分成大小为 $m$ 的组、找到中位数、选择中位数中的中位数以及围绕其分区。递归选择过程确保即使在最坏情况下也能有效找到所需元素。
