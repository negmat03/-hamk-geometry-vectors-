# Vector Formulas

## Notation
- Bold **a** or arrow notation **a⃗** for vectors
- |**a**| for magnitude (length)
- â for unit vector

---

## Basic Operations

### Magnitude
```
|a| = √(ax² + ay² + az²)     (3D)
|a| = √(ax² + ay²)            (2D)
```

### Unit Vector
```
â = a / |a|
```

### Addition & Subtraction
```
a + b = (ax+bx, ay+by, az+bz)
a - b = (ax-bx, ay-by, az-bz)
```

### Scalar Multiplication
```
k·a = (k·ax, k·ay, k·az)
```

---

## Dot Product (Scalar Product)

```
a · b = ax·bx + ay·by + az·bz
a · b = |a|·|b|·cos θ
```

### Properties
- Result is a **scalar** (number)
- `a · b = 0`  ⟹  vectors are **perpendicular** (θ = 90°)
- `a · a = |a|²`
- Commutative: `a · b = b · a`

### Finding the angle
```
cos θ = (a · b) / (|a| · |b|)
θ = arccos( (a · b) / (|a| · |b|) )
```

### Scalar projection of a onto b
```
comp_b(a) = (a · b) / |b|
```

### Vector projection of a onto b
```
proj_b(a) = [ (a · b) / |b|² ] · b
```

---

## Cross Product (Vector Product) — 3D only

```
a × b = ( ay·bz - az·by,
           az·bx - ax·bz,
           ax·by - ay·bx )

|a × b| = |a|·|b|·sin θ
```

### Properties
- Result is a **vector** perpendicular to both a and b
- `a × b = 0`  ⟹  vectors are **parallel** (θ = 0° or 180°)
- **Anti-commutative**: `a × b = -(b × a)`
- Direction: right-hand rule

### Geometric use
```
Area of parallelogram = |a × b|
Area of triangle      = ½ · |a × b|
```

---

## Scalar Triple Product

```
a · (b × c) = | ax ay az |
               | bx by bz |
               | cx cy cz |

Volume of parallelepiped = |a · (b × c)|
Volume of tetrahedron    = (1/6) · |a · (b × c)|
```

---

## Key Questions to Ask

| Goal | Use |
|------|-----|
| Find angle between vectors | Dot product |
| Check perpendicularity | Dot product = 0 |
| Find area | Cross product |
| Check parallelism | Cross product = 0 |
| Find volume | Triple product |
| Decompose a vector | Projection formulas |
