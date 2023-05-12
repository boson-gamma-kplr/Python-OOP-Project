#La classe "InventoryManager" est une classe qui permet de gérer un inventaire de produits. 
import product_classes
from product_classes import Product
from inventory_product_entry import InventoryProductEntry
from profit_tracker import ProfitTracker

class InventoryManager:
    # Initialisation de la classe
    def __init__(self):
        # Vous initialisez un dictionnaire 'inventory' qui stocke l'inventaire de tous les produits
        # Il prend comme clé le nom du produit, et la valeur est un objet InventoryProductEntry
        self.inventory : Dict[str, InventoryProductEntry] = {}
        self._profitTracker = ProfitTracker()

    #Méthode product_exists
    def product_exists(self, product_name):
        """"
        La fonction prend un objet Product en entrée et vérifie si son nom est une clé dans le dictionnaire self.inventory. 
        Si c'est le cas, la fonction retourne True, sinon elle retourne False.
        """
        # pour chaque 'inventory_product_entry_key' dans self.inventory faire:
        #     si 'inventory_product_entry_key' est égal à product.name alors:
        #         retourner True
        # retourner False
        # for inventory_product_entry_key in self.inventory:
        #     if inventory_product_entry_key == product.name:
        #         return True
        # return False
        return product_name in self.inventory
    
    #Méthode add_product
    
    def add_product(self, product:Product, quantity):
        """
        La méthode add_product est utilisée pour ajouter un nouveau produit à l'inventaire.
        Elle prend en argument un objet Product et une quantité initiale.
        """
        # SI le produit existe déjà dans l'inventaire: 
        #     afficher un message pour informer l'utilisateur
        # Sinon:
        #     Créer un nouvel objet InventoryProductEntry en utilisant le produit et la quantité fournis
        #     Ajouter le nouvel objet au dictionnaire 'inventory'
        if self.product_exists(product.name):
            print(f"Product already exist")
        else:
            if self._profitTracker.buy_product(product, quantity):
                self.inventory[product.name] = InventoryProductEntry(product, quantity)
                return True
        return False
    
    #Méthode remove_product
    def remove_product(self, product_name):
        """
        La méthode remove_product est utilisée pour supprimer un produit de l'inventaire.
        Elle prend en argument un nom de produit et supprime l'entrée correspondante dans le dictionnaire 'inventory'.
        """
        #Utiliser la méthode product_exists pour vérifier si le produit existe dans l'inventaire
        #Si le produit est trouvé, supprimer le de l'inventaire
        #Sinon, afficher un message d'erreur indiquant que le produit n'a pas été trouvé
        if self.product_exists(product_name):
            self.inventory.pop(product_name)
        else:
            print(f"No product named {product_name} found")
    
    #Méthode sell_product
    def sell_product(self, product_name, quantity):
        """
        La méthode sell_product est utilisée pour vendre une quantité donnée d'un produit.
        Elle prend en argument le nom du produit et la quantité à vendre.
        """
        #Utiliser une boucle pour parcourir les clés du dictionnaire 'inventory'
        #Pour chaque itération, on vérifie si le nom du produit fourni est équal à la clé du dictionnaire.
        #Si le produit est trouvé, appeler la méthode 'sell' de l'objet InventoryProductEntry correspondant avec la quantité à vendre
        #Sinon, afficher un message d'erreur indiquant que la vente a échoué
        if self.product_exists(product_name):
            self.inventory[product_name].sell(quantity)
            self._profitTracker.sell_product(self.get_product(product_name), quantity)
        else:
            print("Sell failed, no product named {product_name} found")
    
    #Méthode restock_product
   
    def restock_product(self, product_name, quantity):
        """
        La méthode restock_product est utilisée pour restocker une quantité donnée d'un produit.
        Elle prend en argument le nom du produit et la quantité à restocker.
        """
        #Vérifier si le produit existe déjà dans l'inventaire
        #Si le produit est trouvé, appeler la méthode 'restock' de l'objet InventoryProductEntry correspondant avec la quantité à restocker
        #Si le réapprovisionnement est réussi, afficher un message de confirmation
        #Sinon, on appelle la méthode add_product pour ajouter le produit en stock avec une quantité nulle et on rappelle la fonction restock_product pour le restocker
        if self.product_exists(product_name):
            if self._profitTracker.buy_product(self.get_product(product_name), quantity):
                self.inventory[product_name].restock(quantity)
                print(f"Restock completed")
        else:
            if self._profitTracker.buy_product(self.get_product(product_name), quantity):
                self.add_product(self.get_product(product_name),quantity)


    #Méthode get_product
    def get_product(self, product_name):
        """
        La méthode get_product retourne toutes les informations liées au produit en faisant une recherche par son nom.
        Elle prend en entrée un nom de produit.
        """
        # pour chaque inventory_product_entry_key dans self.inventory:
        #     si inventory_product_entry_key == nom de produit:
        #         retourner self.inventaire[inventory_product_entry_key].product
        # afficher un message pour indiquer que le produit n'existe pas
        if self.product_exists(product_name):
            return self.inventory[product_name]._product
        else:
            print(f"No product named {product_name} found")
            return None

    #Méthode list_products
    def list_products(self):
        """
        La méthode list_products(self) parcourt tous les produits de l'inventaire 
        et affiche les informations relatives à chacun d'entre eux (nom, quantité disponible, prix unitaire, coût unitaire, prix de vente unitaire, bénéfice unitaire). 
        """
        # pour chaque clé du dictionnaire 'inventory':
        #     afficher la valeur correspondante à cette clé
        # retourner le dictionnaire inventaire
        for key, _ in self.inventory.items():
            print(key)

        return self.inventory
    
    def get_balance(self):
        return self._profitTracker._balance
