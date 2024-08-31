from collections import deque

def es_estado_valido(misioneros_izq, canibales_izq):
    if misioneros_izq >= 0 and canibales_izq >= 0 and misioneros_izq <= 3 and canibales_izq <= 3:
        if (misioneros_izq == 0 or misioneros_izq >= canibales_izq) and (3 - misioneros_izq == 0 or 3 - misioneros_izq >= 3 - canibales_izq):
            return True
    return False

def obtener_siguientes_estados(estado):
    misioneros_izq, canibales_izq, barco_izq = estado
    posibles_movimientos = []
    if barco_izq:  # Si el barco está en la orilla izquierda
        movimientos = [(-2, 0), (-1, 0), (0, -2), (0, -1), (-1, -1)]
    else:  # Si el barco está en la orilla derecha
        movimientos = [(2, 0), (1, 0), (0, 2), (0, 1), (1, 1)]

    for movimiento in movimientos:
        nuevo_estado = (misioneros_izq + movimiento[0], canibales_izq + movimiento[1], not barco_izq)
        if es_estado_valido(nuevo_estado[0], nuevo_estado[1]):
            posibles_movimientos.append(nuevo_estado)
    
    return posibles_movimientos

def imprimir_estado(estado):
    misioneros_izq, canibales_izq, barco_izq = estado
    lado_izq = f"{'M'*misioneros_izq}{'C'*canibales_izq}"
    lado_der = f"{'M'(3-misioneros_izq)}{'C'(3-canibales_izq)}"
    barco_pos = " (B)" if barco_izq else ""
    print(f"{lado_izq:<6} | {' ' * (6 - len(lado_der))}{lado_der}{barco_pos}")

def mostrar_camino(camino):
    print("Izquierda | Derecha")
    print("-------------------")
    for estado in camino:
        imprimir_estado(estado)
    print("-------------------\n")

def busqueda_en_amplitud(estado_inicial):
    cola = deque([(estado_inicial, [])])
    visitados = set()

    while cola:
        estado, camino = cola.popleft()
        if estado in visitados:
            continue
        visitados.add(estado)

        if estado == (0, 0, False):
            mostrar_camino(camino + [estado])
            return camino + [estado]

        for siguiente_estado in obtener_siguientes_estados(estado):
            cola.append((siguiente_estado, camino + [estado]))

    return None

def busqueda_en_profundidad(estado_inicial):
    pila = [(estado_inicial, [])]
    visitados = set()

    while pila:
        estado, camino = pila.pop()
        if estado in visitados:
            continue
        visitados.add(estado)

        if estado == (0, 0, False):
            mostrar_camino(camino + [estado])
            return camino + [estado]

        for siguiente_estado in obtener_siguientes_estados(estado):
            pila.append((siguiente_estado, camino + [estado]))

    return None

# Estado inicial
estado_inicial = (3, 3, True)

# Resolver con búsqueda en amplitud
print("Solución por búsqueda en amplitud:")
solucion_amplitud = busqueda_en_amplitud(estado_inicial)

# Resolver con búsqueda en profundidad
print("Solución por búsqueda en profundidad:")
solucion_profundidad = busqueda_en_profundidad(estado_inicial)