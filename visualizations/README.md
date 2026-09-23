# Visualizations — Geometry and Vectors

This folder contains scripts and images for visualizing geometric concepts.

## How to Generate Plots

### Requirements
```bash
pip install matplotlib numpy
```

### Run the vector script with plots
```bash
# From the repo root:
python scripts/vector_operations.py
# Uncomment the plot sections in the script to save PNG images here
```

---

## What to Put Here

- PNG/SVG images of vector diagrams
- Geometry plots (lines, planes, conic sections)
- Matplotlib output from scripts
- Screenshots from GeoGebra or Desmos

## Suggested Tools

| Tool | Use |
|------|-----|
| [GeoGebra](https://www.geogebra.org) | Interactive 2D/3D geometry |
| [Desmos](https://www.desmos.com) | Function graphing |
| Python + matplotlib | Programmatic plots |
| Python + plotly | Interactive 3D plots |

## Quick Plot Template (Python)

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)

# Draw vectors
a = np.array([3, 2])
b = np.array([1, 4])
ax.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='blue', label='a')
ax.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='red', label='b')

ax.legend()
plt.title('Vector Diagram')
plt.savefig('visualizations/vectors_example.png', dpi=150, bbox_inches='tight')
plt.show()
```
