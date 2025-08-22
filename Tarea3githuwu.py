def agregar_estudiante(estudiantes):
    """Función para agregar un nuevo estudiante"""
    print("\n--- AGREGAR NUEVO ESTUDIANTE ---")
    
    # Validar ID único
    while True:
        id_estudiante = input("ID del estudiante (ej: A001): ").strip().upper()
        if not id_estudiante:
            print("El ID no puede estar vacío.")
            continue
        if id_estudiante in estudiantes:
            print("Error: Este ID ya existe. Use otro ID.")
            continue
        break
    
    # Validar nombre
    while True:
        nombre = input("Nombre completo: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            continue
        break
    
    # Validar edad
    while True:
        try:
            edad = int(input("Edad: "))
            if edad <= 0:
                print("La edad debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Error: Ingrese un número válido para la edad.")
    
    # Validar calificaciones
    calificaciones = []
    print("Ingrese las calificaciones (ingrese 'fin' para terminar):")
    while True:
        calificacion_input = input("Calificación (0-100): ").strip()
        if calificacion_input.lower() == 'fin':
            if len(calificaciones) == 0:
                print("Debe ingresar al menos una calificación.")
                continue
            break
        
        try:
            calificacion = float(calificacion_input)
            if calificacion < 0 or calificacion > 100:
                print("La calificación debe estar entre 0 y 100.")
                continue
            calificaciones.append(calificacion)
        except ValueError:
            print("Error: Ingrese un número válido o 'fin' para terminar.")
    
    # Agregar estudiante al diccionario
    estudiantes[id_estudiante] = {
        "nombre": nombre,
        "edad": edad,
        "calificaciones": calificaciones
    }
    
    print(f"✅ Estudiante {id_estudiante} agregado exitosamente!")

def mostrar_estudiantes(estudiantes):
    """Función para mostrar todos los estudiantes"""
    print("\n--- LISTA DE ESTUDIANTES ---")
    
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    for id_estudiante, datos in estudiantes.items():
        promedio = calcular_promedio(datos["calificaciones"])
        print(f"Estudiante {id_estudiante} - {datos['nombre']} - Edad: {datos['edad']} - Promedio: {promedio:.1f}")
        print(f"   Calificaciones: {', '.join(map(str, datos['calificaciones']))}")

def calcular_promedio_estudiante(estudiantes):
    """Función para calcular el promedio de un estudiante específico"""
    print("\n--- CALCULAR PROMEDIO DE ESTUDIANTE ---")
    
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    id_estudiante = input("Ingrese el ID del estudiante: ").strip().upper()
    
    if id_estudiante not in estudiantes:
        print("Error: ID de estudiante no encontrado.")
        return
    
    estudiante = estudiantes[id_estudiante]
    promedio = calcular_promedio(estudiante["calificaciones"])
    
    print(f"\nEstudiante {id_estudiante} - {estudiante['nombre']}")
    print(f"Calificaciones: {', '.join(map(str, estudiante['calificaciones']))}")
    print(f"Promedio: {promedio:.1f}")

def calcular_promedio(calificaciones):
    """Función auxiliar para calcular el promedio de una lista de calificaciones"""
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)

def eliminar_estudiante(estudiantes):
    """Función para eliminar un estudiante"""
    print("\n--- ELIMINAR ESTUDIANTE ---")
    
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    id_estudiante = input("Ingrese el ID del estudiante a eliminar: ").strip().upper()
    
    if id_estudiante not in estudiantes:
        print("Error: ID de estudiante no encontrado.")
        return
    
    # Confirmar eliminación
    estudiante = estudiantes[id_estudiante]
    confirmacion = input(f"¿Está seguro de eliminar a {estudiante['nombre']} (ID: {id_estudiante})? (s/n): ").strip().lower()
    
    if confirmacion == 's':
        del estudiantes[id_estudiante]
        print(f"✅ Estudiante {id_estudiante} eliminado exitosamente!")
    else:
        print("❌ Eliminación cancelada.")

def mostrar_menu():
    """Función para mostrar el menú principal"""
    print("\n" + "="*50)
    print("        GESTOR DE ESTUDIANTES")
    print("="*50)
    print("1. Agregar nuevo estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Calcular promedio de un estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")
    print("="*50)

def main():
    """Función principal del programa"""
    # Diccionario principal para almacenar los estudiantes
    estudiantes = {
        "A001": {"nombre": "Ana Torres", "edad": 20, "calificaciones": [90, 85, 78]},
        "A002": {"nombre": "Luis Pérez", "edad": 22, "calificaciones": [88, 91, 79]}
    }
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSeleccione una opción (1-5): ").strip()
            
            if opcion == "1":
                agregar_estudiante(estudiantes)
            elif opcion == "2":
                mostrar_estudiantes(estudiantes)
            elif opcion == "3":
                calcular_promedio_estudiante(estudiantes)
            elif opcion == "4":
                eliminar_estudiante(estudiantes)
            elif opcion == "5":
                print("¡Gracias por usar el Gestor de Estudiantes! 👋")
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

if __name__ == "__main__":
    main()