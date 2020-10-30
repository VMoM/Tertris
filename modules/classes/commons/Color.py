# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Color, qui sert à représenter une couleur (actuellement inutile)
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + GETTERS
# + SETTERS
# + get_rgb()
# + get_hexa()
# ==========================================================


class Color:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_red",
        "_green",
        "_blue"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _red: int
    _green: int
    _blue: int

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            red: int,
            green: int,
            blue: int
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Color, caractérisé par ses nuances en :
        # - rouge (_red)
        # - vert (_green)
        # - bleu (_blue)
        # =============================
        self.set_red(red)
        self.set_green(green)
        self.set_blue(blue)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_red(self) -> int:
        return self._red

    def get_green(self) -> int:
        return self._green

    def get_blue(self) -> int:
        return self._blue

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_red(self, red: int) -> None:
        self._red = red

    def set_green(self, green: int) -> None:
        self._green = green

    def set_blue(self, blue: int) -> None:
        self._blue = blue

    ###############################################################
    ########################### GET_RGB ###########################
    ###############################################################
    def get_rgb(self) -> str:
        return str(self.get_red()) + " " + str(self.get_green()) + " " + str(self.get_blue())

    ###############################################################
    ########################### GET_HEXA ##########################
    ###############################################################
    def get_hexa(self) -> str:
        hexa = ""
        for color in (self.get_red(), self.get_green(), self.get_blue()):
            if color < 16:
                hexa += "0" + hex(color)[2:]
            else:
                hexa += hex(color)[2:]
        return hexa
