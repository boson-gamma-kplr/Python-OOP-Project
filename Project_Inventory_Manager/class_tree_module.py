import json
from unidecode import unidecode

def json_dict_from_file(file_path):
    """
    Cette fonction ouvre et charge les données JSON du fichier
    dans un dictionnaire Python.

    Returns:
        dict: le dictionnaire Python contenant les données JSON du fichier
    """
    # Chargement des données JSON à partir du fichier dans un dictionnaire python
    json_data = json.load(open(file_path, "rb"))
    
    # il est nécessaire de reconvertir le dictionnaire en chaine de caractere pour le traiter ensuite
    json_str = json.dumps(json_data)

    # Utilisation de la fonction unidecode pour enlever les accents et autres caractères spéciaux
    json_data = (unidecode(json_str))

    # Conversion de la chaine de caractere JSON à nouveau en dictionnaire Python
    # Le dictionnaire python est plus pratique à manipuler que la chaine de caractère car il est structuré
    json_dict = json.loads(json_data)

    return json_dict

def create_tree_from_dict(tree, parent_node_id, parent_dict):
    """
    Cette fonction crée un arbre à partir d'un dictionnaire.
    Elle est appelée récursivement pour chaque sous-dictionnaire.

    Args:
        tree (Tree): un objet Tree de la bibliothèque treelib pour représenter l'arbre
        parent_node_id (str): l'identifiant du noeud parent dans l'arbre
        parent_dict (dict): le dictionnaire Python contenant les données à insérer dans l'arbre
    """
    for key, value in parent_dict.items():
        if isinstance(value, dict):
            # Créer un nouveau noeud pour la clé courante du dictionnaire            
            # Créer récursivement le sous-arbre pour le dictionnaire courant
            new_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)
            if "subclasses" in value:
                create_tree_from_dict(tree, new_node_id, value["subclasses"])

