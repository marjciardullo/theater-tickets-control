class Contador:
    def __init__(self):
        self.cont=0
    
    def incrementa(self):
        self.cont+=1
        
    def decrementa(self):
        self.cont-=1
        
    def pegaContador(self):
        return self.cont
    
