# AVL Tree | AVL 树

## Introduction | 简介

An AVL tree is a self-balancing binary search tree where the difference between the heights of the left and right subtrees of any node (known as the balance factor) is at most 1. This property ensures that the tree remains approximately balanced, which guarantees that the height of the tree is $O(\log n)$, where $n$ is the number of nodes. This makes AVL trees efficient for search, insertion, and deletion operations, each of which runs in $O(\log n)$ time.

AVL 树是一种自平衡二叉搜索树，其中任一节点的左子树和右子树的高度差（即平衡因子）最多为 1。该属性确保了树始终保持大致平衡，从而保证了树的高度为 $O(\log n)$，其中 $n$ 是节点的数量。这使得 AVL 树在查找、插入和删除操作中都具有 $O(\log n)$ 的时间复杂度。

The "AVL" in AVL tree stands for the initials of the surnames of the inventors of this data structure. The tree was introduced in 1962 by Russian mathematicians G. M. Adelson-Velsky and E. M. Landis. Therefore, "AVL" in AVL tree comes from the surnames **Adelson-Velsky** and **Landis**.

AVL 树中的“AVL”表示的是该数据结构的发明者的姓氏缩写。这种树是由俄罗斯数学家 G. M. Adelson-Velsky 和 E. M. Landis 在 1962 年共同提出的，因此，AVL 树中的“AVL”分别取自这两位发明者的姓氏**Adelson-Velsky**和**Landis**。

## Balance Factor | 平衡因子

The balance factor for a node in an AVL tree is defined as the difference between the heights of its left and right subtrees:

在 AVL 树中，某个节点的平衡因子定义为其左子树和右子树高度之间的差值：

$$
\text{Balance Factor} = \text{Height of Left Subtree} - \text{Height of Right Subtree}
$$

If the balance factor of any node is not in the set $\{-1, 0, 1\}$, the tree needs to be rebalanced.

如果任一节点的平衡因子不属于集合 $\{-1, 0, 1\}$，则需要对树进行再平衡。

## Rotations | 旋转

To maintain the balance of an AVL tree after insertion or deletion, rotations are used. There are four types of rotations:

为了在插入或删除后保持 AVL 树的平衡，需要使用旋转操作。旋转操作分为四种类型：

1. **Right Rotation (Single Rotation) | 右旋（单旋转）**
2. **Left Rotation (Single Rotation) | 左旋（单旋转）**
3. **Left-Right Rotation (Double Rotation) | 左右旋（双旋转）**
4. **Right-Left Rotation (Double Rotation) | 右左旋（双旋转）**

### Right Rotation | 右旋

This is applied when the left subtree is taller and the imbalance occurs in the left child of the left subtree.

当左子树比右子树高且不平衡发生在左子树的左子节点时，应用此旋转。

```
T1, T2, T3, and T4 are subtrees.
          y                                      x
         / \                                   /   \
        x   T4      Right Rotate (y)          z     y
       / \          - - - - - - - - ->      /  \   /  \ 
      z   T3                                T1  T2 T3  T4
     / \
   T1   T2
```

### Left Rotation | 左旋

This is applied when the right subtree is taller and the imbalance occurs in the right child of the right subtree.

当右子树比左子树高且不平衡发生在右子树的右子节点时，应用此旋转。

```
T1, T2, T3, and T4 are subtrees.
          x                                   y
         /  \                               /   \ 
        T1   y      Left Rotate(x)         x     z
            /  \   - - - - - - - ->       /  \   /  \ 
           T2   z                        T1  T2 T3  T4
               /  \
             T3   T4
```

### Left-Right Rotation | 左右旋

This is a combination of a left rotation followed by a right rotation. It is applied when the left subtree is taller and the imbalance occurs in the right child of the left subtree.

这是先左旋再右旋的组合。当左子树比右子树高且不平衡发生在左子树的右子节点时，应用此旋转。

```
Left Rotation: x's left child (z) is rotated to the left.
Right Rotation: y (z's parent) is rotated to the right.
```

### Right-Left Rotation | 右左旋

This is a combination of a right rotation followed by a left rotation. It is applied when the right subtree is taller and the imbalance occurs in the left child of the right subtree.

这是先右旋再左旋的组合。当右子树比左子树高且不平衡发生在右子树的左子节点时，应用此旋转。

```
Right Rotation: y's right child (z) is rotated to the right.
Left Rotation: x (z's parent) is rotated to the left.
```

## Insertion | 插入

When a new node is inserted into an AVL tree, it is first added like in a regular binary search tree. After insertion, the tree is checked for balance starting from the node's parent up to the root. If an imbalance is detected, the appropriate rotation(s) are performed to restore balance.

在 AVL 树中插入新节点时，首先按照普通二叉搜索树的方式添加节点。插入后，从节点的父节点开始一直到根节点检查树的平衡。如果检测到不平衡，则执行适当的旋转操作以恢复平衡。

## Deletion | 删除

Deletion in an AVL tree also follows the deletion process of a binary search tree. After deleting a node, the tree is checked for balance starting from the node's parent up to the root. If an imbalance is detected, the necessary rotations are performed to restore balance.

AVL 树中的删除操作也遵循二叉搜索树的删除过程。删除节点后，从节点的父节点开始一直到根节点检查树的平衡。如果检测到不平衡，则执行必要的旋转操作以恢复平衡。

## Summary | 总结

AVL trees are powerful data structures that maintain balance through rotations. They ensure that all basic operations such as search, insertion, and deletion remain efficient, with a time complexity of $O(\log n)$. Understanding how rotations work is crucial for working with AVL trees.

AVL 树是一种通过旋转操作保持平衡的强大数据结构。它们确保了所有基本操作，如查找、插入和删除，都保持高效，具有 $O(\log n)$ 的时间复杂度。理解旋转操作的工作原理是使用 AVL 树的关键。
