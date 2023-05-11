# Vous allez créer une classe InventoryProductEntry qui a pour role 
# de représenter une entrée d'inventaire pour un produit spécifique.
import product_classes
from product_classes import Product

class InventoryProductEntry:
    # Initialisation de la classe, en prenant en argument un objet Product et une quantité initiale
    def __init__(self, product:Product, quantity):
        """
        'product' : un objet de type produit qui rassemble les différents attributs et caractéristiques de ce dernier
        'quantity' : un entier qui représente le nombre des pièces du produit en question
        """
        # Initialisation des variables
        # Vous devez initialiser deux variables. 
        # la variable 'sales' qui stocke le total des revenues des ventes du produit
        # la variable 'expenses' qui stocke le total des dépenses pour restocker le produit
        self._product = product
        self._quantity = quantity
        self._sales = 0
        self._expenses = 0

    #Méthode Sell
    def sell(self, quantity):
        """
        La méthode sell est utilisée pour retirer la quantité vendue du produit depuis le stock.
        Elle met également à jour les ventes totales pour le produit.
        """
        #Avant de mettre à jour l'état du stocke du produit, on doit vérifier si on a déjà une quantité suffisante à vendre.
        # En utilisant des conditions, vérifier: 

        # SI la quantité en stock est inférieure à la quantité demandée:
        #     Afficher "Le stock du produit [nom du produit] est insuffisant."
        #     Retourner Faux
        # SINON:
        #     Réduire la quantité en stock par la quantité demandée
        #     Ajouter le revenue total de la vente à la variable 'sales' en multipliant la quantité vendue par le prix du produit
        #     Retourner Vrai
        if quantity > self._quantity:
            print(f"Le stock du produit {self._product.name} est insuffisant")
            return False
        else:
            self._quantity -= quantity
            self._sales += quantity * self._product.price
            return True
    
    #Méthode Restock  
    def restock(self, quantity):
        """
        La méthode restock est utilisée pour augmenter la quantité en stock lorsqu'un nouveau stock de produit est reçu. 
        Elle met également à jour les dépenses totales pour restocker ce produit.
        """
        # Ajouter la quantité reçue à la quantité en stock
        # Ajouter le coût total de la nouvelle quantité reçue à la variable 'expenses' en multipliant la quantité reçue par le coût du produit
        self._quantity += quantity
        self._expenses += quantity * self._product.price
    
    #Méthode repr 
    def __repr__(self):
        """
        La méthode repr est utilisée pour fournir une représentation en chaîne de caractères de l'objet InventoryProductEntry, 
        qui contient des informations utiles telles que le nom du produit, la marque, la quantité en stock et le prix du produit.
        """
        # Retourner une chaîne de caractères formatée contenant le nom du produit, la marque, la quantité en stock et le prix du produit.
        return f"{self._product.name} ({self._product.marque}): {self._quantity} in stock, price:{self._product.price}"
