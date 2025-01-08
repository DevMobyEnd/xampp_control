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

def print_banner():
    banner = """
    ██╗  ██╗ █████╗ ███╗   ███╗██████╗ ██████╗ 
    ╚██╗██╔╝██╔══██╗████╗ ████║██╔══██╗██╔══██╗
     ╚███╔╝ ███████║██╔████╔██║██████╔╝██████╔╝
     ██╔██╗ ██╔══██║██║╚██╔╝██║██╔═══╝ ██╔═══╝ 
    ██╔╝ ██╗██║  ██║██║ ╚═╝ ██║██║     ██║     
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝     
    =============================================
         Control Panel - Versión Terminal
    =============================================
    """
    print(f"{Fore.CYAN}{banner}{Style.RESET_ALL}")

class TerminalStyle:
    """Clase para manejar los estilos y decoraciones de la terminal."""
    
    @staticmethod
    def header(text):
        """Formato para encabezados."""
        return f"\n{Fore.CYAN}{Style.BRIGHT}╔{'═' * (len(text) + 4)}╗\n║  {text}  ║\n╚{'═' * (len(text) + 4)}╝{Style.RESET_ALL}\n"
    
    @staticmethod
    def success(text):
        """Formato para mensajes de éxito."""
        return f"{Fore.GREEN}[✔] {text}{Style.RESET_ALL}"
    
    @staticmethod
    def error(text):
        """Formato para mensajes de error."""
        return f"{Fore.RED}[✘] {text}{Style.RESET_ALL}"
    
    @staticmethod
    def info(text):
        """Formato para mensajes informativos."""
        return f"{Fore.YELLOW}[ℹ] {text}{Style.RESET_ALL}"
    
    @staticmethod
    def prompt(text):
        """Formato para prompts de usuario."""
        return f"{Fore.MAGENTA}[?] {text}{Style.RESET_ALL}"

class XAMPPController:
    def __init__(self):
        """Inicializa el controlador de XAMPP con la configuración base."""
        self.xampp_path = "/opt/lampp"
        self.pid_files = {
            'apache': f"{self.xampp_path}/logs/httpd.pid",
            'proftpd': f"{self.xampp_path}/var/proftpd.pid"
        }
        self.style = TerminalStyle()
    
    def service_is_running(self, service):
        """
        Verifica si un servicio está en ejecución usando ps.
        """
        try:
            if service == 'apache':
                result = subprocess.run(['pgrep', 'httpd'], capture_output=True, text=True)
            elif service == 'proftpd':
                result = subprocess.run(['pgrep', 'proftpd'], capture_output=True, text=True)
            return result.returncode == 0
        except Exception:
            return False
        
    def check_root(self):
        """Verifica si el script se está ejecutando con privilegios de root."""
        if os.geteuid() != 0:
            print(self.style.error("Este script necesita privilegios de root."))
            print(self.style.info("Por favor, ejecuta con: sudo python3 xampp_control.py"))
            sys.exit(1)
    
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
        print(f"{Fore.CYAN}┌{'─' * 30}┐{Style.RESET_ALL}")
        print(f"{Fore.CYAN}│{Style.RESET_ALL} {self.style.info('0) MySQL de XAMPP')}")
        print(f"{Fore.CYAN}│{Style.RESET_ALL} {self.style.info('1) MySQL del Sistema')}")
        print(f"{Fore.CYAN}└{'─' * 30}┘{Style.RESET_ALL}")
        
        while True:
            choice = input(self.style.prompt("Seleccione una opción (0/1): "))
            if choice in ['0', '1']:
                return choice
            print(self.style.error("Opción inválida. Por favor, seleccione 0 o 1."))

    def toggle_services(self):
        """Gestiona la activación/desactivación de servicios con interfaz mejorada."""
        print(self.style.header("Control de Servicios XAMPP"))
        
        apache_running = self.service_is_running('apache')
        proftpd_running = self.service_is_running('proftpd')
        
        print(f"{Fore.CYAN}┌{'─' * 40}┐{Style.RESET_ALL}")
        print(f"{Fore.CYAN}│{Style.RESET_ALL} Apache:   {self.style.success('Activo') if apache_running else self.style.error('Inactivo')}")
        print(f"{Fore.CYAN}│{Style.RESET_ALL} ProFTPD:  {self.style.success('Activo') if proftpd_running else self.style.error('Inactivo')}")
        print(f"{Fore.CYAN}└{'─' * 40}┘{Style.RESET_ALL}")
        
        if apache_running or proftpd_running:
            print(self.style.header("Desactivando Servicios"))
            
            if apache_running:
                if self.execute_command([f"{self.xampp_path}/xampp", "stopapache"]):
                    print(self.style.success("Apache detenido correctamente"))
            if proftpd_running:
                if self.execute_command([f"{self.xampp_path}/xampp", "stopftp"]):
                    print(self.style.success("ProFTPD detenido correctamente"))
                
            try:
                result = subprocess.run(["systemctl", "is-active", "mysql"], capture_output=True, text=True)
                if result.stdout.strip() == "active":
                    print(self.style.info("Deteniendo MySQL del sistema..."))
                    if self.execute_command(["systemctl", "stop", "mysql"]):
                        print(self.style.success("MySQL del sistema detenido correctamente"))
            except Exception as e:
                print(self.style.error(f"Error al verificar MySQL: {str(e)}"))
                
        else:
            print(self.style.header("Activando Servicios"))
            
            if self.execute_command([f"{self.xampp_path}/xampp", "startapache"]):
                print(self.style.success("Apache iniciado correctamente"))
            if self.execute_command([f"{self.xampp_path}/xampp", "startftp"]):
                print(self.style.success("ProFTPD iniciado correctamente"))
            
            mysql_choice = self.select_mysql_type()
            if mysql_choice == '0':
                print(self.style.info("Iniciando MySQL de XAMPP..."))
                if self.execute_command([f"{self.xampp_path}/xampp", "startmysql"]):
                    print(self.style.success("MySQL de XAMPP iniciado correctamente"))
                else:
                    print(self.style.error("Error al iniciar MySQL de XAMPP"))
            else:
                print(self.style.info("Iniciando MySQL del Sistema..."))
                try:
                    check_service = subprocess.run(["systemctl", "list-unit-files", "mysql.service"], 
                                                capture_output=True, text=True)
                    if "mysql.service" not in check_service.stdout:
                        print(self.style.error("El servicio MySQL no está instalado en el sistema"))
                        return
                        
                    if self.execute_command(["systemctl", "start", "mysql"]):
                        print(self.style.success("MySQL del sistema iniciado correctamente"))
                    else:
                        print(self.style.error("Error al iniciar MySQL del sistema"))
                        print(self.style.info("Verifique que MySQL está instalado correctamente"))
                except Exception as e:
                    print(self.style.error(f"Error al iniciar MySQL: {str(e)}"))

def main():
    """Función principal que inicializa y ejecuta el controlador."""
    try:
        os.system('clear')  # Limpia la pantalla
        print_banner()  # Muestra el banner al inicio
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