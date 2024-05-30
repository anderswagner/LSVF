import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

points = np.random.rand(100, 2)
vor = Voronoi(points)

fig, ax = plt.subplots()
voronoi_plot_2d(vor, ax=ax, show_vertices=False)

ax.plot(points[:, 0], points[:, 1], 'r.')

ax.axis('off')
ax.set_aspect('equal')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
plt.savefig('voronoi_diagram_square.png', bbox_inches='tight', pad_inches=0)
plt.show()
