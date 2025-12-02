import paramiko

def backup_remote_file():
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        ssh_client.connect(
            hostname="192.168.100.107",
            username="ubuntu", 
            password="Ss310234!",
            port=22
        )       
    except Exception as e:
        print("Error: There was an error while trying to establish a connection to the remote host")
        print(f"Error: {e}")
        quit()

    while True:
        try:
            user_path = input("Please specify the full path for the file that needs to be backed up: ")
            if user_path[0] != '/':
                print("There needs to be a '/'.")
                continue

            stdin, stdout, stderr = ssh_client.exec_command(f"test -d {user_path} && echo 'directory' || echo 'file'")
            path_type = stdout.read().decode().strip()
            if path_type == 'directory':
                cmd = f"cp -r {user_path} {user_path}.old"
            else:
                cmd = f"cp {user_path} {user_path}.old"

            stdin, stdout, stderr = ssh_client.exec_command(cmd)
            exit_status = stdout.channel.recv_exit_status()
            error_msg = stderr.read().decode()
            
            if exit_status != 0:
                raise Exception(f"Command failed with exit status {exit_status}: {error_msg}")
            path_parts = user_path.split("/")
            filename = path_parts[-1]
            has_error = False
            show_result(filename, user_path, has_error,)
        except Exception as e:
            has_error = True
            show_result(has_error, {e})
    ssh_client.close()

def show_result(filename, file_path, error_occurred, exception):
    if error_occurred:
        message = f"Unsuccessful! Please Retry."
        if exception is not None:
            print(f"Error: {exception}")
    else:
        message = f"Success! You created a backup of {filename} in the {file_path} directory called {filename}.old\n"
    print(message)