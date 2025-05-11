import tkinter as tk
from tkinter import messagebox
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("tictactoe_model.h5")

def ia_choisit_coup(plateau):
    prediction = model.predict(np.array([plateau]), verbose=0)[0]
    coups_possibles = [i for i, val in enumerate(plateau) if val == 0]
    prediction_filtered = [(i, prediction[i]) for i in coups_possibles]
    meilleur_coup = max(prediction_filtered, key=lambda x: x[1])[0]
    return divmod(meilleur_coup, 3)

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe avec IA")
        self.joueur = "X"
        self.grille = [[0 for _ in range(3)] for _ in range(3)]
        self.boutons = [[None for _ in range(3)] for _ in range(3)]
        self.creer_grille()

    def creer_grille(self):
        for i in range(3):
            for j in range(3):
                bouton = tk.Button(self.root, text="", font=('Arial', 40), width=5, height=2,
                                   command=lambda i=i, j=j: self.clic_utilisateur(i, j))
                bouton.grid(row=i, column=j)
                self.boutons[i][j] = bouton

    def clic_utilisateur(self, i, j):
        if self.boutons[i][j]['text'] == "" and not self.verifier_fin():
            self.boutons[i][j]['text'] = "X"
            self.grille[i][j] = 1
            if self.verifier_victoire(1):
                messagebox.showinfo("Fin de partie", "Tu as gagné !")
                self.reset()
                return
            elif self.est_plein():
                messagebox.showinfo("Fin de partie", "Match nul !")
                self.reset()
                return
            self.root.after(500, self.tour_ia)

    def tour_ia(self):
        grille_flat = [case for ligne in self.grille for case in ligne]
        i, j = ia_choisit_coup(grille_flat)
        if self.grille[i][j] == 0:
            self.boutons[i][j]['text'] = "O"
            self.grille[i][j] = -1
            if self.verifier_victoire(-1):
                messagebox.showinfo("Fin de partie", "L'IA a gagné !")
                self.reset()
            elif self.est_plein():
                messagebox.showinfo("Fin de partie", "Match nul !")
                self.reset()

    def verifier_victoire(self, joueur):
        for i in range(3):
            if all(self.grille[i][j] == joueur for j in range(3)) or all(self.grille[j][i] == joueur for j in range(3)):
                return True
        if all(self.grille[i][i] == joueur for i in range(3)) or all(self.grille[i][2 - i] == joueur for i in range(3)):
            return True
        return False

    def est_plein(self):
        return all(all(cell != 0 for cell in ligne) for ligne in self.grille)

    def verifier_fin(self):
        return self.verifier_victoire(1) or self.verifier_victoire(-1) or self.est_plein()

    def reset(self):
        for i in range(3):
            for j in range(3):
                self.grille[i][j] = 0
                self.boutons[i][j]['text'] = ""

if __name__ == "__main__":
    root = tk.Tk()
    jeu = TicTacToe(root)
    root.mainloop()
