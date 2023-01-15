class Carro():
    def __init__(self, modelo, velocidade, marca):
        self.modelo = modelo
        self.velocidade = velocidade
        self.marca = marca
    
    def setmodelo(self):
        print(f'O modelo do carro é {self.modelo}')
    
    def setvelocidade(self):
        print(f'O velocidade do carro é {self.velocidade}')
    
    def setmarca(self):
        print(f'A marca do carro é {self.marca}')

carro1 = Carro('Lamborghini Sesto Elemento', 320, 'Lamborghini')
carro1.setmodelo()
carro1.setvelocidade()
carro1.setmarca()