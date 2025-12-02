
import requests
def save_webpage():
    try:
        url = input("Enter the full URL of the webpage:\n").strip()
        if not url:
            print("No URL entered.")
            return
        
        response = requests.get(url)
        userFilename = input("What do you want this file to be named as?\n")
        userExtension = input("What file extension do you want to use? (Example: .txt,.html...etc)\n").strip()
        while True:
            filename = userFilename + userExtension
            if ("." in filename):
                with open(filename, "w",) as f:
                    f.write(response.text)
                print(f"Webpage has been backed up within this project's directory as: {filename}")
                break
            else:
                print(f"ERROR: Incorrect file extension - must start with '.' ")
                userExtension = input("Enter a valid file extension or Q to quit\n").upper().strip()
                if userExtension == "Q":
                    break
    except requests.exceptions as e:
        print("Error downloading webpage:", e)
    except Exception as e:
        print("Error saving webpage:", e)
