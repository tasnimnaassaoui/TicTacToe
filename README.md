# Tic Tac Toe avec IA intelligente (Minimax)

Ce projet implémente un jeu de **Tic Tac Toe** avec une **intelligence artificielle** utilisant l'algorithme **Minimax**. L'IA apprend à jouer de manière optimale grâce à des données générées à partir de parties simulées. L'IA peut jouer contre un utilisateur humain dans une interface graphique construite avec **Tkinter**.

L'IA utilise l'algorithme Minimax, qui évalue tous les coups possibles à partir de l'état actuel du plateau.  
Génération du dataset : Lors de chaque simulation de partie, les positions du plateau et le meilleur coup à jouer sont stockés dans un fichier .npz.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les bibliothèques suivantes :

- **Python**
- **TensorFlow**
- **NumPy**
- **Tkinter** (pour l'interface graphique)

### Installation des dépendances

1. Installez **Python 3.x** depuis [python.org](https://www.python.org) (si ce n'est pas déjà fait).

2. Installez les dépendances nécessaires avec **pip** :

   ```bash
   pip install tensorflow numpy
   ```

   **TensorFlow** est utilisé pour la gestion du modèle d'IA.

   **NumPy** est utilisé pour manipuler les matrices (le plateau du jeu).

## Structure du Projet

La structure du projet est la suivante :

```bash
TIC/
├── data_generator.py      # Génère les données pour entraîner l'IA
├── jeu_tkinter.py         # Interface graphique et logique du jeu
├── train_model.py         # Entraînement du modèle d'IA avec les données générées
├── tictactoe_data.npz     # Fichier contenant les données d'entraînement du modèle
└── README.md                  # Ce fichier
```
