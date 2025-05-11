import numpy as np
import random
import copy

def gagnant(plateau):
    lignes = [plateau[0:3], plateau[3:6], plateau[6:9]]
    colonnes = [plateau[i::3] for i in range(3)]
    diagonales = [[plateau[0], plateau[4], plateau[8]], [plateau[2], plateau[4], plateau[6]]]
    for ligne in lignes + colonnes + diagonales:
        if ligne.count(ligne[0]) == 3 and ligne[0] != 0:
            return ligne[0]
    return 0

def est_plein(plateau):
    return all(c != 0 for c in plateau)

def minimax(plateau, joueur, profondeur=0, max_profondeur=4):
    gagnant_partie = gagnant(plateau)
    if gagnant_partie != 0:
        return gagnant_partie * joueur
    if est_plein(plateau) or profondeur >= max_profondeur:
        return 0  # Limiter la recherche à max_profondeur

    meilleur_score = -2
    for i in range(9):
        if plateau[i] == 0:
            plateau[i] = joueur
            score = -minimax(plateau, -joueur, profondeur + 1, max_profondeur)
            plateau[i] = 0
            if score > meilleur_score:
                meilleur_score = score
    return meilleur_score


def meilleur_coup(plateau, joueur):
    meilleurs = []
    meilleur_score = -2
    for i in range(9):
        if plateau[i] == 0:
            plateau[i] = joueur
            score = -minimax(plateau, -joueur, profondeur=0, max_profondeur=4)
            plateau[i] = 0
            if score > meilleur_score:
                meilleurs = [i]
                meilleur_score = score
            elif score == meilleur_score:
                meilleurs.append(i)

    if meilleurs:
        return random.choice(meilleurs)
    else:
        # Cas où il n'y a pas de meilleur coup, choisir aléatoirement
        coups_possibles = [i for i, c in enumerate(plateau) if c == 0]
        return random.choice(coups_possibles) if coups_possibles else 0



def generer_donnees(nb_exemples=5000):
    X = []
    y = []

    for _ in range(nb_exemples):
        plateau = [0] * 9
        historique = []

        for _ in range(random.randint(2, 5)):
            coups = [i for i in range(9) if plateau[i] == 0]
            if not coups:
                break
            # Joueur aléatoire
            i = random.choice(coups)
            plateau[i] = 1
            gagn = gagnant(plateau)
            if gagn != 0:
                break
            coups = [i for i in range(9) if plateau[i] == 0]
            if not coups:
                break
            j = random.choice(coups)
            plateau[j] = -1
            gagn = gagnant(plateau)
            if gagn != 0:
                break

        plateau_actuel = plateau.copy()
        coup_optimal = meilleur_coup(plateau_actuel, 1)

        entree = plateau_actuel
        sortie = [0] * 9
        sortie[coup_optimal] = 1
        X.append(entree)
        y.append(sortie)

    return np.array(X), np.array(y)

if __name__ == "__main__":
    X, y = generer_donnees(10000)
    np.savez("tictactoe_data.npz", X=X, y=y)
    print("✅ Dataset intelligent généré dans 'tictactoe_data.npz'")
