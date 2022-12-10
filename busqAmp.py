"""
    Busqueda por amplitud, inteligencia artificial.
    Integrantes:
    Cruz Zamora Joel David
    Zarate Diaz Sofia Viridiana
"""
import time
# Libreria para manejar listas
from collections import deque as deq
# Libreria para quitar repetidos
from collections import OrderedDict

# Recibe un estado y regresa los 3 hijos posibles
def generaHijos(padre, lista):
    pos0 = padre[0]
    pos1 = padre[1]
    pos2 = padre[2]
    pos3 = padre[3]

    lista.append("{}{}{}{}".format(pos1,pos0,pos2,pos3))
    lista.append("{}{}{}{}".format(pos0,pos2,pos1,pos3))
    lista.append("{}{}{}{}".format(pos0,pos1,pos3,pos2))

# Quita estados en la lista1 que estén en la lista2, y quita repetidos
def quitarEdosPasados(lista1, lista2):
    temp = deq()
    if lista2:    
        for item1 in lista1:
            if item1 not in lista2:
                    temp.append(item1)
    else:
        temp = lista1

    # quita repetidos dentro de la lista
    temp = deq(OrderedDict.fromkeys(temp))
    return temp
    

            
# Principal
def amplitud():
    edoInicial = input("Ingresa el estado inicial:")
    edoFinal = input("Ingresa el estado final:")

    no_revisados = deq()
    revisados = deq()
    indicePadre = deq()
    ruta = deq()

    edoAct = ""
    edoPadre = ""
    nivel = 0
    no_revisados.append(edoInicial)

    while True:
        if edoAct == edoFinal:
            print("Estado actual y final iguales")
            break
        else:
            # Si el estado actual NO es el final
            if no_revisados:
                # Si la cola no_revisados no esta vacia
                edoAct = no_revisados.popleft()
            else:
                # Si la cola no_revisados esta vacia
                edoPadre = revisados[nivel]
                print("Nuevo estado padre: {}".format(edoPadre))
                generaHijos(edoPadre, no_revisados)
                no_revisados = quitarEdosPasados(no_revisados, revisados)
                #print("No revisados: {}".format(no_revisados))

                # Cuando ya no hay mas hijos nuevos, causa un error. Acá se evita
                try:
                    edoAct = no_revisados.popleft()
                except IndexError:
                    print("No hay hijos nuevos para este estado.")
                
                nivel += 1
        
            print("Estado actual: {}".format(edoAct))
            revisados.append(edoAct)
            indicePadre.append([edoAct,nivel-1])
            #print("Revisados: {}".format(revisados))

        time.sleep(0.5)

    # Inicializa variables para obtener ruta
    duo = indicePadre.pop()
    indice = duo[1]
    ruta.append(duo[0])

    while indice >= 0:
        duo = indicePadre[indice]
        indice = duo[1]
        ruta.append(duo[0])

    ruta.reverse()
    print("La ruta de solución es: {}".format(ruta))


amplitud()