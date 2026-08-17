# LIWEELI Green Computing Architecture

**文档** | **中文版** | **社区** | **加入讨论** | **License** | **Apache 2.0**

---

A scalable open‑source computing framework based on **3D heterogeneous stacking** and **real‑world signal‑driven online learning** — designed for energy‑efficient, physically‑grounded, and continuously adapting systems.

---

## The Vision

We envision a future where computational capacity is as accessible, affordable, and environmentally sustainable as water and electricity.

This architecture is not a fixed design. It is a **framework** — a way of organising computation around physical signals, causal continuity, and adaptive learning — that can be implemented across diverse technologies and application domains.

---

## Core Principles

### 1. Real‑World Signal Directly Ingested

The system reads continuous physical signals (light, sound, vibration, magnetic fields) **without** discretising them into tokens or digital samples. The input is the physical event itself, preserving its original phase and timing information.

### 2. Linear Fidelity in Processing

Once ingested, signals are transformed linearly (e.g., via Fourier decomposition) into frequency, phase, and amplitude components. This step:

- Preserves the original causal timing of the signal
- Keeps all operations traceable to the physical input
- Does not introduce non‑linear distortion or “guessing”

### 3. Noise Removal Without Signal Distortion

Instrument‑generated noise (thermal, quantisation, etc.) is removed via linear filtering **strictly scoped to the instrument‑noise band**. This cleans the canvas without repainting the image — the physical information remains untouched.

### 4. Controlled Non‑Linear Repair

When signals overlap or become entangled (e.g., through atmospheric scattering), linear processing alone cannot fully restore the original causal chain. In such cases, **model‑based sparse reconstruction** is used — but only when:

- The channel and source models are physically defined
- No generative fill or diffusion prior is allowed
- The goal is to restore continuity, not to invent missing content

### 5. Online Learning Through Temporal Association

The system does not rely on offline backpropagation or frozen weights. Instead, it learns through **temporal correlation** — patterns that repeatedly co‑occur are associatively strengthened in real time. This enables:

- Continuous, incremental adaptation
- No separation between “training” and “inference” phases
- Learning from the physical world as it happens

### 6. Causality Preservation

Every output must be traceable back to a real physical input. There is no statistical “plausibility” without a physical anchor. This is enforced by the sequential combination of linear fidelity, controlled repair, and online associative learning.

---

## What This Architecture Solves

| Challenge | Current AI | This Framework |
| :--- | :--- | :--- |
| **Catastrophic forgetting** | New knowledge overwrites old | Online association preserves prior patterns |
| **Energy & latency** | Digital sampling + data movement dominate power | Direct signal processing reduces unnecessary conversion |
| **Hallucination / causality gap** | Statistical correlation only | Outputs must be physically traceable |

---

## How This Connects to 3D Heterogeneous Stacking

The principles above are **stacking‑agnostic** — they can be realised across different technologies. The 3D heterogeneous stacking approach is one way to implement this framework at the system level:

- **Layered integration** — different functional layers (signal ingress, transform, storage, adaptation) can be stacked vertically
- **Reduced data movement** — shorter physical paths between layers lower energy overhead
- **Flexible material / process choices** — each layer can use the most suitable technology without imposing constraints on others

This version of the architecture focuses on the stacking organisation and the signal‑processing principles. It does **not** prescribe specific logic implementations, material compositions, or proprietary techniques.

---

## Current Status & Collaboration

This framework is released for public review and community collaboration. We welcome discussions on:

- 3D stacking and heterogeneous integration approaches
- Real‑time signal processing and online learning algorithms
- System‑level co‑design for AI, edge, and sensing applications

---

## Contact

**IP Owner:** LI WEI LI  
**Email:** contact@liweili-architecture.com  
**GitHub:** [LIWEI-LI-prog](https://github.com/LIWEI-LI-prog)  
**Date:** 2026‑08‑17

---

*This document describes the architecture at the principle and stacking‑organisation level. It does not include logic‑layer implementations, detailed circuit designs, or proprietary technical parameters.*

# LIWEILI 绿色计算架构

**文档** | **English** | **社区** | **加入讨论** | **License** | **Apache 2.0**

---

一个基于 **3D 异构堆叠** 与 **真实世界信号驱动的在线学习** 的可扩展开源计算框架——面向高能效、物理锚定、持续自适应的计算系统。

---

## 愿景

我们 envision 一个计算能力像水电一样可及、平价、可持续的未来。

本架构不是一个固定的设计，而是一个 **框架** ——一种围绕物理信号、因果连续性与自适应学习来组织计算的方式，可跨多种技术与应用场景实现。

---

## 核心原则

### 1. 直接接入真实世界信号

系统直接读取连续物理信号（光、声、振动、磁场），**不经** 离散化处理为 Token 或数字样本。输入即物理事件本身，保留其原始相位与 timing 信息。

### 2. 处理中的线性保真

信号接入后，通过线性变换（如傅里叶分解）转换为频率、相位与振幅分量。此步骤：

- 保留信号的原始因果时序
- 确保所有运算可追溯至物理输入
- 不引入非线性失真或“猜测”

### 3. 无信号失真的噪声去除

仪器噪声（热噪声、量化误差等）通过 **严格限定于仪器噪声频带** 的线性滤波去除。此举清理画布而不重画图像——物理信息保持原样。

### 4. 受控非线性修复

当信号重叠或纠缠（如大气散射）时，线性处理无法完全还原原始因果链。此时使用 **基于模型的稀疏重构**，但仅当：

- 信道与源模型已物理定义
- 不允许生成式填充或扩散先验
- 目标是恢复连续性，而非凭空创造缺失内容

### 5. 通过时间关联实现在线学习

系统不依赖离线反向传播或冻结权重，而是通过 **时间相关性** 学习——重复共现的模式在实时中被关联性增强。这使得：

- 持续、增量的自适应
- 无“训练”与“推理”阶段之分
- 从物理世界中实时学习

### 6. 因果保持

每个输出必须可追溯至真实的物理输入。不存在无物理锚点的统计“合理性”。这一点通过线性保真、受控修复与在线关联学习的序列组合来保证。

---

## 本架构解决的问题

| 挑战 | 当前 AI | 本框架 |
| :--- | :--- | :--- |
| **灾难性遗忘** | 新知识覆盖旧知识 | 在线关联保留已有模式 |
| **能耗与延迟** | 数字采样 + 数据搬运主导功耗 | 直接信号处理减少不必要的转换 |
| **幻觉 / 因果缺口** | 仅统计相关 | 输出必须物理可追溯 |

---

## 与 3D 异构堆叠的关联

上述原则是 **堆叠无关的** ——可跨不同技术实现。3D 异构堆叠是在系统层面实现此框架的一种方式：

- **分层集成** ——不同功能层（信号接入、变换、存储、自适应）可垂直堆叠
- **减少数据搬运** ——层间更短的物理路径降低能耗开销
- **灵活的材料/工艺选择** ——每层可使用最适合的技术，不相互约束

本版本架构聚焦于堆叠组织与信号处理原理，**不** 指定具体逻辑实现、材料组成或专有技术。

---

## 当前状态与合作

本框架已开放供公开 review 与社区合作。欢迎以下方向的讨论：

- 3D 堆叠与异构集成方法
- 实时信号处理与在线学习算法
- AI、边缘计算与传感应用的系统级协同设计

---

## 联系方式

**IP Owner:** LI WEI LI  
**邮箱:** contact@liweili-architecture.com  
**GitHub:** [LIWEI-LI-prog](https://github.com/LIWEI-LI-prog)  
**日期:** 2026-08-17

---

*本文档描述架构于原理与堆叠组织层面，不包含逻辑层实现、详细电路设计或专有技术参数。*