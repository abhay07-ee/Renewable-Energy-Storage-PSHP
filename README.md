# 💧 Micro-Hydro Pumped Storage Plant Design & Estimation ⚡

<div align="center">
  <img src="https://img.shields.io/badge/Domain-Renewable%20Energy-blue?style=for-the-badge&logo=eco" />
  <img src="https://img.shields.io/badge/Focus-Grid%20Stability-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Location-Himachal%20Pradesh-orange?style=for-the-badge" />
</div>

## 📌 Project Overview
This project presents a comprehensive design and mathematical model for a **Micro-Hydro Pumped Storage Plant (PSHP)**. Designed specifically for the hilly terrain of **Himachal Pradesh**, this system acts as a "Water Battery," storing excess energy during low demand and generating power during peak hours.

### 🌟 Key Innovations
- **Energy Arbitrage:** Pumping water to an upper reservoir when solar/wind energy is surplus.
- **Micro-Grid Stability:** Providing instant power to remote areas where the main grid is unstable.
- **Cost-Effective Estimation:** Full Bill of Quantities (BOQ) for small-scale implementation (10kW - 50kW).
- **Eco-Friendly:** Zero-carbon emission solution using natural geography.

---

## 📐 System Architecture & Design

The system consists of two reservoirs at different elevations, a pump-turbine set, and a smart control unit.



### 🛠️ Technical Specifications
| Parameter | Value (Simulated) | Description |
| :--- | :--- | :--- |
| **Net Head (H)** | 50 Meters | Vertical height between reservoirs |
| **Flow Rate (Q)** | 0.2 m³/s | Water volume per second |
| **Turbine Type** | Pelton / Cross-flow | High-efficiency micro-turbine |
| **Storage Capacity** | 5000 m³ | Equivalent to ~500 kWh of storage |
| **Round-trip Efficiency**| 75% - 80% | Combined pump and turbine efficiency |

---

## 📊 Mathematical Modeling (Power Calculation)
The power output is calculated using the standard hydraulic power equation:

$$P = \eta \cdot \rho \cdot g \cdot h \cdot \dot{q}$$

Where:
- $P$ = Power in Watts
- $\eta$ = Efficiency (0.8 approx)
- $\rho$ = Density of water ($1000 \, kg/m^3$)
- $g$ = Acceleration due to gravity ($9.81 \, m/s^2$)
- $h$ = Net Head (m)
- $\dot{q}$ = Flow rate ($m^3/s$)

---

## 📂 Repository Structure
- **`/Calculations`**: Excel sheets and Python scripts for load flow and head loss.
- **`/Designs`**: AutoCAD Single Line Diagrams (SLD) of the powerhouse.
- **`/Estimation`**: Detailed list of components (Pipes, Turbine, Generator, Governor).

---

## 🛠️ Tools Used
- **Simulation:** MATLAB / Python for efficiency modeling.
- **Drafting:** AutoCAD Electrical for the control panel layout.
- **Analysis:** ETAP for grid synchronization studies.

---

## 📈 Future Scope
- **Hybrid Integration:** Combining with Solar PV for a 24/7 standalone power solution.
- **IoT Monitoring:** Using ESP32 to monitor water levels and flow rates remotely.
- **Smart Governor:** Automated frequency control based on load variations.

---

## 👨‍💻 Developer
**Abhay** *Electrical Engineer | B.Tech (2026) @ HIET*
*Specialist in Power Systems & Renewable Energy*

<p align="left">
  <a href="https://www.linkedin.com/in/abhay-abhay-9806a0355"><img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin" /></a>
</p>

---
