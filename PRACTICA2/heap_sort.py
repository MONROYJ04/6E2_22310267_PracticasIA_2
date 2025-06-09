# =================================================================
# HEAP SORT (Ordenamiento por Montículos)
# =================================================================
# ¿Para qué sirve?: 
# - Cuando se necesita O(1) en memoria adicional
# - Sistemas embebidos con recursos limitados

# Complejidad: O(n log n) en todos los casos

# Ventajas:
# - Ordena en el lugar
# - Rendimiento consistente

# Desventajas:
# - No es estable
# - Más lento en la práctica que Quick Sort

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and arr[i] < arr[l]:
        largest = l
        
    if r < n and arr[largest] < arr[r]:
        largest = r
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Array original:", data)
    sorted_data = heap_sort(data.copy())
    print("Array ordenado:", sorted_data)