#Here are all the operations of the project

import os
import requests
import paramiko
import posixpath

def backup_remote_file():
    host = "192.168.100.107"
    username = "ubuntu"
    password = "Ss3102341!"
    local_file_path = r"C:\Vscode\Project\test_backup_file.txt"
    remote_dir = "/home/ubuntu"
    remote_file_path = posixpath.join(remote_dir, os.path.basename(local_file_path))

    try:
        # Verify local file exists first
        if not os.path.exists(local_file_path):
            print(f"Error: Local file {local_file_path} not found!")
            return

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password, timeout=10)
        
        sftp = ssh.open_sftp()
        
        # Try to create directory if it doesn't exist
        try:
            sftp.stat(remote_dir)
        except FileNotFoundError:
            print(f"Remote directory {remote_dir} doesn't exist")
            return
            
        sftp.put(local_file_path, remote_file_path)
        sftp.close()
        ssh.close()

        print(f"Backup successful! File uploaded to: {remote_file_path}")

    except Exception as e:
        print(f"Detailed Error: {type(e).__name__}: {e}")

    except Exception as e:
        print("Error:", e)

def save_webpage():
    try:
        
        url = input("\nEnter the full URL of the webpage:\n").strip()
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
    except requests.exceptions.RequestException as e:
        print("Error downloading webpage:", e)
    except Exception as e:
        print("Error saving webpage:", e)