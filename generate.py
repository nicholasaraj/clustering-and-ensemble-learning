import matplotlib.pyplot as plt
from graphviz import Digraph

# Create a new directed graph
dot = Digraph()

# Add nodes (decision nodes and leaf nodes)
dot.node('X2', 'x2 < 15?')  # Root node
dot.node('X1_1', 'x1 < 25?')  # Decision for x2 < 15
dot.node('F', 'F')  # Leaf for x1 >= 25, x2 >= 15
dot.node('E', 'E')  # Leaf for x1 >= 25, x2 < 15
dot.node('X1_2', 'x1 < 5?')  # Decision for x2 >= 15, x1 < 25
dot.node('D', 'D')  # Leaf for 5 <= x1 < 25, x2 >= 15
dot.node('C', 'C')  # Leaf for x1 < 5, x2 >= 15
dot.node('X1_3', 'x1 < 10?')  # Decision for x2 < 15, x1 < 25
dot.node('B', 'B')  # Leaf for x1 >= 10, x2 < 15
dot.node('A', 'A')  # Leaf for x1 < 10, x2 < 15

# Add edges (ensuring false is always left and true is always right)
dot.edge('X2', 'X1_1', label='false')  # x2 < 15 (false goes left)
dot.edge('X2', 'X1_2', label='true')   # x2 >= 15 (true goes right)

dot.edge('X1_1', 'E', label='false')    # x1 >= 25 (false goes left)
dot.edge('X1_1', 'X1_3', label='true')  # x1 < 25 (true goes right)

dot.edge('X1_2', 'C', label='false')    # x1 < 5 (false goes left)
dot.edge('X1_2', 'F', label='true')     # x1 >= 25 (true goes right)

dot.edge('X1_3', 'A', label='false')    # x1 < 10 (false goes left)
dot.edge('X1_3', 'B', label='true')     # x1 >= 10 (true goes right)

dot.edge('X1_2', 'D', label='false')    # x1 >= 5, x2 >= 15 (false goes left)

# Render the graph as a PNG file (or you can choose other formats like PDF)
dot.render('decision_tree_fixed_simplified', format='png', cleanup=True)

# Display the image
img = plt.imread('decision_tree_fixed_simplified.png')
plt.imshow(img)
plt.axis('off')
plt.show()
