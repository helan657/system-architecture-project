import paramiko

def remote_home():
    ssh_client = paramiko.SSHClient()
    
    try:
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(
            hostname="192.168.100.107",      
            username="ubuntu",      
            password="Ss310234!",      
            port=22
        )
    except Exception as e:
        print("**ERROR**: There was an error while trying to establish a connection to the remote host")
        print(f"**ERROR Information**: {e}")
        return
    
    try:
        stdin, stdout, stderr = ssh_client.exec_command("ls -l /home/")
        command_output = stdout.read().decode('utf-8')
        error_output = stderr.read().decode('utf-8')
        if error_output:
            print(f"**WARNING**: {error_output}")
        print(command_output)
    except Exception as e:
        print(f"There was an error while trying to execute the command. Ensure that you are connecting to a linux-based OS")
        print(f"Error: {e}")
    finally:
        ssh_client.close()