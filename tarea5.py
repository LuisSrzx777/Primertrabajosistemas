def leer_estudiantes(archivo):
    """
    Lee el archivo de estudiantes y retorna una lista de tuplas (nombre, calificacion)
    """
    estudiantes = []
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            for numero_linea, linea in enumerate(file, 1):
                linea = linea.strip()
                if linea:  # Ignorar líneas vacías
                    try:
                        nombre, calificacion_str = linea.split(',')
                        calificacion = float(calificacion_str)
                        estudiantes.append((nombre, calificacion))
                    except ValueError:
                        print(f"Error en línea {numero_linea}: Formato incorrecto - '{linea}'")
                        print("El formato debe ser: Nombre,Calificacion")
        return estudiantes
    
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no existe.")
        return []
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        return []

def calcular_promedio(estudiantes):
    """
    Calcula el promedio de calificaciones
    """
    if not estudiantes:
        return 0.0
    
    total = sum(calificacion for _, calificacion in estudiantes)
    return total / len(estudiantes)

def generar_reporte(archivo_entrada, archivo_salida):
    """
    Genera un archivo de reporte con los estudiantes y el promedio
    """
    estudiantes = leer_estudiantes(archivo_entrada)
    
    if not estudiantes:
        print("No hay datos para generar el reporte.")
        return False
    
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as file:
            # Escribir los estudiantes
            for nombre, calificacion in estudiantes:
                file.write(f"{nombre},{calificacion}\n")
            
            # Escribir el promedio
            promedio = calcular_promedio(estudiantes)
            file.write(f"\nPromedio general: {promedio:.1f}")
        
        print(f"✅ Reporte generado exitosamente en '{archivo_salida}'")
        print(f"📊 Promedio calculado: {promedio:.1f}")
        return True
    
    except Exception as e:
        print(f"Error al generar el reporte: {e}")
        return False

def agregar_estudiante(archivo):
    """
    Permite al usuario agregar un nuevo estudiante al archivo
    """
    print("\n--- AGREGAR NUEVO ESTUDIANTE ---")
    
    # Validar nombre
    while True:
        nombre = input("Nombre del estudiante: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            continue
        if ',' in nombre:
            print("El nombre no puede contener comas.")
            continue
        break
    
    # Validar calificación
    while True:
        try:
            calificacion = float(input("Calificación (0-100): "))
            if calificacion < 0 or calificacion > 100:
                print("La calificación debe estar entre 0 y 100.")
                continue
            break
        except ValueError:
            print("Error: Ingrese un número válido.")
    
    try:
        # Abrir el archivo en modo append (agregar al final)
        with open(archivo, 'a', encoding='utf-8') as file:
            file.write(f"{nombre},{calificacion}\n")
        
        print(f"✅ Estudiante '{nombre}' agregado exitosamente!")
        return True
    
    except Exception as e:
        print(f"Error al agregar estudiante: {e}")
        return False

def mostrar_estudiantes(archivo):
    """
    Muestra los estudiantes actuales en el archivo
    """
    estudiantes = leer_estudiantes(archivo)
    
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    print("\n--- LISTA DE ESTUDIANTES ---")
    print(f"{'Nombre':<15} {'Calificación':<12}")
    print("-" * 30)
    
    for nombre, calificacion in estudiantes:
        print(f"{nombre:<15} {calificacion:<12}")
    
    promedio = calcular_promedio(estudiantes)
    print("-" * 30)
    print(f"{'PROMEDIO':<15} {promedio:<12.1f}")

def crear_archivo_ejemplo():
    """
    Crea un archivo de ejemplo si no existe
    """
    contenido_ejemplo = """Ana,90
Jorge,75
Laura,85
Maria,95
Carlos,68"""
    
    try:
        with open('estudiantes.txt', 'w', encoding='utf-8') as file:
            file.write(contenido_ejemplo)
        print("✅ Archivo 'estudiantes.txt' creado con datos de ejemplo.")
    except Exception as e:
        print(f"Error al crear archivo de ejemplo: {e}")

def main():
    """
    Función principal del programa
    """
    archivo_estudiantes = 'estudiantes.txt'
    archivo_reporte = 'reporte.txt'
    
    print("=" * 50)
    print("       📚 GESTOR DE CALIFICACIONES")
    print("=" * 50)
    
    # Verificar si el archivo existe, sino crear uno de ejemplo
    try:
        with open(archivo_estudiantes, 'r', encoding='utf-8'):
            pass
    except FileNotFoundError:
        print("El archivo 'estudiantes.txt' no existe.")
        crear = input("¿Desea crear un archivo con datos de ejemplo? (s/n): ").lower()
        if crear == 's':
            crear_archivo_ejemplo()
        else:
            print("Saliendo del programa...")
            return
    
    while True:
        print("\n" + "=" * 50)
        print("           MENÚ PRINCIPAL")
        print("=" * 50)
        print("1. 📋 Mostrar estudiantes actuales")
        print("2. 📊 Generar reporte de calificaciones")
        print("3. ➕ Agregar nuevo estudiante")
        print("4. 📖 Ver reporte generado")
        print("5. 🚪 Salir")
        print("=" * 50)
        
        try:
            opcion = input("Seleccione una opción (1-5): ").strip()
            
            if opcion == "1":
                mostrar_estudiantes(archivo_estudiantes)
                
            elif opcion == "2":
                if generar_reporte(archivo_estudiantes, archivo_reporte):
                    print("✅ Reporte generado exitosamente!")
                
            elif opcion == "3":
                if agregar_estudiante(archivo_estudiantes):
                    print("✅ Estudiante agregado correctamente!")
                
            elif opcion == "4":
                try:
                    with open(archivo_reporte, 'r', encoding='utf-8') as file:
                        contenido = file.read()
                    print("\n--- CONTENIDO DEL REPORTE ---")
                    print(contenido)
                except FileNotFoundError:
                    print("❌ El reporte no existe. Genere primero un reporte.")
                except Exception as e:
                    print(f"Error al leer el reporte: {e}")
                    
            elif opcion == "5":
                print("👋 ¡Hasta pronto!")
                break
                
            else:
                print("❌ Opción no válida. Por favor, seleccione 1-5.")
                
        except ValueError:
            print("❌ Error: Ingrese un número válido.")
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        # Pausa antes de continuar
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()