
import DateAndTime # type: ignore
import ipAddress # type: ignore
import RemoteHome # type: ignore
import BackupRemoteFile # type: ignore
import SaveWebpage # type: ignore
from rich.console import Console
from rich.panel import Panel

options = {
    "1": DateAndTime.showDate_Time,
    "2": ipAddress.ip_address,
    "3": RemoteHome.remote_home,
    "4": BackupRemoteFile.backup_remote_file,
    "5": SaveWebpage.save_webpage,
}
def DisplayMenu():
    console = Console()
    console.print(Panel(f"""
[white]=====================================================
[bold red]
 __  __    _    ___ _   _   __  __ _____ _   _ _   _ 
|  \/  |  / \  |_ _| \ | | |  \/  | ____| \ | | | | |
| |\/| | / _ \  | ||  \| | | |\/| |  _| |  \| | | | |
| |  | |/ ___ \ | || |\  | | |  | | |___| |\  | |_| |
|_|  |_/_/   \_\___|_| \_| |_|  |_|_____|_| \_|\___/ 
[/bold red]
[white]=====================================================
[cyan]
1. Display current local date and time
2. Display IP address of local computer
3. Display remote home directory listing
4. Backup remote files
5. Save contents of a webpage to a local file
Q. Quit
[/cyan]
[white]=====================================================
""",title="Welcome To System Utilities", style="bold red", title_align="left"))
