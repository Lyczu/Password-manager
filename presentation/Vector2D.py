class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __len__(self):
        return sqrt(self.x**2 + self.y**2)
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
    def __call__(self):
        return self.x + self.y
    def __repr__(self):
        return f"Wektor2D({self.x}, {self.y})"