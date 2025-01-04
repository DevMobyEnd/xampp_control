"""
Control de Servicios XAMPP
-------------------------
Un script elegante y eficiente para gestionar servicios XAMPP en Linux.

Desarrollado por: DevMobyEnd (Jhonny Torres)
GitHub: https://github.com/DevMobyEnd
Versión: 2.0

"""
import os
import subprocess
import sys
from pathlib import Path
try:
    from colorama import init, Fore, Back, Style
    init()
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
    from colorama import init, Fore, Back, Style
    init()

class TerminalStyle:
    """Clase para manejar los estilos y decoraciones de la terminal."""
    
    @staticmethod
    def header(text):
        """Formato para encabezados."""
        return f"\n{Fore.CYAN}{Style.BRIGHT}=== {text} ==={Style.RESET_ALL}\n"
    
    @staticmethod
    def success(text):
        """Formato para mensajes de éxito."""
        return f"{Fore.GREEN}✔ {text}{Style.RESET_ALL}"
    
    @staticmethod
    def error(text):
        """Formato para mensajes de error."""
        return f"{Fore.RED}✘ {text}{Style.RESET_ALL}"
    
    @staticmethod
    def info(text):
        """Formato para mensajes informativos."""
        return f"{Fore.YELLOW}ℹ {text}{Style.RESET_ALL}"
    
    @staticmethod
    def prompt(text):
        """Formato para prompts de usuario."""
        return f"{Fore.MAGENTA}? {text}{Style.RESET_ALL}"

class XAMPPController:
    def __init__(self):
        """Inicializa el controlador de XAMPP con la configuración base."""
        self.xampp_path = "/opt/lampp"
        self.pid_files = {
            'apache': f"{self.xampp_path}/logs/httpd.pid",
            'proftpd': f"{self.xampp_path}/var/proftpd.pid"
        }
        self.style = TerminalStyle()
    
    def check_root(self):
        """Verifica si el script se está ejecutando con privilegios de root."""
        if os.geteuid() != 0:
            print(self.style.error("Este script necesita privilegios de root."))
            print(self.style.info("Por favor, ejecuta con: sudo python3 xampp_control.py"))
            sys.exit(1)
    
    def service_is_running(self, service):
        """
        Verifica si un servicio está en ejecución.
        
        Args:
            service (str): Nombre del servicio ('apache' o 'proftpd')
            
        Returns:
            bool: True si el servicio está ejecutándose
        """
        pid_file = self.pid_files.get(service)
        if pid_file and Path(pid_file).exists():
            return True
        return False
    
    def execute_command(self, command):
        """
        Ejecuta un comando del sistema de manera segura.
        
        Args:
            command (list): Comando a ejecutar en formato lista
            
        Returns:
            bool: True si el comando se ejecutó correctamente
        """
        try:
            subprocess.run(command, check=True, capture_output=True, text=True)
            return True
        except subprocess.CalledProcessError as e:
            print(self.style.error(f"Error ejecutando: {' '.join(command)}"))
            print(self.style.error(f"Código de error: {e.returncode}"))
            return False

    def select_mysql_type(self):
        """Permite al usuario seleccionar qué versión de MySQL utilizar."""
        print(self.style.header("Selección de MySQL"))
        print(self.style.info("1) MySQL de XAMPP"))
        print(self.style.info("2) MySQL del Sistema"))
        
        while True:
            choice = input(self.style.prompt("Seleccione una opción (1/2): "))
            if choice in ['1', '2']:
                return choice
            print(self.style.error("Opción inválida. Por favor, seleccione 1 o 2."))

    def toggle_services(self):
        """Gestiona la activación/desactivación de servicios con interfaz mejorada."""
        print(self.style.header("Control de Servicios XAMPP"))
        
        # Determinar estado actual
        apache_running = self.service_is_running('apache')
        proftpd_running = self.service_is_running('proftpd')
        
        # Mostrar estado actual
        print(self.style.info(f"Apache: {'Activo' if apache_running else 'Inactivo'}"))
        print(self.style.info(f"ProFTPD: {'Activo' if proftpd_running else 'Inactivo'}"))
        
        if apache_running or proftpd_running:
            print(self.style.header("Desactivando Servicios"))
            self.execute_command([f"{self.xampp_path}/lampp", "stopapache"])
            self.execute_command([f"{self.xampp_path}/lampp", "stopftp"])
            print(self.style.success("Servicios web desactivados exitosamente."))
            
            # Detener MySQL si está en uso
            print(self.style.info("Deteniendo servicio MySQL..."))
            self.execute_command(["sudo", "systemctl", "stop", "mysql"])
            print(self.style.success("MySQL detenido exitosamente."))
        else:
            print(self.style.header("Activando Servicios"))
            self.execute_command([f"{self.xampp_path}/lampp", "startapache"])
            self.execute_command([f"{self.xampp_path}/lampp", "startftp"])
            print(self.style.success("Servicios web activados exitosamente."))
            
            # Seleccionar y activar MySQL
            mysql_choice = self.select_mysql_type()
            if mysql_choice == '1':
                print(self.style.info("Iniciando MySQL de XAMPP..."))
                self.execute_command([f"{self.xampp_path}/lampp", "startmysql"])
            else:
                print(self.style.info("Iniciando MySQL del Sistema..."))
                self.execute_command(["sudo", "systemctl", "start", "mysql"])
            print(self.style.success("MySQL iniciado exitosamente."))

def main():
    """Función principal que inicializa y ejecuta el controlador."""
    try:
        controller = XAMPPController()
        controller.check_root()
        controller.toggle_services()
    except KeyboardInterrupt:
        print(TerminalStyle.info("\nOperación cancelada por el usuario."))
        sys.exit(0)
    except Exception as e:
        print(TerminalStyle.error(f"Error inesperado: {str(e)}"))
        sys.exit(1)

if __name__ == "__main__":
    main()