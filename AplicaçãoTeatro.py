import teatro
import contador

conta = contador.Contador()


opc=0
teatro.inicializar()
mteat=teatro.teatro

while opc != 9:
    print("Teatro das Asturias")
    for lin in range(len(mteat)):
        for col in range(len(mteat[0])):
            print(mteat[lin][col],end="  ")
        print()
    print("Total de vendas:"+str(conta.pegaContador()))
    print("1 - vender ingresso")
    print("2 - devolver ingresso")
    print("3 - trocar ingresso")
    print("9 - finalizar")
    opc=int(input("Selecione um opção:"))
    if opc==1:
        print("vender ingresso")
        lin=int(input("Digite a fileira:"))
        col=int(input("Digite a cadeira:"))
        if teatro.foradoLimite(lin,col):
            print("Lugar fora do limite")
        else:
            if teatro.estaOcupado(lin,col):
                print("Lugar ocupado")
            else:
                teatro.vender(lin,col)
                print("Venda com sucesso!!!!")
                conta.incrementa()
    elif opc==2:
        print("devolver ingresso")
        lin=int(input("Digite a fileira:"))
        col=int(input("Digite a cadeira:"))
        if teatro.foradoLimite(lin,col):
            print("Lugar fora do limite")
        else:
            if not teatro.estaOcupado(lin,col):
                print("Lugar está vazio")
            else:
                teatro.devolver(lin,col)
                print("devolução realizada com sucesso!")
                conta.decrementa()
    elif opc==3:
        print("trocar ingresso")
        
        
        

    elif opc==9:
        print("fim")
    else:
        print("opcao inválida")
        

