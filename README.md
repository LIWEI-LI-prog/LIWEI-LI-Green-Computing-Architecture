🔐 LIWEI LI Green Computing Architecture - 技术共享边界说明 (README.de)

# Green Computing Architecture (FMOS-T / 4+1 BTA)

> The next-generation 3D optoelectronic balanced ternary computing architecture.

## 📖 Documentation
- **[English](README.md)** (this file)
- **[Deutsch/German](README.de.md)** - Detailed technical sharing boundaries and commercial licensing

## 🚀 Quick Start
1. Clone the repository
2. Explore the architecture docs in `docs/`
3. Run the behavioral simulator in `simulator/`
4. Check examples in `examples/`

## 🔐 Commercial Licensing
For access to RTL, PDK, production rights, please contact:
- **Licensing**: licensing@green-architecture.org
- **Technical**: support@green-architecture.org

© 2025 LIWEI LI. All rights reserved.

🎯 开放共享的内容

架构文档与规范

```
docs/architecture/ - 架构概念说明
docs/specification/ - 接口规范定义
whitepapers/ - 技术白皮书
api/ - 软件接口定义
```

开发工具与模拟器

```
simulator/ - 行为级模拟器
tools/compiler/ - 编译器前端
tools/debugger/ - 调试工具框架
examples/ - 示例代码
```

标准与接口

```
standards/isa/ - 指令集架构文档
standards/protocols/ - 通信协议
standards/interfaces/ - 硬件接口规范
```

---

🚫 不共享的专有技术

1. 硬件实现代码

```
❌ Verilog/VHDL/SystemVerilog RTL 源代码
❌ GDSII/LEF/DEF 物理设计文件
❌ 综合脚本与时序约束文件
❌ 布局布线数据库
```

2. 制造工艺技术

```
❌ 工艺设计包 (PDK)
❌ 材料配方与工艺参数
❌ 制造工艺流程卡
❌ 测试与封装方案
```

3. 核心算法

```
❌ 三态算术单元实现
❌ 光子调制算法
❌ 错误纠正码实现
❌ 热管理算法
❌ 功耗优化算法
```

4. 测试验证套件

```
❌ 完整验证环境
❌ 生产测试程序
❌ 特性化数据
❌ 良率优化参数
```

5. 商业机密

```
❌ 客户定制方案
❌ 价格与合同条款
❌ 供应链信息
❌ 生产良率数据
```

---

🔒 技术获取途径

访问级别 内容 许可证 费用
开放级 文档/模拟器 Apache 2.0 免费
评估级 RTL评估代码 商业评估 
开发级 完整RTL 开发许可 面议
生产级 全技术栈 生产许可 8M€

---

⚠️ 法律声明

知识产权所有权
### 专利授权声明

1. **开源部分专利授权**
   贡献者（LIWEI LI）在此授予您一项全球性的、免许可费的、非独占的、不可再授权的专利许可，仅限**为使用、复制、修改、分发本开源软件（即本仓库中依据Apache 2.0许可证授权的所有内容）之目的**，实施其所拥有的、覆盖该开源软件的必不可少专利权利要求。

2. **授权明确排除**
   上述授权**明确排除**任何实施本文件`🚫 不共享的专有技术`章节中所列内容的权利。获取此类权利需另行签署商业许可协议。

3. **专利 retaliation 条款**
   若您或您的关联实体就本开源软件对贡献者发起专利侵权诉讼，则本条款1项下授予您的所有专利许可将自动终止。

使用限制

· 仅限非商业研究使用
· 禁止反向工程
· 禁止军事用途
· 遵守出口管制

---

© 2025 LIWEI LI. 保留所有权利。
本文件最后更新: 2025年12月21日

---