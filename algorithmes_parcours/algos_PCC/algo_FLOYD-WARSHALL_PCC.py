import networkx as nx
import matplotlib.pyplot as plt
from math import inf

# -------------------------------
# 1. Création du graphe
# -------------------------------

sommets = ["A", "B", "C"]
edges = [
    ("A", "B", 3),
    ("B", "C", 5),
    ("A", "C", 10)
]

# créer la matrice de pondération
n = len(sommets)
index = {sommets[i]: i for i in range(n)}
D0 = [[inf] * n for _ in range(n)]
for i in range(n):
    D0[i][i] = 0
for u, v, w in edges:
    D0[index[u]][index[v]] = w


# -------------------------------
# 2. Floyd-Warshall
# -------------------------------

def floyd_warshall(D0):
    n = len(D0)
    D = [row[:] for row in D0]
    Pi = [[None] * n for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    Pi[i][j] = k
    return D, Pi


def reconstruire_chemin_fw(i, j, Pi):
    k = Pi[i][j]
    if k is None:
        return [i, j]
    else:
        gauche = reconstruire_chemin_fw(i, k, Pi)
        droite = reconstruire_chemin_fw(k, j, Pi)
        return gauche[:-1] + droite


D, Pi = floyd_warshall(D0)

# -------------------------------
# 3. Construire le graphe NetworkX
# -------------------------------

G = nx.DiGraph()  # graphe orienté
for u in sommets:
    G.add_node(u)
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# -------------------------------
# 4. Choisir le chemin à colorer
# -------------------------------

source = "A"
cible = "C"

idx_s = index[source]
idx_c = index[cible]
cout_total = D[idx_s][idx_c]

if cout_total == inf:
    print(f"Pas de chemin entre {source} et {cible}")
    chemin_sommets = []
else:
    chemin_indices = reconstruire_chemin_fw(idx_s, idx_c, Pi)
    chemin_sommets = [sommets[i] for i in chemin_indices]

# -------------------------------
# 5. AFFICHAGE AMÉLIORÉ (Design Pro)
# -------------------------------
plt.figure(figsize=(8, 6))

# Layout : Spring layout avec seed pour la reproductibilité
pos = nx.spring_layout(G, seed=42)

# --- A. Dessiner les arêtes (Fond) ---
# Ajout de la courbure (connectionstyle) et couleur neutre
nx.draw_networkx_edges(G, pos,
                       edgelist=G.edges(),
                       edge_color='#BDC3C7',  # Gris clair
                       width=1.5,
                       arrowstyle='-|>',
                       arrowsize=15,
                       connectionstyle="arc3,rad=0.1")  # Courbure légère

# --- B. Dessiner le chemin (Premier plan) ---
if len(chemin_sommets) > 1:
    path_edges = list(zip(chemin_sommets, chemin_sommets[1:]))
    nx.draw_networkx_edges(G, pos,
                           edgelist=path_edges,
                           edge_color='#E74C3C',  # Rouge vif
                           width=3.0,
                           arrowstyle='-|>',
                           arrowsize=25,
                           connectionstyle="arc3,rad=0.1")  # Même courbure

# --- C. Dessiner les nœuds ---
nx.draw_networkx_nodes(G, pos,
                       node_color='#ECF0F1',  # Blanc cassé
                       edgecolors='#2C3E50',  # Bordure foncée
                       linewidths=2,
                       node_size=1000)

# --- D. Dessiner les labels des arêtes ---
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
                             font_size=10,
                             font_color='#2C3E50',
                             label_pos=0.5,  # Position standard
                             bbox=dict(facecolor="white", edgecolor="none", alpha=0.8, pad=0.5))

# --- E. Dessiner les labels des nœuds (Attention : Zorder supprimé pour éviter l'erreur de compatibilité)
nx.draw_networkx_labels(G, pos,
                        font_size=14,
                        font_family='sans-serif',
                        font_weight='bold',
                        font_color='#2C3E50')

# --- Titre et finition ---
if cout_total != inf:
    # A->B->C (3+5=8) est plus court que A->C (10)
    titre = f"Chemin le plus court : {' → '.join(chemin_sommets)}\nCoût Total = {cout_total}"
else:
    titre = f"Aucun chemin entre {source} et {cible}"

plt.title(titre, fontsize=14, fontweight='bold', pad=15, color='#34495E')
plt.axis('off')  # Cache les axes X/Y
plt.tight_layout()
plt.show()