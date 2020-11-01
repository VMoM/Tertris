# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Model
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + GETTERS
# + SETTERS
# + send_query()
# + do_tick()
# ==========================================================

from typing import Optional
from random import choice

from modules.classes.commons.Grid import Grid
from modules.classes.commons.Tetromino import Tetromino, tetromino_factory
from modules.classes.commons.ActiveTetromino import ActiveTetromino
from modules.classes.commons.Statistics import Statistics

from modules.classes.commons.Direction import Direction
from modules.classes.commons.TetrominoType import TetrominoType

from modules.settings import GRID_WIDTH, GRID_HEIGHT


class Model:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_grid",
        "_active_tetromino",
        "_next_tetromino",
        "_stored_tetromino",
        "_statistics"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _grid: Grid
    _active_tetromino: ActiveTetromino
    _next_tetromino: Tetromino
    _stored_tetromino: Optional[Tetromino]
    _statistics: Statistics

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            grid: Grid = None,
            active_tetromino: ActiveTetromino = None,
            next_tetromino: Tetromino = None,
            stored_tetromino: Optional[Tetromino] = None,
            statistics: Statistics = None
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Model, caractérisé par :
        # - la grille de jeu (_grid)
        # - le tetromino actif (_active_tetromino)
        # - le prochain tétromino (_next_tetromino)
        # - le tetromino stocké (_stored_tetromino)
        # - les statistiques de la partie (_statistics)
        # =============================
        if grid is None:
            grid = Grid()

        if active_tetromino is None:
            active_tetromino = ActiveTetromino(4, 0, tetromino=random_next_tetromino())

        if next_tetromino is None:
            next_tetromino = random_next_tetromino()

        if statistics is None:
            statistics = Statistics()

        self.set_grid(grid)
        self.set_active_tetromino(active_tetromino)
        self.set_next_tetromino(next_tetromino)
        self.set_stored_tetromino(stored_tetromino)
        self.set_statistics(statistics)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_grid(self) -> Grid:
        return self._grid

    def get_active_tetromino(self) -> ActiveTetromino:
        return self._active_tetromino

    def get_next_tetromino(self) -> Tetromino:
        return self._next_tetromino

    def get_stored_tetromino(self) -> Optional[Tetromino]:
        return self._stored_tetromino

    def get_statistics(self) -> Statistics:
        return self._statistics

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_grid(self, grid: Grid) -> None:
        self._grid = grid

    def set_active_tetromino(self, active_tetromino: ActiveTetromino) -> None:
        self._active_tetromino = active_tetromino

    def set_next_tetromino(self, next_tetromino: Tetromino) -> None:
        self._next_tetromino = next_tetromino

    def set_stored_tetromino(self, stored_tetromino: Optional[Tetromino]) -> None:
        self._stored_tetromino = stored_tetromino

    def set_statistics(self, statistics: Statistics) -> None:
        self._statistics = statistics

    ###############################################################
    ########################### DO_TICK ###########################
    ###############################################################
    def do_tick(self):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Effectue la séquence d'évènement qui se joue à chaque tick
        # dans le modèle :
        # - Regarder si le tétromino actif peut faire un mouvement vers le bas
        # - Si oui, le faire
        # - Si non, l'ajouter à la grille, passer au prochain tétromino, et générer un nouveau prochain tétromino
        # =============================
        if self.can_active_tetromino_move(Direction.DOWN):
            self.get_active_tetromino().move(Direction.DOWN)
        else:
            self.get_grid().add_active_tetromino(self.get_active_tetromino())
            self.set_active_tetromino(ActiveTetromino(x=4, y=0, tetromino=self.get_next_tetromino()))
            self.set_next_tetromino(random_next_tetromino())

    ###############################################################
    ################# CAN_ACTIVE_TETROMINO_MOVE ###################
    ###############################################################
    def can_active_tetromino_move(self, direction: Direction) -> bool:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne si le tétromino actuel peut effectuer le mouvement
        # =============================
        line = 0

        possible = True
        while line < 4 and possible:
            column = 0
            while column < 4 and possible:
                possible = (
                    not self.get_active_tetromino().is_occupied(x=column, y=line)  # Soit il n'y a pas de bloc
                    or  # ou
                    (  # Soit le bloc va aller dans les bordures de la grille ...
                        0 <= self.get_active_tetromino().get_x() + column + direction.value.get_x() < GRID_WIDTH
                        and
                        0 <= self.get_active_tetromino().get_y() + line + direction.value.get_y() < GRID_HEIGHT
                    )
                    and not (  # ... et l'emplacement futur n'est pas occupé
                        self.get_grid().is_occupied(
                            self.get_active_tetromino().get_x() + direction.value.get_x() + column,
                            self.get_active_tetromino().get_y() + direction.value.get_y() + line
                        )
                    )
                )
                column += 1
            line += 1
        return possible


###############################################################
################### RANDOM_NEXT_TETROMINO #####################
###############################################################
def random_next_tetromino() -> Tetromino:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Tire au hazard le prochain tétromino
    # =============================
    return tetromino_factory(choice(list(TetrominoType)))
