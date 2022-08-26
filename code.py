def bubbleSort(array, choice):   
  # percorre cada elemento do array
  for i in range(len(array)):       
    swapped = False  
    # loop para comparar os elementos
    for j in range(0, len(array) - i - 1):
      # compara dois elementos vizinhos (adjacentes)
      # se usarmos "<" ao inves de ">" teremos uma array ordenado decrecentemente 
        if(choice == 1):
            if (array[j] > array[j + 1]):
                array[j],array[j+1] = array[j+1],array[j]          
                swapped = True    
        else:
            if (array[j] < array[j + 1]):  
                array[j],array[j+1] = array[j+1],array[j] 
                swapped = True     
    print (array)
    # se nao ha trocas significa que esta ordenado
    if not swapped:
      break

vet = [11, -41, 38, -86, -55, -95,  7, 28, -70, 31, 19, -66, 43, -67, 45]
escolha = input('Escolha uma das opções:\n1 - Crescente.\n2 - Decrescente.\n')
print(escolha)
bubbleSort(vet,escolha)
print('Array:')
print(vet)