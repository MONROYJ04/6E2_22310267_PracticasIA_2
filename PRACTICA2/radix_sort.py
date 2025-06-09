# =================================================================
# RADIX SORT (Ordenamiento por Raíz)
# =================================================================
# ¿Para qué sirve?: 
# - Para ordenar números grandes con muchos dígitos
# - Cuando Counting Sort no es suficiente por el rango de valores

# Complejidad: O(d(n + k)) donde d es el número de dígitos

# Ventajas:
# - Más rápido que algoritmos comparativos para números grandes
# - Estable

# Desventajas:
# - Solo funciona con números enteros
# - Requiere memoria adicional

def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
        
    for i in range(1, 10):
        count[i] += count[i-1]
        
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
        
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    data = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Array original:", data)
    sorted_data = radix_sort(data.copy())
    print("Array ordenado:", sorted_data)