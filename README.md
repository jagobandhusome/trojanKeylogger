\# Windows System Manipulation and Keylogger Scripts



This repository contains two Python scripts, \*\*Cockroach.py\*\* and \*\*Trojan.py\*\*, which are designed for system manipulation, information logging, and keylogging on Windows systems. These scripts are intended for educational and research purposes only. They showcase the potential risks associated with security vulnerabilities, specifically focusing on system access, data exfiltration, and remote control functionalities.



\*\*Important Note\*\*: These scripts are \*\*malicious\*\* in nature and should not be used on any unauthorized machines. Always ensure you have explicit permission before running any penetration testing or security research scripts.



\## Features



\### \*\*Cockroach.py\*\*:

\- \*\*User Information Logging\*\*: Collects system details (username, IP addresses, public IP, and logs the timestamp).

\- \*\*Admin Privileges\*\*: Checks if the script is running as an administrator and re-launches with admin privileges if needed.

\- \*\*Remote Desktop Protocol (RDP) Enabler\*\*: Enables RDP on the target machine.

\- \*\*Backdoor Creation\*\*: Creates a user with administrative privileges for unauthorized access.

\- \*\*Keylogger\*\*: Records keystrokes and logs them for exfiltration.

\- \*\*Log Upload via SFTP\*\*: Uploads the collected logs to a remote server via SFTP.

\- \*\*Email Exfiltration\*\*: Sends the collected logs via email to a designated address.

\- \*\*Removable Drive Infection\*\*: Infects removable drives connected to the system with malicious files.



\### \*\*Trojan.py\*\*:

\- \*\*User Time Logging\*\*: Tracks user activity and logs timestamps.

\- \*\*Keylogger\*\*: Captures and logs keystrokes.

\- \*\*Removable Drive Infection\*\*: Infects connected removable drives with a copy of the script.

\- \*\*SMTP Data Exfiltration\*\*: Sends the captured log files via SMTP email to a predefined address.



\## Requirements



Before running these scripts, make sure you have the following dependencies installed:



\- `win32api` - Access Windows API functions.

\- `win32con` - Constants for interacting with the Windows environment.

\- `win32file` - Provides functions for file operations.

\- `paramiko` - Used for SFTP file transfer.

\- `smtplib` - Python's built-in module for sending emails.

\- `uuid` - For generating unique identifiers.

\- `time`, `os`, `socket`, `ctypes`, `subprocess`, `winreg` - Standard Python libraries for system and network operations.



You can install missing libraries using the following command:

```bash

pip install pywin32 paramiko


Usage

Run as Administrator: Ensure that the script has administrator privileges to perform certain actions, such as enabling RDP or creating backdoor users.

Configure Email and Remote Host: Update the email credentials and remote server details in the script to match your configuration.

Run the Script: Execute the script using Python.

python Cockroach.py


Monitor Logs: The script will generate log files that are uploaded to a remote server via SFTP or sent via email.

Ethical Usage

These scripts are for educational and research purposes only. They should not be deployed on any systems without explicit permission. Unauthorized use of these scripts on machines you do not own is illegal and unethical.

If you're interested in learning about cybersecurity, consider setting up a controlled environment such as a virtual machine for safe experimentation.

License

This repository is not licensed and is intended strictly for educational purposes. Use it at your own risk.

Disclaimer

By using these scripts, you agree that the author is not responsible for any damage, loss of data, or legal consequences arising from the use of these scripts. Use these scripts responsibly and ethically.


### GitHub Description:

**Project Name**: Windows System Manipulation and Keylogger Scripts

**Description**:  
This project contains two Python scripts (**Cockroach.py** and **Trojan.py**) that perform system manipulation tasks, such as enabling remote access, creating backdoor users, logging keystrokes, and infecting removable drives. The scripts also include functionality to upload logs via SFTP and send them via email. They are intended for **educational purposes** and should only be used in controlled environments with explicit consent.

---

Let me know if you need further adjustments or additions!
