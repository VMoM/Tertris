# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe TitleView, qui gère la partie Vue du MVC
# quand on est sur l'écran titre
# ==========================================================

import curses
import locale

from typing import Any

from modules.view import View
import modules.view.color_pairs as color_pairs

from modules.direction import Direction

import modules.view.title_view.config as config


class TitleView(View):
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_window_logo",
        "_window_buttons",
        "_window_bottom_texts",
        "_highlighted_button"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    # Since the curses module puts the _CursesWindow class private, I had
    # to declare them as Any :/
    _window_logo: Any
    _window_buttons: Any
    _window_bottom_texts: Any
    _highlighted_button: int

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            highlighted_button: int = config.BUTTON_START
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet TitleView, héritant de View, ajoutant :
        # - une fenêtre contenant le logo (_window_logo)
        # - une fenêtre contenant les boutons de l'écran titre (_window_buttons)
        # - une fenêtre contenant les textes en bas de l'écran titre (_window_bottom_texts)
        # Et le paramètre pour qu'il soit capable de gérer la partie
        # -----------------------------
        # REMARQUES :
        # - Se referer aux remarques de View
        # =============================
        View.__init__(self)

        self.set_window_logo(
            curses.newwin(
                config.LOGO_HEIGHT,
                config.LOGO_WIDTH,
                config.LOGO_BEGIN_Y,
                config.LOGO_BEGIN_X
            )
        )

        self.set_window_buttons(
            curses.newwin(
                config.BUTTONS_HEIGHT,
                config.BUTTONS_WIDTH,
                config.BUTTONS_BEGIN_Y,
                config.BUTTONS_BEGIN_X
            )
        )

        self.set_window_texts(
            curses.newwin(
                config.TEXTS_HEIGHT,
                config.TEXTS_WIDTH,
                config.TEXTS_BEGIN_Y,
                config.TEXTS_BEGIN_X
            )
        )

        self.set_highlighted_button(highlighted_button)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_window_logo(self) -> Any:
        return self._window_logo

    def get_window_buttons(self) -> Any:
        return self._window_buttons

    def get_window_bottom_texts(self) -> Any:
        return self._window_bottom_texts

    def get_highlighted_button(self) -> int:
        return self._highlighted_button

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_window_logo(self, window_logo: Any) -> None:
        self._window_logo = window_logo

    def set_window_buttons(self, window_buttons: Any) -> None:
        self._window_buttons = window_buttons

    def set_window_texts(self, window_bottom_texts: Any) -> None:
        self._window_bottom_texts = window_bottom_texts

    def set_highlighted_button(self, highlighted_button: int):
        self._highlighted_button = highlighted_button

    ###############################################################
    ####################### SET_BACKGROUNDS #######################
    ###############################################################
    def set_backgrounds(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Met les fonds d'écran des différentes fenêtres de la bonne couleur
        # -----------------------------
        # PRÉCONDITIONS :
        # - set_colorscheme() a déjà été appelé
        # =============================
        View.set_backgrounds(self)
        self.get_window_logo().bkgd(' ', curses.color_pair(color_pairs.BLACK_N_WHITE))
        self.get_window_buttons().bkgd(' ', curses.color_pair(color_pairs.BLACK_N_WHITE))
        self.get_window_bottom_texts().bkgd(' ', curses.color_pair(color_pairs.BLACK_N_WHITE))

        self.refresh_all()

    ###############################################################
    ######################## REFRESH_ALL ##########################
    ###############################################################
    def refresh_all(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Actualise toutes les fenêtres
        # -----------------------------
        # PRÉCONDITIONS :
        # - Toutes les fenêtres existent
        # =============================
        View.refresh_all(self)
        self.get_window_logo().refresh()
        self.get_window_buttons().refresh()
        self.get_window_bottom_texts().refresh()

    ###############################################################
    ############## PRINT_WITHOUT_PARAMETER_WINDOWS ################
    ###############################################################
    def print_without_parameter_windows(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche toutes les fenêtres qui n'ont pas besoin de paramètres
        # =============================
        self.print_logo()
        self.print_bottom_texts()
        self.print_buttons()

    ###############################################################
    ########################## PRINT_LOGO #########################
    ###############################################################
    def print_logo(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche le logo
        # =============================
        # Ligne 0
        self.get_window_logo().addstr(
            0, 11,
            "▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_BLUE)
        )
        self.get_window_logo().addstr(
            0, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_WHITE)
        )

        # Ligne 1
        # début du >
        self.get_window_logo().addstr(
            1, 0,
            "▄".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        # bordure gauche
        self.get_window_logo().addstr(
            1, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_BLUE)
        )
        # début du T
        self.get_window_logo().addstr(
            1, 12,
            "▛▀▀▀▀▜".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # début du E
        self.get_window_logo().addstr(
            "▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        self.get_window_logo().addstr(
            "▀▀▀▀▜".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # début du R
        self.get_window_logo().addstr(
            "▛▀▀▀▀".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        self.get_window_logo().addstr(
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # début du T
        self.get_window_logo().addstr(
            "▛▀▀▀▀▜".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # début du deuxième R
        self.get_window_logo().addstr(
            "▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        self.get_window_logo().addstr(
            "▀▀▀▀▜".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # début du I
        self.get_window_logo().addstr(
            "▛▜".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # début du S
        self.get_window_logo().addstr(
            "▐",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        self.get_window_logo().addstr(
            "▀▀▀▀▀".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        self.get_window_logo().addstr(
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # bordure droite
        self.get_window_logo().addstr(
            1, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_WHITE)
        )

        # Ligne 2
        # début du >
        self.get_window_logo().addstr(
            2, 0,
            "▀█▄".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        # bordure gauche
        self.get_window_logo().addstr(
            2, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_BLUE)
        )
        # début du T
        self.get_window_logo().addstr(
            2, 12,
            "▙▄▖▗▄▟".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # début du E
        self.get_window_logo().addstr(
            "▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        self.get_window_logo().addstr(
            "   ▗".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        self.get_window_logo().addstr(
            "▘ ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # début du R
        self.get_window_logo().addstr(
            "▌▗▄▖▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # début du deuxième T
        self.get_window_logo().addstr(
            "▙▄▖▗▄▟".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # début du deuxième R
        self.get_window_logo().addstr(
            "▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        self.get_window_logo().addstr(
            " ▄▄ ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        self.get_window_logo().addstr(
            "▌ ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # début du I
        self.get_window_logo().addstr(
            "▙▟".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # début du S
        self.get_window_logo().addstr(
            "▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        self.get_window_logo().addstr(
            "    ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # bordure droite
        self.get_window_logo().addstr(
            2, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_WHITE)
        )

        # Ligne 3
        # début du >
        self.get_window_logo().addstr(
            3, 2,
            "▀█▄".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        # bordure gauche
        self.get_window_logo().addstr(
            3, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_BLUE)
        )
        self.get_window_logo().addstr(
            3, 12,
            "  ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # début du T
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # début du E
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        self.get_window_logo().addstr(
            " ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        self.get_window_logo().addstr(
            "▀▀".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        self.get_window_logo().addstr(
            "  ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # début du R
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        self.get_window_logo().addstr(
            "▗".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        self.get_window_logo().addstr(
            "▘".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        self.get_window_logo().addstr(
            "▌   ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # début du deuxième T
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # début du deuxième R
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        self.get_window_logo().addstr(
            "▌▟".encode(locale.getpreferredencoding()),  # on devrait afficher ▌▞ mais ça pose problème
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        self.get_window_logo().addstr(
            "▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # I et début du S
        self.get_window_logo().addstr(
            "  ▄▄▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        self.get_window_logo().addstr(
            "▀▌ ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # bordure droite
        self.get_window_logo().addstr(
            3, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_WHITE)
        )

        # Ligne 4
        self.get_window_logo().addstr(
            4, 4,
            "▀█▄".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        # bordure gauche
        self.get_window_logo().addstr(
            4, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_BLUE)
        )
        # Espace entre bordure gauche et T
        self.get_window_logo().addstr(
            "  ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # T
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre T et E & début du E
        self.get_window_logo().addstr(
            "  ▐",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # E
        self.get_window_logo().addstr(
            " ▝▀▜".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre E et R
        self.get_window_logo().addstr(
            "  ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            "▌▐▘▞".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre R et T
        self.get_window_logo().addstr(
            "    ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # T
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre T et R & début du R
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            " ▛▗".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Fin R et espace entre R et I
        self.get_window_logo().addstr(
            "▘  ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # I
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre I et S
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # Début du S
        self.get_window_logo().addstr(
            "▌  ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Fin du S et espace entre S et bordure droite
        self.get_window_logo().addstr(
            "▌  ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        self.get_window_logo().addstr(
            4, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_WHITE)
        )

        # Ligne 5
        self.get_window_logo().addstr(
            5, 6,
            "▀█▄".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        # Bordure gauche
        self.get_window_logo().addstr(
            5, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_BLUE)
        )
        # Espace entre bordure gauche et T
        self.get_window_logo().addstr(
            "  ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # T
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre T et E & début du E
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # E
        self.get_window_logo().addstr(
            "   ",
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Fin du E & espace entre E et R
        self.get_window_logo().addstr(
            "▌  ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            "▌▐▚▝".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # fin R et espace entre R et T
        self.get_window_logo().addstr(
            "▖   ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # T
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre T et R & début de R
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            " ▛▖▚".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre R et I
        self.get_window_logo().addstr(
            "  ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # I
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre I et S & début de S
        self.get_window_logo().addstr(
            " ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # S
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre S et bordure droite
        self.get_window_logo().addstr(
            "  ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # Bordure droite
        self.get_window_logo().addstr(
            5, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_WHITE)
        )

        # Ligne 6
        self.get_window_logo().addstr(
            6, 6,
            "▄█▀".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        # Bordure gauche
        self.get_window_logo().addstr(
            6, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_BLUE)
        )
        # Espace entre bordure gauche et T
        self.get_window_logo().addstr(
            "  ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # T
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre T et E & debut E
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # E
        self.get_window_logo().addstr(
            " ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Fin E et espace E - R
        self.get_window_logo().addstr(
            "▀   ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # R
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace R - T
        self.get_window_logo().addstr(
            "   ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # T
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace R - T & début R
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # R
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Fin R & espace R - I
        self.get_window_logo().addstr(
            "▌ ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # I
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace I - S
        self.get_window_logo().addstr(
            "  ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # S
        self.get_window_logo().addstr(
            "▌  ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Fin S et espace S - bordure droite
        self.get_window_logo().addstr(
            "▌ ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # Bordure droite
        self.get_window_logo().addstr(
            6, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_WHITE)
        )

        # Ligne 7
        self.get_window_logo().addstr(
            7, 4,
            "▄█▀".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        # Bordure gauche
        self.get_window_logo().addstr(
            7, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_BLUE)
        )
        # Espace entre bordure gauche et T
        self.get_window_logo().addstr(
            "  ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # T
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre T et E & debut E
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # E
        self.get_window_logo().addstr(
            " ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace E - R
        self.get_window_logo().addstr(
            "    ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # R
        self.get_window_logo().addstr(
            " ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Fin R et espace R - T
        self.get_window_logo().addstr(
            "▌  ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # T
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace T - R et début du R
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # R
        self.get_window_logo().addstr(
            "▌ ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace R - I
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # I
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace I - S et début du S
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # S
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace S - bordure droite
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # Bordure droite
        self.get_window_logo().addstr(
            7, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_WHITE)
        )

        # Ligne 8
        self.get_window_logo().addstr(
            8, 2,
            "▄█▀".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        # Bordure gauche
        self.get_window_logo().addstr(
            8, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_BLUE)
        )
        # Espace entre bordure gauche et T
        self.get_window_logo().addstr(
            "  ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # T
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre T et E & debut E
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # E
        self.get_window_logo().addstr(
            " ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # E et espace E - R
        self.get_window_logo().addstr(
            "▄▄▖ ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # R
        self.get_window_logo().addstr(
            "  ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre R et T
        self.get_window_logo().addstr(
            "  ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # T
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre T et R et début de R
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # R
        self.get_window_logo().addstr(
            "▌ ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Fin de R et espace entre R et I
        self.get_window_logo().addstr(
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # I
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre I et S et début de S
        self.get_window_logo().addstr(
            "▐▄▄".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # S
        self.get_window_logo().addstr(
            "▌  ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Fin de S et espace S - bordure droite
        self.get_window_logo().addstr(
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # Bordure droite
        self.get_window_logo().addstr(
            8, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_WHITE)
        )

        # Ligne 9
        self.get_window_logo().addstr(
            9, 0,
            "▄█▀".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        # Bordure gauche
        self.get_window_logo().addstr(
            9, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_BLUE)
        )
        # Espace entre bordure gauche et T
        self.get_window_logo().addstr(
            "  ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # T
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre T et E & debut E
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # E
        self.get_window_logo().addstr(
            "    ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre E et R
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # R
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Fin R et espace R - T
        self.get_window_logo().addstr(
            "▌ ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # T
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace T - R et début de R
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # R
        self.get_window_logo().addstr(
            "▌  ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # I
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # S
        self.get_window_logo().addstr(
            "▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # S
        self.get_window_logo().addstr(
            "     ",
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # S
        self.get_window_logo().addstr(
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        self.get_window_logo().addstr(
            9, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_WHITE)
        )

        # Ligne 10
        self.get_window_logo().addstr(
            10, 0,
            "▀".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        # Bordure gauche
        self.get_window_logo().addstr(
            10, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_BLUE)
        )
        # Espace entre bordure gauche et T
        self.get_window_logo().addstr(
            "  ".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # T
        self.get_window_logo().addstr(
            "▙▟".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre T et E & debut E
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # E
        self.get_window_logo().addstr(
            "▄▄▄▄▄".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Fin E et espace E - R
        self.get_window_logo().addstr(
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            "▙▟".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # R
        self.get_window_logo().addstr(
            "   ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            "▙▟".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace R - T
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # T
        self.get_window_logo().addstr(
            "▙▟".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace T - R et début de R
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R
        self.get_window_logo().addstr(
            "▄".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # R
        self.get_window_logo().addstr(
            "▌  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # R et I
        self.get_window_logo().addstr(
            "▄█▟".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Espace entre I et S et début S
        self.get_window_logo().addstr(
            "▐".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # S
        self.get_window_logo().addstr(
            "▄▄▄▄▄".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLACK)
        )
        # Fin S et espace S - bordure gauche
        self.get_window_logo().addstr(
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_BLUE)
        )
        # Bordure gauche
        self.get_window_logo().addstr(
            10, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_WHITE)
        )

        # Ligne 11
        self.get_window_logo().addstr(
            11, 11,
            "▙▄▄▄▄▄▄▄▄▄▄▄▄▄▖             ▄▄▄▄▄▄▄▄▄▄▄▄▄▄".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_BLUE)
        )
        self.get_window_logo().addstr(
            11, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_WHITE)
        )

        # Lignes 12 à 22
        for line in range(12, 23):
            self.get_window_logo().addstr(
                line, 25,
                "▌             ".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.RED_N_BLUE)
            )
            self.get_window_logo().addstr(
                line, 39,
                "▌".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.RED_N_WHITE)
            )

        # Ligne 23
        self.get_window_logo().addstr(
            23, 25,
            "▙▄▄▄▄▄▄▄▄▄▄▄▄▄".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_BLUE)
        )
        self.get_window_logo().addstr(
            23, 39,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.RED_N_WHITE)
        )

        self.get_window_logo().refresh()

    ###############################################################
    ######################## PRINT_BUTTONS ########################
    ###############################################################
    def print_buttons(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche les boutons, avec l'actif en surbrillance
        # =============================
        color_for_start = curses.color_pair(color_pairs.BLACK_N_BLUE)
        color_for_options = curses.color_pair(color_pairs.BLACK_N_BLUE)
        color_for_high_scores = curses.color_pair(color_pairs.BLACK_N_BLUE)
        color_for_quit = curses.color_pair(color_pairs.BLACK_N_BLUE)
        if self._highlighted_button == config.BUTTON_START:
            color_for_start = curses.color_pair(color_pairs.BLACK_N_WHITE)
        elif self._highlighted_button == config.BUTTON_OPTIONS:
            color_for_options = curses.color_pair(color_pairs.BLACK_N_WHITE)
        elif self._highlighted_button == config.BUTTON_HIGH_SCORES:
            color_for_high_scores = curses.color_pair(color_pairs.BLACK_N_WHITE)
        elif self._highlighted_button == config.BUTTON_QUIT:
            color_for_quit = curses.color_pair(color_pairs.BLACK_N_WHITE)

        self.get_window_buttons().addstr(0, 3, "START", color_for_start)
        self.get_window_buttons().addstr(2, 2, "OPTIONS", color_for_options)
        self.get_window_buttons().addstr(4, 0, "HIGH SCORES", color_for_high_scores)
        self.get_window_buttons().addstr(6, 3, "QUIT", color_for_quit)

        self.get_window_buttons().refresh()

    ###############################################################
    ##################### PRINT_BOTTOM_TEXTS ######################
    ###############################################################
    def print_bottom_texts(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche les texts en bas de l'écran
        # =============================
        self.get_window_bottom_texts().addstr(
            0, 0,
            "Tertris is a Tetris © clone made by VMoM, under MIT License".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        self.get_window_bottom_texts().addstr(
            1, 12,
            "Tetris © 1985~2021 Tetris Holding.".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        self.get_window_bottom_texts().addstr(
            2, 4,
            "Tetris logos, Tetris theme song and Tetriminos are",
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        self.get_window_bottom_texts().addstr(
            3, 15,
            "trademarks of Tetris Holding.",
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        self.get_window_bottom_texts().addstr(
            4, 4,
            "The Tetris trade dress is owned by Tetris Holding.",
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        self.get_window_bottom_texts().addstr(
            5, 14,
            "Licensed to The Tetris Company.",
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        self.get_window_bottom_texts().addstr(
            6, 10,
            "Tetris Game Design by Alexey Pajitnov.",
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        self.get_window_bottom_texts().addstr(
            7, 13,
            "Tetris Logo Design by Roger Dean.",
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        self.get_window_bottom_texts().addstr(
            8, 19,
            "All Rights Reserved.",
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )

        self.get_window_bottom_texts().refresh()

    def get_button(self, direction: Direction) -> int:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne le nom du bouton selon la direction
        # =============================
        if direction == Direction.DOWN:
            return (self.get_highlighted_button() + 1) % 4
        elif direction == Direction.UP:
            return 3 if (self.get_highlighted_button() - 1 < 0) else (self.get_highlighted_button() - 1)
        else:
            return self.get_highlighted_button()
