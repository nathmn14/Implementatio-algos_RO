# Pour visualiser, on va se servir de networkx et de matplotlib

#1. Imporation des modules-----------------------------------------------------------------------------------------------

import networkx as nx
import matplotlib.pyplot as plt

#2. Representation du graphe--------------------------------------------------------------------------------------------

# liste d'adjacence

graphe_exo = {
     1 : [2,3],
     2 : [1,5],
     3 : [1,4,6],
     4 : [3],
     5 : [2,6,7],
     6 : [3,5,8],
     7 : [5,8],
     8 : [6,7,9],
     9 : [8]
 }

# graphe avec networkx
G = nx.Graph()  # instanciation d'un graphe
#Creation du graphe a l'aide de networkx, le graphe a des sommets (nodes) et des arretes(edges)

for sommet , voisins  in graphe_exo.items() : # on itere sur chaque sommet et ses voisins
    for voisin in voisins :                     # pour chaque sommet, on cree les arretes =  on le connecte a ses voisins
        G.add_edge(sommet,voisin)

# fin de la creation du graphe a partir de la liste d'adjacence.
# NB : il s'agit d'un graphe non-oriente.


#3. visualisation avec matplotlib et networkx----------------------------------------------------------------------------------
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=800, arrows=True) # fait appel a matplotlib pour creer une representation du graphe
plt.show() # affiche le graphe deja represente via matplotlib en arriere plan avec nx.draw, avec plt.show de matplotlib


# TODO : Creer une fonction pour qui nous renvoie un graphe G a partir d'une liste d'adjacence
# TODO : Comment créer un graphe orienté avec networkx