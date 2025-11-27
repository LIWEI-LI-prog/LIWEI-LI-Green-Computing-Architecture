"Qian" Series 4+1 Heterogeneous Stacked Ternary LED-Style Wafer Fabrication Technology Report

Document ID: QIAN-PTR-001
Version: 3.0
Release Date: November 27, 2025
Original Inventor: LIWEI LI
Core Technologies: Ternary Optical Logic / Micro-LED Light Sources / Heterogeneous Stacking / Photonic-Native Computing
Process Platform: 200mm GaN-on-Silicon Photonics Platform
License: CERN Open Hardware License Version 2 - Permissive

1. Abstract

This report presents a revolutionary chip fabrication paradigm - "Heterogeneous Stacking." This technology abandons the traditional von Neumann architecture and electronic computing paradigm of silicon-based CMOS, instead adopting a ternary photonic computing architecture that uses micro-LEDs as native computing elements. Through the "4+1" functional partitioning and heterogeneous wafer stacking technology, we achieve optical integration of computing, memory, and communication in three-dimensional space, providing a physical foundation for next-generation high-efficiency, low-latency, and secure computing systems.

2. Core Philosophy: From "Etching Silicon" to "Growing Light"

The fundamental breakthrough of this technology lies in a philosophical shift:

· Traditional Paradigm (Etching Silicon): "Carving" paths for electrons (transistors) through complex etching processes on passive silicon substrates.
· Our Paradigm (Growing Light): "Growing" computational structures that can generate, modulate, and manipulate photons through epitaxial growth on active light-emitting materials (like GaN).

The term "Heterogeneous Stacking" precisely describes the core feature of integrating wafers of different materials, different functions, and different processes (heterogeneous) into a high-density system through vertical interconnection technology (stacking).

3. "4+1" Photonic-Native Architecture

Our architecture is a bottom-up vertically integrated system:

L1: Intelligent Substrate Layer

· Function: System foundation, providing wafer-level power delivery, global clocking, thermal management, and external optical I/O.
· Technology: High-resistivity silicon substrate with integrated microchannels and Through-Silicon Vias.

L2: Optical Memory Layer

· Function: Ternary optical storage and compute-in-memory.
· Technology: Phase-change material based ternary state (-1, 0, +1) storage via optical write/read, supporting parallel optical matrix operations.

L3: Optical Routing Layer

· Function: On-die global optical communication and reconfigurable optical network.
· Technology: Silicon nitride waveguides and micro-LED optical I/O arrays enabling wavelength-division multiplexed ultra-high bandwidth communication.

L4: Optical Computing Layer

· Function: Ternary optical logic computing core.
· Technology: Micro-LED Computing Array. Each micro-LED is not just a light source but a ternary logic operation unit, directly representing ternary states through its luminous intensity (no light, threshold light, saturated light).

+1: Meta-Orchestration Layer

· Function: System soul, responsible for optical path orchestration, resource scheduling, and ternary instruction execution.
· Technology: TRISC-V instruction set and compiler specifically designed for ternary photonic computing, mapping computational tasks to physical optical path configurations.

4. LED-Style Wafer Fabrication Process Details

Our process is a typical "bottom-up" construction process.

4.1 L1 Intelligent Substrate Fabrication (Silicon-based)

1. Preparation of high-resistivity silicon substrate.
2. Deep silicon etching to form Through-Silicon Vias and embedded microchannels.
3. Deposition of insulating and metal layers to complete the power delivery network.
4. Fabrication of silicon grating couplers to provide optical ports for external fiber attachment.

4.2 L2 Optical Memory Layer Fabrication (Silicon-based + Phase-Change Material)

1. Standard CMOS peripheral circuit fabrication on another silicon wafer.
2. Deposition and patterning of phase-change material in the back-end-of-line to form ternary memory cells.
3. Wafer thinning and planarization via Chemical Mechanical Polishing.

4.3 L3 & L4 Optical Routing & Computing Layer Fabrication (GaN-on-Si Co-growth)

This is the most revolutionary step, where we monolithically integrate the routing elements of the L3 layer and the computing units of the L4 layer within a single GaN epitaxial process:

1. GaN Epitaxial Growth: Sequential growth of n-type GaN, multiple quantum well active region, and p-type GaN on a 200mm silicon substrate.
2. Micro-LED Computing Array Fabrication (L4):
   · Formation of micro-LED mesa structures via Inductively Coupled Plasma - Reactive Ion Etching.
   · Deposition of transparent conductive electrodes.
   · Definition of millions of independent micro-LED pixels, each capable of functioning as a ternary logic gate.
3. Photonic Routing Network Fabrication (L3):
   · Formation of low-loss optical waveguides via etching in different regions of the same GaN wafer.
   · Fabrication of electro-optic modulators and optical switches for dynamic optical routing.
   · Fabrication of micro-LEDs serving as on-chip optical transmitters, replacing traditional external lasers.

4.4 Heterogeneous Stacking (Heterogeneous Wafer Integration)

1. Face-to-face thermo-compression bonding of the completed L3/L4 GaN wafer with the L2 Optical Memory Layer silicon wafer. The bonding interface simultaneously forms millions of copper micro-bumps for inter-layer electrical interconnection.
2. Bonding of this composite wafer stack to the L1 Intelligent Substrate, achieving vertical power delivery and communication through Through-Silicon Vias.
3. Finally, precise wafer-level optical alignment and permanent attachment of the fiber array to the grating couplers on the L1 layer.

5. Key Innovations and Advantages

5.1 Ternary Photonic-Native Computing

· Unification of computing and communication medium as photons, eliminating photoelectric conversion overhead.
· Ternary logic offers higher information density than binary, proving more efficient for processing balanced data (e.g., positive/negative weights in AI).

5.2 Micro-LED as Computing Element

· Integration of light source and computing unit simplifies the architecture drastically.
· Nanosecond-scale switching speed of micro-LEDs provides a physical basis for ultra-fast parallel computing.

5.3 Heterogeneous Stacking

· Breaks the limitation of "silicon for everything," allowing the selection of the most suitable material for each function (Si for control, GaN for light emission, PCM for memory).
· 3D stacking drastically shortens interconnect lengths, achieving unprecedented bandwidth and energy efficiency.

5.4 Intrinsic Security

· The computational process occurs internally via light, emitting no electromagnetic radiation, providing inherent resistance to side-channel attacks.

6. Performance Targets

· Computational Efficiency: > 100 TOPS/W (Ternary Operations Per Second per Watt)
· Computational Density: > 10 TOPS/mm²
· Inter-Layer Bandwidth: > 10 Tbps/mm²
· Memory Access Latency: < 10 ns
· Thermal Density: < 0.5 W/cm² (with microchannel cooling)

7. Roadmap

· 2026: Demonstrate a test chip containing 1K ternary photonic computing units; complete the basic toolchain.
· 2027: Scale computing units to 1M; demonstrate a full "4+1" prototype system; open-source all hardware designs.
· 2028+: Promote industry chain maturity towards commercialization; explore hybrid architectures with quantum computing units.

8. Conclusion

The "4+1 Heterogeneous Stacked Ternary LED-Style Wafer Fabrication Process" described in this report is not an incremental improvement over existing technology, but a complete paradigm shift. It aims to build a future computing system that is light-speed, three-dimensionally integrated, and intrinsically intelligent. We believe this represents a highly promising new path forward in the post-Moore era.

---

Appendices

· Appendix A: Ternary Optical Logic Truth Tables and Gate Circuit Designs
· Appendix B: Detailed GaN Micro-LED Epitaxial Growth Parameters
· Appendix C: Heterogeneous Wafer Bonding Process Design Kit

---

This technical report and all associated design files are released under the CERN Open Hardware License Version 2 - Permissive. Commercial implementation requires appropriate attribution to LIWEI LI as the original inventor.