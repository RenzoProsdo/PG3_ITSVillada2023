
class Familia:
    def __init__(self, padre:str, madre:str, hijos:list):
        self.padre = padre
        self.madre = madre 
        self.hijos = hijos
    def __str__(self):
        return f"""
        Padre: {self.padre}
        Madre: {self.madre}
        Hijos: {",".join(self.hijos)}
        """

family = Familia("Carlos", "Carla", ["Carlitos, Carlin, Crlitus"])

print(family)