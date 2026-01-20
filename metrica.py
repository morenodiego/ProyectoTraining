class Metrica:
    def __init__(self, peso, altura, edad):
        self.peso = peso
        self.altura = altura
        self.edad = edad
    
    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc
