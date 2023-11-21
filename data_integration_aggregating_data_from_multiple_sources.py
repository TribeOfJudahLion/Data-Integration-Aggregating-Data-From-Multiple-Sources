import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot

# Initialize a directed graph with a more efficient data structure
G = nx.DiGraph()

# Define a large number of data sources for a more realistic scenario
num_sources = 100
source_names = [f"Source_{i}" for i in range(num_sources)]

# Define properties for the central aggregation node
agg_attrs = {"color": "darkorange", "size": 1000}

# Add the central aggregation node
G.add_node("Data Aggregation", **agg_attrs)

# Connect each data source to the central node with a weight and add nodes
for i, source in enumerate(source_names):
    weight = np.random.rand()  # Random weight representing data flow complexity
    G.add_node(source, color=plt.cm.viridis(i / num_sources), size=300 + 200 * weight)
    G.add_edge(source, "Data Aggregation", weight=weight)

# Use a layout that is efficient for larger graphs
# Increased k value for better spread and reduced overlap
pos = nx.spring_layout(G, k=0.3, iterations=100)

# Close the Matplotlib plot since we're not displaying it
plt.close()

# Initialize Plotly figure
plotly_fig = go.Figure(layout=go.Layout(
    title='Enhanced Data Integration Representation',
    showlegend=False,
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
))

# Add nodes to Plotly figure
for i, node in enumerate(G.nodes()):
    x, y = pos[node]
    node_size = (G.nodes[node]['size'] / 1000) * 20  # Adjust size for Plotly
    plotly_fig.add_trace(go.Scatter(
        x=[x], y=[y],
        mode='markers+text',
        marker=dict(size=node_size, color=plt.cm.viridis(i / num_sources)),
        text=node,
        textposition="bottom center"
    ))

# Add edges to Plotly figure
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    plotly_fig.add_trace(go.Scatter(
        x=[x0, x1], y=[y0, y1],
        mode='lines',
        line=dict(width=0.5, color='black'),  # Adjusted line width for visibility
        opacity=0.5
    ))

# Save as HTML for an interactive visualization
plot(plotly_fig, filename='data_integration_graph.html')
