#!/usr/bin/env python3
"""
Green Computing Architecture 简单演示
运行: python examples/simple_demo.py
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.ternary import TernaryLogic, TAND, TOR, TNOT

def main():
    print("=" * 60)
    print("🚀 Green Computing Architecture - 简单演示")
    print("=" * 60)
    
    print("\n🧮 三元逻辑演示:")
    print(f"  1 AND 0 = {TAND(1, 0)}")
    print(f"  -1 OR 1 = {TOR(-1, 1)}") 
    print(f"  NOT 1 = {TNOT(1)}")
    
    print("\n🔢 值转换演示:")
    values = [0.8, -0.2, 0.6, -0.9, 0.1]
    for v in values:
        t = TernaryLogic.to_ternary(v)
        state = {1: "TRUE", 0: "UNKNOWN", -1: "FALSE"}[t]
        print(f"  {v:5.2f} → {t} ({state})")
    
    print("\n🏗️  4+1架构概述:")
    print("  1. 计算层 - 三元逻辑核心")
    print("  2. 存储层 - 存算一体内存") 
    print("  3. 互连层 - 硅基光子网络")
    print("  4. 接口层 - 标准化硬件接口")
    print("  +1. 管理层 - 智能功耗热管理")
    
    print("\n" + "=" * 60)
    print("✅ 演示完成!")
    print("\n📚 详细文档:")
    print("  • Whitepaper.md - 技术白皮书")
    print("  • Technical-Report.md - 技术报告")
    print("  • Vision.md - 项目愿景")
    print("=" * 60)

if __name__ == "__main__":
    main()