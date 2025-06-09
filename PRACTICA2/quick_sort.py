# =================================================================
# QUICK SORT (Ordenamiento Rápido)
# =================================================================
# ¿Para qué sirve?: 
# - Algoritmo general más rápido en la práctica
# - Usado en implementaciones de lenguajes (como sort() de Python)

# Complejidad:
# - Promedio: O(n log n)
# - Peor caso: O(n²) (raro con buenos pivotes)

# Ventajas:
# - Más rápido en la práctica que Merge Sort
# - Ordena en el lugar (poca memoria adicional)

# Desventajas:
# - No es estable
# - Peor caso depende de la selección del pivote

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Ejemplo de uso
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Array original:", data)
    sorted_data = quick_sort(data.copy())
    print("Array ordenado:", sorted_data)