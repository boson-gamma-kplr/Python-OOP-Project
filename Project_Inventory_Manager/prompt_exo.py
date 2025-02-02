import readline
import re
from inventory_manager import InventoryManager
from class_tree_module import json_dict_from_file, create_tree_from_dict
from treelib import Tree
from product_classes import *

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
class TreeExt(Tree):
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
    json_dict = json_dict_from_file("Data/json_data_classes.json")

    readline.set_completer_delims('\t\n')
    readline.parse_and_bind("tab: complete")

    # Define a function to handle user input
    def auto_complete(text, list):
        global current_entry_index
        matching_entry = [entry for entry in list if entry.startswith(text)]
        if len(matching_entry) >= 1:
            current_entry_index = current_entry_index + 1 if current_entry_index<len(matching_entry)-1 else 0
            entry_name = matching_entry[current_entry_index]
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
        try:

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
                print("Choisissez une catégorie parmis la liste suivante :\n")
                product_categories = class_tree.get_penultimate_nodes()
                product_categories_tag_id = dict(zip([class_tree.get_node(node).tag for node in product_categories], product_categories))
                for tag,_ in product_categories_tag_id.items():
                    print(tag)
                print("\n")

                set_autocomplete(list(product_categories_tag_id.keys()))
                category = input("Choisissez la catégorie du produit :\n")
                # Get the immediate children nodes of node 'B'
                print("Choisissez un produit parmis la liste suivante :\n")
                children_nodes = class_tree.get_children_nodes(product_categories_tag_id[category])
                product_children_tag_id = dict(zip([class_tree.get_node(node).tag for node in children_nodes], children_nodes))
                # write code to print list of children_nodes
                for tag,_ in product_children_tag_id.items():
                    print(tag)
                print("\n")

                set_autocomplete(list(product_children_tag_id.keys()))
                product_name = input("Choisissez le produit :\n")
        
                # write code to add product_entry and quantity in Inventory Manager
                product_entry = prompt_for_instance(globals()[re.sub("-|\s", "_", product_name.split('.')[-1])])
                quantity = int(input("Enter quantity: "))
                # write code to create a instance of classe product_name
                if inventory_manager.add_product(product_entry,quantity):
                    print(f"{quantity} {product_entry.name} ont été rajoutés à l'inventaire .")
            elif choice == "R":
                # write code to get product by name
                print("Liste des produits en stock : \n")
                list_of_products = inventory_manager.list_products()
                print('\n')
                set_autocomplete(list_of_products.keys())
                name = input("Entrez le nom du produit a reapprovisionner :\n")
                quantity = int(input("Entrez la quantité de produit a réapprovisionner: \n"))

                # write code to restock product
                inventory_manager.restock_product(name,quantity)    
            elif choice == "S":
                print("Liste des produits en stock : \n")
                list_of_products = inventory_manager.list_products()
                print('\n')
                set_autocomplete(list_of_products.keys())
                name = input("Entrez le nom du produit a vendre :\n")
                quantity = int(input("Entrez la quantité de produit à vendre: \n"))

                inventory_manager.sell_product(name,quantity)
            elif choice == "D":
                print("Liste des produits en stock : \n")
                list_of_products = inventory_manager.list_products()
                print('\n')
                set_autocomplete(list_of_products.keys())
                name = input("Enter the name of the product: ")
                # write code to get product
                product = inventory_manager.get_product(name)
                if product:
                    # write code to remove product
                    inventory_manager.remove_product(name)
                    print(f"{name} a été supprimé du stock.")
                else:
                    print(f"{name} n'est pas dans le stock")
            elif choice == "L":
                print("Liste des produits en stock : \n")
                inventory_manager.list_products()
            elif choice == "B":
                # write code to print current balance
                print(f"Balance : {inventory_manager.get_balance()}")
            elif choice == "Q":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        except Exception as exception:
            print(f"Error : {exception}")


if __name__ == '__main__':
    current_entry_index = -1
    main()
