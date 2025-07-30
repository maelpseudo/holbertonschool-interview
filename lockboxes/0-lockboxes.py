#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Détermine si l’on peut ouvrir toutes les boîtes numérotées de 0 à n-1.

    Args:
        boxes (list of list of int): 
            Liste de n listes, où boxes[i] contient les clés (entiers) trouvées dans la boîte i.
    Returns:
        bool: 
            True si chaque boîte de 0 à n-1 a pu être ouverte en partant de la boîte 0, 
            False sinon.
    """
    # --- Initialisation : on garde pour chaque boîte un indicateur "ouvert" (1) ou "fermé" (0)
    isopen = [0] * len(boxes)
    isopen[0] = 1   # la boîte 0 est déverrouillée par défaut

    # --- Parcours des clés : pour chaque boîte (même celles non ouvertes, ton code actuel les traite toutes)
    #     on marque ouverte la boîte référencée par chacune des clés
    for box in boxes:
        for key in box:
            # si la clé correspond à une boîte valide, on peut l'ouvrir
            if 0 <= key < len(boxes):
                isopen[key] = 1
            # on ne fait qu'un seul key par boîte dans ton code d’origine (le `break`),
            # mais pour documenter il faudrait expliquer pourquoi
            break

    # --- Vérification finale : s’il reste au moins une boîte non ouverte, on échoue
    if 0 in isopen:
        return False
    else:
        return True
