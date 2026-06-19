import networkx as nx

#Graph
G = nx.Graph()

#Regional Energy Zones with customized attributes (Smart Grid parameters)
G.add_node("K_Zone", importance=1, eco_efficiency=0.85)   # Main Hub: High Importance, High Solar/Wind Output
G.add_node("L_Zone", importance=1, eco_efficiency=0.30)   # Western Sector: High Importance, Steady Hydro Output
G.add_node("H_Zone", importance=2, eco_efficiency=0.95)   # Frontier Sector: Secondary Hub, High Peak Efficiency

#Smart Transmission Lines with capacities
G.add_edge("K_Zone", "L_Zone", capacity=500) # 500 MW green energy line
G.add_edge("K_Zone", "H_Zone", capacity=300) # 300 MW green energy line

print("-SMART GRID ENERGY MODEL-")
for node, attributes in G.nodes(data=True):
    print(f"Zone: {node:10} | Importance Tier: {attributes['importance']} | Eco-Efficiency Rating: {attributes['eco_efficiency']*100}%")

print("\n-GREEN POWER TRANSMISSION PATHWAYS-")
for u, v, attributes in G.edges(data=True):
    print(f"Line: {u} <-> {v:10} | Max Distribution Capacity: {attributes['capacity']} MW")
