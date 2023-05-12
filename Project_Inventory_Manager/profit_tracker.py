from product_classes import Product

class ProfitTracker:
    """ Compute the balance with each entry or sell"""
    def __init__(self):
        # Créer une variable 'balance' et l'initialiser à 1000 euros
        self._balance = 1000
    
    def buy_product(self, product: Product, quantity): 
        """   
        La méthode buy_product est utilisée pour acheter un produit et mettre à jour le coût total et le solde.
        """
        # Vérifie si le solde est suffisant pour acheter la quantité demandée de produit
        #     Si le solde est insuffisant:
        #         affiche un message d'erreur 
        #         retourne False pour indiquer que l'achat a échoué.
        #     Sinon, si le solde est suffisant:
        #         met à jour le solde en soustrayant le coût du produit multiplié par la quantité achetée
        #         retourne True pour indiquer que l'achat a réussi
        if self._balance >= float(product.cost) * quantity:
            self._balance -= float(product.cost) * quantity
            return True
        else:
            print("Solde insuffisant pour acheter la quantité demandée")
            return False

    def sell_product(self, product: Product, quantity):
        """   
        La méthode sell_product est utilisée pour vendre un produit et mettre à jour le solde.
        """
        # Met à jour le solde en ajoutant le prix du produit multiplié par la quantité vendue
        self._balance += float(product.price) * quantity
