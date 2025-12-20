# creation d'une matrice de ponderation en python

# 1. definir les sommets ----------------------------------------------------------------------------------------------------------
def creer_matrice_ponderation(sommets, arete):
    """Fonctions qui cree une marrice de ponderation a parte d'une liste de sommets et
    et une liste d'aretes

    ex sommets : sommets = ["A", "B", "C"]
    ex aretes :
    edges = [
    ("A", "B", 3),   # A → B de coût 3
    ("B", "C", 5),   # B → C de coût 5
    ("A", "C", 10)   # A → C de coût 10
]

NB : une arete est une liaison entre 2 points
    """
    n = len(sommets)

    # dictionnaire pour retrouver l'index d'un sommet dans la matrice
    index = {sommets[i]: i for i in range(n)}

    # 2. Initialiser la matrice --------------------------------------------------------------------------------------------------------

    INFINI = float("inf")  # valeur représentant l'infini en python

    # créer une matrice carrée n x n remplie d'infini
    mat = [[INFINI] * n for _ in range(n)]

    # distance de chaque sommet par rapport à lui-même
    for i in range(n):
        mat[i][i] = 0  # ex : distance de A -> A = 0

    # 3. Ajouter les arcs selon leur sens ---------------------------------------------------------------------------------------------
    # insertion des valeurs dans la matrice
    for u, v, w in arete:
        mat[index[u]][index[v]] = w

    # 4. afficher la matrice -----------------------------------------------------------------------------------------------------------

    for row in mat:
        print(row)

    return mat


# Programme principal -----------------------------------------------------------------------------------------------------------------------------------------

# Entrees : sommets + arretes
sommets = ["A", "B", "C"]
aretes = [
    ("A", "B", 3),   # A → B de coût 3
    ("B", "C", 5),   # B → C de coût 5
    ("A", "C", 10)   # A → C de coût 10
]

matrice1 = creer_matrice_ponderation(sommets, aretes)
