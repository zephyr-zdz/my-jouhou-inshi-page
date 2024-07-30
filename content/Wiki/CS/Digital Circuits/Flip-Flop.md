# Flip-Flop 数字电路（Flip-Flop Digital Circuit）

## 概述 (Overview)

Flip-Flop 是一种基本的数字存储电路元件，具有两个稳定状态，用于存储一个位的信息。Flip-Flop 被广泛应用于寄存器、计数器和存储单元等数字系统中。

A flip-flop is a basic digital storage circuit element that has two stable states and is used to store one bit of information. Flip-flops are widely used in registers, counters, and memory units in digital systems.

## 主要类型 (Main Types)

### SR Flip-Flop

SR (Set-Reset) Flip-Flop 是最简单的一种，由两个交叉耦合的 NOR 门或 NAND 门组成。其输入包括 Set ($\mathbf{S}$) 和 Reset ($\mathbf{R}$) 信号。

The SR (Set-Reset) flip-flop is the simplest type, consisting of two cross-coupled NOR gates or NAND gates. Its inputs include Set ($\mathbf{S}$) and Reset ($\mathbf{R}$) signals.

#### 真值表 (Truth Table)

| $\mathbf{S}$ | $\mathbf{R}$ | $\mathbf{Q}$ (Next State) | $\mathbf{Q'}$ (Complement) |
| ------------ | ------------ | ------------------------- | -------------------------- |
| 0            | 0            | No Change                 | No Change                  |
| 0            | 1            | 0                         | 1                          |
| 1            | 0            | 1                         | 0                          |
| 1            | 1            | Invalid                   | Invalid                    |

### D Flip-Flop

D (Data 或 Delay) Flip-Flop 是在 SR Flip-Flop 的基础上增加一个逻辑门来防止非法状态 ($\mathbf{S} = 1, \mathbf{R} = 1$)。其输入包括 Data ($\mathbf{D}$) 和 Clock ($\mathbf{CLK}$) 信号。

The D (Data or Delay) flip-flop is based on the SR flip-flop with an additional logic gate to prevent the illegal state ($\mathbf{S} = 1, \mathbf{R} = 1$). Its inputs include Data ($\mathbf{D}$) and Clock ($\mathbf{CLK}$) signals.

#### 真值表 (Truth Table)

| $\mathbf{CLK}$ | $\mathbf{D}$   | $\mathbf{Q}$ (Next State) |
| -------------- | -------------- | ------------------------- |
| ↑ (Rising)     | 0              | 0                         |
| ↑ (Rising)     | 1              | 1                         |
| 0 or 1 or ↓    | X (Don't Care) | No Change                 |

### JK Flip-Flop

JK Flip-Flop 是对 SR Flip-Flop 的改进，解决了 $\mathbf{S} = 1, \mathbf{R} = 1$ 时的非法状态问题。其输入包括 J 和 K 信号，以及 Clock ($\mathbf{CLK}$) 信号。

The JK flip-flop is an improvement over the SR flip-flop, addressing the illegal state issue when $\mathbf{S} = 1$ and $\mathbf{R} = 1$. Its inputs include J and K signals, as well as the Clock ($\mathbf{CLK}$) signal.

#### 真值表 (Truth Table)

| $\mathbf{CLK}$ | $\mathbf{J}$   | $\mathbf{K}$   | $\mathbf{Q}$ (Next State) |
| -------------- | -------------- | -------------- | ------------------------- |
| ↑ (Rising)     | 0              | 0              | No Change                 |
| ↑ (Rising)     | 0              | 1              | 0                         |
| ↑ (Rising)     | 1              | 0              | 1                         |
| ↑ (Rising)     | 1              | 1              | $\mathbf{Q'}$ (Toggle)    |
| 0 or ↓         | X (Don't Care) | X (Don't Care) | No Change                 |

### T Flip-Flop

T (Toggle) Flip-Flop 是一种特殊的 JK Flip-Flop，当 J 和 K 都为 1 时，其输出状态会翻转。其输入包括 Toggle ($\mathbf{T}$) 和 Clock ($\mathbf{CLK}$) 信号。

The T (Toggle) flip-flop is a special type of JK flip-flop, where the output state toggles when both J and K are 1. Its inputs include the Toggle ($\mathbf{T}$) and Clock ($\mathbf{CLK}$) signals.

#### 真值表 (Truth Table)

| $\mathbf{CLK}$ | $\mathbf{T}$   | $\mathbf{Q}$ (Next State) |
| -------------- | -------------- | ------------------------- |
| ↑ (Rising)     | 0              | No Change                 |
| ↑ (Rising)     | 1              | $\mathbf{Q'}$ (Toggle)    |
| 0 or ↓         | X (Don't Care) | No Change                 |

## 应用 (Applications)

1. **寄存器 (Registers):** 用于数据存储和传输
2. **计数器 (Counters):** 实现计数功能的基本构建块
3. **频率分频器 (Frequency Dividers):** 通过翻转输出信号实现频率减半
4. **状态机 (State Machines):** 用于实现有限状态机的状态存储和转换

5. **Registers:** Used for data storage and transfer
6. **Counters:** Basic building blocks for counting functions
7. **Frequency Dividers:** Achieve frequency halving by toggling the output signal
8. **State Machines:** Used for state storage and transitions in finite state machines

## 示例代码 (Example Code)

### D Flip-Flop Verilog 实现 (D Flip-Flop Verilog Implementation)

```verilog
module DFlipFlop (
    input wire D,
    input wire CLK,
    output reg Q
);
    always @(posedge CLK) begin
        Q <= D;
    end
endmodule
```

### JK Flip-Flop Verilog 实现 (JK Flip-Flop Verilog Implementation)

```verilog
module JKFlipFlop (
    input wire J,
    input wire K,
    input wire CLK,
    output reg Q
);
    always @(posedge CLK) begin
        if (J == 0 && K == 0)
            Q <= Q; // No change
        else if (J == 0 && K == 1)
            Q <= 0;
        else if (J == 1 && K == 0)
            Q <= 1;
        else
            Q <= ~Q; // Toggle
    end
endmodule
```

### T Flip-Flop Verilog 实现 (T Flip-Flop Verilog Implementation)

```verilog
module TFlipFlop (
    input wire T,
    input wire CLK,
    output reg Q
);
    always @(posedge CLK) begin
        if (T)
            Q <= ~Q; // Toggle
    end
endmodule
```

## 注意事项 (Notes)

1. **时钟信号 (Clock Signal):** Flip-Flop 的输出状态变化通常在时钟信号的上升沿或下降沿发生
2. **异步和同步复位 (Asynchronous and Synchronous Reset):** 在某些设计中，复位信号可以是异步的（不依赖时钟信号）或同步的（依赖时钟信号）
3. **建立时间和保持时间 (Setup and Hold Time):** 数据输入信号需要在时钟信号到达前的某一段时间内保持稳定（建立时间），并在时钟信号到达后的某一段时间内继续保持稳定（保持时间）

4. **Clock Signal:** The output state of a flip-flop usually changes on the rising or falling edge of the clock signal
5. **Asynchronous and Synchronous Reset:** In some designs, the reset signal can be asynchronous (independent of the clock signal) or synchronous (dependent on the clock signal)
6. **Setup and Hold Time:** The data input signal needs to remain stable for a certain period before the clock signal arrives (setup time) and continue to remain stable for a certain period after the clock signal arrives (hold time)

这份 Flip-Flop 数字电路的中英双语 Wiki 介绍了 Flip-Flop 的主要类型、应用和注意事项，同时提供了 Verilog 实现的示例代码，有助于理解和应用 Flip-Flop 电路。
