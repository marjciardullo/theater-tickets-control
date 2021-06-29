teatro=[]

def inicializar(linha=5,coluna=10):
    for i in range(linha):
        fileira=[]
        for j in range(coluna):
            fileira.append('vazio')
        teatro.append(fileira)


def vender(lin,col):
    teatro[lin][col]='Vendido'
    
def devolver(lin,col):
    teatro[lin][col]='vazio'

def Ocupado(lin,col):
    if teatro[lin][col] == 'Vendido':
        return True
    else:
        return False


def foradoLimite(lin,col):
    if (lin > len(teatro) or col > len(teatro[0])):
        print(lin)
        return True
    else:
        return False


    
        
       
    

    
    
    






