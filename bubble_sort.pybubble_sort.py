# =================================================================
# BUBBLE SORT (Ordenamiento de Burbuja)
# =================================================================
# ¿Para qué sirve?: 
# - Ideal para enseñar conceptos básicos de ordenamiento
# - Útil para datasets pequeños o casi ordenados

# Complejidad:
# - Peor caso: O(n²)   (cuando está en orden inverso)
# - Mejor caso: O(n)    (cuando ya está ordenado)
# - Promedio: O(n²)

# Ventajas:
# - Simple de implementar
# - Fácil de entender

# Desventajas: 
# - Muy lento para datasets grandes
# - Ineficiente en la mayoría de casos prácticos

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Intercambia elementos si están en el orden incorrecto
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Si no hubo intercambios, el array ya está ordenado
        if not swapped:
            break
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Array original:", data)
    sorted_data = bubble_sort(data.copy())
    print("Array ordenado:", sorted_data)