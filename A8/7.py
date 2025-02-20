"""
Create a class for representing any 2-D point or vector. The methods inside this class include
its magnitude and its rotation with respect to the X-axis. Using the objects define functions for
calculating the distance between two vectors, dot product, cross product of two vectors. Extend
the 2-D vectors into 3-D using the concept of inheritance. Update the methods according to 3-
D.
"""

import math

class Vector2D: def init(self, x, y): self.x = x self.y = y

def magnitude(self):
    return math.sqrt(self.x**2 + self.y**2)

def angle_with_x_axis(self):
    return math.degrees(math.atan2(self.y, self.x))

def distance_to(self, other):
    return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

def dot(self, other):
    return self.x * other.x + self.y * other.y

def cross(self, other):
    return self.x * other.y - self.y * other.x

def __repr__(self):
    return f"Vector2D({self.x}, {self.y})"

class Vector3D(Vector2D): def init(self, x, y, z): super().init(x, y) self.z = z

def magnitude(self):
    return math.sqrt(self.x**2 + self.y**2 + self.z**2)

def distance_to(self, other):
    return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2 + (other.z - self.z)**2)

def dot(self, other):
    return self.x * other.x + self.y * other.y + self.z * other.z

def cross(self, other):
    return Vector3D(
        self.y * other.z - self.z * other.y,
        self.z * other.x - self.x * other.z,
        self.x * other.y - self.y * other.x
    )

def __repr__(self):
    return f"Vector3D({self.x}, {self.y}, {self.z})"

def get_vector_input(dimension): if dimension == 2: x, y = map(float, input("Enter x and y coordinates (space-separated): ").split()) return Vector2D(x, y) elif dimension == 3: x, y, z = map(float, input("Enter x, y, and z coordinates (space-separated): ").split()) return Vector3D(x, y, z)

def main(): while True: print("\nMenu:") print("1. Create 2D Vector") print("2. Create 3D Vector") print("3. Calculate Magnitude") print("4. Calculate Angle with X-axis (2D only)") print("5. Calculate Distance between Two Vectors") print("6. Calculate Dot Product") print("7. Calculate Cross Product") print("8. Exit") choice = int(input("Enter your choice: "))

if choice == 1:
        v1 = get_vector_input(2)
        print("Created:", v1)
    elif choice == 2:
        v1 = get_vector_input(3)
        print("Created:", v1)
    elif choice == 3:
        v1 = get_vector_input(int(input("Enter dimension (2 or 3): ")))
        print("Magnitude:", v1.magnitude())
    elif choice == 4:
        v1 = get_vector_input(2)
        print("Angle with X-axis:", v1.angle_with_x_axis())
    elif choice == 5:
        v1 = get_vector_input(int(input("Enter dimension (2 or 3): ")))
        v2 = get_vector_input(int(input("Enter dimension (2 or 3): ")))
        print("Distance:", v1.distance_to(v2))
    elif choice == 6:
        v1 = get_vector_input(int(input("Enter dimension (2 or 3): ")))
        v2 = get_vector_input(int(input("Enter dimension (2 or 3): ")))
        print("Dot Product:", v1.dot(v2))
    elif choice == 7:
        v1 = get_vector_input(int(input("Enter dimension (2 or 3): ")))
        v2 = get_vector_input(int(input("Enter dimension (2 or 3): ")))
        print("Cross Product:", v1.cross(v2))
    elif choice == 8:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")

main()

