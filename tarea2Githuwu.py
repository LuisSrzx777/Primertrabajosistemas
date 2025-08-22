import numpy as np

def ingresar_matriz(nombre):
    """Función para ingresar una matriz desde la consola"""
    print(f"\n--- Ingresar matriz {nombre} ---")
    
    while True:
        try:
            filas = int(input("Número de filas: "))
            columnas = int(input("Número de columnas: "))
            
            if filas <= 0 or columnas <= 0:
                print("Las dimensiones deben ser números positivos.")
                continue
                
            print(f"Ingrese los elementos de la matriz {filas}x{columnas} (fila por fila):")
            print("Ejemplo para 2x2: '1 2' ENTER '3 4'")
            
            matriz = []
            for i in range(filas):
                while True:
                    fila_input = input(f"Fila {i+1}: ").strip()
                    elementos = fila_input.split()
                    
                    if len(elementos) != columnas:
                        print(f"Error: debe ingresar exactamente {columnas} elementos por fila")
                        continue
                    
                    try:
                        fila = [float(x) for x in elementos]
                        matriz.append(fila)
                        break
                    except ValueError:
                        print("Error: todos los elementos deben ser números")
            
            return np.array(matriz)
            
        except ValueError:
            print("Error: ingrese números válidos para las dimensiones")

def mostrar_matriz(matriz, nombre):
    """Función para mostrar una matriz de forma legible"""
    print(f"\nMatriz {nombre}:")
    print(matriz)

def main():
    print("=== CALCULADORA MATRICIAL CON NUMPY ===")
    print("Operaciones disponibles:")
    print("1. Suma de matrices (A + B)")
    print("2. Resta de matrices (A - B)")
    print("3. Multiplicación de matrices (A × B)")
    print("4. Transposición de matriz (Aᵀ)")
    print("5. Salir")
    
    while True:
        try:
            opcion = int(input("\nSeleccione una operación (1-5): "))
            
            if opcion == 5:
                print("¡Hasta luego!")
                break
                
            if opcion == 4:  # Transposición (solo necesita una matriz)
                matriz_A = ingresar_matriz("A")
                mostrar_matriz(matriz_A, "A")
                
                resultado = matriz_A.T
                print("\n--- RESULTADO ---")
                print("Transposición de A (Aᵀ):")
                print(resultado)
                
            elif 1 <= opcion <= 3:  # Operaciones que necesitan dos matrices
                matriz_A = ingresar_matriz("A")
                matriz_B = ingresar_matriz("B")
                
                mostrar_matriz(matriz_A, "A")
                mostrar_matriz(matriz_B, "B")
                
                try:
                    if opcion == 1:  # Suma
                        if matriz_A.shape != matriz_B.shape:
                            print("Error: Las matrices deben tener las mismas dimensiones para la suma")
                            continue
                        resultado = np.add(matriz_A, matriz_B)
                        print("\n--- RESULTADO ---")
                        print("A + B =")
                        print(resultado)
                        
                    elif opcion == 2:  # Resta
                        if matriz_A.shape != matriz_B.shape:
                            print("Error: Las matrices deben tener las mismas dimensiones para la resta")
                            continue
                        resultado = np.subtract(matriz_A, matriz_B)
                        print("\n--- RESULTADO ---")
                        print("A - B =")
                        print(resultado)
                        
                    elif opcion == 3:  # Multiplicación
                        if matriz_A.shape[1] != matriz_B.shape[0]:
                            print("Error: El número de columnas de A debe ser igual al número de filas de B")
                            continue
                        resultado = np.matmul(matriz_A, matriz_B)
                        print("\n--- RESULTADO ---")
                        print("A × B =")
                        print(resultado)
                        
                except Exception as e:
                    print(f"Error durante la operación: {e}")
                    
            else:
                print("Opción no válida. Por favor, seleccione 1-5.")
                
        except ValueError:
            print("Error: Ingrese un número válido (1-5)")
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
  
    try:
        import numpy
        main()
    except ImportError:
        print("Error: NumPy no está instalado.")
        print("Instálelo con: pip install numpy")