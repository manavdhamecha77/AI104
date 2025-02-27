"""
Create a class for representing any 2-D point or vector. The methods inside this class include
its magnitude and its rotation with respect to the X-axis. Using the objects define functions for
calculating the distance between two vectors, dot product, cross product of two vectors. Extend
the 2-D vectors into 3-D using the concept of inheritance. Update the methods according to 3-
D.
"""
import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def rotation(self):
        return math.degrees(math.atan2(self.y, self.x))
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def distance(self, other):
        diff = self - other
        return diff.magnitude()
    
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y
    
    def cross_product(self, other):
        return self.x * other.y - self.y * other.x
    
    def __str__(self):
        return f"({self.x}, {self.y})"

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def distance(self, other):
        diff = self - other
        return diff.magnitude()
    
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross_product(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

def vector_menu():
    while True:
        print("\nVector Operations Menu:")
        print("1. 2D Vector Operations")
        print("2. 3D Vector Operations")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            x1, y1 = map(float, input("Enter x1, y1 for first vector: ").split())
            x2, y2 = map(float, input("Enter x2, y2 for second vector: ").split())
            v1 = Vector2D(x1, y1)
            v2 = Vector2D(x2, y2)
            
            print("Magnitude of v1:", v1.magnitude())
            print("Magnitude of v2:", v2.magnitude())
            print("Rotation of v1:", v1.rotation(), "degrees")
            print("Rotation of v2:", v2.rotation(), "degrees")
            print("Distance between v1 and v2:", v1.distance(v2))
            print("Dot product:", v1.dot_product(v2))
            print("Cross product:", v1.cross_product(v2))
        
        elif choice == "2":
            x1, y1, z1 = map(float, input("Enter x1, y1, z1 for first vector: ").split())
            x2, y2, z2 = map(float, input("Enter x2, y2, z2 for second vector: ").split())
            v1 = Vector3D(x1, y1, z1)
            v2 = Vector3D(x2, y2, z2)
            
            print("Magnitude of v1:", v1.magnitude())
            print("Magnitude of v2:", v2.magnitude())
            print("Distance between v1 and v2:", v1.distance(v2))
            print("Dot product:", v1.dot_product(v2))
            print("Cross product:", v1.cross_product(v2))
        
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

vector_menu()