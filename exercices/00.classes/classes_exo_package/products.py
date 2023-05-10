class Product:
    def __init__(self, cost, price, brand):
        self.cost = cost
        self.price = price
        self.brand = brand

class Furniture(Product):
    def __init__(self, cost, price, brand, material, color, dimension):
        super().__init__(cost,price,brand)
        self.material = material
        self.color = color
        self.dimension = dimension

class Couch(Furniture):
    def __init__(self, cost, price, brand, material, color, dimension):
        super().__init__(cost, price, brand, material, color, dimension)

class Chair(Furniture):
    def __init__(self, cost, price, brand, material, color, dimension):
        super().__init__(cost, price, brand, material, color, dimension)

class Table(Furniture):
    def __init__(self, cost, price, brand, material, color, dimension):
        super().__init__(cost, price, brand, material, color, dimension)