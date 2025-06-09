import heapq
import matplotlib.pyplot as plt
import networkx as nx

class SimuladorPrim:
    def __init__(self, grafo):
        """
        Inicializa el simulador del algoritmo de Prim.
        
        Args:
            grafo (dict): Diccionario que representa el grafo ponderado no dirigido
        """
        self.grafo = grafo
        self.nodos = list(grafo.keys())
        self.nodos_visitados = set()
        self.aristas_arbol = []
        self.cola_prioridad = []
        self.contador_pasos = 0
        self.peso_total = 0
        
    def mostrar_paso(self, nodo_actual=None, arista_agregada=None):
        """
        Muestra en consola la información del paso actual del algoritmo.
        
        Args:
            nodo_actual (str): Nodo que se está procesando en este paso
            arista_agregada (tuple): Arista agregada al árbol en este paso (nodo1, nodo2, peso)
        """
        self.contador_pasos += 1
        print(f"\n--- Paso {self.contador_pasos} ---")
        
        if nodo_actual:
            print(f"Nodo actual: {nodo_actual}")
        
        if arista_agregada:
            print(f"Arista agregada al árbol: {arista_agregada[0]} - {arista_agregada[1]} (peso: {arista_agregada[2]})")
            print(f"Peso total acumulado: {self.peso_total}")
        
        print("Nodos visitados:", self.nodos_visitados)
        print("Aristas del árbol:", self.aristas_arbol)
        print("Cola de prioridad:", self.cola_prioridad)
    
    def ejecutar(self, visualizar=False, nodo_inicio=None):
        """
        Ejecuta el algoritmo de Prim.
        
        Args:
            visualizar (bool): Si es True, muestra visualización gráfica
            nodo_inicio (str): Nodo desde donde comenzar (si None, se elige aleatoriamente)
        """
        if not nodo_inicio:
            nodo_inicio = self.nodos[0]  # Comenzamos desde el primer nodo por defecto
        
        if visualizar:
            self.preparar_visualizacion()
        
        # Inicialización: marcamos el nodo inicial como visitado
        self.nodos_visitados.add(nodo_inicio)
        self.mostrar_paso(nodo_inicio)
        if visualizar:
            self.actualizar_visualizacion(nodo_inicio)
        
        # Agregamos todas las aristas del nodo inicial a la cola de prioridad
        for vecino, peso in self.grafo[nodo_inicio].items():
            heapq.heappush(self.cola_prioridad, (peso, nodo_inicio, vecino))
        
        # Mientras haya aristas en la cola de prioridad
        while self.cola_prioridad:
            peso, nodo_a, nodo_b = heapq.heappop(self.cola_prioridad)
            
            # Si ambos nodos ya están visitados, ignoramos esta arista
            if nodo_b in self.nodos_visitados:
                continue
                
            # Agregamos la arista al árbol
            self.aristas_arbol.append((nodo_a, nodo_b, peso))
            self.peso_total += peso
            
            # Marcamos el nuevo nodo como visitado
            self.nodos_visitados.add(nodo_b)
            
            # Mostramos información del paso actual
            self.mostrar_paso(nodo_b, (nodo_a, nodo_b, peso))
            if visualizar:
                self.actualizar_visualizacion(nodo_b)
            
            # Agregamos las aristas del nuevo nodo a la cola de prioridad
            for vecino, peso in self.grafo[nodo_b].items():
                if vecino not in self.nodos_visitados:
                    heapq.heappush(self.cola_prioridad, (peso, nodo_b, vecino))
        
        # Mostramos resultados finales
        print("\n--- Resultados Finales ---")
        print("Aristas del Árbol de Expansión Mínima:")
        for arista in self.aristas_arbol:
            print(f"  {arista[0]} - {arista[1]} (peso: {arista[2]})")
        print(f"Peso total del árbol: {self.peso_total}")
        
        if visualizar:
            plt.ioff()
            plt.show()
    
    def preparar_visualizacion(self):
        """Prepara la visualización gráfica del grafo."""
        self.G = nx.Graph()  # Grafo no dirigido
        
        # Agregamos todos los nodos y aristas al grafo de visualización
        for nodo, vecinos in self.grafo.items():
            for vecino, peso in vecinos.items():
                self.G.add_edge(nodo, vecino, weight=peso)
        
        # Calculamos la posición de los nodos para el dibujo
        self.posiciones = nx.spring_layout(self.G)
        
        # Configuración para visualización interactiva
        plt.ion()
        self.figura, self.ejes = plt.subplots(figsize=(10, 8))
    
    def actualizar_visualizacion(self, nodo_actual=None):
        """Actualiza la visualización gráfica en cada paso."""
        plt.clf()  # Limpia la figura
        
        # Asignamos colores a los nodos según su estado
        colores_nodos = []
        for nodo in self.G.nodes():
            if nodo == nodo_actual:
                colores_nodos.append('red')  # Nodo actual (rojo)
            elif nodo in self.nodos_visitados:
                colores_nodos.append('green')  # Nodos visitados (verde)
            else:
                colores_nodos.append('skyblue')  # Nodos no visitados (azul claro)
        
        # Dibujamos todos los nodos
        nx.draw_networkx_nodes(self.G, self.posiciones, node_size=700, 
                              node_color=colores_nodos)
        
        # Dibujamos las etiquetas de los nodos
        nx.draw_networkx_labels(self.G, self.posiciones, font_size=12, 
                               font_family='sans-serif')
        
        # Dibujamos todas las aristas del grafo original (en gris claro)
        nx.draw_networkx_edges(self.G, self.posiciones, edgelist=self.G.edges(), 
                              width=1, edge_color='lightgray', alpha=0.5)
        
        # Dibujamos las aristas del árbol (en verde y más gruesas)
        aristas_arbol_grafico = [(a[0], a[1]) for a in self.aristas_arbol]
        nx.draw_networkx_edges(self.G, self.posiciones, edgelist=aristas_arbol_grafico, 
                              width=3, edge_color='green')
        
        # Mostramos los pesos de todas las aristas
        pesos_aristas = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, self.posiciones, 
                                    edge_labels=pesos_aristas)
        
        # Configuramos el título de la figura
        titulo = f"Algoritmo de Prim - Paso {self.contador_pasos}"
        if nodo_actual:
            titulo += f"\nNodo actual: {nodo_actual}"
        plt.title(titulo)
        
        plt.tight_layout()
        plt.draw()
        plt.pause(1.5)  # Pausa para visualización

def main():
    """Función principal que maneja la ejecución del simulador."""
    
    # Grafo de ejemplo no dirigido (puede ser modificado)
    grafo_ejemplo = {
        'A': {'B': 4, 'H': 8},
        'B': {'A': 4, 'H': 11, 'C': 8},
        'C': {'B': 8, 'I': 2, 'F': 4, 'D': 7},
        'D': {'C': 7, 'F': 14, 'E': 9},
        'E': {'D': 9, 'F': 10},
        'F': {'C': 4, 'D': 14, 'E': 10, 'G': 2},
        'G': {'F': 2, 'H': 1, 'I': 6},
        'H': {'A': 8, 'B': 11, 'I': 7, 'G': 1},
        'I': {'C': 2, 'H': 7, 'G': 6}
    }
    
    print("=== Simulador del Algoritmo de Prim para Árbol de Expansión Mínima ===")
    print("Grafo de ejemplo:")
    for nodo, vecinos in grafo_ejemplo.items():
        print(f"  {nodo}: {vecinos}")
    
    # Preguntar si desea visualización gráfica
    visualizar = input("\n¿Desea visualización gráfica? (s/n): ").lower() == 's'
    
    # Preguntar por nodo de inicio (opcional)
    nodo_inicio = input("Ingrese el nodo de inicio (deje vacío para elegir automáticamente): ").upper()
    if nodo_inicio and nodo_inicio not in grafo_ejemplo:
        print("Nodo inválido. Se elegirá uno automáticamente.")
        nodo_inicio = None
    
    # Crear y ejecutar el simulador
    simulador = SimuladorPrim(grafo_ejemplo)
    simulador.ejecutar(visualizar=visualizar, nodo_inicio=nodo_inicio if nodo_inicio else None)

if __name__ == "__main__":
    main()