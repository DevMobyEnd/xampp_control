# XAMPP Control Script - Documentación
[![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Tabla de Contenidos
1. [Descripción](#descripción)
2. [Características](#características)
3. [Requisitos](#requisitos)
4. [Instalación](#instalación)
5. [Uso](#uso)
6. [Estructura del Código](#estructura-del-código)
7. [Solución de Problemas](#solución-de-problemas)
8. [Contribuir](#contribuir)
9. [Aprendizaje y Desarrollo](#aprendizaje-y-desarrollo)

## 📝 Descripción
Este script proporciona una interfaz de línea de comandos elegante y eficiente para controlar los servicios de XAMPP en sistemas Linux. Permite gestionar Apache, MySQL y ProFTPD de manera sencilla con una interfaz visual mejorada.

## ✨ Características
- Interfaz de línea de comandos con diseño ASCII art
- Gestión de servicios Apache, MySQL y ProFTPD
- Soporte para MySQL del sistema y MySQL de XAMPP
- Interfaz colorida y amigable usando Colorama
- Mensajes de estado claros y detallados
- Manejo de errores robusto
- Verificación de privilegios de root

## 📋 Requisitos
- Python 3.6 o superior
- XAMPP instalado en `/opt/lampp`
- Privilegios de root
- Sistema operativo Linux

### Dependencias de Python
```bash
pip install colorama
```

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/xampp-control.git
cd xampp-control
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Da permisos de ejecución:
```bash
chmod +x xampp_control.py
```

## 💻 Uso

### Comandos Básicos

1. Ejecutar el script:
```bash
sudo python3 xampp_control.py
```

2. Detener el script:
- Presiona `Ctrl + C` en cualquier momento

### Opciones de MySQL
- `0`: Usar MySQL de XAMPP
- `1`: Usar MySQL del sistema

## 🔍 Estructura del Código

### Clases Principales

#### `TerminalStyle`
Maneja los estilos y decoraciones de la terminal:
- `header()`: Formato para encabezados
- `success()`: Mensajes de éxito
- `error()`: Mensajes de error
- `info()`: Mensajes informativos
- `prompt()`: Prompts de usuario

#### `XAMPPController`
Controlador principal de servicios:
- `service_is_running()`: Verifica el estado de servicios
- `check_root()`: Verifica privilegios de root
- `execute_command()`: Ejecuta comandos del sistema
- `toggle_services()`: Gestiona servicios
- `select_mysql_type()`: Selección de versión MySQL

### Funciones Auxiliares

#### `print_banner()`
Muestra el banner ASCII art de XAMPP al inicio del programa.

#### `main()`
Función principal que inicializa y ejecuta el controlador.

## ❗ Solución de Problemas

### Error: "Permission denied"
**Problema**: No tienes permisos de root
**Solución**: Ejecuta el script con sudo
```bash
sudo python3 xampp_control.py
```

### Error: "MySQL service not found"
**Problema**: MySQL no está instalado en el sistema
**Solución**: Instala MySQL o usa la versión de XAMPP
```bash
sudo apt-get install mysql-server
```

### Error: "XAMPP not found in /opt/lampp"
**Problema**: XAMPP no está instalado o la ruta es incorrecta
**Solución**: 
1. Verifica la instalación de XAMPP
2. Modifica la variable `xampp_path` en el código si tu instalación está en otra ubicación

### Error: "Command not found"
**Problema**: Falta alguna dependencia del sistema
**Solución**: Instala las dependencias necesarias
```bash
sudo apt-get update
sudo apt-get install python3-pip
pip3 install colorama
```

## 🤝 Contribuir

¿Quieres contribuir al proyecto? ¡Excelente! Aquí hay algunas formas de hacerlo:

1. Reporta bugs o sugiere mejoras creando un issue
2. Mejora la documentación
3. Añade nuevas características
4. Optimiza el código existente

### Guía de Contribución
1. Haz fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📚 Aprendizaje y Desarrollo

### Conceptos Clave para Aprender
1. **Programación Orientada a Objetos en Python**
   - Clases y objetos
   - Herencia y encapsulación
   - Métodos estáticos y de clase

2. **Manejo de Procesos en Linux**
   - Comandos del sistema
   - Gestión de servicios
   - Permisos y privilegios

3. **Interfaz de Usuario en Terminal**
   - ANSI color codes
   - ASCII art
   - Diseño de interfaces TUI

### Áreas de Mejora Potencial
1. **Funcionalidad**
   - Añadir soporte para más servicios
   - Implementar logging
   - Añadir configuración personalizable
   - Crear backup automático de configuraciones

2. **Interfaz**
   - Implementar menú interactivo con ncurses
   - Añadir más opciones de personalización visual
   - Mejorar la accesibilidad

3. **Código**
   - Implementar tests unitarios
   - Mejorar el manejo de errores
   - Optimizar el rendimiento
   - Añadir documentación tipo docstring

### Recursos de Aprendizaje
- [Python Official Documentation](https://docs.python.org/)
- [Linux Service Management](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)
- [Terminal User Interfaces with Python](https://python.plainenglish.io/build-a-terminal-user-interface-using-python-93342a9e0adb)

## 📜 Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor
Desarrollado por [DevMobyEnd (Jhonny Torres)](https://github.com/DevMobyEnd)

---
¿Encontraste útil esta documentación? ¡Dale una ⭐ al repositorio!
