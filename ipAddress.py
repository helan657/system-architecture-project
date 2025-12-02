import socket
from rich.console import Console
from rich.panel import Panel

def get_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))
                return s.getsockname()[0]
        except:
            return "Unable to determine IP address"

def ip_address():
    console = Console()
    try:
        ip = get_local_ip()
        console.print(Panel(f"🌐 Local IP Address: [bold cyan]{ip}[/bold cyan]",title="Network Information", style=" bold red",title_align="left"))
    
    except Exception as e:
        console.print(f"[red]Error getting IP address: {e}[/red]")