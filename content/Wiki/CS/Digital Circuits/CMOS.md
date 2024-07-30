# CMOS Transistor Level Circuit - CMOS 晶体管级电路

## Definition - 定义

**CMOS (Complementary Metal-Oxide-Semiconductor)** is a technology for constructing integrated circuits. CMOS technology is used in microprocessors, microcontrollers, static RAM, and other digital logic circuits. CMOS circuits are characterized by their low power consumption and high noise immunity.

**CMOS（互补金属氧化物半导体）**是一种构建集成电路的技术。CMOS 技术用于微处理器、微控制器、静态 RAM 以及其他数字逻辑电路。CMOS 电路的特点是低功耗和高噪声抗扰性。

## Basic Concepts - 基本概念

### Transistor - 晶体管

A transistor is a semiconductor device used to amplify or switch electronic signals and electrical power. CMOS circuits use both **n-channel MOSFETs (NMOS)** and **p-channel MOSFETs (PMOS)**.

晶体管是一种用于放大或切换电子信号和电力的半导体器件。CMOS 电路同时使用**n 沟道 MOSFET（NMOS）**和**p 沟道 MOSFET（PMOS）**。

### NMOS and PMOS

- **NMOS (n-channel MOSFET)**: When a positive voltage is applied to the gate, it creates a conductive channel between the source and drain, allowing current to flow. This means that when the input is high, the NMOS conducts, and the output is low; when the input is low, the NMOS is off, and the output is high.
- **PMOS (p-channel MOSFET)**: When a negative voltage is applied to the gate, it creates a conductive channel between the source and drain, allowing current to flow. This means that when the input is low, the PMOS conducts, and the output is high; when the input is high, the PMOS is off, and the output is low.

- **NMOS（n 沟道 MOSFET）**：当正电压施加到栅极时，会在源极和漏极之间形成导电通道，允许电流流动。这表示当输入高电平时，NMOS 导通，输出为低电平；当输入低电平时，NMOS 截止，输出为高电平。
- **PMOS（p 沟道 MOSFET）**：当负电压施加到栅极时，会在源极和漏极之间形成导电通道，允许电流流动。这表示当输入低电平时，PMOS 导通，输出为高电平；当输入高电平时，PMOS 截止，输出为低电平。

### Complementary Pair - 互补对

In CMOS circuits, **NMOS and PMOS transistors are used in pairs** to implement logic functions.

在 CMOS 电路中，**NMOS 和 PMOS 晶体管成对使用**来实现逻辑功能。

### Pull-Up and Pull-Down Networks - 上拉和下拉网络

- **Pull-Up Network**: Consists of PMOS transistors that connect the output to the positive power supply (V$_{DD}$) when the input condition is met, making the output high. Hence, it is called the "pull-up" network.
- **Pull-Down Network**: Consists of NMOS transistors that connect the output to ground (`GND`) when the input condition is met, making the output low. Hence, it is called the "pull-down" network.

- **上拉网络**：由 PMOS 晶体管组成，当输入条件满足时将输出连接到正电源（V$_{DD}$）。当上拉网络中的 PMOS 导通时，输出为高电平，因此叫做“上拉”网络。
- **下拉网络**：由 NMOS 晶体管组成，当输入条件满足时将输出连接到地（`GND`）。当下拉网络中的 NMOS 导通时，输出为低电平，因此叫做“下拉”网络。

## Typical CMOS Gate Logic Circuit - 典型 CMOS 门逻辑电路

### Complementary Nature of CMOS Circuits - CMOS 电路的互补性质

**Notice**: Since CMOS circuits will naturally convert the input to the complement form, we have to design the circuit based on the complement form of the input variables or the complement form of the Boolean expression.

**注意**：由于 CMOS 电路会自然地将输入转换为补码形式，我们必须根据输入变量的补码形式或布尔表达式的补码形式设计电路。

> For example, a single input variable will be corresponded to a complementary pairs of transistors. When input is high, the PMOS is OFF, and the NMOS is ON, and the output is low. When input is low, the PMOS is ON, and the NMOS is OFF, and the output is high.
>
> 例如，单个输入变量将对应于一对互补的晶体管。当输入为高电平时，PMOS 截止，NMOS 导通，输出为低电平。当输入为低电平时，PMOS 导通，NMOS 截止，输出为高电平。

### Schematic Diagram - 示意图

A typical CMOS gate logic circuit consists of the following components and features:

1. **Power Supply (V$_{DD}$) and Ground (`GND`)**: The power supply, usually at 5V, is connected to the PMOS transistors, and the ground is connected to the NMOS transistors.
2. **PMOS Transistors**: These transistors are used in the pull-up network, which connects the output to V$_{DD}$ when the input condition is met.
3. **NMOS Transistors**: These transistors are used in the pull-down network, which connects the output to GND when the input condition is met.
4. **Input and Output Nodes**: The input nodes receive the Boolean variables, and the output node provides the result of the logic operation.

典型的 CMOS 门逻辑电路包括以下组件和特征：

1. **电源 (V$_{DD}$) 和接地 (GND)**：电源通常为 5V，连接到 PMOS 晶体管，接地连接到 NMOS 晶体管。
2. **PMOS 晶体管**：这些晶体管用于**上拉网络**，当输入条件满足时将输出连接到 V$_{DD}$。
3. **NMOS 晶体管**：这些晶体管用于**下拉网络**，当输入条件满足时将输出连接到 GND。
4. **输入和输出节点**：输入节点接收布尔变量，输出节点提供逻辑运算的结果。

### Drawing Components - 元件绘图

- **Transistor Symbols**:
  - **PMOS Transistor**: Typically drawn with the source connected to V$_{DD}$, the drain connected to the output, and the gate receiving the input signal. The arrow on the PMOS transistor points outwards.
  - **NMOS Transistor**: Typically drawn with the source connected to GND, the drain connected to the output, and the gate receiving the input signal. The arrow on the NMOS transistor points inwards.
- **Connecting Wires**: Clear lines representing the connections between transistors and between transistors and power supply/ground.

- **晶体管符号**：
  - **PMOS 晶体管**：通常绘制时源极连接到 V$_{DD}$，漏极连接到输出，栅极接收输入信号。PMOS 晶体管上的箭头指向外。
  - **NMOS 晶体管**：通常绘制时源极连接到 GND，漏极连接到输出，栅极接收输入信号。NMOS 晶体管上的箭头指向内。
- **连接导线**：表示晶体管之间以及晶体管与电源/地之间连接的清晰线条。

### Symbolic Representation of PMOS and NMOS Transistors - PMOS 和 NMOS 晶体管的符号表示

**PMOS**: ON when input is low (0), OFF when input is high (1).

```plaintext
                     Drain(Output)
                     |
                     |
              |------|
Gate(Input)-O| |
              |------|
                     |
                     |
                     Source(GND)
```

**NMOS**: ON when input is high (1), OFF when input is low (0).

```plaintext
                     Source(VDD)
                     |
                     |
              |------|
Gate(Input)--| |
              |------|
                     |
                     |
                     Drain(Output)
```

### Boolean Function Implementation - 布尔函数实现

Suppose we have connected the input to the gate of the transistors and the output to the drain of the transistors. PMOS & NMOS transistors act complementary to each other. When PMOS is ON, NMOS is OFF, and vice versa. Thus, we have to calculate the Boolean expression both with input variables and the complement of input variables to design the CMOS circuit.

假设我们已经将输入连接到晶体管的栅极，将输出连接到晶体管的漏极。PMOS 和 NMOS 晶体管互补作用。当 PMOS 导通时，NMOS 截止，反之亦然。因此，我们必须计算带有输入变量和输入变量的补码的布尔表达式，以设计 CMOS 电路。

We can use De Morgan's theorem to simplify the expression and maximize the use of complementary pairs.

我们可以使用德摩根定律来简化表达式，并最大化使用互补对。

#### Basic CMOS Logic Gates - 基本 CMOS 逻辑门

1. `AND` Gate: $P = A \cdot B$
    - Pull-Up Network: $P1 = A \cdot B$
    - Pull-Down Network: $P2 = \

overline{A} + \overline{B}$

2. `OR` Gate: $P = A + B$
    - Pull-Up Network: $P1 = A + B$
    - Pull-Down Network: $P2 = \overline{A} \cdot \overline{B}$

3. `NOT` Gate: $P = \overline{A}$

### A General Recipe for Designing CMOS Circuits - 设计 CMOS 电路的步骤

1. Choose to write the complementary form of the Boolean expression in terms of input variables or the Boolean expression itself in terms of the complement of the input variables, whichever is simpler. (e.g.: $P' = \overline{A \cdot B}$ or $P = \overline{A} + \overline{B}$. In the former, we will use $A$ and $B$ as inputs and add a `NOT` gate at the output; in the latter, we will use $\overline{A}$ and $\overline{B}$ as inputs, i.e., inputs are added with `NOT` gates.)
2. Apply **De Morgan's theorem** to simplify the expression.
3. Design the pull-up network using **PMOS** transistors, according to the simplified expression in **the complement form of the input variables**.
4. Design the pull-down network using **NMOS** transistors, according to the simplified expression in the input variables form.
5. Connect V$_{DD}$ to the pull-up network and `GND` to the pull-down network, and connect the output to the drain of both pull-up and pull-down networks.

---

1. 选择根据输入变量的补码形式编写布尔表达式的互补形式，或者根据输入变量的补码形式编写布尔表达式本身，以简化表达式。（例如：$P' = \overline{A \cdot B}$ 或 $P = \overline{A} + \overline{B}$。前者我们将使用 $A$ 和 $B$ 作为输入并在输出加上一个 `NOT` 门；后者我们将使用 $\overline{A}$ 和 $\overline{B}$ 作为输入，即输入分别加上 `NOT` 门。）
2. 应用**德摩根定律**简化表达式。
3. 根据输入变量的补码形式中的简化表达式设计使用 PMOS 晶体管的上拉网络。
4. 根据输入变量形式中的简化表达式设计使用 NMOS 晶体管的下拉网络。
5. 将 V$_{DD}$ 连接到上拉网络，将 `GND` 连接到下拉网络，并将输出连接到上拉和下拉网络的漏极。

**Note**: The circuit of pull-up and pull-down networks are usually complementary to each other. If we connect PMOS in series in the pull-up network, we connect NMOS in parallel in the pull-down network, and vice versa.

**注意**：上拉和下拉网络的电路通常互补。如果我们在上拉网络中串联 PMOS，我们在下拉网络中并联 NMOS，反之亦然。
