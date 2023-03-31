class Persona:
    def __init__(self, nombre:str, edad:int):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola mi nombre es: {self.nombre}"
class Empleado(Persona):
    def __init__(self, nombre: str, edad: int, sueldo:int):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    def pagaImpuestos(self):
        if self.sueldo > 3000:
            return f"{self.nombre} tiene que pagar impuesto"
        return f"{self.nombre} no tiene que pagar impuesto"
persona = Persona("Renz", 25)
print(persona.saludar())

empleado = Empleado("Carlos", 77, 1500)
print(empleado.saludar())
print(empleado.pagaImpuestos())