# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe PlayerAction, l'énumération des inputs que peut faire le joueur
# ==========================================================

from enum import Enum, auto

import curses  # nécessaire pour les constantes de curses

class PlayerInput(Enum):
    NOTHING = curses.ERR

    KEY_LEFT = curses.KEY_LEFT
    KEY_RIGHT = curses.KEY_RIGHT
    KEY_UP = curses.KEY_UP
    KEY_DOWN = curses.KEY_DOWN

    # les caractère ne peuvent être qu'en minuscule pour des raisons
    # de simplicité
    KEY_D = 100
    KEY_P = 112
    KEY_Q = 113
    KEY_S = 115

    KEY_ESC = 27

    KEY_UNUSED = auto()
