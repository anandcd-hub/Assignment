import os
import datetime
import socket
import paramiko
import requests

remote_ip = "192.168.0.19"  # Replace with the actual IP
username = "anandcd"  # Replace with the actual username
password = "Padayappa@1"  # Replace with the actual password

def show_date_and_time():
    now = datetime.datetime.now() # Using the datatime module to fetch current date and time
    print(f"Local Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}") # Printing the local date and time


def show_ip_address():
    hostname = socket.gethostname() 
    ip_address = socket.gethostbyname(hostname)
    print(f"Local IP Address: {ip_address}") #printing the ip address


def backup_remote_file():

    remote_file_path = input("Enter the full path of the remote file to back up: ") #enter the backup file

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(remote_ip, username=username, password=password)
        backup_path = remote_file_path + ".old"
        stdin, stdout, stderr = ssh.exec_command(f"cp {remote_file_path} {backup_path}")
        print("Backup Finished!") #here backup will complete
        print(stdout.read().decode())
        ssh.close()

    except Exception as e:
        print(f"Error: {e}") #if any error occurs


def show_remote_home_directory():


    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(remote_ip, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command("ls ~")
        print("Home Directory Listing:") #printing home directory listing file
        print(stdout.read().decode())
        ssh.close()
    except Exception as e:
        print(f"Error: {e}") #if any error occurs


def save_web_page():
    url = input("Enter the full URL of the web page: ") #entering the full url of webpage 
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_name = url.replace("https://", "").replace("http://", "").split("/")[0] + ".html"
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"Web page saved as {file_name}") #saving webpage file name
        else:
            print(f"Failed to fetch the web page. Status code: {response.status_code}") #if webpage doesnt found
    except Exception as e:
        print(f"Error: {e}") #if any error occurs

def main():
    while True:
        print("\nMenu:") #here is the option which allows you to select whatever u want
        print("1- Show date and time (local computer)")
        print("2- Show IP address (local computer)")
        print("3- Show Remote home directory listing")
        print("4- Backup remote file")
        print("5- Save web page")
        print("Q- Quit")

        choice = input("Enter your choice: ").strip().upper() #below shows the choice and options of the menu

        if choice == "1":
            show_date_and_time()
        elif choice == "2":
            show_ip_address()
        elif choice == "3":
            show_remote_home_directory()
        elif choice == "4":
            backup_remote_file()
        elif choice == "5":
            save_web_page()
        elif choice == "Q":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()


