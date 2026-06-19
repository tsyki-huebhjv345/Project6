# Project6
one more exploring code
# Eco-Friendly Smart Energy Grid

A NetworkX Python script that models a green microgrid network topology using centralized power zones, distribution metrics, and localized efficiency parameters.

## Project Overview
This project uses the NetworkX graph theory framework to map a high-efficiency smart energy grid. The grid consists of three green energy zones (represented cleanly by their initial letters: **K**, **L**, and **H**) that balance dynamic power metrics and direct eco-efficiency ratings across smart power transmission pathways.

The grid initializes the following architecture:
* **K_Zone**: Main energy hub with tier-1 importance and high production throughput.
* **L_Zone**: Western hydro sector with tier-1 importance and steady baseline output.
* **H_Zone**: Frontier sector with tier-2 importance optimized for high peak efficiency.

---

## How It Works

### 1. Graph Node Attributes
Every node in the energy grid stores custom semantic metadata defining its role in the network layout:
* `importance`: Defines the routing tier and distribution priority of the node.
* `eco_efficiency`: Tracks the environmental performance metric and clean generation rating.

### 2. Edge Routing Attributes
Edges denote physical high-voltage smart power lines connecting the regional sectors. Each connection holds a custom `capacity` attribute that dictates the maximum electrical throughput measured in Megawatts (MW).

---

## Prerequisites & Installation

To run this structural grid model, you only need Python and the NetworkX network library.

Install the required library via pip:
```bash
pip install networkx
```

---

## How to Run

1. Save the clean source code into a file named `smart_grid.py`.
2. Launch the script using your python environment:
```bash
python smart_grid.py
```

---

## Expected Terminal Output

When executed successfully, your terminal will print the following telemetry breakdown:

```text
-SMART GRID ENERGY MODEL INJECTED-
Zone: K_Zone     | Importance Tier: 1 | Eco-Efficiency Rating: 85.0%
Zone: L_Zone     | Importance Tier: 1 | Eco-Efficiency Rating: 30.0%
Zone: H_Zone     | Importance Tier: 2 | Eco-Efficiency Rating: 95.0%

-GREEN POWER TRANSMISSION PATHWAYS-
Line: K_Zone <-> L_Zone     | Max Distribution Capacity: 500 MW
Line: K_Zone <-> H_Zone     | Max Distribution Capacity: 300 MW
```
