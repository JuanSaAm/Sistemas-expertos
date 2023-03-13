# Importamos la librería PyKnow
from pyknow import *

# Definimos los hechos iniciales del dominio
class Donante(Fact):
    pass

# Definimos las reglas
class ReglasDonacion(KnowledgeEngine):
    # Regla 1: La edad del donante debe estar entre 18 y 65 años
    @Rule(Donante(edad=P(lambda x: x < 18)))
    def no_apto(self):
        print("El donante es demasiado joven")
        self.declare(Donante(apto=False))

    @Rule(Donante(edad=P(lambda x: x > 65)))
    def no_apto2(self):
        print("El donante es demasiado mayor")
        self.declare(Donante(apto=False))

    # Regla 2: El peso del donante debe ser mayor o igual a 50 kilos
    @Rule(Donante(peso=P(lambda x: x < 50)))
    def no_apto3(self):
        print("El donante pesa menos de 50 kilos")
        self.declare(Donante(apto=False))

    # Regla 3: El donante debe estar en buen estado de salud
    @Rule(Donante(estado_salud='enfermo'))
    def no_apto4(self):
        print("El donante está enfermo")
        self.declare(Donante(apto=False))

    # Regla 4: Si el donante cumple todas las condiciones anteriores, es apto para donar sangre
    @Rule(AND(Donante(edad=P(lambda x: x >= 18)), Donante(edad=P(lambda x: x <= 65)), Donante(peso=P(lambda x: x >= 50)), Donante(estado_salud
