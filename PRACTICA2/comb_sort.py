# =================================================================
# COMB SORT (Ordenamiento por Peine)
# =================================================================
# ¿Para qué sirve?: 
# - Mejora de Bubble Sort para datasets medianos
# - Cuando se quiere un algoritmo simple pero más eficiente que Bubble Sort

# Complejidad:
# - Promedio: O(n²) pero más rápido que Bubble Sort en la práctica
# - Mejor caso: O(n log n)

# Ventajas:
# - Simple implementación
# - Más rápido que Bubble Sort

# Desventajas:
# - Todavía O(n²) en promedio
# - No es estable

def comb_sort(arr):
    n = len(arr)
    gap = n
    swapped = True
    
    while gap != 1 or swapped:
        gap = max(1, int(gap / 1.3))  # Factor de reducción
        swapped = False
        
        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Array original:", data)
    sorted_data = comb_sort(data.copy())
    print("Array ordenado:", sorted_data)