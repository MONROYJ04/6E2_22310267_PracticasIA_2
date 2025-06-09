# Importación de bibliotecas necesarias
import heapq  # Para la cola de prioridad
import sys    # Para valores infinitos
import matplotlib.pyplot as plt  # Para visualización gráfica
import networkx as nx  # Para manejo y dibujo de grafos

class SimuladorDijkstra:
    def __init__(self, grafo, nodo_inicial):
        """
        Inicializa el simulador del algoritmo de Dijkstra.
        
        Args:
            grafo (dict): Diccionario que representa el grafo ponderado
            nodo_inicial (str): Nodo desde donde comenzará el algoritmo
        """
        self.grafo = grafo  # El grafo a analizar
        self.nodo_inicial = nodo_inicial  # Nodo de inicio
        
        # Inicializa las distancias con infinito para todos los nodos
        self.distancias = {nodo: float('infinity') for nodo in grafo}
        self.distancias[nodo_inicial] = 0  # La distancia al nodo inicial es 0
        
        # Diccionario para guardar el nodo previo en el camino más corto
        self.nodos_previos = {nodo: None for nodo in grafo}
        
        self.nodos_visitados = set()  # Conjunto de nodos ya visitados
        self.cola_prioridad = [(0, nodo_inicial)]  # Cola de prioridad inicializada
        self.contador_pasos = 0  # Contador para numerar los pasos
        
    def mostrar_paso(self, nodo_actual):
        """
        Muestra en consola la información del paso actual del algoritmo.
        
        Args:
            nodo_actual (str): Nodo que se está procesando en este paso
        """
        self.contador_pasos += 1
        print(f"\n--- Paso {self.contador_pasos} ---")
        print(f"Nodo actual: {nodo_actual}")
        
        # Mostrar distancias conocidas hasta el momento
        print("Distancias conocidas:")
        for nodo, distancia in self.distancias.items():
            estado = "(Visitado)" if nodo in self.nodos_visitados else ""
            print(f"  {nodo}: {distancia} {estado}")
        
        # Mostrar estado actual de la cola de prioridad
        print("Cola de prioridad:", self.cola_prioridad)
    
    def ejecutar(self, visualizar=False):
        """
        Ejecuta el algoritmo de Dijkstra.
        
        Args:
            visualizar (bool): Si es True, muestra visualización gráfica
        """
        if visualizar:
            self.preparar_visualizacion()
        
        # Mientras haya nodos por procesar en la cola de prioridad
        while self.cola_prioridad:
            # Extrae el nodo con la menor distancia actual
            distancia_actual, nodo_actual = heapq.heappop(self.cola_prioridad)
            
            # Si ya fue visitado, lo saltamos
            if nodo_actual in self.nodos_visitados:
                continue
                
            # Mostrar información del paso actual
            self.mostrar_paso(nodo_actual)
            if visualizar:
                self.actualizar_visualizacion(nodo_actual)
                
            # Para cada vecino del nodo actual
            for vecino, peso in self.grafo[nodo_actual].items():
                # Si el vecino ya fue visitado, lo saltamos
                if vecino in self.nodos_visitados:
                    continue
                    
                # Calcula la distancia tentativa al vecino
                distancia_tentativa = distancia_actual + peso
                
                # Si encontramos un camino más corto
                if distancia_tentativa < self.distancias[vecino]:
                    self.distancias[vecino] = distancia_tentativa
                    self.nodos_previos[vecino] = nodo_actual
                    # Agrega a la cola de prioridad
                    heapq.heappush(self.cola_prioridad, (distancia_tentativa, vecino))
            
            # Marca el nodo actual como visitado
            self.nodos_visitados.add(nodo_actual)
        
        # Mostrar resultados finales
        print("\n--- Resultados Finales ---")
        for nodo in self.grafo:
            ruta = self.obtener_ruta(nodo)
            print(f"Ruta más corta a {nodo}: {ruta} (Distancia: {self.distancias[nodo]})")
    
    def obtener_ruta(self, nodo):
        """
        Reconstruye la ruta más corta desde el nodo inicial hasta el nodo dado.
        
        Args:
            nodo (str): Nodo destino
            
        Returns:
            list: Lista de nodos que forman la ruta más corta
        """
        ruta = []
        while nodo is not None:
            ruta.insert(0, nodo)  # Inserta al principio para mantener el orden
            nodo = self.nodos_previos.get(nodo, None)
        
        # Si no hay ruta válida (nodo no alcanzable)
        return ruta if ruta[0] == self.nodo_inicial else ["No alcanzable"]
    
    def preparar_visualizacion(self):
        """Prepara la visualización gráfica del grafo."""
        self.G = nx.DiGraph()  # Crea un grafo dirigido
        
        # Agrega nodos y aristas al grafo de visualización
        for nodo, vecinos in self.grafo.items():
            for vecino, peso in vecinos.items():
                self.G.add_edge(nodo, vecino, weight=peso)
        
        # Calcula la posición de los nodos para el dibujo
        self.posiciones = nx.spring_layout(self.G)
        
        # Configuración para visualización interactiva
        plt.ion()
        self.figura, self.ejes = plt.subplots(figsize=(10, 8))
    
    def actualizar_visualizacion(self, nodo_actual):
        """Actualiza la visualización gráfica en cada paso."""
        plt.clf()  # Limpia la figura
        
        # Asigna colores a los nodos según su estado
        colores_nodos = []
        for nodo in self.G.nodes():
            if nodo == nodo_actual:
                colores_nodos.append('red')  # Nodo actual (rojo)
            elif nodo in self.nodos_visitados:
                colores_nodos.append('green')  # Nodos visitados (verde)
            else:
                colores_nodos.append('skyblue')  # Nodos no visitados (azul claro)
        
        # Dibuja los nodos
        nx.draw_networkx_nodes(self.G, self.posiciones, node_size=700, 
                              node_color=colores_nodos)
        
        # Dibuja las etiquetas de los nodos
        nx.draw_networkx_labels(self.G, self.posiciones, font_size=12, 
                               font_family='sans-serif')
        
        # Obtiene y dibuja los pesos de las aristas
        pesos_aristas = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edges(self.G, self.posiciones, edgelist=self.G.edges(), 
                              width=2)
        nx.draw_networkx_edge_labels(self.G, self.posiciones, 
                                    edge_labels=pesos_aristas)
        
        # Crea etiquetas con las distancias conocidas
        etiquetas_distancias = {nodo: f"{nodo}\nDist: {self.distancias[nodo]}" 
                              for nodo in self.G.nodes()}
        
        # Ajusta la posición de las etiquetas para que no se solapen
        pos_etiquetas = {k: (v[0], v[1]+0.05) for k, v in self.posiciones.items()}
        nx.draw_networkx_labels(self.G, pos_etiquetas, labels=etiquetas_distancias, 
                              font_size=10, font_color='darkred')
        
        # Configura el título de la figura
        plt.title(f"Algoritmo de Dijkstra - Paso {self.contador_pasos}\nNodo actual: {nodo_actual}")
        plt.tight_layout()
        plt.draw()
        plt.pause(1.5)  # Pausa para visualización

def main():
    """Función principal que maneja la ejecución del simulador."""
    
    # Grafo de ejemplo (puede ser modificado)
    grafo_ejemplo = {
        'A': {'B': 6, 'D': 1},
        'B': {'A': 6, 'D': 2, 'E': 2, 'C': 5},
        'C': {'B': 5, 'E': 5},
        'D': {'A': 1, 'B': 2, 'E': 1},
        'E': {'D': 1, 'B': 2, 'C': 5}
    }
    
    print("=== Simulador del Algoritmo de Dijkstra ===")
    print("Grafo de ejemplo:")
    for nodo, vecinos in grafo_ejemplo.items():
        print(f"  {nodo}: {vecinos}")
    
    # Solicitar nodo de inicio al usuario
    nodo_inicio = input("\nIngrese el nodo de inicio (A-E): ").upper()
    while nodo_inicio not in grafo_ejemplo:
        print("Nodo inválido. Intente nuevamente.")
        nodo_inicio = input("Ingrese el nodo de inicio (A-E): ").upper()
    
    # Preguntar si desea visualización gráfica
    visualizar = input("¿Desea visualización gráfica? (s/n): ").lower() == 's'
    
    # Crear y ejecutar el simulador
    simulador = SimuladorDijkstra(grafo_ejemplo, nodo_inicio)
    simulador.ejecutar(visualizar)
    
    # Mantener la visualización abierta al finalizar
    if visualizar:
        plt.ioff()
        plt.show()

if __name__ == "__main__":
    main()