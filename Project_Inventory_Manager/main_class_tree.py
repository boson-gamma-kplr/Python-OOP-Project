from treelib import Tree

from class_tree_module import json_dict_from_file
from class_tree_module import create_tree_from_dict


def main():
    """
    Cette fonction est la fonction principale qui orchestre toutes les autres.
    Elle charge les données JSON depuis un fichier, crée un objet Tree de la bibliothèque treelib,
    et crée un arbre à partir des données JSON.

    Elle affiche ensuite l'arbre créé.
    """
    my_tree = Tree()
    # Créer le noeud racine pour l'arbre
    my_tree.create_node(tag="Product Classes Hierarchy", identifier="racine")

    # Charger les données JSON depuis un fichier et créer la structure de l'arbre à partir du dictionnaire
    json_dict = json_dict_from_file('Data/json_data_classes.json')
    create_tree_from_dict(my_tree, "racine", json_dict)

    # Afficher l'arbre
    my_tree.show()

if __name__ == '__main__':
    # Appeler la fonction principale
    main()