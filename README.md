# Tic Tac Toe avec IA intelligente (Minimax)

Ce projet implémente un jeu de **Tic Tac Toe** (Morpion) avec une **intelligence artificielle** utilisant l'algorithme **Minimax**. L'IA apprend à jouer de manière optimale grâce à des données générées à partir de parties simulées. L'IA peut jouer contre un utilisateur humain dans une interface graphique construite avec **Tkinter**.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les bibliothèques suivantes :

- **Python 3.6+**
- **TensorFlow 2.x**
- **NumPy**
- **Tkinter** (pour l'interface graphique)

### Installation des dépendances

1. Installez **Python 3.x** depuis [python.org](https://www.python.org) (si ce n'est pas déjà fait).
2. Créez un environnement virtuel (recommandé) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux / macOS
   venv\Scripts\activate     # Windows
   ```
3. Installez les dépendances nécessaires avec **pip** :

   ```bash
   pip install tensorflow numpy
   ```

   **TensorFlow** est utilisé pour la gestion du modèle d'IA.

   **NumPy** est utilisé pour manipuler les matrices (par exemple, le plateau du jeu).

   **Tkinter** : Tkinter est normalement installé avec Python, mais si ce n’est pas le cas, vous pouvez l’installer via votre gestionnaire de paquets (par exemple apt-get sur Linux) ou brew sur macOS.

## Structure du Projet

La structure du projet est la suivante :

```bash
tictactoe-ai/
├── intelligent/
│   ├── data_generator.py      # Génère les données pour entraîner l'IA
│   ├── jeu_tkinter.py         # Interface graphique et logique du jeu
│   └── train_model.py         # Entraînement du modèle d'IA avec les données générées
├── tictactoe_data.npz         # Fichier contenant les données d'entraînement du modèle
└── README.md                  # Ce fichier
```
