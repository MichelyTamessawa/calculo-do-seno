# Cálculos do seno de 0 a 360 graus e dos erros de precisão
# Aplicamos o esquema de Horner nas fórmulas dos cálculos de seno e cosseno
# Utilizamos redução para o primeiro quadrante para que o angulo ficasse no intervalo de seguranca
# intervalo de seguranca = [-pi/4 , pi/4]

import math

def seno(x):
    A = -1.666666666666667e-1
    B = 8.33333333333333e-3
    C = -1.98412698412698e-4
    D = 2.75573192239859e-6
    E = -2.505210838544172e-08
    F = 1.6059043836821613e-10
    G = - 7.647163731819816e-13
    w = x*x

    senx = x*(1+w*(A+w*(B+w*(C+w*(D+w*(E+w*(F+G*w)))))));

    return senx


def cosseno(x):
    A = -5.000000000e-1
    B = 0.041666666666666664
    C = - 0.001388888888888889
    D = 2.48015873015873e-05
    E = -2.755731922398589e-07
    F = 2.08767569878681e-09
    G = -1.1470745597729725e-11
    w = x*x

    cosx = 1 + w*(A+w*(B+w*(C+w*(D+w*(E+w*(F+G*w))))))

    return cosx


# reduz para o primeiro quadrante
def reduzQuad(x):
    if x > 90 and x <= 180:
        return (180 -  x)
    elif x > 180 and  x <= 270:
        return (x - 180)
    else:
        return (360 - x)


def calculaSeno(entrada):
    # dentro do intervalo de seguranca
    if (entrada >= -45) and (entrada <= 45): 
            resultado = seno(math.radians(entrada))
    
    # angulo entre 45 e 90 graus
    elif entrada > 45 and entrada<= 90:
        resultado = cosseno(math.radians(90-entrada))

    # fora do primeiro quadrante
    else:
        novo_angulo = reduzQuad(entrada) 
        resultado =  calculaSeno(novo_angulo)
        
        # terceiro e quarto quadrante têm seno negativo
        if  entrada > 180:
            resultado =  -resultado  

    return resultado


def main():
    diferenca = 0
    maiorDiferenca = 0
    maiorDifIndex = -1

    for i in range(0, 361, 10):
        print("====== Seno " + str(i) + " ======")

        resultado = calculaSeno(i)

        print(resultado, "(nosso resultado)")
        print(math.sin(math.radians(i)), "(math)")

        diferenca = abs(resultado - math.sin(math.radians(i)))
        print("Diferença: " + str(diferenca))
        if(diferenca > maiorDiferenca):
            maiorDiferenca = diferenca
            maiorDifIndex= i

    print("===============")
    print("Resultado final")
    print("A maior diferenca foi de " + str(maiorDiferenca) + " no seno de " + str(maiorDifIndex) + " graus")
    
main()
