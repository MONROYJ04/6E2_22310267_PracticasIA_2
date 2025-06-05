# =================================================================
# INSERTION SORT (Ordenamiento por Inserción)
# =================================================================
# ¿Para qué sirve?: 
# - Excelente para datasets pequeños o casi ordenados
# - Usado en algoritmos híbridos como TimSort

# Complejidad:
# - Peor caso: O(n²)
# - Mejor caso: O(n) (array ya ordenado)

# Ventajas:
# - Eficiente para datasets pequeños
# - Estable (no cambia el orden de elementos iguales)
# - Ordena en el lugar (poca memoria adicional)

# Desventajas:
# - Ineficiente para datasets grandes

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Array original:", data)
    sorted_data = insertion_sort(data.copy())
    print("Array ordenado:", sorted_data)