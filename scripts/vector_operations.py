import math

def magnitude(v):
    return math.sqrt(sum(x**2 for x in v))

def dot_product(a, b):
    return sum(x*y for x, y in zip(a, b))

def cross_product(a, b):
    return [
        a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0]
    ]

def angle_between(a, b):
    cos_theta = dot_product(a, b) / (magnitude(a) * magnitude(b))
    return math.degrees(math.acos(cos_theta))

def unit_vector(v):
    mag = magnitude(v)
    return [x/mag for x in v]

# Example usage
if __name__ == "__main__":
    A = [1, 2, 3]
    B = [4, 5, 6]
    
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"|A| = {magnitude(A):.4f}")
    print(f"A · B = {dot_product(A, B)}")
    print(f"A × B = {cross_product(A, B)}")
    print(f"Angle = {angle_between(A, B):.2f}°")
    print(f"Unit A = {[round(x,4) for x in unit_vector(A)]}")
