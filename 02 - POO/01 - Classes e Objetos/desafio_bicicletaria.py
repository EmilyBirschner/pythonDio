class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Plim plim")
        
    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parada")
    
    def correr(self):
        print("Acelerando a bicicleta...")
        print("Correndo")

        
  #  def __str__(self):
   #     return f'--------------------- \nModelo: {self.modelo} \nCor: {self.cor} \nAno: {self.ano} \nValor: {self.valor} \n---------------------\n'
   
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
b1 = Bicicleta("Vermelha", "caloi", 2022, 600)
#b1.buzinar()
#b1.correr()
#b1.parar()

b2 = Bicicleta("verde", "monark", 2000, 200)
#b2.buzinar() #Bicicleta.buzinar(b2)
print(b2)
print(b1)

   