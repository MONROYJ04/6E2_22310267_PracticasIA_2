# =================================================================
# BUCKET SORT (Ordenamiento por Cubetas)
# =================================================================
# ¿Para qué sirve?: 
# - Cuando los datos están uniformemente distribuidos
# - Como paso intermedio en otros algoritmos

# Complejidad:
# - Promedio: O(n + k)
# - Peor caso: O(n²)

# Ventajas:
# - Muy rápido cuando los datos están uniformemente distribuidos
# - Puede ser estable dependiendo de la implementación

# Desventajas:
# - No funciona bien con datos no uniformes
# - Requiere conocimiento previo de la distribución de los datos

def bucket_sort(arr):
    max_val = max(arr)
    size = max_val / len(arr)
    buckets = [[] for _ in range(len(arr))]
    
    for num in arr:
        idx = int(num / size)
        if idx != len(arr):
            buckets[idx].append(num)
        else:
            buckets[len(arr) - 1].append(num)
            
    for i in range(len(arr)):
        buckets[i] = sorted(buckets[i])
        
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    return sorted_arr

# Ejemplo de uso
if __name__ == "__main__":
    data = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    print("Array original:", data)
    sorted_data = bucket_sort(data.copy())
    print("Array ordenado:", sorted_data)