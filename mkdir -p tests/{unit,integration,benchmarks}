#!/usr/bin/env python3
"""
4+1架构演示
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from src.architecture.fourplus1_architecture import FourPlusOneArchitecture
from src.core.ternary_computing import TernaryLogic, TernaryState, TernaryValue
import numpy as np

def demo_ternary_computing():
    """演示三元计算"""
    print("🧮 TERNARY COMPUTING DEMO")
    print("=" * 60)
    
    logic = TernaryLogic()
    
    # 基础运算
    print("\n1. Basic Ternary Logic:")
    print(f"   TRUE AND UNKNOWN = {logic.and_gate(TernaryState.TRUE, TernaryState.UNKNOWN)}")
    print(f"   FALSE OR UNKNOWN = {logic.or_gate(TernaryState.FALSE, TernaryState.UNKNOWN)}")
    print(f"   NOT TRUE = {logic.not_gate(TernaryState.TRUE)}")
    
    # 批量转换
    print("\n2. Batch Conversion:")
    values = np.array([0.8, -0.2, 0.6, -0.9, 0.1, 0.0])
    ternary_values = logic.batch_convert(values)
    print(f"   Input: {values}")
    print(f"   Ternary: {ternary_values}")
    
    # 矩阵运算
    print("\n3. Matrix Multiplication:")
    A = np.array([[1, 0, -1], [0, 1, 0], [-1, 0, 1]])
    B = np.array([[0, 1, 0], [1, 0, -1], [0, -1, 0]])
    result = logic.matrix_multiply(A, B)
    print(f"   A:\n{A}")
    print(f"   B:\n{B}")
    print(f"   A × B:\n{result}")
    
    return logic

def demo_architecture():
    """演示4+1架构"""
    print("\n🏗️  4+1 ARCHITECTURE DEMO")
    print("=" * 60)
    
    arch = FourPlusOneArchitecture()
    
    # 生成技术摘要
    print(arch.generate_technical_summary())
    
    # 功耗分析
    print("\n📊 POWER BREAKDOWN ANALYSIS:")
    breakdown = arch.estimate_power_breakdown()
    for layer, data in breakdown.items():
        print(f"   {layer:25} {data['power_w']:5.1f} W ({data['percentage']:5.1f}%)")
    
    # 性能指标
    perf = arch.calculate_performance()
    print("\n🎯 KEY PERFORMANCE INDICATORS:")
    print(f"   Energy Efficiency: {perf['energy_efficiency_tops_per_w']:.2f} TOPS/W")
    print(f"   Compute Density:   {perf['compute_density_tops_per_mm2']:.2f} TOPS/mm²")
    print(f"   Bandwidth Density: {perf['bandwidth_density_tbps_per_mm2']:.3f} Tbps/mm²")
    
    return arch

def comparative_analysis():
    """对比分析"""
    print("\n📈 COMPARATIVE ANALYSIS")
    print("=" * 60)
    
    # 与传统架构对比
    traditional_metrics = {
        "Energy Efficiency (TOPS/W)": 1.0,  # 基准
        "Compute Density (TOPS/mm²)": 10.0,
        "Bandwidth (Tbps)": 0.8,
        "Precision": "Binary"
    }
    
    gca_metrics = {
        "Energy Efficiency (TOPS/W)": 4.1,  # 4.1倍提升
        "Compute Density (TOPS/mm²)": 32.0,  # 3.2倍提升
        "Bandwidth (Tbps)": 1.6,  # 2.0倍提升
        "Precision": "Ternary"
    }
    
    print("\n  Metric                Traditional     GCA       Improvement")
    print("  " + "-" * 55)
    for key in traditional_metrics:
        if key != "Precision":
            trad = traditional_metrics[key]
            gca = gca_metrics[key]
            improvement = gca / trad if trad > 0 else 0
            print(f"  {key:25} {trad:8.1f}       {gca:8.1f}       {improvement:5.1f}x")
        else:
            print(f"  {key:25} {traditional_metrics[key]:8}       {gca_metrics[key]:8}")

def main():
    """主演示函数"""
    print("\n" + "=" * 70)
    print("🚀 GREEN COMPUTING ARCHITECTURE - COMPLETE DEMONSTRATION")
    print("=" * 70)
    
    # 演示三元计算
    ternary = demo_ternary_computing()
    
    # 演示架构
    arch = demo_architecture()
    
    # 对比分析
    comparative_analysis()
    
    print("\n" + "=" * 70)
    print("✅ DEMONSTRATION COMPLETE")
    print("=" * 70)
    print("\nNext Steps:")
    print("  1. View detailed documentation: docs/")
    print("  2. Run tests: pytest tests/")
    print("  3. Explore examples: examples/")
    print("  4. Join the community: CONTRIBUTING.md")
    print("=" * 70)

if __name__ == "__main__":
    main()