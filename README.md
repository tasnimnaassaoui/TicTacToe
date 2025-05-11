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
├── tictactoe_data.npz     # Fichier contenant les données d'entraînement du modèle (généré suite à l'exécution de data_generator.py)
├── tictactoe_model.h5     # Fichier contenant le modèle à utiliser (généré suite à l'exécution de train_model.py)
└── README.md             
```

## Étapes du Projet

Le projet se divise en plusieurs étapes principales, et chacune de ces étapes est détaillée ci-dessous :

### Étape 1 : Générer des données avec data_generator.py
#### But :
Cette étape génère un jeu de données à partir de parties simulées entre l'IA et un joueur aléatoire. Ces données sont ensuite utilisées pour entraîner un modèle de prédiction des meilleurs coups à jouer par l'IA.

#### Fonctionnement :
* La fonction Minimax est utilisée pour choisir les meilleurs coups pour l'IA.

* Le jeu est simulé, et à chaque étape, le coup optimal de l'IA est enregistré.

* Le dataset généré contient des positions du plateau et le meilleur coup à jouer par l'IA.

```bash
python data_generator.py

```
Après l'exécution, un fichier tictactoe_data.npz contenant les données générées sera créé.

### Étape 2 : Entraîner le modèle avec train_model.py
#### But :
Cette étape entraîne un modèle d'IA en utilisant les données générées dans l'étape 1. Le modèle sera utilisé pour prédire le meilleur coup de l'IA à partir d'un état donné du plateau.

#### Fonctionnement :
* Les données générées (plateaux et coups associés) sont chargées à partir du fichier tictactoe_data.npz.

* Un modèle de réseau de neurones est créé et entraîné sur ces données avec TensorFlow.

* L'IA apprend à identifier les bons coups à partir des positions sur le plateau.

```bash
python train_model.py
```
Après l'exécution, un fichier tictactoe_model.h5 representant le modèle sera créé.

### Étape 3 : Jouer avec l'IA dans une interface graphique avec jeu_tkinter.py
#### But :
Cette étape permet à l'utilisateur de jouer contre l'IA via une interface graphique créée avec Tkinter.

#### Fonctionnement :
* Un plateau de jeu 3x3 est affiché avec des boutons interactifs.

* L'utilisateur peut cliquer sur une case pour jouer.

* Après chaque coup de l'utilisateur, l'IA choisit son coup en utilisant le modèle entraîné pour jouer de manière optimale.

* La partie se termine lorsqu'un joueur gagne ou que la partie est un match nul.

Commande pour lancer le jeu :

```bash
python jeu_tkinter.py
```

### Explication du Code
* data_generator.py : Génération de données d’entraînement
* Minimax : L'algorithme Minimax est utilisé pour choisir le meilleur coup possible en simulant tous les coups futurs possibles. Il évalue chaque coup selon un score, et l'IA choisit le coup avec le score le plus élevé.

* Simulation de parties : Le code simule des parties avec des coups choisis aléatoirement et enregistre les coups optimaux en utilisant Minimax.

* Génération du dataset : Lors de chaque simulation de partie, les positions du plateau et le meilleur coup à jouer sont stockés dans un fichier .npz.

* train_model.py : Entraînement du modèle
* Modèle TensorFlow : Un réseau de neurones simple est utilisé pour prédire le meilleur coup basé sur les entrées du plateau.

* Entraînement : Le modèle est entraîné sur les données générées dans l’étape précédente en utilisant la fonction de perte mean squared error et l’optimiseur Adam.

Le modèle prend les positions du plateau comme entrée et prédit le meilleur coup possible à chaque étape.

* jeu_tkinter.py : Interface graphique
* Tkinter : La bibliothèque Tkinter est utilisée pour créer une interface graphique avec un plateau de jeu 3x3.

* Interaction utilisateur : L'utilisateur clique sur les cases pour jouer, et l'IA répond avec un coup choisi par le modèle.

* Affichage de la partie : Après chaque coup, le plateau est mis à jour et l'état de la partie est affiché dans l'interface graphique.

