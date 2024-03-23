def afficher_plateau(plateau):
    for ligne in plateau:
        print("|".join(ligne))
        print("-" * 5)
 
def verifier_victoire(plateau, joueur):
   
    for i in range(3):
        if all(plateau[i][j] == joueur for j in range(3)) or all(plateau[j][i] == joueur for j in range(3)):
            return True
   
    if all(plateau[i][i] == joueur for i in range(3)) or all(plateau[i][2 - i] == joueur for i in range(3)):
        return True
    return False

def morpion():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    symboles = ["X", "O"]
    tour = 0

    while True:
        afficher_plateau(plateau)
        joueur = symboles[tour % 2]
        print("Tour du joueur", joueur)
        ligne = int(input("Entrez le numéro de ligne (0, 1, 2) : "))
        colonne = int(input("Entrez le numéro de colonne (0, 1, 2) : "))

        if plateau[ligne][colonne] == " ":
            plateau[ligne][colonne] = joueur
            if verifier_victoire(plateau, joueur):
                afficher_plateau(plateau)
                print("Le joueur", joueur, "a gagné !")
                break
            if all(plateau[i][j] != " " for i in range(3) for j in range(3)):
                afficher_plateau(plateau)
                print("Match nul !")
                break
            tour += 1
        else:
            print("Cette case est déjà occupée. Veuillez choisir une autre case.")

if __name__ == "__main__":
    morpion()
