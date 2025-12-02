import datetime
from rich.console import Console
from rich.text import Text
from rich.panel import Panel


def showDate_Time():
    try:
        console = Console()
        current = datetime.datetime.now()
        text = Text()
        text.append(f"Date: {current.strftime('%Y-%m-%d')}\n", style="cyan")
        text.append(f"Time: {current.strftime('%H:%M:%S')}\n", style="cyan")
        text.append(f"Day:  {current.strftime('%A')}", style="cyan")
        
        panel= Panel(
            text,
            title="Current Date, Time and Day",
            title_align="left",
            style= "bold red"
        )
        
        console.print(panel)
    except Exception as e:
        console.print(f"[red]Error getting date and time: {e}[/red]")