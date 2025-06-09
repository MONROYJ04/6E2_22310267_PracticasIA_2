import matplotlib.pyplot as plt
import networkx as nx

class SimuladorKruskal:
    def __init__(self, grafo):
        """
        Inicializa el simulador del algoritmo de Kruskal.
        
        Args:
            grafo (dict): Diccionario que representa el grafo ponderado no dirigido
        """
        self.grafo = grafo
        self.nodos = list(grafo.keys())
        self.aristas = self._obtener_aristas()
        self.arbol = []
        self.conjuntos_disjuntos = {nodo: {nodo} for nodo in self.nodos}
        self.contador_pasos = 0
        self.peso_total = 0
        
    def _obtener_aristas(self):
        """
        Obtiene todas las aristas del grafo sin duplicados (para grafo no dirigido).
        
        Returns:
            list: Lista de tuplas (nodo1, nodo2, peso)
        """
        aristas = set()
        for nodo, vecinos in self.grafo.items():
            for vecino, peso in vecinos.items():
                if (vecino, nodo, peso) not in aristas:
                    aristas.add((nodo, vecino, peso))
        return sorted(aristas, key=lambda x: x[2])  # Ordena por peso
    
    def _encontrar_conjunto(self, nodo):
        """
        Encuentra el conjunto al que pertenece un nodo.
        
        Args:
            nodo (str): Nodo a buscar
            
        Returns:
            set: Conjunto que contiene al nodo
        """
        for conjunto in self.conjuntos_disjuntos.values():
            if nodo in conjunto:
                return conjunto
        return None
    
    def _unir_conjuntos(self, conjunto_a, conjunto_b):
        """
        Une dos conjuntos disjuntos.
        
        Args:
            conjunto_a (set): Primer conjunto
            conjunto_b (set): Segundo conjunto
        """
        # Encuentra los representantes de cada conjunto
        rep_a = next(iter(conjunto_a))
        rep_b = next(iter(conjunto_b))
        
        # Une los conjuntos bajo un mismo representante
        self.conjuntos_disjuntos[rep_a].update(self.conjuntos_disjuntos[rep_b])
        del self.conjuntos_disjuntos[rep_b]
    
    def mostrar_paso(self, arista_actual=None, agregada=False, razon=None):
        """
        Muestra en consola la información del paso actual del algoritmo.
        
        Args:
            arista_actual (tuple): Arista que se está procesando (nodo1, nodo2, peso)
            agregada (bool): Indica si la arista fue agregada al árbol
            razon (str): Razón por la que se agregó o no la arista
        """
        self.contador_pasos += 1
        print(f"\n--- Paso {self.contador_pasos} ---")
        
        if arista_actual:
            print(f"Procesando arista: {arista_actual[0]} - {arista_actual[1]} (peso: {arista_actual[2]})")
        
        if agregada:
            print("-> ARISTA AGREGADA al árbol")
            print(f"Razón: {razon}")
        elif arista_actual:
            print("-> Arista NO agregada")
            print(f"Razón: {razon}")
        
        print("Aristas del árbol actual:", self.arbol)
        print(f"Peso total acumulado: {self.peso_total}")
        print("Conjuntos disjuntos actuales:", self.conjuntos_disjuntos)
    
    def ejecutar(self, minimo=True, visualizar=False):
        """
        Ejecuta el algoritmo de Kruskal para árbol de expansión mínima o máxima.
        
        Args:
            minimo (bool): Si True, calcula árbol de expansión mínima; si False, máxima
            visualizar (bool): Si True, muestra visualización gráfica
        """
        tipo = "MÍNIMA" if minimo else "MÁXIMA"
        print(f"\n=== Algoritmo de Kruskal para Árbol de Expansión {tipo} ===")
        
        # Ordenamos las aristas por peso (ascendente para mínimo, descendente para máximo)
        aristas_ordenadas = sorted(self.aristas, key=lambda x: x[2], reverse=not minimo)
        
        if visualizar:
            self.preparar_visualizacion()
        
        # Mostramos estado inicial
        self.mostrar_paso()
        if visualizar:
            self.actualizar_visualizacion()
        
        # Procesamos cada arista en orden
        for arista in aristas_ordenadas:
            nodo_a, nodo_b, peso = arista
            conjunto_a = self._encontrar_conjunto(nodo_a)
            conjunto_b = self._encontrar_conjunto(nodo_b)
            
            # Si los nodos están en conjuntos diferentes, no forman ciclo
            if conjunto_a != conjunto_b:
                self.arbol.append(arista)
                self.peso_total += peso
                self._unir_conjuntos(conjunto_a, conjunto_b)
                self.mostrar_paso(arista, True, "No forma ciclo")
            else:
                self.mostrar_paso(arista, False, "Formaría ciclo")
            
            if visualizar:
                self.actualizar_visualizacion(arista, conjunto_a == conjunto_b)
            
            # Terminamos cuando todos los nodos están conectados
            if len(self.conjuntos_disjuntos) == 1:
                break
        
        # Mostramos resultados finales
        print("\n--- Resultados Finales ---")
        print(f"Aristas del Árbol de Expansión {tipo}:")
        for arista in self.arbol:
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
    
    def actualizar_visualizacion(self, arista_actual=None, forma_ciclo=False):
        """Actualiza la visualización gráfica en cada paso."""
        plt.clf()  # Limpia la figura
        
        # Dibujamos todos los nodos
        nx.draw_networkx_nodes(self.G, self.posiciones, node_size=700, node_color='skyblue')
        
        # Dibujamos las etiquetas de los nodos
        nx.draw_networkx_labels(self.G, self.posiciones, font_size=12, font_family='sans-serif')
        
        # Dibujamos todas las aristas del grafo original (en gris claro)
        todas_aristas = list(self.G.edges())
        nx.draw_networkx_edges(self.G, self.posiciones, edgelist=todas_aristas, 
                              width=1, edge_color='lightgray', alpha=0.5)
        
        # Resaltamos la arista actual
        if arista_actual:
            arista_actual_grafico = (arista_actual[0], arista_actual[1])
            color = 'red' if forma_ciclo else 'blue'
            nx.draw_networkx_edges(self.G, self.posiciones, edgelist=[arista_actual_grafico], 
                                  width=3, edge_color=color, alpha=0.7)
        
        # Dibujamos las aristas del árbol (en verde y más gruesas)
        aristas_arbol_grafico = [(a[0], a[1]) for a in self.arbol]
        nx.draw_networkx_edges(self.G, self.posiciones, edgelist=aristas_arbol_grafico, 
                              width=3, edge_color='green')
        
        # Mostramos los pesos de todas las aristas
        pesos_aristas = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, self.posiciones, edge_labels=pesos_aristas)
        
        # Mostramos los conjuntos disjuntos
        etiquetas_conjuntos = {}
        for nodo in self.G.nodes():
            conjunto = self._encontrar_conjunto(nodo)
            etiquetas_conjuntos[nodo] = f"{nodo}\nConj: {sorted(conjunto)}"
        
        pos_etiquetas = {k: (v[0], v[1]-0.05) for k, v in self.posiciones.items()}
        nx.draw_networkx_labels(self.G, pos_etiquetas, labels=etiquetas_conjuntos, 
                              font_size=8, font_color='darkred')
        
        # Configuramos el título de la figura
        titulo = f"Algoritmo de Kruskal - Paso {self.contador_pasos}"
        if arista_actual:
            titulo += f"\nArista actual: {arista_actual[0]}-{arista_actual[1]} (peso: {arista_actual[2]})"
            if forma_ciclo:
                titulo += "\nFORMA CICLO - NO agregada"
            else:
                titulo += "\nNO forma ciclo - AGREGADA"
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
    
    print("=== Simulador del Algoritmo de Kruskal ===")
    print("Grafo de ejemplo:")
    for nodo, vecinos in grafo_ejemplo.items():
        print(f"  {nodo}: {vecinos}")
    
    # Preguntar si desea visualización gráfica
    visualizar = input("\n¿Desea visualización gráfica? (s/n): ").lower() == 's'
    
    # Preguntar por tipo de árbol (mínimo o máximo)
    tipo = input("¿Calcular árbol de expansión mínima (m) o máxima (M)? ").lower()
    while tipo not in ['m', 'M']:
        print("Opción inválida. Intente nuevamente.")
        tipo = input("¿Calcular árbol de expansión mínima (m) o máxima (M)? ").lower()
    minimo = tipo == 'm'
    
    # Crear y ejecutar el simulador
    simulador = SimuladorKruskal(grafo_ejemplo)
    simulador.ejecutar(minimo=minimo, visualizar=visualizar)

if __name__ == "__main__":
    main()