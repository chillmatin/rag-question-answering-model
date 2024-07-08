import networkx as nx
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation
# Create the graph
G = nx.Graph()

# Add nodes and edges
edges = [
    (0, 1), (0, 2), (0, 3),
    (1, 2), (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6), (5, 8),
    (6, 7),
    (7, 8)
]

G.add_edges_from(edges)

# Define positions of nodes for a better visualization
pos = {
    0: (1, 2),
    1: (0.5, 1.5),
    2: (1.5, 1.5),
    3: (1, 1),
    4: (0.5, 0.5),
    5: (1.5, 0.5),
    6: (2, 0),
    7: (2.5, 0.5),
    8: (2, 1)
}

# Function to update node colors
def update_colors(frame):
    node_colors = ['red' if node in nodes[frame % len(nodes)] else 'skyblue' for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='gray', node_size=500, font_size=10)
    plt.title(f"Frame {frame}")
    time.sleep(1)  # Pause for 1 second

nodes = [
    (6, 7, 8), 
    (5, 6, 8), 
    (5, 6, 7), 
    (5, 7, 8), 
    (4, 5, 8), 
    (4, 5, 7), 
    (4, 5, 6), 
    (4, 6, 8), 
    (4, 6, 7), 
    (4, 7, 8), 
    (3, 4, 8), 
    (3, 4, 7), 
    (3, 4, 6), 
    (3, 4, 5), 
    (3, 5, 8), 
    (3, 5, 7), 
    (3, 5, 6), 
    (3, 6, 8), 
    (3, 6, 7), 
    (3, 7, 8), 
    (2, 3, 8), 
    (2, 3, 7), 
    (2, 3, 6), 
    (2, 3, 5), 
    (2, 3, 4), 
    (2, 4, 8), 
    (2, 4, 7), 
    (2, 4, 6), 
    (2, 4, 5), 
    (2, 5, 8), 
    (2, 5, 7), 
    (2, 5, 6), 
    (2, 6, 8), 
    (2, 6, 7), 
    (2, 7, 8), 
    (1, 2, 8), 
    (1, 2, 7), 
    (1, 2, 6), 
    (1, 2, 5), 
    (1, 2, 4), 
    (1, 3, 8), 
    (1, 3, 7), 
    (1, 3, 6), 
    (1, 3, 5), 
    (1, 3, 4), 
    (1, 4, 8), 
    (1, 4, 7), 
    (1, 4, 6), 
    (1, 4, 5), 
    (1, 5, 8), 
    (1, 5, 7), 
    (1, 5, 6), 
    (1, 6, 8), 
    (1, 6, 7), 
    (1, 7, 8)
]
# Set node colors
# node_colors = ['red' if node in nodes[0] else 'skyblue' for node in G.nodes()]

# Create the animation
fig = plt.figure(figsize=(8, 6))
ani = FuncAnimation(fig, update_colors, frames=10, interval=1000)  # Frames and interval in milliseconds
plt.show()
