# ------------------------------------------------------------
# 1. Importation des modules
# ------------------------------------------------------------

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


# ------------------------------------------------------------
# 2. Parcours en profondeur (DFS) — construction de l'arbre
# ------------------------------------------------------------

def parcours_en_profondeur(G, depart):
    """
    Effectue un parcours en profondeur (DFS) sur un graphe G
    et renvoie l'arbre orienté Père → Enfant.
    """
    Etat = {}      # nv = non-visité, v = visité, t = traité
    Pere = {}      # père dans l'arbre DFS
    Numero = {}    # ordre de visite
    Index = 1      #Valeur de depart de l'index


    S = list(G.nodes()) # prend l'ensemble des sommets

    # Initialisation : tout les sommets sont non-visités au départ
    for x in S:
        Etat[x] = "nv"

    # Si aucun départ donné → prendre le premier sommet
    if depart is None:
        depart = S[0]

    # -------------------------
    #  Fonction récursive DFS (De parcours en profondeur)
    # -------------------------
    def dfs(x): # Pour chaque sommet dans S
        nonlocal Index

        Etat[x] = "v"
        Numero[x] = Index
        Index += 1

        for y in G.neighbors(x):
            if Etat[y] == "nv":
                Pere[y] = x
                dfs(y) # recursion

        Etat[x] = "t"

    # La racine n’a pas de père
    Pere[depart] = None
    #pourquoi dfs depart ici ?
    dfs(depart)

    # -------------------------
    # Construction du graphe-orienté DFS
    # -------------------------

    # Affichage console (pour vérification)
    print("Etat :", Etat)
    print("Père :", Pere)
    print("Numero :", Numero)

    T = nx.DiGraph()

    for fils, pere in Pere.items():
        T.add_node(fils)
        if pere is not None:
            T.add_edge(pere, fils)

    return T


# ------------------------------------------------------------
# 3. Layout hiérarchique
# ------------------------------------------------------------

def hierarchy_layout(T, root):
    """
    Positionne les nœuds d'un arbre orienté T (root → enfants)
    en niveaux horizontaux, sans croiser les arêtes.
    """

    # BFS dans T (orienté)
    levels = {root: 0}
    queue = [root]

    while queue:
        x = queue.pop(0)
        for y in T.successors(x):  # orienté !
            if y not in levels:
                levels[y] = levels[x] + 1
                queue.append(y)

    # Groupement par niveau
    layers = {}
    for node, lvl in levels.items():
        layers.setdefault(lvl, []).append(node)

    # Positionnement
    pos = {}
    for lvl, nodes in layers.items():
        step = 1 / (len(nodes) + 1)
        for i, node in enumerate(nodes):
            pos[node] = (i * step, -lvl)

    return pos


# ------------------------------------------------------------
# 4. Affichage de l'arbre
# ------------------------------------------------------------

def afficher_arbre(T, depart):
    pos = hierarchy_layout(T, depart)
    nx.draw(T, pos, with_labels=True, node_size=800, arrows=True)
    plt.show()


# ------------------------------------------------------------
# 5. Programme principal
# ------------------------------------------------------------
# Liste d'adjacence du graphe
graphe_exo = {
    1: [2, 3],
    2: [1, 5],
    3: [1, 4, 6],
    4: [3],
    5: [2, 6, 7],
    6: [3, 5, 8],
    7: [5, 8],
    8: [6, 7, 9],
    9: [8]
}

# Création du graphe NetworkX
G = nx.Graph()
for sommet, voisins in graphe_exo.items():
    for voisin in voisins:
        G.add_edge(sommet, voisin)

# BFS + construction arbre
depart = 1
arbre_T = parcours_en_profondeur(G, depart=depart)

# Affichage de l'arbre BFS
afficher_arbre(arbre_T, depart=depart)



