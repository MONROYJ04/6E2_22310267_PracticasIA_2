# =================================================================
# SELECTION SORT (Ordenamiento por Selección)
# =================================================================
# ¿Para qué sirve?: 
# - Útil cuando la memoria es limitada (hace menos escrituras que Bubble Sort)
# - Bueno para datasets pequeños

# Complejidad: O(n²) en todos los casos

# Ventajas:
# - Rendimiento consistente
# - Poco uso de memoria adicional

# Desventajas:
# - Lento en datasets grandes
# - No adaptativo (no aprovecha arrays parcialmente ordenados)

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambia el elemento mínimo con la primera posición no ordenada
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Array original:", data)
    sorted_data = selection_sort(data.copy())
    print("Array ordenado:", sorted_data)