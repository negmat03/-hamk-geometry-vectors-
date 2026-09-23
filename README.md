# 📐 Geometry and Vectors — HAMK

> Study materials, formulas, solved exercises and Python scripts for the Geometry and Vectors course at HAMK University of Applied Sciences.

---

## 📚 Topics Covered

| Topic | Formulas | Exercises | Script |
|-------|----------|-----------|--------|
| Vectors (2D/3D) | [📄](formulas/vectors.md) | [📝](exercises/) | [🐍](scripts/vector_operations.py) |
| Analytic Geometry | [📄](formulas/geometry.md) | [📝](exercises/) | — |
| Visualizations | — | — | [📊](visualizations/) |

---

## 🗂️ Folder Structure

```
hamk-geometry-vectors/
├── formulas/
│   ├── vectors.md         # Dot product, cross product, projections
│   └── geometry.md        # Lines, planes, distances, areas, volumes
├── exercises/
│   └── template.md        # Template for solved problems
├── scripts/
│   └── vector_operations.py  # Interactive vector calculator
└── visualizations/
    └── README.md          # How to generate plots
```

---

## 🚀 Quick Start

```bash
# Run the vector calculator
python scripts/vector_operations.py
```

---

## 🔢 Essential Formulas

### Vectors
| Operation | Formula |
|---|---|
| Magnitude | `\|a\| = √(x² + y² + z²)` |
| Dot product | `a·b = ax·bx + ay·by + az·bz` |
| Angle between vectors | `cos θ = (a·b) / (\|a\|·\|b\|)` |
| Cross product magnitude | `\|a×b\| = \|a\|·\|b\|·sin θ` |
| Unit vector | `â = a / \|a\|` |

### Geometry
| Shape | Formula |
|---|---|
| Distance between points | `d = √((x₂-x₁)² + (y₂-y₁)²)` |
| Midpoint | `M = ((x₁+x₂)/2, (y₁+y₂)/2)` |
| Area of triangle (vectors) | `A = ½·\|a×b\|` |
| Volume of parallelepiped | `V = \|a·(b×c)\|` |

---

## 📌 Study Tips

- Always **draw the vectors** before calculating
- Use `vector_operations.py` to **verify manual calculations**
- Remember: dot product → scalar, cross product → vector
- The **geometric interpretation** matters as much as the number

---

*HAMK — Hämeenlinna University of Applied Sciences*
