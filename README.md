# Control de Servicios XAMPP
### Desarrollado por DevMobyEnd (Jhonny Torres)

## 📋 Tabla de Contenidos
- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Código](#estructura-del-código)
- [Guía Técnica](#guía-técnica)
- [Personalización](#personalización)
- [Solución de Problemas](#solución-de-problemas)
- [Contribuir](#contribuir)

## 📝 Descripción
Este script de Python fue desarrollado para automatizar la gestión de servicios XAMPP en sistemas Linux, proporcionando una interfaz de usuario amigable y colorida en la terminal. El proyecto surge de la necesidad de simplificar las tareas repetitivas de inicio/detención de servicios durante el desarrollo web local.

## ✨ Características
- Control automatizado de servicios Apache y ProFTPD
- Selección flexible de MySQL (XAMPP/Sistema)
- Interfaz de terminal decorada con colores
- Manejo robusto de errores
- Verificación automática de privilegios
- Documentación detallada

## 🔧 Requisitos
- Python 3.6 o superior
- XAMPP instalado en el sistema
- Privilegios de superusuario (sudo)
- Biblioteca colorama (se instala automáticamente)

## 📥 Instalación
1. Clone o descargue el script:
```bash
git clone https://tu-repositorio/xampp-control.git
cd xampp-control
```

2. Otorgue permisos de ejecución:
```bash
chmod +x xampp_control.py
```

## 🚀 Uso
1. Ejecute el script con privilegios de superusuario:
```bash
sudo python3 xampp_control.py
```

2. Siga las instrucciones en pantalla para:
   - Ver el estado actual de los servicios
   - Activar/desactivar servicios
   - Seleccionar la versión de MySQL

## 🔍 Estructura del Código
El código está organizado en dos clases principales:

### TerminalStyle
Maneja la decoración y estilos de la terminal:
- `header()`: Formato para encabezados
- `success()`: Mensajes de éxito
- `error()`: Mensajes de error
- `info()`: Mensajes informativos
- `prompt()`: Prompts de usuario

### XAMPPController
Gestiona la lógica principal:
- `__init__()`: Inicialización y configuración
- `check_root()`: Verificación de privilegios
- `service_is_running()`: Comprobación de estado de servicios
- `execute_command()`: Ejecución segura de comandos
- `select_mysql_type()`: Selección de MySQL
- `toggle_services()`: Control principal de servicios

## 📚 Guía Técnica

### Bibliotecas Utilizadas
1. **os**: 
   - Propósito: Operaciones del sistema operativo
   - Uso principal: Verificación de privilegios (geteuid)

2. **subprocess**: 
   - Propósito: Ejecución de comandos del sistema
   - Uso principal: Control de servicios XAMPP

3. **colorama**: 
   - Propósito: Colorear la salida de terminal
   - Componentes usados: Fore, Back, Style
   - Instalación automática si no está presente

### Patrones de Diseño
1. **Singleton**: 
   - Implementado en XAMPPController
   - Garantiza una única instancia de control

2. **Command Pattern**: 
   - Usado en execute_command()
   - Encapsula comandos del sistema

### Manejo de Errores
- Verificación de privilegios root
- Captura de excepciones en comandos del sistema
- Manejo de interrupciones de usuario (Ctrl+C)
- Validación de entrada de usuario

## 🎨 Personalización

### Modificar Rutas
```python
self.xampp_path = "/opt/lampp"  # Cambie según su instalación
```

### Cambiar Colores
```python
# En la clase TerminalStyle
Fore.CYAN    # Encabezados
Fore.GREEN   # Éxito
Fore.RED     # Error
Fore.YELLOW  # Info
Fore.MAGENTA # Prompts
```

### Agregar Nuevos Servicios
1. Añada el archivo PID en self.pid_files
2. Cree los métodos correspondientes en XAMPPController
3. Actualice toggle_services()

## 🔧 Solución de Problemas

### Errores Comunes
1. **"Necesita privilegios de root"**
   - Solución: Ejecute con sudo

2. **"Comando no encontrado"**
   - Verifique la instalación de XAMPP
   - Confirme la ruta en xampp_path

3. **"Error al iniciar MySQL"**
   - Verifique que no haya conflictos de puertos
   - Asegure que el servicio no esté ya en ejecución

## 🤝 Contribuir
1. Fork el repositorio
2. Cree una rama para su característica
3. Commit sus cambios
4. Push a la rama
5. Abra un Pull Request

## 📖 Aprendizaje y Extensión
Para desarrolladores que quieran aprender de este código o extenderlo:

### Conceptos Clave
1. **Manejo de Procesos en Linux**
   - Archivos PID
   - Servicios del sistema
   - Privilegios de usuario

2. **Programación Orientada a Objetos en Python**
   - Clases y métodos
   - Encapsulación
   - Manejo de excepciones

3. **Interfaz de Usuario en Terminal**
   - Colorama para decoración
   - Interacción con usuario
   - Mensajes informativos

### Posibles Extensiones
1. Añadir más servicios de XAMPP
2. Implementar logging
3. Crear una interfaz gráfica (GUI)
4. Agregar monitoreo de recursos
5. Implementar backup automático

---
Desarrollado con ❤️ por DevMobyEnd (Jhonny Torres)
