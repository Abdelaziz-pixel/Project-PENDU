"""This file defines useful functions for the hanged program.

We use the data of the program contained in data.py """

import os
import pickle
from random import choice

from données import *

# Score Management

def recup_scores():
    """This function retrieves the recorded scores if the file exists.
     In all cases, we return a dictionary,
     the unpicked object,
     an empty dictionary.

     We rely on name_file_scores defined in data.py"""
    
    if os.path.exists(nom_fichier_scores): # The file exists
         # We retrieve it
        fichier_scores = open(nom_fichier_scores, "rb")
        mon_depickler = pickle.Unpickler(fichier_scores)
        scores = mon_depickler.load()
        fichier_scores.close()
    else: # File does not exist
        scores = {}
    return scores

def enregistrer_scores(scores):
    """This function is responsible for saving the scores in the file
     nom_fichier_scores. It receives in parameter the dictionary of the scores
     to save"""

    fichier_scores = open(nom_fichier_scores, "wb") # We crush the old scores
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()

# Functions managing the items entered by the user

def recup_nom_utilisateur():
    """Function responsible for retrieving the name of the user.
     The name of the user must be at least 4 characters long,
     numbers and letters exclusively.

     If this name is not valid, the function is called recursively
     to get a new one"""

    nom_utilisateur = input("Type your name: ")
    # The first letter is capitalized and the others in lower case
    nom_utilisateur = nom_utilisateur.capitalize()
    if not nom_utilisateur.isalnum() or len(nom_utilisateur)<4:
        print("This name is invalid.")
        # We call the function again to have another name
        return recup_nom_utilisateur()
    else:
        return nom_utilisateur

def recup_lettre():
    """This function retrieves a letter entered by
     the user. If the retrieved string is not a letter,
     we call the function recursively until we get a letter """

    lettre = input("Type a letter: ")
    lettre = lettre.lower()
    if len(lettre)>1 or not lettre.isalpha():
        print("You did not enter a valid letter.")
        return recup_lettre()
    else:
        return lettre

# Hangman Game Functions
def choisir_mot():
    """This function returns the chosen word in the word list
     wordlist.

    We use the choice function of the random module."""
    
    return choice(liste_mots)

def recup_mot_masque(mot_complet, lettres_trouvees):
    """This function returns a masked word in whole or in part, depending on:
     - the original word (type str)
     - already found letters (type list)

     We return the original word with * replacing the letters that we
     has not yet found."""
    
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque