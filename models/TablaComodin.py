from .Tabla import Tabla


class TablaComodin(Tabla):
    def __init__(self, size="4x4", comodin=1):
        super().__init__(size)
        self.comodin = comodin
