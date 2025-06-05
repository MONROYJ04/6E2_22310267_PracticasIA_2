# =================================================================
# SHELL SORT (Ordenamiento de Shell)
# =================================================================
# ¿Para qué sirve?: 
# - Mejora de Insertion Sort para datasets medianos
# - Cuando se necesita un algoritmo in-place con mejor rendimiento que O(n²)

# Complejidad:
# - Depende de la secuencia de gaps
# - Mejor conocida: O(n log² n)

# Ventajas:
# - Más rápido que Insertion Sort
# - Ordena en el lugar

# Desventajas:
# - Complejidad difícil de analizar
# - No es estable

def shell_sort(arr):
    n = len(arr)
    gap = n//2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Array original:", data)
    sorted_data = shell_sort(data.copy())
    print("Array ordenado:", sorted_data)