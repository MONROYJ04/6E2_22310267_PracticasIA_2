# =================================================================
# GNOME SORT (Ordenamiento Gnomo)
# =================================================================
# ¿Para qué sirve?: 
# - Principalmente didáctico
# - Similar a Insertion Sort pero con diferente enfoque

# Complejidad: O(n²)

# Ventajas:
# - Implementación extremadamente simple
# - No usa estructuras adicionales

# Desventajas:
# - Muy ineficiente para datasets grandes
# - Principalmente de interés académico

def gnome_sort(arr):
    index = 0
    n = len(arr)
    
    while index < n:
        if index == 0:
            index += 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Array original:", data)
    sorted_data = gnome_sort(data.copy())
    print("Array ordenado:", sorted_data)