# LIWEI LI Green Computing Architecture

**Language**: **English** | [中文](./README_ZH.md)

A revolutionary open-source computing architecture that leverages **ternary logic** and **photonic interconnects** to break through the energy and bandwidth walls.

---

## 📖 Overview

The "4+1" Full-Stack Ternary Green Computing Architecture proposes a post-Moore's Law computing paradigm. It aims to achieve orders-of-magnitude improvement in energy efficiency from the physical ground up through the co-design of **ternary logic devices**, **on-chip optoelectronic hybrid interconnects**, and **3D heterogeneous integration**.

**Core Pivot (Latest Update)**: This architecture has officially evolved from its early silicon CMOS-based silicon photonics approach to a disruptive path based on **FMOS (Flexible Metal-Oxide Semiconductor)** and **LED wafer integration**. This pivot aims to leverage the ultra-low leakage characteristics of oxide semiconductors and the mature manufacturing ecosystem of the display industry, exploring a more sustainable and cost-effective route to high-efficiency computing.

## 🏗️ Architectural Core ("4+1" Stack)

The architecture employs a vertical stacking design, from top to bottom:

1.  **Computing Layer (L4)**: Implements ternary logic and compute-in-memory units using **FMOS** processes (e.g., IGZO), targeting picowatt-level static power consumption.
2.  **Optoelectronic Conversion Layer (L3)**: Integrates **GaN-based micro-LED source arrays** and photodetectors to enable efficient electrical-to-optical and optical-to-electrical signal conversion.
3.  **Optical Routing Layer (L2)**: A low-loss optical waveguide network for optical signal distribution.
4.  **Base Electrical Interconnect Layer (L1)**: High-frequency electrical interconnects and chip I/O interfaces.
5.  **"+1" Stress Buffer Layer**: A conceptual layer intended to manage thermal and mechanical stress in heterogeneous integration.

## ⚙️ Technical Specifications & Goals

| Component / Metric | FMOS-LED Path Target | Notes / Comparison |
| :--- | :--- | :--- |
| **Logic Foundation** | Ternary Logic (-Vdd, 0, +Vdd) | Based on FMOS device characteristics |
| **On-Chip Light Source** | Miniaturized GaN LED (450nm Blue Light) | A non-traditional approach vs. infrared silicon photonics |
| **Optical Interconnect Energy Efficiency** | < 50 fJ/bit | **A highly challenging target** |
| **Projected System Energy Efficiency Gain** | Potential for order-of-magnitude improvement over conventional architectures | Refer to comparative analysis in the technical report |
| **Manufacturing Process** | Low-temperature oxide semiconductor process compatible with display industry | Decoupled from standard CMOS processing |

## 📂 Open-Source Contents

This project is open-sourced under the **CERN Open Hardware Licence Version 2 - Permissive**. Currently available contents include:
- **Design Documentation**: Technical architecture report, whitepaper.
- **Design Specifications**: Initial cell library design specifications, optoelectronic interface standards.
- **Simulation Models**: Ternary logic simulation models, system-level power evaluation scripts.

### Technical Challenges and Clarifications (Important)

To uphold the rigor of our open-source work, we explicitly outline the key challenges and data premises currently associated with this architecture:

1.  **Optical Interconnect Scheme:** The use of 450nm blue light for on-chip communication faces inherent challenges due to high absorption loss in silicon-based materials. Demonstrating its feasibility and developing low-loss routing solutions are currently our core research topics.
2.  **Interpretation of Performance Data:** The projected "15-20x system energy efficiency improvement" is a conceptual extrapolation based on a comparison with a **representative** traditional GPU benchmark. This data is intended to illustrate architectural potential and does not reflect measured results from a physical implementation.
3.  **Process Integration:** The heterogeneous integration of **FMOS** and LED wafers represents an entirely new manufacturing flow. Its reliability and production yield currently await verification.

We welcome community discussion and collaboration on these points.

## 📅 Development Roadmap

1.  **Phase 1 (Feasibility Study)**: Validate the key process feasibility of FMOS-driven micro-LEDs.
2.  **Phase 2 (Prototyping)**: Demonstrate a small-scale ternary computing array with on-chip optical interconnects.
3.  **Phase 3 (Integration)**: Complete a full "4+1" four-layer stacked prototype system.

## 👥 Contributing

We welcome contributions in the following areas:
- Metal-oxide semiconductor device modeling
- Optoelectronic hybrid integration design and simulation
- 3D integration and thermo-mechanical stress analysis
- Architecture evaluation and benchmarking

## 📜 License

The hardware design of this project is licensed under **CERN OHL v2**. Documentation is licensed under **Creative Commons Attribution 4.0 International**.