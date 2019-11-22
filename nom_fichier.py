"""Hangman Word List"""

mots = [
    "armoire",
    "boucle",
    "buisson",
    "bureau",
    "chaise",
    "carton",
    "couteau",
    "fichier",
    "garage",
    "glace",
    "journal",
    "kiwi",
    "lampe",
    "liste",
    "montagne",
    "remise",
    "sandale",
    "taxi",
    "vampire",
    "volant",
]

"""display of each error by a graphic representation"""

PENDAISON = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']