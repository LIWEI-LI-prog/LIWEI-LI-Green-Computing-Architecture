# LIWEI LI Green Computing Architecture 🌱

[![中文](https://img.shields.io/badge/文档-中文版-brightgreen)](README_ZH.md)
[![Discussions](https://img.shields.io/badge/社区-加入讨论-blue)](https://github.com/liwei-li/IMWEI-LI-Green-Computing-Architecture/discussions)
[![Apache License 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

**A revolutionary open-source computing architecture leveraging ternary logic and photonic interconnects to break through energy and bandwidth walls.**

---

## 🚀 The Vision

We envision a future where powerful computational capacity is as accessible, affordable, and environmentally sustainable as water and electricity.

## 💡 Core Innovation: "4+1" Architecture

### 🧠 Ternary Computing
- **What**: Three-state logic (-1, 0, +1) beyond traditional binary
- **Why**: Higher information density, reducing computational complexity
- **Example**: Ternary full adder uses 37.5% fewer gates

### 🔦 Photonic Interconnects  
- **What**: Using light instead of electricity for data movement
- **Why**: Eliminates "memory wall" and "bandwidth wall"

## 🎯 Get Started

We welcome contributors from all backgrounds!

**Quick Start:**
1. ⭐ **Star this repo** to show your support
2. 🐛 **Explore [Good First Issues](https://github.com/liwei-li/IMWEI-LI-Green-Computing-Architecture/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22)** - find beginner-friendly tasks
3. 💬 **Join [Discussion](https://github.com/liwei-li/IMWEI-LI-Green-Computing-Architecture/discussions)** - share your ideas
4. 🐛 **Report an [Issue](https://github.com/liwei-li/IMWEI-LI-Green-Computing-Architecture/issues/new)** - found a bug or have a suggestion?

from src.core.ternary_logic import TernaryLogic, TernaryState

# Create ternary logic instance
logic = TernaryLogic()

# Perform ternary operations
result = logic.and_gate(TernaryState.TRUE, TernaryState.UNKNOWN)
print(f"TRUE AND UNKNOWN = {result}")

# More complex operations
a = TernaryState.TRUE
b = TernaryState.FALSE
c = TernaryState.UNKNOWN

ternary_result = logic.ternary_add(a, b, c)
print(f"Ternary addition result: {ternary_result}")

## 💻 代码示例

from src.core.ternary_logic import TernaryLogic, TernaryState

# Create ternary logic instance
logic = TernaryLogic()

# Perform ternary operations
result = logic.and_gate(TernaryState.TRUE, TernaryState.UNKNOWN)
print(f"TRUE AND UNKNOWN = {result}")

# More complex operations
a = TernaryState.TRUE
b = TernaryState.FALSE
c = TernaryState.UNKNOWN

ternary_result = logic.ternary_add(a, b, c)
print(f"Ternary addition result: {ternary_result}")

from src.architecture.fourplus1_architecture import FourPlusOneArchitecture

# Create architecture instance
arch = FourPlusOneArchitecture()

# Analyze performance
performance = arch.analyze_performance()
print(f"Energy Efficiency: {performance['energy_efficiency']:.2f} TOPS/W")
print(f"Bandwidth: {performance['bandwidth']:.2f} Tbps")

# Generate technical report
report = arch.generate_technical_report()
print(report.summary)

# Install dependencies
pip install -r requirements.txt

# Run demo
python examples/simple_demo.py

# 1. Clone the project
git clone https://github.com/LIWEI-LI/LIWEI-LI-Green-Computing-Architecture.git
cd LIWEI-LI-Green-Computing-Architecture

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run tests
python -m pytest tests/ -v

# 4. Run demo
python examples/simple_demo.py

# Run all tests
pytest tests/

# Run specific test with verbose output
pytest tests/test_ternary.py -v

# Run tests with coverage report
pytest tests/ --cov=src --cov-report=html

# Run performance benchmarks
python examples/performance_benchmark.py


from src.architecture.fourplus1_architecture import FourPlusOneArchitecture

# Create architecture instance
arch = FourPlusOneArchitecture()

# Analyze performance
performance = arch.analyze_performance()
print(f"Energy Efficiency: {performance['energy_efficiency']:.2f} TOPS/W")
print(f"Bandwidth: {performance['bandwidth']:.2f} Tbps")

# Generate technical report
report = arch.generate_technical_report()
print(report.summary)

from src.core.ternary_computing import TernaryLogic, TernaryState

# 创建三元逻辑实例
logic = TernaryLogic()

# 执行三元运算
result = logic.and_gate(TernaryState.TRUE, TernaryState.UNKNOWN)
print(f"TRUE AND UNKNOWN = {result}")

from src.architecture.fourplus1_architecture import FourPlusOneArchitecture

# 创建架构实例
arch = FourPlusOneArchitecture()

# 分析性能
performance = arch.calculate_performance()
print(f"Energy Efficiency: {performance['energy_efficiency_tops_per_w']:.2f} TOPS/W")

# 生成技术报告
print(arch.generate_technical_summary())

# 运行所有测试
pytest tests/

# 运行特定测试
pytest tests/test_ternary.py -v

# 带覆盖率的测试
pytest tests/ --cov=src --cov-report=html

## 🚀 快速体验

### 在线运行

**转化为具体研究问题：**

1.  **蓝光波导损耗课题**：如何为 450nm 蓝光设计与制造片上低损耗光波导？目标：在硅或氮化硅衬底上实现 **< 10 dB/cm** 的传播损耗。需研究新型波导截面几何与包层材料。
2.  **FMOS驱动速度课题**：如何提升金属氧化物半导体（如 IGZO）的迁移率与电流驱动能力，以实现对微型LED的 **>1 GHz** 直接强度调制？需探索新材料栈（如多层氧化物）与器件结构。
3.  **异质集成热预算课题**：在将 GaN LED 晶圆与 FMOS 晶圆进行键合时，如何将整个工艺流程的最高温度控制在 **< 250°C** 以下，以避免下层 FMOS 器件性能退化？需开发超低温键合与金属化工艺。
4.  **三元逻辑实现课题**：如何在 FMOS 器件中物理实现稳定、可靠的三元逻辑态（-Vdd, 0, +Vdd）？需设计创新的电路架构，并通过 SPICE 仿真与测试芯片进行验证。

# 1. 克隆项目
git clone https://github.com/LIWEI-LI/LIWEI-LI-Green-Computing-Architecture.git
cd LIWEI-LI-Green-Computing-Architecture

# 2. 安装依赖（可选）
pip install numpy

# 3. 运行演示
python examples/simple_demo.py

from src.ternary import TernaryLogic

# 体验三元计算
result = TernaryLogic.AND(1, 0)  # TRUE AND UNKNOWN
print(f"结果: {result}")


from src.ternary import TernaryLogic

def test_ternary_logic():
    """测试三元逻辑"""
    assert TernaryLogic.AND(1, 1) == 1
    assert TernaryLogic.AND(1, 0) == 0
    assert TernaryLogic.AND(1, -1) == -1
    
    assert TernaryLogic.OR(-1, -1) == -1
    assert TernaryLogic.OR(-1, 0) == 0
    assert TernaryLogic.OR(-1, 1) == 1
    
    assert TernaryLogic.NOT(1) == -1
    assert TernaryLogic.NOT(0) == 0
    assert TernaryLogic.NOT(-1) == 1

def test_conversion():
    """测试值转换"""
    assert TernaryLogic.to_ternary(0.8) == 1
    assert TernaryLogic.to_ternary(0.2) == 0
    assert TernaryLogic.to_ternary(-0.5) == -1

if __name__ == "__main__":
    test_ternary_logic()
    test_conversion()
    print("✅ 所有测试通过!")

# 1. 克隆项目
git clone https://github.com/LIWEI-LI/Green-Computing-Arch
**Status Legend:**
- 🟢 **Active Development** - Ready for contributions
- 🟡 **Planning Phase** - In design, discussions welcome  
- 🔵 **Foundation Ready** - Basic framework established



## 🙋 Join the Movement

This is more than code - it's a collective effort to redefine computing foundations.

**Your curiosity and expertise are our most valuable resources.**

---
*Architectural Concept & Open-Source Release by LIWEI LI*
