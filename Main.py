import Menu
from rich.console import Console

def main():
    console = Console()
    while True:
        Menu.DisplayMenu()
        choice = input("Select an option: \n").strip().upper()
        if choice == "Q":
            console.print("Exiting System Utilities", style="red")
            console.print("Goodbye👋", style="bold green")
            break
        elif choice in Menu.options:
            try:
                Menu.options[choice]()
            except:
                print("An error occured.")
        else:
            print("Invalid choice, please try again.")
if __name__=="__main__":

    main()
