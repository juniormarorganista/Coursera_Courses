class ordenador:
  def selecao_direta(self, lista):
     fim = len(lista)
     for i in range(fim - 1):
        ''' Inicialmente, o menor elemento ja visto eh o i-esimo'''
        pos_min = i
        for j in range(i+1,fim):
           if (lista[j] < lista[pos_min]):
             pos_min = j
        ''' Coloca o elemento encontrado no inicio da sub-lista trocando de lugar'''
        lista[i], lista[pos_min] = lista[pos_min], lista[i]
     return lista

def selecao_direta(lista):
    fim = len(lista)
    for i in range(fim-1):
        pos_menor = i
        for j in range(i+1,fim):
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        lista[i],lista[pos_menor] = lista[pos_menor],lista[i]
        print(lista)
    return lista

numeros = [55,33,0,900,-432,10,77,2,11]
print(selecao_direta(numeros))

