Technical Report: "4+1" Full-Stack Ternary Green Computing Architecture (Open Source Edition)

Version: 3.0 (FMOS-LED Process Edition)
Release Date: 19 December 2025
Original Inventor: LIWEI LI
Open Source License: CERN Open Hardware License Version 2 - Permissive
Project Homepage: LIWEI LI Green Computing Architecture

Abstract

This report details the technical principles and implementation roadmap of the "4+1" Full-Stack Ternary Green Computing Architecture. The architecture synergistically integrates ternary logic, photonic-electronic hybrid interconnects, and 3D integration to overcome the fundamental energy and bandwidth walls of traditional computing at the physical level. This edition first publicly discloses a disruptive implementation path based on the FMOS (Flexible Metal-Oxide Semiconductor) process and LED wafer integration, marking a strategic shift from "silicon-based evolution" to "oxide/compound semiconductor convergence". It lays a novel hardware foundation for the next generation of ultra-low-power, inherently secure computing.

1. Ternary Device Physics

1.1 Ternary Logic Implementation Based on FMOS

Moving beyond conventional CMOS, this architecture employs metal-oxide semiconductors such as Indium-Gallium-Zinc-Oxide as the core channel material.

· Core Advantages:
  1. Native Ternary Suitability: The easily tunable threshold voltage of FMOS enables simpler and more stable tri-state (-Vdd, 0, +Vdd) voltage output, significantly reducing circuit complexity and static power.
  2. Ultra-Low Leakage: Extremely low off-state leakage current can potentially reduce the static power of ternary logic gates from the nanowatt to the picowatt range.
  3. Uniformity & Flexibility Potential: Amorphous nature ensures excellent electrical uniformity across the wafer and opens possibilities for future flexible electronics integration.

1.2 On-Chip Light Source Based on LED Wafers

Miniaturized GaN-based LED arrays are integrated as the light source at the wafer level with the compute layer.

· Core Advantages:
  1. Embedded Light Source: Eliminates losses from external laser coupling, simplifies packaging, and enhances reliability.
  2. Direct Electro-Optic Modulation: FMOS devices can directly drive micro-LEDs, enabling efficient electrical-to-optical conversion and providing a native solution for on-chip optical interconnects.

2. Photonic-Electronic Hybrid Interconnect Layer

2.1 Native Photonic-Electronic Conversion & Modulation

· Modulation Scheme: Direct Intensity Modulation based on micro-LEDs.
· Wavelength: 450nm (Blue light, based on GaN).
· Target Performance: Single-channel bandwidth > 40 Gbps, energy consumption < 50 fJ/bit.

2.2 Optical Waveguide & Routing Network

Low-loss optical waveguides fabricated on silicon nitride or polymer substrates enable intra- and inter-layer optical signal routing.

3. 3D Integration Technology Stack

A novel four-layer stack configuration is proposed (top to bottom):

1. L4: Ternary Compute Layer - FMOS process, implementing ternary logic and compute-in-memory units.
2. L3: Native Photonic Layer - Integrated micro-LED light source arrays and photodetectors.
3. L2: Optical Routing Layer - Low-loss optical waveguides with multiplexers/demultiplexers.
4. L1: Base Interconnect Layer - High-speed electrical interconnects and external I/Os.

4. Fabrication Process Flow (FMOS-LED Path)

This is a forward-looking process roadmap. Key steps include:

1. LED Wafer Preparation: Growth of GaN-based micro-LED arrays on a silicon substrate.
2. Wafer Bonding: High-precision alignment and bonding of the LED wafer to the FMOS driver circuit wafer.
3. FMOS Device Fabrication: Deposition and patterning of oxide semiconductor layers (e.g., IGZO) using low-temperature processes (<400°C).
4. Back-End Interconnect & Hybrid Packaging: Formation of multi-layer electrical interconnects and final optoelectronic hybrid packaging.

5. Projected Performance & Targets

Metric Target (FMOS-LED Path) Comparison (Previous CMOS-SiPh Path)
System Energy Efficiency 15-20x (vs. traditional GPU) 8.9x
Optical Link Energy < 50 fJ/bit 0.85 pJ/bit
Core Advantage Supply chain innovation, potential flexibility, higher efficiency potential Process maturity, complete toolchain
Primary Risk Heterogeneous integration process, reliability, lack of toolchain Advanced node dependency, complex packaging

6. Open Source Contents

Released under the CERN OHL v2 license, this project fully open-sources the following:

1. Architecture & Design Documentation: This technical report, whitepaper, getting-started guide.
2. Design Files: Initial cell library design specifications for the FMOS-LED path, optoelectronic interface standards.
3. Simulation & Tools: Ternary logic simulation models, system-level power estimation scripts.

7. Development Roadmap

1. Phase I (Feasibility Study): Collaborate with leading display technology labs to validate the key process feasibility of FMOS-driven micro-LEDs.
2. Phase II (Prototype): Demonstrate a small-scale ternary FMOS compute array with on-chip optical interconnects.
3. Phase III (Integration): Realize a complete "4+1" four-layer stacked prototype system.

Conclusion

This report marks the entry of the "4+1" architecture into a more radical and forward-looking development phase. We firmly believe that through open-source collaboration, pooling global expertise in oxide semiconductors, photonics, and integrated systems, we can collectively overcome the technical challenges. Together, we can transform this vision into reality and truly usher in a new era of green computing.
