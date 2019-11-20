"""Ce fichier contient le jeu du pendu.

Il s'appuie sur les fichiers :
- donnees.py
- fonctions.py"""


from données import *
from fonctions import *

# We get the scores of the game
scores = recup_scores()

# We recover a user name
user = recup_nom_utilisateur()

# If the user does not have a score, add it
if user not in scores.keys():
    scores[user] = 0 # 0 points to start

# Our variable to know when to stop the game
continuer_partie = 'o'

while continuer_partie != 'n':
    print("Joueur {0}: {1} point(s)".format(user, scores[user]))
    mot_a_trouver = choisir_mot()
    lettres_trouvees = []
    mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)
    nb_chances = nb_coups
    while mot_a_trouver!=mot_trouve and nb_chances>0:
        print("Mot à trouver {0} (encore {1} chances)".format(mot_trouve, nb_chances))
        lettre = recup_lettre()
        if lettre in lettres_trouvees: # The letter has already been chosen
            print("Vous avez déjà choisi cette lettre.")
        elif lettre in mot_a_trouver: # The letter is in the word to find
            lettres_trouvees.append(lettre)
            print("Bien joué.")
        else:
            nb_chances -= 1
            print("... non, cette lettre ne se trouve pas dans le mot...")
        mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)

    # Have we found the word where our chances are exhausted?
    if mot_a_trouver==mot_trouve:
        print("Félicitations ! Vous avez trouvé le mot {0}.".format(mot_a_trouver))
    else:
        print("PENDU !!! Vous avez perdu.")

    # We update the score of the user
    scores[user] += nb_chances

    continuer_partie = input("Souhaitez-vous continuer la partie (O/N) ?")
    continuer_partie = continuer_partie.lower()

# The game is over, we record the scores
enregistrer_scores(scores)

# We display the scores of the user
print("Vous finissez la partie avec {0} points.".format(scores[user]))