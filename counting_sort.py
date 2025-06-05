# =================================================================
# COUNTING SORT (Ordenamiento por Conteo)
# =================================================================
# ¿Para qué sirve?: 
# - Cuando los elementos tienen un rango pequeño de valores enteros
# - Como subrutina de Radix Sort

# Complejidad: O(n + k) donde k es el rango de valores

# Ventajas:
# - Extremadamente rápido para su rango de aplicación
# - Estable

# Desventajas:
# - Solo funciona con valores enteros
# - Requiere memoria adicional O(k)

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
        
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr

# Ejemplo de uso
if __name__ == "__main__":
    data = [1, 4, 1, 2, 7, 5, 2]
    print("Array original:", data)
    sorted_data = counting_sort(data.copy())
    print("Array ordenado:", sorted_data)