#não pode ser alterada. garante a integridade dos dados
numero = (9, 8, 12, 8, 7, 8, 9,)
#para ser uma tupla precisa estar entre parenteses
print("tupla original:", numero)
#inportando para o usuario a tupla original, sem manipulações
print("tamanho da tupla: ", len(numero))
print("acessando pelo indice: ", numero[2])
#escolhendo qual item
print("fazendo slicking do 2 ao 5:", numero[2:5])
#o slicking ele nao paga o ultimo item definido no recorte
print("quantas veses o numero 8 repete: ", numero.count(8), "vezes")
print("posiçao da primeira ocorrencia do numero 7:", numero.index(7))
minimo_tupla=min(numero)
print(minimo_tupla)
maximo_tupla=max(numero)
print("maior numero dentro da tupla é: ",maximo_tupla )
print("soma dos elementos da tupla é: ", sum(numero))
tupla_ordenada=sorted(numero)
print("os numeros em ordem utilizando o metodo sorted", tupla_ordenada)
print("o numero 4 está na tupla ",4 in numero )
numero2=(15,20)
tupla_concatenada=numero+numero2
print(" a concentraçao das tuplas 1e2 resulta na nova tupla:", tupla_concatenada)
tupla_duplicada=numero*2
print("tupla_duplicada")
