class Product:
    """ Product class"""
    def __init__(self, cost, price, marque):
        self._cost = cost
        self._price = price
        self._marque = marque

class Furniture(Product):
    """ herit from Product """
    def __init__(self, cost, price, marque, materiau, couleur, dimensions):
        super().__init__(cost,price,marque)
        self._materiau = materiau
        self._couleur = couleur
        self._dimensions = dimensions

class Couch(Furniture):
    """ uses __init___ from Furniture"""

class Chair(Furniture):
    """ uses __init___ from Furniture"""

class Table(Furniture):
    """ uses __init___ from Furniture"""
