def bubbleSort(array):   
  # percorre cada elemento do array
  for i in range(len(array)):       
    swapped = False  
    # loop para comparar os elementos
    for j in range(0, len(array) - i - 1):
      # compara dois elementos vizinhos (adjacentes)
      # se usarmos "<" ao inves de ">" teremos uma array ordenado decrecentemente 
      #teste Alexandre Olah 
      if array[j] < array[j + 1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        swapped = True
    print (array)
    # se nao a trocas significa que esta ordenado
    if not swapped:
      break

data = [11, -41, 38, -86, -55, -95,  7, 28, -70, 31, 19, -66, 43, -67, 45]
bubbleSort(data)
print('Array ordenado:')
print(data)