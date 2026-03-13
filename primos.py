def es_primo(numero):

    """Función que determina si un número es primo"""
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def main():
    try:
        # Leer los números de entrada
        print("PROBLEMA 1033 - CONTANDO PRIMOS")
        print("-" * 40)
        
        a = int(input("Ingrese el primer número (a): "))
        b = int(input("Ingrese el segundo número (b): "))
        
        # Asegurar que a sea menor que b
        if a > b:
            a, b = b, a
            print(f"\n(Se intercambiaron los valores: ahora a={a}, b={b})")
        
        print(f"\nBuscando números primos entre {a} y {b}:")
        print("-" * 40)
        
        # Contar y mostrar los números primos
        contador = 0
        primos_encontrados = []
        
        for num in range(a, b + 1):
            if es_primo(num):
                contador += 1
                primos_encontrados.append(num)
        
        # Mostrar resultados
        if primos_encontrados:
            print(f"Números primos encontrados: {primos_encontrados}")
        else:
            print("No se encontraron números primos en este rango.")
        
        print(f"\n✨ RESULTADO: {contador} números primos")
        
    except ValueError:
        print("❌ Error: Por favor ingrese solo números enteros válidos")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

# Versión para el juez (solo imprime el resultado)
def version_juez():
    """Versión simplificada para el juez en línea"""
    import sys
    datos = sys.stdin.read().strip().split()
    if len(datos) >= 2:
        a = int(datos[0])
        b = int(datos[1])
        
        if a > b:
            a, b = b, a
            
        contador = 0
        for num in range(a, b + 1):
            if num >= 2:
                primo = True
                for i in range(2, int(num**0.5) + 1):
                    if num % i == 0:
                        primo = False
                        break
                if primo:
                    contador += 1
        print(contador)

if __name__ == "__main__":
    # Para probar localmente usa main()
    # Para el juez, usa version_juez()
    
    # Descomenta la línea que necesites:
    main()  # Versión con mensajes (para probar)
    # version_juez()  # Versión para el juez (solo imprime el número)
