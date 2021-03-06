# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Grid, qui sert à représenter la grille de jeu
# ==========================================================

from typing import List, Optional

from modules.tetromino.active_tetromino import ActiveTetromino
from modules.tetromino import TetrominoType

import modules.config_general as config


class Grid:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_shape"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _shape: List[List[Optional[TetrominoType]]]

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            shape: List[List[Optional[TetrominoType]]] = None
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Grid, caractérisé par :
        # - une forme (_shape)
        # =============================
        self.set_shape(shape)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_shape(self) -> List[List[Optional[TetrominoType]]]:
        return self._shape

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_shape(self, shape: List[List[Optional[TetrominoType]]] = None) -> None:
        if shape is None:
            # On crée un tableau à deux dimensions rempli de False
            self._shape = []
            for line in range(config.GRID_HEIGHT):
                self._shape.append([])
                for _ in range(config.GRID_WIDTH):
                    self._shape[line].append(None)
        else:
            self._shape = shape

    ###############################################################
    ######################### GET_ELEMENT #########################
    ###############################################################
    def get_element(self, x: int, y: int) -> Optional[TetrominoType]:
        return self.get_shape()[y][x]

    ###############################################################
    ######################### IS_OCCUPIED #########################
    ###############################################################
    def is_occupied(self, x: int, y: int) -> bool:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne si la case est occupée par un bloc
        # =============================
        return (
                y >= 0  # Utilisé à la fin d'une partie, au découpage du tétromino actif
                and
                self.get_shape()[y][x] is not None
        )

    ###############################################################
    ######################## IS_LINE_FULL #########################
    ###############################################################
    def is_line_full(self, line_number: int) -> bool:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne si la ligne est remplie
        # =============================
        column = 0
        while column < config.GRID_WIDTH and self.is_occupied(x=column, y=line_number):
            column += 1
        return column == config.GRID_WIDTH

    ###############################################################
    ###################### DROP_LINES_UPPER #######################
    ###############################################################
    def drop_lines_upper(self, line_number: int) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Remplace la ligne par la ligne au-dessus, la ligne au-dessus par celle d'encore au-dessus, etc.
        # La première ligne du tableau deviendra vide
        # =============================
        # On remplace la ligne par la ligne au-dessus, la ligne au-dessus par celle d'encore au-dessus, etc.
        line = line_number
        while line != 0:
            self.get_shape()[line][:] = self.get_shape()[line - 1][:]
            line -= 1
        # On remplie la ligne la plus en haut de None pour la vider
        for column in range(config.GRID_WIDTH):
            self.get_shape()[0][column] = None

    ###############################################################
    #################### ADD_ACTIVE_TETROMINO #####################
    ###############################################################
    def add_active_tetromino(self, active_tetromino: ActiveTetromino) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Ajoute le tétromino actuel dans la grille
        # =============================
        for line in range(active_tetromino.get_height()):
            for column in range(active_tetromino.get_width()):
                if (
                        0 <= active_tetromino.get_x() + column < config.GRID_WIDTH
                        and 0 <= active_tetromino.get_y() + line < config.GRID_HEIGHT
                        and active_tetromino.is_occupied(x=column, y=line)
                ):
                    self.get_shape()[
                            line + active_tetromino.get_y()
                        ][
                            column + active_tetromino.get_x()
                        ] = active_tetromino.get_shape()[line][column]
