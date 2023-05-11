import sys
sys.path.extend(['.','..','/workspaces/Python-OOP-Project/exercices/05.inventory_product_entry',\
                 '/workspaces/Python-OOP-Project/exercices/06.inventory_manager',\
                 '/workspaces/Python-OOP-Project/exercices/03.class_tree'])
from treelib import Tree
import json
from unidecode import unidecode
#import generator
import readline
#import utils
import treelib
import os
from product_classes import *
from inventory_manager import InventoryManager
from class_tree_module import json_dict_from_file, create_tree_from_dict

# Define the prompt_for_instance function 
# that takes a class name as a string as input
def prompt_for_instance(cls):
    """
    # Get the class object from the class name string
    # Get the names of the constructor arguments
    """
    arg_names = cls.__init__.__code__.co_varnames[1:]
    # Prompt the user for the values of the arguments 
    print(cls.__name__,":")
    args = [input("Enter the value for {}: ".format(name)) for name in arg_names]
    # Create an instance of the class using the entered values
    return cls(*args)

# on cree une classe Tree qui herite de treelib.Tree
# et rajoute deux fonctionnalités supplémentaires
# get_penultimate_nodes -> recupère les avant derniers noeuds
# get_children_nodes -> recupère les noeud terminaux
class TreeExt(treelib.Tree):
    def __init__(self) :
        super().__init__()
    
    def get_penultimate_nodes(self):
        penultimate_nodes = set()
        for node in self.all_nodes():
            if not self.children(node.identifier):
                parent_node = self.parent(node.identifier)
                if parent_node is not None and not self.children(node.identifier):
                    penultimate_nodes.add(parent_node.identifier)
        return penultimate_nodes
    
    # Define a function to get the immediate children nodes of a specified node
    def get_children_nodes(self, node_name):
        children_nodes = []
        node = self.get_node(node_name)
        if node is not None:
            children = self.children(node.identifier)
            children_nodes = [child.identifier for child in children]
        return children_nodes

def sep():
    print("====================")

def main():

    inventory_manager = InventoryManager()
    # write code to read json file as dict

    # Chargement des données JSON à partir du fichier dans un dictionnaire python
    json_dict = json_dict = json_dict_from_file("/workspaces/Python-OOP-Project/exercices/03.class_tree/json_data.json")

    readline.set_completer_delims('\t\n')
    readline.parse_and_bind("tab: complete")

    # Define a function to handle user input
    def auto_complete(text, list):
        matching_entry = [entry for entry in list if entry.startswith(text)]
        if len(matching_entry) >= 1:
            entry_name = matching_entry[0]
            remaining_text = entry_name[len(text):]
            if remaining_text:          
                readline.insert_text(remaining_text)
                readline.redisplay()
                
    def set_autocomplete(list):
        readline.set_completer(lambda text, state: auto_complete(text,list))

    while True:
        print("""
			What would you like to do? :
			A. Add a product to stock
			R. Restock a product quantity
			S. Sell a product quantity
			D. Remove a product from stock
			L. List the products in stock
			B. Show the current balance
			Q. Quit
		""")

        
        choice = input("Enter your choice: ")
        choice = choice.upper()
        

        if choice == "A":                         
            # write code to get class tree hierachy
            # convert the tree object to TreeExt to get the new functionalities 
            # described above in TreeExt class
            # class_tree = TreeExt(generate_tree_hierarchy(json_dict))
            
            # ecrire le code pour récupérer les avant dernier noeus de classe
            # (dernier niveau de catégories de produits)
            # product_classes = class_tree.get_penultimate_nodes()
            #class_tree = TreeExt()
            class_tree = TreeExt()
            # Créer le noeud racine pour l'arbre
            class_tree.create_node(tag="Product Classes Hierarchy", identifier="racine")
            create_tree_from_dict(class_tree, "racine", json_dict)
            sep()

            # write code to print list of product_classes
            print(f"Choisissez une catégorie parmis la liste suivante :\n")
            for node in class_tree.get_penultimate_nodes():
                print(node)
            print("\n")
            set_autocomplete(list(class_tree.get_penultimate_nodes()))
            category = input("Choisissez la catégorie du produit :\n")
            
            # Get the immediate children nodes of node 'B'
            print(f"Choisissez un produit parmis la liste suivante :\n")
            children_nodes = class_tree.get_children_nodes(category)
            # write code to print list of children_nodes
            for node in children_nodes:
                print(node)
            print("\n")

            set_autocomplete(children_nodes)
            product_name = input("Choisissez le produit :\n")   
    
            # write code to add product_entry and quantity in Inventory Manager
            product_entry = prompt_for_instance(globals()[product_name.split('.')[-1]])
            quantity = int(input("Enter quantity: "))
            # write code to create a instance of classe product_name
            inventory_manager.add_product(product_entry,quantity)
            print(f"{quantity} {product_entry.name} ont été rajoutés à l'inventaire .")

        elif choice == "R":
            # write code to get product by name
            print(f"Liste des produits en stock : \n")
            list_of_products = inventory_manager.list_products()
            print('\n')
            set_autocomplete(list_of_products.keys())
            name = input("Entrez le nom du produit a reapprovisionner :\n")
            quantity = int(input("Entrez la quantité de produit a réapprovisionner: \n"))

            # write code to restock product
            inventory_manager.restock_product(name,quantity)
            
        elif choice == "S":
            print(f"Liste des produits en stock : \n")
            list_of_products = inventory_manager.list_products()
            print('\n')
            set_autocomplete(list_of_products.keys())
            name = input("Entrez le nom du produit a vendre :\n")
            quantity = int(input("Entrez la quantité de produit à vendre: \n"))

            inventory_manager.sell_product(name,quantity)

        elif choice == "D":
            print(f"Liste des produits en stock : \n")
            list_of_products = inventory_manager.list_products()
            print('\n')
            set_autocomplete(list_of_products.keys())
            name = input("Enter the name of the product: ")
            # write code to get product

            #if product:
                # write code to remove product
                # 
                #
                #
                #print(f"{name} has been removed from stock.")
            #else:
                #print(f"{name} is not in stock.")

        elif choice == "L":
            inventory_manager.list_products()

        elif choice == "B":
            # write code to print current balance
                # 
            # supprimer la ligne suivante apres avoir ecrit cotre code
            pass
        elif choice == "Q":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == '__main__':
    main()
