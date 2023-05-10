class Product:
    def __init__(self, cost, price, marque):
        self._cost = cost
        self._price = price
        self._marque = marque

class Furniture(Product):
    def __init__(self, cost, price, marque, materiau, couleur, dimensions):
        super().__init__(cost,price,marque)
        self._materiau = materiau
        self._couleur = couleur
        self._dimensions = dimensions

class Couch(Furniture):
    def __init__(self, cost, price, marque, materiau, couleur, dimensions):
        super().__init__(cost, price, marque, materiau, couleur, dimensions)

class Chair(Furniture):
    def __init__(self, cost, price, marque, materiau, couleur, dimensions):
        super().__init__(cost, price, marque, materiau, couleur, dimensions)

class Table(Furniture):
    def __init__(self, cost, price, marque, materiau, couleur, dimensions):
        super().__init__(cost, price, marque, materiau, couleur, dimensions)